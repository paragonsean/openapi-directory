# EnvironmentSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**environmentSettingsClaimAny**](EnvironmentSettingsApi.md#environmentSettingsClaimAny) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/claimAny |  |
| [**environmentSettingsCreateOrUpdate**](EnvironmentSettingsApi.md#environmentSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} |  |
| [**environmentSettingsDelete**](EnvironmentSettingsApi.md#environmentSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} |  |
| [**environmentSettingsGet**](EnvironmentSettingsApi.md#environmentSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} |  |
| [**environmentSettingsList**](EnvironmentSettingsApi.md#environmentSettingsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings |  |
| [**environmentSettingsPublish**](EnvironmentSettingsApi.md#environmentSettingsPublish) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/publish |  |
| [**environmentSettingsStart**](EnvironmentSettingsApi.md#environmentSettingsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/start |  |
| [**environmentSettingsStop**](EnvironmentSettingsApi.md#environmentSettingsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/stop |  |
| [**environmentSettingsUpdate**](EnvironmentSettingsApi.md#environmentSettingsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} |  |


<a id="environmentSettingsClaimAny"></a>
# **environmentSettingsClaimAny**
> environmentSettingsClaimAny(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Claims a random environment for a user in an environment settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentSettingsClaimAny(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsClaimAny");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsCreateOrUpdate"></a>
# **environmentSettingsCreateOrUpdate**
> EnvironmentSetting environmentSettingsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting)



Create or replace an existing Environment Setting. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    EnvironmentSetting environmentSetting = new EnvironmentSetting(); // EnvironmentSetting | Represents settings of an environment, from which environment instances would be created
    try {
      EnvironmentSetting result = apiInstance.environmentSettingsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **environmentSetting** | [**EnvironmentSetting**](EnvironmentSetting.md)| Represents settings of an environment, from which environment instances would be created | |

### Return type

[**EnvironmentSetting**](EnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsDelete"></a>
# **environmentSettingsDelete**
> environmentSettingsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Delete environment setting. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentSettingsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsGet"></a>
# **environmentSettingsGet**
> EnvironmentSetting environmentSettingsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, $expand)



Get environment setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=publishingState)'
    try {
      EnvironmentSetting result = apiInstance.environmentSettingsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;publishingState)&#39; | [optional] |

### Return type

[**EnvironmentSetting**](EnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsList"></a>
# **environmentSettingsList**
> ResponseWithContinuationEnvironmentSetting environmentSettingsList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, $expand, $filter, $top, $orderby)



List environment setting in a given lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=publishingState)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationEnvironmentSetting result = apiInstance.environmentSettingsList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;publishingState)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationEnvironmentSetting**](ResponseWithContinuationEnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsPublish"></a>
# **environmentSettingsPublish**
> environmentSettingsPublish(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, publishPayload)



Provisions/deprovisions required resources for an environment setting based on current state of the lab/environment setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    PublishPayload publishPayload = new PublishPayload(); // PublishPayload | Payload for Publish operation on EnvironmentSetting.
    try {
      apiInstance.environmentSettingsPublish(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, publishPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsPublish");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **publishPayload** | [**PublishPayload**](PublishPayload.md)| Payload for Publish operation on EnvironmentSetting. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsStart"></a>
# **environmentSettingsStart**
> environmentSettingsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Starts a template by starting all resources inside the template. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentSettingsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsStart");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsStop"></a>
# **environmentSettingsStop**
> environmentSettingsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Starts a template by starting all resources inside the template. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.environmentSettingsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsStop");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="environmentSettingsUpdate"></a>
# **environmentSettingsUpdate**
> EnvironmentSetting environmentSettingsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting)



Modify properties of environment setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentSettingsApi apiInstance = new EnvironmentSettingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
    String apiVersion = "2018-10-15"; // String | Client API version.
    EnvironmentSettingFragment environmentSetting = new EnvironmentSettingFragment(); // EnvironmentSettingFragment | Represents settings of an environment, from which environment instances would be created
    try {
      EnvironmentSetting result = apiInstance.environmentSettingsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentSettingsApi#environmentSettingsUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **environmentSettingName** | **String**| The name of the environment Setting. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **environmentSetting** | [**EnvironmentSettingFragment**](EnvironmentSettingFragment.md)| Represents settings of an environment, from which environment instances would be created | |

### Return type

[**EnvironmentSetting**](EnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

