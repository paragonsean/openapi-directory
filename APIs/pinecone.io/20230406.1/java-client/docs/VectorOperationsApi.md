# VectorOperationsApi

All URIs are relative to *https://controller.us-east1-gcp.pinecone.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delete**](VectorOperationsApi.md#delete) | **POST** /vectors/delete | Delete |
| [**describeIndexStats**](VectorOperationsApi.md#describeIndexStats) | **POST** /describe_index_stats | Describe Index Stats |
| [**fetch**](VectorOperationsApi.md#fetch) | **POST** /vectors/fetch | Fetch |
| [**query**](VectorOperationsApi.md#query) | **POST** /query | Query |
| [**update**](VectorOperationsApi.md#update) | **POST** /vectors/update | Fetch |
| [**upsert**](VectorOperationsApi.md#upsert) | **POST** /vectors/upsert | Upsert |


<a id="delete"></a>
# **delete**
> Object delete(deleteRequest)

Delete

The &#x60;Delete&#x60; operation deletes vectors, by id, from a single namespace. You can delete items by their id, from a single namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VectorOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    VectorOperationsApi apiInstance = new VectorOperationsApi(defaultClient);
    DeleteRequest deleteRequest = new DeleteRequest(); // DeleteRequest | 
    try {
      Object result = apiInstance.delete(deleteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VectorOperationsApi#delete");
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
| **deleteRequest** | [**DeleteRequest**](DeleteRequest.md)|  | |

### Return type

**Object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |

<a id="describeIndexStats"></a>
# **describeIndexStats**
> DescribeIndexStatsResponse describeIndexStats(describeIndexStatsRequest)

Describe Index Stats

The &#x60;DescribeIndexStats&#x60; operation returns statistics about the index&#39;s contents, including the vector count per namespace and the number of dimensions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VectorOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    VectorOperationsApi apiInstance = new VectorOperationsApi(defaultClient);
    DescribeIndexStatsRequest describeIndexStatsRequest = new DescribeIndexStatsRequest(); // DescribeIndexStatsRequest | 
    try {
      DescribeIndexStatsResponse result = apiInstance.describeIndexStats(describeIndexStatsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VectorOperationsApi#describeIndexStats");
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
| **describeIndexStatsRequest** | [**DescribeIndexStatsRequest**](DescribeIndexStatsRequest.md)|  | |

### Return type

[**DescribeIndexStatsResponse**](DescribeIndexStatsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |

<a id="fetch"></a>
# **fetch**
> FetchResponse fetch(fetchRequest)

Fetch

The &#x60;Fetch&#x60; operation looks up and returns vectors, by ID, from a single namespace. The returned vectors include the vector data and/or metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VectorOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    VectorOperationsApi apiInstance = new VectorOperationsApi(defaultClient);
    FetchRequest fetchRequest = new FetchRequest(); // FetchRequest | 
    try {
      FetchResponse result = apiInstance.fetch(fetchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VectorOperationsApi#fetch");
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
| **fetchRequest** | [**FetchRequest**](FetchRequest.md)|  | |

### Return type

[**FetchResponse**](FetchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |

<a id="query"></a>
# **query**
> QueryResponse query(queryRequest)

Query

The &#x60;Query&#x60; operation searches a namespace, using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VectorOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    VectorOperationsApi apiInstance = new VectorOperationsApi(defaultClient);
    QueryRequest queryRequest = new QueryRequest(); // QueryRequest | 
    try {
      QueryResponse result = apiInstance.query(queryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VectorOperationsApi#query");
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
| **queryRequest** | [**QueryRequest**](QueryRequest.md)|  | |

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |

<a id="update"></a>
# **update**
> Object update(updateRequest)

Fetch

The &#x60;Update&#x60; operation updates vector in a namespace. If a value is included, it will overwrite the previous value. If a set_metadata is included, the values of the fields specified in it will be added or overwrite the previous value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VectorOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    VectorOperationsApi apiInstance = new VectorOperationsApi(defaultClient);
    UpdateRequest updateRequest = new UpdateRequest(); // UpdateRequest | 
    try {
      Object result = apiInstance.update(updateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VectorOperationsApi#update");
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
| **updateRequest** | [**UpdateRequest**](UpdateRequest.md)|  | |

### Return type

**Object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |

<a id="upsert"></a>
# **upsert**
> UpsertResponse upsert(upsertRequest)

Upsert

The Upsert operation writes vectors into a namespace. If a new value is upserted for an existing vector id, it will overwrite the previous value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VectorOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    VectorOperationsApi apiInstance = new VectorOperationsApi(defaultClient);
    UpsertRequest upsertRequest = new UpsertRequest(); // UpsertRequest | 
    try {
      UpsertResponse result = apiInstance.upsert(upsertRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VectorOperationsApi#upsert");
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
| **upsertRequest** | [**UpsertRequest**](UpsertRequest.md)|  | |

### Return type

[**UpsertResponse**](UpsertResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |

