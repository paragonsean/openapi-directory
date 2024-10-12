# ApplicationsApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationGet**](ApplicationsApi.md#applicationGet) | **GET** /applications/{applicationId} |  |
| [**applicationList**](ApplicationsApi.md#applicationList) | **GET** /applications |  |


<a id="applicationGet"></a>
# **applicationGet**
> ApplicationSummary applicationGet(applicationId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)



Gets information about the specified application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The id of the application.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      ApplicationSummary result = apiInstance.applicationGet(applicationId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#applicationGet");
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
| **applicationId** | **String**| The id of the application. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**ApplicationSummary**](ApplicationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="applicationList"></a>
# **applicationList**
> ApplicationListResult applicationList(apiVersion, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the applications available in the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer maxresults = 56; // Integer | Sets the maximum number of items to return in the response.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      ApplicationListResult result = apiInstance.applicationList(apiVersion, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#applicationList");
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
| **maxresults** | **Integer**| Sets the maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**ApplicationListResult**](ApplicationListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

