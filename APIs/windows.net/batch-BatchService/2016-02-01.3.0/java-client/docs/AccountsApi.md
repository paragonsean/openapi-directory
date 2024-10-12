# AccountsApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountListNodeAgentSkus**](AccountsApi.md#accountListNodeAgentSkus) | **GET** /nodeagentskus |  |


<a id="accountListNodeAgentSkus"></a>
# **accountListNodeAgentSkus**
> AccountListNodeAgentSkusResult accountListNodeAgentSkus(apiVersion, $filter, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all node agent SKUs supported by the Azure Batch service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause.
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      AccountListNodeAgentSkusResult result = apiInstance.accountListNodeAgentSkus(apiVersion, $filter, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountListNodeAgentSkus");
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
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**AccountListNodeAgentSkusResult**](AccountListNodeAgentSkusResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

