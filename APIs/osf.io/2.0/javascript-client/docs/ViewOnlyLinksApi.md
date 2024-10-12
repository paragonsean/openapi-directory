# OsfApiv2Documentation.ViewOnlyLinksApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**viewOnlyLinksNodeList**](ViewOnlyLinksApi.md#viewOnlyLinksNodeList) | **GET** /view_only_links/{link_id}/nodes/ | List all nodes
[**viewOnlyLinksRead**](ViewOnlyLinksApi.md#viewOnlyLinksRead) | **GET** /view_only_links/{link_id}/ | Retrieve a view only link



## viewOnlyLinksNodeList

> [Node] viewOnlyLinksNodeList(linkId)

List all nodes

 The list of nodes which this view only link gives read-only access to. #### Permissions Only project administrators may retrieve the nodes of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.ViewOnlyLinksApi();
let linkId = "linkId_example"; // String | The unique identifier of the view only link.
apiInstance.viewOnlyLinksNodeList(linkId, (error, data, response) => {
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
 **linkId** | **String**| The unique identifier of the view only link. | 

### Return type

[**[Node]**](Node.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## viewOnlyLinksRead

> ViewOnlyLinks viewOnlyLinksRead(linkId)

Retrieve a view only link

Retrieves details about a specific view only link. #### Permissions Only project administrators may retrieve the details of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested view only link, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.ViewOnlyLinksApi();
let linkId = "linkId_example"; // String | The unique identifier of the view only link.
apiInstance.viewOnlyLinksRead(linkId, (error, data, response) => {
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
 **linkId** | **String**| The unique identifier of the view only link. | 

### Return type

[**ViewOnlyLinks**](ViewOnlyLinks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

