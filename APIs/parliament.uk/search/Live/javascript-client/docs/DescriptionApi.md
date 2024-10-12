# UkParliamentSearchService.DescriptionApi

All URIs are relative to *https://api.parliament.uk/search*

Method | HTTP request | Description
------------- | ------------- | -------------
[**descriptionGet**](DescriptionApi.md#descriptionGet) | **GET** /description | OpenSearch description document



## descriptionGet

> descriptionGet()

OpenSearch description document

### Example

```javascript
import UkParliamentSearchService from 'uk_parliament_search_service';

let apiInstance = new UkParliamentSearchService.DescriptionApi();
apiInstance.descriptionGet((error, data, response) => {
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
- **Accept**: application/opensearchdescription+xml

