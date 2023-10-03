# client.py

import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    request = calculator_pb2.AddRequest(num1=5, num2=3)
    response = stub.Add(request)
    print(f"Addition result: {response.result}")

if __name__ == '__main__':
    run()
