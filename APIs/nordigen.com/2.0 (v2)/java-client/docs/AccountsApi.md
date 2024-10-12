# AccountsApi

All URIs are relative to *https://ob.nordigen.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveAccountBalancesV2**](AccountsApi.md#retrieveAccountBalancesV2) | **GET** /api/v2/accounts/{id}/balances/ |  |
| [**retrieveAccountDetailsV2**](AccountsApi.md#retrieveAccountDetailsV2) | **GET** /api/v2/accounts/{id}/details/ |  |
| [**retrieveAccountMetadata**](AccountsApi.md#retrieveAccountMetadata) | **GET** /api/v2/accounts/{id}/ |  |
| [**retrieveAccountTransactionsV22**](AccountsApi.md#retrieveAccountTransactionsV22) | **GET** /api/v2/accounts/{id}/transactions/ |  |


<a id="retrieveAccountBalancesV2"></a>
# **retrieveAccountBalancesV2**
> Map&lt;String, Object&gt; retrieveAccountBalancesV2(id)



Access account balances.  Balances will be returned in Berlin Group PSD2 format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      Map<String, Object> result = apiInstance.retrieveAccountBalancesV2(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#retrieveAccountBalancesV2");
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
| **id** | **UUID**|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve account balances |  -  |
| **400** | Date range error |  -  |
| **401** | Failed Authentication |  -  |
| **403** | Account Access Forbidden |  -  |
| **404** | Account not found error |  -  |
| **409** | Account state error |  -  |
| **429** | Rate Limit Error |  -  |
| **500** | Unknown Request Error |  -  |
| **503** | Connection Error |  -  |

<a id="retrieveAccountDetailsV2"></a>
# **retrieveAccountDetailsV2**
> Map&lt;String, Object&gt; retrieveAccountDetailsV2(id)



Access account details.  Account details will be returned in Berlin Group PSD2 format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      Map<String, Object> result = apiInstance.retrieveAccountDetailsV2(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#retrieveAccountDetailsV2");
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
| **id** | **UUID**|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve account details |  -  |
| **400** | Date range error |  -  |
| **401** | Failed Authentication |  -  |
| **403** | Account Access Forbidden |  -  |
| **404** | Account not found error |  -  |
| **409** | Account state error |  -  |
| **429** | Rate Limit Error |  -  |
| **500** | Unknown Request Error |  -  |
| **503** | Connection Error |  -  |

<a id="retrieveAccountMetadata"></a>
# **retrieveAccountMetadata**
> Account retrieveAccountMetadata(id)



Access account metadata.  Information about the account record, such as the processing status and IBAN.  Account status is recalculated based on the error count in the latest req.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      Account result = apiInstance.retrieveAccountMetadata(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#retrieveAccountMetadata");
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
| **id** | **UUID**|  | |

### Return type

[**Account**](Account.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | sample account metadata |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Account not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="retrieveAccountTransactionsV22"></a>
# **retrieveAccountTransactionsV22**
> Map&lt;String, Object&gt; retrieveAccountTransactionsV22(id, dateFrom, dateTo)



Access account transactions.  Transactions will be returned in Berlin Group PSD2 format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    LocalDate dateFrom = LocalDate.parse("2023-01-21"); // LocalDate | 
    LocalDate dateTo = LocalDate.parse("2023-04-21"); // LocalDate | 
    try {
      Map<String, Object> result = apiInstance.retrieveAccountTransactionsV22(id, dateFrom, dateTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#retrieveAccountTransactionsV22");
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
| **id** | **UUID**|  | |
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve account transactions |  -  |
| **400** | Date range error |  -  |
| **401** | Failed Authentication |  -  |
| **403** | Account Access Forbidden |  -  |
| **404** | Account not found error |  -  |
| **409** | Account state error |  -  |
| **429** | Rate Limit Error |  -  |
| **500** | Unknown Request Error |  -  |
| **503** | Connection Error |  -  |

