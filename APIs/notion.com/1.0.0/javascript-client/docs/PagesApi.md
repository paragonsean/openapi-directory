# NotionApi.PagesApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveAPage**](PagesApi.md#retrieveAPage) | **GET** /v1/pages/{id} | Retrieve a Page
[**retrieveAPagePropertyItem**](PagesApi.md#retrieveAPagePropertyItem) | **GET** /v1/pages/{page_id}/properties/{property_id} | Retrieve a Page Property Item
[**updatePageProperties**](PagesApi.md#updatePageProperties) | **PATCH** /v1/pages/{id} | Update Page properties 



## retrieveAPage

> RetrieveAPage200Response retrieveAPage(id, opts)

Retrieve a Page

Retrieves a Page object using the ID in the request path. This endpoint exposes page properties, not page content. 

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.PagesApi();
let id = "{{PAGE_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}", // String | 
  '': "" // String | 
};
apiInstance.retrieveAPage(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **notionVersion** | **String**|  | [optional] 
 **** | **String**|  | [optional] 

### Return type

[**RetrieveAPage200Response**](RetrieveAPage200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAPagePropertyItem

> RetrieveAPagePropertyItem200Response retrieveAPagePropertyItem(pageId, propertyId)

Retrieve a Page Property Item

Retrieve a Page Property Item

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.PagesApi();
let pageId = "{{PAGE_ID}}"; // String | 
let propertyId = "propertyId_example"; // String | 
apiInstance.retrieveAPagePropertyItem(pageId, propertyId, (error, data, response) => {
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
 **pageId** | **String**|  | 
 **propertyId** | **String**|  | 

### Return type

[**RetrieveAPagePropertyItem200Response**](RetrieveAPagePropertyItem200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePageProperties

> UpdatePageProperties200Response updatePageProperties(id, opts)

Update Page properties 

Updates a page by setting the values of any properties specified in the JSON body of the request. Properties not updated via parameters will remain unchanged. 

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.PagesApi();
let id = "{{PAGE_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}", // String | 
  'updatePagePropertiesRequest': {"properties":{"Status":{"select":{"name":"Reading"}}}} // UpdatePagePropertiesRequest | 
};
apiInstance.updatePageProperties(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **notionVersion** | **String**|  | [optional] 
 **updatePagePropertiesRequest** | [**UpdatePagePropertiesRequest**](UpdatePagePropertiesRequest.md)|  | [optional] 

### Return type

[**UpdatePageProperties200Response**](UpdatePageProperties200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

