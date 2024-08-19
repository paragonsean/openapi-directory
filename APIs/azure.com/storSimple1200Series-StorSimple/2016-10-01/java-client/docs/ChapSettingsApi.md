# ChapSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chapSettingsCreateOrUpdate**](ChapSettingsApi.md#chapSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/chapSettings/{chapUserName} |  |
| [**chapSettingsDelete**](ChapSettingsApi.md#chapSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/chapSettings/{chapUserName} |  |
| [**chapSettingsGet**](ChapSettingsApi.md#chapSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/chapSettings/{chapUserName} |  |
| [**chapSettingsListByDevice**](ChapSettingsApi.md#chapSettingsListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/chapSettings |  |


<a id="chapSettingsCreateOrUpdate"></a>
# **chapSettingsCreateOrUpdate**
> ChapSettings chapSettingsCreateOrUpdate(deviceName, chapUserName, subscriptionId, resourceGroupName, managerName, apiVersion, chapSetting)



Creates or updates the chap setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChapSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChapSettingsApi apiInstance = new ChapSettingsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String chapUserName = "chapUserName_example"; // String | The chap user name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    ChapSettings chapSetting = new ChapSettings(); // ChapSettings | The chap setting to be added or updated.
    try {
      ChapSettings result = apiInstance.chapSettingsCreateOrUpdate(deviceName, chapUserName, subscriptionId, resourceGroupName, managerName, apiVersion, chapSetting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChapSettingsApi#chapSettingsCreateOrUpdate");
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
| **chapUserName** | **String**| The chap user name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **chapSetting** | [**ChapSettings**](ChapSettings.md)| The chap setting to be added or updated. | |

### Return type

[**ChapSettings**](ChapSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the chap setting. |  -  |
| **202** | Accepted the request to create or update the chap setting. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="chapSettingsDelete"></a>
# **chapSettingsDelete**
> chapSettingsDelete(deviceName, chapUserName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the chap setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChapSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChapSettingsApi apiInstance = new ChapSettingsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String chapUserName = "chapUserName_example"; // String | The chap user name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.chapSettingsDelete(deviceName, chapUserName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChapSettingsApi#chapSettingsDelete");
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
| **chapUserName** | **String**| The chap user name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

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
| **202** | Accepted the request to delete the chap setting. |  -  |
| **204** | Successfully deleted the chap setting. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="chapSettingsGet"></a>
# **chapSettingsGet**
> ChapSettings chapSettingsGet(deviceName, chapUserName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified chap setting name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChapSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChapSettingsApi apiInstance = new ChapSettingsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name.
    String chapUserName = "chapUserName_example"; // String | The user name of chap to be fetched.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      ChapSettings result = apiInstance.chapSettingsGet(deviceName, chapUserName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChapSettingsApi#chapSettingsGet");
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
| **chapUserName** | **String**| The user name of chap to be fetched. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**ChapSettings**](ChapSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The chap setting. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="chapSettingsListByDevice"></a>
# **chapSettingsListByDevice**
> ChapSettingsList chapSettingsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the chap settings in a device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChapSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChapSettingsApi apiInstance = new ChapSettingsApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The name of the device.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      ChapSettingsList result = apiInstance.chapSettingsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChapSettingsApi#chapSettingsListByDevice");
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
| **deviceName** | **String**| The name of the device. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**ChapSettingsList**](ChapSettingsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of chap settings. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

