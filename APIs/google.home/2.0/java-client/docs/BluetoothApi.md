# BluetoothApi

All URIs are relative to *http://example.com/setup*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeDiscoverability**](BluetoothApi.md#changeDiscoverability) | **POST** /bluetooth/discovery | Change Discoverability |
| [**forgetpaireddevice**](BluetoothApi.md#forgetpaireddevice) | **POST** /bluetooth/bond | Forget paired device |
| [**getPairedDevices**](BluetoothApi.md#getPairedDevices) | **GET** /bluetooth/get_bonded | Get Paired Devices |
| [**getScanResults**](BluetoothApi.md#getScanResults) | **GET** /bluetooth/scan_results | Get Scan Results |
| [**pairwithSpeaker**](BluetoothApi.md#pairwithSpeaker) | **POST** /bluetooth/connect | Pair with Speaker |
| [**scanfordevices**](BluetoothApi.md#scanfordevices) | **POST** /bluetooth/scan | Scan for devices |
| [**status**](BluetoothApi.md#status) | **GET** /bluetooth/status | Status |


<a id="changeDiscoverability"></a>
# **changeDiscoverability**
> Object changeDiscoverability(changeDiscoverabilityRequest)

Change Discoverability

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 1 only**  This enables/disables Home&#39;s bluetooth discovery and other devices can pair with Home (where Home acts as a speaker).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    ChangeDiscoverabilityRequest changeDiscoverabilityRequest = new ChangeDiscoverabilityRequest(); // ChangeDiscoverabilityRequest | 
    try {
      Object result = apiInstance.changeDiscoverability(changeDiscoverabilityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#changeDiscoverability");
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
| **changeDiscoverabilityRequest** | [**ChangeDiscoverabilityRequest**](ChangeDiscoverabilityRequest.md)|  | |

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

<a id="forgetpaireddevice"></a>
# **forgetpaireddevice**
> Object forgetpaireddevice(forgetpaireddeviceRequest)

Forget paired device

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For both parts**  This is to forget paired devices by mac address. Works for both kinds of devices (Part 1 and Part 2).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    ForgetpaireddeviceRequest forgetpaireddeviceRequest = new ForgetpaireddeviceRequest(); // ForgetpaireddeviceRequest | 
    try {
      Object result = apiInstance.forgetpaireddevice(forgetpaireddeviceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#forgetpaireddevice");
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
| **forgetpaireddeviceRequest** | [**ForgetpaireddeviceRequest**](ForgetpaireddeviceRequest.md)|  | |

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

<a id="getPairedDevices"></a>
# **getPairedDevices**
> List&lt;Example111&gt; getPairedDevices()

Get Paired Devices

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For both parts**  This gives a list of all paired or &#39;bonded&#39; devices. The response field names are self-descriptive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    try {
      List<Example111> result = apiInstance.getPairedDevices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#getPairedDevices");
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

[**List&lt;Example111&gt;**](Example111.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getScanResults"></a>
# **getScanResults**
> List&lt;Example112&gt; getScanResults()

Get Scan Results

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This returns a list of all nearby bluetooth devices. While the Home app only shows speakers, this list contains all devices including TVs, mobiles, etc.  &#x60;rssi&#x60; is signal strength, &#x60;name&#x60; is name, &#x60;mac_address&#x60; is mac address.   &#x60;device_class&#x60; and &#x60;device_type&#x60; are bluetooth codes.    The Home app only lists those devices with &#x60;expected_profiles&#x60; &gt; 0. Basically, the device should function as a speaker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    try {
      List<Example112> result = apiInstance.getScanResults();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#getScanResults");
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

[**List&lt;Example112&gt;**](Example112.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="pairwithSpeaker"></a>
# **pairwithSpeaker**
> Object pairwithSpeaker(pairwithSpeakerRequest)

Pair with Speaker

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This pairs with other bluetooth speakers by mac address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    PairwithSpeakerRequest pairwithSpeakerRequest = new PairwithSpeakerRequest(); // PairwithSpeakerRequest | 
    try {
      Object result = apiInstance.pairwithSpeaker(pairwithSpeakerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#pairwithSpeaker");
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
| **pairwithSpeakerRequest** | [**PairwithSpeakerRequest**](PairwithSpeakerRequest.md)|  | |

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

<a id="scanfordevices"></a>
# **scanfordevices**
> Object scanfordevices(scanfordevicesRequest)

Scan for devices

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This initiates scan for other bluetooth speakers/devices. Scan results will be updated continuously for &#x60;timeout&#x60; seconds.   To get the scan results, see /setup/bluetooth/scan_results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    ScanfordevicesRequest scanfordevicesRequest = new ScanfordevicesRequest(); // ScanfordevicesRequest | 
    try {
      Object result = apiInstance.scanfordevices(scanfordevicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#scanfordevices");
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
| **scanfordevicesRequest** | [**ScanfordevicesRequest**](ScanfordevicesRequest.md)|  | |

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

<a id="status"></a>
# **status**
> Example110 status()

Status

&gt; **There are 2 parts of Bluetooth.** &gt; &gt; *Part 1*: Devices like phones connect to Home and play audio through Home.   &gt; For this, /setup/bluetooth/discovery is used to make Home discoverable. Then devices can connect to it as if Home is just another bluetooth speaker. &gt; &gt; *Part 2*: Bluetooth speakers connect to Home and Home plays audio through the speakers. &gt; For this, /setup/bluetooth/scan and /setup/bluetooth/scan_results are used to connect to other speakers. &gt; &gt; The other endpoints are common for both parts.   **For both parts**  This gives the status of all bluetooth things. - Not sure what &#x60;audio_mode&#x60; is. - &#x60;discovery_enabled&#x60; states whether Home is discoverable. (**Part 1**) - &#x60;connecting_devices&#x60; is a list of all media sources (like phones) connected to Home. (**Part 1**) - &#x60;scanning_enabled&#x60; states whether Home scanning for other bluetooth speakers/devices. (**Part 2**) - &#x60;connected_devices&#x60; is a list of all speakers connected to Home. (**Part 2**)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    try {
      Example110 result = apiInstance.status();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#status");
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

[**Example110**](Example110.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

