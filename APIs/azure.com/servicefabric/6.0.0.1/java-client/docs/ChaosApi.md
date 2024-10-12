# ChaosApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChaosReport**](ChaosApi.md#getChaosReport) | **GET** /Tools/Chaos/$/Report | Gets the next segment of the Chaos report based on the passed-in continuation token or the passed-in time-range. |
| [**startChaos**](ChaosApi.md#startChaos) | **POST** /Tools/Chaos/$/Start | Starts Chaos in the cluster. |
| [**stopChaos**](ChaosApi.md#stopChaos) | **POST** /Tools/Chaos/$/Stop | Stops Chaos in the cluster if it is already running, otherwise it does nothing. |


<a id="getChaosReport"></a>
# **getChaosReport**
> ChaosReport getChaosReport(apiVersion, continuationToken, startTimeUtc, endTimeUtc, timeout)

Gets the next segment of the Chaos report based on the passed-in continuation token or the passed-in time-range.

You can either specify the ContinuationToken to get the next segment of the Chaos report or you can specify the time-range through StartTimeUtc and EndTimeUtc, but you cannot specify both the ContinuationToken and the time-range in the same call. When there are more than 100 Chaos events, the Chaos report is returned in segments where a segment contains no more than 100 Chaos events. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChaosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ChaosApi apiInstance = new ChaosApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    String startTimeUtc = "startTimeUtc_example"; // String | The count of ticks representing the start time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v=vs.110%29) for details about tick.
    String endTimeUtc = "endTimeUtc_example"; // String | The count of ticks representing the end time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v=vs.110%29) for details about tick.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      ChaosReport result = apiInstance.getChaosReport(apiVersion, continuationToken, startTimeUtc, endTimeUtc, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChaosApi#getChaosReport");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **startTimeUtc** | **String**| The count of ticks representing the start time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v&#x3D;vs.110%29) for details about tick. | [optional] |
| **endTimeUtc** | **String**| The count of ticks representing the end time of the time range for which a Chaos report is to be generated. Please consult [DateTime.Ticks Property](https://msdn.microsoft.com/en-us/library/system.datetime.ticks%28v&#x3D;vs.110%29) for details about tick. | [optional] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**ChaosReport**](ChaosReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Next segment of Chaos report. |  -  |
| **0** | The detailed error response. |  -  |

<a id="startChaos"></a>
# **startChaos**
> startChaos(apiVersion, chaosParameters, timeout)

Starts Chaos in the cluster.

If Chaos is not already running in the cluster, it starts Chaos with the passed in Chaos parameters. If Chaos is already running when this call is made, the call fails with the error code FABRIC_E_CHAOS_ALREADY_RUNNING. Please refer to the article [Induce controlled Chaos in Service Fabric clusters](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-controlled-chaos) for more details. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChaosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ChaosApi apiInstance = new ChaosApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    ChaosParameters chaosParameters = new ChaosParameters(); // ChaosParameters | Describes all the parameters to configure a Chaos run.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.startChaos(apiVersion, chaosParameters, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChaosApi#startChaos");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **chaosParameters** | [**ChaosParameters**](ChaosParameters.md)| Describes all the parameters to configure a Chaos run. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="stopChaos"></a>
# **stopChaos**
> stopChaos(apiVersion, timeout)

Stops Chaos in the cluster if it is already running, otherwise it does nothing.

Stops Chaos from scheduling further faults; but, the in-flight faults are not affected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChaosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ChaosApi apiInstance = new ChaosApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.stopChaos(apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChaosApi#stopChaos");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

