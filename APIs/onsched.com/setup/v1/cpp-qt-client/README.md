# C++ Qt API client

# 

OnSched Setup API

- API version: v1
- Generator version: 7.9.0

Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.
<br><br>
Take the API for a test drive. Just click on the Authorize button below and authenticate. 
You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.
<br><br>
The API has two interfaces, consumer and setup. 
<ul>
<li>
The consumer interface provides all the endpoints required for implementing consumer booking flows.
</li>
<li>
The setup interface provides endpoints for profile configuration and setup.
</li>
</ul>
Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.



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
#include "../client/OAIAppointmentsApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
    QDateTime create();
    QDateTime create();
    QString create();
    QString create();
    qint32 create();
    qint32 create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIAppointmentsApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QDateTime Example::create(){
    QDateTime obj;
QDateTime Example::create(){
    QDateTime obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
qint32 Example::create(){
    qint32 obj;
qint32 Example::create(){
    qint32 obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIAppointmentsApi apiInstance;
     
      //OAuth Authentication supported right now

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString location_id = create(); // QString | id of business location, defaults to primary business location

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString email = create(); // QString | Filter appointments by email address

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString lastname = create(); // QString | Filter appointments by lastname or part of

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString service_id = create(); // QString | Filter appointments by service

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString calendar_id = create(); // QString | Filter appointments by calendar

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString resource_id = create(); // QString | Filter appointments by resource

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString customer_id = create(); // QString | Filter appointments by customer

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString service_allocation_id = create(); // QString | Filter appointments by service allocation

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QDateTime start_date = create(); // QDateTime | Format YYYY-MM-DD: Filter appointments by on/after startDate

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QDateTime end_date = create(); // QDateTime | Format YYYY-MM-DD: Filter appointments on/before endDate

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString status = create(); // QString | Filter appointments by status: IN, BK, CN, RE, RS

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString booked_by = create(); // QString | Filter appointments by user email who booked

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 offset = create(); // qint32 | Starting row of page, default 0

      QEventLoop loop;
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppointmentsApi::setupV1AppointmentsGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 limit = create(); // qint32 | Page limit default 20, max 100
      apiInstance.setupV1AppointmentsGet(location_idemaillastnameservice_idcalendar_idresource_idcustomer_idservice_allocation_idstart_dateend_datestatusbooked_byoffsetlimit);
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
### oauth2


- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
  - OnSchedApi: Consumer and Setup Interface
  - distance: Travel and Distance calculations


## Author




## License

 for more information visit []()