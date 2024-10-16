# C++ Qt API client

# 

Chain49 API

- API version: 2.0
- Generator version: 7.9.0

Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner

Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)

  For more information, please visit [https://chain49.com/](https://chain49.com/)

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
#include "../client/OAIAddressesApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    QString create();
    qint32 create();
    qint32 create();
    qint32 create();
    qint32 create();
    QString create();
    QString create();
    QString create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIAddressesApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
qint32 Example::create(){
    qint32 obj;
qint32 Example::create(){
    qint32 obj;
qint32 Example::create(){
    qint32 obj;
qint32 Example::create(){
    qint32 obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIAddressesApi apiInstance;
     
      // Configure API key authorization: X-RapidAPI-Host
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      // Configure API key authorization: X-API-Key
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      // Configure API key authorization: X-RapidAPI-Key
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString blockchain = create(); // QString | Blockchain name

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString address = create(); // QString | Wallet address

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 page = create(); // qint32 | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 page_size = create(); // qint32 | number of transactions returned by call (default and maximum 1000)

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 from_block = create(); // qint32 | filter of the returned transactions from block height to block height (default no filter)

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 to_block = create(); // qint32 | filter of the returned transactions from block height to block height (default no filter)

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString details = create(); // QString | specifies level of details returned by request

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString contract = create(); // QString | return only transactions which affect specified contract (applicable only to coins which support contracts)

      QEventLoop loop;
      connect(&apiInstance, &OAIAddressesApi::getAddressV2Signal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAddressesApi::getAddressV2SignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString secondary = create(); // QString | specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values
      apiInstance.getAddressV2(blockchainaddresspagepage_sizefrom_blockto_blockdetailscontractsecondary);
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
### X-API-Key


- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header

### X-RapidAPI-Host


- **Type**: API key
- **API key parameter name**: X-RapidAPI-Host
- **Location**: HTTP header

### X-RapidAPI-Key


- **Type**: API key
- **API key parameter name**: X-RapidAPI-Key
- **Location**: HTTP header


## Author

contact@chain49.com


## License

AGPL for more information visit [AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)