# BandwidthSchedulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bandwidthSchedulesCreateOrUpdate**](BandwidthSchedulesApi.md#bandwidthSchedulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules/{name} |  |
| [**bandwidthSchedulesDelete**](BandwidthSchedulesApi.md#bandwidthSchedulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules/{name} |  |
| [**bandwidthSchedulesGet**](BandwidthSchedulesApi.md#bandwidthSchedulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules/{name} |  |
| [**bandwidthSchedulesListByDataBoxEdgeDevice**](BandwidthSchedulesApi.md#bandwidthSchedulesListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/bandwidthSchedules |  |


<a id="bandwidthSchedulesCreateOrUpdate"></a>
# **bandwidthSchedulesCreateOrUpdate**
> BandwidthSchedule bandwidthSchedulesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, parameters)



Creates or updates a bandwidth schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BandwidthSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BandwidthSchedulesApi apiInstance = new BandwidthSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The bandwidth schedule name which needs to be added/updated.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    BandwidthSchedule parameters = new BandwidthSchedule(); // BandwidthSchedule | The bandwidth schedule to be added or updated.
    try {
      BandwidthSchedule result = apiInstance.bandwidthSchedulesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BandwidthSchedulesApi#bandwidthSchedulesCreateOrUpdate");
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
| **name** | **String**| The bandwidth schedule name which needs to be added/updated. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **parameters** | [**BandwidthSchedule**](BandwidthSchedule.md)| The bandwidth schedule to be added or updated. | |

### Return type

[**BandwidthSchedule**](BandwidthSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the bandwidth schedule. |  -  |
| **202** | Accepted the request to create or update the bandwidth schedule. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="bandwidthSchedulesDelete"></a>
# **bandwidthSchedulesDelete**
> bandwidthSchedulesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Deletes the specified bandwidth schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BandwidthSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BandwidthSchedulesApi apiInstance = new BandwidthSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The bandwidth schedule name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.bandwidthSchedulesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling BandwidthSchedulesApi#bandwidthSchedulesDelete");
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
| **name** | **String**| The bandwidth schedule name. | |
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
| **200** | Successfully deleted the bandwidth schedule. |  -  |
| **202** | Accepted the request to delete the bandwidth schedule. |  -  |
| **204** | Successfully deleted the bandwidth schedule. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="bandwidthSchedulesGet"></a>
# **bandwidthSchedulesGet**
> BandwidthSchedule bandwidthSchedulesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Gets the properties of the specified bandwidth schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BandwidthSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BandwidthSchedulesApi apiInstance = new BandwidthSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The bandwidth schedule name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      BandwidthSchedule result = apiInstance.bandwidthSchedulesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BandwidthSchedulesApi#bandwidthSchedulesGet");
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
| **name** | **String**| The bandwidth schedule name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**BandwidthSchedule**](BandwidthSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The bandwidth schedule. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="bandwidthSchedulesListByDataBoxEdgeDevice"></a>
# **bandwidthSchedulesListByDataBoxEdgeDevice**
> BandwidthSchedulesList bandwidthSchedulesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets all the bandwidth schedules for a Data Box Edge/Data Box Gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BandwidthSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BandwidthSchedulesApi apiInstance = new BandwidthSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      BandwidthSchedulesList result = apiInstance.bandwidthSchedulesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BandwidthSchedulesApi#bandwidthSchedulesListByDataBoxEdgeDevice");
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

### Return type

[**BandwidthSchedulesList**](BandwidthSchedulesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of bandwidth schedules. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

