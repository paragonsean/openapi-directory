# FinancialStatisticsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**financialStatisticsWorkingHoursGet**](FinancialStatisticsApi.md#financialStatisticsWorkingHoursGet) | **GET** /financial_statistics/workingHours | Get Total working hours grouped by time entry type |
| [**getExpensesSalesPrice**](FinancialStatisticsApi.md#getExpensesSalesPrice) | **GET** /financial_statistics/expensesSalesPrice | Get expenses sales price |
| [**getFinancialStatistics**](FinancialStatisticsApi.md#getFinancialStatistics) | **GET** /financial_statistics | Get general statistics |
| [**getFinancialStatisticsOverview**](FinancialStatisticsApi.md#getFinancialStatisticsOverview) | **GET** /financial_statistics/overview | Get statistics overview |
| [**getInvoicedAmount**](FinancialStatisticsApi.md#getInvoicedAmount) | **GET** /financial_statistics/invoicedAmount | Get invoiced amount |
| [**getMargin**](FinancialStatisticsApi.md#getMargin) | **GET** /financial_statistics/margin | Get margin |
| [**getMaterialRentalsCostPrice**](FinancialStatisticsApi.md#getMaterialRentalsCostPrice) | **GET** /financial_statistics/materialRentalsCostPrice | Get products material rentals cost price |
| [**getProductsCostPrice**](FinancialStatisticsApi.md#getProductsCostPrice) | **GET** /financial_statistics/productsCostPrice | Get products cost price |


<a id="financialStatisticsWorkingHoursGet"></a>
# **financialStatisticsWorkingHoursGet**
> FinancialStatisticsWorkingHoursGet200Response financialStatisticsWorkingHoursGet(dateFrom, dateTo, projectId)

Get Total working hours grouped by time entry type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      FinancialStatisticsWorkingHoursGet200Response result = apiInstance.financialStatisticsWorkingHoursGet(dateFrom, dateTo, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#financialStatisticsWorkingHoursGet");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |

### Return type

[**FinancialStatisticsWorkingHoursGet200Response**](FinancialStatisticsWorkingHoursGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getExpensesSalesPrice"></a>
# **getExpensesSalesPrice**
> GetExpensesSalesPrice200Response getExpensesSalesPrice(dateFrom, dateTo, projectId)

Get expenses sales price

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetExpensesSalesPrice200Response result = apiInstance.getExpensesSalesPrice(dateFrom, dateTo, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#getExpensesSalesPrice");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |

### Return type

[**GetExpensesSalesPrice200Response**](GetExpensesSalesPrice200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFinancialStatistics"></a>
# **getFinancialStatistics**
> GetFinancialStatistics200Response getFinancialStatistics(dateFrom, dateTo, projectId, projectStatusIds, onlyNotInvoiced, details)

Get general statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    UUID projectStatusIds = UUID.randomUUID(); // UUID | 
    Boolean onlyNotInvoiced = true; // Boolean | 
    Boolean details = true; // Boolean | 
    try {
      GetFinancialStatistics200Response result = apiInstance.getFinancialStatistics(dateFrom, dateTo, projectId, projectStatusIds, onlyNotInvoiced, details);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#getFinancialStatistics");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |
| **projectStatusIds** | **UUID**|  | [optional] |
| **onlyNotInvoiced** | **Boolean**|  | [optional] |
| **details** | **Boolean**|  | [optional] |

### Return type

[**GetFinancialStatistics200Response**](GetFinancialStatistics200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFinancialStatisticsOverview"></a>
# **getFinancialStatisticsOverview**
> GetFinancialStatisticsOverview200Response getFinancialStatisticsOverview(dateFrom, dateTo, projectId)

Get statistics overview

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetFinancialStatisticsOverview200Response result = apiInstance.getFinancialStatisticsOverview(dateFrom, dateTo, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#getFinancialStatisticsOverview");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |

### Return type

[**GetFinancialStatisticsOverview200Response**](GetFinancialStatisticsOverview200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getInvoicedAmount"></a>
# **getInvoicedAmount**
> GetInvoicedAmount200Response getInvoicedAmount(dateFrom, dateTo, projectId)

Get invoiced amount

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetInvoicedAmount200Response result = apiInstance.getInvoicedAmount(dateFrom, dateTo, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#getInvoicedAmount");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |

### Return type

[**GetInvoicedAmount200Response**](GetInvoicedAmount200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getMargin"></a>
# **getMargin**
> GetMargin200Response getMargin(dateFrom, dateTo, projectId)

Get margin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetMargin200Response result = apiInstance.getMargin(dateFrom, dateTo, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#getMargin");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |

### Return type

[**GetMargin200Response**](GetMargin200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getMaterialRentalsCostPrice"></a>
# **getMaterialRentalsCostPrice**
> GetMaterialRentalsCostPrice200Response getMaterialRentalsCostPrice(dateFrom, dateTo, projectId)

Get products material rentals cost price

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetMaterialRentalsCostPrice200Response result = apiInstance.getMaterialRentalsCostPrice(dateFrom, dateTo, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#getMaterialRentalsCostPrice");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |

### Return type

[**GetMaterialRentalsCostPrice200Response**](GetMaterialRentalsCostPrice200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProductsCostPrice"></a>
# **getProductsCostPrice**
> GetProductsCostPrice200Response getProductsCostPrice(dateFrom, dateTo, projectId)

Get products cost price

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    FinancialStatisticsApi apiInstance = new FinancialStatisticsApi(defaultClient);
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    try {
      GetProductsCostPrice200Response result = apiInstance.getProductsCostPrice(dateFrom, dateTo, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialStatisticsApi#getProductsCostPrice");
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
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |

### Return type

[**GetProductsCostPrice200Response**](GetProductsCostPrice200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

