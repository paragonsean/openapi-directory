# Suggestions.GetVersionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSuggestionbyversion**](GetVersionsApi.md#getSuggestionbyversion) | **GET** /suggestions/{sellerId}/{sellerskuid}/versions/{version} | Get Version by ID
[**getVersions**](GetVersionsApi.md#getVersions) | **GET** /suggestions/{sellerId}/{sellerskuid}/versions | Get all Versions



## getSuggestionbyversion

> getSuggestionbyversion(accountName, accept, contentType, sellerId, sellerskuid, version)

Get Version by ID

Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions.   This endpoint retrieves a specific *version* of a chosen SKU sent by the seller. Add the Seller&#39;s ID, Seller&#39;s SKU ID, and version ID in the path to detail your search.

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

let apiInstance = new Suggestions.GetVersionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let sellerskuid = "'1234'"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
let version = "'09072021142808277'"; // String | Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the `versionId` associated to the version you choose to search for. You can get this field's value through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the `latestVersionId` field.
apiInstance.getSuggestionbyversion(accountName, accept, contentType, sellerId, sellerskuid, version, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;seller123&#39;]
 **sellerskuid** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]
 **version** | **String**| Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the &#x60;versionId&#x60; associated to the version you choose to search for. You can get this field&#39;s value through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the &#x60;latestVersionId&#x60; field. | [default to &#39;09072021142808277&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVersions

> getVersions(accountName, accept, contentType, sellerId, sellerskuid)

Get all Versions

Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions.   This endpoint retrieves the data of *all* previous and latest versions of a specific SKU suggestion, sent by the seller. Whenever an SKU is updated, it is important to map previous versions, to compare and identify changes.   The response&#39;s object [latestversion] provides the information of the most recent version of that SKU suggestion.

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

let apiInstance = new Suggestions.GetVersionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let sellerskuid = "'1234'"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
apiInstance.getVersions(accountName, accept, contentType, sellerId, sellerskuid, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;seller123&#39;]
 **sellerskuid** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

