# openapi-java-client

Fulfillment.com APIv2
- API version: 2.0
  - Build date: 2024-10-12T12:32:09.361421-04:00[America/New_York]
  - Generator version: 7.9.0

Welcome to our current iteration of our REST API. While we encourage you to upgrade to v2.0 we will continue support for our [SOAP API](https://github.com/fulfillment/soap-integration).

# Versioning

The Fulfillment.com (FDC) REST API is version controlled and backwards compatible. We have many future APIs scheduled for publication within our v2.0 spec so please be prepared for us to add data nodes in our responses, however, we will not remove knowledge from previously published APIs.

#### A Current Response

```javascript
{
  id: 123
}
```

#### A Potential Future Response

```javascript
{
  id: 123,
  reason: \"More Knowledge\"
}
```

# Getting Started

We use OAuth v2.0 to authenticate clients, you can choose [implicit](https://oauth.net/2/grant-types/implicit/) or [password](https://oauth.net/2/grant-types/password/) grant type. To obtain an OAuth `client_id` and `client_secret` contact your account executive.

**Tip**: Generate an additional login and use those credentials for your integration so that changes are accredited to that \"user\".

You are now ready to make requests to our other APIs by filling your `Authorization` header with `Bearer {access_token}`.

## Perpetuating Access

Perpetuating access to FDC without storing your password locally can be achieved using the `refresh_token` returned by [POST /oauth/access_token](#operation/generateToken).

A simple concept to achieve this is outlined below.

1. Your application/script will ask you for your `username` and `password`, your `client_id` and `client_secret` will be accessible via a DB or ENV.
2. [Request an access_token](#operation/generateToken)
  + Your function should be capable of formatting your request for both a `grant_type` of \\\"password\\\" (step 1) and \\\"refresh_token\\\" (step 4).
3. Store the `access_token` and `refresh_token` so future requests can skip step 1
4. When the `access_token` expires request anew using your `refresh_token`, replace both tokens in local storage.

+ If this fails you will have to revert to step 1.

Alternatively if you choose for your application/script to have access to your `username` and `password` you can skip step 4.

In all scenarios we recommend storing all credentials outside your codebase.

## Date Time Definitions

We will report all date-time stamps using the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard. When using listing API's where fromDate and toDate are available note that both dates are inclusive while requiring the fromDate to be before or at the toDate.

### The Fulfillment Process

Many steps are required to fulfill your order we report back to you three fundamental milestones inside the orders model.

* `recordedOn` When we received your order. This will never change.

* `dispatchDate` When the current iteration of your order was scheduled for fulfillment. This may change however it is an indicator that the physical process of fulfillment has begun and a tracking number has been **assigned** to your order. The tracking number **MAY CHANGE**. You will not be able to cancel an order once it has been dispatched. If you need to recall an order that has been dispatched please contact your account executive.

* `departDate` When we recorded your order passing our final inspection and placed with the carrier. At this point it is **safe to inform the consignee** of the tracking number as it will not change.

## Evaluating Error Responses

We currently return two different error models, with and without context. All errors will include a `message` node while errors with `context` will include additional information designed to save you time when encountering highly probable errors. For example, when you send us a request to create a duplicate order, we will reject your request and the context will include the FDC order `id` so that you may record it for your records.

### Without Context

New order with missing required fields.

| Header | Response |
| ------ | -------- |
| Status | `400 Bad Request` |

```javascript
{    
  \"message\": \"Invalid request body\"
}
```

### With Context

New order with duplicate `merchantOrderId`.

| Header | Response |
| ------ | -------- |
| Status | `409 Conflict` |

```javascript
{
  \"message\": \"Duplicate Order\",
  \"context\": {
    \"id\": 123
  }
}
```

## Status Codes

Codes are a concatenation of State, Stage, and Detail.

`^([0-9]{2})([0-9]{2})([0-9]{2})$`

| Code | State              | Stage    | Detail         |
| ---- | ------------------ | -------- | -------------- |
| 010101 | Processing Order | Recieved | Customer Order |
| 010102 | Processing Order | Recieved | Recieved |
| 010201 | Processing Order | Approved | |
| 010301 | Processing Order | Hold | Merchant Stock |
| 010302 | Processing Order | Hold | Merchant Funds |
| 010303 | Processing Order | Hold | For Merchant |
| 010304 | Processing Order | Hold | Oversized Shipment |
| 010305 | Processing Order | Hold | Invalid Parent Order |
| 010306 | Processing Order | Hold | Invalid Address |
| 010307 | Processing Order | Hold | By Admin |
| 010401 | Processing Order | Address Problem | Incomplete Address |
| 010402 | Processing Order | Address Problem | Invalid Locality |
| 010403 | Processing Order | Address Problem | Invalid Region |
| 010404 | Processing Order | Address Problem | Address Not Found |
| 010405 | Processing Order | Address Problem | Many Addresses Found |
| 010406 | Processing Order | Address Problem | Invalid Postal Code |
| 010407 | Processing Order | Address Problem | Country Not Mapped |
| 010408 | Processing Order | Address Problem | Invalid Recipient Name |
| 010409 | Processing Order | Address Problem | Bad UK Address |
| 010410 | Processing Order | Address Problem | Invalid Address Line 1 or 2 |
| 010501 | Processing Order | Sku Problem | Invalid SKU |
| 010501 | Processing Order | Sku Problem | Child Order has Invalid SKUs |
| 010601 | Processing Order | Facility Problem | Facility Not Mapped |
| 010701 | Processing Order | Ship Method Problem | Unmapped Ship Method |
| 010702 | Processing Order | Ship Method Problem | Unmapped Ship Cost |
| 010703 | Processing Order | Ship Method Problem | Missing Ship Method |
| 010704 | Processing Order | Ship Method Problem | Invalid Ship Method |
| 010705 | Processing Order | Ship Method Problem | Order Weight Outside of Ship Method Weight |
| 010801 | Processing Order | Inventory Problem | Insufficient Inventory In Facility |
| 010802 | Processing Order | Inventory Problem | Issue Encountered During Inventory Adjustment |
| 010901 | Processing Order | Released To WMS | Released |
| 020101 | Fulfillment In Progress | Postage Problem | Address Issue |
| 020102 | Fulfillment In Progress | Postage Problem | Postage OK, OMS Issue Occurred |
| 020103 | Fulfillment In Progress | Postage Problem | Postage Void Failed |
| 020201 | Fulfillment In Progress | Postage Acquired | |
| 020301 | Fulfillment In Progress | Postage Voided | Postage Void Failed Gracefully |
| 020301 | Fulfillment In Progress | Hold | Departure Hold Requested |
| 020401 | Fulfillment In Progress | 4PL Processing | |
| 020501 | Fulfillment In Progress | 4PL Problem | Order is Proccessable, Postage Issue Occurred |
| 020601 | Fulfillment In Progress | Label Printed | |
| 020701 | Fulfillment In Progress | Shipment Cubed | |
| 020801 | Fulfillment In Progress | Picking Inventory | |
| 020901 | Fulfillment In Progress | Label Print Verified | |
| 021001 | Fulfillment In Progress | Passed Final Inspection | |
| 030101 | Shipped | Fulfilled By 4PL | |
| 030102 | Shipped | Fulfilled By 4PL | Successfully Fulfilled, OMS Encountered Issue During Processing |
| 030201 | Shipped | Fulfilled By FDC | |
| 040101 | Returned | Returned | |
| 050101 | Cancelled | Cancelled | |
| 060101 | Test | Test | Test |


  For more information, please visit [https://fulfillment.com](https://fulfillment.com)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String fromDate = "fromDate_example"; // String | Orders invoice date. Date-time in ISO 8601 format for selecting orders after, or at, the specified time
    String toDate = "toDate_example"; // String | Orders invoice date. Date-time in ISO 8601 format for selecting orders before, or at, the specified time
    List<String> hydrate = Arrays.asList(); // List<String> | Adds additional information to the response, uses a CSV format for multiple values.
    Integer page = 1; // Integer | A multiplier of the number of items (limit parameter) to skip before returning results
    Integer limit = 80; // Integer | The numbers of items to return
    List<Integer> warehouseIds = Arrays.asList(); // List<Integer> | A CSV of warehouse id, '123' or '1,2,3'
    List<Integer> orderIds = Arrays.asList(); // List<Integer> | A CSV of FDC order id, '123' or '1,2,3'
    try {
      AccountingArrayV2 result = apiInstance.getAccounting(fromDate, toDate, hydrate, page, limit, warehouseIds, orderIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getAccounting");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.fulfillment.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountingApi* | [**getAccounting**](docs/AccountingApi.md#getAccounting) | **GET** /accounting | List Order Accounting
*AuthApi* | [**postOauthAccessToken**](docs/AuthApi.md#postOauthAccessToken) | **POST** /oauth/access_token | Generate an Access Token
*InventoryApi* | [**getInventory**](docs/InventoryApi.md#getInventory) | **GET** /inventory | List of Item Inventories
*OrdersApi* | [**deleteOrdersId**](docs/OrdersApi.md#deleteOrdersId) | **DELETE** /orders/{id} | Cancel an Order
*OrdersApi* | [**getOrder**](docs/OrdersApi.md#getOrder) | **GET** /orders/{id} | Order Details
*OrdersApi* | [**getOrders**](docs/OrdersApi.md#getOrders) | **GET** /orders | List of Orders
*OrdersApi* | [**postOrders**](docs/OrdersApi.md#postOrders) | **POST** /orders | New Order
*PartnersApi* | [**putOrdersIdShip**](docs/PartnersApi.md#putOrdersIdShip) | **PUT** /orders/{id}/ship | Ship an Order
*PartnersApi* | [**putOrdersIdStatus**](docs/PartnersApi.md#putOrdersIdStatus) | **PUT** /orders/{id}/status | Update Order Status
*ReturnsApi* | [**getReturns**](docs/ReturnsApi.md#getReturns) | **GET** /returns | List Returns
*ReturnsApi* | [**putReturns**](docs/ReturnsApi.md#putReturns) | **PUT** /returns | Inform us of an RMA
*TrackingApi* | [**getTrack**](docs/TrackingApi.md#getTrack) | **GET** /track | Tracking
*UsersApi* | [**getUsersMe**](docs/UsersApi.md#getUsersMe) | **GET** /users/me | About Me


## Documentation for Models

 - [AccessTokenRequestPasswordV2](docs/AccessTokenRequestPasswordV2.md)
 - [AccessTokenRequestRefreshV2](docs/AccessTokenRequestRefreshV2.md)
 - [AccessTokenRequestV2](docs/AccessTokenRequestV2.md)
 - [AccessTokenResponseV2](docs/AccessTokenResponseV2.md)
 - [AccountingArrayV2](docs/AccountingArrayV2.md)
 - [AccountingArrayV2Meta](docs/AccountingArrayV2Meta.md)
 - [AccountingV2](docs/AccountingV2.md)
 - [AccountingV2Fees](docs/AccountingV2Fees.md)
 - [AccountingV2ItemsInner](docs/AccountingV2ItemsInner.md)
 - [AccountingV2Merchant](docs/AccountingV2Merchant.md)
 - [AccountingV2Order](docs/AccountingV2Order.md)
 - [AccountingV2Warehouse](docs/AccountingV2Warehouse.md)
 - [CarrierHydratedV2](docs/CarrierHydratedV2.md)
 - [CarrierSimpleV2](docs/CarrierSimpleV2.md)
 - [ConsigneeNewV2](docs/ConsigneeNewV2.md)
 - [ConsigneeV2](docs/ConsigneeV2.md)
 - [ErrorStandardV2](docs/ErrorStandardV2.md)
 - [ErrorStandardWithContextV2](docs/ErrorStandardWithContextV2.md)
 - [Feature](docs/Feature.md)
 - [FeatureProperties](docs/FeatureProperties.md)
 - [Geometry](docs/Geometry.md)
 - [GeometryCoordinates](docs/GeometryCoordinates.md)
 - [IsoCountryV2](docs/IsoCountryV2.md)
 - [ItemInventoryArrayV2](docs/ItemInventoryArrayV2.md)
 - [ItemInventoryV2](docs/ItemInventoryV2.md)
 - [ItemInventoryV2Item](docs/ItemInventoryV2Item.md)
 - [ItemInventoryV2Merchant](docs/ItemInventoryV2Merchant.md)
 - [ItemInventoryV2Quantity](docs/ItemInventoryV2Quantity.md)
 - [ItemInventoryV2QuantityTotal](docs/ItemInventoryV2QuantityTotal.md)
 - [LineItemsResponseV2](docs/LineItemsResponseV2.md)
 - [LineItemsResponseV2InventoryDetailsInner](docs/LineItemsResponseV2InventoryDetailsInner.md)
 - [LineItemsResponseV2LineDetails](docs/LineItemsResponseV2LineDetails.md)
 - [LineItemsResponseV2RequestedSkuData](docs/LineItemsResponseV2RequestedSkuData.md)
 - [MerchantV2](docs/MerchantV2.md)
 - [OrderRequestV2](docs/OrderRequestV2.md)
 - [OrderRequestV2ItemsInner](docs/OrderRequestV2ItemsInner.md)
 - [OrderRequestV2Warehouse](docs/OrderRequestV2Warehouse.md)
 - [OrderResponseHydrateV2](docs/OrderResponseHydrateV2.md)
 - [OrderResponseHydrateV2AllOfTrackingNumbersInner](docs/OrderResponseHydrateV2AllOfTrackingNumbersInner.md)
 - [OrderResponseOneOfV2](docs/OrderResponseOneOfV2.md)
 - [OrderResponseV2](docs/OrderResponseV2.md)
 - [OrderResponseV2ParentOrder](docs/OrderResponseV2ParentOrder.md)
 - [OrderShipV2](docs/OrderShipV2.md)
 - [PaginationV2](docs/PaginationV2.md)
 - [ReturnV2](docs/ReturnV2.md)
 - [ReturnV2Order](docs/ReturnV2Order.md)
 - [ReturnV2Reason](docs/ReturnV2Reason.md)
 - [ReturnsArrayV2](docs/ReturnsArrayV2.md)
 - [RmaItemV2](docs/RmaItemV2.md)
 - [RmaItemV2Item](docs/RmaItemV2Item.md)
 - [RmaItemV2NonRestockedReason](docs/RmaItemV2NonRestockedReason.md)
 - [RmaRequestV2](docs/RmaRequestV2.md)
 - [RmaRequestV2ItemsInner](docs/RmaRequestV2ItemsInner.md)
 - [RmaResponseV2](docs/RmaResponseV2.md)
 - [StatusEventV2](docs/StatusEventV2.md)
 - [StatusTypeSimpleV2](docs/StatusTypeSimpleV2.md)
 - [StatusTypeSimpleV2Status](docs/StatusTypeSimpleV2Status.md)
 - [StatusTypeV2](docs/StatusTypeV2.md)
 - [StatusTypeV2ActionRequiredBy](docs/StatusTypeV2ActionRequiredBy.md)
 - [StatusTypeV2Stage](docs/StatusTypeV2Stage.md)
 - [TrackingEventV2](docs/TrackingEventV2.md)
 - [TrackingNumberV2](docs/TrackingNumberV2.md)
 - [TrackingResponse](docs/TrackingResponse.md)
 - [UserContactV2](docs/UserContactV2.md)
 - [UserContactV2Merchant](docs/UserContactV2Merchant.md)
 - [UserV2](docs/UserV2.md)
 - [WarehouseV2](docs/WarehouseV2.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
### apiKey

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

<a id="fdcAuth"></a>
### fdcAuth

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
  - oms: read &amp; write access

<a id="fdcAuth"></a>
### fdcAuth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://api.fulfillment.com/v2/oauth/authorize
- **Scopes**: 
  - oms: read &amp; write access


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

dev@fulfillment.com

