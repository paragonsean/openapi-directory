# SecurityCenter.LocationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsGet**](LocationsApi.md#locationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation} | 
[**locationsList**](LocationsApi.md#locationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations | 



## locationsGet

> AscLocation locationsGet(apiVersion, subscriptionId, ascLocation)



Details of a specific location

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.LocationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
apiInstance.locationsGet(apiVersion, subscriptionId, ascLocation, (error, data, response) => {
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
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 

### Return type

[**AscLocation**](AscLocation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsList

> AscLocationList locationsList(apiVersion, subscriptionId)



The location of the responsible ASC of the specific subscription (home region). For each subscription there is only one responsible location. The location in the response should be used to read or write other resources in ASC according to their ID.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.LocationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.locationsList(apiVersion, subscriptionId, (error, data, response) => {
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

[**AscLocationList**](AscLocationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

