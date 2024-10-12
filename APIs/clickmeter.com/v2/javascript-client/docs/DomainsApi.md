# ClickMeterApi.DomainsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainsCount**](DomainsApi.md#domainsCount) | **GET** /domains/count | Retrieve count of domains
[**domainsDelete**](DomainsApi.md#domainsDelete) | **DELETE** /domains/{id} | Delete a domain
[**domainsGet**](DomainsApi.md#domainsGet) | **GET** /domains | Retrieve a list of domains
[**domainsIdGet**](DomainsApi.md#domainsIdGet) | **GET** /domains/{id} | Get a domain
[**domainsPut**](DomainsApi.md#domainsPut) | **POST** /domains | Create a domain
[**domainsUpdate**](DomainsApi.md#domainsUpdate) | **POST** /domains/{id} | Update a domain



## domainsCount

> ApiCoreResponsesCountResponce domainsCount(opts)

Retrieve count of domains

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DomainsApi();
let opts = {
  'type': "'system'", // String | Type of domain (\"system\"/\"go\"/\"personal\"/\"dedicated\"). If not specified default is \"system\"
  'name': "name_example" // String | Filter domains with this anmen
};
apiInstance.domainsCount(opts, (error, data, response) => {
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
 **type** | **String**| Type of domain (\&quot;system\&quot;/\&quot;go\&quot;/\&quot;personal\&quot;/\&quot;dedicated\&quot;). If not specified default is \&quot;system\&quot; | [optional] [default to &#39;system&#39;]
 **name** | **String**| Filter domains with this anmen | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## domainsDelete

> ApiCoreResponsesEntityUriSystemInt64 domainsDelete(id)

Delete a domain

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DomainsApi();
let id = 789; // Number | Id of domain
apiInstance.domainsDelete(id, (error, data, response) => {
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
 **id** | **Number**| Id of domain | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## domainsGet

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 domainsGet(opts)

Retrieve a list of domains

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DomainsApi();
let opts = {
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'type': "'system'", // String | Type of domain (\"system\"/\"go\"/\"personal\"/\"dedicated\"). If not specified default is \"system\"
  'name': "name_example" // String | Filter domains with this anmen
};
apiInstance.domainsGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **type** | **String**| Type of domain (\&quot;system\&quot;/\&quot;go\&quot;/\&quot;personal\&quot;/\&quot;dedicated\&quot;). If not specified default is \&quot;system\&quot; | [optional] [default to &#39;system&#39;]
 **name** | **String**| Filter domains with this anmen | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## domainsIdGet

> ApiCoreDtoDomainsDomain domainsIdGet(id)

Get a domain

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DomainsApi();
let id = 789; // Number | Id of domain
apiInstance.domainsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of domain | 

### Return type

[**ApiCoreDtoDomainsDomain**](ApiCoreDtoDomainsDomain.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## domainsPut

> ApiCoreResponsesEntityUriSystemInt64 domainsPut(apiCoreDtoDomainsDomain)

Create a domain

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DomainsApi();
let apiCoreDtoDomainsDomain = new ClickMeterApi.ApiCoreDtoDomainsDomain(); // ApiCoreDtoDomainsDomain | The domain to create
apiInstance.domainsPut(apiCoreDtoDomainsDomain, (error, data, response) => {
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
 **apiCoreDtoDomainsDomain** | [**ApiCoreDtoDomainsDomain**](ApiCoreDtoDomainsDomain.md)| The domain to create | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## domainsUpdate

> ApiCoreResponsesEntityUriSystemInt64 domainsUpdate(id, apiCoreDtoDomainsDomain)

Update a domain

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DomainsApi();
let id = 789; // Number | Id of domain
let apiCoreDtoDomainsDomain = new ClickMeterApi.ApiCoreDtoDomainsDomain(); // ApiCoreDtoDomainsDomain | The domain to update
apiInstance.domainsUpdate(id, apiCoreDtoDomainsDomain, (error, data, response) => {
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
 **id** | **Number**| Id of domain | 
 **apiCoreDtoDomainsDomain** | [**ApiCoreDtoDomainsDomain**](ApiCoreDtoDomainsDomain.md)| The domain to update | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

