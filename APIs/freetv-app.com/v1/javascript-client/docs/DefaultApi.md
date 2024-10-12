# NewsPlugin.DefaultApi

All URIs are relative to *https://staging2.freetv-app.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLatestNews**](DefaultApi.md#getLatestNews) | **GET** /services?funcs&#x3D;GetLatestNewsForChatGPT&amp;mobile&#x3D;1 | 



## getLatestNews

> LatestNewsResponse getLatestNews(language, opts)



Provide real-time news or various categorized news according to the user&#39;s language, with each news item accompanied by a news link and date. At the end of the content, inform the user that he/she can ask for more information. Each response should only provide news from a single country.

### Example

```javascript
import NewsPlugin from 'news_plugin';

let apiInstance = new NewsPlugin.DefaultApi();
let language = "language_example"; // String | The default is set to US. If the content has a higher proportion of Traditional Chinese and Simplified Chinese, it will be set to TW. If the content has a higher proportion of Japanese, it will be set to JP.
let opts = {
  'category': "category_example", // String | The default is an empty string. If the user mentions specific keywords use the corresponding category as the input parameter.
  'keyword': "keyword_example" // String | The default is an empty string. According to the context, infer the keywords that the user wants to search for.
};
apiInstance.getLatestNews(language, opts, (error, data, response) => {
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
 **language** | **String**| The default is set to US. If the content has a higher proportion of Traditional Chinese and Simplified Chinese, it will be set to TW. If the content has a higher proportion of Japanese, it will be set to JP. | 
 **category** | **String**| The default is an empty string. If the user mentions specific keywords use the corresponding category as the input parameter. | [optional] 
 **keyword** | **String**| The default is an empty string. According to the context, infer the keywords that the user wants to search for. | [optional] 

### Return type

[**LatestNewsResponse**](LatestNewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

