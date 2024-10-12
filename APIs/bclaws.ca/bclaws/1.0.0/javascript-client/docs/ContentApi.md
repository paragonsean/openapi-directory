# BcLaws.ContentApi

All URIs are relative to *http://www.bclaws.ca/civix*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentAspectIdCivixDocumentIdGet**](ContentApi.md#contentAspectIdCivixDocumentIdGet) | **GET** /content/{aspectId}/{civixDocumentId} | Lists the metadata available for the specified index or directory from the BCLaws legislative respository
[**contentAspectIdGet**](ContentApi.md#contentAspectIdGet) | **GET** /content/{aspectId} | Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library



## contentAspectIdCivixDocumentIdGet

> contentAspectIdCivixDocumentIdGet(aspectId, civixDocumentId)

Lists the metadata available for the specified index or directory from the BCLaws legislative respository

### Example

```javascript
import BcLaws from 'bc_laws';

let apiInstance = new BcLaws.ContentApi();
let aspectId = "'complete'"; // String | The identifier of the 'aspect' (content group) to search
let civixDocumentId = "'statreg'"; // String | The document identification code for an index or directory
apiInstance.contentAspectIdCivixDocumentIdGet(aspectId, civixDocumentId, (error, data, response) => {
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
 **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to &#39;complete&#39;]
 **civixDocumentId** | **String**| The document identification code for an index or directory | [default to &#39;statreg&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## contentAspectIdGet

> contentAspectIdGet(aspectId)

Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library

### Example

```javascript
import BcLaws from 'bc_laws';

let apiInstance = new BcLaws.ContentApi();
let aspectId = "'complete'"; // String | The identifier of the 'aspect' (content group) to search
apiInstance.contentAspectIdGet(aspectId, (error, data, response) => {
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
 **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to &#39;complete&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

