# RemoteSettingsProd.BatchApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch**](BatchApi.md#batch) | **POST** /batch | 



## batch

> BatchResponseBodySchema batch(batchPayloadSchema)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.BatchApi();
let batchPayloadSchema = new RemoteSettingsProd.BatchPayloadSchema(); // BatchPayloadSchema | 
apiInstance.batch(batchPayloadSchema, (error, data, response) => {
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
 **batchPayloadSchema** | [**BatchPayloadSchema**](BatchPayloadSchema.md)|  | 

### Return type

[**BatchResponseBodySchema**](BatchResponseBodySchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

