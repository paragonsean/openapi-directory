# Suggestions.SKUApprovalSettingsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getaccountconfig**](SKUApprovalSettingsApi.md#getaccountconfig) | **GET** /suggestions/configuration | Get Account&#39;s Approval Settings
[**getautoApprovevaluefromconfig**](SKUApprovalSettingsApi.md#getautoApprovevaluefromconfig) | **GET** /suggestions/configuration/autoapproval/toggle | Get autoApprove Status in Account Settings
[**getselleraccountconfig**](SKUApprovalSettingsApi.md#getselleraccountconfig) | **GET** /suggestions/configuration/seller/{sellerId} | Get Seller&#39;s Approval Settings
[**putselleraccountconfig**](SKUApprovalSettingsApi.md#putselleraccountconfig) | **PUT** /suggestions/configuration/seller/{sellerId} | Save Seller&#39;s Approval Settings
[**saveaccountconfig**](SKUApprovalSettingsApi.md#saveaccountconfig) | **PUT** /suggestions/configuration | Save Account&#39;s Approval Settings
[**saveautoapproveforaccount**](SKUApprovalSettingsApi.md#saveautoapproveforaccount) | **PUT** /suggestions/configuration/autoapproval/toggle | Activate autoApprove in Marketplace&#39;s Account
[**saveautoapproveforaccountseller**](SKUApprovalSettingsApi.md#saveautoapproveforaccountseller) | **PUT** /suggestions/configuration/autoapproval/toggle/seller/{sellerId} | Activate autoApprove Setting for a Seller



## getaccountconfig

> Getaccountconfig200Response getaccountconfig(accountName, accept, contentType)

Get Account&#39;s Approval Settings

This endpoint retrieves the current approval settings of a marketplace&#39;s Received SKUs module. Its response includes:   - &#x60;Score&#x60;: Matcher scores for approving and rejecting SKUs received from sellers.   - &#x60;Matchers&#x60;: All Matchers configured on the marketplace, and their respective details.   - &#x60;SpecificationsMapping&#x60;: Mapping of product and SKU specifications, per seller.   - &#x60;MatchFlux&#x60;: This field determines the type of approval configuration applied to SKUs received from a seller.   The possible values include:   -&#x60;default&#x60;, where the Matcher reviews the SKU, and approves it based on its score.   -&#x60;manual&#x60;, for manual approvals through the Received SKU UI, or Match API.   -&#x60;autoApprove&#x60;, for every SKU received from a given seller to be approved automatically, regardless of their Matcher Score.

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.SKUApprovalSettingsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
apiInstance.getaccountconfig(accountName, accept, contentType, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

[**Getaccountconfig200Response**](Getaccountconfig200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getautoApprovevaluefromconfig

> GetautoApprovevaluefromconfig200Response getautoApprovevaluefromconfig(sellerId, accountName, accept, contentType)

Get autoApprove Status in Account Settings

This endpoint can be used to check whether the autoapprove setting is active or not, for a specific seller.   If the response is &#x60;true&#x60;, the autoapprove setting is active. If the response is &#x60;false&#x60;, it is inactive.

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.SKUApprovalSettingsApi();
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
apiInstance.getautoApprovevaluefromconfig(sellerId, accountName, accept, contentType, (error, data, response) => {
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
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

[**GetautoApprovevaluefromconfig200Response**](GetautoApprovevaluefromconfig200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getselleraccountconfig

> getselleraccountconfig(accountName, sellerId, accept, contentType)

Get Seller&#39;s Approval Settings

This endpoint retrieves the current Received SKUs approval settings applied to a specific seller. Its response includes:   - &#x60;sellerId&#x60;: A string that identifies the seller in the marketplace.   - &#x60;accountId&#x60;: Marketplace’s account ID.   - &#x60;accountName&#x60;: Marketplace’s account name.   - &#x60;mapping&#x60;: Mapping of SKU and product Specifications.   - &#x60;matchFlux&#x60;: This field determines the type of approval configuration applied to SKUs received  from a seller.   The possible values include:    -&#x60;default&#x60;, where the Matcher reviews the SKU, and approves it based on its score.   -&#x60;manual&#x60;, for manual approvals through the Received SKU UI and Match API.   -&#x60;autoApprove&#x60;, for every SKU received from a given seller to be approved automatically, regardless of the Matcher Score.

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.SKUApprovalSettingsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
apiInstance.getselleraccountconfig(accountName, sellerId, accept, contentType, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putselleraccountconfig

> putselleraccountconfig(accountName, sellerId, accept, contentType, putselleraccountconfigRequest)

Save Seller&#39;s Approval Settings

Marketplaces use this endpoint to create or update approval settings to a specific seller, on the Received SKUs module.   The request includes all the details necessary to implement the chosen approval settings.

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.SKUApprovalSettingsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let putselleraccountconfigRequest = {"mapping":null,"matchFlux":"Default","sellerId":"1a"}; // PutselleraccountconfigRequest | 
apiInstance.putselleraccountconfig(accountName, sellerId, accept, contentType, putselleraccountconfigRequest, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **putselleraccountconfigRequest** | [**PutselleraccountconfigRequest**](PutselleraccountconfigRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## saveaccountconfig

> Saveaccountconfig200Response saveaccountconfig(accountName, accept, contentType, saveaccountconfigRequest)

Save Account&#39;s Approval Settings

Marketplaces use this endpoint to create or update approval settings on their Received SKUs module.   The request includes all the details necessary to implement the chosen approval settings.

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.SKUApprovalSettingsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let saveaccountconfigRequest = new Suggestions.SaveaccountconfigRequest(); // SaveaccountconfigRequest | 
apiInstance.saveaccountconfig(accountName, accept, contentType, saveaccountconfigRequest, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **saveaccountconfigRequest** | [**SaveaccountconfigRequest**](SaveaccountconfigRequest.md)|  | 

### Return type

[**Saveaccountconfig200Response**](Saveaccountconfig200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveautoapproveforaccount

> Saveautoapproveforaccount200Response saveautoapproveforaccount(accountName, accept, contentType, saveautoapproveforaccountRequest)

Activate autoApprove in Marketplace&#39;s Account

This endpoint enables the autoapprove rule to a marketplace&#39;s whole Received SKUs module. Once enabling the rule, received SKUs will be automatically approved on your store, regardless of the seller.    For the autoapprove rule to work as expected, the approval [Matcher score](https://help.vtex.com/en/tutorial/entendendo-a-pontuacao-do-vtex-matcher--tutorials_424) should be set up as 80 (default value), but you can configure a different number through the field &#x60;Score&#x60; in [Save Account&#39;s Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/saveaccountconfig).

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.SKUApprovalSettingsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let saveautoapproveforaccountRequest = {"Enabled":true}; // SaveautoapproveforaccountRequest | 
apiInstance.saveautoapproveforaccount(accountName, accept, contentType, saveautoapproveforaccountRequest, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **saveautoapproveforaccountRequest** | [**SaveautoapproveforaccountRequest**](SaveautoapproveforaccountRequest.md)|  | 

### Return type

[**Saveautoapproveforaccount200Response**](Saveautoapproveforaccount200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveautoapproveforaccountseller

> saveautoapproveforaccountseller(accountName, sellerId, accept, contentType, saveautoapproveforaccountsellerRequest)

Activate autoApprove Setting for a Seller

This endpoint enables the auto approve setting to received SKUs from a specific seller. Be aware that once enabling the rule through this request, all received SKUs from that seller will be automatically approved on your store, regardless of the Matcher Score.

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.SKUApprovalSettingsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let saveautoapproveforaccountsellerRequest = {"Enabled":true}; // SaveautoapproveforaccountsellerRequest | 
apiInstance.saveautoapproveforaccountseller(accountName, sellerId, accept, contentType, saveautoapproveforaccountsellerRequest, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **saveautoapproveforaccountsellerRequest** | [**SaveautoapproveforaccountsellerRequest**](SaveautoapproveforaccountsellerRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

