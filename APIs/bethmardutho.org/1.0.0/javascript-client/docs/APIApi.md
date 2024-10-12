# SedraIvApi.APIApi

All URIs are relative to *http://sedra.bethmardutho.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lexemeIdGet**](APIApi.md#lexemeIdGet) | **GET** /lexeme/{id} | Get Syriac lexeme.
[**wordIdGet**](APIApi.md#wordIdGet) | **GET** /word/{id} | Get Syriac word.



## lexemeIdGet

> LexemeIdGet200Response lexemeIdGet(id)

Get Syriac lexeme.

Returns linguistic information for a Syriac lexeme.

### Example

```javascript
import SedraIvApi from 'sedra_iv_api';

let apiInstance = new SedraIvApi.APIApi();
let id = "id_example"; // String | The Id of a lexeme from the Sedra database.
apiInstance.lexemeIdGet(id, (error, data, response) => {
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
 **id** | **String**| The Id of a lexeme from the Sedra database. | 

### Return type

[**LexemeIdGet200Response**](LexemeIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wordIdGet

> [WordIdGet200ResponseInner] wordIdGet(id)

Get Syriac word.

Returns an array of linguistic information for every word that matches the Syriac word. Adjustment is made if the Syriac word is consonantal, partially, or fully vocalized.

### Example

```javascript
import SedraIvApi from 'sedra_iv_api';

let apiInstance = new SedraIvApi.APIApi();
let id = "id_example"; // String | The id parameters must contain either the Id of a word from the Sedra database or a Syriac word in the unicode character set. When the id parameter is a Syriac word it may be consonantal, partially vocalized, or fully vocalized. Fully vocalized Syriac words will have less false positive results than partially vocalized or consonantal Syriac words. When id is the Id of a word from the SEDRA database then that word will be the only word in the result.
apiInstance.wordIdGet(id, (error, data, response) => {
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
 **id** | **String**| The id parameters must contain either the Id of a word from the Sedra database or a Syriac word in the unicode character set. When the id parameter is a Syriac word it may be consonantal, partially vocalized, or fully vocalized. Fully vocalized Syriac words will have less false positive results than partially vocalized or consonantal Syriac words. When id is the Id of a word from the SEDRA database then that word will be the only word in the result. | 

### Return type

[**[WordIdGet200ResponseInner]**](WordIdGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

