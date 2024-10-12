# TagsApi

All URIs are relative to *https://api.up.com.au/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tagsGet**](TagsApi.md#tagsGet) | **GET** /tags | List tags |
| [**transactionsTransactionIdRelationshipsTagsDelete**](TagsApi.md#transactionsTransactionIdRelationshipsTagsDelete) | **DELETE** /transactions/{transactionId}/relationships/tags | Remove tags from transaction |
| [**transactionsTransactionIdRelationshipsTagsPost**](TagsApi.md#transactionsTransactionIdRelationshipsTagsPost) | **POST** /transactions/{transactionId}/relationships/tags | Add tags to transaction |


<a id="tagsGet"></a>
# **tagsGet**
> ListTagsResponse tagsGet(pageSize)

List tags

Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered lexicographically. The &#x60;transactions&#x60; relationship for each tag exposes a link to get the transactions with the given tag. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Integer pageSize = 50; // Integer | The number of records to return in each page. 
    try {
      ListTagsResponse result = apiInstance.tagsGet(pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGet");
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
| **pageSize** | **Integer**| The number of records to return in each page.  | [optional] |

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="transactionsTransactionIdRelationshipsTagsDelete"></a>
# **transactionsTransactionIdRelationshipsTagsDelete**
> transactionsTransactionIdRelationshipsTagsDelete(transactionId, updateTransactionTagsRequest)

Remove tags from transaction

Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String transactionId = "c3feb4ba-829c-4482-b882-1b9bd23da82d"; // String | The unique identifier for the transaction. 
    UpdateTransactionTagsRequest updateTransactionTagsRequest = new UpdateTransactionTagsRequest(); // UpdateTransactionTagsRequest | 
    try {
      apiInstance.transactionsTransactionIdRelationshipsTagsDelete(transactionId, updateTransactionTagsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#transactionsTransactionIdRelationshipsTagsDelete");
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
| **transactionId** | **String**| The unique identifier for the transaction.  | |
| **updateTransactionTagsRequest** | [**UpdateTransactionTagsRequest**](UpdateTransactionTagsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |

<a id="transactionsTransactionIdRelationshipsTagsPost"></a>
# **transactionsTransactionIdRelationshipsTagsPost**
> transactionsTransactionIdRelationshipsTagsPost(transactionId, updateTransactionTagsRequest)

Add tags to transaction

Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String transactionId = "acde4631-db56-49a6-aea3-4e2311ef1d6a"; // String | The unique identifier for the transaction. 
    UpdateTransactionTagsRequest updateTransactionTagsRequest = new UpdateTransactionTagsRequest(); // UpdateTransactionTagsRequest | 
    try {
      apiInstance.transactionsTransactionIdRelationshipsTagsPost(transactionId, updateTransactionTagsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#transactionsTransactionIdRelationshipsTagsPost");
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
| **transactionId** | **String**| The unique identifier for the transaction.  | |
| **updateTransactionTagsRequest** | [**UpdateTransactionTagsRequest**](UpdateTransactionTagsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |

