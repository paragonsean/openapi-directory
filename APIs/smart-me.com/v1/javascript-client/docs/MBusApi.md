# SmartMe.MBusApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mBusPost**](MBusApi.md#mBusPost) | **POST** /api/MBus | M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.



## mBusPost

> Object mBusPost(mBusData)

M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.

M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.MBusApi();
let mBusData = new SmartMe.MBusData(); // MBusData | The M-BUS Telegram
apiInstance.mBusPost(mBusData, (error, data, response) => {
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
 **mBusData** | [**MBusData**](MBusData.md)| The M-BUS Telegram | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

