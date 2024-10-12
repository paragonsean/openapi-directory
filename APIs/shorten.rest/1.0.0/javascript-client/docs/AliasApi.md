# ShortenRestApiDocumentation.AliasApi

All URIs are relative to *https://api.shorten.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAlias**](AliasApi.md#createAlias) | **POST** /aliases | Create alias
[**deleteAlias**](AliasApi.md#deleteAlias) | **DELETE** /aliases | Delete alias
[**getAlias**](AliasApi.md#getAlias) | **GET** /aliases | Get alias
[**getAliases**](AliasApi.md#getAliases) | **GET** /aliases/all | Get aliases by domain
[**updateAlias**](AliasApi.md#updateAlias) | **PUT** /aliases | Update alias



## createAlias

> CreateAliasResponseModel createAlias(createAliasModel, opts)

Create alias

This POST method creates a new alias under a specified domain. If no domain is specified in the request the alias will be attached to the default domain Short.fyi    **NOTE:** You can override the domain level Meta Tags and Tracking Snippets by specifying them for each URL. Any variables you add to a specific URL will always override domain level settings.

### Example

```javascript
import ShortenRestApiDocumentation from 'shorten_rest_api_documentation';
let defaultClient = ShortenRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ShortenRestApiDocumentation.AliasApi();
let createAliasModel = new ShortenRestApiDocumentation.CreateAliasModel(); // CreateAliasModel | alias properties
let opts = {
  'domainName': "your.domain.com", // String | domain which alias will belong to (string without `http/https` or `/`)
  'aliasName': "aBcDe012" // String | alias (without `/` at the beginning)
};
apiInstance.createAlias(createAliasModel, opts, (error, data, response) => {
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
 **createAliasModel** | [**CreateAliasModel**](CreateAliasModel.md)| alias properties | 
 **domainName** | **String**| domain which alias will belong to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to &#39;short.fyi&#39;]
 **aliasName** | **String**| alias (without &#x60;/&#x60; at the beginning) | [optional] [default to &#39;@rnd&#39;]

### Return type

[**CreateAliasResponseModel**](CreateAliasResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAlias

> deleteAlias(aliasName, opts)

Delete alias

Deletes a single alias by providing alias and domain. If no domain is provided the API will search for the matching alias within the Short.fyi domain

### Example

```javascript
import ShortenRestApiDocumentation from 'shorten_rest_api_documentation';
let defaultClient = ShortenRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ShortenRestApiDocumentation.AliasApi();
let aliasName = "aBcDe012"; // String | alias (without `/` at the beginning)
let opts = {
  'domainName': "your.domain.com" // String | domain which alias belongs to (string without `http/https` or `/`)
};
apiInstance.deleteAlias(aliasName, opts, (error, data, response) => {
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
 **aliasName** | **String**| alias (without &#x60;/&#x60; at the beginning) | 
 **domainName** | **String**| domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to &#39;short.fyi&#39;]

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAlias

> AliasModel getAlias(aliasName, opts)

Get alias

Get detailed information for a single alias by providing its alias and domain name

### Example

```javascript
import ShortenRestApiDocumentation from 'shorten_rest_api_documentation';
let defaultClient = ShortenRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ShortenRestApiDocumentation.AliasApi();
let aliasName = "aBcDe012"; // String | alias value (without `/` at the beginning)
let opts = {
  'domainName': "your.domain.com" // String | domain which alias belongs to (string without `http/https` or `/`)
};
apiInstance.getAlias(aliasName, opts, (error, data, response) => {
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
 **aliasName** | **String**| alias value (without &#x60;/&#x60; at the beginning) | 
 **domainName** | **String**| domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to &#39;short.fyi&#39;]

### Return type

[**AliasModel**](AliasModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAliases

> GetAliasesModel getAliases(opts)

Get aliases by domain

Obtain a list of all alias names associated with your account and given domain. Result array is in descending order by creation date.    If no domain is specified you will receive a list of all the alias names you have created using the Short.fyi domain.    If there are more results than the limit for the request the response will return you a value in lastId property you can specify it in the continueFrom query parameter to get the next batch of records.

### Example

```javascript
import ShortenRestApiDocumentation from 'shorten_rest_api_documentation';
let defaultClient = ShortenRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ShortenRestApiDocumentation.AliasApi();
let opts = {
  'domainName': "your.domain.com", // String | The domain name to get the aliases for (string without `http/https` or `/`)
  'continueFrom': "1588788835614657618", // String | An ID returned by a previous query to continue aliases retrieval (see lastId in response)
  'limit': 100 // Number | Number of results to return per request
};
apiInstance.getAliases(opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name to get the aliases for (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to &#39;short.fyi&#39;]
 **continueFrom** | **String**| An ID returned by a previous query to continue aliases retrieval (see lastId in response) | [optional] 
 **limit** | **Number**| Number of results to return per request | [optional] [default to 1000]

### Return type

[**GetAliasesModel**](GetAliasesModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAlias

> updateAlias(aliasName, createAliasModel, opts)

Update alias

Update a single short URL by providing its alias and domain as a parameter, and the data you wish to update in the body of the request. If no domain is provided you will receive the alias found attached to the Short.fyi domain (if it exists and is linked to your account!)   ### NOTE:    ( * )If you add a metatag or a snippet with a same name to an alias and the domain it&#39;s related to, the value will be taken from the alias and not the domain    ( ** ) When you update any array property (like destinations) the block is updated **completely** so you have to specify the old records to avoid deleting them   ( *** ) The method updates only the specified properties so if there was no change in one of them you don&#39;t have to send it.

### Example

```javascript
import ShortenRestApiDocumentation from 'shorten_rest_api_documentation';
let defaultClient = ShortenRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ShortenRestApiDocumentation.AliasApi();
let aliasName = "aBcDe012"; // String | alias (without `/` at the beginning)
let createAliasModel = new ShortenRestApiDocumentation.CreateAliasModel(); // CreateAliasModel | alias properties you wish to be updated
let opts = {
  'domainName': "your.domain.com" // String | domain which alias belongs to (string without `http/https` or `/`)
};
apiInstance.updateAlias(aliasName, createAliasModel, opts, (error, data, response) => {
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
 **aliasName** | **String**| alias (without &#x60;/&#x60; at the beginning) | 
 **createAliasModel** | [**CreateAliasModel**](CreateAliasModel.md)| alias properties you wish to be updated | 
 **domainName** | **String**| domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to &#39;short.fyi&#39;]

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

