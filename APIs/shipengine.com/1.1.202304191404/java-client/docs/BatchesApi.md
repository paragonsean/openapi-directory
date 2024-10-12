# BatchesApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addToBatch**](BatchesApi.md#addToBatch) | **POST** /v1/batches/{batch_id}/add | Add to a Batch |
| [**createBatch**](BatchesApi.md#createBatch) | **POST** /v1/batches | Create A Batch |
| [**deleteBatch**](BatchesApi.md#deleteBatch) | **DELETE** /v1/batches/{batch_id} | Delete Batch By Id |
| [**getBatchByExternalId**](BatchesApi.md#getBatchByExternalId) | **GET** /v1/batches/external_batch_id/{external_batch_id} | Get Batch By External ID |
| [**getBatchById**](BatchesApi.md#getBatchById) | **GET** /v1/batches/{batch_id} | Get Batch By ID |
| [**listBatchErrors**](BatchesApi.md#listBatchErrors) | **GET** /v1/batches/{batch_id}/errors | Get Batch Errors |
| [**listBatches**](BatchesApi.md#listBatches) | **GET** /v1/batches | List Batches |
| [**processBatch**](BatchesApi.md#processBatch) | **POST** /v1/batches/{batch_id}/process/labels | Process Batch ID Labels |
| [**removeFromBatch**](BatchesApi.md#removeFromBatch) | **POST** /v1/batches/{batch_id}/remove | Remove From Batch |
| [**updateBatch**](BatchesApi.md#updateBatch) | **PUT** /v1/batches/{batch_id} | Update Batch By Id |


<a id="addToBatch"></a>
# **addToBatch**
> String addToBatch(batchId, addToBatchRequestBody)

Add to a Batch

Add a Shipment or Rate to a Batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String batchId = "batchId_example"; // String | Batch ID
    AddToBatchRequestBody addToBatchRequestBody = new AddToBatchRequestBody(); // AddToBatchRequestBody | 
    try {
      String result = apiInstance.addToBatch(batchId, addToBatchRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#addToBatch");
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
| **batchId** | **String**| Batch ID | |
| **addToBatchRequestBody** | [**AddToBatchRequestBody**](AddToBatchRequestBody.md)|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="createBatch"></a>
# **createBatch**
> CreateBatchResponseBody createBatch(createBatchRequestBody)

Create A Batch

Create a Batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    CreateBatchRequestBody createBatchRequestBody = new CreateBatchRequestBody(); // CreateBatchRequestBody | 
    try {
      CreateBatchResponseBody result = apiInstance.createBatch(createBatchRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#createBatch");
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
| **createBatchRequestBody** | [**CreateBatchRequestBody**](CreateBatchRequestBody.md)|  | |

### Return type

[**CreateBatchResponseBody**](CreateBatchResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested object creation was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="deleteBatch"></a>
# **deleteBatch**
> String deleteBatch(batchId)

Delete Batch By Id

Delete Batch By Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String batchId = "batchId_example"; // String | Batch ID
    try {
      String result = apiInstance.deleteBatch(batchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#deleteBatch");
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
| **batchId** | **String**| Batch ID | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getBatchByExternalId"></a>
# **getBatchByExternalId**
> GetBatchByExternalIdResponseBody getBatchByExternalId(externalBatchId)

Get Batch By External ID

Get Batch By External ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String externalBatchId = "13553d7f-3c87-4771-bae1-c49bacef11cb"; // String | 
    try {
      GetBatchByExternalIdResponseBody result = apiInstance.getBatchByExternalId(externalBatchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#getBatchByExternalId");
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
| **externalBatchId** | **String**|  | |

### Return type

[**GetBatchByExternalIdResponseBody**](GetBatchByExternalIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getBatchById"></a>
# **getBatchById**
> GetBatchByIdResponseBody getBatchById(batchId)

Get Batch By ID

Get Batch By ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String batchId = "batchId_example"; // String | Batch ID
    try {
      GetBatchByIdResponseBody result = apiInstance.getBatchById(batchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#getBatchById");
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
| **batchId** | **String**| Batch ID | |

### Return type

[**GetBatchByIdResponseBody**](GetBatchByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listBatchErrors"></a>
# **listBatchErrors**
> ListBatchErrorsResponseBody listBatchErrors(batchId, page, pagesize)

Get Batch Errors

Error handling in batches are handled differently than in a single synchronous request. You must retrieve the status of your batch by [getting a batch](https://www.shipengine.com/docs/reference/get-batch-by-id/) and getting an overview of the statuses or you can list errors directly here below to get detailed information about the errors. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String batchId = "batchId_example"; // String | Batch ID
    Integer page = 1; // Integer | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
    Integer pagesize = 56; // Integer | 
    try {
      ListBatchErrorsResponseBody result = apiInstance.listBatchErrors(batchId, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#listBatchErrors");
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
| **batchId** | **String**| Batch ID | |
| **page** | **Integer**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1] |
| **pagesize** | **Integer**|  | [optional] |

### Return type

[**ListBatchErrorsResponseBody**](ListBatchErrorsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listBatches"></a>
# **listBatches**
> ListBatchesResponseBody listBatches(status, page, pageSize, sortDir, batchNumber, sortBy)

List Batches

List Batches associated with your Shipengine account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    BatchStatus status = BatchStatus.fromValue("open"); // BatchStatus | 
    Integer page = 1; // Integer | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
    Integer pageSize = 25; // Integer | The number of results to return per response.
    SortDir sortDir = SortDir.fromValue("asc"); // SortDir | Controls the sort order of the query.
    String batchNumber = "batchNumber_example"; // String | Batch Number
    BatchesSortBy sortBy = BatchesSortBy.fromValue("ship_date"); // BatchesSortBy | 
    try {
      ListBatchesResponseBody result = apiInstance.listBatches(status, page, pageSize, sortDir, batchNumber, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#listBatches");
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
| **status** | [**BatchStatus**](.md)|  | [optional] [enum: open, queued, processing, completed, completed_with_errors, archived, notifying, invalid] |
| **page** | **Integer**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per response. | [optional] [default to 25] |
| **sortDir** | [**SortDir**](.md)| Controls the sort order of the query. | [optional] [default to desc] [enum: asc, desc] |
| **batchNumber** | **String**| Batch Number | [optional] |
| **sortBy** | [**BatchesSortBy**](.md)|  | [optional] [enum: ship_date, processed_at, created_at] |

### Return type

[**ListBatchesResponseBody**](ListBatchesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="processBatch"></a>
# **processBatch**
> String processBatch(batchId, processBatchRequestBody)

Process Batch ID Labels

Process Batch ID Labels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String batchId = "batchId_example"; // String | Batch ID
    ProcessBatchRequestBody processBatchRequestBody = new ProcessBatchRequestBody(); // ProcessBatchRequestBody | 
    try {
      String result = apiInstance.processBatch(batchId, processBatchRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#processBatch");
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
| **batchId** | **String**| Batch ID | |
| **processBatchRequestBody** | [**ProcessBatchRequestBody**](ProcessBatchRequestBody.md)|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="removeFromBatch"></a>
# **removeFromBatch**
> String removeFromBatch(batchId, removeFromBatchRequestBody)

Remove From Batch

Remove a shipment or rate from a batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String batchId = "batchId_example"; // String | Batch ID
    RemoveFromBatchRequestBody removeFromBatchRequestBody = new RemoveFromBatchRequestBody(); // RemoveFromBatchRequestBody | 
    try {
      String result = apiInstance.removeFromBatch(batchId, removeFromBatchRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#removeFromBatch");
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
| **batchId** | **String**| Batch ID | |
| **removeFromBatchRequestBody** | [**RemoveFromBatchRequestBody**](RemoveFromBatchRequestBody.md)|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="updateBatch"></a>
# **updateBatch**
> String updateBatch(batchId)

Update Batch By Id

Update Batch By Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BatchesApi apiInstance = new BatchesApi(defaultClient);
    String batchId = "batchId_example"; // String | Batch ID
    try {
      String result = apiInstance.updateBatch(batchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchesApi#updateBatch");
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
| **batchId** | **String**| Batch ID | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

