# TicketsApi

All URIs are relative to *http://api.ss.solarvps.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ticketsDepartmentAddPost**](TicketsApi.md#ticketsDepartmentAddPost) | **POST** /tickets/{department}/add | Open ticket with desired department |
| [**ticketsGet**](TicketsApi.md#ticketsGet) | **GET** /tickets | View all your tickets |
| [**ticketsTicketIdGet**](TicketsApi.md#ticketsTicketIdGet) | **GET** /tickets/{ticketId} | View details on a specific ticket |
| [**ticketsTicketidUpdatePost**](TicketsApi.md#ticketsTicketidUpdatePost) | **POST** /tickets/{ticketid}/update | Post a reply to a ticket |


<a id="ticketsDepartmentAddPost"></a>
# **ticketsDepartmentAddPost**
> ticketsDepartmentAddPost(department, subject, contents)

Open ticket with desired department

Available departments are support, billing, sales

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    String department = "department_example"; // String | Department you want to open a ticket with
    String subject = "subject_example"; // String | Subject of the ticket you are opening
    String contents = "contents_example"; // String | Message reply being sent
    try {
      apiInstance.ticketsDepartmentAddPost(department, subject, contents);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketsDepartmentAddPost");
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
| **department** | **String**| Department you want to open a ticket with | |
| **subject** | **String**| Subject of the ticket you are opening | |
| **contents** | **String**| Message reply being sent | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="ticketsGet"></a>
# **ticketsGet**
> ticketsGet()

View all your tickets

Shows all your tickets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    try {
      apiInstance.ticketsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="ticketsTicketIdGet"></a>
# **ticketsTicketIdGet**
> ticketsTicketIdGet(ticketId)

View details on a specific ticket

Shows all information of a specific ticketId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    BigDecimal ticketId = new BigDecimal(78); // BigDecimal | TicketId you want to see
    try {
      apiInstance.ticketsTicketIdGet(ticketId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketsTicketIdGet");
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
| **ticketId** | **BigDecimal**| TicketId you want to see | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="ticketsTicketidUpdatePost"></a>
# **ticketsTicketidUpdatePost**
> ticketsTicketidUpdatePost(ticketid, contents)

Post a reply to a ticket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    TicketsApi apiInstance = new TicketsApi(defaultClient);
    BigDecimal ticketid = new BigDecimal(78); // BigDecimal | TicketId of the ticket you want to post an update to
    String contents = "contents_example"; // String | Message reply being sent
    try {
      apiInstance.ticketsTicketidUpdatePost(ticketid, contents);
    } catch (ApiException e) {
      System.err.println("Exception when calling TicketsApi#ticketsTicketidUpdatePost");
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
| **ticketid** | **BigDecimal**| TicketId of the ticket you want to post an update to | |
| **contents** | **String**| Message reply being sent | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

