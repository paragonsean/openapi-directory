# C++ Qt API client

# 

Fire Financial Services Business API

- API version: 1.0
- Generator version: 7.9.0

The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.

The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.


The API exposes 3 main areas of functionality: financial functions, service information and service configuration.
## Financial Functions
These functions provide access to your account details, transactions, payee accounts, payment initiation etc.
## Service Functions
These provide information about the fees and limits applied to your account.
## Service configuration
These provide information about your service configs - applications, webhooks, API tokens, etc.


  For more information, please visit [https://docs.fire.com](https://docs.fire.com)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:

1. CMake 3.2+
2. Qt
3. C++ Compiler

## Getting Started

example.h:
```c++

#include <iostream>
#include "../client/OAIAPIApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    OAINewApiApplication create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIAPIApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

OAINewApiApplication Example::create(){
    OAINewApiApplication obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIAPIApi apiInstance;
     
      // Configure HTTP bearer authorization: bearerAuth
      apiInstance.setBearerToken("BEARER TOKEN");

      QEventLoop loop;
      connect(&apiInstance, &OAIAPIApi::createApiApplicationSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAPIApi::createApiApplicationSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAINewApiApplication oai_new_api_application = create(); // OAINewApiApplication | Details of the new API Application
      apiInstance.createApiApplication(oai_new_api_application);
      QTimer::singleShot(5000, &loop, &QEventLoop::quit);
      loop.exec();
  }

```

## Documentation for Servers

Parameterized Servers are supported. Define a server in the API for each endpoint with arbitrary numbers of variables:

```yaml
servers:
- url: http://{server}:{port}/{basePath}
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
    port:
      enum:
        - '3000'
        - '1000'
      default: '3000'
    basePath:
      default: v1
```
To change the default variable, use this function in each Api:
```c++
int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
```
The parameter "serverIndex" will choose a server from the server list for each endpoint. There is always at least one server with index 0. The Parameter "operation" should be the desired endpoint operationid.
Variable is the name of the variable you wish to change and the value is the new default Value.
The function will return -1 when the variable does not exists, -2 if value is not defined in the variable enum and -3 if the operation is not found.

If your endpoint has multiple server objects in the servers array, you can set the server that will be used with this function:
```c++
void setServerIndex(const QString &operation, int serverIndex);
```
Parameter "operation" should be your operationid. "serverIndex" is the index you want to set as your default server. The function will check if there is a server with your index.
Here is an example of multiple servers in the servers array. The first server will have index 0 and the second will have index 1.
```yaml
servers:
- url: http://{server}:8080/
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
- url: https://localhost:8080/v1
```

## Documentation for Authorization

Authentication schemes defined for the API:
### bearerAuth


- **Type**: HTTP Bearer Token authentication (API Access Token)


## Author

api@fire.com


## License

 for more information visit []()