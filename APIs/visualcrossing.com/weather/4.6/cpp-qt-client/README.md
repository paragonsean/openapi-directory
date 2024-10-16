# C++ Qt API client

# 

Visual Crossing Weather API

- API version: 4.6
- Generator version: 7.9.0

Weather Forecast and Historical Weather Data via RESTful API.

  For more information, please visit [https://www.visualcrossing.com/weather-api](https://www.visualcrossing.com/weather-api)

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
#include "../client/OAIHistoricalWeatherApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    bool create();
    QString create();
    QString create();
    bool create();
    QString create();
    QString create();
    bool create();
    QString create();
    bool create();
    QString create();
    QString create();
    QString create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIHistoricalWeatherApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
bool Example::create(){
    bool obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
bool Example::create(){
    bool obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
bool Example::create(){
    bool obj;
QString Example::create(){
    QString obj;
bool Example::create(){
    bool obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIHistoricalWeatherApi apiInstance;
     
      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString max_distance = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      bool short_column_names = create(); // bool | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString end_date_time = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString aggregate_hours = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      bool collect_station_contributions = create(); // bool | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString start_date_time = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString max_stations = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      bool allow_asynch = create(); // bool | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString locations = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      bool include_normals = create(); // bool | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString content_type = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString unit_group = create(); // QString | 

      QEventLoop loop;
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIHistoricalWeatherApi::visualCrossingWebServicesRestServicesWeatherdataHistoryGetSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString key = create(); // QString | 
      apiInstance.visualCrossingWebServicesRestServicesWeatherdataHistoryGet(max_distanceshort_column_namesend_date_timeaggregate_hourscollect_station_contributionsstart_date_timemax_stationsallow_asynchlocationsinclude_normalscontent_typeunit_groupkey);
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

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Author

info@visualcrossing.com


## License

Visual Crossing Weather API for more information visit [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)