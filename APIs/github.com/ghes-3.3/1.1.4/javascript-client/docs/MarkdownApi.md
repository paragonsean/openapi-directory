# GitHubV3RestApi.MarkdownApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markdownRender**](MarkdownApi.md#markdownRender) | **POST** /markdown | Render a Markdown document
[**markdownRenderRaw**](MarkdownApi.md#markdownRenderRaw) | **POST** /markdown/raw | Render a Markdown document in raw mode



## markdownRender

> String markdownRender(markdownRenderRequest)

Render a Markdown document



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MarkdownApi();
let markdownRenderRequest = {"text":"Hello **world**"}; // MarkdownRenderRequest | 
apiInstance.markdownRender(markdownRenderRequest, (error, data, response) => {
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
 **markdownRenderRequest** | [**MarkdownRenderRequest**](MarkdownRenderRequest.md)|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/html


## markdownRenderRaw

> String markdownRenderRaw(opts)

Render a Markdown document in raw mode

You must send Markdown as plain text (using a &#x60;Content-Type&#x60; header of &#x60;text/plain&#x60; or &#x60;text/x-markdown&#x60;) to this endpoint, rather than using JSON format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/) is not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MarkdownApi();
let opts = {
  'body': {"text":"Hello **world**"} // String | 
};
apiInstance.markdownRenderRaw(opts, (error, data, response) => {
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
 **body** | **String**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain, text/x-markdown
- **Accept**: text/html

