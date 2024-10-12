# C++ Qt API client

# 

Rebilly REST API

- API version: 2.1
- Generator version: 7.9.0

# Introduction
The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable
resource URLs.  It returns HTTP response codes to indicate errors.  It also
accepts and returns JSON in the HTTP body.  You can use your favorite
HTTP/REST library for your programming language to use Rebilly's API, or
you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php)
and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).

We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com)
is supported by an API which is documented and available for use so that you
may automate any workflows necessary.  This document contains the most commonly
integrated resources.

# Authentication

When you sign up for an account, you are given your first secret API key.
You can generate additional API keys, and delete API keys (as you may
need to rotate your keys in the future). You authenticate to the
Rebilly API by providing your secret key in the request header.

Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key.
- [Secret API key](#section/Authentication/SecretApiKey): used for requests made
  from the server side. Never share these keys. Keep them guarded and secure.
- [Publishable API key](#section/Authentication/PublishableApiKey): used for 
  requests from the client side. For now can only be used to create 
  a [Payment Token](#operation/PostToken) and 
  a [File token](#operation/PostFile).
- [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.

Never share your secret keys. Keep them guarded and secure.

&lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;

# Errors
Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.

## Forbidden
&lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;

## Conflict
&lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;

## NotFound
&lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;

## Unauthorized
&lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;

## ValidationError
&lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;

# SDKs

Rebilly offers a Javascript SDK and a PHP SDK to help interact with
the API.  However, no SDK is required to use the API.

Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),
 a client-side iFrame-based solution to help
create payment tokens while minimizing PCI DSS compliance burdens
and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/)
is interacting with the [payment tokens creation operation](#operation/PostToken).

## Javascript SDK

Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks).
SDK code examples are included in these docs.

## PHP SDK
For all PHP SDK examples provided in these docs you will need to configure the `$client`.
You may do it like this:

```php
$client = new Rebilly\\Client([
    'apiKey' =&gt; 'YourApiKeyHere',
    'baseUrl' =&gt; 'https://api.rebilly.com',
]);
```

# Using filter with collections
Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.

Here is filter format description:

- Fields and values in filter are separated with `:`: `?filter=firstName:John`.

- Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.

- Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.

- You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.

- To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.

- You can use range filters like this: `?filter=amount:1..10`.

- You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.

- You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.

- Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`. 

# Expand to include embedded objects
Rebilly provides the ability to pre-load additional 
objects with a request. 

You can use `?expand` param on most requests to expand
and include embedded objects within the
`_embedded` property of the response.

The `_embedded` property contains an array of 
objects keyed by the expand parameter value(s).

You may expand multiple objects by passing them
as comma-separated to the expand value like so:

```
?expand=recentInvoice,customer
```

And in the response, you would see:

```
\"_embedded\": [
    \"recentInvoice\": {...},
    \"customer\": {...}
]
```
Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.


# Getting started guide

Rebilly's API has over 300 operations.  That's more than you'll 
need to implement your use cases.  If you have a use 
case you would like to implement, please consult us for
feedback on the best API operations for the task.

Our getting started guide will demonstrate a basic order form use
case.  It will allow us to highlight core resources
in Rebilly that will be helpful for many other use cases
too.

Within 25 minutes, you'll have sent API requests (via our console)
to create a subscription order.


  For more information, please visit [https://www.rebilly.com/contact/](https://www.rebilly.com/contact/)

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
#include "../client/OAIAMLApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
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

#include "../client/OAIAMLApi.h"
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
 return obj;
}

void Example::exampleFunction1(){
     OAIAMLApi apiInstance;
     
      // Configure API key authorization: SecretApiKey
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      // Configure HTTP bearer authorization: JWT
      apiInstance.setBearerToken("BEARER TOKEN");

      QEventLoop loop;
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString first_name = create(); // QString | First name of individual to search.

      QEventLoop loop;
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString last_name = create(); // QString | Last name of individual to search.

      QEventLoop loop;
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString organization_id = create(); // QString | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).

      QEventLoop loop;
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString dob = create(); // QString | Date of birth in format YYYY-MM-DD.

      QEventLoop loop;
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAMLApi::getAmlEntrySignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString country = create(); // QString | Country of individual as an ISO Alpha-2 code.
      apiInstance.getAmlEntry(first_namelast_nameorganization_iddobcountry);
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
### JWT


- **Type**: HTTP Bearer Token authentication (JWT)

### PublishableApiKey


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

### SecretApiKey


- **Type**: API key
- **API key parameter name**: REB-APIKEY
- **Location**: HTTP header


## Author

integrations@rebilly.com


## License

Rebilly for more information visit [Rebilly](https://www.rebilly.com/api-license/)