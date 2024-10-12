# BioLinkApi.VariationSetApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteVariantSetItem**](VariationSetApi.md#deleteVariantSetItem) | **DELETE** /variation/set/{id} | Deletes variant set
[**getVariantAnalyze**](VariationSetApi.md#getVariantAnalyze) | **GET** /variation/set/analyze/{id} | Returns list of matches
[**getVariantSetItem**](VariationSetApi.md#getVariantSetItem) | **GET** /variation/set/{id} | Returns a variant set
[**getVariantSetsArchiveCollection**](VariationSetApi.md#getVariantSetsArchiveCollection) | **GET** /variation/set/archive/{year}/{month}/{day} | Returns list of variant sets from a specified time period
[**getVariantSetsCollection**](VariationSetApi.md#getVariantSetsCollection) | **GET** /variation/set/ | Returns list of variant sets
[**postVariantSetsCollection**](VariationSetApi.md#postVariantSetsCollection) | **POST** /variation/set/ | Creates a new variant set
[**putVariantSetItem**](VariationSetApi.md#putVariantSetItem) | **PUT** /variation/set/{id} | Updates a variant set



## deleteVariantSetItem

> deleteVariantSetItem(id)

Deletes variant set

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.VariationSetApi();
let id = "id_example"; // String | 
apiInstance.deleteVariantSetItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVariantAnalyze

> [Association] getVariantAnalyze(id)

Returns list of matches

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.VariationSetApi();
let id = "id_example"; // String | 
apiInstance.getVariantAnalyze(id, (error, data, response) => {
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


## getVariantSetItem

> VariantSet getVariantSetItem(id)

Returns a variant set

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.VariationSetApi();
let id = "id_example"; // String | 
apiInstance.getVariantSetItem(id, (error, data, response) => {
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

[**VariantSet**](VariantSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantSetsArchiveCollection

> PageOfVariantSets getVariantSetsArchiveCollection(year, month, day, opts)

Returns list of variant sets from a specified time period

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.VariationSetApi();
let year = 56; // Number | 
let month = 56; // Number | 
let day = 56; // Number | 
let opts = {
  'page': 1, // Number | Page number
  'perPage': 10 // Number | Results per page {error_msg}
};
apiInstance.getVariantSetsArchiveCollection(year, month, day, opts, (error, data, response) => {
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
 **year** | **Number**|  | 
 **month** | **Number**|  | 
 **day** | **Number**|  | 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Results per page {error_msg} | [optional] [default to 10]

### Return type

[**PageOfVariantSets**](PageOfVariantSets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantSetsCollection

> PageOfVariantSets getVariantSetsCollection(opts)

Returns list of variant sets

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.VariationSetApi();
let opts = {
  'page': 1, // Number | Page number
  'perPage': 10 // Number | Results per page {error_msg}
};
apiInstance.getVariantSetsCollection(opts, (error, data, response) => {
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
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Results per page {error_msg} | [optional] [default to 10]

### Return type

[**PageOfVariantSets**](PageOfVariantSets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postVariantSetsCollection

> postVariantSetsCollection(variantSet)

Creates a new variant set

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.VariationSetApi();
let variantSet = new BioLinkApi.VariantSet(); // VariantSet | 
apiInstance.postVariantSetsCollection(variantSet, (error, data, response) => {
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
 **variantSet** | [**VariantSet**](VariantSet.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putVariantSetItem

> putVariantSetItem(id, variantSet)

Updates a variant set

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.VariationSetApi();
let id = "id_example"; // String | 
let variantSet = new BioLinkApi.VariantSet(); // VariantSet | 
apiInstance.putVariantSetItem(id, variantSet, (error, data, response) => {
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
 **id** | **String**|  | 
 **variantSet** | [**VariantSet**](VariantSet.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

