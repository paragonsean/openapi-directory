# AnnunciatorContentApi.MessageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMessageMessageAnnunciatorCurrentGet**](MessageApi.md#apiMessageMessageAnnunciatorCurrentGet) | **GET** /api/Message/message/{annunciator}/current | Return the current message by annunciator type
[**apiMessageMessageAnnunciatorDateGet**](MessageApi.md#apiMessageMessageAnnunciatorDateGet) | **GET** /api/Message/message/{annunciator}/{date} | Return the most recent message by annunciator after date time specified



## apiMessageMessageAnnunciatorCurrentGet

> MessageViewModel apiMessageMessageAnnunciatorCurrentGet(annunciator)

Return the current message by annunciator type

### Example

```javascript
import AnnunciatorContentApi from 'annunciator_content_api';

let apiInstance = new AnnunciatorContentApi.MessageApi();
let annunciator = new AnnunciatorContentApi.AnnunciatorMessageType(); // AnnunciatorMessageType | Current message by annunciator
apiInstance.apiMessageMessageAnnunciatorCurrentGet(annunciator, (error, data, response) => {
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
 **annunciator** | [**AnnunciatorMessageType**](.md)| Current message by annunciator | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMessageMessageAnnunciatorDateGet

> MessageViewModel apiMessageMessageAnnunciatorDateGet(annunciator, date)

Return the most recent message by annunciator after date time specified

### Example

```javascript
import AnnunciatorContentApi from 'annunciator_content_api';

let apiInstance = new AnnunciatorContentApi.MessageApi();
let annunciator = new AnnunciatorContentApi.AnnunciatorMessageType(); // AnnunciatorMessageType | Message by annunciator type
let date = new Date("2013-10-20T19:20:30+01:00"); // Date | First message after date time specified
apiInstance.apiMessageMessageAnnunciatorDateGet(annunciator, date, (error, data, response) => {
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
 **annunciator** | [**AnnunciatorMessageType**](.md)| Message by annunciator type | 
 **date** | **Date**| First message after date time specified | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

