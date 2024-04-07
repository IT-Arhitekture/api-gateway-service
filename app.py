from flask import Flask, request
import requests
import json
import grpc
import reservation_pb2
import reservation_pb2_grpc

app = Flask(__name__)


class ServiceNotRunningError(Exception):
    def __init__(self, message="Service is not running"):
        self.message = message
        super().__init__(self.message)


@app.route('/mobile/restaurant-management-service/restaurants', methods=['GET'])
def mobile_get_all_restaurants():
    try:
        response = requests.get('http://localhost:8080/restaurants')
        response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/mobile/restaurant-management-service/restaurants/<id>', methods=['GET'])
def mobile_get_restaurant_by_id(id):
    try:
        response = requests.get(f'http://localhost:8080/restaurants/{id}')
        response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/web/restaurant-management-service/restaurants', methods=['GET', 'POST', 'DELETE'])
def web_restaurants():
    try:
        if request.method == 'GET':
            response = requests.get('http://localhost:8080/restaurants')
            response.raise_for_status()
        elif request.method == 'POST':
            response = requests.post('http://localhost:8080/restaurants', data=json.dumps(request.get_json()),
                                     headers={'Content-Type': 'application/json'})
            response.raise_for_status()
        elif request.method == 'DELETE':
            id = request.args.get('id')
            if id:
                response = requests.delete(f'http://localhost:8080/restaurants/{id}')
                response.raise_for_status()
            else:
                return "Missing id parameter", 400
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/web/restaurant-management-service/restaurants/<id>', methods=['GET', 'DELETE'])
def web_restaurants_id(id):
    try:
        if request.method == 'GET':
            response = requests.get(f'http://localhost:8080/restaurants/{id}')
            response.raise_for_status()
        elif request.method == 'DELETE':
            response = requests.delete(f'http://localhost:8080/restaurants/{id}')
            response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/mobile/table-reservation-service/reservations', methods=['GET'])
def mobile_get_all_table_reservations():
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = reservation_pb2_grpc.ReservationGrpcStub(channel)
        response = stub.getReservations(reservation_pb2.EmptyRequest())
    except grpc.RpcError:
        raise ServiceNotRunningError()
    return json.dumps(response)


@app.route('/mobile/table-reservation-service/reservations/<id>', methods=['GET'])
def mobile_get_table_reservation_by_restaurant_id(id):
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = reservation_pb2_grpc.ReservationGrpcStub(channel)
        response = stub.getReservationByRestaurantId(reservation_pb2.RestaurantIdRequest(restaurantId=id))
    except grpc.RpcError:
        raise ServiceNotRunningError()
    return json.dumps(response)


@app.route('/web/table-reservation-service/reservations', methods=['GET', 'POST', 'DELETE'])
def web_table_reservations():
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = reservation_pb2_grpc.ReservationGrpcStub(channel)

        if request.method == 'GET':
            response = stub.getReservations(reservation_pb2.EmptyRequest())
        elif request.method == 'POST':
            data = request.get_json()
            response = stub.createReservation(reservation_pb2.CreateReservationRequest(
                restaurantId=data.get('restaurantId'),
                customerId=data.get('customerId'),
                date=data.get('date')
            ))
        elif request.method == 'DELETE':
            data = request.get_json()
            response = stub.deleteReservation(reservation_pb2.DeleteReservationRequest(
                reservationId=data.get('reservationId')
            ))
        else:
            return "Invalid method", 400
    except grpc.RpcError:
        raise ServiceNotRunningError()
    return json.dumps(response)


@app.route('/web/table-reservation-service/reservations/<id>', methods=['GET', 'DELETE'])
def web_table_reservations_id(id):
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = reservation_pb2_grpc.ReservationGrpcStub(channel)

        if request.method == 'GET':
            response = stub.getReservationByRestaurantId(reservation_pb2.RestaurantIdRequest(restaurantId=id))
        elif request.method == 'DELETE':
            response = stub.deleteReservation(reservation_pb2.DeleteReservationRequest(reservationId=id))
        else:
            return "Invalid method", 400
    except grpc.RpcError:
        raise ServiceNotRunningError()
    return json.dumps(response)


@app.route('/mobile/user-service/users', methods=['GET'])
def mobile_get_all_users():
    try:
        response = requests.get('http://localhost:8081/users')
        response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/mobile/user-service/users/get-user', methods=['POST'])
def mobile_get_user():
    try:
        response = requests.post('http://localhost:8081/users/get-user', data=request.get_json(),
                                 headers={'Content-Type': 'application/json'})
        response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/web/user-service/users', methods=['GET', 'POST'])
def web_users():
    try:
        if request.method == 'GET':
            response = requests.get('http://localhost:8081/users')
            response.raise_for_status()
        elif request.method == 'POST':
            response = requests.post('http://localhost:8081/users', data=request.get_json(),
                                     headers={'Content-Type': 'application/json'})
            response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/web/user-service/users/<id>', methods=['PUT', 'DELETE'])
def web_users_id(id):
    try:
        if request.method == 'PUT':
            response = requests.put(f'http://localhost:8081/users/{id}', data=request.get_json(),
                                    headers={'Content-Type': 'application/json'})
            response.raise_for_status()
        elif request.method == 'DELETE':
            response = requests.delete(f'http://localhost:8081/users/{id}')
            response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content


@app.route('/web/user-service/users/get-user', methods=['POST'])
def web_get_user():
    try:
        response = requests.post('http://localhost:8081/users/get-user', data=request.get_json(),
                                 headers={'Content-Type': 'application/json'})
        response.raise_for_status()
    except (requests.ConnectionError, requests.HTTPError):
        raise ServiceNotRunningError()
    return response.content

@app.route('/', methods=['GET'])
def index():
    links = {
        "mobile_get_all_restaurants": "/mobile/restaurant-management-service/restaurants",
        "mobile_get_restaurant_by_id": "/mobile/restaurant-management-service/restaurants/{id}",
        "web_restaurants": "/web/restaurant-management-service/restaurants",
        "web_restaurants_id": "/web/restaurant-management-service/restaurants/{id}",
        "mobile_get_all_table_reservations": "/mobile/table-reservation-service/reservations",
        "mobile_get_table_reservation_by_restaurant_id": "/mobile/table-reservation-service/reservations/{id}",
        "web_table_reservations": "/web/table-reservation-service/reservations",
        "web_table_reservations_id": "/web/table-reservation-service/reservations/{id}",
        "mobile_get_all_users": "/mobile/user-service/users",
        "mobile_get_user": "/mobile/user-service/users/get-user",
        "web_users": "/web/user-service/users",
        "web_users_id": "/web/user-service/users/{id}",
        "web_get_user": "/web/user-service/users/get-user"
    }

    html = "<h1>API Endpoints</h1>"
    for name, path in links.items():
        html += f'<p><a href="{path}">{name}</a></p>'
    return html


if __name__ == '__main__':
    app.run(port=5000)
