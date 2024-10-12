# MarketcheckApis.CarCachedImageApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCachedImage**](CarCachedImageApi.md#getCachedImage) | **GET** /image/cache/car/{listingID}/{imageID} | Fetch cached image



## getCachedImage

> File getCachedImage(listingID, imageID, opts)

Fetch cached image

Fetch the cached car image

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarCachedImageApi();
let listingID = "listingID_example"; // String | ID of the listing to fetch cached images for
let imageID = "imageID_example"; // String | ID of the image to fetch
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.getCachedImage(listingID, imageID, opts, (error, data, response) => {
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
 **listingID** | **String**| ID of the listing to fetch cached images for | 
 **imageID** | **String**| ID of the image to fetch | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

**File**

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

