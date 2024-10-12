# SecurityCenter.ComplianceResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complianceResultsGet**](ComplianceResultsApi.md#complianceResultsGet) | **GET** /{resourceId}/providers/Microsoft.Security/complianceResults/{complianceResultName} | 
[**complianceResultsList**](ComplianceResultsApi.md#complianceResultsList) | **GET** /{scope}/providers/Microsoft.Security/complianceResults | 



## complianceResultsGet

> ComplianceResult complianceResultsGet(apiVersion, resourceId, complianceResultName)



Security Compliance Result

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ComplianceResultsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let resourceId = "resourceId_example"; // String | The identifier of the resource.
let complianceResultName = "complianceResultName_example"; // String | name of the desired assessment compliance result
apiInstance.complianceResultsGet(apiVersion, resourceId, complianceResultName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **resourceId** | **String**| The identifier of the resource. | 
 **complianceResultName** | **String**| name of the desired assessment compliance result | 

### Return type

[**ComplianceResult**](ComplianceResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## complianceResultsList

> ComplianceResultList complianceResultsList(apiVersion, scope)



Security compliance results in the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ComplianceResultsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
apiInstance.complianceResultsList(apiVersion, scope, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **scope** | **String**| Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName). | 

### Return type

[**ComplianceResultList**](ComplianceResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

