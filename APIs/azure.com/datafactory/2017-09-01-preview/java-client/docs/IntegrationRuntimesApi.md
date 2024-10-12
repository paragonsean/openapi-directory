# IntegrationRuntimesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationRuntimesCreateOrUpdate**](IntegrationRuntimesApi.md#integrationRuntimesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} |  |
| [**integrationRuntimesDelete**](IntegrationRuntimesApi.md#integrationRuntimesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} |  |
| [**integrationRuntimesGet**](IntegrationRuntimesApi.md#integrationRuntimesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} |  |
| [**integrationRuntimesGetConnectionInfo**](IntegrationRuntimesApi.md#integrationRuntimesGetConnectionInfo) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getConnectionInfo |  |
| [**integrationRuntimesGetMonitoringData**](IntegrationRuntimesApi.md#integrationRuntimesGetMonitoringData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/monitoringData |  |
| [**integrationRuntimesGetStatus**](IntegrationRuntimesApi.md#integrationRuntimesGetStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getStatus |  |
| [**integrationRuntimesListAuthKeys**](IntegrationRuntimesApi.md#integrationRuntimesListAuthKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/listAuthKeys |  |
| [**integrationRuntimesListByFactory**](IntegrationRuntimesApi.md#integrationRuntimesListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes |  |
| [**integrationRuntimesRegenerateAuthKey**](IntegrationRuntimesApi.md#integrationRuntimesRegenerateAuthKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/regenerateAuthKey |  |
| [**integrationRuntimesRemoveNode**](IntegrationRuntimesApi.md#integrationRuntimesRemoveNode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/removeNode |  |
| [**integrationRuntimesStart**](IntegrationRuntimesApi.md#integrationRuntimesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/start |  |
| [**integrationRuntimesStop**](IntegrationRuntimesApi.md#integrationRuntimesStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/stop |  |
| [**integrationRuntimesSyncCredentials**](IntegrationRuntimesApi.md#integrationRuntimesSyncCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/syncCredentials |  |
| [**integrationRuntimesUpdate**](IntegrationRuntimesApi.md#integrationRuntimesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} |  |
| [**integrationRuntimesUpgrade**](IntegrationRuntimesApi.md#integrationRuntimesUpgrade) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/upgrade |  |


<a id="integrationRuntimesCreateOrUpdate"></a>
# **integrationRuntimesCreateOrUpdate**
> IntegrationRuntimeResource integrationRuntimesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, integrationRuntime, ifMatch)



Creates or updates an integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationRuntimeResource integrationRuntime = new IntegrationRuntimeResource(); // IntegrationRuntimeResource | Integration runtime resource definition.
    String ifMatch = "ifMatch_example"; // String | ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    try {
      IntegrationRuntimeResource result = apiInstance.integrationRuntimesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, integrationRuntime, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |
| **integrationRuntime** | [**IntegrationRuntimeResource**](IntegrationRuntimeResource.md)| Integration runtime resource definition. | |
| **ifMatch** | **String**| ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] |

### Return type

[**IntegrationRuntimeResource**](IntegrationRuntimeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from PUT integration runtime operation. |  -  |

<a id="integrationRuntimesDelete"></a>
# **integrationRuntimesDelete**
> integrationRuntimesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Deletes an integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationRuntimesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesDelete");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
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
| **200** | OK. |  -  |
| **204** | No Content. |  -  |
| **0** | An error response received from DELETE integration runtime operation. |  -  |

<a id="integrationRuntimesGet"></a>
# **integrationRuntimesGet**
> IntegrationRuntimeResource integrationRuntimesGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Gets an integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimeResource result = apiInstance.integrationRuntimesGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesGet");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimeResource**](IntegrationRuntimeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from GET integration runtime operation. |  -  |

<a id="integrationRuntimesGetConnectionInfo"></a>
# **integrationRuntimesGetConnectionInfo**
> IntegrationRuntimesGetConnectionInfo200Response integrationRuntimesGetConnectionInfo(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Gets the on-premises integration runtime connection information for encrypting the on-premises data source credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimesGetConnectionInfo200Response result = apiInstance.integrationRuntimesGetConnectionInfo(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesGetConnectionInfo");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimesGetConnectionInfo200Response**](IntegrationRuntimesGetConnectionInfo200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesGetMonitoringData"></a>
# **integrationRuntimesGetMonitoringData**
> IntegrationRuntimesGetMonitoringData200Response integrationRuntimesGetMonitoringData(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Get the integration runtime monitoring data, which includes the monitor data for all the nodes under this integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimesGetMonitoringData200Response result = apiInstance.integrationRuntimesGetMonitoringData(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesGetMonitoringData");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimesGetMonitoringData200Response**](IntegrationRuntimesGetMonitoringData200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesGetStatus"></a>
# **integrationRuntimesGetStatus**
> IntegrationRuntimeStatusResponse integrationRuntimesGetStatus(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Gets detailed status information for an integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimeStatusResponse result = apiInstance.integrationRuntimesGetStatus(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesGetStatus");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimeStatusResponse**](IntegrationRuntimeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesListAuthKeys"></a>
# **integrationRuntimesListAuthKeys**
> IntegrationRuntimesListAuthKeys200Response integrationRuntimesListAuthKeys(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Retrieves the authentication keys for an integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimesListAuthKeys200Response result = apiInstance.integrationRuntimesListAuthKeys(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesListAuthKeys");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimesListAuthKeys200Response**](IntegrationRuntimesListAuthKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesListByFactory"></a>
# **integrationRuntimesListByFactory**
> IntegrationRuntimeListResponse integrationRuntimesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists integration runtimes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimeListResponse result = apiInstance.integrationRuntimesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesListByFactory");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimeListResponse**](IntegrationRuntimeListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesRegenerateAuthKey"></a>
# **integrationRuntimesRegenerateAuthKey**
> IntegrationRuntimesListAuthKeys200Response integrationRuntimesRegenerateAuthKey(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, regenerateKeyParameters)



Regenerates the authentication key for an integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationRuntimesRegenerateAuthKeyRequest regenerateKeyParameters = new IntegrationRuntimesRegenerateAuthKeyRequest(); // IntegrationRuntimesRegenerateAuthKeyRequest | The parameters for regenerating integration runtime authentication key.
    try {
      IntegrationRuntimesListAuthKeys200Response result = apiInstance.integrationRuntimesRegenerateAuthKey(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, regenerateKeyParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesRegenerateAuthKey");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |
| **regenerateKeyParameters** | [**IntegrationRuntimesRegenerateAuthKeyRequest**](IntegrationRuntimesRegenerateAuthKeyRequest.md)| The parameters for regenerating integration runtime authentication key. | |

### Return type

[**IntegrationRuntimesListAuthKeys200Response**](IntegrationRuntimesListAuthKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesRemoveNode"></a>
# **integrationRuntimesRemoveNode**
> integrationRuntimesRemoveNode(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, removeNodeParameters)



Remove a node from integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationRuntimesRemoveNodeRequest removeNodeParameters = new IntegrationRuntimesRemoveNodeRequest(); // IntegrationRuntimesRemoveNodeRequest | The name of the node to be removed from an integration runtime.
    try {
      apiInstance.integrationRuntimesRemoveNode(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, removeNodeParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesRemoveNode");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |
| **removeNodeParameters** | [**IntegrationRuntimesRemoveNodeRequest**](IntegrationRuntimesRemoveNodeRequest.md)| The name of the node to be removed from an integration runtime. | |

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
| **200** | OK. |  -  |
| **204** | No Content. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesStart"></a>
# **integrationRuntimesStart**
> IntegrationRuntimeStatusResponse integrationRuntimesStart(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Starts a ManagedReserved type integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimeStatusResponse result = apiInstance.integrationRuntimesStart(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesStart");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimeStatusResponse**](IntegrationRuntimeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesStop"></a>
# **integrationRuntimesStop**
> integrationRuntimesStop(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Stops a ManagedReserved type integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationRuntimesStop(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesStop");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
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
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesSyncCredentials"></a>
# **integrationRuntimesSyncCredentials**
> integrationRuntimesSyncCredentials(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Force the integration runtime to synchronize credentials across integration runtime nodes, and this will override the credentials across all worker nodes with those available on the dispatcher node. If you already have the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime node than using this API directly.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationRuntimesSyncCredentials(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesSyncCredentials");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
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
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesUpdate"></a>
# **integrationRuntimesUpdate**
> IntegrationRuntimeStatusResponse integrationRuntimesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, updateIntegrationRuntimeRequest)



Updates an integration runtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    UpdateIntegrationRuntimeRequest updateIntegrationRuntimeRequest = new UpdateIntegrationRuntimeRequest(); // UpdateIntegrationRuntimeRequest | The parameters for updating an integration runtime.
    try {
      IntegrationRuntimeStatusResponse result = apiInstance.integrationRuntimesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, updateIntegrationRuntimeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **apiVersion** | **String**| The API version. | |
| **updateIntegrationRuntimeRequest** | [**UpdateIntegrationRuntimeRequest**](UpdateIntegrationRuntimeRequest.md)| The parameters for updating an integration runtime. | |

### Return type

[**IntegrationRuntimeStatusResponse**](IntegrationRuntimeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimesUpgrade"></a>
# **integrationRuntimesUpgrade**
> integrationRuntimesUpgrade(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Upgrade self-hosted integration runtime to latest version if availability.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimesApi apiInstance = new IntegrationRuntimesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationRuntimesUpgrade(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimesApi#integrationRuntimesUpgrade");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
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
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

