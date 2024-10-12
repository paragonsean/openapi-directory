# ServerlessV1FunctionVersionContentApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchFunctionVersionContent**](ServerlessV1FunctionVersionContentApi.md#fetchFunctionVersionContent) | **GET** /v1/Services/{ServiceSid}/Functions/{FunctionSid}/Versions/{Sid}/Content |  |


<a id="fetchFunctionVersionContent"></a>
# **fetchFunctionVersionContent**
> ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent fetchFunctionVersionContent(serviceSid, functionSid, sid)



Retrieve a the content of a specific Function Version resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionVersionContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionVersionContentApi apiInstance = new ServerlessV1FunctionVersionContentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Function Version content from.
    String functionSid = "functionSid_example"; // String | The SID of the Function that is the parent of the Function Version content to fetch.
    String sid = "sid_example"; // String | The SID of the Function Version content to fetch.
    try {
      ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent result = apiInstance.fetchFunctionVersionContent(serviceSid, functionSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionVersionContentApi#fetchFunctionVersionContent");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Function Version content from. | |
| **functionSid** | **String**| The SID of the Function that is the parent of the Function Version content to fetch. | |
| **sid** | **String**| The SID of the Function Version content to fetch. | |

### Return type

[**ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent**](ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

