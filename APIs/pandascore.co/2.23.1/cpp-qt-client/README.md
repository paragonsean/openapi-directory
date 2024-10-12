# C++ Qt API client

# 

PandaScore REST API for All Videogames

- API version: 2.23.1
- Generator version: 7.9.0


# Introduction

Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).

The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.

- The current endpoint is [https://api.pandascore.co](https://api.pandascore.co).
- All data is sent and received as JSON by default.
- Blank fields are included with `null` values instead of being omitted.
- All timestamps are returned in ISO-8601 format

### About this documentation

Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)

You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)

## Events hierarchy

The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.

**Leagues**

Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.  
Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._  
Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._

**Series**

A Serie represents an occurrence of a league event.  
The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._  
Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._

**Tournaments**

Tournaments groups all the matches of a serie under \"stages\" and \"groups\".  
The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._  
Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._

**Matches**

Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).  
Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._  
Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._  

**Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**  
![Structure](/doc/images/structure.png)

## Formats

&lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt;
The API currently supports the JSON format by default.

Other formats may be added depending on user needs.

## Pagination

The Pandascore API paginates all resources on the index method.

Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.

The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format

```
Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\"
```

There is also:

* A `X-Page` header field, which contains the current page.
* A `X-Per-Page` header field, which contains the current pagination length.
* A `X-Total` header field, which contains the total count of items across all pages.

## Filtering

The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).

For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:

```
GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN
```

## Range

The `range` parameter is a hash that allows filtering fields by an interval.
Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.

For example, the following is a request for all the champions with `hp` within 500 and 1000:

```
GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN
```

## Search

The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.

Note: this only works on strings.
Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.

For example, to get all the champions with a name containing `\"twi\"`:

```
$ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name'
\"Twitch\"
\"Twisted Fate\"
```

## Sorting

All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.

The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.

For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage.
Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.

## Rate limiting

Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).

With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.

Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**

# Authentication

The authentication on the Pandascore API works with access tokens.

All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.

**Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**

The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.

&lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;



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
#include "../client/OAIIncidentsApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    OAIGet_additions_page_parameter create();
    qint32 create();
    QList<QString> create();
    QDateTime create();
    QList<OAIVideogameIDOrSlug> create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIIncidentsApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

OAIGet_additions_page_parameter Example::create(){
    OAIGet_additions_page_parameter obj;
qint32 Example::create(){
    qint32 obj;
QList&lt;QString&gt; Example::create(){
    QList<QString> obj;
QDateTime Example::create(){
    QDateTime obj;
QList&lt;OAIVideogameIDOrSlug&gt; Example::create(){
    QList<OAIVideogameIDOrSlug> obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIIncidentsApi apiInstance;
     
      // Configure HTTP bearer authorization: BearerToken
      apiInstance.setBearerToken("BEARER TOKEN");

      // Configure API key authorization: QueryToken
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      QEventLoop loop;
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAIGet_additions_page_parameter page = create(); // OAIGet_additions_page_parameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`

      QEventLoop loop;
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      qint32 per_page = create(); // qint32 | Equivalent to `page[size]`

      QEventLoop loop;
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QList<QString> type = create(); // QList<QString> | Filter by result type(s)

      QEventLoop loop;
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QDateTime since = create(); // QDateTime | Filter out older results

      QEventLoop loop;
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIIncidentsApi::getAdditionsSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QList<OAIVideogameIDOrSlug> videogame = create(); // QList<OAIVideogameIDOrSlug> | Filter by videogame(s)
      apiInstance.getAdditions(pageper_pagetypesincevideogame);
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
### BearerToken


- **Type**: HTTP Bearer Token authentication

### QueryToken


- **Type**: API key
- **API key parameter name**: token
- **Location**: URL query string


## Author




## License

 for more information visit []()