# OnSchedSetupApi.CustomersApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupV1CustomersGet**](CustomersApi.md#setupV1CustomersGet) | **GET** /setup/v1/customers | List Customers
[**setupV1CustomersIdGet**](CustomersApi.md#setupV1CustomersIdGet) | **GET** /setup/v1/customers/{id} | Get Customer
[**setupV1CustomersIdPrivacyGet**](CustomersApi.md#setupV1CustomersIdPrivacyGet) | **GET** /setup/v1/customers/{id}/privacy | Get Customer Data



## setupV1CustomersGet

> CustomerListViewModel setupV1CustomersGet(opts)

List Customers

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Customers&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.CustomersApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'groupId': "groupId_example", // String | Filter by groupId
  'email': "email_example", // String | Filter by email address.
  'lastname': "lastname_example", // String | Search by lastname.
  'deleted': true, // Boolean | Filter by deleted status.
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1CustomersGet(opts, (error, data, response) => {
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
 **locationId** | **String**| id of business location, defaults to primary business location | [optional] 
 **groupId** | **String**| Filter by groupId | [optional] 
 **email** | **String**| Filter by email address. | [optional] 
 **lastname** | **String**| Search by lastname. | [optional] 
 **deleted** | **Boolean**| Filter by deleted status. | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**CustomerListViewModel**](CustomerListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1CustomersIdGet

> CustomerViewModel setupV1CustomersIdGet(id)

Get Customer

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s by using the &lt;i&gt;GET /setup/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.CustomersApi();
let id = "id_example"; // String | id of customer object
apiInstance.setupV1CustomersIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of customer object | 

### Return type

[**CustomerViewModel**](CustomerViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1CustomersIdPrivacyGet

> CustomerPrivacyViewModel setupV1CustomersIdPrivacyGet(id)

Get Customer Data

&lt;p&gt;Use this endpoint to return the &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s using the &lt;i&gt;GET /setup/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.CustomersApi();
let id = "id_example"; // String | id of customer object
apiInstance.setupV1CustomersIdPrivacyGet(id, (error, data, response) => {
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
 **id** | **String**| id of customer object | 

### Return type

[**CustomerPrivacyViewModel**](CustomerPrivacyViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

