# ApiDatumboxCom.InformationRetrievalApi

All URIs are relative to *http://api.datumbox.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywordExtraction**](InformationRetrievalApi.md#keywordExtraction) | **POST** /1.0/KeywordExtraction.json | Extracts the Keywords of the Document
[**textExtraction**](InformationRetrievalApi.md#textExtraction) | **POST** /1.0/TextExtraction.json | Extracts the clear text from Webpage



## keywordExtraction

> keywordExtraction(apiKey, opts)

Extracts the Keywords of the Document

The Keyword Extraction function enables you to extract from an arbitrary document all the keywords and word-combinations along with their occurrences in the text.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.InformationRetrievalApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'n': 56, // Number | The number of keyword combinations (n-grams) that you wish to extract.
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.keywordExtraction(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **n** | **Number**| The number of keyword combinations (n-grams) that you wish to extract. | [optional] 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## textExtraction

> textExtraction(apiKey, opts)

Extracts the clear text from Webpage

The Text Extraction function enables you to extract the important information from a given webpage. Extracting the clear text of the documents is an important step before any other analysis.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.InformationRetrievalApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The HTML source of the webpage.
};
apiInstance.textExtraction(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The HTML source of the webpage. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

