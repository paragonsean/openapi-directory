# NameAuthorityApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nameAuthoritiesGet**](NameAuthorityApi.md#nameAuthoritiesGet) | **GET** /nameAuthorities | Get all name authorities |


<a id="nameAuthoritiesGet"></a>
# **nameAuthoritiesGet**
> nameAuthoritiesGet(outputFormat)

Get all name authorities

Gets a list of all name authorities responsible for naming decisions of the geographical names in the BC Geographical Names Information System (BCGNIS)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NameAuthorityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    NameAuthorityApi apiInstance = new NameAuthorityApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    try {
      apiInstance.nameAuthoritiesGet(outputFormat);
    } catch (ApiException e) {
      System.err.println("Exception when calling NameAuthorityApi#nameAuthoritiesGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml] |

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
| **200** | A list of name authorities |  -  |

