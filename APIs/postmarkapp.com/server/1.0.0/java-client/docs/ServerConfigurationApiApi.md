# ServerConfigurationApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**editCurrentServerConfiguration**](ServerConfigurationApiApi.md#editCurrentServerConfiguration) | **PUT** /server | Edit Server Configuration |
| [**getCurrentServerConfiguration**](ServerConfigurationApiApi.md#getCurrentServerConfiguration) | **GET** /server | Get Server Configuration |


<a id="editCurrentServerConfiguration"></a>
# **editCurrentServerConfiguration**
> ServerConfigurationResponse editCurrentServerConfiguration(xPostmarkServerToken, body)

Edit Server Configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerConfigurationApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    ServerConfigurationApiApi apiInstance = new ServerConfigurationApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    EditServerConfigurationRequest body = new EditServerConfigurationRequest(); // EditServerConfigurationRequest | The settings that should be modified for the current server.
    try {
      ServerConfigurationResponse result = apiInstance.editCurrentServerConfiguration(xPostmarkServerToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerConfigurationApiApi#editCurrentServerConfiguration");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **body** | [**EditServerConfigurationRequest**](EditServerConfigurationRequest.md)| The settings that should be modified for the current server. | [optional] |

### Return type

[**ServerConfigurationResponse**](ServerConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getCurrentServerConfiguration"></a>
# **getCurrentServerConfiguration**
> ServerConfigurationResponse getCurrentServerConfiguration(xPostmarkServerToken)

Get Server Configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerConfigurationApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    ServerConfigurationApiApi apiInstance = new ServerConfigurationApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    try {
      ServerConfigurationResponse result = apiInstance.getCurrentServerConfiguration(xPostmarkServerToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerConfigurationApiApi#getCurrentServerConfiguration");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |

### Return type

[**ServerConfigurationResponse**](ServerConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

