# ResourcesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesJsonGet**](ResourcesApi.md#resourcesJsonGet) | **GET** /resources.json | Get Resources by search query |


<a id="resourcesJsonGet"></a>
# **resourcesJsonGet**
> List&lt;Object&gt; resourcesJsonGet(q)

Get Resources by search query

Global search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String q = "q_example"; // String | The search query supplied by the user
    try {
      List<Object> result = apiInstance.resourcesJsonGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesJsonGet");
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
| **q** | **String**| The search query supplied by the user | |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | \&quot;Returns the list of Resources matching the search query &#39;q&#39;.&lt;p&gt;The search query &#39;q&#39; is a Lucene query.&lt;br&gt;The syntax for a Lucene query can be found &lt;a href&#x3D;\&quot;http://lucene.apache.org/core/2_9_4/queryparsersyntax.html\&quot;&gt;here&lt;/a&gt;.\&quot; |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

