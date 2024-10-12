# SynchronizationSettingApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**synchronizationSettingsCreate**](SynchronizationSettingApi.md#synchronizationSettingsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName} | Adds a new synchronization setting to an existing share or updates it if existing. |
| [**synchronizationSettingsDelete**](SynchronizationSettingApi.md#synchronizationSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName} | Delete synchronizationSetting in a share. |
| [**synchronizationSettingsGet**](SynchronizationSettingApi.md#synchronizationSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName} | Get synchronizationSetting in a share. |
| [**synchronizationSettingsListByShare**](SynchronizationSettingApi.md#synchronizationSettingsListByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings | List synchronizationSettings in a share. |


<a id="synchronizationSettingsCreate"></a>
# **synchronizationSettingsCreate**
> SynchronizationSetting synchronizationSettingsCreate(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion, synchronizationSetting)

Adds a new synchronization setting to an existing share or updates it if existing.

Create or update a synchronizationSetting 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SynchronizationSettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SynchronizationSettingApi apiInstance = new SynchronizationSettingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share to add the synchronization setting to.
    String synchronizationSettingName = "synchronizationSettingName_example"; // String | The name of the synchronizationSetting.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    SynchronizationSetting synchronizationSetting = new SynchronizationSetting(); // SynchronizationSetting | The new synchronization setting information.
    try {
      SynchronizationSetting result = apiInstance.synchronizationSettingsCreate(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion, synchronizationSetting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SynchronizationSettingApi#synchronizationSettingsCreate");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share to add the synchronization setting to. | |
| **synchronizationSettingName** | **String**| The name of the synchronizationSetting. | |
| **apiVersion** | **String**| The api version to use. | |
| **synchronizationSetting** | [**SynchronizationSetting**](SynchronizationSetting.md)| The new synchronization setting information. | |

### Return type

[**SynchronizationSetting**](SynchronizationSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="synchronizationSettingsDelete"></a>
# **synchronizationSettingsDelete**
> OperationResponse synchronizationSettingsDelete(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion)

Delete synchronizationSetting in a share.

Delete a synchronizationSetting in a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SynchronizationSettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SynchronizationSettingApi apiInstance = new SynchronizationSettingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String synchronizationSettingName = "synchronizationSettingName_example"; // String | The name of the synchronizationSetting .
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      OperationResponse result = apiInstance.synchronizationSettingsDelete(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SynchronizationSettingApi#synchronizationSettingsDelete");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **synchronizationSettingName** | **String**| The name of the synchronizationSetting . | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Accepted |  -  |
| **204** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="synchronizationSettingsGet"></a>
# **synchronizationSettingsGet**
> SynchronizationSetting synchronizationSettingsGet(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion)

Get synchronizationSetting in a share.

Get a synchronizationSetting in a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SynchronizationSettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SynchronizationSettingApi apiInstance = new SynchronizationSettingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String synchronizationSettingName = "synchronizationSettingName_example"; // String | The name of the synchronizationSetting.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      SynchronizationSetting result = apiInstance.synchronizationSettingsGet(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SynchronizationSettingApi#synchronizationSettingsGet");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **synchronizationSettingName** | **String**| The name of the synchronizationSetting. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**SynchronizationSetting**](SynchronizationSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="synchronizationSettingsListByShare"></a>
# **synchronizationSettingsListByShare**
> SynchronizationSettingList synchronizationSettingsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken)

List synchronizationSettings in a share.

List synchronizationSettings in a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SynchronizationSettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SynchronizationSettingApi apiInstance = new SynchronizationSettingApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | continuation token
    try {
      SynchronizationSettingList result = apiInstance.synchronizationSettingsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SynchronizationSettingApi#synchronizationSettingsListByShare");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| continuation token | [optional] |

### Return type

[**SynchronizationSettingList**](SynchronizationSettingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

