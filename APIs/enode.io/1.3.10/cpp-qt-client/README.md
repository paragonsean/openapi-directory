# C++ Qt API client

# 

Enode API

- API version: 1.3.10
- Generator version: 7.9.0

Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)

Download [Postman Collection](/Postman-Enode-v1.4.0.json)

The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.

The API has a RESTful architecture and utilizes OAuth2 authorization.

We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io


## Registration for API access
In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.

# Authorization
Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.

> The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.

### Preparation: Configure your OAuth client

Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)

To configure your chosen OAuth client, you will need these details:
- Your `client_id`
- Your `client_secret`
- Authorization URL: `https://link.test.enode.io/oauth2/auth`
- Token URL: `https://link.test.enode.io/oauth2/token`

```javascript
// Node.js + openid-client example
const enodeIssuer = await Issuer.discover('https://link.test.enode.io');
const client = new enodeIssuer.Client({
  client_id: 'xyz',
  client_secret: 'shhhhh',
  redirect_uris: ['http://localhost:5000/callback'],
  response_types: ['code'],
});
```


### Preparation: Obtain a client access token via OAuth Client Credentials Grant
Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.

```javascript
// Node.js + openid-client example
const clientAccessToken = await client.grant({grant_type: \"client_credentials\"});
```

This access token belongs to your client and is used for administrative actions, such as the next step.

This token should be cached by your server and reused until it expires, at which point your server should request a new one.



### Step 1. Generate an Enode Link session for your User and launch the OAuth flow

When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.

Example Request:
```
POST /users/{userId}/link HTTP/1.1
Authorization: Bearer {access_token}
{
  \"forceLanguage\": \"nb-NO\",
  \"vendor\": \"Tesla\",
}
```

Example Response:
```
{
    \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\",
}
```

The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.

Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details:
- Redirect URI - The URI to which your user should be redirected when the Oauth flow completes
- Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer))
- State - The value of `linkState` from the request above

To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.

```javascript
// Node.js + openid-client + express example

// Construct an OAuth authorization URL
const authorizationUrl = client.authorizationUrl({
  scope: \"offline_access all\",
  state: linkState
});

// Redirect user to authorization URL
res.redirect(authorizationUrl);
```


### Step 2. User grants consent
In the Link UI webapp the user will follow 3 steps:

1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box.
2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in.
3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.


### Step 3. OAuth flow concludes with a callback
When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.

Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.

Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).

```javascript
// Node.js + openid-client + express example

// Fetch linkState from user session
const linkState = get(req, 'session.linkState');

// Parse relevant parameters from request URL
const params = client.callbackParams(req);

// Exchange authorization code for access and refresh tokens
// In this example, openid-client does the linkState validation check for us
const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState})
```

With the access token in hand, you can now access resources on behalf of the user.


# Errors And Problems
## OAuth Authorization Request

When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:

|error                      |error_description|
|---------------------------|-----------------|
|invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.|
|unauthorized_client        |The client is not authorized to request an authorization code using this method.|
|access_denied              |The resource owner or authorization server denied the request.|
|unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.|
|invalid_scope              |The requested scope is invalid, unknown, or malformed.|
|server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.|
|temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|

Example:
```
https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request.
```


## Errors when accessing a User's resources

When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:

|HTTP Status Code           |Explanation      |
|---------------------------|-----------------|
|400 Bad Request            |The request payload has failed schema validation / parsing
|401 Unauthorized           |Authentication details are missing or invalid
|403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource
|404 Not Found              |A non-existent resource is requested
|429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request


In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.

Example:
```
HTTP/1.1 400 Bad Request
Content-Type: application/problem+json
{
  \"type\": \"https://docs.enode.io/problems/payload-validation-error\",
  \"title\": \"Payload validation failed\",
  \"detail\": \"\\\"authorizationRequest.scope\\\" is required\",
}
```




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
#include "../client/OAIChargersApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    OAIControlChargerCharging_request create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIChargersApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
OAIControlChargerCharging_request Example::create(){
    OAIControlChargerCharging_request obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIChargersApi apiInstance;
     
      //OAuth Authentication supported right now

      QEventLoop loop;
      connect(&apiInstance, &OAIChargersApi::controlChargerChargingSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIChargersApi::controlChargerChargingSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString charger_id = create(); // QString | ID of the Charger

      QEventLoop loop;
      connect(&apiInstance, &OAIChargersApi::controlChargerChargingSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIChargersApi::controlChargerChargingSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAIControlChargerCharging_request oai_control_charger_charging_request = create(); // OAIControlChargerCharging_request | 
      apiInstance.controlChargerCharging(charger_idoai_control_charger_charging_request);
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
### ClientAccessToken


- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A

### UserAccessToken


- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://link.test.enode.io/oauth2/auth
- **Scopes**: 
  - all: Read and write all resources
  - charger:charge_state: Read charger charge state
  - charger:information: Read charger information
  - charging_location: Read &amp; write user&#39;s charging locations
  - control:charger:charging: Control charger charging
  - control:vehicle:charging: Control vehicle charging
  - vehicle:charge_state: Read vehicle charge state
  - vehicle:information: Read vehicle information
  - vehicle:location: Read vehicle location
  - vehicle:odometer: Read vehicle odometer
  - vehicle:smart_charging_policy: Read &amp; write vehicle smart charging policy


## Author




## License

 for more information visit []()