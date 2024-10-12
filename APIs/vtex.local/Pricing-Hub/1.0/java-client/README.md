# openapi-java-client

Pricing Hub
- API version: 1.0
  - Build date: 2024-10-12T11:55:40.459-04:00[America/New_York]
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
  <version>1.0</version>
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
     implementation "org.openapitools:openapi-java-client:1.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.jar`
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
import org.openapitools.client.api.PricingHubPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    PricingHubPricesApi apiInstance = new PricingHubPricesApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | The AppKey configured by the merchant
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | The AppToken configured by the merchant
    GetPricesRequestObject getPricesRequestObject = new GetPricesRequestObject(); // GetPricesRequestObject | 
    try {
      Response2 result = apiInstance.apiPricingHubPricesPost(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingHubPricesApi#apiPricingHubPricesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://vtex.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PricingHubPricesApi* | [**apiPricingHubPricesPost**](docs/PricingHubPricesApi.md#apiPricingHubPricesPost) | **POST** /api/pricing-hub/prices | Get Prices
*PricingHubPricesApi* | [**configExternalPriceSource**](docs/PricingHubPricesApi.md#configExternalPriceSource) | **PUT** /config | Configure External Price Source


## Documentation for Models

 - [ConfigExternalPriceSourceRequest](docs/ConfigExternalPriceSourceRequest.md)
 - [GetPricesRequestObject](docs/GetPricesRequestObject.md)
 - [Item1](docs/Item1.md)
 - [ItemsInner](docs/ItemsInner.md)
 - [Response2](docs/Response2.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="appKey"></a>
### appKey

- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppKey
- **Location**: HTTP header

<a id="appToken"></a>
### appToken

- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppToken
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



