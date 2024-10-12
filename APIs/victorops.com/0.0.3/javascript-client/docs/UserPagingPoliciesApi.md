# VictorOps.UserPagingPoliciesApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1UserUserPoliciesGet**](UserPagingPoliciesApi.md#apiPublicV1UserUserPoliciesGet) | **GET** /api-public/v1/user/{user}/policies | Get a list of paging policies for a user



## apiPublicV1UserUserPoliciesGet

> Policies apiPublicV1UserUserPoliciesGet(xVOApiId, xVOApiKey, user)

Get a list of paging policies for a user

Get paging policies for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserPagingPoliciesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
apiInstance.apiPublicV1UserUserPoliciesGet(xVOApiId, xVOApiKey, user, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 

### Return type

[**Policies**](Policies.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

