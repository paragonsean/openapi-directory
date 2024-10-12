# ExpenseFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expenseFilesExpenseFileIdDelete**](ExpenseFilesApi.md#expenseFilesExpenseFileIdDelete) | **DELETE** /expense_files/{expense_file_id} | Delete file |
| [**expenseFilesExpenseFileIdGet**](ExpenseFilesApi.md#expenseFilesExpenseFileIdGet) | **GET** /expense_files/{expense_file_id} | Show file |
| [**expenseFilesExpenseFileIdPut**](ExpenseFilesApi.md#expenseFilesExpenseFileIdPut) | **PUT** /expense_files/{expense_file_id} | Edit file |
| [**expenseFilesGet**](ExpenseFilesApi.md#expenseFilesGet) | **GET** /expense_files | Show list of expense files |
| [**expenseFilesPost**](ExpenseFilesApi.md#expenseFilesPost) | **POST** /expense_files | Add file to expense |


<a id="expenseFilesExpenseFileIdDelete"></a>
# **expenseFilesExpenseFileIdDelete**
> ExpenseFilesExpenseFileIdGet200Response expenseFilesExpenseFileIdDelete(expenseFileId)

Delete file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseFilesApi;

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

    ExpenseFilesApi apiInstance = new ExpenseFilesApi(defaultClient);
    String expenseFileId = "expenseFileId_example"; // String | 
    try {
      ExpenseFilesExpenseFileIdGet200Response result = apiInstance.expenseFilesExpenseFileIdDelete(expenseFileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseFilesApi#expenseFilesExpenseFileIdDelete");
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
| **expenseFileId** | **String**|  | |

### Return type

[**ExpenseFilesExpenseFileIdGet200Response**](ExpenseFilesExpenseFileIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseFilesExpenseFileIdGet"></a>
# **expenseFilesExpenseFileIdGet**
> ExpenseFilesExpenseFileIdGet200Response expenseFilesExpenseFileIdGet(expenseFileId)

Show file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseFilesApi;

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

    ExpenseFilesApi apiInstance = new ExpenseFilesApi(defaultClient);
    String expenseFileId = "expenseFileId_example"; // String | 
    try {
      ExpenseFilesExpenseFileIdGet200Response result = apiInstance.expenseFilesExpenseFileIdGet(expenseFileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseFilesApi#expenseFilesExpenseFileIdGet");
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
| **expenseFileId** | **String**|  | |

### Return type

[**ExpenseFilesExpenseFileIdGet200Response**](ExpenseFilesExpenseFileIdGet200Response.md)

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

<a id="expenseFilesExpenseFileIdPut"></a>
# **expenseFilesExpenseFileIdPut**
> ExpenseFilesExpenseFileIdPut200Response expenseFilesExpenseFileIdPut(expenseFileId)

Edit file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseFilesApi;

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

    ExpenseFilesApi apiInstance = new ExpenseFilesApi(defaultClient);
    UUID expenseFileId = UUID.randomUUID(); // UUID | 
    try {
      ExpenseFilesExpenseFileIdPut200Response result = apiInstance.expenseFilesExpenseFileIdPut(expenseFileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseFilesApi#expenseFilesExpenseFileIdPut");
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
| **expenseFileId** | **UUID**|  | |

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseFilesGet"></a>
# **expenseFilesGet**
> ExpenseFilesGet200Response expenseFilesGet(createdById, expenseId)

Show list of expense files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseFilesApi;

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

    ExpenseFilesApi apiInstance = new ExpenseFilesApi(defaultClient);
    UUID createdById = UUID.randomUUID(); // UUID | 
    UUID expenseId = UUID.randomUUID(); // UUID | 
    try {
      ExpenseFilesGet200Response result = apiInstance.expenseFilesGet(createdById, expenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseFilesApi#expenseFilesGet");
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
| **expenseId** | **UUID**|  | [optional] |

### Return type

[**ExpenseFilesGet200Response**](ExpenseFilesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseFilesPost"></a>
# **expenseFilesPost**
> ClockingRecordsPost201Response expenseFilesPost(_file, description)

Add file to expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseFilesApi;

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

    ExpenseFilesApi apiInstance = new ExpenseFilesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | 
    String description = "description_example"; // String | 
    try {
      ClockingRecordsPost201Response result = apiInstance.expenseFilesPost(_file, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseFilesApi#expenseFilesPost");
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
| **_file** | **File**|  | |
| **description** | **String**|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully added file |  -  |
| **422** | Validation error |  -  |

