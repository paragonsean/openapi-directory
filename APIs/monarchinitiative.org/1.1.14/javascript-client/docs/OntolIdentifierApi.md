# BioLinkApi.OntolIdentifierApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOntolIdentifierResource**](OntolIdentifierApi.md#getOntolIdentifierResource) | **GET** /ontol/identifier/ | Fetches a map from CURIEs/IDs to labels
[**postOntolIdentifierResource**](OntolIdentifierApi.md#postOntolIdentifierResource) | **POST** /ontol/identifier/ | Fetches a map from CURIEs/IDs to labels



## getOntolIdentifierResource

> getOntolIdentifierResource(label)

Fetches a map from CURIEs/IDs to labels

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntolIdentifierApi();
let label = ["null"]; // [String] | List of labels
apiInstance.getOntolIdentifierResource(label, (error, data, response) => {
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
 **label** | [**[String]**](String.md)| List of labels | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOntolIdentifierResource

> postOntolIdentifierResource(label)

Fetches a map from CURIEs/IDs to labels

Takes &#39;label&#39; list argument either as a querystring argument or as a key in the POST body when content-type is application/json.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntolIdentifierApi();
let label = ["null"]; // [String] | List of labels
apiInstance.postOntolIdentifierResource(label, (error, data, response) => {
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
 **label** | [**[String]**](String.md)| List of labels | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

