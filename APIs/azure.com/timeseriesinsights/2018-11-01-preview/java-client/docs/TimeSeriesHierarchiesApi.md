# TimeSeriesHierarchiesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeSeriesHierarchiesExecuteBatch**](TimeSeriesHierarchiesApi.md#timeSeriesHierarchiesExecuteBatch) | **POST** /timeseries/hierarchies/$batch |  |
| [**timeSeriesHierarchiesGet**](TimeSeriesHierarchiesApi.md#timeSeriesHierarchiesGet) | **GET** /timeseries/hierarchies |  |


<a id="timeSeriesHierarchiesExecuteBatch"></a>
# **timeSeriesHierarchiesExecuteBatch**
> HierarchiesBatchResponse timeSeriesHierarchiesExecuteBatch(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId)



Executes a batch get, create, update, delete operation on multiple time series hierarchy definitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesHierarchiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesHierarchiesApi apiInstance = new TimeSeriesHierarchiesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    HierarchiesBatchRequest parameters = new HierarchiesBatchRequest(); // HierarchiesBatchRequest | Time series hierarchies batch request body.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      HierarchiesBatchResponse result = apiInstance.timeSeriesHierarchiesExecuteBatch(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesHierarchiesApi#timeSeriesHierarchiesExecuteBatch");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;. | [default to 2018-11-01-preview] |
| **parameters** | [**HierarchiesBatchRequest**](HierarchiesBatchRequest.md)| Time series hierarchies batch request body. | |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**HierarchiesBatchResponse**](HierarchiesBatchResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |
| **0** | Unexpected error. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |

<a id="timeSeriesHierarchiesGet"></a>
# **timeSeriesHierarchiesGet**
> GetHierarchiesPage timeSeriesHierarchiesGet(apiVersion, xMsContinuation, xMsClientRequestId, xMsClientSessionId)



Returns time series hierarchies definitions in pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesHierarchiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesHierarchiesApi apiInstance = new TimeSeriesHierarchiesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    String xMsContinuation = "xMsContinuation_example"; // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      GetHierarchiesPage result = apiInstance.timeSeriesHierarchiesGet(apiVersion, xMsContinuation, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesHierarchiesApi#timeSeriesHierarchiesGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;. | [default to 2018-11-01-preview] |
| **xMsContinuation** | **String**| Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results. | [optional] |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**GetHierarchiesPage**](GetHierarchiesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |
| **0** | Unexpected error. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |

