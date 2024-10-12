# SquareConnectApi.CustomersApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addGroupToCustomer**](CustomersApi.md#addGroupToCustomer) | **PUT** /v2/customers/{customer_id}/groups/{group_id} | AddGroupToCustomer
[**createCustomer**](CustomersApi.md#createCustomer) | **POST** /v2/customers | CreateCustomer
[**createCustomerCard**](CustomersApi.md#createCustomerCard) | **POST** /v2/customers/{customer_id}/cards | CreateCustomerCard
[**deleteCustomer**](CustomersApi.md#deleteCustomer) | **DELETE** /v2/customers/{customer_id} | DeleteCustomer
[**deleteCustomerCard**](CustomersApi.md#deleteCustomerCard) | **DELETE** /v2/customers/{customer_id}/cards/{card_id} | DeleteCustomerCard
[**listCustomers**](CustomersApi.md#listCustomers) | **GET** /v2/customers | ListCustomers
[**removeGroupFromCustomer**](CustomersApi.md#removeGroupFromCustomer) | **DELETE** /v2/customers/{customer_id}/groups/{group_id} | RemoveGroupFromCustomer
[**retrieveCustomer**](CustomersApi.md#retrieveCustomer) | **GET** /v2/customers/{customer_id} | RetrieveCustomer
[**searchCustomers**](CustomersApi.md#searchCustomers) | **POST** /v2/customers/search | SearchCustomers
[**updateCustomer**](CustomersApi.md#updateCustomer) | **PUT** /v2/customers/{customer_id} | UpdateCustomer



## addGroupToCustomer

> AddGroupToCustomerResponse addGroupToCustomer(customerId, groupId)

AddGroupToCustomer

Adds a group membership to a customer.  The customer is identified by the &#x60;customer_id&#x60; value and the customer group is identified by the &#x60;group_id&#x60; value.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let customerId = "customerId_example"; // String | The ID of the customer to add to a group.
let groupId = "groupId_example"; // String | The ID of the customer group to add the customer to.
apiInstance.addGroupToCustomer(customerId, groupId, (error, data, response) => {
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
 **customerId** | **String**| The ID of the customer to add to a group. | 
 **groupId** | **String**| The ID of the customer group to add the customer to. | 

### Return type

[**AddGroupToCustomerResponse**](AddGroupToCustomerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createCustomer

> CreateCustomerResponse createCustomer(createCustomerRequest)

CreateCustomer

Creates a new customer for a business.  You must provide at least one of the following values in your request to this endpoint:  - &#x60;given_name&#x60; - &#x60;family_name&#x60; - &#x60;company_name&#x60; - &#x60;email_address&#x60; - &#x60;phone_number&#x60;

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let createCustomerRequest = new SquareConnectApi.CreateCustomerRequest(); // CreateCustomerRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createCustomer(createCustomerRequest, (error, data, response) => {
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
 **createCustomerRequest** | [**CreateCustomerRequest**](CreateCustomerRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateCustomerResponse**](CreateCustomerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCustomerCard

> CreateCustomerCardResponse createCustomerCard(customerId, createCustomerCardRequest)

CreateCustomerCard

Adds a card on file to an existing customer.  As with charges, calls to &#x60;CreateCustomerCard&#x60; are idempotent. Multiple calls with the same card nonce return the same card record that was created with the provided nonce during the _first_ call.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let customerId = "customerId_example"; // String | The Square ID of the customer profile the card is linked to.
let createCustomerCardRequest = new SquareConnectApi.CreateCustomerCardRequest(); // CreateCustomerCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createCustomerCard(customerId, createCustomerCardRequest, (error, data, response) => {
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
 **customerId** | **String**| The Square ID of the customer profile the card is linked to. | 
 **createCustomerCardRequest** | [**CreateCustomerCardRequest**](CreateCustomerCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateCustomerCardResponse**](CreateCustomerCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCustomer

> DeleteCustomerResponse deleteCustomer(customerId, opts)

DeleteCustomer

Deletes a customer profile from a business. This operation also unlinks any associated cards on file.   As a best practice, you should include the &#x60;version&#x60; field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.   To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let customerId = "customerId_example"; // String | The ID of the customer to delete.
let opts = {
  'version': 789 // Number | The current version of the customer profile.  As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile).
};
apiInstance.deleteCustomer(customerId, opts, (error, data, response) => {
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
 **customerId** | **String**| The ID of the customer to delete. | 
 **version** | **Number**| The current version of the customer profile.  As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile). | [optional] 

### Return type

[**DeleteCustomerResponse**](DeleteCustomerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCustomerCard

> DeleteCustomerCardResponse deleteCustomerCard(customerId, cardId)

DeleteCustomerCard

Removes a card on file from a customer.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let customerId = "customerId_example"; // String | The ID of the customer that the card on file belongs to.
let cardId = "cardId_example"; // String | The ID of the card on file to delete.
apiInstance.deleteCustomerCard(customerId, cardId, (error, data, response) => {
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
 **customerId** | **String**| The ID of the customer that the card on file belongs to. | 
 **cardId** | **String**| The ID of the card on file to delete. | 

### Return type

[**DeleteCustomerCardResponse**](DeleteCustomerCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomers

> ListCustomersResponse listCustomers(opts)

ListCustomers

Lists customer profiles associated with a Square account.  Under normal operating conditions, newly created or updated customer profiles become available for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to one minute or longer, especially during network incidents and outages.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let opts = {
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
  'limit': 56, // Number | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 100. The default value is 100.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
  'sortField': "sortField_example", // String | Indicates how customers should be sorted.  The default value is `DEFAULT`.
  'sortOrder': "sortOrder_example" // String | Indicates whether customers should be sorted in ascending (`ASC`) or descending (`DESC`) order.  The default value is `ASC`.
};
apiInstance.listCustomers(opts, (error, data, response) => {
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
 **limit** | **Number**| The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 100. The default value is 100.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
 **sortField** | **String**| Indicates how customers should be sorted.  The default value is &#x60;DEFAULT&#x60;. | [optional] 
 **sortOrder** | **String**| Indicates whether customers should be sorted in ascending (&#x60;ASC&#x60;) or descending (&#x60;DESC&#x60;) order.  The default value is &#x60;ASC&#x60;. | [optional] 

### Return type

[**ListCustomersResponse**](ListCustomersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeGroupFromCustomer

> RemoveGroupFromCustomerResponse removeGroupFromCustomer(customerId, groupId)

RemoveGroupFromCustomer

Removes a group membership from a customer.  The customer is identified by the &#x60;customer_id&#x60; value and the customer group is identified by the &#x60;group_id&#x60; value.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let customerId = "customerId_example"; // String | The ID of the customer to remove from the group.
let groupId = "groupId_example"; // String | The ID of the customer group to remove the customer from.
apiInstance.removeGroupFromCustomer(customerId, groupId, (error, data, response) => {
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
 **customerId** | **String**| The ID of the customer to remove from the group. | 
 **groupId** | **String**| The ID of the customer group to remove the customer from. | 

### Return type

[**RemoveGroupFromCustomerResponse**](RemoveGroupFromCustomerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveCustomer

> RetrieveCustomerResponse retrieveCustomer(customerId)

RetrieveCustomer

Returns details for a single customer.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let customerId = "customerId_example"; // String | The ID of the customer to retrieve.
apiInstance.retrieveCustomer(customerId, (error, data, response) => {
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
 **customerId** | **String**| The ID of the customer to retrieve. | 

### Return type

[**RetrieveCustomerResponse**](RetrieveCustomerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCustomers

> SearchCustomersResponse searchCustomers(searchCustomersRequest)

SearchCustomers

Searches the customer profiles associated with a Square account using a supported query filter.  Calling &#x60;SearchCustomers&#x60; without any explicit query filter returns all customer profiles ordered alphabetically based on &#x60;given_name&#x60; and &#x60;family_name&#x60;.  Under normal operating conditions, newly created or updated customer profiles become available for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to one minute or longer, especially during network incidents and outages.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let searchCustomersRequest = new SquareConnectApi.SearchCustomersRequest(); // SearchCustomersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchCustomers(searchCustomersRequest, (error, data, response) => {
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
 **searchCustomersRequest** | [**SearchCustomersRequest**](SearchCustomersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchCustomersResponse**](SearchCustomersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCustomer

> UpdateCustomerResponse updateCustomer(customerId, updateCustomerRequest)

UpdateCustomer

Updates a customer profile. To change an attribute, specify the new value. To remove an attribute, specify the value as an empty string or empty object.  As a best practice, you should include the &#x60;version&#x60; field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.  To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.  You cannot use this endpoint to change cards on file. To make changes, use the [Cards API](https://developer.squareup.com/reference/square_2021-08-18/cards-api) or [Gift Cards API](https://developer.squareup.com/reference/square_2021-08-18/gift-cards-api).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CustomersApi();
let customerId = "customerId_example"; // String | The ID of the customer to update.
let updateCustomerRequest = new SquareConnectApi.UpdateCustomerRequest(); // UpdateCustomerRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateCustomer(customerId, updateCustomerRequest, (error, data, response) => {
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
 **customerId** | **String**| The ID of the customer to update. | 
 **updateCustomerRequest** | [**UpdateCustomerRequest**](UpdateCustomerRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateCustomerResponse**](UpdateCustomerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

