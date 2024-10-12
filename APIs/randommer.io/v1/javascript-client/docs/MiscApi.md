# RandommerApi.MiscApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMiscCulturesGet**](MiscApi.md#apiMiscCulturesGet) | **GET** /api/Misc/Cultures | 
[**apiMiscRandomAddressGet**](MiscApi.md#apiMiscRandomAddressGet) | **GET** /api/Misc/Random-Address | 



## apiMiscCulturesGet

> apiMiscCulturesGet(opts)



### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.MiscApi();
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiMiscCulturesGet(opts, (error, data, response) => {
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
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiMiscRandomAddressGet

> apiMiscRandomAddressGet(number, opts)



### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.MiscApi();
let number = 56; // Number | 
let opts = {
  'culture': "'en'", // String | 
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiMiscRandomAddressGet(number, opts, (error, data, response) => {
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
 **number** | **Number**|  | 
 **culture** | **String**|  | [optional] [default to &#39;en&#39;]
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

