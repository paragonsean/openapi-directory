# TopStories.StoriesApi

All URIs are relative to *http://api.nytimes.com/svc/topstories/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sectionFormatGet**](StoriesApi.md#sectionFormatGet) | **GET** /{section}.{format} | Top Stories



## sectionFormatGet

> SectionFormatGet200Response sectionFormatGet(section, format, opts)

Top Stories

The Top Stories API returns a list of articles and associated images currently on the specified section.  Support JSON and JSONP. 

### Example

```javascript
import TopStories from 'top_stories';
let defaultClient = TopStories.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TopStories.StoriesApi();
let section = "section_example"; // String | The section the story appears in.
let format = "format_example"; // String | if this is JSONP or JSON
let opts = {
  'callback': "callback_example" // String | The name of the function the API call results will be passed to. Required when using JSONP. This parameter has only one valid value per section. The format is {section_name}TopStoriesCallback. 
};
apiInstance.sectionFormatGet(section, format, opts, (error, data, response) => {
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
 **section** | **String**| The section the story appears in. | 
 **format** | **String**| if this is JSONP or JSON | 
 **callback** | **String**| The name of the function the API call results will be passed to. Required when using JSONP. This parameter has only one valid value per section. The format is {section_name}TopStoriesCallback.  | [optional] 

### Return type

[**SectionFormatGet200Response**](SectionFormatGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

