# VerifyApi.FraudManagementApi

All URIs are relative to *https://api.nexmo.com/verify*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkUnblock**](FraudManagementApi.md#networkUnblock) | **POST** /network-unblock | Request a network unblock



## networkUnblock

> NetworkUnblockResponseOk networkUnblock(networkUnblock)

Request a network unblock

Request to unblock a network that has been blocked due to potential fraud detection &lt;div class&#x3D;\&quot;Vlt-callout Vlt-callout--critical\&quot;&gt;   &lt;div class&#x3D;\&quot;Vlt-callout__content\&quot;&gt;     &lt;h4&gt;Network Unblock is switched off by default.&lt;/h4&gt;     Please contact Sales to enable the Network Unblock API for your account.   &lt;/div&gt; &lt;/div&gt;

### Example

```javascript
import VerifyApi from 'verify_api';

let apiInstance = new VerifyApi.FraudManagementApi();
let networkUnblock = new VerifyApi.NetworkUnblock(); // NetworkUnblock | 
apiInstance.networkUnblock(networkUnblock, (error, data, response) => {
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
 **networkUnblock** | [**NetworkUnblock**](NetworkUnblock.md)|  | 

### Return type

[**NetworkUnblockResponseOk**](NetworkUnblockResponseOk.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

