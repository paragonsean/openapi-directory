# OsfApiv2Documentation.WikisApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wikiContent**](WikisApi.md#wikiContent) | **GET** /wikis/{wiki_id}/content/ | Retrieve the Content of a Wiki
[**wikiRead**](WikisApi.md#wikiRead) | **GET** /wikis/{wiki_id}/ | Retrieve a Wiki



## wikiContent

> wikiContent(wikiId)

Retrieve the Content of a Wiki

Retrieves the plaintext content of a wiki in markdown format. #### Returns Returns &#x60;text/markdown&#x60; of the wiki content itself. If the request is unsuccessful, plaintext with the error message will be displayed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.WikisApi();
let wikiId = "wikiId_example"; // String | The unique identifier of the wiki.
apiInstance.wikiContent(wikiId, (error, data, response) => {
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
 **wikiId** | **String**| The unique identifier of the wiki. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wikiRead

> Wiki wikiRead(wikiId)

Retrieve a Wiki

Retrieves the details about a specific wiki. A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested wiki, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.WikisApi();
let wikiId = "wikiId_example"; // String | The unique identifier of the wiki.
apiInstance.wikiRead(wikiId, (error, data, response) => {
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
 **wikiId** | **String**| The unique identifier of the wiki. | 

### Return type

[**Wiki**](Wiki.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

