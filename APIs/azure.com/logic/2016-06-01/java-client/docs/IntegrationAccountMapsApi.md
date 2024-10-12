# IntegrationAccountMapsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapsCreateOrUpdate**](IntegrationAccountMapsApi.md#mapsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} |  |
| [**mapsDelete**](IntegrationAccountMapsApi.md#mapsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} |  |
| [**mapsGet**](IntegrationAccountMapsApi.md#mapsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} |  |
| [**mapsListByIntegrationAccounts**](IntegrationAccountMapsApi.md#mapsListByIntegrationAccounts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps |  |
| [**mapsListContentCallbackUrl**](IntegrationAccountMapsApi.md#mapsListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}/listContentCallbackUrl |  |


<a id="mapsCreateOrUpdate"></a>
# **mapsCreateOrUpdate**
> IntegrationAccountMap mapsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, map)



Creates or updates an integration account map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountMapsApi apiInstance = new IntegrationAccountMapsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String mapName = "mapName_example"; // String | The integration account map name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccountMap map = new IntegrationAccountMap(); // IntegrationAccountMap | The integration account map.
    try {
      IntegrationAccountMap result = apiInstance.mapsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, map);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountMapsApi#mapsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **mapName** | **String**| The integration account map name. | |
| **apiVersion** | **String**| The API version. | |
| **map** | [**IntegrationAccountMap**](IntegrationAccountMap.md)| The integration account map. | |

### Return type

[**IntegrationAccountMap**](IntegrationAccountMap.md)

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

<a id="mapsDelete"></a>
# **mapsDelete**
> mapsDelete(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion)



Deletes an integration account map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountMapsApi apiInstance = new IntegrationAccountMapsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String mapName = "mapName_example"; // String | The integration account map name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.mapsDelete(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountMapsApi#mapsDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **mapName** | **String**| The integration account map name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="mapsGet"></a>
# **mapsGet**
> IntegrationAccountMap mapsGet(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion)



Gets an integration account map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountMapsApi apiInstance = new IntegrationAccountMapsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String mapName = "mapName_example"; // String | The integration account map name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccountMap result = apiInstance.mapsGet(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountMapsApi#mapsGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **mapName** | **String**| The integration account map name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationAccountMap**](IntegrationAccountMap.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="mapsListByIntegrationAccounts"></a>
# **mapsListByIntegrationAccounts**
> IntegrationAccountMapListResult mapsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter)



Gets a list of integration account maps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountMapsApi apiInstance = new IntegrationAccountMapsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Options for filters include: MapType.
    try {
      IntegrationAccountMapListResult result = apiInstance.mapsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountMapsApi#mapsListByIntegrationAccounts");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. Options for filters include: MapType. | [optional] |

### Return type

[**IntegrationAccountMapListResult**](IntegrationAccountMapListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="mapsListContentCallbackUrl"></a>
# **mapsListContentCallbackUrl**
> WorkflowTriggerCallbackUrl mapsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, listContentCallbackUrl)



Get the content callback url.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountMapsApi apiInstance = new IntegrationAccountMapsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String mapName = "mapName_example"; // String | The integration account map name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    GetCallbackUrlParameters listContentCallbackUrl = new GetCallbackUrlParameters(); // GetCallbackUrlParameters | 
    try {
      WorkflowTriggerCallbackUrl result = apiInstance.mapsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, listContentCallbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountMapsApi#mapsListContentCallbackUrl");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **mapName** | **String**| The integration account map name. | |
| **apiVersion** | **String**| The API version. | |
| **listContentCallbackUrl** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)|  | |

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

