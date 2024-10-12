# SnykApi.LicensesApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listAllLicenses**](LicensesApi.md#listAllLicenses) | **POST** /org/{orgId}/licenses | List all licenses



## listAllLicenses

> ListAllLicenses200Response listAllLicenses(orgId, opts)

List all licenses



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.LicensesApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
let opts = {
  'sortBy': "license", // String | The field to sort results by.
  'order': "'asc'", // String | The direction to sort results by.
  'listAllLicensesRequest': new SnykApi.ListAllLicensesRequest() // ListAllLicensesRequest | 
};
apiInstance.listAllLicenses(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **sortBy** | **String**| The field to sort results by. | [optional] [default to &#39;license&#39;]
 **order** | **String**| The direction to sort results by. | [optional] [default to &#39;asc&#39;]
 **listAllLicensesRequest** | [**ListAllLicensesRequest**](ListAllLicensesRequest.md)|  | [optional] 

### Return type

[**ListAllLicenses200Response**](ListAllLicenses200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

