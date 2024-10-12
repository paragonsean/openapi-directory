# OrgHunter.GeoLocationApi

All URIs are relative to *http://data.orghunter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CharitygeolocationPost**](GeoLocationApi.md#v1CharitygeolocationPost) | **POST** /v1/charitygeolocation | Get details!



## v1CharitygeolocationPost

> v1CharitygeolocationPost(opts)

Get details!

&lt;p&gt;This operation detail data.&lt;/p&gt;

### Example

```javascript
import OrgHunter from 'org_hunter';
let defaultClient = OrgHunter.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new OrgHunter.GeoLocationApi();
let opts = {
  'ein': "ein_example" // String | ein (Employer Identification Number)
};
apiInstance.v1CharitygeolocationPost(opts, (error, data, response) => {
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
 **ein** | **String**| ein (Employer Identification Number) | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

