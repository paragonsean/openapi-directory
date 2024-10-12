# SalesLoftPlatform.RecordingSettingsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2PhoneNumbersRecordingSettingsIdJsonGet**](RecordingSettingsApi.md#v2PhoneNumbersRecordingSettingsIdJsonGet) | **GET** /v2/phone_numbers/recording_settings/{id}.json | Fetch recording setting



## v2PhoneNumbersRecordingSettingsIdJsonGet

> RecordingSetting v2PhoneNumbersRecordingSettingsIdJsonGet(id)

Fetch recording setting

Fetches the recording status for a given phone number, based on Do Not Record and Recording Governance for your team. Phone number should be in E.164 format. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.RecordingSettingsApi();
let id = "id_example"; // String | E.164 Phone Number
apiInstance.v2PhoneNumbersRecordingSettingsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| E.164 Phone Number | 

### Return type

[**RecordingSetting**](RecordingSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

