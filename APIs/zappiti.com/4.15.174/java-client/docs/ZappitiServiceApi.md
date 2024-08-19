# ZappitiServiceApi

All URIs are relative to *http://192.168.1.5:8990*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkZappitiServicePost**](ZappitiServiceApi.md#checkZappitiServicePost) | **POST** /CheckZappitiService | Check if Zappiti Service app status on the player |
| [**installZappitiServicePost**](ZappitiServiceApi.md#installZappitiServicePost) | **POST** /InstallZappitiService | Open a popup that allow the user to install Zappiti Service, if not already installed |
| [**startZappitiServicePost**](ZappitiServiceApi.md#startZappitiServicePost) | **POST** /StartZappitiService | Start Zappiti Service if not started yet |


<a id="checkZappitiServicePost"></a>
# **checkZappitiServicePost**
> CheckZappitiServiceResult checkZappitiServicePost(body)

Check if Zappiti Service app status on the player

ErrorCode.NotInstalled ErrorCode.NotRunning ErrorCode.Running 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZappitiServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://192.168.1.5:8990");

    ZappitiServiceApi apiInstance = new ZappitiServiceApi(defaultClient);
    CheckZappitiServiceRequest body = new CheckZappitiServiceRequest(); // CheckZappitiServiceRequest | 
    try {
      CheckZappitiServiceResult result = apiInstance.checkZappitiServicePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZappitiServiceApi#checkZappitiServicePost");
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
| **body** | [**CheckZappitiServiceRequest**](CheckZappitiServiceRequest.md)|  | |

### Return type

[**CheckZappitiServiceResult**](CheckZappitiServiceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CheckZappitiServiceResult |  -  |

<a id="installZappitiServicePost"></a>
# **installZappitiServicePost**
> InstallZappitiServiceResult installZappitiServicePost(body)

Open a popup that allow the user to install Zappiti Service, if not already installed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZappitiServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://192.168.1.5:8990");

    ZappitiServiceApi apiInstance = new ZappitiServiceApi(defaultClient);
    InstallZappitiServiceRequest body = new InstallZappitiServiceRequest(); // InstallZappitiServiceRequest | 
    try {
      InstallZappitiServiceResult result = apiInstance.installZappitiServicePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZappitiServiceApi#installZappitiServicePost");
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
| **body** | [**InstallZappitiServiceRequest**](InstallZappitiServiceRequest.md)|  | |

### Return type

[**InstallZappitiServiceResult**](InstallZappitiServiceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InstallZappitiServiceResult |  -  |

<a id="startZappitiServicePost"></a>
# **startZappitiServicePost**
> StartZappitiServiceResult startZappitiServicePost(body)

Start Zappiti Service if not started yet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZappitiServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://192.168.1.5:8990");

    ZappitiServiceApi apiInstance = new ZappitiServiceApi(defaultClient);
    StartZappitiServiceRequest body = new StartZappitiServiceRequest(); // StartZappitiServiceRequest | 
    try {
      StartZappitiServiceResult result = apiInstance.startZappitiServicePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZappitiServiceApi#startZappitiServicePost");
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
| **body** | [**StartZappitiServiceRequest**](StartZappitiServiceRequest.md)|  | |

### Return type

[**StartZappitiServiceResult**](StartZappitiServiceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | StartZappitiServiceResult |  -  |

