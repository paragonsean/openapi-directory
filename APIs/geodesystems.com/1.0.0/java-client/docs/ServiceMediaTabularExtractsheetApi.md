# ServiceMediaTabularExtractsheetApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaTabularExtractsheet**](ServiceMediaTabularExtractsheetApi.md#mediaTabularExtractsheet) | **GET** /repository/entry/show | API for Extract sheets |


<a id="mediaTabularExtractsheet"></a>
# **mediaTabularExtractsheet**
> mediaTabularExtractsheet(output, entryid, arg1)

API for Extract sheets

API to call: Extract sheets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMediaTabularExtractsheetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    ServiceMediaTabularExtractsheetApi apiInstance = new ServiceMediaTabularExtractsheetApi(defaultClient);
    String output = "media_tabular_extractsheet"; // String | Output type  -don't change
    String entryid = "entryid_example"; // String | Entry ID
    String arg1 = "arg1_example"; // String | Sheets
    try {
      apiInstance.mediaTabularExtractsheet(output, entryid, arg1);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMediaTabularExtractsheetApi#mediaTabularExtractsheet");
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
| **output** | **String**| Output type  -don&#39;t change | [default to media_tabular_extractsheet] |
| **entryid** | **String**| Entry ID | |
| **arg1** | **String**| Sheets | [optional] |

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
| **200** | No response was specified |  -  |

