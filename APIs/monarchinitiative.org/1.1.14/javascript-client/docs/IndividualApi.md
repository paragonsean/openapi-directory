# BioLinkApi.IndividualApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIndividual**](IndividualApi.md#getIndividual) | **GET** /individual/{id} | Returns list of matches
[**getPedigree**](IndividualApi.md#getPedigree) | **GET** /individual/pedigree/{id} | Returns list of matches



## getIndividual

> [Association] getIndividual(id)

Returns list of matches

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.IndividualApi();
let id = "id_example"; // String | 
apiInstance.getIndividual(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPedigree

> [Association] getPedigree(id)

Returns list of matches

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.IndividualApi();
let id = "id_example"; // String | 
apiInstance.getPedigree(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

