# HhsMediaServicesApi.TagsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesTagsFormatGet**](TagsApi.md#resourcesTagsFormatGet) | **GET** /resources/tags.{format} | Get Tags
[**resourcesTagsIdFormatGet**](TagsApi.md#resourcesTagsIdFormatGet) | **GET** /resources/tags/{id}.{format} | Get Tag by ID
[**resourcesTagsIdMediaFormatGet**](TagsApi.md#resourcesTagsIdMediaFormatGet) | **GET** /resources/tags/{id}/media.{format} | Get MediaItems for Tag
[**resourcesTagsIdRelatedFormatGet**](TagsApi.md#resourcesTagsIdRelatedFormatGet) | **GET** /resources/tags/{id}/related.{format} | Get related Tags by ID
[**resourcesTagsIdSyndicateFormatGet**](TagsApi.md#resourcesTagsIdSyndicateFormatGet) | **GET** /resources/tags/{id}/syndicate.{format} | Get MediaItems for Tag
[**resourcesTagsTagLanguagesFormatGet**](TagsApi.md#resourcesTagsTagLanguagesFormatGet) | **GET** /resources/tags/tagLanguages.{format} | Get TagLanguages
[**resourcesTagsTagTypesFormatGet**](TagsApi.md#resourcesTagsTagTypesFormatGet) | **GET** /resources/tags/tagTypes.{format} | Get MediaItems for Tag



## resourcesTagsFormatGet

> [TagMarshallerWrapped] resourcesTagsFormatGet(format, opts)

Get Tags

List of Tags

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.TagsApi();
let format = "format_example"; // String | Automatically added
let opts = {
  'sort': "sort_example", // String | The name of the property to which sorting will be applied
  'max': 56, // Number | The maximum number of records to return
  'offset': 56, // Number | Return records starting at the offset index.
  'name': "name_example", // String | Return tags[s] matching the supplied name
  'nameContains': "nameContains_example", // String | Return tags which contain the supplied partial name.
  'mediaId': 789, // Number | Return tags associated with the supplied media id.
  'typeId': 789, // Number | Return tags belonging to the supplied tag type id.
  'typeName': "typeName_example" // String | Return tags belonging to the supplied tag type name.
};
apiInstance.resourcesTagsFormatGet(format, opts, (error, data, response) => {
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
 **format** | **String**| Automatically added | 
 **sort** | **String**| The name of the property to which sorting will be applied | [optional] 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| Return records starting at the offset index. | [optional] 
 **name** | **String**| Return tags[s] matching the supplied name | [optional] 
 **nameContains** | **String**| Return tags which contain the supplied partial name. | [optional] 
 **mediaId** | **Number**| Return tags associated with the supplied media id. | [optional] 
 **typeId** | **Number**| Return tags belonging to the supplied tag type id. | [optional] 
 **typeName** | **String**| Return tags belonging to the supplied tag type name. | [optional] 

### Return type

[**[TagMarshallerWrapped]**](TagMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesTagsIdFormatGet

> [TagMarshallerWrapped] resourcesTagsIdFormatGet(id, format)

Get Tag by ID

Information about a specific tag

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.TagsApi();
let id = 789; // Number | The id of the record to look up
let format = "format_example"; // String | Automatically added
apiInstance.resourcesTagsIdFormatGet(id, format, (error, data, response) => {
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
 **id** | **Number**| The id of the record to look up | 
 **format** | **String**| Automatically added | 

### Return type

[**[TagMarshallerWrapped]**](TagMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesTagsIdMediaFormatGet

> [MediaItemWrapped] resourcesTagsIdMediaFormatGet(id, format, opts)

Get MediaItems for Tag

MediaItem

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.TagsApi();
let id = 789; // Number | The id of the tag to look up
let format = "format_example"; // String | Automatically added
let opts = {
  'sort': "sort_example", // String | The name of the property to which sorting will be applied
  'max': 56, // Number | The maximum number of records to return
  'offset': 56 // Number | Return records starting at the offset index.
};
apiInstance.resourcesTagsIdMediaFormatGet(id, format, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the tag to look up | 
 **format** | **String**| Automatically added | 
 **sort** | **String**| The name of the property to which sorting will be applied | [optional] 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| Return records starting at the offset index. | [optional] 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesTagsIdRelatedFormatGet

> [TagMarshallerWrapped] resourcesTagsIdRelatedFormatGet(id, format, opts)

Get related Tags by ID

Information about related tags to a specific tag

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.TagsApi();
let id = 789; // Number | The id of the tag to look up
let format = "format_example"; // String | Automatically added
let opts = {
  'sort': "sort_example", // String | The name of the property to which sorting will be applied
  'max': 56, // Number | The maximum number of records to return
  'offset': 56 // Number | Return records starting at the offset index.
};
apiInstance.resourcesTagsIdRelatedFormatGet(id, format, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the tag to look up | 
 **format** | **String**| Automatically added | 
 **sort** | **String**| The name of the property to which sorting will be applied | [optional] 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| Return records starting at the offset index. | [optional] 

### Return type

[**[TagMarshallerWrapped]**](TagMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesTagsIdSyndicateFormatGet

> String resourcesTagsIdSyndicateFormatGet(id, format, opts)

Get MediaItems for Tag

MediaItem

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.TagsApi();
let id = 789; // Number | The id of the record to look up
let format = "format_example"; // String | Automatically added
let opts = {
  'displayMethod': "displayMethod_example" // String | Method used to render an html request. Accepts one: [mv, list, feed]
};
apiInstance.resourcesTagsIdSyndicateFormatGet(id, format, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the record to look up | 
 **format** | **String**| Automatically added | 
 **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesTagsTagLanguagesFormatGet

> [TagLanguageMarshallerWrapped] resourcesTagsTagLanguagesFormatGet(format)

Get TagLanguages

List of Tag Languages

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.TagsApi();
let format = "format_example"; // String | Automatically added
apiInstance.resourcesTagsTagLanguagesFormatGet(format, (error, data, response) => {
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
 **format** | **String**| Automatically added | 

### Return type

[**[TagLanguageMarshallerWrapped]**](TagLanguageMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesTagsTagTypesFormatGet

> [TagTypeMarshallerWrapped] resourcesTagsTagTypesFormatGet(format)

Get MediaItems for Tag

List of Types

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.TagsApi();
let format = "format_example"; // String | Automatically added
apiInstance.resourcesTagsTagTypesFormatGet(format, (error, data, response) => {
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
 **format** | **String**| Automatically added | 

### Return type

[**[TagTypeMarshallerWrapped]**](TagTypeMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

