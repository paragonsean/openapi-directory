# Ecwid.CustomersApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomer**](CustomersApi.md#createCustomer) | **POST** /customers | Create a new customer in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Customer&#39; model are those required to create a new customer
[**deleteCustomerById**](CustomersApi.md#deleteCustomerById) | **DELETE** /customers/{id} | Delete a customer associated with a given ID from your eCommerce system. Specifying a customer associated with a given ID that does not exist will result in an error message
[**getCustomerById**](CustomersApi.md#getCustomerById) | **GET** /customers/{id} | Retrieve a customer associated with a given ID from the eCommerce system. Specifying a customer with an ID that does not exist will result in an error response
[**getCustomers**](CustomersApi.md#getCustomers) | **GET** /customers | Find customers in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved
[**getCustomersOrders**](CustomersApi.md#getCustomersOrders) | **GET** /customers/{id}/orders | Find orders in the customer associated with a given ID. If the customer does not exist, an error response will be returned. If no orders are found in the given customer then an empty array will be returned
[**updateCustomerById**](CustomersApi.md#updateCustomerById) | **PATCH** /customers/{id} | Update an customer associated with a given ID in the eCommerce system.The update API uses the PATCH HTTP verb, so only those fields provided in the customer object will be updated, and those fields not provided will be left alone. Updating a customer with a specified ID that does not exist will result in an error response



## createCustomer

> Customer createCustomer(authorization, customer)

Create a new customer in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Customer&#39; model are those required to create a new customer

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.CustomersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let customer = new Ecwid.CustomerPost(); // CustomerPost | The customer object to be created
apiInstance.createCustomer(authorization, customer, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **customer** | [**CustomerPost**](CustomerPost.md)| The customer object to be created | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteCustomerById

> deleteCustomerById(authorization, id)

Delete a customer associated with a given ID from your eCommerce system. Specifying a customer associated with a given ID that does not exist will result in an error message

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.CustomersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the customer to delete from the eCommerce system
apiInstance.deleteCustomerById(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the customer to delete from the eCommerce system | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCustomerById

> Customer getCustomerById(authorization, id)

Retrieve a customer associated with a given ID from the eCommerce system. Specifying a customer with an ID that does not exist will result in an error response

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.CustomersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the customer to retrieve from the eCommerce system
apiInstance.getCustomerById(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the customer to retrieve from the eCommerce system | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getCustomers

> [Customer] getCustomers(authorization, opts)

Find customers in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.CustomersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let opts = {
  'where': "where_example", // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field='value'). <p>Supported search terms: customer_id and customer_email. All other search criteria are ignored. NOTE: When searching by customer_id, do not quote the value (ex: customer_id=15693430), as the ID is a number rather than a string.  When searching by email, quote the value (ex: customer_email='a@b.c'), as the email parameter is a string
  'pageSize': 789, // Number | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getCustomers(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: customer_id and customer_email. All other search criteria are ignored. NOTE: When searching by customer_id, do not quote the value (ex: customer_id&#x3D;15693430), as the ID is a number rather than a string.  When searching by email, quote the value (ex: customer_email&#x3D;&#39;a@b.c&#39;), as the email parameter is a string | [optional] 
 **pageSize** | **Number**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[Customer]**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getCustomersOrders

> [Order] getCustomersOrders(authorization, id, opts)

Find orders in the customer associated with a given ID. If the customer does not exist, an error response will be returned. If no orders are found in the given customer then an empty array will be returned

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.CustomersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the customer to get orders form in the eCommerce system
let opts = {
  'pageSize': 789, // Number | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getCustomersOrders(authorization, id, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the customer to get orders form in the eCommerce system | 
 **pageSize** | **Number**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[Order]**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateCustomerById

> Customer updateCustomerById(authorization, id, customer)

Update an customer associated with a given ID in the eCommerce system.The update API uses the PATCH HTTP verb, so only those fields provided in the customer object will be updated, and those fields not provided will be left alone. Updating a customer with a specified ID that does not exist will result in an error response

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.CustomersApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the customer to update in the eCommerce system
let customer = new Ecwid.CustomerPatch(); // CustomerPatch | The customer object to be created
apiInstance.updateCustomerById(authorization, id, customer, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the customer to update in the eCommerce system | 
 **customer** | [**CustomerPatch**](CustomerPatch.md)| The customer object to be created | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

