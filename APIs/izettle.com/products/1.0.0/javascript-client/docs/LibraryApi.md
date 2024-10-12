# ProductLibraryApi.LibraryApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLibrary**](LibraryApi.md#getLibrary) | **GET** /organizations/{organizationUuid}/library | Retrieve the entire library



## getLibrary

> LibraryResponse getLibrary(organizationUuid, opts)

Retrieve the entire library

Will return the entire library for the authenticated user. If size of the library exceeds server preferences (normally 500) or the value of the optional limit parameter, the result will be paginated. Paginated responses return a Link header, indicating the next URI to fetch. The resulting header value will look something like:  &lt;https://products.izettle.com/organizations/self/library?limit&#x3D;X&amp;offset&#x3D;Y&gt;; rel&#x3D;\&quot;next\&quot;  where limit is number of items in response, and offset is the current position in pagination. The rel-part in the header is the links relation to the data previously recieved. The idea is that as long as this header is present there are still items remaining to be fetched. When either the header is not present or it&#39;s value doesn&#39;t contain any \&quot;next\&quot; value, all items have been sent to the client.  Note: The client should NOT try to extract query parameters from the URI, but rather use it as-is for the next request. Also, clients should be perpared that one Link header might contain multiple other IRIs that are not \&quot;next\&quot; (there will never be more than one \&quot;next\&quot; though). See more at:      IETF: https://tools.ietf.org/html/rfc5988     GitHub: https://developer.github.com/guides/traversing-with-pagination/  If eventLogUuid is provided, the response will only include events affecting the library since that event. Such responses are normally quite small and would be a preferred method for most fat clients after retrieving the initial full library. 

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.LibraryApi();
let organizationUuid = "organizationUuid_example"; // String | 
let opts = {
  'eventLogUuid': "eventLogUuid_example", // String | 
  'limit': 500, // Number | 
  'offset': "offset_example", // String | 
  'all': true // Boolean | 
};
apiInstance.getLibrary(organizationUuid, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **eventLogUuid** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 500]
 **offset** | **String**|  | [optional] 
 **all** | **Boolean**|  | [optional] 

### Return type

[**LibraryResponse**](LibraryResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

