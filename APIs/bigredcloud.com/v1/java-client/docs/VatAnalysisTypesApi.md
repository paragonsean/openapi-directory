# VatAnalysisTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vatAnalysisTypesGet**](VatAnalysisTypesApi.md#vatAnalysisTypesGet) | **GET** /v1/vatAnalysisTypes | Returns a list of global Vat Analysis Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field. |


<a id="vatAnalysisTypesGet"></a>
# **vatAnalysisTypesGet**
> PageResultVatAnalysisTypeDto vatAnalysisTypesGet()

Returns a list of global Vat Analysis Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VatAnalysisTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    VatAnalysisTypesApi apiInstance = new VatAnalysisTypesApi(defaultClient);
    try {
      PageResultVatAnalysisTypeDto result = apiInstance.vatAnalysisTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VatAnalysisTypesApi#vatAnalysisTypesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PageResultVatAnalysisTypeDto**](PageResultVatAnalysisTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

