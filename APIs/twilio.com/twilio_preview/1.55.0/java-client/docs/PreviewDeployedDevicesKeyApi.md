# PreviewDeployedDevicesKeyApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#createDeployedDevicesKey) | **POST** /DeployedDevices/Fleets/{FleetSid}/Keys |  |
| [**deleteDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#deleteDeployedDevicesKey) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Keys/{Sid} |  |
| [**fetchDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#fetchDeployedDevicesKey) | **GET** /DeployedDevices/Fleets/{FleetSid}/Keys/{Sid} |  |
| [**listDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#listDeployedDevicesKey) | **GET** /DeployedDevices/Fleets/{FleetSid}/Keys |  |
| [**updateDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#updateDeployedDevicesKey) | **POST** /DeployedDevices/Fleets/{FleetSid}/Keys/{Sid} |  |


<a id="createDeployedDevicesKey"></a>
# **createDeployedDevicesKey**
> PreviewDeployedDevicesFleetKey createDeployedDevicesKey(fleetSid, deviceSid, friendlyName)



Create a new Key credential in the Fleet, optionally giving it a friendly name and assigning to a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesKeyApi apiInstance = new PreviewDeployedDevicesKeyApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String deviceSid = "deviceSid_example"; // String | Provides the unique string identifier of an existing Device to become authenticated with this Key credential.
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Key credential, up to 256 characters long.
    try {
      PreviewDeployedDevicesFleetKey result = apiInstance.createDeployedDevicesKey(fleetSid, deviceSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesKeyApi#createDeployedDevicesKey");
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
| **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Key credential. | [optional] |
| **friendlyName** | **String**| Provides a human readable descriptive text for this Key credential, up to 256 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetKey**](PreviewDeployedDevicesFleetKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteDeployedDevicesKey"></a>
# **deleteDeployedDevicesKey**
> deleteDeployedDevicesKey(fleetSid, sid)



Delete a specific Key credential from the Fleet, effectively disallowing any inbound client connections that are presenting it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesKeyApi apiInstance = new PreviewDeployedDevicesKeyApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Key credential resource.
    try {
      apiInstance.deleteDeployedDevicesKey(fleetSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesKeyApi#deleteDeployedDevicesKey");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Key credential resource. | |

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

<a id="fetchDeployedDevicesKey"></a>
# **fetchDeployedDevicesKey**
> PreviewDeployedDevicesFleetKey fetchDeployedDevicesKey(fleetSid, sid)



Fetch information about a specific Key credential in the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesKeyApi apiInstance = new PreviewDeployedDevicesKeyApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Key credential resource.
    try {
      PreviewDeployedDevicesFleetKey result = apiInstance.fetchDeployedDevicesKey(fleetSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesKeyApi#fetchDeployedDevicesKey");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Key credential resource. | |

### Return type

[**PreviewDeployedDevicesFleetKey**](PreviewDeployedDevicesFleetKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeployedDevicesKey"></a>
# **listDeployedDevicesKey**
> ListDeployedDevicesKeyResponse listDeployedDevicesKey(fleetSid, deviceSid, pageSize, page, pageToken)



Retrieve a list of all Keys credentials belonging to the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesKeyApi apiInstance = new PreviewDeployedDevicesKeyApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String deviceSid = "deviceSid_example"; // String | Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeployedDevicesKeyResponse result = apiInstance.listDeployedDevicesKey(fleetSid, deviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesKeyApi#listDeployedDevicesKey");
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
| **deviceSid** | **String**| Filters the resulting list of Keys by a unique string identifier of an authenticated Device. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeployedDevicesKeyResponse**](ListDeployedDevicesKeyResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDeployedDevicesKey"></a>
# **updateDeployedDevicesKey**
> PreviewDeployedDevicesFleetKey updateDeployedDevicesKey(fleetSid, sid, deviceSid, friendlyName)



Update the given properties of a specific Key credential in the Fleet, giving it a friendly name or assigning to a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesKeyApi apiInstance = new PreviewDeployedDevicesKeyApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Key credential resource.
    String deviceSid = "deviceSid_example"; // String | Provides the unique string identifier of an existing Device to become authenticated with this Key credential.
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Key credential, up to 256 characters long.
    try {
      PreviewDeployedDevicesFleetKey result = apiInstance.updateDeployedDevicesKey(fleetSid, sid, deviceSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesKeyApi#updateDeployedDevicesKey");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Key credential resource. | |
| **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Key credential. | [optional] |
| **friendlyName** | **String**| Provides a human readable descriptive text for this Key credential, up to 256 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetKey**](PreviewDeployedDevicesFleetKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

