# VestorlyApi.AdvisorsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findAdvisorByID**](AdvisorsApi.md#findAdvisorByID) | **GET** /advisors/{id} | 



## findAdvisorByID

> Advisor findAdvisorByID(vestorlyAuth, id, opts)



Returns a single advisor given their ID

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.AdvisorsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Advisor Id to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findAdvisorByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| Advisor Id to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Advisor**](Advisor.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

