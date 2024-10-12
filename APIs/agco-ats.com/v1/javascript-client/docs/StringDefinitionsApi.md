# AgcoApi.StringDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stringDefinitionsGetDefinition**](StringDefinitionsApi.md#stringDefinitionsGetDefinition) | **GET** /api/v2/StringDefinitions/{ID} | Get a paged response of Global String Definitions.
[**stringDefinitionsGetDefinitions**](StringDefinitionsApi.md#stringDefinitionsGetDefinitions) | **GET** /api/v2/StringDefinitions | Get a paged response of Global String Definitions.
[**stringDefinitionsPostDefinition**](StringDefinitionsApi.md#stringDefinitionsPostDefinition) | **POST** /api/v2/StringDefinitions/Batch | Create StringDefinition object. The originating translation must be provided. Accepts an array of StringDefinition objects. Returns nothing.
[**stringDefinitionsUpdateDefinitions**](StringDefinitionsApi.md#stringDefinitionsUpdateDefinitions) | **PUT** /api/v2/StringDefinitions/Batch | Update StringDefinition objects. Accepts an array of StringDefinition objects. This endpoint will add StringDefinitionChange objects to the database. The DescriptionForTranslator may not be modified after a String is submitted for translation.



## stringDefinitionsGetDefinition

> GlobalResourcesSharedModelsStringDefinition stringDefinitionsGetDefinition(ID, opts)

Get a paged response of Global String Definitions.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringDefinitionsApi();
let ID = "ID_example"; // String | 
let opts = {
  'includeTranslations': true, // Boolean | Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
  'includeDeletedLanguages': true, // Boolean | Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
  'languageIds': "languageIds_example" // String | Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
};
apiInstance.stringDefinitionsGetDefinition(ID, opts, (error, data, response) => {
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
 **ID** | **String**|  | 
 **includeTranslations** | **Boolean**| Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false. | [optional] 
 **includeDeletedLanguages** | **Boolean**| Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false. | [optional] 
 **languageIds** | **String**| Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty. | [optional] 

### Return type

[**GlobalResourcesSharedModelsStringDefinition**](GlobalResourcesSharedModelsStringDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stringDefinitionsGetDefinitions

> APIIPagedResponseGlobalResourcesSharedModelsStringDefinition stringDefinitionsGetDefinitions(opts)

Get a paged response of Global String Definitions.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringDefinitionsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10. Ignored if 'stringIds' is provided.
  'modifiedAfterTimestamp': "modifiedAfterTimestamp_example", // String | Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
  'includeTranslations': true, // Boolean | Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
  'stringText': "stringText_example", // String | Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.
  'descriptionText': "descriptionText_example", // String | Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.
  'useFullText': true, // Boolean | Optional. This flag is used to determin whether to use the FullText Search or not.
  'includeDeletedLanguages': true, // Boolean | Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
  'languageIds': "languageIds_example", // String | Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
  'stringIds': "stringIds_example", // String | Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with 'modifiedAfterTimestamp', 'stringText', 'descriptionText', or 'useFullText'.
  'matchingTranslationsOnly': true // Boolean | Optional. If false, all translations for returned String Definitions are included. Must be used with 'stringText' provided and 'includeTranslations' = true.
};
apiInstance.stringDefinitionsGetDefinitions(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. Ignored if &#39;stringIds&#39; is provided. | [optional] 
 **modifiedAfterTimestamp** | **String**| Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array. | [optional] 
 **includeTranslations** | **Boolean**| Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false. | [optional] 
 **stringText** | **String**| Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true. | [optional] 
 **descriptionText** | **String**| Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. | [optional] 
 **useFullText** | **Boolean**| Optional. This flag is used to determin whether to use the FullText Search or not. | [optional] 
 **includeDeletedLanguages** | **Boolean**| Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false. | [optional] 
 **languageIds** | **String**| Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty. | [optional] 
 **stringIds** | **String**| Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with &#39;modifiedAfterTimestamp&#39;, &#39;stringText&#39;, &#39;descriptionText&#39;, or &#39;useFullText&#39;. | [optional] 
 **matchingTranslationsOnly** | **Boolean**| Optional. If false, all translations for returned String Definitions are included. Must be used with &#39;stringText&#39; provided and &#39;includeTranslations&#39; &#x3D; true. | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsStringDefinition**](APIIPagedResponseGlobalResourcesSharedModelsStringDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stringDefinitionsPostDefinition

> stringDefinitionsPostDefinition(globalResourcesSharedModelsStringDefinition)

Create StringDefinition object. The originating translation must be provided. Accepts an array of StringDefinition objects. Returns nothing.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringDefinitionsApi();
let globalResourcesSharedModelsStringDefinition = [new AgcoApi.GlobalResourcesSharedModelsStringDefinition()]; // [GlobalResourcesSharedModelsStringDefinition] | The StringDefinition Object array, along with originating translation.
apiInstance.stringDefinitionsPostDefinition(globalResourcesSharedModelsStringDefinition, (error, data, response) => {
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
 **globalResourcesSharedModelsStringDefinition** | [**[GlobalResourcesSharedModelsStringDefinition]**](GlobalResourcesSharedModelsStringDefinition.md)| The StringDefinition Object array, along with originating translation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## stringDefinitionsUpdateDefinitions

> stringDefinitionsUpdateDefinitions(globalResourcesSharedModelsStringDefinition)

Update StringDefinition objects. Accepts an array of StringDefinition objects. This endpoint will add StringDefinitionChange objects to the database. The DescriptionForTranslator may not be modified after a String is submitted for translation.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringDefinitionsApi();
let globalResourcesSharedModelsStringDefinition = [new AgcoApi.GlobalResourcesSharedModelsStringDefinition()]; // [GlobalResourcesSharedModelsStringDefinition] | The Array of Definitions to update
apiInstance.stringDefinitionsUpdateDefinitions(globalResourcesSharedModelsStringDefinition, (error, data, response) => {
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
 **globalResourcesSharedModelsStringDefinition** | [**[GlobalResourcesSharedModelsStringDefinition]**](GlobalResourcesSharedModelsStringDefinition.md)| The Array of Definitions to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

