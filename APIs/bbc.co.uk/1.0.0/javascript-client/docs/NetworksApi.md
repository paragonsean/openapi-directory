# RadioMusicServices.NetworksApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRadioNetworks**](NetworksApi.md#getRadioNetworks) | **GET** /radio/networks.json | Networks



## getRadioNetworks

> NetworksResponse getRadioNetworks(xAPIKey, opts)

Networks

All iPlayer Radio networks - contains business logic for masterbrand and service relationships 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.NetworksApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'preset': true, // Boolean | Returns all networks needed for iPlayer Radio responsive web navigation
  'international': true // Boolean | Returns all networks available internationally
};
apiInstance.getRadioNetworks(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **preset** | **Boolean**| Returns all networks needed for iPlayer Radio responsive web navigation | [optional] 
 **international** | **Boolean**| Returns all networks available internationally | [optional] 

### Return type

[**NetworksResponse**](NetworksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

