# AutoProvisioningSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoProvisioningSettingsCreate**](AutoProvisioningSettingsApi.md#autoProvisioningSettingsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/autoProvisioningSettings/{settingName} |  |
| [**autoProvisioningSettingsGet**](AutoProvisioningSettingsApi.md#autoProvisioningSettingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/autoProvisioningSettings/{settingName} |  |
| [**autoProvisioningSettingsList**](AutoProvisioningSettingsApi.md#autoProvisioningSettingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/autoProvisioningSettings |  |


<a id="autoProvisioningSettingsCreate"></a>
# **autoProvisioningSettingsCreate**
> AutoProvisioningSetting autoProvisioningSettingsCreate(apiVersion, subscriptionId, settingName, setting)



Details of a specific setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoProvisioningSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoProvisioningSettingsApi apiInstance = new AutoProvisioningSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String settingName = "settingName_example"; // String | Auto provisioning setting key
    AutoProvisioningSetting setting = new AutoProvisioningSetting(); // AutoProvisioningSetting | Auto provisioning setting key
    try {
      AutoProvisioningSetting result = apiInstance.autoProvisioningSettingsCreate(apiVersion, subscriptionId, settingName, setting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoProvisioningSettingsApi#autoProvisioningSettingsCreate");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **settingName** | **String**| Auto provisioning setting key | |
| **setting** | [**AutoProvisioningSetting**](AutoProvisioningSetting.md)| Auto provisioning setting key | |

### Return type

[**AutoProvisioningSetting**](AutoProvisioningSetting.md)

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

<a id="autoProvisioningSettingsGet"></a>
# **autoProvisioningSettingsGet**
> AutoProvisioningSetting autoProvisioningSettingsGet(apiVersion, subscriptionId, settingName)



Details of a specific setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoProvisioningSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoProvisioningSettingsApi apiInstance = new AutoProvisioningSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String settingName = "settingName_example"; // String | Auto provisioning setting key
    try {
      AutoProvisioningSetting result = apiInstance.autoProvisioningSettingsGet(apiVersion, subscriptionId, settingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoProvisioningSettingsApi#autoProvisioningSettingsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **settingName** | **String**| Auto provisioning setting key | |

### Return type

[**AutoProvisioningSetting**](AutoProvisioningSetting.md)

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

<a id="autoProvisioningSettingsList"></a>
# **autoProvisioningSettingsList**
> AutoProvisioningSettingList autoProvisioningSettingsList(apiVersion, subscriptionId)



Exposes the auto provisioning settings of the subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoProvisioningSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoProvisioningSettingsApi apiInstance = new AutoProvisioningSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      AutoProvisioningSettingList result = apiInstance.autoProvisioningSettingsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoProvisioningSettingsApi#autoProvisioningSettingsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**AutoProvisioningSettingList**](AutoProvisioningSettingList.md)

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

