# AuthenticationDevicesApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateNewDeviceCodes**](AuthenticationDevicesApi.md#generateNewDeviceCodes) | **POST** /oauth/device/code | Generate new device codes |
| [**pollForTheAccessToken**](AuthenticationDevicesApi.md#pollForTheAccessToken) | **POST** /oauth/device/token | Poll for the access_token |


<a id="generateNewDeviceCodes"></a>
# **generateNewDeviceCodes**
> generateNewDeviceCodes(generateNewDeviceCodesRequest)

Generate new device codes

Generate new codes to start the device authentication process. The &#x60;device_code&#x60; and &#x60;interval&#x60; will be used later to poll for the &#x60;access_token&#x60;. The &#x60;user_code&#x60; and &#x60;verification_url&#x60; should be presented to the user as mentioned in the flow steps above.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationDevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    AuthenticationDevicesApi apiInstance = new AuthenticationDevicesApi(defaultClient);
    GenerateNewDeviceCodesRequest generateNewDeviceCodesRequest = new GenerateNewDeviceCodesRequest(); // GenerateNewDeviceCodesRequest | 
    try {
      apiInstance.generateNewDeviceCodes(generateNewDeviceCodesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationDevicesApi#generateNewDeviceCodes");
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
| **generateNewDeviceCodesRequest** | [**GenerateNewDeviceCodesRequest**](GenerateNewDeviceCodesRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="pollForTheAccessToken"></a>
# **pollForTheAccessToken**
> pollForTheAccessToken(pollForTheAccessTokenRequest)

Poll for the access_token

Use the &#x60;device_code&#x60; and poll at the &#x60;interval&#x60; (in seconds) to check if the user has authorized you app. Use &#x60;expires_in&#x60; to stop polling after that many seconds, and gracefully instruct the user to restart the process. **It is important to poll at the correct interval and also stop polling when expired.**  When you receive a &#x60;200&#x60; success response, save the &#x60;access_token&#x60; so your app can authenticate the user in methods that require it. The &#x60;access_token&#x60; is valid for 3 months. Save and use the &#x60;refresh_token&#x60; to get a new &#x60;access_token&#x60; without asking the user to re-authenticate. Check below for all the error codes that you should handle.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;code&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | &#x60;device_code&#x60; from the initial method. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. |  ####  Status Codes  This method will send various HTTP status codes that you should handle accordingly.  | Code | Description | |---|---| | &#x60;200&#x60; | Success - *save the &#x60;access_token&#x60;* | &#x60;400&#x60; | Pending - *waiting for the user to authorize your app* | &#x60;404&#x60; | Not Found - *invalid &#x60;device_code&#x60;* | &#x60;409&#x60; | Already Used - *user already approved this code* | &#x60;410&#x60; | Expired - *the tokens have expired, restart the process* | &#x60;418&#x60; | Denied - *user explicitly denied this code* | &#x60;429&#x60; | Slow Down - *your app is polling too quickly*

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationDevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    AuthenticationDevicesApi apiInstance = new AuthenticationDevicesApi(defaultClient);
    PollForTheAccessTokenRequest pollForTheAccessTokenRequest = new PollForTheAccessTokenRequest(); // PollForTheAccessTokenRequest | 
    try {
      apiInstance.pollForTheAccessToken(pollForTheAccessTokenRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationDevicesApi#pollForTheAccessToken");
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
| **pollForTheAccessTokenRequest** | [**PollForTheAccessTokenRequest**](PollForTheAccessTokenRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

