# ENanoMapperDatabase.FacetsApi

All URIs are relative to *https://api.ideaconsult.net/nanoreg1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEndpointSummary_0**](FacetsApi.md#getEndpointSummary_0) | **GET** /enm/{db}/query/study | Search endpoint summary



## getEndpointSummary_0

> Facet getEndpointSummary_0(db, opts)

Search endpoint summary

Returns endpoint summary

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.FacetsApi();
let db = "'nanoreg1'"; // String | Database ID
let opts = {
  'top': "top_example", // String | Top endpoint category
  'category': "category_example" // String | Endpoint category (The value in the protocol.category.code field)
};
apiInstance.getEndpointSummary_0(db, opts, (error, data, response) => {
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
 **db** | **String**| Database ID | [default to &#39;nanoreg1&#39;]
 **top** | **String**| Top endpoint category | [optional] 
 **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] 

### Return type

[**Facet**](Facet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

