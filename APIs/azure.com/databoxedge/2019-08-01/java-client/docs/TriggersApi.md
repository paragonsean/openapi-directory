# TriggersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**triggersCreateOrUpdate**](TriggersApi.md#triggersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/triggers/{name} |  |
| [**triggersDelete**](TriggersApi.md#triggersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/triggers/{name} |  |
| [**triggersGet**](TriggersApi.md#triggersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/triggers/{name} |  |
| [**triggersListByDataBoxEdgeDevice**](TriggersApi.md#triggersListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/triggers |  |


<a id="triggersCreateOrUpdate"></a>
# **triggersCreateOrUpdate**
> Trigger triggersCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, trigger)



Creates or updates a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | Creates or updates a trigger
    String name = "name_example"; // String | The trigger name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Trigger trigger = new Trigger(); // Trigger | The trigger.
    try {
      Trigger result = apiInstance.triggersCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, trigger);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersCreateOrUpdate");
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
| **deviceName** | **String**| Creates or updates a trigger | |
| **name** | **String**| The trigger name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **trigger** | [**Trigger**](Trigger.md)| The trigger. | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the trigger. |  -  |
| **202** | Accepted the request to create or update the trigger. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="triggersDelete"></a>
# **triggersDelete**
> triggersDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Deletes the trigger on the gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The trigger name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.triggersDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersDelete");
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
| **deviceName** | **String**| The device name. | |
| **name** | **String**| The trigger name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the trigger. |  -  |
| **202** | Accepted the request to delete the trigger. |  -  |
| **204** | The trigger is already deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="triggersGet"></a>
# **triggersGet**
> Trigger triggersGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Get a specific trigger by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The trigger name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      Trigger result = apiInstance.triggersGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersGet");
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
| **deviceName** | **String**| The device name. | |
| **name** | **String**| The trigger name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**Trigger**](Trigger.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The trigger. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="triggersListByDataBoxEdgeDevice"></a>
# **triggersListByDataBoxEdgeDevice**
> TriggerList triggersListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion, $filter)



Lists all the triggers configured in the device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    String $filter = "$filter_example"; // String | Specify $filter='CustomContextTag eq <tag>' to filter on custom context tag property
    try {
      TriggerList result = apiInstance.triggersListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersListByDataBoxEdgeDevice");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **$filter** | **String**| Specify $filter&#x3D;&#39;CustomContextTag eq &lt;tag&gt;&#39; to filter on custom context tag property | [optional] |

### Return type

[**TriggerList**](TriggerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List all the triggers configured in the device |  -  |
| **0** | Error response describing why the operation failed. |  -  |

