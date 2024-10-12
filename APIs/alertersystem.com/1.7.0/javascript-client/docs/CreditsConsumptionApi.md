# AlerterSystemApi.CreditsConsumptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCreditsConsumptionGetCollection**](CreditsConsumptionApi.md#apiCreditsConsumptionGetCollection) | **GET** /api/credits-consumption | Retrieves the collection of CreditsConsumption resources.
[**apiCreditsConsumptionIdGet**](CreditsConsumptionApi.md#apiCreditsConsumptionIdGet) | **GET** /api/credits-consumption/{id} | Retrieves a CreditsConsumption resource.



## apiCreditsConsumptionGetCollection

> [CreditsConsumptionGet] apiCreditsConsumptionGetCollection(opts)

Retrieves the collection of CreditsConsumption resources.

Retrieves the collection of CreditsConsumption resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.CreditsConsumptionApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiCreditsConsumptionGetCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] [default to 1]
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[CreditsConsumptionGet]**](CreditsConsumptionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiCreditsConsumptionIdGet

> CreditsConsumptionGet apiCreditsConsumptionIdGet(id)

Retrieves a CreditsConsumption resource.

Retrieves a CreditsConsumption resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.CreditsConsumptionApi();
let id = "id_example"; // String | CreditsConsumption identifier
apiInstance.apiCreditsConsumptionIdGet(id, (error, data, response) => {
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
 **id** | **String**| CreditsConsumption identifier | 

### Return type

[**CreditsConsumptionGet**](CreditsConsumptionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

