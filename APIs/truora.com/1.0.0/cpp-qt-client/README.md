# C++ Qt API client

# 

Checks API

- API version: 1.0.0
- Generator version: 7.9.0

**NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.

# Introduction

Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).

Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:

- **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.

- **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.  

- **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.

# API Key V1 is live!

API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:

- The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law.
- The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.


# API composition

## Endpoints

- **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.
 
```plain
https://api.truora.com/v1/checks
```

- **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.
 
```plain
https://api.truora.com/v1/reports
```

- **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.

```plain
https://api.truora.com/v1/config
```

- **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.

```plain
https://api.truora.com/v1/continuous_checks
```

- **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.

```plain
https://api.truora.com/v1/behaviour
```

- **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.

```plain
https://api.truora.com/v1/hooks
```

## Datasets

Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:

- **Personal identity**: Corroborates the existence and validates personal identity documents. 

- **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.

- **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.

- **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.

- **Professional background**: Checks professional regulatory entities for relevant information.

- **Affiliations and insurances**: Checks the history and status of social security affiliations.

- **Alert in media**: Checks major media agencies for relevant news related to violent actions.    

- **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.

- **Traffic fines**: Checks for outstanding traffic fines.

- **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.

- **Business background**: Checks for business status, legal and criminal history, and other relevant information.

- **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.

## Requests Format

The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:

```plain
type=person&national_id=123456&country=CO
```

The responses are always encoded in `JSON` format.

## Errors

Whenever there is an error, a JSON with the following format is returned:

```json
{
    \"code\": <Truora error code>,
    \"http_code\": <The HTTP status of the response>,
    \"message\": <The error message>
}
```

for instance:

```json
{
    \"code\": 10404,
    \"http_code\": 404,
    \"message\": \"The Check was not found\"
}
```

## SDKs

If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).

To download the SDK click on the desired programming language:

- [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)

- [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)

- [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)

- [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)

- [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)

- [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)

- [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)

- [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)

- [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)

You can see the full list of supported platforms here:

https://openapi-generator.tech/docs/generators




  For more information, please visit [https://www.truora.com](https://www.truora.com)

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
#include "../client/OAIBehaviorApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QDateTime create();
    QString create();
    QString create();
    QString create();
    QString create();
    QDateTime create();
    QString create();
    QString create();
    QString create();
    QString create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIBehaviorApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QDateTime Example::create(){
    QDateTime obj;
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
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIBehaviorApi apiInstance;
     
      // Configure API key authorization: api-key
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QDateTime birth_date = create(); // QDateTime | Birth date of reported person

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString country = create(); // QString | Document country

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString document_id = create(); // QString | Person document ID

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString document_type = create(); // QString | Document type associated with the background check

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString email = create(); // QString | Reported person e-mail

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QDateTime feedback_date = create(); // QDateTime | Behavior report date

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString first_name = create(); // QString | Person first name

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString last_name = create(); // QString | Person last name

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString reason = create(); // QString | Report reason

      QEventLoop loop;
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBehaviorApi::reportBehaviorSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString phone_number = create(); // QString | Phone number of the reported person
      apiInstance.reportBehavior(birth_datecountrydocument_iddocument_typeemailfeedback_datefirst_namelast_namereasonphone_number);
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
### api-key


- **Type**: API key
- **API key parameter name**: Truora-API-Key
- **Location**: HTTP header


## Author

api@truora.com


## License

MIT License for more information visit [MIT License](https://opensource.org/licenses/MIT)