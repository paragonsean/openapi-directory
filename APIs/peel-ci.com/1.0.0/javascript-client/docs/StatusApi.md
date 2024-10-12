# PeelTuneInApi.StatusApi

All URIs are relative to *http://hashtag.peel-ci.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatuses**](StatusApi.md#getStatuses) | **GET** /status/{showID} | Gets the last 100 statuses for this show.



## getStatuses

> getStatuses(showID)

Gets the last 100 statuses for this show.

For Twitter, statuses are synonymous with tweets.

### Example

```javascript
import PeelTuneInApi from 'peel_tune_in_api';

let apiInstance = new PeelTuneInApi.StatusApi();
let showID = "showID_example"; // String | Unique ID for a show
apiInstance.getStatuses(showID, (error, data, response) => {
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
 **showID** | **String**| Unique ID for a show | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

