# ServerlessV1LogApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchLog**](ServerlessV1LogApi.md#fetchLog) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Logs/{Sid} |  |
| [**listLog**](ServerlessV1LogApi.md#listLog) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Logs |  |


<a id="fetchLog"></a>
# **fetchLog**
> ServerlessV1ServiceEnvironmentLog fetchLog(serviceSid, environmentSid, sid)



Retrieve a specific log.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1LogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1LogApi apiInstance = new ServerlessV1LogApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Log resource from.
    String environmentSid = "environmentSid_example"; // String | The SID of the environment with the Log resource to fetch.
    String sid = "sid_example"; // String | The SID of the Log resource to fetch.
    try {
      ServerlessV1ServiceEnvironmentLog result = apiInstance.fetchLog(serviceSid, environmentSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1LogApi#fetchLog");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Log resource from. | |
| **environmentSid** | **String**| The SID of the environment with the Log resource to fetch. | |
| **sid** | **String**| The SID of the Log resource to fetch. | |

### Return type

[**ServerlessV1ServiceEnvironmentLog**](ServerlessV1ServiceEnvironmentLog.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listLog"></a>
# **listLog**
> ListLogResponse listLog(serviceSid, environmentSid, functionSid, startDate, endDate, pageSize, page, pageToken)



Retrieve a list of all logs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1LogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1LogApi apiInstance = new ServerlessV1LogApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Log resource from.
    String environmentSid = "environmentSid_example"; // String | The SID of the environment with the Log resources to read.
    String functionSid = "functionSid_example"; // String | The SID of the function whose invocation produced the Log resources to read.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The date/time (in GMT, ISO 8601) after which the Log resources must have been created. Defaults to 1 day prior to current date/time.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The date/time (in GMT, ISO 8601) before which the Log resources must have been created. Defaults to current date/time.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListLogResponse result = apiInstance.listLog(serviceSid, environmentSid, functionSid, startDate, endDate, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1LogApi#listLog");
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
| **serviceSid** | **String**| The SID of the Service to read the Log resource from. | |
| **environmentSid** | **String**| The SID of the environment with the Log resources to read. | |
| **functionSid** | **String**| The SID of the function whose invocation produced the Log resources to read. | [optional] |
| **startDate** | **OffsetDateTime**| The date/time (in GMT, ISO 8601) after which the Log resources must have been created. Defaults to 1 day prior to current date/time. | [optional] |
| **endDate** | **OffsetDateTime**| The date/time (in GMT, ISO 8601) before which the Log resources must have been created. Defaults to current date/time. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListLogResponse**](ListLogResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

