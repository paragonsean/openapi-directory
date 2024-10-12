# TimeSeriesTypesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeSeriesTypesExecuteBatch**](TimeSeriesTypesApi.md#timeSeriesTypesExecuteBatch) | **POST** /timeseries/types/$batch |  |
| [**timeSeriesTypesGet**](TimeSeriesTypesApi.md#timeSeriesTypesGet) | **GET** /timeseries/types |  |


<a id="timeSeriesTypesExecuteBatch"></a>
# **timeSeriesTypesExecuteBatch**
> TypesBatchResponse timeSeriesTypesExecuteBatch(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId)



Executes a batch get, create, update, delete operation on multiple time series types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesTypesApi apiInstance = new TimeSeriesTypesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    TypesBatchRequest parameters = new TypesBatchRequest(); // TypesBatchRequest | Time series types batch request body.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      TypesBatchResponse result = apiInstance.timeSeriesTypesExecuteBatch(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesTypesApi#timeSeriesTypesExecuteBatch");
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
| **parameters** | [**TypesBatchRequest**](TypesBatchRequest.md)| Time series types batch request body. | |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**TypesBatchResponse**](TypesBatchResponse.md)

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

<a id="timeSeriesTypesGet"></a>
# **timeSeriesTypesGet**
> GetTypesPage timeSeriesTypesGet(apiVersion, xMsContinuation, xMsClientRequestId, xMsClientSessionId)



Gets time series types in pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesTypesApi apiInstance = new TimeSeriesTypesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    String xMsContinuation = "xMsContinuation_example"; // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      GetTypesPage result = apiInstance.timeSeriesTypesGet(apiVersion, xMsContinuation, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesTypesApi#timeSeriesTypesGet");
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

[**GetTypesPage**](GetTypesPage.md)

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

