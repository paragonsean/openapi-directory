# QueryApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryExecute**](QueryApi.md#queryExecute) | **POST** /timeseries/query |  |
| [**queryGetAvailability**](QueryApi.md#queryGetAvailability) | **GET** /availability |  |
| [**queryGetEventSchema**](QueryApi.md#queryGetEventSchema) | **POST** /eventSchema |  |


<a id="queryExecute"></a>
# **queryExecute**
> QueryResultPage queryExecute(apiVersion, parameters, storeType, xMsContinuation, xMsClientRequestId, xMsClientSessionId)



Executes Time Series Query in pages of results - Get Events, Get Series or Aggregate Series.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    QueryRequest parameters = new QueryRequest(); // QueryRequest | Time series query request body.
    String storeType = "storeType_example"; // String | For the environments with warm store enabled, the query can be executed either on the 'WarmStore' or 'ColdStore'. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
    String xMsContinuation = "xMsContinuation_example"; // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      QueryResultPage result = apiInstance.queryExecute(apiVersion, parameters, storeType, xMsContinuation, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryExecute");
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
| **parameters** | [**QueryRequest**](QueryRequest.md)| Time series query request body. | |
| **storeType** | **String**| For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store. | [optional] |
| **xMsContinuation** | **String**| Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results. | [optional] |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**QueryResultPage**](QueryResultPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful query. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |
| **0** | Unexpected error. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |

<a id="queryGetAvailability"></a>
# **queryGetAvailability**
> AvailabilityResponse queryGetAvailability(apiVersion, storeType, xMsClientRequestId, xMsClientSessionId)



Returns the time range and distribution of event count over the event timestamp ($ts). This API can be used to provide landing experience of navigating to the environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    String storeType = "storeType_example"; // String | For the environments with warm store enabled, the query can be executed either on the 'WarmStore' or 'ColdStore'. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      AvailabilityResponse result = apiInstance.queryGetAvailability(apiVersion, storeType, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryGetAvailability");
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
| **storeType** | **String**| For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store. | [optional] |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**AvailabilityResponse**](AvailabilityResponse.md)

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

<a id="queryGetEventSchema"></a>
# **queryGetEventSchema**
> EventSchema queryGetEventSchema(apiVersion, parameters, storeType, xMsClientRequestId, xMsClientSessionId)



Returns environment event schema for a given search span. Event schema is a set of property definitions. Event schema may not be contain all persisted properties when there are too many properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    GetEventSchemaRequest parameters = new GetEventSchemaRequest(); // GetEventSchemaRequest | Parameters to get event schema.
    String storeType = "storeType_example"; // String | For the environments with warm store enabled, the query can be executed either on the 'WarmStore' or 'ColdStore'. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      EventSchema result = apiInstance.queryGetEventSchema(apiVersion, parameters, storeType, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryGetEventSchema");
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
| **parameters** | [**GetEventSchemaRequest**](GetEventSchemaRequest.md)| Parameters to get event schema. | |
| **storeType** | **String**| For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store. | [optional] |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**EventSchema**](EventSchema.md)

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

