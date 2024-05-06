import sys
sys.path.append('./')

import grpc
import calculadora_pb2 as pb2
import calculadora_pb2_grpc as pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.CalculadoraServiceStub(channel)

    n1 = 10
    n2 = 5

    request = pb2.OperacionRequest(n1=n1, n2 = n2)

    rsum = stub.suma(request)
    rrest = stub.resta(request)
    rmult = stub.mult(request)
    rdiv = stub.div(request)

    print(f"{n1} + {n2} = {rsum}")
    print(f"{n1} - {n2} = {rrest}")
    print(f"{n1} * {n2} = {rmult}")
    print(f"{n1} / {n2} = {rdiv}")

    print("fin del cliente...")
    channel.close()

if __name__ == '__main__':
    main()