# SpellCheckPro.DefaultApi

All URIs are relative to *https://spellcheckpro.p.rapidapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkSpellingRussian**](DefaultApi.md#checkSpellingRussian) | **POST** /check_spelling | Check Spelling (Russian)



## checkSpellingRussian

> checkSpellingRussian(opts)

Check Spelling (Russian)

Check Spelling (Russian)

### Example

```javascript
import SpellCheckPro from 'spell_check_pro';

let apiInstance = new SpellCheckPro.DefaultApi();
let opts = {
  'xRapidAPIKey': "", // String | 
  'checkSpellingRussianRequest': {"lang_code":"ru","text":"Добрый вее!"} // CheckSpellingRussianRequest | 
};
apiInstance.checkSpellingRussian(opts, (error, data, response) => {
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
 **xRapidAPIKey** | **String**|  | [optional] 
 **checkSpellingRussianRequest** | [**CheckSpellingRussianRequest**](CheckSpellingRussianRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

