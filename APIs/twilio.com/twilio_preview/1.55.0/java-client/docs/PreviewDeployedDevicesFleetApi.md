# PreviewDeployedDevicesFleetApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#createDeployedDevicesFleet) | **POST** /DeployedDevices/Fleets |  |
| [**deleteDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#deleteDeployedDevicesFleet) | **DELETE** /DeployedDevices/Fleets/{Sid} |  |
| [**fetchDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#fetchDeployedDevicesFleet) | **GET** /DeployedDevices/Fleets/{Sid} |  |
| [**listDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#listDeployedDevicesFleet) | **GET** /DeployedDevices/Fleets |  |
| [**updateDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#updateDeployedDevicesFleet) | **POST** /DeployedDevices/Fleets/{Sid} |  |


<a id="createDeployedDevicesFleet"></a>
# **createDeployedDevicesFleet**
> PreviewDeployedDevicesFleet createDeployedDevicesFleet(friendlyName)



Create a new Fleet for scoping of deployed devices within your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesFleetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesFleetApi apiInstance = new PreviewDeployedDevicesFleetApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Fleet, up to 256 characters long.
    try {
      PreviewDeployedDevicesFleet result = apiInstance.createDeployedDevicesFleet(friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesFleetApi#createDeployedDevicesFleet");
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
| **friendlyName** | **String**| Provides a human readable descriptive text for this Fleet, up to 256 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleet**](PreviewDeployedDevicesFleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteDeployedDevicesFleet"></a>
# **deleteDeployedDevicesFleet**
> deleteDeployedDevicesFleet(sid)



Delete a specific Fleet from your account, also destroys all nested resources: Devices, Deployments, Certificates, Keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesFleetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesFleetApi apiInstance = new PreviewDeployedDevicesFleetApi(defaultClient);
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Fleet resource.
    try {
      apiInstance.deleteDeployedDevicesFleet(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesFleetApi#deleteDeployedDevicesFleet");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Fleet resource. | |

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

<a id="fetchDeployedDevicesFleet"></a>
# **fetchDeployedDevicesFleet**
> PreviewDeployedDevicesFleet fetchDeployedDevicesFleet(sid)



Fetch information about a specific Fleet in your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesFleetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesFleetApi apiInstance = new PreviewDeployedDevicesFleetApi(defaultClient);
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Fleet resource.
    try {
      PreviewDeployedDevicesFleet result = apiInstance.fetchDeployedDevicesFleet(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesFleetApi#fetchDeployedDevicesFleet");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Fleet resource. | |

### Return type

[**PreviewDeployedDevicesFleet**](PreviewDeployedDevicesFleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeployedDevicesFleet"></a>
# **listDeployedDevicesFleet**
> ListDeployedDevicesFleetResponse listDeployedDevicesFleet(pageSize, page, pageToken)



Retrieve a list of all Fleets belonging to your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesFleetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesFleetApi apiInstance = new PreviewDeployedDevicesFleetApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeployedDevicesFleetResponse result = apiInstance.listDeployedDevicesFleet(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesFleetApi#listDeployedDevicesFleet");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeployedDevicesFleetResponse**](ListDeployedDevicesFleetResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDeployedDevicesFleet"></a>
# **updateDeployedDevicesFleet**
> PreviewDeployedDevicesFleet updateDeployedDevicesFleet(sid, defaultDeploymentSid, friendlyName)



Update the friendly name property of a specific Fleet in your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewDeployedDevicesFleetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewDeployedDevicesFleetApi apiInstance = new PreviewDeployedDevicesFleetApi(defaultClient);
    String sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Fleet resource.
    String defaultDeploymentSid = "defaultDeploymentSid_example"; // String | Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.
    String friendlyName = "friendlyName_example"; // String | Provides a human readable descriptive text for this Fleet, up to 256 characters long.
    try {
      PreviewDeployedDevicesFleet result = apiInstance.updateDeployedDevicesFleet(sid, defaultDeploymentSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewDeployedDevicesFleetApi#updateDeployedDevicesFleet");
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
| **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Fleet resource. | |
| **defaultDeploymentSid** | **String**| Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet. | [optional] |
| **friendlyName** | **String**| Provides a human readable descriptive text for this Fleet, up to 256 characters long. | [optional] |

### Return type

[**PreviewDeployedDevicesFleet**](PreviewDeployedDevicesFleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

