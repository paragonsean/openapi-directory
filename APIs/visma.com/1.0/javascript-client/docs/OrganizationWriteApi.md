# SeveraPublicRestApiDocumentation.OrganizationWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizationDetailsPatchOrganizationDetails**](OrganizationWriteApi.md#organizationDetailsPatchOrganizationDetails) | **PATCH** /v1/organizationdetails | Update (Patch) a organization details or a part of it



## organizationDetailsPatchOrganizationDetails

> OrganizationDetailsOutputModel organizationDetailsPatchOrganizationDetails(opts)

Update (Patch) a organization details or a part of it

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.OrganizationWriteApi();
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | 
};
apiInstance.organizationDetailsPatchOrganizationDetails(opts, (error, data, response) => {
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
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)|  | [optional] 

### Return type

[**OrganizationDetailsOutputModel**](OrganizationDetailsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

