# SquareConnectApi.CustomerGroupsApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomerGroup**](CustomerGroupsApi.md#createCustomerGroup) | **POST** /v2/customers/groups | CreateCustomerGroup
[**deleteCustomerGroup**](CustomerGroupsApi.md#deleteCustomerGroup) | **DELETE** /v2/customers/groups/{group_id} | DeleteCustomerGroup
[**listCustomerGroups**](CustomerGroupsApi.md#listCustomerGroups) | **GET** /v2/customers/groups | ListCustomerGroups
[**retrieveCustomerGroup**](CustomerGroupsApi.md#retrieveCustomerGroup) | **GET** /v2/customers/groups/{group_id} | RetrieveCustomerGroup
[**updateCustomerGroup**](CustomerGroupsApi.md#updateCustomerGroup) | **PUT** /v2/customers/groups/{group_id} | UpdateCustomerGroup



## createCustomerGroup

> CreateCustomerGroupResponse createCustomerGroup(createCustomerGroupRequest)

CreateCustomerGroup

Creates a new customer group for a business.  The request must include the &#x60;name&#x60; value of the group.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomerGroupsApi();
let createCustomerGroupRequest = new SquareConnectApi.CreateCustomerGroupRequest(); // CreateCustomerGroupRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createCustomerGroup(createCustomerGroupRequest, (error, data, response) => {
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
 **createCustomerGroupRequest** | [**CreateCustomerGroupRequest**](CreateCustomerGroupRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateCustomerGroupResponse**](CreateCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCustomerGroup

> DeleteCustomerGroupResponse deleteCustomerGroup(groupId)

DeleteCustomerGroup

Deletes a customer group as identified by the &#x60;group_id&#x60; value.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomerGroupsApi();
let groupId = "groupId_example"; // String | The ID of the customer group to delete.
apiInstance.deleteCustomerGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| The ID of the customer group to delete. | 

### Return type

[**DeleteCustomerGroupResponse**](DeleteCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomerGroups

> ListCustomerGroupsResponse listCustomerGroups(opts)

ListCustomerGroups

Retrieves the list of customer groups of a business.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomerGroupsApi();
let opts = {
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
  'limit': 56 // Number | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
};
apiInstance.listCustomerGroups(opts, (error, data, response) => {
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
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
 **limit** | **Number**| The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 

### Return type

[**ListCustomerGroupsResponse**](ListCustomerGroupsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveCustomerGroup

> RetrieveCustomerGroupResponse retrieveCustomerGroup(groupId)

RetrieveCustomerGroup

Retrieves a specific customer group as identified by the &#x60;group_id&#x60; value.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomerGroupsApi();
let groupId = "groupId_example"; // String | The ID of the customer group to retrieve.
apiInstance.retrieveCustomerGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| The ID of the customer group to retrieve. | 

### Return type

[**RetrieveCustomerGroupResponse**](RetrieveCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCustomerGroup

> UpdateCustomerGroupResponse updateCustomerGroup(groupId, updateCustomerGroupRequest)

UpdateCustomerGroup

Updates a customer group as identified by the &#x60;group_id&#x60; value.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomerGroupsApi();
let groupId = "groupId_example"; // String | The ID of the customer group to update.
let updateCustomerGroupRequest = new SquareConnectApi.UpdateCustomerGroupRequest(); // UpdateCustomerGroupRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateCustomerGroup(groupId, updateCustomerGroupRequest, (error, data, response) => {
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
 **groupId** | **String**| The ID of the customer group to update. | 
 **updateCustomerGroupRequest** | [**UpdateCustomerGroupRequest**](UpdateCustomerGroupRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateCustomerGroupResponse**](UpdateCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

