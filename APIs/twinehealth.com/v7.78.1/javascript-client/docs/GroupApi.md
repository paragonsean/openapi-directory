# FitbitPlusApi.GroupApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroup**](GroupApi.md#createGroup) | **POST** /group | Create a group
[**fetchGroup**](GroupApi.md#fetchGroup) | **GET** /group/{id} | Get a group
[**fetchGroups**](GroupApi.md#fetchGroups) | **GET** /group | List groups



## createGroup

> CreateGroupResponse createGroup(createGroupRequest)

Create a group

Create a group record.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.GroupApi();
let createGroupRequest = new FitbitPlusApi.CreateGroupRequest(); // CreateGroupRequest | 
apiInstance.createGroup(createGroupRequest, (error, data, response) => {
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
 **createGroupRequest** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | 

### Return type

[**CreateGroupResponse**](CreateGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchGroup

> FetchGroupResponse fetchGroup(id)

Get a group

Get a group record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.GroupApi();
let id = "id_example"; // String | Group identifier
apiInstance.fetchGroup(id, (error, data, response) => {
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
 **id** | **String**| Group identifier | 

### Return type

[**FetchGroupResponse**](FetchGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchGroups

> FetchGroupsResponse fetchGroups(filterOrganization, opts)

List groups

Get a list of groups matching the specified filters.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.GroupApi();
let filterOrganization = "filterOrganization_example"; // String | Organization identifier
let opts = {
  'filterName': "filterName_example" // String | Group name
};
apiInstance.fetchGroups(filterOrganization, opts, (error, data, response) => {
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
 **filterOrganization** | **String**| Organization identifier | 
 **filterName** | **String**| Group name | [optional] 

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

