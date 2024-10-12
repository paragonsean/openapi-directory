# RouteOptimizationApiApi

All URIs are relative to *https://graphhopper.com/api/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**asyncVRP**](RouteOptimizationApiApi.md#asyncVRP) | **POST** /vrp/optimize | POST route optimization problem (batch mode) |
| [**getSolution**](RouteOptimizationApiApi.md#getSolution) | **GET** /vrp/solution/{jobId} | GET the solution (batch mode) |
| [**solveVRP**](RouteOptimizationApiApi.md#solveVRP) | **POST** /vrp | POST route optimization problem |


<a id="asyncVRP"></a>
# **asyncVRP**
> JobId asyncVRP(request)

POST route optimization problem (batch mode)

 To solve a vehicle routing problem, perform the following steps:  1.) Make a HTTP POST to this URL  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/optimize?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  It returns a job id (job_id).  2.) Take the job id and fetch the solution for the vehicle routing problem from this URL:  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  We recommend to query the solution every 500ms until it returns &#39;status&#x3D;finished&#39;.  **Note**: Since the workflow is a bit more cumbersome and since you lose some time in fetching the solution, you should always prefer the [synchronous endpoint](#operation/solveVRP). You should use the batch mode only for long running problems. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteOptimizationApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteOptimizationApiApi apiInstance = new RouteOptimizationApiApi(defaultClient);
    Request request = new Request(); // Request | The request that contains the problem to be solved.
    try {
      JobId result = apiInstance.asyncVRP(request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteOptimizationApiApi#asyncVRP");
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
| **request** | [**Request**](Request.md)| The request that contains the problem to be solved. | |

### Return type

[**JobId**](JobId.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A jobId you can use to retrieve your solution from the server - see solution endpoint. |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **400** | Error occurred when reading client request. Request is invalid. |  -  |
| **500** | Error occurred on server side. |  -  |

<a id="getSolution"></a>
# **getSolution**
> Response getSolution(jobId)

GET the solution (batch mode)

 Take the job id and fetch the solution for the vehicle routing problem from this URL:  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  You get the job id by sending a vehicle routing problem to the [batch mode URL](#operation/asyncVRP). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteOptimizationApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteOptimizationApiApi apiInstance = new RouteOptimizationApiApi(defaultClient);
    String jobId = "jobId_example"; // String | Request solution with jobId
    try {
      Response result = apiInstance.getSolution(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteOptimizationApiApi#getSolution");
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
| **jobId** | **String**| Request solution with jobId | |

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the solution |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **400** | Error occurred on client side such as invalid input. |  -  |
| **404** | Requested solution could not be found. |  -  |
| **500** | Error occurred on server side. |  -  |

<a id="solveVRP"></a>
# **solveVRP**
> Response solveVRP(request)

POST route optimization problem

 To get started with the Route Optimization API, please read the [introduction](#tag/Route-Optimization-API).  To solve a new vehicle routing problem, make a HTTP POST to this URL  &#x60;&#x60;&#x60; https://graphhopper.com/api/1/vrp?key&#x3D;&lt;your_key&gt; &#x60;&#x60;&#x60;  It returns the solution to this problem in the JSON response.  Please note that this URL is very well suited to solve minor problems. Larger vehicle routing problems, which take longer than 10 seconds to solve, cannot be solved. To solve them, please use the [batch mode URL](#operation/asyncVRP) instead. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteOptimizationApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteOptimizationApiApi apiInstance = new RouteOptimizationApiApi(defaultClient);
    Request request = new Request(); // Request | The request that contains the vehicle routing problem to be solved.
    try {
      Response result = apiInstance.solveVRP(request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteOptimizationApiApi#solveVRP");
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
| **request** | [**Request**](Request.md)| The request that contains the vehicle routing problem to be solved. | |

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the solution |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **400** | Error occurred when reading the request. Request is invalid. |  -  |
| **500** | Error occurred on server side. |  -  |

