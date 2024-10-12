# SettingsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllSettings**](SettingsApi.md#getAllSettings) | **GET** /settings | List all settings |
| [**getAllowedNetworks**](SettingsApi.md#getAllowedNetworks) | **GET** /settings/allowed_networks/{nodeId} | Get allowed networks for a policy server |
| [**getSetting**](SettingsApi.md#getSetting) | **GET** /settings/{settingId} | Get the value of a setting |
| [**modifyAllowedNetworks**](SettingsApi.md#modifyAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId}/diff | Modify allowed networks for a policy server |
| [**modifySetting**](SettingsApi.md#modifySetting) | **POST** /settings/{settingId} | Set the value of a setting |
| [**setAllowedNetworks**](SettingsApi.md#setAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId} | Set allowed networks for a policy server |


<a id="getAllSettings"></a>
# **getAllSettings**
> GetAllSettings200Response getAllSettings()

List all settings

Get the current value of all the settings

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    try {
      GetAllSettings200Response result = apiInstance.getAllSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getAllSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAllSettings200Response**](GetAllSettings200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |

<a id="getAllowedNetworks"></a>
# **getAllowedNetworks**
> GetAllowedNetworks200Response getAllowedNetworks(nodeId)

Get allowed networks for a policy server

Get the list of allowed networks for a policy server

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Policy server ID for which you want to manage allowed networks.
    try {
      GetAllowedNetworks200Response result = apiInstance.getAllowedNetworks(nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getAllowedNetworks");
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
| **nodeId** | **String**| Policy server ID for which you want to manage allowed networks. | |

### Return type

[**GetAllowedNetworks200Response**](GetAllowedNetworks200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Allowed Networks |  -  |

<a id="getSetting"></a>
# **getSetting**
> GetSetting200Response getSetting(settingId)

Get the value of a setting

Get the current value of a specific setting

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String settingId = "global_policy_mode"; // String | Id of the setting to set
    try {
      GetSetting200Response result = apiInstance.getSetting(settingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#getSetting");
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
| **settingId** | **String**| Id of the setting to set | |

### Return type

[**GetSetting200Response**](GetSetting200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |

<a id="modifyAllowedNetworks"></a>
# **modifyAllowedNetworks**
> ModifyAllowedNetworks200Response modifyAllowedNetworks(nodeId, modifyAllowedNetworksRequest)

Modify allowed networks for a policy server

Add or delete allowed networks for a policy server

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Policy server ID for which you want to manage allowed networks.
    ModifyAllowedNetworksRequest modifyAllowedNetworksRequest = new ModifyAllowedNetworksRequest(); // ModifyAllowedNetworksRequest | 
    try {
      ModifyAllowedNetworks200Response result = apiInstance.modifyAllowedNetworks(nodeId, modifyAllowedNetworksRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#modifyAllowedNetworks");
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
| **nodeId** | **String**| Policy server ID for which you want to manage allowed networks. | |
| **modifyAllowedNetworksRequest** | [**ModifyAllowedNetworksRequest**](ModifyAllowedNetworksRequest.md)|  | |

### Return type

[**ModifyAllowedNetworks200Response**](ModifyAllowedNetworks200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Allowed Networks |  -  |

<a id="modifySetting"></a>
# **modifySetting**
> ModifySetting200Response modifySetting(settingId, modifySettingRequest)

Set the value of a setting

Set the current value of a specific setting

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String settingId = "global_policy_mode"; // String | Id of the setting to set
    ModifySettingRequest modifySettingRequest = new ModifySettingRequest(); // ModifySettingRequest | 
    try {
      ModifySetting200Response result = apiInstance.modifySetting(settingId, modifySettingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#modifySetting");
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
| **settingId** | **String**| Id of the setting to set | |
| **modifySettingRequest** | [**ModifySettingRequest**](ModifySettingRequest.md)|  | |

### Return type

[**ModifySetting200Response**](ModifySetting200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |

<a id="setAllowedNetworks"></a>
# **setAllowedNetworks**
> SetAllowedNetworks200Response setAllowedNetworks(nodeId, setAllowedNetworksRequest)

Set allowed networks for a policy server

Set the list of allowed networks for a policy server

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SettingsApi apiInstance = new SettingsApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Policy server ID for which you want to manage allowed networks.
    SetAllowedNetworksRequest setAllowedNetworksRequest = new SetAllowedNetworksRequest(); // SetAllowedNetworksRequest | 
    try {
      SetAllowedNetworks200Response result = apiInstance.setAllowedNetworks(nodeId, setAllowedNetworksRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsApi#setAllowedNetworks");
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
| **nodeId** | **String**| Policy server ID for which you want to manage allowed networks. | |
| **setAllowedNetworksRequest** | [**SetAllowedNetworksRequest**](SetAllowedNetworksRequest.md)|  | |

### Return type

[**SetAllowedNetworks200Response**](SetAllowedNetworks200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Allowed Networks |  -  |

