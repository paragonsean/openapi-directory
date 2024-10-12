# PreviewDeployedDevicesCertificateApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#createDeployedDevicesCertificate) | **POST** /DeployedDevices/Fleets/{FleetSid}/Certificates |  |
| [**deleteDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#deleteDeployedDevicesCertificate) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Certificates/{Sid} |  |
| [**fetchDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#fetchDeployedDevicesCertificate) | **GET** /DeployedDevices/Fleets/{FleetSid}/Certificates/{Sid} |  |
| [**listDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#listDeployedDevicesCertificate) | **GET** /DeployedDevices/Fleets/{FleetSid}/Certificates |  |
| [**updateDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#updateDeployedDevicesCertificate) | **POST** /DeployedDevices/Fleets/{FleetSid}/Certificates/{Sid} |  |


<a id="createDeployedDevicesCertificate"></a>
# **createDeployedDevicesCertificate**
> PreviewDeployedDevicesFleetCertificate createDeployedDevicesCertificate(fleetSid, certificateData, deviceSid, friendlyName)



Enroll a new Certificate credential to the Fleet, optionally giving it a friendly name and assigning to a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesCertificateApi apiInstance = new PreviewDeployedDevicesCertificateApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String certificateData = "certificateData_example"; // String | Provides a URL encoded representation of the public certificate in PEM format.
    String deviceSid = "deviceSid_example"; // String | Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
    try {
      PreviewDeployedDevicesFleetCertificate result = apiInstance.createDeployedDevicesCertificate(fleetSid, certificateData, deviceSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesCertificateApi#createDeployedDevicesCertificate");
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
| **fleetSid** | **String**|  | |
| **certificateData** | **String**| Provides a URL encoded representation of the public certificate in PEM format. | |
| **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential. | [optional] |
| **friendlyName** | **String**| Provides a human readable descriptive text for this Certificate credential, up to 256 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetCertificate**](PreviewDeployedDevicesFleetCertificate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteDeployedDevicesCertificate"></a>
# **deleteDeployedDevicesCertificate**
> deleteDeployedDevicesCertificate(fleetSid, sid)



Unregister a specific Certificate credential from the Fleet, effectively disallowing any inbound client connections that are presenting it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesCertificateApi apiInstance = new PreviewDeployedDevicesCertificateApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
    try {
      apiInstance.deleteDeployedDevicesCertificate(fleetSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesCertificateApi#deleteDeployedDevicesCertificate");
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
| **fleetSid** | **String**|  | |
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Certificate credential resource. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchDeployedDevicesCertificate"></a>
# **fetchDeployedDevicesCertificate**
> PreviewDeployedDevicesFleetCertificate fetchDeployedDevicesCertificate(fleetSid, sid)



Fetch information about a specific Certificate credential in the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesCertificateApi apiInstance = new PreviewDeployedDevicesCertificateApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
    try {
      PreviewDeployedDevicesFleetCertificate result = apiInstance.fetchDeployedDevicesCertificate(fleetSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesCertificateApi#fetchDeployedDevicesCertificate");
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
| **fleetSid** | **String**|  | |
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Certificate credential resource. | |

### Return type

[**PreviewDeployedDevicesFleetCertificate**](PreviewDeployedDevicesFleetCertificate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeployedDevicesCertificate"></a>
# **listDeployedDevicesCertificate**
> ListDeployedDevicesCertificateResponse listDeployedDevicesCertificate(fleetSid, deviceSid, pageSize, page, pageToken)



Retrieve a list of all Certificate credentials belonging to the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesCertificateApi apiInstance = new PreviewDeployedDevicesCertificateApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String deviceSid = "deviceSid_example"; // String | Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeployedDevicesCertificateResponse result = apiInstance.listDeployedDevicesCertificate(fleetSid, deviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesCertificateApi#listDeployedDevicesCertificate");
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
| **fleetSid** | **String**|  | |
| **deviceSid** | **String**| Filters the resulting list of Certificates by a unique string identifier of an authenticated Device. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeployedDevicesCertificateResponse**](ListDeployedDevicesCertificateResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDeployedDevicesCertificate"></a>
# **updateDeployedDevicesCertificate**
> PreviewDeployedDevicesFleetCertificate updateDeployedDevicesCertificate(fleetSid, sid, deviceSid, friendlyName)



Update the given properties of a specific Certificate credential in the Fleet, giving it a friendly name or assigning to a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesCertificateApi apiInstance = new PreviewDeployedDevicesCertificateApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
    String deviceSid = "deviceSid_example"; // String | Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
    try {
      PreviewDeployedDevicesFleetCertificate result = apiInstance.updateDeployedDevicesCertificate(fleetSid, sid, deviceSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesCertificateApi#updateDeployedDevicesCertificate");
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
| **fleetSid** | **String**|  | |
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Certificate credential resource. | |
| **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential. | [optional] |
| **friendlyName** | **String**| Provides a human readable descriptive text for this Certificate credential, up to 256 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetCertificate**](PreviewDeployedDevicesFleetCertificate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

