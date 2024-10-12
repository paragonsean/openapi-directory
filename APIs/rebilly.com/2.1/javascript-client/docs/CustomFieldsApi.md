# RebillyRestApi.CustomFieldsApi

All URIs are relative to *https://api-sandbox.rebilly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCustomField**](CustomFieldsApi.md#getCustomField) | **GET** /custom-fields/{resource}/{name} | Retrieve a Custom Field
[**getCustomFieldCollection**](CustomFieldsApi.md#getCustomFieldCollection) | **GET** /custom-fields/{resource} | Retrieve Custom Fields
[**putCustomField**](CustomFieldsApi.md#putCustomField) | **PUT** /custom-fields/{resource}/{name} | Create or alter a Custom Field



## getCustomField

> CustomField getCustomField(resource, name, opts)

Retrieve a Custom Field

Retrieve a schema of the given Custom Field for the given resource type. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.CustomFieldsApi();
let resource = "resource_example"; // String | The resource type string.
let name = "name_example"; // String | The custom field's identifier string.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.getCustomField(resource, name, opts, (error, data, response) => {
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
 **resource** | **String**| The resource type string. | 
 **name** | **String**| The custom field&#39;s identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomFieldCollection

> [CustomField] getCustomFieldCollection(resource, opts)

Retrieve Custom Fields

Retrieve a schema of Custom Fields for the given resource type. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.CustomFieldsApi();
let resource = "resource_example"; // String | The resource type string.
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'limit': 56, // Number | The collection items limit.
  'offset': 56 // Number | The collection items offset.
};
apiInstance.getCustomFieldCollection(resource, opts, (error, data, response) => {
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
 **resource** | **String**| The resource type string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **limit** | **Number**| The collection items limit. | [optional] 
 **offset** | **Number**| The collection items offset. | [optional] 

### Return type

[**[CustomField]**](CustomField.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putCustomField

> CustomField putCustomField(resource, name, customField, opts)

Create or alter a Custom Field

Create or alter a schema of the given Custom Field for the given resource. type. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.CustomFieldsApi();
let resource = "resource_example"; // String | The resource type string.
let name = "name_example"; // String | The custom field's identifier string.
let customField = new RebillyRestApi.CustomField(); // CustomField | Custom Fields schema of the given resource type.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.putCustomField(resource, name, customField, opts, (error, data, response) => {
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
 **resource** | **String**| The resource type string. | 
 **name** | **String**| The custom field&#39;s identifier string. | 
 **customField** | [**CustomField**](CustomField.md)| Custom Fields schema of the given resource type. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

