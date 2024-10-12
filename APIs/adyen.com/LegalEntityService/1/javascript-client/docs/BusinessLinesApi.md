# LegalEntityManagementApi.BusinessLinesApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteBusinessLinesId**](BusinessLinesApi.md#deleteBusinessLinesId) | **DELETE** /businessLines/{id} | Delete a business line
[**getBusinessLinesId**](BusinessLinesApi.md#getBusinessLinesId) | **GET** /businessLines/{id} | Get a business line
[**postBusinessLines**](BusinessLinesApi.md#postBusinessLines) | **POST** /businessLines | Create a business line



## deleteBusinessLinesId

> deleteBusinessLinesId(id)

Delete a business line

Deletes a business line.   &gt;If you delete a business line linked to a [payment method](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api), it can affect your merchant account&#39;s ability to use the [payment method](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings). The business line is removed from all linked merchant accounts.

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.BusinessLinesApi();
let id = "id_example"; // String | The unique identifier of the business line to be deleted.
apiInstance.deleteBusinessLinesId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the business line to be deleted. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBusinessLinesId

> BusinessLine getBusinessLinesId(id)

Get a business line

Returns the detail of a business line.

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.BusinessLinesApi();
let id = "id_example"; // String | The unique identifier of the business line.
apiInstance.getBusinessLinesId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the business line. | 

### Return type

[**BusinessLine**](BusinessLine.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postBusinessLines

> BusinessLine postBusinessLines(opts)

Create a business line

Creates a business line.   This resource contains information about your user&#39;s line of business, including their industry and their source of funds. Adyen uses this information to verify your users as required by payment industry regulations. Adyen informs you of the verification results through webhooks or API responses.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.BusinessLinesApi();
let opts = {
  'businessLineInfo': new LegalEntityManagementApi.BusinessLineInfo() // BusinessLineInfo | 
};
apiInstance.postBusinessLines(opts, (error, data, response) => {
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
 **businessLineInfo** | [**BusinessLineInfo**](BusinessLineInfo.md)|  | [optional] 

### Return type

[**BusinessLine**](BusinessLine.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

