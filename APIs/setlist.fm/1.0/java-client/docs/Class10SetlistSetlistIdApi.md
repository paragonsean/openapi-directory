# Class10SetlistSetlistIdApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10SetlistSetlistIdGetSetlistGET**](Class10SetlistSetlistIdApi.md#resource10SetlistSetlistIdGetSetlistGET) | **GET** /1.0/setlist/{setlistId} | . |


<a id="resource10SetlistSetlistIdGetSetlistGET"></a>
# **resource10SetlistSetlistIdGetSetlistGET**
> JsonSetlist resource10SetlistSetlistIdGetSetlistGET(setlistId)

.

&lt;p&gt; Returns the current version of a setlist. E.g. if you pass the id of a setlist that got edited since you last accessed it, you&#39;ll get the current version. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10SetlistSetlistIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10SetlistSetlistIdApi apiInstance = new Class10SetlistSetlistIdApi(defaultClient);
    String setlistId = "setlistId_example"; // String | the setlist id
    try {
      JsonSetlist result = apiInstance.resource10SetlistSetlistIdGetSetlistGET(setlistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10SetlistSetlistIdApi#resource10SetlistSetlistIdGetSetlistGET");
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
| **setlistId** | **String**| the setlist id | |

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

