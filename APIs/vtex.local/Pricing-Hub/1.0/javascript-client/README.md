# pricing_hub

PricingHub - JavaScript client for pricing_hub
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

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install pricing_hub --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your pricing_hub from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var PricingHub = require('pricing_hub');

var defaultClient = PricingHub.ApiClient.instance;
// Configure API key authorization: appToken
var appToken = defaultClient.authentications['appToken'];
appToken.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix['X-VTEX-API-AppToken'] = "Token"
// Configure API key authorization: appKey
var appKey = defaultClient.authentications['appKey'];
appKey.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix['X-VTEX-API-AppKey'] = "Token"

var api = new PricingHub.PricingHubPricesApi()
var accountName = "'apiexamples'"; // {String} Name of the VTEX account. Used as part of the URL
var accept = "'application/json'"; // {String} HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
var contentType = "'application/json'"; // {String} Describes the type of the content being sent
var xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // {String} The AppKey configured by the merchant
var xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // {String} The AppToken configured by the merchant
var getPricesRequestObject = {"UtmCampaign":"summer","UtmInternalCampaign":"sale","UtmMedium":"social","UtmSource":"facebook","email":"customer@email.com","items":[{"brandId":"2000000","categoriesIds":["1"],"index":0,"priceTableIds":[],"quantity":1,"sellerId":"1","skuId":"13"}],"salesChannel":"1"}; // {GetPricesRequestObject} 
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.apiPricingHubPricesPost(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://vtex.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PricingHub.PricingHubPricesApi* | [**apiPricingHubPricesPost**](docs/PricingHubPricesApi.md#apiPricingHubPricesPost) | **POST** /api/pricing-hub/prices | Get Prices
*PricingHub.PricingHubPricesApi* | [**configExternalPriceSource**](docs/PricingHubPricesApi.md#configExternalPriceSource) | **PUT** /config | Configure External Price Source


## Documentation for Models

 - [PricingHub.ConfigExternalPriceSourceRequest](docs/ConfigExternalPriceSourceRequest.md)
 - [PricingHub.GetPricesRequestObject](docs/GetPricesRequestObject.md)
 - [PricingHub.Item1](docs/Item1.md)
 - [PricingHub.ItemsInner](docs/ItemsInner.md)
 - [PricingHub.Response2](docs/Response2.md)


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

