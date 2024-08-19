# VictorOps.AlertsApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1AlertsUuidGet**](AlertsApi.md#apiPublicV1AlertsUuidGet) | **GET** /api-public/v1/alerts/{uuid} | Retrieve alert details.



## apiPublicV1AlertsUuidGet

> GetAlertResponse apiPublicV1AlertsUuidGet(xVOApiId, xVOApiKey, uuid)

Retrieve alert details.

Retrieve the details of an alert that was sent VictorOps by you.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.AlertsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let uuid = "uuid_example"; // String | The VictorOps uuid of the alert
apiInstance.apiPublicV1AlertsUuidGet(xVOApiId, xVOApiKey, uuid, (error, data, response) => {
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
 **uuid** | **String**| The VictorOps uuid of the alert | 

### Return type

[**GetAlertResponse**](GetAlertResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

