# C++ Qt API client

# 

Jumpseller API

- API version: 1.0.0
- Generator version: 7.9.0

# Endpoint Structure

All URLs are in the format: 

```text
https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken  
```

The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token.
<br/><br/>
***

# Version

The current version of the API is **v1**.  
If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls.
<br/><br/>
***

# Authentication

The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.

![Store Login](/images/support/api/apilogin.png)

The auth token is a **32 characters** string.

If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information.
<br/><br/>
***

# Curl Examples

To request all the products at your store, you would append the products index path to the base url to create an URL with the format:  

```text
https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX
```

In curl, you can invoque that URL with:  

```text
curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\"
```

To create a product, you will include the JSON data and specify the MIME Type:  

```text
curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\"
```

and to update the product identified with 123:  

```text
curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\"
```

or delete it:  

```text
curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\"
```
<br/><br/>
***

# PHP Examples

Create a new Product (POST method)

```php
$url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX;
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method
curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');

$result = curl_exec($ch);
print_r($result);
curl_close($ch);
```
<br/><br/>
***

# Plain JSON only. No XML.

* We only support JSON for data serialization.
* Our node format has no root element.  
* We use snake_case to describe attribute keys (like \"created_at\").  
* All empty value are replaced with **null** strings.
* All API URLs end in .json to indicate that they accept and return JSON.
* POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**.
<br/><br/>
***

# Rate Limit
You can perform a maximum of:

+ 240 (two hundred forty) requests per minute and
+ 8 (eight) requests per second 

If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.  

The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.

This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:

```ruby
tries = 0; max_tries = 3;
begin
  HTTParty.send(method, uri) # perform an API call.
  sleep 0.5
  tries += 1
rescue
  unless tries >= max_tries
    sleep 1.0 # wait the necessary time before retrying the call again.
    retry
  end
end
```

Finally, you can review the Response Headers of each request:

```text
Jumpseller-PerMinuteRateLimit-Limit: 60  
Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval  
Jumpseller-PerSecondRateLimit-Limit: 2  
Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval
``` 

to better model your application requests intervals.

In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted.
<br/><br/>
***

# Pagination

By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`.
If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.

```text
https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100
```
<br/><br/>
***

# More
* [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API;
* [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts;
* [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files.
<br/><br/>
***
<br/><br/>



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
#include "../client/OAIAppsApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    QString create();
    QString create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIAppsApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIAppsApi apiInstance;
     
      QEventLoop loop;
      connect(&apiInstance, &OAIAppsApi::jsappsCodeJsonDeleteSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppsApi::jsappsCodeJsonDeleteSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString login = create(); // QString | API OAuth login.

      QEventLoop loop;
      connect(&apiInstance, &OAIAppsApi::jsappsCodeJsonDeleteSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppsApi::jsappsCodeJsonDeleteSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString authtoken = create(); // QString | API OAuth token.

      QEventLoop loop;
      connect(&apiInstance, &OAIAppsApi::jsappsCodeJsonDeleteSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIAppsApi::jsappsCodeJsonDeleteSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString code = create(); // QString | Code of the App
      apiInstance.jsappsCodeJsonDelete(loginauthtokencode);
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




## License

 for more information visit []()