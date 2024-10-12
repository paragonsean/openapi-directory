# Conjur.RolesApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addMemberToRole**](RolesApi.md#addMemberToRole) | **POST** /roles/{account}/{kind}/{identifier} | Update or modify an existing role membership
[**removeMemberFromRole**](RolesApi.md#removeMemberFromRole) | **DELETE** /roles/{account}/{kind}/{identifier} | Deletes an existing role membership
[**showRole**](RolesApi.md#showRole) | **GET** /roles/{account}/{kind}/{identifier} | Get role information



## addMemberToRole

> addMemberToRole(account, kind, identifier, members, member, opts)

Update or modify an existing role membership

Updates or modifies an existing role membership.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  When the &#x60;members&#x60; query parameter is provided, you will get the members of a role.  When the &#x60;members&#x60; and &#x60;member&#x60; query parameters are provided, the role specfified by &#x60;member&#x60; will be added as a member of the role specified in the endpoint URI. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.RolesApi();
let account = "account_example"; // String | Organization account name
let kind = "user"; // String | Type of resource
let identifier = "admin"; // String | ID of the role for which to get the information about
let members = "members_example"; // String | Returns a list of the Role's members.
let member = "member_example"; // String | The identifier of the Role to be added as a member.
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.addMemberToRole(account, kind, identifier, members, member, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **kind** | **String**| Type of resource | 
 **identifier** | **String**| ID of the role for which to get the information about | 
 **members** | **String**| Returns a list of the Role&#39;s members. | 
 **member** | **String**| The identifier of the Role to be added as a member. | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeMemberFromRole

> removeMemberFromRole(account, kind, identifier, members, member, opts)

Deletes an existing role membership

Deletes an existing role membership.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  When the &#x60;members&#x60; query parameter is provided, you will get the members of a role.  When the &#x60;members&#x60; and &#x60;member&#x60; query parameters are provided, the role specfified by &#x60;member&#x60; will be removed as a member of the role specified in the endpoint URI. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.RolesApi();
let account = "account_example"; // String | Organization account name
let kind = "user"; // String | Type of resource
let identifier = "admin"; // String | ID of the role for which to get the information about
let members = "members_example"; // String | Returns a list of the Role's members.
let member = "member_example"; // String | The identifier of the Role to be added as a member.
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.removeMemberFromRole(account, kind, identifier, members, member, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **kind** | **String**| Type of resource | 
 **identifier** | **String**| ID of the role for which to get the information about | 
 **members** | **String**| Returns a list of the Role&#39;s members. | 
 **member** | **String**| The identifier of the Role to be added as a member. | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## showRole

> Object showRole(account, kind, identifier, opts)

Get role information

Gets detailed information about a specific role, including the role members.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  ##### Listing members  If &#x60;members&#x60; is provided, you will get the members of a role.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give limit a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is true, returns only the number of items in the list.  ##### Text search  If the search parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weights results so that those with matching id or a matching value of an annotation called name appear first, then those with another matching annotation value, and finally those with a matching kind.  ##### Parameter Priority  If Conjur is given any combination of optional parameters, it responds with ONLY results for the parameter of the highest priority.  1. &#x60;graph&#x60; 2. &#x60;all&#x60; 3. &#x60;memberships&#x60; 4. &#x60;members&#x60; 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.RolesApi();
let account = "account_example"; // String | Organization account name
let kind = "user"; // String | Type of resource
let identifier = "admin"; // String | ID of the role for which to get the information about
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'all': "all_example", // String | Returns an array of Role IDs representing all role memberships, expanded recursively.
  'memberships': "memberships_example", // String | Returns all direct role memberships (members not expanded recursively).
  'members': "members_example", // String | Returns a list of the Role's members.
  'offset': 56, // Number | When listing members, start at this item number.
  'limit': 56, // Number | When listing members, return up to this many results.
  'count': true, // Boolean | When listing members, if `true`, return only the count of members.
  'search': "user", // String | When listing members, the results will be narrowed to only those matching the provided string
  'graph': "" // String | If included in the query returns a graph view of the role
};
apiInstance.showRole(account, kind, identifier, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **kind** | **String**| Type of resource | 
 **identifier** | **String**| ID of the role for which to get the information about | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **all** | **String**| Returns an array of Role IDs representing all role memberships, expanded recursively. | [optional] 
 **memberships** | **String**| Returns all direct role memberships (members not expanded recursively). | [optional] 
 **members** | **String**| Returns a list of the Role&#39;s members. | [optional] 
 **offset** | **Number**| When listing members, start at this item number. | [optional] 
 **limit** | **Number**| When listing members, return up to this many results. | [optional] 
 **count** | **Boolean**| When listing members, if &#x60;true&#x60;, return only the count of members. | [optional] 
 **search** | **String**| When listing members, the results will be narrowed to only those matching the provided string | [optional] 
 **graph** | **String**| If included in the query returns a graph view of the role | [optional] 

### Return type

**Object**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

