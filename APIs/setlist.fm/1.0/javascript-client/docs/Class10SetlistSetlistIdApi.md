# SetlistFmApi.Class10SetlistSetlistIdApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10SetlistSetlistIdGetSetlistGET**](Class10SetlistSetlistIdApi.md#resource10SetlistSetlistIdGetSetlistGET) | **GET** /1.0/setlist/{setlistId} | .



## resource10SetlistSetlistIdGetSetlistGET

> JsonSetlist resource10SetlistSetlistIdGetSetlistGET(setlistId)

.

&lt;p&gt; Returns the current version of a setlist. E.g. if you pass the id of a setlist that got edited since you last accessed it, you&#39;ll get the current version. &lt;/p&gt;

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10SetlistSetlistIdApi();
let setlistId = "setlistId_example"; // String | the setlist id
apiInstance.resource10SetlistSetlistIdGetSetlistGET(setlistId, (error, data, response) => {
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
 **setlistId** | **String**| the setlist id | 

### Return type

[**JsonSetlist**](JsonSetlist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

