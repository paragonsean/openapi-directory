# ExpenseLinesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expenseLinesExpenseLineIdDelete**](ExpenseLinesApi.md#expenseLinesExpenseLineIdDelete) | **DELETE** /expense_lines/{expense_line_id} | Delete expense line |
| [**expenseLinesExpenseLineIdGet**](ExpenseLinesApi.md#expenseLinesExpenseLineIdGet) | **GET** /expense_lines/{expense_line_id} | Show expense line |
| [**expenseLinesExpenseLineIdPut**](ExpenseLinesApi.md#expenseLinesExpenseLineIdPut) | **PUT** /expense_lines/{expense_line_id} | Edit expense line |
| [**expenseLinesGet**](ExpenseLinesApi.md#expenseLinesGet) | **GET** /expense_lines | Show list of expense lines |
| [**expenseLinesPost**](ExpenseLinesApi.md#expenseLinesPost) | **POST** /expense_lines | Add line to expense |


<a id="expenseLinesExpenseLineIdDelete"></a>
# **expenseLinesExpenseLineIdDelete**
> ExpenseLinesExpenseLineIdGet200Response expenseLinesExpenseLineIdDelete(expenseLineId)

Delete expense line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseLinesApi;

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

    ExpenseLinesApi apiInstance = new ExpenseLinesApi(defaultClient);
    String expenseLineId = "expenseLineId_example"; // String | 
    try {
      ExpenseLinesExpenseLineIdGet200Response result = apiInstance.expenseLinesExpenseLineIdDelete(expenseLineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseLinesApi#expenseLinesExpenseLineIdDelete");
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
| **expenseLineId** | **String**|  | |

### Return type

[**ExpenseLinesExpenseLineIdGet200Response**](ExpenseLinesExpenseLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseLinesExpenseLineIdGet"></a>
# **expenseLinesExpenseLineIdGet**
> ExpenseLinesExpenseLineIdGet200Response expenseLinesExpenseLineIdGet(expenseLineId)

Show expense line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseLinesApi;

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

    ExpenseLinesApi apiInstance = new ExpenseLinesApi(defaultClient);
    String expenseLineId = "expenseLineId_example"; // String | 
    try {
      ExpenseLinesExpenseLineIdGet200Response result = apiInstance.expenseLinesExpenseLineIdGet(expenseLineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseLinesApi#expenseLinesExpenseLineIdGet");
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
| **expenseLineId** | **String**|  | |

### Return type

[**ExpenseLinesExpenseLineIdGet200Response**](ExpenseLinesExpenseLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="expenseLinesExpenseLineIdPut"></a>
# **expenseLinesExpenseLineIdPut**
> ExpenseLinesExpenseLineIdGet200Response expenseLinesExpenseLineIdPut(expenseLineId)

Edit expense line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseLinesApi;

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

    ExpenseLinesApi apiInstance = new ExpenseLinesApi(defaultClient);
    String expenseLineId = "expenseLineId_example"; // String | 
    try {
      ExpenseLinesExpenseLineIdGet200Response result = apiInstance.expenseLinesExpenseLineIdPut(expenseLineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseLinesApi#expenseLinesExpenseLineIdPut");
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
| **expenseLineId** | **String**|  | |

### Return type

[**ExpenseLinesExpenseLineIdGet200Response**](ExpenseLinesExpenseLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseLinesGet"></a>
# **expenseLinesGet**
> ExpenseLinesGet200Response expenseLinesGet(createdById, currencyId, expenseId)

Show list of expense lines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseLinesApi;

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

    ExpenseLinesApi apiInstance = new ExpenseLinesApi(defaultClient);
    UUID createdById = UUID.randomUUID(); // UUID | 
    UUID currencyId = UUID.randomUUID(); // UUID | 
    UUID expenseId = UUID.randomUUID(); // UUID | 
    try {
      ExpenseLinesGet200Response result = apiInstance.expenseLinesGet(createdById, currencyId, expenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseLinesApi#expenseLinesGet");
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
| **createdById** | **UUID**|  | [optional] |
| **currencyId** | **UUID**|  | [optional] |
| **expenseId** | **UUID**|  | [optional] |

### Return type

[**ExpenseLinesGet200Response**](ExpenseLinesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseLinesPost"></a>
# **expenseLinesPost**
> ClockingRecordsPost201Response expenseLinesPost(expenseLinesPostRequest)

Add line to expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseLinesApi;

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

    ExpenseLinesApi apiInstance = new ExpenseLinesApi(defaultClient);
    ExpenseLinesPostRequest expenseLinesPostRequest = new ExpenseLinesPostRequest(); // ExpenseLinesPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.expenseLinesPost(expenseLinesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseLinesApi#expenseLinesPost");
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
| **expenseLinesPostRequest** | [**ExpenseLinesPostRequest**](ExpenseLinesPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

