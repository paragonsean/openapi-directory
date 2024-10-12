# CollectionChangesetApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCollectionChangeset**](CollectionChangesetApi.md#getCollectionChangeset) | **GET** /buckets/{bid}/collections/{cid}/changeset |  |


<a id="getCollectionChangeset"></a>
# **getCollectionChangeset**
> getCollectionChangeset(bid, cid, expected, since, limit, bucket, collection)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionChangesetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    CollectionChangesetApi apiInstance = new CollectionChangesetApi(defaultClient);
    String bid = "bid_example"; // String | 
    String cid = "cid_example"; // String | 
    String expected = "expected_example"; // String | 
    String since = "since_example"; // String | 
    Integer limit = 56; // Integer | 
    String bucket = "bucket_example"; // String | 
    String collection = "collection_example"; // String | 
    try {
      apiInstance.getCollectionChangeset(bid, cid, expected, since, limit, bucket, collection);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionChangesetApi#getCollectionChangeset");
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
| **bid** | **String**|  | |
| **cid** | **String**|  | |
| **expected** | **String**|  | |
| **since** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **bucket** | **String**|  | [optional] |
| **collection** | **String**|  | [optional] |

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
| **0** | UNDOCUMENTED RESPONSE |  -  |

