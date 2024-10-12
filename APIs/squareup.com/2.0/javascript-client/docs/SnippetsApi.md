# SquareConnectApi.SnippetsApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSnippet**](SnippetsApi.md#deleteSnippet) | **DELETE** /v2/sites/{site_id}/snippet | DeleteSnippet
[**retrieveSnippet**](SnippetsApi.md#retrieveSnippet) | **GET** /v2/sites/{site_id}/snippet | RetrieveSnippet
[**upsertSnippet**](SnippetsApi.md#upsertSnippet) | **POST** /v2/sites/{site_id}/snippet | UpsertSnippet



## deleteSnippet

> DeleteSnippetResponse deleteSnippet(siteId)

DeleteSnippet

Removes your snippet from a Square Online site.  You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SnippetsApi();
let siteId = "siteId_example"; // String | The ID of the site that contains the snippet.
apiInstance.deleteSnippet(siteId, (error, data, response) => {
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
 **siteId** | **String**| The ID of the site that contains the snippet. | 

### Return type

[**DeleteSnippetResponse**](DeleteSnippetResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveSnippet

> RetrieveSnippetResponse retrieveSnippet(siteId)

RetrieveSnippet

Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.  You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SnippetsApi();
let siteId = "siteId_example"; // String | The ID of the site that contains the snippet.
apiInstance.retrieveSnippet(siteId, (error, data, response) => {
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
 **siteId** | **String**| The ID of the site that contains the snippet. | 

### Return type

[**RetrieveSnippetResponse**](RetrieveSnippetResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## upsertSnippet

> UpsertSnippetResponse upsertSnippet(siteId, upsertSnippetRequest)

UpsertSnippet

Adds a snippet to a Square Online site or updates the existing snippet on the site.  The snippet code is appended to the end of the &#x60;head&#x60; element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.   You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.SnippetsApi();
let siteId = "siteId_example"; // String | The ID of the site where you want to add or update the snippet.
let upsertSnippetRequest = new SquareConnectApi.UpsertSnippetRequest(); // UpsertSnippetRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.upsertSnippet(siteId, upsertSnippetRequest, (error, data, response) => {
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
 **siteId** | **String**| The ID of the site where you want to add or update the snippet. | 
 **upsertSnippetRequest** | [**UpsertSnippetRequest**](UpsertSnippetRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpsertSnippetResponse**](UpsertSnippetResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

