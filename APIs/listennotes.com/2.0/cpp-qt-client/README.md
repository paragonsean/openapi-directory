# C++ Qt API client

# 

Listen API: Podcast Search, Directory, and Insights API

- API version: 2.0
- Generator version: 7.9.0

Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics.


  For more information, please visit [https://www.listennotes.com/api/](https://www.listennotes.com/api/)

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
#include "../client/OAIDirectoryAPIApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    QString create();
    qint32 create();
    QString create();
    QString create();
    QString create();
    QString create();
    qint32 create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIDirectoryAPIApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
qint32 Example::create(){
    qint32 obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
qint32 Example::create(){
    qint32 obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIDirectoryAPIApi apiInstance;
     
      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_listen_api_key = create(); // QString | Get API Key on listennotes.com/api

      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString genre_id = create(); // QString | You can get the id from `GET /genres`. If not specified, it'll be the overall best podcasts, which can be considered as a special genre.

      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 page = create(); // qint32 | Page number of those podcasts in this genre.

      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString region = create(); // QString | Filter best podcasts by country/region. Please note that podcasts that are \"best\" in a country/region may not be produced in that country/region. For example, a podcast from the US may be very popular in Canada. You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`. If not specified, you'll get \"best podcasts\" in United States. 

      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString publisher_region = create(); // QString | Filter best podcasts by the publisher's country/region. This is to narrow down the results to include \"best podcasts\" produced in a specific country/region. You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`. If not specified, you'll get \"best podcasts\" produced in any country/region. If you want to get a country/region's \"best podcasts\" that are also produced in that country/region, then you need to specify both **region** and **publisher_region**, e.g., `region=jp` and `publisher_region=jp`. 

      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString language = create(); // QString | Filter best podcasts by language. You can get a list of supported languages (e.g., English, Chinese, Japanese...) from `GET /languages`. If not specified, you'll get \"best podcasts\" in any language. 

      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString sort = create(); // QString | How do you want to sort these podcasts? If you'd like to sort by popularity, please use **listen_score**. 

      QEventLoop loop;
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDirectoryAPIApi::getBestPodcastsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 safe_mode = create(); // qint32 | Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
      apiInstance.getBestPodcasts(x_listen_api_keygenre_idpageregionpublisher_regionlanguagesortsafe_mode);
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

hello@listennotes.com


## License

 for more information visit []()