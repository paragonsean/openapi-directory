# JellyfinApi.UserViewsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGroupingOptions**](UserViewsApi.md#getGroupingOptions) | **GET** /Users/{userId}/GroupingOptions | Get user view grouping options.
[**getUserViews**](UserViewsApi.md#getUserViews) | **GET** /Users/{userId}/Views | Get user views.



## getGroupingOptions

> [SpecialViewOptionDto] getGroupingOptions(userId)

Get user view grouping options.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.UserViewsApi();
let userId = "userId_example"; // String | User id.
apiInstance.getGroupingOptions(userId, (error, data, response) => {
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
 **userId** | **String**| User id. | 

### Return type

[**[SpecialViewOptionDto]**](SpecialViewOptionDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getUserViews

> BaseItemDtoQueryResult getUserViews(userId, opts)

Get user views.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.UserViewsApi();
let userId = "userId_example"; // String | User id.
let opts = {
  'includeExternalContent': true, // Boolean | Whether or not to include external views such as channels or live tv.
  'presetViews': ["null"], // [String] | Preset views.
  'includeHidden': false // Boolean | Whether or not to include hidden content.
};
apiInstance.getUserViews(userId, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **includeExternalContent** | **Boolean**| Whether or not to include external views such as channels or live tv. | [optional] 
 **presetViews** | [**[String]**](String.md)| Preset views. | [optional] 
 **includeHidden** | **Boolean**| Whether or not to include hidden content. | [optional] [default to false]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

