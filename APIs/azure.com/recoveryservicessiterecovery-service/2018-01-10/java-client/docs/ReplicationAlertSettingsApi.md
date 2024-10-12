# ReplicationAlertSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationAlertSettingsCreate**](ReplicationAlertSettingsApi.md#replicationAlertSettingsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationAlertSettings/{alertSettingName} | Configures email notifications for this vault. |
| [**replicationAlertSettingsGet**](ReplicationAlertSettingsApi.md#replicationAlertSettingsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationAlertSettings/{alertSettingName} | Gets an email notification(alert) configuration. |
| [**replicationAlertSettingsList**](ReplicationAlertSettingsApi.md#replicationAlertSettingsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationAlertSettings | Gets the list of configured email notification(alert) configurations. |


<a id="replicationAlertSettingsCreate"></a>
# **replicationAlertSettingsCreate**
> Alert replicationAlertSettingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, alertSettingName, request)

Configures email notifications for this vault.

Create or update an email notification(alert) configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationAlertSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationAlertSettingsApi apiInstance = new ReplicationAlertSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String alertSettingName = "alertSettingName_example"; // String | The name of the email notification(alert) configuration.
    ConfigureAlertRequest request = new ConfigureAlertRequest(); // ConfigureAlertRequest | The input to configure the email notification(alert).
    try {
      Alert result = apiInstance.replicationAlertSettingsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, alertSettingName, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationAlertSettingsApi#replicationAlertSettingsCreate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **alertSettingName** | **String**| The name of the email notification(alert) configuration. | |
| **request** | [**ConfigureAlertRequest**](ConfigureAlertRequest.md)| The input to configure the email notification(alert). | |

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationAlertSettingsGet"></a>
# **replicationAlertSettingsGet**
> Alert replicationAlertSettingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, alertSettingName)

Gets an email notification(alert) configuration.

Gets the details of the specified email notification(alert) configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationAlertSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationAlertSettingsApi apiInstance = new ReplicationAlertSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String alertSettingName = "alertSettingName_example"; // String | The name of the email notification configuration.
    try {
      Alert result = apiInstance.replicationAlertSettingsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, alertSettingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationAlertSettingsApi#replicationAlertSettingsGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **alertSettingName** | **String**| The name of the email notification configuration. | |

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationAlertSettingsList"></a>
# **replicationAlertSettingsList**
> AlertCollection replicationAlertSettingsList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of configured email notification(alert) configurations.

Gets the list of email notification(alert) configurations for the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationAlertSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationAlertSettingsApi apiInstance = new ReplicationAlertSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      AlertCollection result = apiInstance.replicationAlertSettingsList(apiVersion, resourceName, resourceGroupName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationAlertSettingsApi#replicationAlertSettingsList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |

### Return type

[**AlertCollection**](AlertCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

