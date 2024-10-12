# TargetsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTargetsUsingGET**](TargetsApi.md#getTargetsUsingGET) | **GET** /targets | Get ChEMBL targets |


<a id="getTargetsUsingGET"></a>
# **getTargetsUsingGET**
> Targets getTargetsUsingGET(accession, limit, page, targetIds)

Get ChEMBL targets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    TargetsApi apiInstance = new TargetsApi(defaultClient);
    List<String> accession = Arrays.asList(); // List<String> | accession
    Integer limit = 10; // Integer | limit
    Integer page = 0; // Integer | page
    List<String> targetIds = Arrays.asList(); // List<String> | targetIds
    try {
      Targets result = apiInstance.getTargetsUsingGET(accession, limit, page, targetIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TargetsApi#getTargetsUsingGET");
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
| **accession** | [**List&lt;String&gt;**](String.md)| accession | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **targetIds** | [**List&lt;String&gt;**](String.md)| targetIds | [optional] |

### Return type

[**Targets**](Targets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

