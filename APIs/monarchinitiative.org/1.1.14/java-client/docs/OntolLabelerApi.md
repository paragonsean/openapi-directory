# OntolLabelerApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOntolLabelerResource**](OntolLabelerApi.md#getOntolLabelerResource) | **GET** /ontol/labeler/ | Fetches a map from CURIEs/IDs to labels |


<a id="getOntolLabelerResource"></a>
# **getOntolLabelerResource**
> getOntolLabelerResource(id)

Fetches a map from CURIEs/IDs to labels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntolLabelerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntolLabelerApi apiInstance = new OntolLabelerApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | List of ids
    try {
      apiInstance.getOntolLabelerResource(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntolLabelerApi#getOntolLabelerResource");
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
| **id** | [**List&lt;String&gt;**](String.md)| List of ids | |

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
| **200** | Success |  -  |

