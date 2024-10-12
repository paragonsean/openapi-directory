# TransactionStatusApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSyncTransaction**](TransactionStatusApi.md#getSyncTransaction) | **GET** /companies/{companyId}/sync/expenses/syncs/{syncId}/transactions/{transactionId} | Get Sync Transaction |
| [**listSyncTransactions**](TransactionStatusApi.md#listSyncTransactions) | **GET** /companies/{companyId}/sync/expenses/syncs/{syncId}/transactions | Get Sync transactions |


<a id="getSyncTransaction"></a>
# **getSyncTransaction**
> List&lt;TransactionMetadata&gt; getSyncTransaction(companyId, syncId, transactionId)

Get Sync Transaction

Gets the status of a transaction for a sync

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    TransactionStatusApi apiInstance = new TransactionStatusApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    UUID syncId = UUID.fromString("6fb40d5e-b13e-11ed-afa1-0242ac120002"); // UUID | Unique identifier for a sync.
    UUID transactionId = UUID.fromString("336694d8-2dca-4cb5-a28d-3ccb83e55eee"); // UUID | The unique identifier for your SMB's transaction.
    try {
      List<TransactionMetadata> result = apiInstance.getSyncTransaction(companyId, syncId, transactionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionStatusApi#getSyncTransaction");
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
| **syncId** | **UUID**| Unique identifier for a sync. | |
| **transactionId** | **UUID**| The unique identifier for your SMB&#39;s transaction. | |

### Return type

[**List&lt;TransactionMetadata&gt;**](TransactionMetadata.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listSyncTransactions"></a>
# **listSyncTransactions**
> TransactionMetadataList listSyncTransactions(companyId, syncId, page, pageSize)

Get Sync transactions

Get&#39;s the transactions and status for a sync

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    TransactionStatusApi apiInstance = new TransactionStatusApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    UUID syncId = UUID.fromString("6fb40d5e-b13e-11ed-afa1-0242ac120002"); // UUID | Unique identifier for a sync.
    Integer page = 1; // Integer | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    Integer pageSize = 100; // Integer | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    try {
      TransactionMetadataList result = apiInstance.listSyncTransactions(companyId, syncId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionStatusApi#listSyncTransactions");
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
| **syncId** | **UUID**| Unique identifier for a sync. | |
| **page** | **Integer**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1] |
| **pageSize** | **Integer**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100] |

### Return type

[**TransactionMetadataList**](TransactionMetadataList.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

