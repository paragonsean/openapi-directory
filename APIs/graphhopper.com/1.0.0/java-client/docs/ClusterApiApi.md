# ClusterApiApi

All URIs are relative to *https://graphhopper.com/api/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**asyncClusteringProblem**](ClusterApiApi.md#asyncClusteringProblem) | **POST** /cluster/calculate | Batch Cluster Endpoint |
| [**getClusterSolution**](ClusterApiApi.md#getClusterSolution) | **GET** /cluster/solution/{jobId} | GET Batch Solution Endpoint |
| [**solveClusteringProblem**](ClusterApiApi.md#solveClusteringProblem) | **POST** /cluster | POST Cluster Endpoint |


<a id="asyncClusteringProblem"></a>
# **asyncClusteringProblem**
> JobId asyncClusteringProblem(clusterRequest)

Batch Cluster Endpoint

 Prefer the [synchronous endpoint](#operation/solveClusteringProblem) and use this Batch Cluster endpoint for long running problems only. The work flow is asynchronous:  - send a POST request towards &#x60;https://graphhopper.com/api/1/cluster/calculate?key&#x3D;&lt;your_key&gt;&#x60; and fetch the job_id. - poll the solution every 500ms until it gives &#x60;status&#x3D;finished&#x60;. Do this with a GET request   towards &#x60;https://graphhopper.com/api/1/cluster/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt;&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApiApi apiInstance = new ClusterApiApi(defaultClient);
    ClusterRequest clusterRequest = new ClusterRequest(); // ClusterRequest | Request object that contains the problem to be solved
    try {
      JobId result = apiInstance.asyncClusteringProblem(clusterRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApiApi#asyncClusteringProblem");
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
| **clusterRequest** | [**ClusterRequest**](ClusterRequest.md)| Request object that contains the problem to be solved | |

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

<a id="getClusterSolution"></a>
# **getClusterSolution**
> ClusterResponse getClusterSolution(jobId)

GET Batch Solution Endpoint

This endpoint returns the solution of the clustering problems submitted to the [Batch Cluster endpoint](#operation/asyncClusteringProblem). You can fetch it with the job_id, you have been sent. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApiApi apiInstance = new ClusterApiApi(defaultClient);
    String jobId = "jobId_example"; // String | Request solution with jobId
    try {
      ClusterResponse result = apiInstance.getClusterSolution(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApiApi#getClusterSolution");
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

[**ClusterResponse**](ClusterResponse.md)

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

<a id="solveClusteringProblem"></a>
# **solveClusteringProblem**
> ClusterResponse solveClusteringProblem(clusterRequest)

POST Cluster Endpoint

 The Cluster endpoint is used with a POST request towards &#x60;https://graphhopper.com/api/1/cluster?key&#x3D;&lt;your_key&gt;&#x60;. The solution will be provided in the JSON response. Please note that for problems that take longer than 10 seconds a bad request error is returned. In this case please use the asynchronous [Batch Cluster Endpoint](#operation/asyncClusteringProblem) instead. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApiApi apiInstance = new ClusterApiApi(defaultClient);
    ClusterRequest clusterRequest = new ClusterRequest(); // ClusterRequest | Request object that contains the problem to be solved
    try {
      ClusterResponse result = apiInstance.solveClusteringProblem(clusterRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApiApi#solveClusteringProblem");
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
| **clusterRequest** | [**ClusterRequest**](ClusterRequest.md)| Request object that contains the problem to be solved | |

### Return type

[**ClusterResponse**](ClusterResponse.md)

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

