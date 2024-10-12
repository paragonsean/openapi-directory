# ExpensesApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createExpenseDataset**](ExpensesApi.md#createExpenseDataset) | **POST** /companies/{companyId}/sync/expenses/data/expense-transactions | Create expense-transactions |
| [**uploadAttachment**](ExpensesApi.md#uploadAttachment) | **POST** /companies/{companyId}/sync/expenses/syncs/{syncId}/transactions/{transactionId}/attachments | Upload attachment |


<a id="createExpenseDataset"></a>
# **createExpenseDataset**
> CreateExpenseResponse createExpenseDataset(companyId, createExpenseRequest)

Create expense-transactions

Create an expense transaction

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
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    CreateExpenseRequest createExpenseRequest = new CreateExpenseRequest(); // CreateExpenseRequest | 
    try {
      CreateExpenseResponse result = apiInstance.createExpenseDataset(companyId, createExpenseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#createExpenseDataset");
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
| **companyId** | **UUID**|  | |
| **createExpenseRequest** | [**CreateExpenseRequest**](CreateExpenseRequest.md)|  | [optional] |

### Return type

[**CreateExpenseResponse**](CreateExpenseResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="uploadAttachment"></a>
# **uploadAttachment**
> Attachment uploadAttachment(companyId, transactionId, syncId)

Upload attachment

Creates an attachment in the accounting software against the given transactionId

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
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    UUID transactionId = UUID.fromString("336694d8-2dca-4cb5-a28d-3ccb83e55eee"); // UUID | The unique identifier for your SMB's transaction.
    UUID syncId = UUID.fromString("6fb40d5e-b13e-11ed-afa1-0242ac120002"); // UUID | Unique identifier for a sync.
    try {
      Attachment result = apiInstance.uploadAttachment(companyId, transactionId, syncId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#uploadAttachment");
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
| **companyId** | **UUID**|  | |
| **transactionId** | **UUID**| The unique identifier for your SMB&#39;s transaction. | |
| **syncId** | **UUID**| Unique identifier for a sync. | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

