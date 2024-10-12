# WatchfulLi.TagsApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTags**](TagsApi.md#createTags) | **POST** /tags | Create a tag
[**getSitesByTags**](TagsApi.md#getSitesByTags) | **GET** /tags/{id}/sites | Find sites by tag ID
[**getTagById**](TagsApi.md#getTagById) | **GET** /tags/{id} | Find tag by ID
[**tagsGet**](TagsApi.md#tagsGet) | **GET** /tags | Get a list of tags
[**tagsIdDelete**](TagsApi.md#tagsIdDelete) | **DELETE** /tags/{id} | Delete a specific tag
[**tagsMetadataGet**](TagsApi.md#tagsMetadataGet) | **GET** /tags/metadata | Get the list of fields
[**updateTag**](TagsApi.md#updateTag) | **PUT** /tags/{id} | Update a tag



## createTags

> Tag createTags(body)

Create a tag

Create a tag

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.TagsApi();
let body = new WatchfulLi.Tag(); // Tag | JSON object Tag
apiInstance.createTags(body, (error, data, response) => {
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
 **body** | [**Tag**](Tag.md)| JSON object Tag | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getSitesByTags

> Site getSitesByTags(id, opts)

Find sites by tag ID

Returns a list of sites based with a specific tag id

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.TagsApi();
let id = 789; // Number | ID of tag that needs to be fetched
let opts = {
  'name': "name_example", // String | Do a 'LIKE' search, you can also use '%'
  'accessUrl': "accessUrl_example", // String | Do a 'LIKE' search, you can also use '%'
  'jVersion': "jVersion_example", // String | Do a 'LIKE' search, you can also use '%'
  'ip': "ip_example", // String | Do a 'LIKE' search, you can also use '%'
  'jUpdate': 56, // Number | Joomla core update
  'published': 56, // Number | is published
  'error': "error_example", // String | have errors
  'nbUpdates': "nbUpdates_example", // String | 
  'up': 56, // Number | is the website online
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
};
apiInstance.getSitesByTags(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of tag that needs to be fetched | 
 **name** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **accessUrl** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **jVersion** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **ip** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **jUpdate** | **Number**| Joomla core update | [optional] 
 **published** | **Number**| is published | [optional] 
 **error** | **String**| have errors | [optional] 
 **nbUpdates** | **String**|  | [optional] 
 **up** | **Number**| is the website online | [optional] 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getTagById

> Tag getTagById(id, opts)

Find tag by ID

Returns a tag based on ID

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.TagsApi();
let id = 789; // Number | ID of tag that needs to be fetched
let opts = {
  'fields': "fields_example" // String | Fields to return separate by comas: name,id
};
apiInstance.getTagById(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of tag that needs to be fetched | 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## tagsGet

> Tag tagsGet(opts)

Get a list of tags

Returns a list of tags

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.TagsApi();
let opts = {
  'name': "name_example", // String | Do a 'LIKE' search, you can also use '%'
  'type': "type_example", // String | Bootstrap color of the tag
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
};
apiInstance.tagsGet(opts, (error, data, response) => {
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
 **name** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **type** | **String**| Bootstrap color of the tag | [optional] 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## tagsIdDelete

> String tagsIdDelete(id)

Delete a specific tag

Delete a specific tag

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.TagsApi();
let id = 789; // Number | ID of tag that needs to be deleted
apiInstance.tagsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of tag that needs to be deleted | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## tagsMetadataGet

> String tagsMetadataGet()

Get the list of fields

Returns a list of fields

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.TagsApi();
apiInstance.tagsMetadataGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## updateTag

> Tag updateTag(id, body)

Update a tag

Update a tag

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.TagsApi();
let id = 789; // Number | ID of tag
let body = new WatchfulLi.Tag(); // Tag | JSON object of the updated tag
apiInstance.updateTag(id, body, (error, data, response) => {
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
 **id** | **Number**| ID of tag | 
 **body** | [**Tag**](Tag.md)| JSON object of the updated tag | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain

