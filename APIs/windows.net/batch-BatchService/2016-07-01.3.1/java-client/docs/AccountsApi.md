# AccountsApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountListNodeAgentSkus**](AccountsApi.md#accountListNodeAgentSkus) | **GET** /nodeagentskus | Lists all node agent SKUs supported by the Azure Batch service. |


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
    Integer maxresults = 1000; // Integer | The maximum number of items to return in the response. A maximum of 1000 results will be returned.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
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
| **maxresults** | **Integer**| The maximum number of items to return in the response. A maximum of 1000 results will be returned. | [optional] [default to 1000] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
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
| **200** | A response containing the list of node agent SKUs. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - This header uniquely identifies the request that was made and can be used for troubleshooting the request. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this header, the approximate time that the request was made, the Batch account against which the request was made, and the region that account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

