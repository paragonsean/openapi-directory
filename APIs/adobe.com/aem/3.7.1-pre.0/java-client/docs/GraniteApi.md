# GraniteApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sslSetup**](GraniteApi.md#sslSetup) | **POST** /libs/granite/security/post/sslSetup.html |  |


<a id="sslSetup"></a>
# **sslSetup**
> String sslSetup(keystorePassword, keystorePasswordConfirm, truststorePassword, truststorePasswordConfirm, httpsHostname, httpsPort, certificateFile, privatekeyFile)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GraniteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: aemAuth
    HttpBasicAuth aemAuth = (HttpBasicAuth) defaultClient.getAuthentication("aemAuth");
    aemAuth.setUsername("YOUR USERNAME");
    aemAuth.setPassword("YOUR PASSWORD");

    GraniteApi apiInstance = new GraniteApi(defaultClient);
    String keystorePassword = "keystorePassword_example"; // String | 
    String keystorePasswordConfirm = "keystorePasswordConfirm_example"; // String | 
    String truststorePassword = "truststorePassword_example"; // String | 
    String truststorePasswordConfirm = "truststorePasswordConfirm_example"; // String | 
    String httpsHostname = "httpsHostname_example"; // String | 
    String httpsPort = "httpsPort_example"; // String | 
    File certificateFile = new File("/path/to/file"); // File | 
    File privatekeyFile = new File("/path/to/file"); // File | 
    try {
      String result = apiInstance.sslSetup(keystorePassword, keystorePasswordConfirm, truststorePassword, truststorePasswordConfirm, httpsHostname, httpsPort, certificateFile, privatekeyFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GraniteApi#sslSetup");
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
| **keystorePassword** | **String**|  | |
| **keystorePasswordConfirm** | **String**|  | |
| **truststorePassword** | **String**|  | |
| **truststorePasswordConfirm** | **String**|  | |
| **httpsHostname** | **String**|  | |
| **httpsPort** | **String**|  | |
| **certificateFile** | **File**|  | [optional] |
| **privatekeyFile** | **File**|  | [optional] |

### Return type

**String**

### Authorization

[aemAuth](../README.md#aemAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

