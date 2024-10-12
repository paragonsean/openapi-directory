# SettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**settingsGet**](SettingsApi.md#settingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/settings/{settingName} |  |
| [**settingsList**](SettingsApi.md#settingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/settings |  |
| [**settingsUpdate**](SettingsApi.md#settingsUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/settings/{settingName} |  |


<a id="settingsGet"></a>
# **settingsGet**
> Setting settingsGet(apiVersion, subscriptionId, settingName)



Settings of different configurations in security center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String settingName = "MCAS"; // String | Name of setting: (MCAS/WDATP)
    try {
      Setting result = apiInstance.settingsGet(apiVersion, subscriptionId, settingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#settingsGet");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **settingName** | **String**| Name of setting: (MCAS/WDATP) | [enum: MCAS, WDATP] |

### Return type

[**Setting**](Setting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="settingsList"></a>
# **settingsList**
> SettingsList settingsList(apiVersion, subscriptionId)



Settings about different configurations in security center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      SettingsList result = apiInstance.settingsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#settingsList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**SettingsList**](SettingsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="settingsUpdate"></a>
# **settingsUpdate**
> Setting settingsUpdate(apiVersion, subscriptionId, settingName, setting)



updating settings about different configurations in security center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String settingName = "MCAS"; // String | Name of setting: (MCAS/WDATP)
    Setting setting = new Setting(); // Setting | Setting object
    try {
      Setting result = apiInstance.settingsUpdate(apiVersion, subscriptionId, settingName, setting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#settingsUpdate");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **settingName** | **String**| Name of setting: (MCAS/WDATP) | [enum: MCAS, WDATP] |
| **setting** | [**Setting**](Setting.md)| Setting object | |

### Return type

[**Setting**](Setting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

