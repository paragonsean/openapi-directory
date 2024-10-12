# ServerlessV1FunctionVersionApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchFunctionVersion**](ServerlessV1FunctionVersionApi.md#fetchFunctionVersion) | **GET** /v1/Services/{ServiceSid}/Functions/{FunctionSid}/Versions/{Sid} |  |
| [**listFunctionVersion**](ServerlessV1FunctionVersionApi.md#listFunctionVersion) | **GET** /v1/Services/{ServiceSid}/Functions/{FunctionSid}/Versions |  |


<a id="fetchFunctionVersion"></a>
# **fetchFunctionVersion**
> ServerlessV1ServiceFunctionFunctionVersion fetchFunctionVersion(serviceSid, functionSid, sid)



Retrieve a specific Function Version resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionVersionApi apiInstance = new ServerlessV1FunctionVersionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Function Version resource from.
    String functionSid = "functionSid_example"; // String | The SID of the function that is the parent of the Function Version resource to fetch.
    String sid = "sid_example"; // String | The SID of the Function Version resource to fetch.
    try {
      ServerlessV1ServiceFunctionFunctionVersion result = apiInstance.fetchFunctionVersion(serviceSid, functionSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionVersionApi#fetchFunctionVersion");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Function Version resource from. | |
| **functionSid** | **String**| The SID of the function that is the parent of the Function Version resource to fetch. | |
| **sid** | **String**| The SID of the Function Version resource to fetch. | |

### Return type

[**ServerlessV1ServiceFunctionFunctionVersion**](ServerlessV1ServiceFunctionFunctionVersion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listFunctionVersion"></a>
# **listFunctionVersion**
> ListFunctionVersionResponse listFunctionVersion(serviceSid, functionSid, pageSize, page, pageToken)



Retrieve a list of all Function Version resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionVersionApi apiInstance = new ServerlessV1FunctionVersionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Function Version resources from.
    String functionSid = "functionSid_example"; // String | The SID of the function that is the parent of the Function Version resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListFunctionVersionResponse result = apiInstance.listFunctionVersion(serviceSid, functionSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionVersionApi#listFunctionVersion");
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
| **serviceSid** | **String**| The SID of the Service to read the Function Version resources from. | |
| **functionSid** | **String**| The SID of the function that is the parent of the Function Version resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListFunctionVersionResponse**](ListFunctionVersionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

