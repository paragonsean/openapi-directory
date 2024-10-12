# Class10SetlistVersionVersionIdApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10SetlistVersionVersionIdGetSetlistVersionGET**](Class10SetlistVersionVersionIdApi.md#resource10SetlistVersionVersionIdGetSetlistVersionGET) | **GET** /1.0/setlist/version/{versionId} | . |


<a id="resource10SetlistVersionVersionIdGetSetlistVersionGET"></a>
# **resource10SetlistVersionVersionIdGetSetlistVersionGET**
> JsonSetlist resource10SetlistVersionVersionIdGetSetlistVersionGET(versionId)

.

&lt;p&gt; Returns a setlist for the given versionId. The setlist returned isn&#39;t necessarily the most recent version. E.g. if you pass the versionId of a setlist that got edited since you last accessed it, you&#39;ll get the same version as last time. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10SetlistVersionVersionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10SetlistVersionVersionIdApi apiInstance = new Class10SetlistVersionVersionIdApi(defaultClient);
    String versionId = "versionId_example"; // String | the version id
    try {
      JsonSetlist result = apiInstance.resource10SetlistVersionVersionIdGetSetlistVersionGET(versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10SetlistVersionVersionIdApi#resource10SetlistVersionVersionIdGetSetlistVersionGET");
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
| **versionId** | **String**| the version id | |

### Return type

[**JsonSetlist**](JsonSetlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

