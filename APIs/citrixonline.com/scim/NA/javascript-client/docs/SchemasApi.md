# Scim.SchemasApi

All URIs are relative to *https://api.citrixonline.com/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getServiceProviderConfigs**](SchemasApi.md#getServiceProviderConfigs) | **GET** /ServiceProviderConfigs | Get Service Provider Configurations
[**getUserSchema**](SchemasApi.md#getUserSchema) | **GET** /Schemas/Users | Get User Schema



## getServiceProviderConfigs

> ServiceProviderConfigs getServiceProviderConfigs(authorization)

Get Service Provider Configurations

Queries service provider configurations. The service provider configurations are defined in SCIM Core Schema (http://www.simplecloud.info/specs/draft-scim-core-schema-01.html#anchor6). This call returns a description, a documentationURL, name, and specURL.

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.SchemasApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
apiInstance.getServiceProviderConfigs(authorization, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 

### Return type

[**ServiceProviderConfigs**](ServiceProviderConfigs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserSchema

> ResourceSchema getUserSchema(authorization)

Get User Schema

Queries the user schema. The user schema is defined in SCIM Core Schema (http://www.simplecloud.info/specs/draft-scim-core-schema-01.html#resource-schema).

### Example

```javascript
import Scim from 'scim';

let apiInstance = new Scim.SchemasApi();
let authorization = "authorization_example"; // String | Access token prefixed with 'Bearer ', e.g. 'Bearer 123456abcdef'
apiInstance.getUserSchema(authorization, (error, data, response) => {
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
 **authorization** | **String**| Access token prefixed with &#39;Bearer &#39;, e.g. &#39;Bearer 123456abcdef&#39; | 

### Return type

[**ResourceSchema**](ResourceSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

