# CustomersApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomer**](CustomersApi.md#createCustomer) | **POST** /customers | Create a new customer in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Customer&#39; model are those required to create a new customer |
| [**deleteCustomerById**](CustomersApi.md#deleteCustomerById) | **DELETE** /customers/{id} | Delete a customer associated with a given ID from your eCommerce system. Specifying a customer associated with a given ID that does not exist will result in an error message |
| [**getCustomerById**](CustomersApi.md#getCustomerById) | **GET** /customers/{id} | Retrieve a customer associated with a given ID from the eCommerce system. Specifying a customer with an ID that does not exist will result in an error response |
| [**getCustomers**](CustomersApi.md#getCustomers) | **GET** /customers | Find customers in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved |
| [**getCustomersOrders**](CustomersApi.md#getCustomersOrders) | **GET** /customers/{id}/orders | Find orders in the customer associated with a given ID. If the customer does not exist, an error response will be returned. If no orders are found in the given customer then an empty array will be returned |
| [**updateCustomerById**](CustomersApi.md#updateCustomerById) | **PATCH** /customers/{id} | Update an customer associated with a given ID in the eCommerce system.The update API uses the PATCH HTTP verb, so only those fields provided in the customer object will be updated, and those fields not provided will be left alone. Updating a customer with a specified ID that does not exist will result in an error response |


<a id="createCustomer"></a>
# **createCustomer**
> Customer createCustomer(authorization, customer)

Create a new customer in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Customer&#39; model are those required to create a new customer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    CustomerPost customer = new CustomerPost(); // CustomerPost | The customer object to be created
    try {
      Customer result = apiInstance.createCustomer(authorization, customer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#createCustomer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **customer** | [**CustomerPost**](CustomerPost.md)| The customer object to be created | |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="deleteCustomerById"></a>
# **deleteCustomerById**
> deleteCustomerById(authorization, id)

Delete a customer associated with a given ID from your eCommerce system. Specifying a customer associated with a given ID that does not exist will result in an error message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the customer to delete from the eCommerce system
    try {
      apiInstance.deleteCustomerById(authorization, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#deleteCustomerById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the customer to delete from the eCommerce system | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getCustomerById"></a>
# **getCustomerById**
> Customer getCustomerById(authorization, id)

Retrieve a customer associated with a given ID from the eCommerce system. Specifying a customer with an ID that does not exist will result in an error response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the customer to retrieve from the eCommerce system
    try {
      Customer result = apiInstance.getCustomerById(authorization, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#getCustomerById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the customer to retrieve from the eCommerce system | |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getCustomers"></a>
# **getCustomers**
> List&lt;Customer&gt; getCustomers(authorization, where, pageSize, nextPage, fields)

Find customers in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String where = "where_example"; // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field='value'). <p>Supported search terms: customer_id and customer_email. All other search criteria are ignored. NOTE: When searching by customer_id, do not quote the value (ex: customer_id=15693430), as the ID is a number rather than a string.  When searching by email, quote the value (ex: customer_email='a@b.c'), as the email parameter is a string
    Long pageSize = 56L; // Long | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<Customer> result = apiInstance.getCustomers(authorization, where, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#getCustomers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: customer_id and customer_email. All other search criteria are ignored. NOTE: When searching by customer_id, do not quote the value (ex: customer_id&#x3D;15693430), as the ID is a number rather than a string.  When searching by email, quote the value (ex: customer_email&#x3D;&#39;a@b.c&#39;), as the email parameter is a string | [optional] |
| **pageSize** | **Long**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;Customer&gt;**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getCustomersOrders"></a>
# **getCustomersOrders**
> List&lt;Order&gt; getCustomersOrders(authorization, id, pageSize, nextPage, fields)

Find orders in the customer associated with a given ID. If the customer does not exist, an error response will be returned. If no orders are found in the given customer then an empty array will be returned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the customer to get orders form in the eCommerce system
    Long pageSize = 56L; // Long | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<Order> result = apiInstance.getCustomersOrders(authorization, id, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#getCustomersOrders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the customer to get orders form in the eCommerce system | |
| **pageSize** | **Long**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;Order&gt;**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="updateCustomerById"></a>
# **updateCustomerById**
> Customer updateCustomerById(authorization, id, customer)

Update an customer associated with a given ID in the eCommerce system.The update API uses the PATCH HTTP verb, so only those fields provided in the customer object will be updated, and those fields not provided will be left alone. Updating a customer with a specified ID that does not exist will result in an error response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the customer to update in the eCommerce system
    CustomerPatch customer = new CustomerPatch(); // CustomerPatch | The customer object to be created
    try {
      Customer result = apiInstance.updateCustomerById(authorization, id, customer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#updateCustomerById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the customer to update in the eCommerce system | |
| **customer** | [**CustomerPatch**](CustomerPatch.md)| The customer object to be created | |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

