# Conjur.ResourcesApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**showResource**](ResourcesApi.md#showResource) | **GET** /resources/{account}/{kind}/{identifier} | Shows a description of a single resource.
[**showResourcesForAccount**](ResourcesApi.md#showResourcesForAccount) | **GET** /resources/{account} | Lists resources within an organization account.
[**showResourcesForAllAccounts**](ResourcesApi.md#showResourcesForAllAccounts) | **GET** /resources | Lists resources within an organization account.
[**showResourcesForKind**](ResourcesApi.md#showResourcesForKind) | **GET** /resources/{account}/{kind} | Lists resources of the same kind within an organization account.



## showResource

> Object showResource(account, kind, identifier, opts)

Shows a description of a single resource.

Details about a single resource.  If &#x60;permitted_roles&#x60; and &#x60;privilege&#x60; are given, Conjur lists the roles with the specified privilege on the resource.  If &#x60;check&#x60;, &#x60;privilege&#x60; and &#x60;role&#x60; are given, Conjur checks if the specified role has the privilege on the resource.  If &#x60;permitted_roles&#x60; and &#x60;check&#x60; are both given, Conjur responds to the &#x60;check&#x60; call ONLY.  ##### Permissions Required 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.ResourcesApi();
let account = "account_example"; // String | Organization account name
let kind = "user"; // String | Type of resource
let identifier = "conjur/authn-iam/test"; // String | ID of the resource for which to get the information about
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'permittedRoles': true, // Boolean | Lists the roles which have the named privilege on a resource.
  'privilege': "execute", // String | Level of privilege to filter on. Can only be used in combination with `permitted_roles` or `check` parameter.
  'check': true, // Boolean | Check whether a role has a privilege on a resource.
  'role': "myorg:host:host1" // String | Role to check privilege on. Can only be used in combination with `check` parameter.
};
apiInstance.showResource(account, kind, identifier, opts, (error, data, response) => {
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
 **identifier** | **String**| ID of the resource for which to get the information about | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **permittedRoles** | **Boolean**| Lists the roles which have the named privilege on a resource. | [optional] 
 **privilege** | **String**| Level of privilege to filter on. Can only be used in combination with &#x60;permitted_roles&#x60; or &#x60;check&#x60; parameter. | [optional] 
 **check** | **Boolean**| Check whether a role has a privilege on a resource. | [optional] 
 **role** | **String**| Role to check privilege on. Can only be used in combination with &#x60;check&#x60; parameter. | [optional] 

### Return type

**Object**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showResourcesForAccount

> showResourcesForAccount(account, opts)

Lists resources within an organization account.

Lists resources within an organization account.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.ResourcesApi();
let account = "account_example"; // String | Organization account name
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'kind': "user", // String | Type of resource
  'search': new Conjur.ERRORUNKNOWN(), // ERRORUNKNOWN | Filter resources based on this value by name
  'offset': 56, // Number | When listing resources, start at this item number.
  'limit': 56, // Number | When listing resources, return up to this many results.
  'count': true, // Boolean | When listing resources, if `true`, return only the count of the results.
  'role': "myorg:host:host1", // String | Retrieves the resources list for a different role if the authenticated role has access
  'actingAs': "myorg:host:host1" // String | Retrieves the resources list for a different role if the authenticated role has access
};
apiInstance.showResourcesForAccount(account, opts, (error, data, response) => {
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
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **kind** | **String**| Type of resource | [optional] 
 **search** | [**ERRORUNKNOWN**](.md)| Filter resources based on this value by name | [optional] 
 **offset** | **Number**| When listing resources, start at this item number. | [optional] 
 **limit** | **Number**| When listing resources, return up to this many results. | [optional] 
 **count** | **Boolean**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] 
 **role** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **actingAs** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## showResourcesForAllAccounts

> [ShowResourcesForAllAccounts200ResponseInner] showResourcesForAllAccounts(opts)

Lists resources within an organization account.

Lists resources within an organization account.  In the absence of an &#x60;account&#x60; query parameter, shows results for the account of the authorization token user.  If an &#x60;account&#x60; query parameter is given, shows results for the specified account.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;.\&quot; 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.ResourcesApi();
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'account': "myorg", // String | Organization account name
  'kind': "user", // String | Type of resource
  'search': "db", // String | Filter resources based on this value by name
  'offset': 56, // Number | When listing resources, start at this item number.
  'limit': 56, // Number | When listing resources, return up to this many results.
  'count': true, // Boolean | When listing resources, if `true`, return only the count of the results.
  'role': "myorg:host:host1", // String | Retrieves the resources list for a different role if the authenticated role has access
  'actingAs': "myorg:host:host1" // String | Retrieves the resources list for a different role if the authenticated role has access
};
apiInstance.showResourcesForAllAccounts(opts, (error, data, response) => {
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
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **account** | **String**| Organization account name | [optional] 
 **kind** | **String**| Type of resource | [optional] 
 **search** | **String**| Filter resources based on this value by name | [optional] 
 **offset** | **Number**| When listing resources, start at this item number. | [optional] 
 **limit** | **Number**| When listing resources, return up to this many results. | [optional] 
 **count** | **Boolean**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] 
 **role** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **actingAs** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 

### Return type

[**[ShowResourcesForAllAccounts200ResponseInner]**](ShowResourcesForAllAccounts200ResponseInner.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showResourcesForKind

> showResourcesForKind(account, kind, opts)

Lists resources of the same kind within an organization account.

Lists resources of the same kind within an organization account.  Kinds of resources include: policy, user, host, group, layer, or variable  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.ResourcesApi();
let account = "account_example"; // String | Organization account name
let kind = "user"; // String | Type of resource
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'search': new Conjur.ERRORUNKNOWN(), // ERRORUNKNOWN | Filter resources based on this value by name
  'offset': 56, // Number | When listing resources, start at this item number.
  'limit': 56, // Number | When listing resources, return up to this many results.
  'count': true, // Boolean | When listing resources, if `true`, return only the count of the results.
  'role': "myorg:host:host1", // String | Retrieves the resources list for a different role if the authenticated role has access
  'actingAs': "myorg:host:host1" // String | Retrieves the resources list for a different role if the authenticated role has access
};
apiInstance.showResourcesForKind(account, kind, opts, (error, data, response) => {
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
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **search** | [**ERRORUNKNOWN**](.md)| Filter resources based on this value by name | [optional] 
 **offset** | **Number**| When listing resources, start at this item number. | [optional] 
 **limit** | **Number**| When listing resources, return up to this many results. | [optional] 
 **count** | **Boolean**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] 
 **role** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 
 **actingAs** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

