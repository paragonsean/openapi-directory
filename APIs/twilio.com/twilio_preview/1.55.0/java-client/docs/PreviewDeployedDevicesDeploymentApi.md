# PreviewDeployedDevicesDeploymentApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#createDeployedDevicesDeployment) | **POST** /DeployedDevices/Fleets/{FleetSid}/Deployments |  |
| [**deleteDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#deleteDeployedDevicesDeployment) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Deployments/{Sid} |  |
| [**fetchDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#fetchDeployedDevicesDeployment) | **GET** /DeployedDevices/Fleets/{FleetSid}/Deployments/{Sid} |  |
| [**listDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#listDeployedDevicesDeployment) | **GET** /DeployedDevices/Fleets/{FleetSid}/Deployments |  |
| [**updateDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#updateDeployedDevicesDeployment) | **POST** /DeployedDevices/Fleets/{FleetSid}/Deployments/{Sid} |  |


<a id="createDeployedDevicesDeployment"></a>
# **createDeployedDevicesDeployment**
> PreviewDeployedDevicesFleetDeployment createDeployedDevicesDeployment(fleetSid, friendlyName, syncServiceSid)



Create a new Deployment in the Fleet, optionally giving it a friendly name and linking to a specific Twilio Sync service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeploymentApi apiInstance = new PreviewDeployedDevicesDeploymentApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Deployment, up to 256 characters long.
    String syncServiceSid = "syncServiceSid_example"; // String | Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.
    try {
      PreviewDeployedDevicesFleetDeployment result = apiInstance.createDeployedDevicesDeployment(fleetSid, friendlyName, syncServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeploymentApi#createDeployedDevicesDeployment");
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
| **friendlyName** | **String**| Provides a human readable descriptive text for this Deployment, up to 256 characters long. | [optional] |
| **syncServiceSid** | **String**| Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetDeployment**](PreviewDeployedDevicesFleetDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteDeployedDevicesDeployment"></a>
# **deleteDeployedDevicesDeployment**
> deleteDeployedDevicesDeployment(fleetSid, sid)



Delete a specific Deployment from the Fleet, leaving associated devices effectively undeployed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeploymentApi apiInstance = new PreviewDeployedDevicesDeploymentApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Deployment resource.
    try {
      apiInstance.deleteDeployedDevicesDeployment(fleetSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeploymentApi#deleteDeployedDevicesDeployment");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Deployment resource. | |

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

<a id="fetchDeployedDevicesDeployment"></a>
# **fetchDeployedDevicesDeployment**
> PreviewDeployedDevicesFleetDeployment fetchDeployedDevicesDeployment(fleetSid, sid)



Fetch information about a specific Deployment in the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeploymentApi apiInstance = new PreviewDeployedDevicesDeploymentApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Deployment resource.
    try {
      PreviewDeployedDevicesFleetDeployment result = apiInstance.fetchDeployedDevicesDeployment(fleetSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeploymentApi#fetchDeployedDevicesDeployment");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Deployment resource. | |

### Return type

[**PreviewDeployedDevicesFleetDeployment**](PreviewDeployedDevicesFleetDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeployedDevicesDeployment"></a>
# **listDeployedDevicesDeployment**
> ListDeployedDevicesDeploymentResponse listDeployedDevicesDeployment(fleetSid, pageSize, page, pageToken)



Retrieve a list of all Deployments belonging to the Fleet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeploymentApi apiInstance = new PreviewDeployedDevicesDeploymentApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeployedDevicesDeploymentResponse result = apiInstance.listDeployedDevicesDeployment(fleetSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeploymentApi#listDeployedDevicesDeployment");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeployedDevicesDeploymentResponse**](ListDeployedDevicesDeploymentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDeployedDevicesDeployment"></a>
# **updateDeployedDevicesDeployment**
> PreviewDeployedDevicesFleetDeployment updateDeployedDevicesDeployment(fleetSid, sid, friendlyName, syncServiceSid)



Update the given properties of a specific Deployment credential in the Fleet, giving it a friendly name or linking to a specific Twilio Sync service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesDeploymentApi apiInstance = new PreviewDeployedDevicesDeploymentApi(defaultClient);
    String fleetSid = "fleetSid_example"; // String | 
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Deployment resource.
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Deployment, up to 64 characters long
    String syncServiceSid = "syncServiceSid_example"; // String | Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.
    try {
      PreviewDeployedDevicesFleetDeployment result = apiInstance.updateDeployedDevicesDeployment(fleetSid, sid, friendlyName, syncServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesDeploymentApi#updateDeployedDevicesDeployment");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Deployment resource. | |
| **friendlyName** | **String**| Provides a human readable descriptive text for this Deployment, up to 64 characters long | [optional] |
| **syncServiceSid** | **String**| Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment. | [optional] |

### Return type

[**PreviewDeployedDevicesFleetDeployment**](PreviewDeployedDevicesFleetDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

