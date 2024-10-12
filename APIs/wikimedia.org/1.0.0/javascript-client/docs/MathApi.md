# Wikimedia.MathApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaMathCheckTypePost**](MathApi.md#mediaMathCheckTypePost) | **POST** /media/math/check/{type} | Check and normalize a TeX formula.
[**mediaMathFormulaHashGet**](MathApi.md#mediaMathFormulaHashGet) | **GET** /media/math/formula/{hash} | Get a previously-stored formula
[**mediaMathRenderFormatHashGet**](MathApi.md#mediaMathRenderFormatHashGet) | **GET** /media/math/render/{format}/{hash} | Get rendered formula in the given format.



## mediaMathCheckTypePost

> mediaMathCheckTypePost(type, q)

Check and normalize a TeX formula.

Checks the supplied TeX formula for correctness and returns the normalised formula representation as well as information about identifiers. Available types are tex and inline-tex. The response contains the &#x60;x-resource-location&#x60; header which can be used to retrieve the render of the checked formula in one of the supported rendering formats. Just append the value of the header to &#x60;/media/math/{format}/&#x60; and perform a GET request against that URL.  Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.MathApi();
let type = "type_example"; // String | The input type of the given formula; can be tex or inline-tex
let q = "q_example"; // String | The formula to check
apiInstance.mediaMathCheckTypePost(type, q, (error, data, response) => {
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
 **type** | **String**| The input type of the given formula; can be tex or inline-tex | 
 **q** | **String**| The formula to check | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/problem+json


## mediaMathFormulaHashGet

> mediaMathFormulaHashGet(hash)

Get a previously-stored formula

Returns the previously-stored formula via &#x60;/media/math/check/{type}&#x60; for the given hash.  Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.MathApi();
let hash = "hash_example"; // String | The hash string of the previous POST data
apiInstance.mediaMathFormulaHashGet(hash, (error, data, response) => {
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
 **hash** | **String**| The hash string of the previous POST data | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## mediaMathRenderFormatHashGet

> mediaMathRenderFormatHashGet(format, hash)

Get rendered formula in the given format.

Given a request hash, renders a TeX formula into its mathematic representation in the given format. When a request is issued to the &#x60;/media/math/check/{format}&#x60; POST endpoint, the response contains the &#x60;x-resource-location&#x60; header denoting the hash ID of the POST data. Once obtained, this endpoint has to be used to obtain the actual render.  Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.MathApi();
let format = "format_example"; // String | The output format; can be svg or mml
let hash = "hash_example"; // String | The hash string of the previous POST data
apiInstance.mediaMathRenderFormatHashGet(format, hash, (error, data, response) => {
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
 **format** | **String**| The output format; can be svg or mml | 
 **hash** | **String**| The hash string of the previous POST data | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/svg+xml, application/mathml+xml, image/png, application/problem+json

