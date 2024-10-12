# SecurityCenter.InformationProtectionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**informationProtectionPoliciesCreateOrUpdate**](InformationProtectionPoliciesApi.md#informationProtectionPoliciesCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName} | 
[**informationProtectionPoliciesGet**](InformationProtectionPoliciesApi.md#informationProtectionPoliciesGet) | **GET** /{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName} | 
[**informationProtectionPoliciesList**](InformationProtectionPoliciesApi.md#informationProtectionPoliciesList) | **GET** /{scope}/providers/Microsoft.Security/informationProtectionPolicies | 



## informationProtectionPoliciesCreateOrUpdate

> InformationProtectionPolicy informationProtectionPoliciesCreateOrUpdate(apiVersion, scope, informationProtectionPolicyName)



Details of the information protection policy.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.InformationProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
let informationProtectionPolicyName = "informationProtectionPolicyName_example"; // String | Name of the information protection policy.
apiInstance.informationProtectionPoliciesCreateOrUpdate(apiVersion, scope, informationProtectionPolicyName, (error, data, response) => {
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
 **informationProtectionPolicyName** | **String**| Name of the information protection policy. | 

### Return type

[**InformationProtectionPolicy**](InformationProtectionPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## informationProtectionPoliciesGet

> InformationProtectionPolicy informationProtectionPoliciesGet(apiVersion, scope, informationProtectionPolicyName)



Details of the information protection policy.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.InformationProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
let informationProtectionPolicyName = "informationProtectionPolicyName_example"; // String | Name of the information protection policy.
apiInstance.informationProtectionPoliciesGet(apiVersion, scope, informationProtectionPolicyName, (error, data, response) => {
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
 **informationProtectionPolicyName** | **String**| Name of the information protection policy. | 

### Return type

[**InformationProtectionPolicy**](InformationProtectionPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## informationProtectionPoliciesList

> InformationProtectionPolicyList informationProtectionPoliciesList(apiVersion, scope)



Information protection policies of a specific management group.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.InformationProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
apiInstance.informationProtectionPoliciesList(apiVersion, scope, (error, data, response) => {
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

[**InformationProtectionPolicyList**](InformationProtectionPolicyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

