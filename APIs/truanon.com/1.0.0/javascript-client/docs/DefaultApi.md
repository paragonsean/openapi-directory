# TruAnonPrivateApi.DefaultApi

All URIs are relative to *https://staging.truanon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProfile**](DefaultApi.md#getProfile) | **GET** /api/get_profile | Get Profile
[**getToken**](DefaultApi.md#getToken) | **GET** /api/request_token | Get Token



## getProfile

> getProfile(opts)

Get Profile

get_profile Private API: Request confirmed profile data for your unique member ID

### Example

```javascript
import TruAnonPrivateApi from 'tru_anon_private_api';

let apiInstance = new TruAnonPrivateApi.DefaultApi();
let opts = {
  'id': "{{your-member-id}}", // String | This is your unique username or member ID
  'service': "{{service-identifier}}" // String | The service name given to you by TruAnon
};
apiInstance.getProfile(opts, (error, data, response) => {
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
 **id** | **String**| This is your unique username or member ID | [optional] 
 **service** | **String**| The service name given to you by TruAnon | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getToken

> getToken(opts)

Get Token

request_token Private API: Request a Proof token to let the member confirm in a popup interface          {\&quot;id\&quot;:\&quot;qjgblv72bzzio\&quot;,\&quot;type\&quot;:\&quot;Proof\&quot;,\&quot;active\&quot;:true,\&quot;name\&quot;:\&quot;New Proof\&quot;}  Step 2. Create a verifyProfile Public Web link: Use the Proof token id as the token argument in your public URL used to open a new target popup. This activity is where members may confirm immediately.              https://staging.truanon.com/verifyProfile?id&#x3D;john_doe&amp;service&#x3D;securecannabisalliance&amp;token&#x3D;qjgblv72bzzio

### Example

```javascript
import TruAnonPrivateApi from 'tru_anon_private_api';

let apiInstance = new TruAnonPrivateApi.DefaultApi();
let opts = {
  'id': "{{your-member-id}}", // String | This is your unique username or member ID
  'service': "{{service-identifier}}" // String | The service name given to you by TruAnon
};
apiInstance.getToken(opts, (error, data, response) => {
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
 **id** | **String**| This is your unique username or member ID | [optional] 
 **service** | **String**| The service name given to you by TruAnon | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

