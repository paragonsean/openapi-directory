# PromotionsTaxesApi.PromotionsAndTaxesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRnbPvtImportCalculatorConfigurationPost**](PromotionsAndTaxesApi.md#apiRnbPvtImportCalculatorConfigurationPost) | **POST** /api/rnb/pvt/import/calculatorConfiguration | Create Multiple SKU Promotion
[**apiRnbPvtImportCalculatorConfigurationPromotionIdPut**](PromotionsAndTaxesApi.md#apiRnbPvtImportCalculatorConfigurationPromotionIdPut) | **PUT** /api/rnb/pvt/import/calculatorConfiguration/{promotionId} | Update Multiple SKU Promotion
[**archivePromotion**](PromotionsAndTaxesApi.md#archivePromotion) | **POST** /api/rnb/pvt/archive/calculatorConfiguration/{idCalculatorConfiguration} | Archive Promotion or Tax
[**createOrUpdateCalculatorConfiguration**](PromotionsAndTaxesApi.md#createOrUpdateCalculatorConfiguration) | **POST** /api/rnb/pvt/calculatorconfiguration | Create or Update Promotion or Tax
[**getAllBenefits**](PromotionsAndTaxesApi.md#getAllBenefits) | **GET** /api/rnb/pvt/benefits/calculatorconfiguration | Get All Promotions
[**getAllTaxes**](PromotionsAndTaxesApi.md#getAllTaxes) | **GET** /api/rnb/pvt/taxes/calculatorconfiguration | Get All Taxes
[**getArchivedPromotions**](PromotionsAndTaxesApi.md#getArchivedPromotions) | **GET** /api/rnb/pvt/archive/benefits/calculatorConfiguration | List Archived Promotions
[**getArchivedTaxes**](PromotionsAndTaxesApi.md#getArchivedTaxes) | **GET** /api/rnb/pvt/archive/taxes/calculatorConfiguration | List Archived Taxes
[**getCalculatorConfigurationById**](PromotionsAndTaxesApi.md#getCalculatorConfigurationById) | **GET** /api/rnb/pvt/calculatorconfiguration/{idCalculatorConfiguration} | Get Promotion or Tax by ID
[**unarchivePromotion**](PromotionsAndTaxesApi.md#unarchivePromotion) | **POST** /api/rnb/pvt/unarchive/calculatorConfiguration/{idCalculatorConfiguration} | Unarchive Promotion or Tax



## apiRnbPvtImportCalculatorConfigurationPost

> apiRnbPvtImportCalculatorConfigurationPost(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, opts)

Create Multiple SKU Promotion

Creates a Multiple SKU Promotion. This scenario allows to create a single promotion for multiples SKUs with the Percentage Effect.   &gt; ⚠️   &gt;  &gt; The limit of SKUs on a Multiple Effects promotion is 400.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "text/csv"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let xVTEXCalculatorName = "Test"; // String | Promotion Name.
let xVTEXStartDate = "2020-08-18T16:00:00+3:00"; // String | Promotion start date.
let xVTEXEndDate = "2020-08-18T16:30:00+3:00"; // String | Promotion end date.
let xVTEXAccumulateWithManualPrices = false; // Boolean | Condition that will accumulate the Promotion with manual prices or not.
let opts = {
  'xVTEXCumulative': false, // Boolean | Defines if the Promotion is cumulative with other promotions.
  'xVTEXClusterOperator': "any", // String | This header allows implementing the Promotion in multiples client clusters. You can set the value as `all` - the Promotion will be valid to all the clusters - or `any` - the Promotion will be valid to any of the clusters.
  'xVTEXClusterExpression': "cluster_name=true", // String | Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them.
  'body': "/path/to/file" // File | 
};
apiInstance.apiRnbPvtImportCalculatorConfigurationPost(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **xVTEXCalculatorName** | **String**| Promotion Name. | 
 **xVTEXStartDate** | **String**| Promotion start date. | 
 **xVTEXEndDate** | **String**| Promotion end date. | 
 **xVTEXAccumulateWithManualPrices** | **Boolean**| Condition that will accumulate the Promotion with manual prices or not. | 
 **xVTEXCumulative** | **Boolean**| Defines if the Promotion is cumulative with other promotions. | [optional] 
 **xVTEXClusterOperator** | **String**| This header allows implementing the Promotion in multiples client clusters. You can set the value as &#x60;all&#x60; - the Promotion will be valid to all the clusters - or &#x60;any&#x60; - the Promotion will be valid to any of the clusters. | [optional] 
 **xVTEXClusterExpression** | **String**| Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them. | [optional] 
 **body** | **File**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: text/csv
- **Accept**: Not defined


## apiRnbPvtImportCalculatorConfigurationPromotionIdPut

> apiRnbPvtImportCalculatorConfigurationPromotionIdPut(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, promotionId, opts)

Update Multiple SKU Promotion

Updates information from a Multiple SKU Promotion. This scenario allows to create a single promotion for multiples SKUs with the Percentage Effect.    &gt; ⚠️   &gt;  &gt; The limit of SKUs on a Multiple Effects promotion is 400.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "text/csv"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let xVTEXCalculatorName = "Test"; // String | Promotion Name.
let xVTEXStartDate = "2020-08-18T16:00:00+3:00"; // String | Promotion start date.
let xVTEXEndDate = "2020-08-18T16:30:00+3:00"; // String | Promotion end date.
let xVTEXAccumulateWithManualPrices = false; // Boolean | Condition that will accumulate the Promotion with manual prices or not.
let promotionId = "dc6b6f59-ec2b-4a13-8490-0d1e0c53ddf9"; // String | Promotion unique identifier.
let opts = {
  'xVTEXCumulative': false, // Boolean | Defines if the Promotion is cumulative with other promotions.
  'xVTEXClusterOperator': "any", // String | This header allows implementing the Promotion in multiples client clusters. You can set the value as `all` - the Promotion will be valid to all the clusters - or `any` - the Promotion will be valid to any of the clusters.
  'xVTEXClusterExpression': "cluster_name=true", // String | Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them.
  'body': "/path/to/file" // File | 
};
apiInstance.apiRnbPvtImportCalculatorConfigurationPromotionIdPut(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, promotionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **xVTEXCalculatorName** | **String**| Promotion Name. | 
 **xVTEXStartDate** | **String**| Promotion start date. | 
 **xVTEXEndDate** | **String**| Promotion end date. | 
 **xVTEXAccumulateWithManualPrices** | **Boolean**| Condition that will accumulate the Promotion with manual prices or not. | 
 **promotionId** | **String**| Promotion unique identifier. | 
 **xVTEXCumulative** | **Boolean**| Defines if the Promotion is cumulative with other promotions. | [optional] 
 **xVTEXClusterOperator** | **String**| This header allows implementing the Promotion in multiples client clusters. You can set the value as &#x60;all&#x60; - the Promotion will be valid to all the clusters - or &#x60;any&#x60; - the Promotion will be valid to any of the clusters. | [optional] 
 **xVTEXClusterExpression** | **String**| Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them. | [optional] 
 **body** | **File**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: text/csv
- **Accept**: Not defined


## archivePromotion

> archivePromotion(contentType, accept, idCalculatorConfiguration)

Archive Promotion or Tax

Archives a Promotion or Tax by its ID.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let idCalculatorConfiguration = "d8a1cd2e-b667-4054-b3ae-b79124c7218e"; // String | Promotion ID or tax ID.
apiInstance.archivePromotion(contentType, accept, idCalculatorConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **idCalculatorConfiguration** | **String**| Promotion ID or tax ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createOrUpdateCalculatorConfiguration

> CreateOrUpdateCalculatorConfiguration200Response createOrUpdateCalculatorConfiguration(contentType, accept, createOrUpdateCalculatorConfigurationRequest)

Create or Update Promotion or Tax

Creates or updates a specific Promotion by its Promotion ID or a specific Tax by its Tax ID.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let createOrUpdateCalculatorConfigurationRequest = {"absoluteShippingDiscountValue":0,"accumulateWithManualPrice":false,"activateGiftsMultiplier":false,"activeDaysOfWeek":[],"affiliates":[],"applyToAllShippings":false,"areSalesChannelIdsExclusive":false,"beginDateUtc":"2020-05-01T18:47:15.89Z","brands":[],"brandsAreInclusive":false,"campaigns":[],"cardIssuers":[],"categories":[],"categoriesAreInclusive":false,"clusterExpressions":[],"collections":[],"collections1BuyTogether":[],"collections2BuyTogether":[],"collectionsIsInclusive":false,"compareListPriceAndPrice":false,"conditionsIds":["372e1868-2c0e-4437-be45-1ef8c9cab735"],"coupon":[],"cumulative":false,"daysAgoOfPurchases":0,"description":"Promotion for Social Seller","disableDeal":false,"discountType":"percentual","enableBuyTogetherPerSku":false,"firstBuyIsProfileOptimistic":false,"giftListTypes":[],"idCalculatorConfiguration":"d8a1cd2e-b667-4054-b3ae-b79124c7218e","idSellerIsInclusive":false,"idsSalesChannel":[],"installment":0,"isActive":true,"isArchived":false,"isDifferentListPriceAndPrice":false,"isFeatured":false,"isFirstBuy":false,"isMinMaxInstallments":false,"isSlaSelected":false,"itemMaxPrice":0,"itemMinPrice":0,"lastModified":"2021-09-17T18:13:16.2896414Z","listSku1BuyTogether":[],"listSku2BuyTogether":[],"marketingTags":[],"marketingTagsAreNotInclusive":false,"maxInstallment":0,"maxNumberOfAffectedItems":0,"maxNumberOfAffectedItemsGroupKey":"perCart","maxPricesPerItems":[],"maxUsage":0,"maxUsagePerClient":0,"maximumUnitPriceDiscount":0,"merchants":[],"minInstallment":0,"minimumQuantityBuyTogether":0,"multipleUsePerClient":false,"name":"Promoção Social Seller","newOffset":-3,"nominalDiscountValue":0,"nominalRewardValue":0,"nominalShippingDiscountValue":0,"nominalTax":0,"offset":-3,"orderStatusRewardValue":"invoiced","origin":"marketplace","paymentsMethods":[],"paymentsRules":[],"percentualDiscountValue":10,"percentualDiscountValueList":[],"percentualDiscountValueList1":0,"percentualDiscountValueList2":0,"percentualRewardValue":0,"percentualShippingDiscountValue":0,"percentualTax":0,"products":[],"productsAreInclusive":false,"productsSpecifications":[],"quantityToAffectBuyTogether":0,"rebatePercentualDiscountValue":0,"restrictionsBins":[],"shippingPercentualTax":0,"shouldDistributeDiscountAmongMatchedItems":false,"skus":[],"skusAreInclusive":true,"skusGift":{"quantitySelectable":0},"slasIds":[],"stores":[],"storesAreInclusive":false,"totalValueCeling":0,"totalValueFloor":0,"totalValueIncludeAllItems":false,"totalValueMode":"IncludeMatchedItems","totalValuePurchase":0,"type":"regular","useNewProgressiveAlgorithm":false,"utmCampaign":"georgeTest","utmSource":"georgeSource","zipCodeRanges":[]}; // CreateOrUpdateCalculatorConfigurationRequest | 
apiInstance.createOrUpdateCalculatorConfiguration(contentType, accept, createOrUpdateCalculatorConfigurationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **createOrUpdateCalculatorConfigurationRequest** | [**CreateOrUpdateCalculatorConfigurationRequest**](CreateOrUpdateCalculatorConfigurationRequest.md)|  | 

### Return type

[**CreateOrUpdateCalculatorConfiguration200Response**](CreateOrUpdateCalculatorConfiguration200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAllBenefits

> GetAllBenefits200Response getAllBenefits(contentType, accept)

Get All Promotions

Retrieves all promotions from an account.     &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Promotions and is organized by focusing on the developer&#39;s journey.    

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getAllBenefits(contentType, accept, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**GetAllBenefits200Response**](GetAllBenefits200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllTaxes

> GetAllTaxes200Response getAllTaxes(contentType, accept)

Get All Taxes

Retrieves all taxes from an account.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getAllTaxes(contentType, accept, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**GetAllTaxes200Response**](GetAllTaxes200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArchivedPromotions

> GetArchivedPromotions200Response getArchivedPromotions(contentType, accept)

List Archived Promotions

Lists all archived promotions.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getArchivedPromotions(contentType, accept, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**GetArchivedPromotions200Response**](GetArchivedPromotions200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArchivedTaxes

> GetArchivedTaxes200Response getArchivedTaxes(contentType, accept)

List Archived Taxes

Lists all archived taxes.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getArchivedTaxes(contentType, accept, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**GetArchivedTaxes200Response**](GetArchivedTaxes200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCalculatorConfigurationById

> GetCalculatorConfigurationById200Response getCalculatorConfigurationById(contentType, accept, idCalculatorConfiguration)

Get Promotion or Tax by ID

Retrieves a specific promotion by its Promotion ID or a specific tax by its Tax ID.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let idCalculatorConfiguration = "d8a1cd2e-b667-4054-b3ae-b79124c7218e"; // String | Promotion ID or tax ID.
apiInstance.getCalculatorConfigurationById(contentType, accept, idCalculatorConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **idCalculatorConfiguration** | **String**| Promotion ID or tax ID. | 

### Return type

[**GetCalculatorConfigurationById200Response**](GetCalculatorConfigurationById200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Promotion, Tax


## unarchivePromotion

> unarchivePromotion(contentType, accept, idCalculatorConfiguration)

Unarchive Promotion or Tax

Unarchives a Promotion or Tax by its ID.

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PromotionsTaxesApi.PromotionsAndTaxesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let idCalculatorConfiguration = "d8a1cd2e-b667-4054-b3ae-b79124c7218e"; // String | Promotion ID or tax ID.
apiInstance.unarchivePromotion(contentType, accept, idCalculatorConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **idCalculatorConfiguration** | **String**| Promotion ID or tax ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

