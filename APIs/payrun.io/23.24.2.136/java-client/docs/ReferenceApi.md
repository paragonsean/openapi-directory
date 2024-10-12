# ReferenceApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getJournalExpressionSchema**](ReferenceApi.md#getJournalExpressionSchema) | **GET** /ReferenceData/JournalExpressionDataTable | Gets the journal expression data schema |


<a id="getJournalExpressionSchema"></a>
# **getJournalExpressionSchema**
> JournalExpressionDataTable getJournalExpressionSchema(authorization, apiVersion)

Gets the journal expression data schema

Gets the data schema for all available journal expression values. Includes table names, column names and data types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReferenceApi apiInstance = new ReferenceApi(defaultClient);
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      JournalExpressionDataTable result = apiInstance.getJournalExpressionSchema(authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceApi#getJournalExpressionSchema");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**JournalExpressionDataTable**](JournalExpressionDataTable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The journal expression data table object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

