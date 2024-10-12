# CustomerLockbox.RequestsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestsGet**](RequestsApi.md#requestsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CustomerLockbox/requests/{requestId} | 
[**requestsList**](RequestsApi.md#requestsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CustomerLockbox/requests | 
[**requestsUpdateStatus**](RequestsApi.md#requestsUpdateStatus) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CustomerLockbox/requests/{requestId}/UpdateApproval | 



## requestsGet

> LockboxRequestResponse requestsGet(requestId, subscriptionId, apiVersion)



Get Customer Lockbox request

### Example

```javascript
import CustomerLockbox from 'customer_lockbox';
let defaultClient = CustomerLockbox.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerLockbox.RequestsApi();
let requestId = "requestId_example"; // String | The Lockbox request ID.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.requestsGet(requestId, subscriptionId, apiVersion, (error, data, response) => {
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
 **requestId** | **String**| The Lockbox request ID. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**LockboxRequestResponse**](LockboxRequestResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestsList

> RequestListResult requestsList(subscriptionId, opts)



Lists all of the Lockbox requests in the given subscription.

### Example

```javascript
import CustomerLockbox from 'customer_lockbox';
let defaultClient = CustomerLockbox.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerLockbox.RequestsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let opts = {
  'filter': "filter_example" // String | The $filter OData query parameter. Only filter by request status is supported, e.g $filter=properties/status eq 'Pending'
};
apiInstance.requestsList(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **filter** | **String**| The $filter OData query parameter. Only filter by request status is supported, e.g $filter&#x3D;properties/status eq &#39;Pending&#39; | [optional] 

### Return type

[**RequestListResult**](RequestListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestsUpdateStatus

> Approval requestsUpdateStatus(subscriptionId, requestId, apiVersion, approval)



Update Customer Lockbox request approval status API

### Example

```javascript
import CustomerLockbox from 'customer_lockbox';
let defaultClient = CustomerLockbox.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerLockbox.RequestsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let requestId = "requestId_example"; // String | The Lockbox request ID.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let approval = new CustomerLockbox.Approval(); // Approval | The approval object to update request status.
apiInstance.requestsUpdateStatus(subscriptionId, requestId, apiVersion, approval, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **requestId** | **String**| The Lockbox request ID. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **approval** | [**Approval**](Approval.md)| The approval object to update request status. | 

### Return type

[**Approval**](Approval.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

