# ArticleRewriterAndArticleExtractorApi.DefaultApi

All URIs are relative to *https://api.spinbot.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInfo**](DefaultApi.md#getInfo) | **GET** /api/acc | Return the user credit information.
[**postArticle**](DefaultApi.md#postArticle) | **POST** /api/article | Extracting the main article of the given URL.
[**postPrettySpinner**](DefaultApi.md#postPrettySpinner) | **POST** /api/pretty-spinner | Human readable auto rewrite your article.
[**postSpinner**](DefaultApi.md#postSpinner) | **POST** /api/spinner | Rewriting (spinning) your input article.
[**postSpintax**](DefaultApi.md#postSpintax) | **POST** /api/spintax | Generate Spintax format for the input article



## getInfo

> Object getInfo(key)

Return the user credit information.

Return the user credit information.

### Example

```javascript
import ArticleRewriterAndArticleExtractorApi from 'article_rewriter_and_article_extractor_api';
let defaultClient = ArticleRewriterAndArticleExtractorApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new ArticleRewriterAndArticleExtractorApi.DefaultApi();
let key = "key_example"; // String | Your api key
apiInstance.getInfo(key, (error, data, response) => {
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
 **key** | **String**| Your api key | 

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## postArticle

> Object postArticle(key, url, opts)

Extracting the main article of the given URL.

Extracting the main article of the given URL. The response is in JSON format.

### Example

```javascript
import ArticleRewriterAndArticleExtractorApi from 'article_rewriter_and_article_extractor_api';
let defaultClient = ArticleRewriterAndArticleExtractorApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new ArticleRewriterAndArticleExtractorApi.DefaultApi();
let key = "key_example"; // String | Your spinbot API key
let url = "url_example"; // String | The url of target article
let opts = {
  'fasterMode': "fasterMode_example" // String | you can set this input value to 1 to skip detecting the size (width and height in pixel) of all the images inside the extracted article. The response time of your request will be shortened if you set this input value to 1.
};
apiInstance.postArticle(key, url, opts, (error, data, response) => {
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
 **key** | **String**| Your spinbot API key | 
 **url** | **String**| The url of target article | 
 **fasterMode** | **String**| you can set this input value to 1 to skip detecting the size (width and height in pixel) of all the images inside the extracted article. The response time of your request will be shortened if you set this input value to 1. | [optional] 

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## postPrettySpinner

> Object postPrettySpinner(key, text, keep, accuracy)

Human readable auto rewrite your article.

Human readable auto rewrite your article. The response is in JSON format.

### Example

```javascript
import ArticleRewriterAndArticleExtractorApi from 'article_rewriter_and_article_extractor_api';
let defaultClient = ArticleRewriterAndArticleExtractorApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new ArticleRewriterAndArticleExtractorApi.DefaultApi();
let key = "key_example"; // String | Your spinbot API key
let text = "text_example"; // String | Input article that need to be rewrited.
let keep = "keep_example"; // String | Keep words/phrases, separated by newline, those remain unchanged during the rewrite process.
let accuracy = "accuracy_example"; // String | Rewrite accuracy profile, accepted values are very-low, low, medium, high, very-high
apiInstance.postPrettySpinner(key, text, keep, accuracy, (error, data, response) => {
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
 **key** | **String**| Your spinbot API key | 
 **text** | **String**| Input article that need to be rewrited. | 
 **keep** | **String**| Keep words/phrases, separated by newline, those remain unchanged during the rewrite process. | 
 **accuracy** | **String**| Rewrite accuracy profile, accepted values are very-low, low, medium, high, very-high | 

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## postSpinner

> Object postSpinner(key, text)

Rewriting (spinning) your input article.

Rewriting (spinning) you input article. The response is in JSON format.

### Example

```javascript
import ArticleRewriterAndArticleExtractorApi from 'article_rewriter_and_article_extractor_api';
let defaultClient = ArticleRewriterAndArticleExtractorApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new ArticleRewriterAndArticleExtractorApi.DefaultApi();
let key = "key_example"; // String | Your spinbot API key
let text = "text_example"; // String | Input article that need to be rewrited.
apiInstance.postSpinner(key, text, (error, data, response) => {
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
 **key** | **String**| Your spinbot API key | 
 **text** | **String**| Input article that need to be rewrited. | 

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## postSpintax

> Object postSpintax(key, text, opts)

Generate Spintax format for the input article

Generate Spintax format for the input article, so you can rewrite it yourself. The response is in JSON format.

### Example

```javascript
import ArticleRewriterAndArticleExtractorApi from 'article_rewriter_and_article_extractor_api';
let defaultClient = ArticleRewriterAndArticleExtractorApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new ArticleRewriterAndArticleExtractorApi.DefaultApi();
let key = "key_example"; // String | Your spinbot API key
let text = "text_example"; // String | Input article that need to be rewritten.
let opts = {
  'fullMode': "fullMode_example" // String | Full mode option.
};
apiInstance.postSpintax(key, text, opts, (error, data, response) => {
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
 **key** | **String**| Your spinbot API key | 
 **text** | **String**| Input article that need to be rewritten. | 
 **fullMode** | **String**| Full mode option. | [optional] 

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*

