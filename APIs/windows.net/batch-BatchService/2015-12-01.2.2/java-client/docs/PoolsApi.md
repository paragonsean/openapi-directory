# PoolsApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**poolAdd**](PoolsApi.md#poolAdd) | **POST** /pools |  |
| [**poolDelete**](PoolsApi.md#poolDelete) | **DELETE** /pools/{poolId} |  |
| [**poolDisableAutoScale**](PoolsApi.md#poolDisableAutoScale) | **POST** /pools/{poolId}/disableautoscale |  |
| [**poolEnableAutoScale**](PoolsApi.md#poolEnableAutoScale) | **POST** /pools/{poolId}/enableautoscale |  |
| [**poolEvaluateAutoScale**](PoolsApi.md#poolEvaluateAutoScale) | **POST** /pools/{poolId}/evaluateautoscale |  |
| [**poolExists**](PoolsApi.md#poolExists) | **HEAD** /pools/{poolId} |  |
| [**poolGet**](PoolsApi.md#poolGet) | **GET** /pools/{poolId} |  |
| [**poolGetAllPoolsLifetimeStatistics**](PoolsApi.md#poolGetAllPoolsLifetimeStatistics) | **GET** /lifetimepoolstats |  |
| [**poolList**](PoolsApi.md#poolList) | **GET** /pools |  |
| [**poolListPoolUsageMetrics**](PoolsApi.md#poolListPoolUsageMetrics) | **GET** /poolusagemetrics |  |
| [**poolPatch**](PoolsApi.md#poolPatch) | **PATCH** /pools/{poolId} |  |
| [**poolResize**](PoolsApi.md#poolResize) | **POST** /pools/{poolId}/resize |  |
| [**poolStopResize**](PoolsApi.md#poolStopResize) | **POST** /pools/{poolId}/stopresize |  |
| [**poolUpdateProperties**](PoolsApi.md#poolUpdateProperties) | **POST** /pools/{poolId}/updateproperties |  |
| [**poolUpgradeOS**](PoolsApi.md#poolUpgradeOS) | **POST** /pools/{poolId}/upgradeos |  |


<a id="poolAdd"></a>
# **poolAdd**
> poolAdd(apiVersion, poolAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Adds a pool to the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    PoolAddParameter poolAddParameter = new PoolAddParameter(); // PoolAddParameter | Specifies the pool to be added.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.poolAdd(apiVersion, poolAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolAdd");
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
| **poolAddParameter** | [**PoolAddParameter**](PoolAddParameter.md)| Specifies the pool to be added. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolDelete"></a>
# **poolDelete**
> poolDelete(poolId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Deletes a pool from the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool to delete.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.poolDelete(poolId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolDelete");
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
| **poolId** | **String**| The id of the pool to delete. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolDisableAutoScale"></a>
# **poolDisableAutoScale**
> poolDisableAutoScale(poolId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)



Disables automatic scaling for a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool on which to disable automatic scaling.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.poolDisableAutoScale(poolId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolDisableAutoScale");
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
| **poolId** | **String**| The id of the pool on which to disable automatic scaling. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolEnableAutoScale"></a>
# **poolEnableAutoScale**
> poolEnableAutoScale(poolId, apiVersion, poolEnableAutoScaleParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Enables automatic scaling for a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool on which to enable automatic scaling.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    PoolEnableAutoScaleParameter poolEnableAutoScaleParameter = new PoolEnableAutoScaleParameter(); // PoolEnableAutoScaleParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.poolEnableAutoScale(poolId, apiVersion, poolEnableAutoScaleParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolEnableAutoScale");
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
| **poolId** | **String**| The id of the pool on which to enable automatic scaling. | |
| **apiVersion** | **String**| Client API Version. | |
| **poolEnableAutoScaleParameter** | [**PoolEnableAutoScaleParameter**](PoolEnableAutoScaleParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolEvaluateAutoScale"></a>
# **poolEvaluateAutoScale**
> AutoScaleRun poolEvaluateAutoScale(poolId, apiVersion, poolEvaluateAutoScaleParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Gets the result of evaluating an automatic scaling formula on the pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool on which to evaluate the automatic scaling formula.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    PoolEvaluateAutoScaleParameter poolEvaluateAutoScaleParameter = new PoolEvaluateAutoScaleParameter(); // PoolEvaluateAutoScaleParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      AutoScaleRun result = apiInstance.poolEvaluateAutoScale(poolId, apiVersion, poolEvaluateAutoScaleParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolEvaluateAutoScale");
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
| **poolId** | **String**| The id of the pool on which to evaluate the automatic scaling formula. | |
| **apiVersion** | **String**| Client API Version. | |
| **poolEvaluateAutoScaleParameter** | [**PoolEvaluateAutoScaleParameter**](PoolEvaluateAutoScaleParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**AutoScaleRun**](AutoScaleRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolExists"></a>
# **poolExists**
> poolExists(poolId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Gets basic properties of a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool to get.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.poolExists(poolId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolExists");
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
| **poolId** | **String**| The id of the pool to get. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **404** | Pool not found |  -  |
| **0** | Error from the Batch service |  -  |

<a id="poolGet"></a>
# **poolGet**
> CloudPool poolGet(poolId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Gets information about the specified pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool to get.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    String $expand = "$expand_example"; // String | Sets an OData $expand clause.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      CloudPool result = apiInstance.poolGet(poolId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolGet");
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
| **poolId** | **String**| The id of the pool to get. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **$expand** | **String**| Sets an OData $expand clause. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

[**CloudPool**](CloudPool.md)

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

<a id="poolGetAllPoolsLifetimeStatistics"></a>
# **poolGetAllPoolsLifetimeStatistics**
> PoolStatistics poolGetAllPoolsLifetimeStatistics(apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)



Gets lifetime summary statistics for all of the pools in the specified account. Statistics are aggregated across all pools that have ever existed in the account, from account creation to the last update time of the statistics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      PoolStatistics result = apiInstance.poolGetAllPoolsLifetimeStatistics(apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolGetAllPoolsLifetimeStatistics");
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
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**PoolStatistics**](PoolStatistics.md)

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

<a id="poolList"></a>
# **poolList**
> CloudPoolListResult poolList(apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the pools in the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | Sets an OData $filter clause.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    String $expand = "$expand_example"; // String | Sets an OData $expand clause.
    Integer maxresults = 56; // Integer | Sets the maximum number of items to return in the response.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      CloudPoolListResult result = apiInstance.poolList(apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolList");
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
| **$filter** | **String**| Sets an OData $filter clause. | [optional] |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **$expand** | **String**| Sets an OData $expand clause. | [optional] |
| **maxresults** | **Integer**| Sets the maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CloudPoolListResult**](CloudPoolListResult.md)

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

<a id="poolListPoolUsageMetrics"></a>
# **poolListPoolUsageMetrics**
> PoolListPoolUsageMetricsResult poolListPoolUsageMetrics(apiVersion, starttime, endtime, $filter, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists the usage metrics, aggregated by pool across individual time intervals, for the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    OffsetDateTime starttime = OffsetDateTime.now(); // OffsetDateTime | The earliest time from which to include metrics. This must be at least two and a half hours before the current time.
    OffsetDateTime endtime = OffsetDateTime.now(); // OffsetDateTime | The latest time from which to include metrics. This must be at least two hours before the current time.
    String $filter = "$filter_example"; // String | Sets an OData $filter clause.
    Integer maxresults = 56; // Integer | Sets the maximum number of items to return in the response.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      PoolListPoolUsageMetricsResult result = apiInstance.poolListPoolUsageMetrics(apiVersion, starttime, endtime, $filter, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolListPoolUsageMetrics");
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
| **starttime** | **OffsetDateTime**| The earliest time from which to include metrics. This must be at least two and a half hours before the current time. | [optional] |
| **endtime** | **OffsetDateTime**| The latest time from which to include metrics. This must be at least two hours before the current time. | [optional] |
| **$filter** | **String**| Sets an OData $filter clause. | [optional] |
| **maxresults** | **Integer**| Sets the maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**PoolListPoolUsageMetricsResult**](PoolListPoolUsageMetricsResult.md)

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

<a id="poolPatch"></a>
# **poolPatch**
> poolPatch(poolId, apiVersion, poolPatchParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Updates the properties of a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    PoolPatchParameter poolPatchParameter = new PoolPatchParameter(); // PoolPatchParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.poolPatch(poolId, apiVersion, poolPatchParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolPatch");
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
| **poolId** | **String**| The id of the pool to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **poolPatchParameter** | [**PoolPatchParameter**](PoolPatchParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolResize"></a>
# **poolResize**
> poolResize(poolId, apiVersion, poolResizeParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Changes the number of compute nodes that are assigned to a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool to resize.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    PoolResizeParameter poolResizeParameter = new PoolResizeParameter(); // PoolResizeParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.poolResize(poolId, apiVersion, poolResizeParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolResize");
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
| **poolId** | **String**| The id of the pool to resize. | |
| **apiVersion** | **String**| Client API Version. | |
| **poolResizeParameter** | [**PoolResizeParameter**](PoolResizeParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolStopResize"></a>
# **poolStopResize**
> poolStopResize(poolId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Stops an ongoing resize operation on the pool. This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool whose resizing you want to stop.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.poolStopResize(poolId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolStopResize");
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
| **poolId** | **String**| The id of the pool whose resizing you want to stop. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolUpdateProperties"></a>
# **poolUpdateProperties**
> poolUpdateProperties(poolId, apiVersion, poolUpdatePropertiesParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Updates the properties of a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    PoolUpdatePropertiesParameter poolUpdatePropertiesParameter = new PoolUpdatePropertiesParameter(); // PoolUpdatePropertiesParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.poolUpdateProperties(poolId, apiVersion, poolUpdatePropertiesParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolUpdateProperties");
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
| **poolId** | **String**| The id of the pool to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **poolUpdatePropertiesParameter** | [**PoolUpdatePropertiesParameter**](PoolUpdatePropertiesParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="poolUpgradeOS"></a>
# **poolUpgradeOS**
> poolUpgradeOS(poolId, apiVersion, poolUpgradeOSParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Upgrades the operating system of the specified pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    PoolsApi apiInstance = new PoolsApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool to upgrade.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    PoolUpgradeOSParameter poolUpgradeOSParameter = new PoolUpgradeOSParameter(); // PoolUpgradeOSParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.poolUpgradeOS(poolId, apiVersion, poolUpgradeOSParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoolsApi#poolUpgradeOS");
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
| **poolId** | **String**| The id of the pool to upgrade. | |
| **apiVersion** | **String**| Client API Version. | |
| **poolUpgradeOSParameter** | [**PoolUpgradeOSParameter**](PoolUpgradeOSParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

