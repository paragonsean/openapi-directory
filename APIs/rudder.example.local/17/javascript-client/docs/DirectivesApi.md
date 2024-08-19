# RudderApi.DirectivesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkDirective**](DirectivesApi.md#checkDirective) | **POST** /directives/{directiveId}/check | Check that update on a directive is valid
[**createDirective**](DirectivesApi.md#createDirective) | **PUT** /directives | Create a directive
[**deleteDirective**](DirectivesApi.md#deleteDirective) | **DELETE** /directives/{directiveId} | Delete a directive
[**directiveDetails**](DirectivesApi.md#directiveDetails) | **GET** /directives/{directiveId} | Get directive details
[**listDirectives**](DirectivesApi.md#listDirectives) | **GET** /directives | List all directives
[**updateDirective**](DirectivesApi.md#updateDirective) | **POST** /directives/{directiveId} | Update a directive details



## checkDirective

> CheckDirective200Response checkDirective(directiveId, directive)

Check that update on a directive is valid

Check that update on a directive is valid

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DirectivesApi();
let directiveId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the directive
let directive = new RudderApi.Directive(); // Directive | 
apiInstance.checkDirective(directiveId, directive, (error, data, response) => {
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
 **directiveId** | **String**| Id of the directive | 
 **directive** | [**Directive**](Directive.md)|  | 

### Return type

[**CheckDirective200Response**](CheckDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDirective

> CreateDirective200Response createDirective(opts)

Create a directive

Create a new directive from provided parameters. You can specify a source directive to clone it.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DirectivesApi();
let opts = {
  'directiveNew': new RudderApi.DirectiveNew() // DirectiveNew | 
};
apiInstance.createDirective(opts, (error, data, response) => {
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
 **directiveNew** | [**DirectiveNew**](DirectiveNew.md)|  | [optional] 

### Return type

[**CreateDirective200Response**](CreateDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDirective

> DeleteDirective200Response deleteDirective(directiveId)

Delete a directive

Delete a directive

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DirectivesApi();
let directiveId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the directive
apiInstance.deleteDirective(directiveId, (error, data, response) => {
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
 **directiveId** | **String**| Id of the directive | 

### Return type

[**DeleteDirective200Response**](DeleteDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## directiveDetails

> DirectiveDetails200Response directiveDetails(directiveId)

Get directive details

Get all information about a given directive

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DirectivesApi();
let directiveId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the directive
apiInstance.directiveDetails(directiveId, (error, data, response) => {
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
 **directiveId** | **String**| Id of the directive | 

### Return type

[**DirectiveDetails200Response**](DirectiveDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDirectives

> ListDirectives200Response listDirectives()

List all directives

List all directives

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DirectivesApi();
apiInstance.listDirectives((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDirectives200Response**](ListDirectives200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDirective

> UpdateDirective200Response updateDirective(directiveId, directive)

Update a directive details

Update directive information

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.DirectivesApi();
let directiveId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the directive
let directive = new RudderApi.Directive(); // Directive | 
apiInstance.updateDirective(directiveId, directive, (error, data, response) => {
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
 **directiveId** | **String**| Id of the directive | 
 **directive** | [**Directive**](Directive.md)|  | 

### Return type

[**UpdateDirective200Response**](UpdateDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

