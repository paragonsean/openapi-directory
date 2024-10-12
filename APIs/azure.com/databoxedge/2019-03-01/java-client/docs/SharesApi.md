# SharesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharesCreateOrUpdate**](SharesApi.md#sharesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name} | Creates a new share or updates an existing share on the device. |
| [**sharesDelete**](SharesApi.md#sharesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name} |  |
| [**sharesGet**](SharesApi.md#sharesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name} | Gets a share by name. |
| [**sharesListByDataBoxEdgeDevice**](SharesApi.md#sharesListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares | Lists all the shares in a data box edge/gateway device. |
| [**sharesRefresh**](SharesApi.md#sharesRefresh) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}/refresh | Refreshes the share metadata with the data from the cloud. |


<a id="sharesCreateOrUpdate"></a>
# **sharesCreateOrUpdate**
> Share sharesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, share)

Creates a new share or updates an existing share on the device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The share name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Share share = new Share(); // Share | The share properties.
    try {
      Share result = apiInstance.sharesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, share);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesCreateOrUpdate");
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
| **name** | **String**| The share name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **share** | [**Share**](Share.md)| The share properties. | |

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the share. |  -  |
| **202** | Accepted the request to create or update the share. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sharesDelete"></a>
# **sharesDelete**
> sharesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Deletes the share on the data box edge/gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The share name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.sharesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesDelete");
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
| **name** | **String**| The share name. | |
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
| **200** | Successfully deleted the share. |  -  |
| **202** | Accepted the request to delete the share. |  -  |
| **204** | The share is already deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sharesGet"></a>
# **sharesGet**
> Share sharesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion)

Gets a share by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The share name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      Share result = apiInstance.sharesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesGet");
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
| **name** | **String**| The share name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The share details. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sharesListByDataBoxEdgeDevice"></a>
# **sharesListByDataBoxEdgeDevice**
> ShareList sharesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)

Lists all the shares in a data box edge/gateway device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      ShareList result = apiInstance.sharesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesListByDataBoxEdgeDevice");
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

[**ShareList**](ShareList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of all the shares on the device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sharesRefresh"></a>
# **sharesRefresh**
> sharesRefresh(deviceName, name, subscriptionId, resourceGroupName, apiVersion)

Refreshes the share metadata with the data from the cloud.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The share name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.sharesRefresh(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sharesRefresh");
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
| **name** | **String**| The share name. | |
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
| **200** | Successfully refreshed the share on the device. |  -  |
| **202** | Accepted the request to refresh the share on the device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

