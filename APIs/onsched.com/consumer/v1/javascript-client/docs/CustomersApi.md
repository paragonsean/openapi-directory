# OnSchedConsumerApi.CustomersApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerV1CustomersBookingfieldsGet**](CustomersApi.md#consumerV1CustomersBookingfieldsGet) | **GET** /consumer/v1/customers/bookingfields | Get Customer Booking Fields
[**consumerV1CustomersCountriesGet**](CustomersApi.md#consumerV1CustomersCountriesGet) | **GET** /consumer/v1/customers/countries | List Country Codes
[**consumerV1CustomersCustomfieldsGet**](CustomersApi.md#consumerV1CustomersCustomfieldsGet) | **GET** /consumer/v1/customers/customfields | Get Customer Custom Fields
[**consumerV1CustomersGet**](CustomersApi.md#consumerV1CustomersGet) | **GET** /consumer/v1/customers | List Customers
[**consumerV1CustomersIdDelete**](CustomersApi.md#consumerV1CustomersIdDelete) | **DELETE** /consumer/v1/customers/{id} | Delete Customer
[**consumerV1CustomersIdGet**](CustomersApi.md#consumerV1CustomersIdGet) | **GET** /consumer/v1/customers/{id} | Get Customer
[**consumerV1CustomersIdPut**](CustomersApi.md#consumerV1CustomersIdPut) | **PUT** /consumer/v1/customers/{id} | Update Customer
[**consumerV1CustomersPost**](CustomersApi.md#consumerV1CustomersPost) | **POST** /consumer/v1/customers | Create Customer
[**consumerV1CustomersStatesGet**](CustomersApi.md#consumerV1CustomersStatesGet) | **GET** /consumer/v1/customers/states | List Country States



## consumerV1CustomersBookingfieldsGet

> BookingFieldListViewModel consumerV1CustomersBookingfieldsGet(opts)

Get Customer Booking Fields

&lt;p&gt;Use this endpoint to return &lt;b&gt;Customer Booking Fields&lt;/b&gt;. Customer booking fields are stored with each customer object. They are used when the information collected during the booking is for a particular customer. Customer Booking Fields include any custom customer fields you define and want to capture with the Booking.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let opts = {
  'locationId': "locationId_example" // String | id of business location, defaults to primary business location
};
apiInstance.consumerV1CustomersBookingfieldsGet(opts, (error, data, response) => {
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

### Return type

[**BookingFieldListViewModel**](BookingFieldListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1CustomersCountriesGet

> [CountryViewModel] consumerV1CustomersCountriesGet()

List Country Codes

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Countries with their associated Country Code&lt;/b&gt;. Country codes are based on the 2-character ANSI standard. If your countries of operation are not currently listed, contact us at &lt;i&gt;&lt;b&gt;support@onsched.com&lt;/b&gt;&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
apiInstance.consumerV1CustomersCountriesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[CountryViewModel]**](CountryViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1CustomersCustomfieldsGet

> CustomFieldDefinitionListViewModel consumerV1CustomersCustomfieldsGet(opts)

Get Customer Custom Fields

&lt;p&gt;Use this endpoint to return &lt;b&gt;Customer Custom Fields&lt;/b&gt;. Customer custom fields are stored with the customer object. They are used when the information collected during the booking is specific to a particular customer.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'leadQuestions': true // Boolean | A true/false indicator to filter on custom fields used for lead questions
};
apiInstance.consumerV1CustomersCustomfieldsGet(opts, (error, data, response) => {
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
 **leadQuestions** | **Boolean**| A true/false indicator to filter on custom fields used for lead questions | [optional] 

### Return type

[**CustomFieldDefinitionListViewModel**](CustomFieldDefinitionListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1CustomersGet

> CustomerListViewModel consumerV1CustomersGet(opts)

List Customers

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Customers&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'groupId': "groupId_example", // String | Filter by groupId
  'email': "email_example", // String | Filter by email address
  'lastname': "lastname_example", // String | Filter by lastname
  'deleted': true, // Boolean | Filter by deleted status
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.consumerV1CustomersGet(opts, (error, data, response) => {
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
 **email** | **String**| Filter by email address | [optional] 
 **lastname** | **String**| Filter by lastname | [optional] 
 **deleted** | **Boolean**| Filter by deleted status | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**CustomerListViewModel**](CustomerListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1CustomersIdDelete

> consumerV1CustomersIdDelete(id)

Delete Customer

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Customer object. A valid &lt;b&gt;customer id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let id = "id_example"; // String | id of customer object
apiInstance.consumerV1CustomersIdDelete(id, (error, data, response) => {
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
 **id** | **String**| id of customer object | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## consumerV1CustomersIdGet

> CustomerViewModel consumerV1CustomersIdGet(id)

Get Customer

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s by using the &lt;i&gt;GET /consumer/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let id = "id_example"; // String | id of customer object
apiInstance.consumerV1CustomersIdGet(id, (error, data, response) => {
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


## consumerV1CustomersIdPut

> consumerV1CustomersIdPut(id, opts)

Update Customer

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Customer object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Note: Blank fields are not changed.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let id = "id_example"; // String | id of customer object
let opts = {
  'customerUpdateModel': new OnSchedConsumerApi.CustomerUpdateModel() // CustomerUpdateModel | 
};
apiInstance.consumerV1CustomersIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| id of customer object | 
 **customerUpdateModel** | [**CustomerUpdateModel**](CustomerUpdateModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## consumerV1CustomersPost

> CustomerViewModel consumerV1CustomersPost(opts)

Create Customer

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new Customer. A customer object is automatically created with the first appointment booking if it doesn&#39;t already exist. If not specified, the business location id defaults to the primary business location.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt; or &lt;b&gt;First and Lastname&lt;/b&gt; depending on customer type. Type 0 &#x3D; Person, Type 1 &#x3D; Business. For type 0, the firstname and lastname fields are used. For type 1, the Name field is used, and the name field is also used to populate the lastname.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let opts = {
  'customerInputModel': new OnSchedConsumerApi.CustomerInputModel() // CustomerInputModel | 
};
apiInstance.consumerV1CustomersPost(opts, (error, data, response) => {
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
 **customerInputModel** | [**CustomerInputModel**](CustomerInputModel.md)|  | [optional] 

### Return type

[**CustomerViewModel**](CustomerViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## consumerV1CustomersStatesGet

> [StateViewModel] consumerV1CustomersStatesGet(opts)

List Country States

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Countries with their associated State Codes&lt;/b&gt;. Supply a country code to filter results further. If states for your countries of operation are not currently listed, contact us at &lt;i&gt;&lt;b&gt;support@onsched.com&lt;/b&gt;&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.CustomersApi();
let opts = {
  'country': "country_example" // String | 
};
apiInstance.consumerV1CustomersStatesGet(opts, (error, data, response) => {
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
 **country** | **String**|  | [optional] 

### Return type

[**[StateViewModel]**](StateViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

