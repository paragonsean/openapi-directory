# Class2AccountApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccount**](Class2AccountApi.md#getAccount) | **GET** /account |  |
| [**getAccountBalance**](Class2AccountApi.md#getAccountBalance) | **GET** /account/{accountNo} |  |
| [**getTransactions**](Class2AccountApi.md#getTransactions) | **POST** /account/{accountNo}/transactions |  |
| [**showLastTenTransactions**](Class2AccountApi.md#showLastTenTransactions) | **GET** /account/{accountNo}/transactions |  |


<a id="getAccount"></a>
# **getAccount**
> getAccount(authorization)



Returns a list of all the accounts owned by the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class2AccountApi apiInstance = new Class2AccountApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    try {
      apiInstance.getAccount(authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2AccountApi#getAccount");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |

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
| **200** | Successful operation |  -  |
| **401** | Unauthorized request |  -  |
| **500** | Internal server error |  -  |

<a id="getAccountBalance"></a>
# **getAccountBalance**
> getAccountBalance(authorization, accountNo)



Returns details about a specific account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class2AccountApi apiInstance = new Class2AccountApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    String accountNo = "accountNo_example"; // String | Account id
    try {
      apiInstance.getAccountBalance(authorization, accountNo);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2AccountApi#getAccountBalance");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |
| **accountNo** | **String**| Account id | |

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
| **200** | Successful operation |  -  |
| **401** | Unauthorized request |  -  |
| **500** | Internal server error |  -  |

<a id="getTransactions"></a>
# **getTransactions**
> getTransactions(authorization, accountNo, body)



Return transactions between 2 specific dates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class2AccountApi apiInstance = new Class2AccountApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    String accountNo = "accountNo_example"; // String | Account id
    Dates body = new Dates(); // Dates | A start date and an end date
    try {
      apiInstance.getTransactions(authorization, accountNo, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2AccountApi#getTransactions");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |
| **accountNo** | **String**| Account id | |
| **body** | [**Dates**](Dates.md)| A start date and an end date | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad parameters: Please check provided values |  -  |
| **401** | Unauthorized request |  -  |
| **501** | Internal server error |  -  |

<a id="showLastTenTransactions"></a>
# **showLastTenTransactions**
> showLastTenTransactions(authorization, accountNo)



Returns the last 10 transactions attached to an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class2AccountApi apiInstance = new Class2AccountApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    String accountNo = "accountNo_example"; // String | Account id
    try {
      apiInstance.showLastTenTransactions(authorization, accountNo);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2AccountApi#showLastTenTransactions");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |
| **accountNo** | **String**| Account id | |

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
| **200** | Successful operation |  -  |
| **401** | Unauthorized request |  -  |
| **500** | Internal server error |  -  |

