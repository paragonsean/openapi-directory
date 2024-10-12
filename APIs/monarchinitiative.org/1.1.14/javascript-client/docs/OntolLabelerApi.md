# BioLinkApi.OntolLabelerApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOntolLabelerResource**](OntolLabelerApi.md#getOntolLabelerResource) | **GET** /ontol/labeler/ | Fetches a map from CURIEs/IDs to labels



## getOntolLabelerResource

> getOntolLabelerResource(id)

Fetches a map from CURIEs/IDs to labels

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntolLabelerApi();
let id = ["null"]; // [String] | List of ids
apiInstance.getOntolLabelerResource(id, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| List of ids | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

