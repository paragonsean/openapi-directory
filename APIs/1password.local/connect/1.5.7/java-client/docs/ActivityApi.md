# ActivityApi

All URIs are relative to *http://1password.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getApiActivity**](ActivityApi.md#getApiActivity) | **GET** /activity | Retrieve a list of API Requests that have been made. |


<a id="getApiActivity"></a>
# **getApiActivity**
> List&lt;APIRequest&gt; getApiActivity(limit, offset)

Retrieve a list of API Requests that have been made.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer limit = 50; // Integer | How many API Events should be retrieved in a single request.
    Integer offset = 0; // Integer | How far into the collection of API Events should the response start
    try {
      List<APIRequest> result = apiInstance.getApiActivity(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#getApiActivity");
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
| **limit** | **Integer**| How many API Events should be retrieved in a single request. | [optional] [default to 50] |
| **offset** | **Integer**| How far into the collection of API Events should the response start | [optional] [default to 0] |

### Return type

[**List&lt;APIRequest&gt;**](APIRequest.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Content-Range - An decription of what part of the collection has been returned as well as the total size. <br>  |
| **401** | Invalid or missing token |  -  |

