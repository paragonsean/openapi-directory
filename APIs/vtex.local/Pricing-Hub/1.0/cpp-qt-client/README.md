# C++ Qt API client

# 

Pricing Hub

- API version: 1.0
- Generator version: 7.9.0

> This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 

 In the B2B scenario, it is common for stores to have personalized prices per customer and complex pricing systems that require external integrations. Pricing Hub is a system developed for the B2B context that works as an intermediary between VTEX and external pricing systems.

 In VTEX, B2B stores have the option to use our internal pricing system or an external one. If the store chooses to operate with an external pricing system, Pricing Hub will query an external price calculation API. The external API should then respond with the price for all items in the shopping cart according to its predefined tax rules.

![Pricing hub protocal diagram](https://user-images.githubusercontent.com/77292838/211634260-e4f7a516-91df-416e-ab43-d9c79d56bc91.png)

## Implementation

To connect with external pricing systems using Pricing Hub, it is necessary to build a VTEX IO middleware app. We offer two reference implementation templates to simplify this process:

- [C# template](https://github.com/vtex-apps/external-prices-app)
- [Node template](https://github.com/vtex-apps/external-prices-node)

Read the documentation on each repository to learn more about the required steps to use and customize the app.

> The app used by Pricing Hub to connect must be a `major 0`. 

## Specifications

See below all the specifications of the request and the response expected when communicating with Pricing Hub.

### Price calculation request

The external prices calculation tool must provide an endpoint that will receive a `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices) request. This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.

>⚠️ Responses from Pricing Hub tend to have a greater delay when compared to other VTEX systems. That is expected, however, due to the complexity of its nested requests. The timeout for this request is 900 milliseconds.

In this request, Pricing Hub provides a body in a specific format, exemplified below. This means that either the endpoint must be prepared to receive this body format, or the app must contain a parser to adapt it to the correct format.

#### Request body example

```json
{
    \"item\": 
        {
            \"index\": 0,
            \"skuId\": \"880011\",
            \"quantity\": 1
        },
    \"context\":{
        \"email\": \"john@email.com\"
    }
}
```

The request body should have the following properties:

| **Attribute** | **Type** | **Description**                                                                                                                                                                                          |
|---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `item`        | object   | The item whose price is supposed to be fetched by Pricing Hub.                                                                                                                                           |
| ↪ `index`     | integer  | This is the index of the item at Checkout's cart. It has to be unique in the items array.                                                                                                                |
| ↪ `skuId`     | string   | This is the SKU ID of the item that will be priced.                                                                                                                                                      |
| ↪ `quantity`  | integer  | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price. |
| `context`     | object   | The object that contains the context to inform the query.                                                                                                                                                |
| ↪ `email`     | string   | The customer's email address. If there is no value, use an empty string.                                                                                                                                 |

### External prices provider response

In response to the request sent by Pricing Hub, we expect an outcome in the following format:

```json
{
    \"item\": {
        \"price\": 54035,
        \"priceTables\": \"special\",
        \"index\": 0,
        \"skuId\": \"880011\",
        \"listPrice\": 54035,
        \"costPrice\": 50000,
        \"sellingPrice\": 54035,
        \"priceValidUntil\": \"2023-01-27T20:29:57Z\",
        \"tradePolicyId\": \"special\"
    }
}
```

The response should have the following properties:

| **Attribute**       | **Type** | **Description**                                                                                                                                        |
|---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `item`              | object   | The object that contains the price data.                                                                                                               |
| ↪ `price`           | integer  | The price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.                    |
| ↪ `priceTables`     | string   | The price table that was used to price the item.                                                                                                       |
| ↪ `index`           | integer  | The same index referring to Checkout's cart that was passed to the API.                                                                                |
| ↪ `skuId`           | string   | The same SKU ID that was passed to the API.                                                                                                            |
| ↪ `listPrice`       | integer  | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |
| ↪ `costPrice`       | integer  | The cost price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |
| ↪ `sellingPrice`    | integer  | The computed price before applying coupons, taxes or promotions.                                                                                       |
| ↪ `priceValidUntil` | string   | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339. |
| ↪ `tradePolicyId`   | string   | Trade Policy ID.                                                                                                                                       |

## Index - Pricing Hub API

`POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices)
`PUT` [Configure External Price Source](https://developers.vtex.com/docs/api-reference/pricing-hub#put-/config)



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
#include "../client/OAIPricingHubPricesApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
    OAIGetPricesRequestObject create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIPricingHubPricesApi.h"
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
OAIGetPricesRequestObject Example::create(){
    OAIGetPricesRequestObject obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIPricingHubPricesApi apiInstance;
     
      // Configure API key authorization: appToken
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      // Configure API key authorization: appKey
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      QEventLoop loop;
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString account_name = create(); // QString | Name of the VTEX account. Used as part of the URL

      QEventLoop loop;
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString accept = create(); // QString | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand

      QEventLoop loop;
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString content_type = create(); // QString | Describes the type of the content being sent

      QEventLoop loop;
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_vtex_api_app_key = create(); // QString | The AppKey configured by the merchant

      QEventLoop loop;
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString x_vtex_api_app_token = create(); // QString | The AppToken configured by the merchant

      QEventLoop loop;
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIPricingHubPricesApi::apiPricingHubPricesPostSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAIGetPricesRequestObject oai_get_prices_request_object = create(); // OAIGetPricesRequestObject | 
      apiInstance.apiPricingHubPricesPost(account_nameacceptcontent_typex_vtex_api_app_keyx_vtex_api_app_tokenoai_get_prices_request_object);
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