# ApiInfoApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containersMessagesGet**](ApiInfoApi.md#containersMessagesGet) | **GET** /containers/messages | List messages for the user |
| [**containersVersionGet**](ApiInfoApi.md#containersVersionGet) | **GET** /containers/version | List latest API version |


<a id="containersMessagesGet"></a>
# **containersMessagesGet**
> ContainersMessagesGet200Response containersMessagesGet(xAuthToken, xAuthProjectId)

List messages for the user

This endpoint retrieves all IBM Containers system messages for the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ApiInfoApi apiInstance = new ApiInfoApi(defaultClient);
    String xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
    String xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. To retrieve your space ID, run `cf space <space_name> --guid` and replace `<space_name>` with the name of the space where you want to create or work with your container. 
    try {
      ContainersMessagesGet200Response result = apiInstance.containersMessagesGet(xAuthToken, xAuthProjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiInfoApi#containersMessagesGet");
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
| **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | |
| **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. To retrieve your space ID, run &#x60;cf space &lt;space_name&gt; --guid&#x60; and replace &#x60;&lt;space_name&gt;&#x60; with the name of the space where you want to create or work with your container.  | |

### Return type

[**ContainersMessagesGet200Response**](ContainersMessagesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list of messages is returned. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

<a id="containersVersionGet"></a>
# **containersVersionGet**
> ContainersVersionGetInfo containersVersionGet()

List latest API version

This endpoint retrieves a list of all microservices that are used in the IBM Containers service with their current build version. This method does not require authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://containers-api.ng.bluemix.net/v3");

    ApiInfoApi apiInstance = new ApiInfoApi(defaultClient);
    try {
      ContainersVersionGetInfo result = apiInstance.containersVersionGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiInfoApi#containersVersionGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContainersVersionGetInfo**](ContainersVersionGetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. A list of the current API and microservices versions is returend. |  -  |
| **500** | Internal Server Error. The IBM Containers service is currently unavailable. Your request could not be processed. Please wait a few minutes and try again. If you still encounter this problem, note the incident ID and contact the IBM Bluemix support. |  -  |

