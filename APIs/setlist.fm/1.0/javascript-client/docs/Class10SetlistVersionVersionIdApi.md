# SetlistFmApi.Class10SetlistVersionVersionIdApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10SetlistVersionVersionIdGetSetlistVersionGET**](Class10SetlistVersionVersionIdApi.md#resource10SetlistVersionVersionIdGetSetlistVersionGET) | **GET** /1.0/setlist/version/{versionId} | .



## resource10SetlistVersionVersionIdGetSetlistVersionGET

> JsonSetlist resource10SetlistVersionVersionIdGetSetlistVersionGET(versionId)

.

&lt;p&gt; Returns a setlist for the given versionId. The setlist returned isn&#39;t necessarily the most recent version. E.g. if you pass the versionId of a setlist that got edited since you last accessed it, you&#39;ll get the same version as last time. &lt;/p&gt;

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10SetlistVersionVersionIdApi();
let versionId = "versionId_example"; // String | the version id
apiInstance.resource10SetlistVersionVersionIdGetSetlistVersionGET(versionId, (error, data, response) => {
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
 **versionId** | **String**| the version id | 

### Return type

[**JsonSetlist**](JsonSetlist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

