# ExpensesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkDeleteExpenses**](ExpensesApi.md#bulkDeleteExpenses) | **DELETE** /expenses/bulkDelete | Bulk delete expenses |
| [**expensesExpenseIdDelete**](ExpensesApi.md#expensesExpenseIdDelete) | **DELETE** /expenses/{expense_id} | Delete expense |
| [**expensesExpenseIdGet**](ExpensesApi.md#expensesExpenseIdGet) | **GET** /expenses/{expense_id} | Show expense |
| [**expensesExpenseIdPut**](ExpensesApi.md#expensesExpenseIdPut) | **PUT** /expenses/{expense_id} | Edit expense |
| [**expensesGet**](ExpensesApi.md#expensesGet) | **GET** /expenses | Show list of expenses |
| [**expensesHighestAmountGet**](ExpensesApi.md#expensesHighestAmountGet) | **GET** /expenses/highest_amount | Show highest Expense amount(&#x60;total_selling_price&#x60;) |
| [**expensesPost**](ExpensesApi.md#expensesPost) | **POST** /expenses | Add line to expense |
| [**sendEmailsExpenses**](ExpensesApi.md#sendEmailsExpenses) | **DELETE** /expenses/sendEmails | Bulk delete expenses |


<a id="bulkDeleteExpenses"></a>
# **bulkDeleteExpenses**
> EmptySuccessResponse bulkDeleteExpenses(bulkActionRequestBody)

Bulk delete expenses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | expense ids
    try {
      EmptySuccessResponse result = apiInstance.bulkDeleteExpenses(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#bulkDeleteExpenses");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| expense ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="expensesExpenseIdDelete"></a>
# **expensesExpenseIdDelete**
> ExpensesExpenseIdGet200Response expensesExpenseIdDelete(expenseId)

Delete expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    String expenseId = "expenseId_example"; // String | 
    try {
      ExpensesExpenseIdGet200Response result = apiInstance.expensesExpenseIdDelete(expenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesExpenseIdDelete");
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
| **expenseId** | **String**|  | |

### Return type

[**ExpensesExpenseIdGet200Response**](ExpensesExpenseIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expensesExpenseIdGet"></a>
# **expensesExpenseIdGet**
> ExpensesExpenseIdGet200Response expensesExpenseIdGet(expenseId)

Show expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    String expenseId = "expenseId_example"; // String | 
    try {
      ExpensesExpenseIdGet200Response result = apiInstance.expensesExpenseIdGet(expenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesExpenseIdGet");
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
| **expenseId** | **String**|  | |

### Return type

[**ExpensesExpenseIdGet200Response**](ExpensesExpenseIdGet200Response.md)

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

<a id="expensesExpenseIdPut"></a>
# **expensesExpenseIdPut**
> ExpensesExpenseIdGet200Response expensesExpenseIdPut(expenseId)

Edit expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    String expenseId = "expenseId_example"; // String | 
    try {
      ExpensesExpenseIdGet200Response result = apiInstance.expensesExpenseIdPut(expenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesExpenseIdPut");
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
| **expenseId** | **String**|  | |

### Return type

[**ExpensesExpenseIdGet200Response**](ExpensesExpenseIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expensesGet"></a>
# **expensesGet**
> ExpensesGet200Response expensesGet(createdById, companyId, contactId, projectId, dueDate, gtCreated, ltCreated, status, isImported, minAmount, maxAmount, projects)

Show list of expenses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    UUID createdById = UUID.randomUUID(); // UUID | 
    UUID companyId = UUID.randomUUID(); // UUID | 
    UUID contactId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    String dueDate = "valid"; // String | Filter by [valid=records in future including today], [exceeded=records in past] or [null=all records]
    LocalDate gtCreated = LocalDate.now(); // LocalDate | Created after date
    LocalDate ltCreated = LocalDate.now(); // LocalDate | Created before date
    String status = "expired_subscription"; // String | Filter by status identifier. [null=all records]
    Boolean isImported = true; // Boolean | 
    Float minAmount = 3.4F; // Float | Expenses `total_selling_price` > `min_amount`
    Float maxAmount = 3.4F; // Float | Expenses `total_selling_price` < `max_amount`
    String projects = "all"; // String | You can select `all projects`, `no projects` or select `multiple projects`
    try {
      ExpensesGet200Response result = apiInstance.expensesGet(createdById, companyId, contactId, projectId, dueDate, gtCreated, ltCreated, status, isImported, minAmount, maxAmount, projects);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesGet");
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
| **companyId** | **UUID**|  | [optional] |
| **contactId** | **UUID**|  | [optional] |
| **projectId** | **UUID**|  | [optional] |
| **dueDate** | **String**| Filter by [valid&#x3D;records in future including today], [exceeded&#x3D;records in past] or [null&#x3D;all records] | [optional] [enum: valid, exceeded, ] |
| **gtCreated** | **LocalDate**| Created after date | [optional] |
| **ltCreated** | **LocalDate**| Created before date | [optional] |
| **status** | **String**| Filter by status identifier. [null&#x3D;all records] | [optional] [enum: expired_subscription, approved, ] |
| **isImported** | **Boolean**|  | [optional] [default to true] |
| **minAmount** | **Float**| Expenses &#x60;total_selling_price&#x60; &gt; &#x60;min_amount&#x60; | [optional] |
| **maxAmount** | **Float**| Expenses &#x60;total_selling_price&#x60; &lt; &#x60;max_amount&#x60; | [optional] |
| **projects** | **String**| You can select &#x60;all projects&#x60;, &#x60;no projects&#x60; or select &#x60;multiple projects&#x60; | [optional] [enum: all, none, ["project1","project2","project3"]] |

### Return type

[**ExpensesGet200Response**](ExpensesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expensesHighestAmountGet"></a>
# **expensesHighestAmountGet**
> ExpensesHighestAmountGet200Response expensesHighestAmountGet(gtCreated, ltCreated)

Show highest Expense amount(&#x60;total_selling_price&#x60;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    LocalDate gtCreated = LocalDate.now(); // LocalDate | Used to filter time range
    LocalDate ltCreated = LocalDate.now(); // LocalDate | Used to filter time range
    try {
      ExpensesHighestAmountGet200Response result = apiInstance.expensesHighestAmountGet(gtCreated, ltCreated);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesHighestAmountGet");
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
| **gtCreated** | **LocalDate**| Used to filter time range | |
| **ltCreated** | **LocalDate**| Used to filter time range | |

### Return type

[**ExpensesHighestAmountGet200Response**](ExpensesHighestAmountGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expensesPost"></a>
# **expensesPost**
> ClockingRecordsPost201Response expensesPost(expensesPostRequest)

Add line to expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    ExpensesPostRequest expensesPostRequest = new ExpensesPostRequest(); // ExpensesPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.expensesPost(expensesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesPost");
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
| **expensesPostRequest** | [**ExpensesPostRequest**](ExpensesPostRequest.md)|  | [optional] |

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

<a id="sendEmailsExpenses"></a>
# **sendEmailsExpenses**
> EmptySuccessResponse sendEmailsExpenses(bulkActionRequestBody)

Bulk delete expenses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

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

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | expense ids
    try {
      EmptySuccessResponse result = apiInstance.sendEmailsExpenses(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#sendEmailsExpenses");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| expense ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

