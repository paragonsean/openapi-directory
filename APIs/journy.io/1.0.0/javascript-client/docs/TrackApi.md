# DeveloperDocumentation.TrackApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trackEvent**](TrackApi.md#trackEvent) | **POST** /track | Track event



## trackEvent

> DeleteAccount202Response trackEvent(trackEventRequest)

Track event

Endpoint used to track an event for a user or an account.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.TrackApi();
let trackEventRequest = new DeveloperDocumentation.TrackEventRequest(); // TrackEventRequest | 
apiInstance.trackEvent(trackEventRequest, (error, data, response) => {
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
 **trackEventRequest** | [**TrackEventRequest**](TrackEventRequest.md)|  | 

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

