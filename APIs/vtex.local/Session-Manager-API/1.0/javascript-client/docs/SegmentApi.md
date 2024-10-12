# SessionManagerApi.SegmentApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSegment**](SegmentApi.md#getSegment) | **GET** /segments | Get Segment



## getSegment

> getSegment()

Get Segment

You can add certain public fields in the query string and the system will attempt to fulfill it. Values such as &#x60;cultureInfo&#x60; and &#x60;utm&#x60; are overwriteable, just keep in mind such changes will not be reflected in the client&#39;s session.    If you wish to change the value on the session (and thus be reflected on the segment without special query strings), then use the PATCH request to session.

### Example

```javascript
import SessionManagerApi from 'session_manager_api';

let apiInstance = new SessionManagerApi.SegmentApi();
apiInstance.getSegment((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

