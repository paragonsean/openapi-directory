# ConfigCatPublicManagementApi.OrganizationsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizations**](OrganizationsApi.md#getOrganizations) | **GET** /v1/organizations | List Organizations



## getOrganizations

> [OrganizationModelHaljson] getOrganizations()

List Organizations

This endpoint returns the list of the Organizations that belongs to the user.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.OrganizationsApi();
apiInstance.getOrganizations((error, data, response) => {
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

[**[OrganizationModelHaljson]**](OrganizationModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json

