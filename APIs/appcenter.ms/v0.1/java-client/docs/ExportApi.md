# ExportApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportConfigurationsCreate**](ExportApi.md#exportConfigurationsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations |  |
| [**exportConfigurationsDelete**](ExportApi.md#exportConfigurationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} |  |
| [**exportConfigurationsDisable**](ExportApi.md#exportConfigurationsDisable) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/disable |  |
| [**exportConfigurationsEnable**](ExportApi.md#exportConfigurationsEnable) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/enable |  |
| [**exportConfigurationsGet**](ExportApi.md#exportConfigurationsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} |  |
| [**exportConfigurationsList**](ExportApi.md#exportConfigurationsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/export_configurations |  |
| [**exportConfigurationsPartialUpdate**](ExportApi.md#exportConfigurationsPartialUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} |  |


<a id="exportConfigurationsCreate"></a>
# **exportConfigurationsCreate**
> ExportConfigurationsList200ResponseValuesInner exportConfigurationsCreate(ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration)



Create new export configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ExportConfigurationsList200ResponseValuesInnerExportConfiguration exportConfigurationsList200ResponseValuesInnerExportConfiguration = new ExportConfigurationsList200ResponseValuesInnerExportConfiguration(); // ExportConfigurationsList200ResponseValuesInnerExportConfiguration | Export configurations.
    try {
      ExportConfigurationsList200ResponseValuesInner result = apiInstance.exportConfigurationsCreate(ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportConfigurationsCreate");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **exportConfigurationsList200ResponseValuesInnerExportConfiguration** | [**ExportConfigurationsList200ResponseValuesInnerExportConfiguration**](ExportConfigurationsList200ResponseValuesInnerExportConfiguration.md)| Export configurations. | |

### Return type

[**ExportConfigurationsList200ResponseValuesInner**](ExportConfigurationsList200ResponseValuesInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Create export configuration request successfully received. |  -  |
| **0** | Error code with reason |  -  |

<a id="exportConfigurationsDelete"></a>
# **exportConfigurationsDelete**
> exportConfigurationsDelete(exportConfigurationId, ownerName, appName)



Delete export configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.exportConfigurationsDelete(exportConfigurationId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportConfigurationsDelete");
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
| **exportConfigurationId** | **String**| The id of the export configuration. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export configuration was successfully deleted. |  -  |
| **0** | Error code with reason |  -  |

<a id="exportConfigurationsDisable"></a>
# **exportConfigurationsDisable**
> exportConfigurationsDisable(exportConfigurationId, ownerName, appName)



Disable export configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.exportConfigurationsDisable(exportConfigurationId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportConfigurationsDisable");
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
| **exportConfigurationId** | **String**| The id of the export configuration. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export configuration was successfully disabled. |  -  |
| **0** | Error code with reason |  -  |

<a id="exportConfigurationsEnable"></a>
# **exportConfigurationsEnable**
> exportConfigurationsEnable(exportConfigurationId, ownerName, appName)



Enable export configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.exportConfigurationsEnable(exportConfigurationId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportConfigurationsEnable");
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
| **exportConfigurationId** | **String**| The id of the export configuration. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export configuration was successfully enabled. |  -  |
| **0** | Error code with reason |  -  |

<a id="exportConfigurationsGet"></a>
# **exportConfigurationsGet**
> ExportConfigurationsList200ResponseValuesInner exportConfigurationsGet(exportConfigurationId, ownerName, appName)



Get export configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ExportConfigurationsList200ResponseValuesInner result = apiInstance.exportConfigurationsGet(exportConfigurationId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportConfigurationsGet");
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
| **exportConfigurationId** | **String**| The id of the export configuration. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ExportConfigurationsList200ResponseValuesInner**](ExportConfigurationsList200ResponseValuesInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get export configuration. |  -  |
| **0** | Error code with reason |  -  |

<a id="exportConfigurationsList"></a>
# **exportConfigurationsList**
> ExportConfigurationsList200Response exportConfigurationsList(ownerName, appName)



List export configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ExportConfigurationsList200Response result = apiInstance.exportConfigurationsList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportConfigurationsList");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ExportConfigurationsList200Response**](ExportConfigurationsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List export configurations. |  -  |
| **0** | Error code with reason |  -  |

<a id="exportConfigurationsPartialUpdate"></a>
# **exportConfigurationsPartialUpdate**
> ExportConfigurationsList200ResponseValuesInner exportConfigurationsPartialUpdate(exportConfigurationId, ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration)



Partially update export configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ExportApi apiInstance = new ExportApi(defaultClient);
    String exportConfigurationId = "exportConfigurationId_example"; // String | The id of the export configuration.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ExportConfigurationsList200ResponseValuesInnerExportConfiguration exportConfigurationsList200ResponseValuesInnerExportConfiguration = new ExportConfigurationsList200ResponseValuesInnerExportConfiguration(); // ExportConfigurationsList200ResponseValuesInnerExportConfiguration | Export configurations.
    try {
      ExportConfigurationsList200ResponseValuesInner result = apiInstance.exportConfigurationsPartialUpdate(exportConfigurationId, ownerName, appName, exportConfigurationsList200ResponseValuesInnerExportConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportConfigurationsPartialUpdate");
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
| **exportConfigurationId** | **String**| The id of the export configuration. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **exportConfigurationsList200ResponseValuesInnerExportConfiguration** | [**ExportConfigurationsList200ResponseValuesInnerExportConfiguration**](ExportConfigurationsList200ResponseValuesInnerExportConfiguration.md)| Export configurations. | |

### Return type

[**ExportConfigurationsList200ResponseValuesInner**](ExportConfigurationsList200ResponseValuesInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export configuration updated successfully. |  -  |
| **0** | Error code with reason |  -  |

