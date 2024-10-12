# C++ Qt API client

# 

Checkout API

- API version: 1.0
- Generator version: 7.9.0

>ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.

The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.

>ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.

>⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.

## Shopping cart

Allows merchants to simulate, configure and customize shopping cart information.

- [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)
- [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)
- [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)
- [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)
- [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)
- [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)
- [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)
- [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)
- [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)
- [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)
- [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)


## Cart attachments

Allows merchants to obtain client profiles and add information to a given shopping cart.

- [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)
- [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)
- [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)
- [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)
- [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)
- [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)
- [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)


## Custom data

Allows merchants to manage custom fields that were created by an app in their account.

- [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)
- [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)
- [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)


## Configuration

Allows merchants to configure orderForm in the account and seller exchange on a given order.

- [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)
- [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)
- [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)
- [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)
- [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)


## Fulfillment

Allows merchants to obtain pickup points and address information.

- [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)
- [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)


## Order placement

Allows merchants to place and process orders by creating a new cart or using an existing cart.

- [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)
- [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)
- [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)


## Region

Allows merchants to obtain a list of sellers serving a specific delivery region.

- [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)


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
#include "../client/OAICartAttachmentsApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    QString create();
    QString create();
    OAIAddClientPreferences_request create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAICartAttachmentsApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
OAIAddClientPreferences_request Example::create(){
    OAIAddClientPreferences_request obj;
 return obj;
}

void Example::exampleFunction1(){
     OAICartAttachmentsApi apiInstance;
     
      QEventLoop loop;
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString content_type = create(); // QString | Type of the content being sent.

      QEventLoop loop;
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString accept = create(); // QString | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.

      QEventLoop loop;
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString order_form_id = create(); // QString | ID of the orderForm that will receive client profile information.

      QEventLoop loop;
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAICartAttachmentsApi::addClientPreferencesSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAIAddClientPreferences_request oai_add_client_preferences_request = create(); // OAIAddClientPreferences_request | 
      apiInstance.addClientPreferences(content_typeacceptorder_form_idoai_add_client_preferences_request);
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
### appKey


- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppKey
- **Location**: HTTP header

### appToken


- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppToken
- **Location**: HTTP header


## Author




## License

 for more information visit []()