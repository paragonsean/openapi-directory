# PreviewDeployedDevicesDeviceApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#createDeployedDevicesDevice) | **POST** /DeployedDevices/Fleets/{FleetSid}/Devices |  |
| [**deleteDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#deleteDeployedDevicesDevice) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Devices/{Sid} |  |
| [**fetchDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#fetchDeployedDevicesDevice) | **GET** /DeployedDevices/Fleets/{FleetSid}/Devices/{Sid} |  |
| [**listDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#listDeployedDevicesDevice) | **GET** /DeployedDevices/Fleets/{FleetSid}/Devices |  |
| [**updateDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#updateDeployedDevicesDevice) | **POST** /DeployedDevices/Fleets/{FleetSid}/Devices/{Sid} |  |


<a id="createDeployedDevicesDevice"></a>
# **createDeployedDevicesDevice**
> PreviewDeployedDevicesFleetDevice createDeployedDevicesDevice(fleetSid, deploymentSid, enabled, friendlyName, identity, uniqueName)



Create a new Device in the Fleet, optionally giving it a unique name, friendly name, and assigning to a Deployment and/or human identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeviceApi apiInstance = new PreviewDeployedDevicesDeviceApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String deploymentSid = "deploymentSid_example"; // String | Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
    Boolean enabled = true; // Boolean | 
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
    String identity = "identity_example"; // String | Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
    String uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this Device, to be used in addition to SID, up to 128 characters long.
    try {
      PreviewDeployedDevicesFleetDevice result = apiInstance.createDeployedDevicesDevice(fleetSid, deploymentSid, enabled, friendlyName, identity, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeviceApi#createDeployedDevicesDevice");
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
| **deploymentSid** | **String**| Specifies the unique string identifier of the Deployment group that this Device is going to be associated with. | [optional] |
| **enabled** | **Boolean**|  | [optional] |
| **friendlyName** | **String**| Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long. | [optional] |
| **identity** | **String**| Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long. | [optional] |
| **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Device, to be used in addition to SID, up to 128 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetDevice**](PreviewDeployedDevicesFleetDevice.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteDeployedDevicesDevice"></a>
# **deleteDeployedDevicesDevice**
> deleteDeployedDevicesDevice(fleetSid, sid)



Delete a specific Device from the Fleet, also removing it from associated Deployments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeviceApi apiInstance = new PreviewDeployedDevicesDeviceApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Device resource.
    try {
      apiInstance.deleteDeployedDevicesDevice(fleetSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeviceApi#deleteDeployedDevicesDevice");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Device resource. | |

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

<a id="fetchDeployedDevicesDevice"></a>
# **fetchDeployedDevicesDevice**
> PreviewDeployedDevicesFleetDevice fetchDeployedDevicesDevice(fleetSid, sid)



Fetch information about a specific Device in the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeviceApi apiInstance = new PreviewDeployedDevicesDeviceApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Device resource.
    try {
      PreviewDeployedDevicesFleetDevice result = apiInstance.fetchDeployedDevicesDevice(fleetSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeviceApi#fetchDeployedDevicesDevice");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Device resource. | |

### Return type

[**PreviewDeployedDevicesFleetDevice**](PreviewDeployedDevicesFleetDevice.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeployedDevicesDevice"></a>
# **listDeployedDevicesDevice**
> ListDeployedDevicesDeviceResponse listDeployedDevicesDevice(fleetSid, deploymentSid, pageSize, page, pageToken)



Retrieve a list of all Devices belonging to the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeviceApi apiInstance = new PreviewDeployedDevicesDeviceApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String deploymentSid = "deploymentSid_example"; // String | Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeployedDevicesDeviceResponse result = apiInstance.listDeployedDevicesDevice(fleetSid, deploymentSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeviceApi#listDeployedDevicesDevice");
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
| **deploymentSid** | **String**| Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeployedDevicesDeviceResponse**](ListDeployedDevicesDeviceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDeployedDevicesDevice"></a>
# **updateDeployedDevicesDevice**
> PreviewDeployedDevicesFleetDevice updateDeployedDevicesDevice(fleetSid, sid, deploymentSid, enabled, friendlyName, identity)



Update the given properties of a specific Device in the Fleet, giving it a friendly name, assigning to a Deployment, or a human identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeviceApi apiInstance = new PreviewDeployedDevicesDeviceApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Device resource.
    String deploymentSid = "deploymentSid_example"; // String | Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
    Boolean enabled = true; // Boolean | 
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
    String identity = "identity_example"; // String | Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
    try {
      PreviewDeployedDevicesFleetDevice result = apiInstance.updateDeployedDevicesDevice(fleetSid, sid, deploymentSid, enabled, friendlyName, identity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeviceApi#updateDeployedDevicesDevice");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Device resource. | |
| **deploymentSid** | **String**| Specifies the unique string identifier of the Deployment group that this Device is going to be associated with. | [optional] |
| **enabled** | **Boolean**|  | [optional] |
| **friendlyName** | **String**| Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long. | [optional] |
| **identity** | **String**| Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetDevice**](PreviewDeployedDevicesFleetDevice.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

