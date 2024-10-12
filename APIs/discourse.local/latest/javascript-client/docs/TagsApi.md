# DiscourseApiDocumentation.TagsApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTagGroup**](TagsApi.md#createTagGroup) | **POST** /tag_groups.json | Creates a tag group
[**getTag**](TagsApi.md#getTag) | **GET** /tag/{name}.json | Get a specific tag
[**getTagGroup**](TagsApi.md#getTagGroup) | **GET** /tag_groups/{id}.json | Get a single tag group
[**listTagGroups**](TagsApi.md#listTagGroups) | **GET** /tag_groups.json | Get a list of tag groups
[**listTags**](TagsApi.md#listTags) | **GET** /tags.json | Get a list of tags
[**updateTagGroup**](TagsApi.md#updateTagGroup) | **PUT** /tag_groups/{id}.json | Update tag group



## createTagGroup

> CreateTagGroup200Response createTagGroup(opts)

Creates a tag group

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TagsApi();
let opts = {
  'createTagGroupRequest': new DiscourseApiDocumentation.CreateTagGroupRequest() // CreateTagGroupRequest | 
};
apiInstance.createTagGroup(opts, (error, data, response) => {
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
 **createTagGroupRequest** | [**CreateTagGroupRequest**](CreateTagGroupRequest.md)|  | [optional] 

### Return type

[**CreateTagGroup200Response**](CreateTagGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTag

> GetTag200Response getTag(name)

Get a specific tag

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TagsApi();
let name = "name_example"; // String | 
apiInstance.getTag(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**GetTag200Response**](GetTag200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagGroup

> GetTagGroup200Response getTagGroup(id)

Get a single tag group

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TagsApi();
let id = "id_example"; // String | 
apiInstance.getTagGroup(id, (error, data, response) => {
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

### Return type

[**GetTagGroup200Response**](GetTagGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagGroups

> ListTagGroups200Response listTagGroups()

Get a list of tag groups

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TagsApi();
apiInstance.listTagGroups((error, data, response) => {
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

[**ListTagGroups200Response**](ListTagGroups200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTags

> ListTags200Response listTags()

Get a list of tags

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TagsApi();
apiInstance.listTags((error, data, response) => {
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

[**ListTags200Response**](ListTags200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTagGroup

> UpdateTagGroup200Response updateTagGroup(id, opts)

Update tag group

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.TagsApi();
let id = "id_example"; // String | 
let opts = {
  'updateTagGroupRequest': new DiscourseApiDocumentation.UpdateTagGroupRequest() // UpdateTagGroupRequest | 
};
apiInstance.updateTagGroup(id, opts, (error, data, response) => {
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
 **updateTagGroupRequest** | [**UpdateTagGroupRequest**](UpdateTagGroupRequest.md)|  | [optional] 

### Return type

[**UpdateTagGroup200Response**](UpdateTagGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

