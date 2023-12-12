from zeep import Client

cliente = Client(wsdl=r'C:\Users\revaz\PycharmProjects\soapAPI\index.xml')
print(cliente.service.Add(11,5))
print(cliente.service.Subtract(10,5))
print(cliente.service.Multiply(10,5))
print(cliente.service.Divide(10,5))