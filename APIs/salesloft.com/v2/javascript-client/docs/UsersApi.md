# SalesLoftPlatform.UsersApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2UsersIdJsonGet**](UsersApi.md#v2UsersIdJsonGet) | **GET** /v2/users/{id}.json | Fetch a user
[**v2UsersIdJsonPut**](UsersApi.md#v2UsersIdJsonPut) | **PUT** /v2/users/{id}.json | Update a user
[**v2UsersJsonGet**](UsersApi.md#v2UsersJsonGet) | **GET** /v2/users.json | List users



## v2UsersIdJsonGet

> User v2UsersIdJsonGet(id)

Fetch a user

Fetches a user, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.UsersApi();
let id = "id_example"; // String | User ID
apiInstance.v2UsersIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| User ID | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2UsersIdJsonPut

> User v2UsersIdJsonPut(id, opts)

Update a user

Updates a user. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.UsersApi();
let id = "id_example"; // String | User ID
let opts = {
  'active': true, // Boolean | Active status of the user's account
  'groupId': 56, // Number | Group assigned to the user
  'roleId': "roleId_example", // String | Role assigned to the user. Must be one of: Admin, User, or a custom role ID
  'workCountry': "workCountry_example" // String | The user's work country (alpha-2 code)
};
apiInstance.v2UsersIdJsonPut(id, opts, (error, data, response) => {
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
 **id** | **String**| User ID | 
 **active** | **Boolean**| Active status of the user&#39;s account | [optional] 
 **groupId** | **Number**| Group assigned to the user | [optional] 
 **roleId** | **String**| Role assigned to the user. Must be one of: Admin, User, or a custom role ID | [optional] 
 **workCountry** | **String**| The user&#39;s work country (alpha-2 code) | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2UsersJsonGet

> [User] v2UsersJsonGet(opts)

List users

Non Admin: Lists only your user, or all on team depending on group visibility policy Team Admin: Lists users associated with your team 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.UsersApi();
let opts = {
  'ids': [null], // [Number] | IDs of users to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'guid': ["null"], // [String] | Filters list to only include guids
  'groupId': ["null"], // [String] | Filters users by group_id.  An additional value of \"_is_null\" can be passed to filter users that are not in a group
  'roleId': ["null"], // [String] | Filters users by role_id
  'search': "search_example", // String | Space-separated list of keywords used to find case-insensitive substring matches against First Name, Last Name, or Email
  'active': true, // Boolean | Filters users based on active attribute. Defaults to not applied
  'visibleOnly': true, // Boolean | Defaults to true.  When true, only shows users that are actionable based on the team's privacy settings. When false, shows all users on the team, even if you can't take action on that user. Deactivated users are also included when false. 
  'perPage': 56, // Number | How many users to show per page in the range [1, 100]. Defaults to 25.  Results are only paginated if the page parameter is defined
  'page': 56, // Number | The current page to fetch users from. Defaults to returning all users
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'hasCrmUser': true, // Boolean | Filters users based on if they have a crm user mapped or not.
  'workCountry': ["null"], // [String] | Filters users based on assigned work_country.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: id, email, name, group, role. Defaults to id
  'sortDirection': "sortDirection_example" // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
};
apiInstance.v2UsersJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of users to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **guid** | [**[String]**](String.md)| Filters list to only include guids | [optional] 
 **groupId** | [**[String]**](String.md)| Filters users by group_id.  An additional value of \&quot;_is_null\&quot; can be passed to filter users that are not in a group | [optional] 
 **roleId** | [**[String]**](String.md)| Filters users by role_id | [optional] 
 **search** | **String**| Space-separated list of keywords used to find case-insensitive substring matches against First Name, Last Name, or Email | [optional] 
 **active** | **Boolean**| Filters users based on active attribute. Defaults to not applied | [optional] 
 **visibleOnly** | **Boolean**| Defaults to true.  When true, only shows users that are actionable based on the team&#39;s privacy settings. When false, shows all users on the team, even if you can&#39;t take action on that user. Deactivated users are also included when false.  | [optional] 
 **perPage** | **Number**| How many users to show per page in the range [1, 100]. Defaults to 25.  Results are only paginated if the page parameter is defined | [optional] 
 **page** | **Number**| The current page to fetch users from. Defaults to returning all users | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **hasCrmUser** | **Boolean**| Filters users based on if they have a crm user mapped or not. | [optional] 
 **workCountry** | [**[String]**](String.md)| Filters users based on assigned work_country. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: id, email, name, group, role. Defaults to id | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

