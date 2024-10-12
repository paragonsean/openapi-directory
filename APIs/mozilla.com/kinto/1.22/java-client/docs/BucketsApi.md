# BucketsApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBucket**](BucketsApi.md#getBucket) | **GET** /buckets/{id} |  |
| [**getBuckets**](BucketsApi.md#getBuckets) | **GET** /buckets |  |


<a id="getBucket"></a>
# **getBucket**
> ObjectSchema3 getBucket(id, fields, ifMatch, ifNoneMatch)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String id = "id_example"; // String | 
    List<String> fields = Arrays.asList(); // List<String> | 
    String ifMatch = "ifMatch_example"; // String | 
    String ifNoneMatch = "ifNoneMatch_example"; // String | 
    try {
      ObjectSchema3 result = apiInstance.getBucket(id, fields, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getBucket");
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
| **id** | **String**|  | |
| **fields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **ifMatch** | **String**|  | [optional] |
| **ifNoneMatch** | **String**|  | [optional] |

### Return type

[**ObjectSchema3**](ObjectSchema3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the target object. |  * Etag -  <br>  * Last-Modified -  <br>  |
| **304** | Reponse has not changed since value in If-None-Match header |  * Etag -  <br>  * Last-Modified -  <br>  |
| **400** | The request is invalid. |  -  |
| **401** | The request is missing authentication headers. |  -  |
| **403** | The user is not allowed to perform the operation, or the resource is not accessible. |  -  |
| **404** | The object does not exist or was deleted. |  -  |
| **406** | The client doesn&#39;t accept supported responses Content-Type. |  -  |
| **412** | Object was changed or deleted since value in &#x60;If-Match&#x60; header. |  -  |
| **0** | Unexpected error. |  -  |

<a id="getBuckets"></a>
# **getBuckets**
> Schema getBuckets(limit, sort, token, since, to, before, id, lastModified, fields, ifMatch, ifNoneMatch)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    Integer limit = 56; // Integer | 
    List<String> sort = Arrays.asList(); // List<String> | 
    String token = "token_example"; // String | 
    Integer since = 56; // Integer | 
    Integer to = 56; // Integer | 
    Integer before = 56; // Integer | 
    String id = "id_example"; // String | 
    Integer lastModified = 56; // Integer | 
    List<String> fields = Arrays.asList(); // List<String> | 
    String ifMatch = "ifMatch_example"; // String | 
    String ifNoneMatch = "ifNoneMatch_example"; // String | 
    try {
      Schema result = apiInstance.getBuckets(limit, sort, token, since, to, before, id, lastModified, fields, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getBuckets");
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
| **limit** | **Integer**|  | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **token** | **String**|  | [optional] |
| **since** | **Integer**|  | [optional] |
| **to** | **Integer**|  | [optional] |
| **before** | **Integer**|  | [optional] |
| **id** | **String**|  | [optional] |
| **lastModified** | **Integer**|  | [optional] |
| **fields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **ifMatch** | **String**|  | [optional] |
| **ifNoneMatch** | **String**|  | [optional] |

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a list of matching objects. |  * Etag -  <br>  * Last-Modified -  <br>  |
| **304** | Reponse has not changed since value in If-None-Match header |  * Etag -  <br>  * Last-Modified -  <br>  |
| **400** | The request is invalid. |  -  |
| **401** | The request is missing authentication headers. |  -  |
| **403** | The user is not allowed to perform the operation, or the resource is not accessible. |  -  |
| **406** | The client doesn&#39;t accept supported responses Content-Type. |  -  |
| **412** | Object was changed or deleted since value in &#x60;If-Match&#x60; header. |  -  |
| **0** | Unexpected error. |  -  |

