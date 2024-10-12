# ManagementGroups.EntitiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitiesList**](EntitiesApi.md#entitiesList) | **POST** /providers/Microsoft.Management/getEntities | 



## entitiesList

> EntityListResult entitiesList(apiVersion, opts)



List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.EntitiesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'skiptoken': "skiptoken_example", // String | Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
  'skip': 56, // Number | Number of entities to skip over when retrieving results. Passing this in will override $skipToken.
  'top': 56, // Number | Number of elements to return when retrieving results. Passing this in will override $skipToken.
  'select': "select_example", // String | This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. '$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain'. When specified the $select parameter can override select in $skipToken.
  'search': "search_example", // String | The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. With $search=AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user's permissions.With $search=AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity.With $search=ParentAndFirstLevelChildren the API will return the parent and  first level of children that the user has either direct access to or indirect access via one of their descendants.With $search=ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group.With $search=ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter.  The user must have direct access to the children entities or one of it's descendants for it to show up in the results.
  'filter': "filter_example", // String | The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq '{entityName}')  and you can check for substrings on either the name or display name fields(e.g. contains(name, '{substringToSearch}'), contains(displayName, '{substringToSearch')). Note that the '{entityName}' and '{substringToSearch}' fields are checked case insensitively.
  'view': "view_example", // String | The view parameter allows clients to filter the type of data that is returned by the getEntities call.
  'groupName': "groupName_example", // String | A filter which allows the get entities call to focus on a particular group (i.e. \"$filter=name eq 'groupName'\")
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
};
apiInstance.entitiesList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **skip** | **Number**| Number of entities to skip over when retrieving results. Passing this in will override $skipToken. | [optional] 
 **top** | **Number**| Number of elements to return when retrieving results. Passing this in will override $skipToken. | [optional] 
 **select** | **String**| This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. &#39;$select&#x3D;Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain&#39;. When specified the $select parameter can override select in $skipToken. | [optional] 
 **search** | **String**| The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. With $search&#x3D;AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user&#39;s permissions.With $search&#x3D;AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity.With $search&#x3D;ParentAndFirstLevelChildren the API will return the parent and  first level of children that the user has either direct access to or indirect access via one of their descendants.With $search&#x3D;ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group.With $search&#x3D;ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter.  The user must have direct access to the children entities or one of it&#39;s descendants for it to show up in the results. | [optional] 
 **filter** | **String**| The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq &#39;{entityName}&#39;)  and you can check for substrings on either the name or display name fields(e.g. contains(name, &#39;{substringToSearch}&#39;), contains(displayName, &#39;{substringToSearch&#39;)). Note that the &#39;{entityName}&#39; and &#39;{substringToSearch}&#39; fields are checked case insensitively. | [optional] 
 **view** | **String**| The view parameter allows clients to filter the type of data that is returned by the getEntities call. | [optional] 
 **groupName** | **String**| A filter which allows the get entities call to focus on a particular group (i.e. \&quot;$filter&#x3D;name eq &#39;groupName&#39;\&quot;) | [optional] 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

[**EntityListResult**](EntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

