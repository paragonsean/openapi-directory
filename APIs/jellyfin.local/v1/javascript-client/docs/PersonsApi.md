# JellyfinApi.PersonsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPerson**](PersonsApi.md#getPerson) | **GET** /Persons/{name} | Get person by name.
[**getPersons**](PersonsApi.md#getPersons) | **GET** /Persons | Gets all persons.



## getPerson

> BaseItemDto getPerson(name, opts)

Get person by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PersonsApi();
let name = "name_example"; // String | Person name.
let opts = {
  'userId': "userId_example" // String | Optional. Filter by user id, and attach user data.
};
apiInstance.getPerson(name, opts, (error, data, response) => {
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
 **name** | **String**| Person name. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPersons

> BaseItemDtoQueryResult getPersons(opts)

Gets all persons.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PersonsApi();
let opts = {
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'searchTerm': "searchTerm_example", // String | The search term.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'filters': [new JellyfinApi.ItemFilter()], // [ItemFilter] | Optional. Specify additional filters to apply.
  'isFavorite': true, // Boolean | Optional filter by items that are marked as favorite, or not. userId is required.
  'enableUserData': true, // Boolean | Optional, include user data.
  'imageTypeLimit': 56, // Number | Optional, the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'excludePersonTypes': ["null"], // [String] | Optional. If specified results will be filtered to exclude those containing the specified PersonType. Allows multiple, comma-delimited.
  'personTypes': ["null"], // [String] | Optional. If specified results will be filtered to include only those containing the specified PersonType. Allows multiple, comma-delimited.
  'appearsInItemId': "appearsInItemId_example", // String | Optional. If specified, person results will be filtered on items related to said persons.
  'userId': "userId_example", // String | User id.
  'enableImages': true // Boolean | Optional, include image information in output.
};
apiInstance.getPersons(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **searchTerm** | **String**| The search term. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **filters** | [**[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **isFavorite** | **Boolean**| Optional filter by items that are marked as favorite, or not. userId is required. | [optional] 
 **enableUserData** | **Boolean**| Optional, include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional, the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **excludePersonTypes** | [**[String]**](String.md)| Optional. If specified results will be filtered to exclude those containing the specified PersonType. Allows multiple, comma-delimited. | [optional] 
 **personTypes** | [**[String]**](String.md)| Optional. If specified results will be filtered to include only those containing the specified PersonType. Allows multiple, comma-delimited. | [optional] 
 **appearsInItemId** | **String**| Optional. If specified, person results will be filtered on items related to said persons. | [optional] 
 **userId** | **String**| User id. | [optional] 
 **enableImages** | **Boolean**| Optional, include image information in output. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

