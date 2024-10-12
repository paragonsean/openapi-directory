# VatTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vatTypesGet**](VatTypesApi.md#vatTypesGet) | **GET** /v1/vatTypes | Returns a list of global Vat Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field. |


<a id="vatTypesGet"></a>
# **vatTypesGet**
> PageResultVatTypeDto vatTypesGet()

Returns a list of global Vat Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VatTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    VatTypesApi apiInstance = new VatTypesApi(defaultClient);
    try {
      PageResultVatTypeDto result = apiInstance.vatTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VatTypesApi#vatTypesGet");
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

[**PageResultVatTypeDto**](PageResultVatTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

