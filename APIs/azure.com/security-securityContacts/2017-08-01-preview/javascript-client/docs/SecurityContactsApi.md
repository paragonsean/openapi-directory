# SecurityCenter.SecurityContactsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securityContactsCreate**](SecurityContactsApi.md#securityContactsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} | 
[**securityContactsDelete**](SecurityContactsApi.md#securityContactsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} | 
[**securityContactsGet**](SecurityContactsApi.md#securityContactsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} | 
[**securityContactsList**](SecurityContactsApi.md#securityContactsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts | 
[**securityContactsUpdate**](SecurityContactsApi.md#securityContactsUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName} | 



## securityContactsCreate

> SecurityContact securityContactsCreate(apiVersion, subscriptionId, securityContactName, securityContact)



Security contact configurations for the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SecurityContactsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let securityContactName = "securityContactName_example"; // String | Name of the security contact object
let securityContact = new SecurityCenter.SecurityContact(); // SecurityContact | Security contact object
apiInstance.securityContactsCreate(apiVersion, subscriptionId, securityContactName, securityContact, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **securityContactName** | **String**| Name of the security contact object | 
 **securityContact** | [**SecurityContact**](SecurityContact.md)| Security contact object | 

### Return type

[**SecurityContact**](SecurityContact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## securityContactsDelete

> securityContactsDelete(apiVersion, subscriptionId, securityContactName)



Security contact configurations for the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SecurityContactsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let securityContactName = "securityContactName_example"; // String | Name of the security contact object
apiInstance.securityContactsDelete(apiVersion, subscriptionId, securityContactName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **securityContactName** | **String**| Name of the security contact object | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## securityContactsGet

> SecurityContact securityContactsGet(apiVersion, subscriptionId, securityContactName)



Security contact configurations for the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SecurityContactsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let securityContactName = "securityContactName_example"; // String | Name of the security contact object
apiInstance.securityContactsGet(apiVersion, subscriptionId, securityContactName, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **securityContactName** | **String**| Name of the security contact object | 

### Return type

[**SecurityContact**](SecurityContact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## securityContactsList

> SecurityContactList securityContactsList(apiVersion, subscriptionId)



Security contact configurations for the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SecurityContactsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.securityContactsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 

### Return type

[**SecurityContactList**](SecurityContactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## securityContactsUpdate

> SecurityContact securityContactsUpdate(apiVersion, subscriptionId, securityContactName, securityContact)



Security contact configurations for the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SecurityContactsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let securityContactName = "securityContactName_example"; // String | Name of the security contact object
let securityContact = new SecurityCenter.SecurityContact(); // SecurityContact | Security contact object
apiInstance.securityContactsUpdate(apiVersion, subscriptionId, securityContactName, securityContact, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **securityContactName** | **String**| Name of the security contact object | 
 **securityContact** | [**SecurityContact**](SecurityContact.md)| Security contact object | 

### Return type

[**SecurityContact**](SecurityContact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

