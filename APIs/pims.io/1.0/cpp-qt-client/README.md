# C++ Qt API client

# 

Pims

- API version: 1.0
- Generator version: 7.9.0


Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).

## Authentication
The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.

As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)

<div class=\"info\">
To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):
  <ul>
    <li>Base path: `https://demo.pims.io/api`</li>
    <li>Username: `demo`</li>
    <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>
  </ul>
</div>

## Response format
The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.

Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition.
<div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">
 <div style=\"display: inline-block; width:100%;\">
  <strong>So when you read in the doc:</strong>
<pre><code class=\"lang-json\">{
 <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,
 <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,
 <span class=\"token string\">\"object\"</span>: {
  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,
  <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>
 }
}</code></pre>
 </div>
 <div style=\"display: inline-block; width:100%;\">
  <strong>... you'll get in the Real World®:</strong>
<pre><code class=\"lang-json\">{
 <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,
 <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,
 <span class=\"token string\">\"_embedded\"</span>: {
  <span class=\"token string\">\"object\"</span>: {
   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,
   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,
   <span class=\"token string\">\"_links\"</span>: {
    <span class=\"token string\">\"self\"</span>: {
     <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>
    }
   }
  }
 }
 <span class=\"token string\">\"_links\"</span>: {
  <span class=\"token string\">\"self\"</span>: {
   <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>
  }
 }
}</code></pre>
 </div>
</div>

### Errors
Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.

The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON:
```json
{
 \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",
    \"title\": \"Not Found\",
 \"status\": 404,
    \"detail\": \"Entity not found\"
}
```

## Versioning
The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...

The version part of the URL is optional, and will be completed with the last stable version if omitted.

## Pagination
All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.

If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.

Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below:
```json
{
 \"_links\": {
  \"self\": {
   \"href\": \"https://demo.pims.io/api/v1/events?page=1\"
  },
  \"first\": {
   \"href\": \"https://demo.pims.io/api/v1/events\"
  },
  \"last\": {
   \"href\": \"https://demo.pims.io/api/v1/events?page=14\"
  },
  \"next\": {
   \"href\": \"https://demo.pims.io/api/v1/events?page=2\"
  }
 },
 \"_embedded\": {
   ... // data content goes here
 },
 \"page_count\": 14,
 \"page_size\": 25,
 \"total_items\": 331,
 \"page\": 1
}
```

## Filtering and sorting
Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is:
- Case insensitive: “Chloé” will be considered the same as “CHLOÉ”;
- Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.

When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).

## I18n
In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.

By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.

## PHP SDK
We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).

## And now?
Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).

Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>):
- Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts)
- Or get a full insight by calling these endpoints:
    1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)
    2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)
    3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)

Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.


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
#include "../client/OAICapacitiesApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    qint32 create();
    bool create();
    QString create();
    qint32 create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAICapacitiesApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

qint32 Example::create(){
    qint32 obj;
bool Example::create(){
    bool obj;
QString Example::create(){
    QString obj;
qint32 Example::create(){
    qint32 obj;
 return obj;
}

void Example::exampleFunction1(){
     OAICapacitiesApi apiInstance;
     
      // Configure HTTP basic authorization: Basic Auth
      apiInstance.setUsername("YOUR USERNAME");
      apiInstance.setPassword("YOUR PASSWORD");

      QEventLoop loop;
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 event_id = create(); // qint32 | ID of the targeted event.

      QEventLoop loop;
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      bool show_ignored = create(); // bool | If set to `false`, show only the [event-]categories which are not ignored. If set to `true`, show everything.

      QEventLoop loop;
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString sort = create(); // QString | Sort the capacities in the corresponding order.

      QEventLoop loop;
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICapacitiesApi::fetchAllEventsCapacitiesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 page_size = create(); // qint32 | Pagination size, i.e. maximum number of items to be displayed in the response.
      apiInstance.fetchAllEventsCapacities(event_idshow_ignoredsortpage_size);
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
### Basic Auth


- **Type**: HTTP basic authentication


## Author

support@pims.io


## License

Creative Commons CC BY-NC-ND 2.0 for more information visit [Creative Commons CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/)