# WifiApi

All URIs are relative to *http://example.com/setup*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connecttoWiFiNetwork**](WifiApi.md#connecttoWiFiNetwork) | **POST** /connect_wifi | Connect to Wi-Fi Network |
| [**forgetWiFiNetwork**](WifiApi.md#forgetWiFiNetwork) | **POST** /forget_wifi | Forget Wi-Fi Network |
| [**getSavedNetworks**](WifiApi.md#getSavedNetworks) | **GET** /configured_networks | Get Saved Networks |
| [**getWiFiScanResults**](WifiApi.md#getWiFiScanResults) | **GET** /scan_results | Get Wi-Fi Scan Results |
| [**scanforNetworks**](WifiApi.md#scanforNetworks) | **POST** /scan_wifi | Scan for Networks |


<a id="connecttoWiFiNetwork"></a>
# **connecttoWiFiNetwork**
> connecttoWiFiNetwork(connecttoWiFiNetworkRequest)

Connect to Wi-Fi Network

**Note:** Not sure how the password is encrypted. Might be using the public certificate from /setup/eureka_info. So this cannot be used as of now. If someone figures it out, please [create a new issue here](https://github.com/rithvikvibhu/GHLocalApi/issues/new).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WifiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    WifiApi apiInstance = new WifiApi(defaultClient);
    ConnecttoWiFiNetworkRequest connecttoWiFiNetworkRequest = new ConnecttoWiFiNetworkRequest(); // ConnecttoWiFiNetworkRequest | 
    try {
      apiInstance.connecttoWiFiNetwork(connecttoWiFiNetworkRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WifiApi#connecttoWiFiNetwork");
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
| **connecttoWiFiNetworkRequest** | [**ConnecttoWiFiNetworkRequest**](ConnecttoWiFiNetworkRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="forgetWiFiNetwork"></a>
# **forgetWiFiNetwork**
> Object forgetWiFiNetwork(forgetWiFiNetworkRequest)

Forget Wi-Fi Network

This is to forget a saved network by &#x60;wpa_id&#x60;. Get the &#x60;wpa_id&#x60; from /setup/configured_networks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WifiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    WifiApi apiInstance = new WifiApi(defaultClient);
    ForgetWiFiNetworkRequest forgetWiFiNetworkRequest = new ForgetWiFiNetworkRequest(); // ForgetWiFiNetworkRequest | 
    try {
      Object result = apiInstance.forgetWiFiNetwork(forgetWiFiNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WifiApi#forgetWiFiNetwork");
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
| **forgetWiFiNetworkRequest** | [**ForgetWiFiNetworkRequest**](ForgetWiFiNetworkRequest.md)|  | |

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getSavedNetworks"></a>
# **getSavedNetworks**
> List&lt;Example113&gt; getSavedNetworks()

Get Saved Networks

This gets a list of all saved Wi-Fi networks.  Each network has &#x60;ssid&#x60;, &#x60;wpa_auth&#x60;, &#x60;wpa_cipher&#x60; and &#x60;wpa_id&#x60;.   &#x60;wpa_id&#x60; is an incrementing number used to identify a saved network.   #TODO: Add values for &#x60;wpa_auth&#x60; and &#x60;wpa_cipher&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WifiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    WifiApi apiInstance = new WifiApi(defaultClient);
    try {
      List<Example113> result = apiInstance.getSavedNetworks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WifiApi#getSavedNetworks");
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

[**List&lt;Example113&gt;**](Example113.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getWiFiScanResults"></a>
# **getWiFiScanResults**
> List&lt;Example114&gt; getWiFiScanResults()

Get Wi-Fi Scan Results

This gets a list of all nearby Wi-Fi access points.  The list only has the connected AP by default. Once a scan is triggered by &#x60;/setup/scan_wifi&#x60;, the whole list is cached for ~3 minutes. Then it will revert to returning only the connected AP again.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WifiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    WifiApi apiInstance = new WifiApi(defaultClient);
    try {
      List<Example114> result = apiInstance.getWiFiScanResults();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WifiApi#getWiFiScanResults");
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

[**List&lt;Example114&gt;**](Example114.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="scanforNetworks"></a>
# **scanforNetworks**
> Object scanforNetworks()

Scan for Networks

This initiates scanning for Wi-Fi networks.  The results can be obtained with &#x60;/setup/scan_results&#x60; after triggering the scan with this request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WifiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    WifiApi apiInstance = new WifiApi(defaultClient);
    try {
      Object result = apiInstance.scanforNetworks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WifiApi#scanforNetworks");
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

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

