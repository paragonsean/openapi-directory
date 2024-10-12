# TimeSeriesInstancesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeSeriesInstancesExecuteBatch**](TimeSeriesInstancesApi.md#timeSeriesInstancesExecuteBatch) | **POST** /timeseries/instances/$batch |  |
| [**timeSeriesInstancesGet**](TimeSeriesInstancesApi.md#timeSeriesInstancesGet) | **GET** /timeseries/instances |  |
| [**timeSeriesInstancesSearch**](TimeSeriesInstancesApi.md#timeSeriesInstancesSearch) | **POST** /timeseries/instances/search |  |
| [**timeSeriesInstancesSuggest**](TimeSeriesInstancesApi.md#timeSeriesInstancesSuggest) | **POST** /timeseries/instances/suggest |  |


<a id="timeSeriesInstancesExecuteBatch"></a>
# **timeSeriesInstancesExecuteBatch**
> InstancesBatchResponse timeSeriesInstancesExecuteBatch(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId)



Executes a batch get, create, update, delete operation on multiple time series instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesInstancesApi apiInstance = new TimeSeriesInstancesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    InstancesBatchRequest parameters = new InstancesBatchRequest(); // InstancesBatchRequest | Time series instances suggest request body.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      InstancesBatchResponse result = apiInstance.timeSeriesInstancesExecuteBatch(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesInstancesApi#timeSeriesInstancesExecuteBatch");
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
| **parameters** | [**InstancesBatchRequest**](InstancesBatchRequest.md)| Time series instances suggest request body. | |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**InstancesBatchResponse**](InstancesBatchResponse.md)

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

<a id="timeSeriesInstancesGet"></a>
# **timeSeriesInstancesGet**
> GetInstancesPage timeSeriesInstancesGet(apiVersion, xMsContinuation, xMsClientRequestId, xMsClientSessionId)



Gets time series instances in pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesInstancesApi apiInstance = new TimeSeriesInstancesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    String xMsContinuation = "xMsContinuation_example"; // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      GetInstancesPage result = apiInstance.timeSeriesInstancesGet(apiVersion, xMsContinuation, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesInstancesApi#timeSeriesInstancesGet");
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

[**GetInstancesPage**](GetInstancesPage.md)

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

<a id="timeSeriesInstancesSearch"></a>
# **timeSeriesInstancesSearch**
> SearchInstancesResponsePage timeSeriesInstancesSearch(apiVersion, parameters, xMsContinuation, xMsClientRequestId, xMsClientSessionId)



Partial list of hits on search for time series instances based on instance attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesInstancesApi apiInstance = new TimeSeriesInstancesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    SearchInstancesRequest parameters = new SearchInstancesRequest(); // SearchInstancesRequest | Time series instances search request body.
    String xMsContinuation = "xMsContinuation_example"; // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      SearchInstancesResponsePage result = apiInstance.timeSeriesInstancesSearch(apiVersion, parameters, xMsContinuation, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesInstancesApi#timeSeriesInstancesSearch");
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
| **parameters** | [**SearchInstancesRequest**](SearchInstancesRequest.md)| Time series instances search request body. | |
| **xMsContinuation** | **String**| Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results. | [optional] |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**SearchInstancesResponsePage**](SearchInstancesResponsePage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful search response. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |
| **0** | Unexpected error. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |

<a id="timeSeriesInstancesSuggest"></a>
# **timeSeriesInstancesSuggest**
> InstancesSuggestResponse timeSeriesInstancesSuggest(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId)



Suggests keywords based on time series instance attributes to be later used in Search Instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeSeriesInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TimeSeriesInstancesApi apiInstance = new TimeSeriesInstancesApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    InstancesSuggestRequest parameters = new InstancesSuggestRequest(); // InstancesSuggestRequest | Time series instances suggest request body.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      InstancesSuggestResponse result = apiInstance.timeSeriesInstancesSuggest(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeSeriesInstancesApi#timeSeriesInstancesSuggest");
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
| **parameters** | [**InstancesSuggestRequest**](InstancesSuggestRequest.md)| Time series instances suggest request body. | |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**InstancesSuggestResponse**](InstancesSuggestResponse.md)

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

