# CustomersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customersGetCustomerLocationListCustomerIdlocations**](CustomersApi.md#customersGetCustomerLocationListCustomerIdlocations) | **GET** /api/v3/Customers/{customerId}/locations | Gets a list of locations for the specified customer |
| [**customersGetList**](CustomersApi.md#customersGetList) | **GET** /api/v3/Customers | Gets a list of customers |


<a id="customersGetCustomerLocationListCustomerIdlocations"></a>
# **customersGetCustomerLocationListCustomerIdlocations**
> List&lt;CustomerLocationItemDto&gt; customersGetCustomerLocationListCustomerIdlocations(customerId)

Gets a list of locations for the specified customer

Sample rquest:                GET /customers/10000/locations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String customerId = "customerId_example"; // String | The customer id (CustomerCd) to retrieve locations for
    try {
      List<CustomerLocationItemDto> result = apiInstance.customersGetCustomerLocationListCustomerIdlocations(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGetCustomerLocationListCustomerIdlocations");
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
| **customerId** | **String**| The customer id (CustomerCd) to retrieve locations for | |

### Return type

[**List&lt;CustomerLocationItemDto&gt;**](CustomerLocationItemDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of locations for the specified customer |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If customer with id customerId is not found or is not accessible |  -  |

<a id="customersGetList"></a>
# **customersGetList**
> CustomerDtoPagedResult customersGetList(filter, pageSize, pageIndex)

Gets a list of customers

Sample request:                GET /customers?filter&#x3D;visma&amp;pageSize&#x3D;10

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String filter = "filter_example"; // String | An optional text string to find customers matching (searching fields id, name, gln, tax registration id). If not specified all customers are returned.
    Integer pageSize = 100; // Integer | The number of customers retrieved per page. If not specified, the default value of 100 will be used.
    Integer pageIndex = 0; // Integer | The zero based page index to retrieve
    try {
      CustomerDtoPagedResult result = apiInstance.customersGetList(filter, pageSize, pageIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customersGetList");
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
| **filter** | **String**| An optional text string to find customers matching (searching fields id, name, gln, tax registration id). If not specified all customers are returned. | [optional] |
| **pageSize** | **Integer**| The number of customers retrieved per page. If not specified, the default value of 100 will be used. | [optional] [default to 100] |
| **pageIndex** | **Integer**| The zero based page index to retrieve | [optional] [default to 0] |

### Return type

[**CustomerDtoPagedResult**](CustomerDtoPagedResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of customers found |  -  |
| **400** | If pageSize or pageIndex is not within the allowed range |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

