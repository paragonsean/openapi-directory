# ConfigurationStoresApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurationStoresCreate**](ConfigurationStoresApi.md#configurationStoresCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} |  |
| [**configurationStoresDelete**](ConfigurationStoresApi.md#configurationStoresDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} |  |
| [**configurationStoresGet**](ConfigurationStoresApi.md#configurationStoresGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} |  |
| [**configurationStoresList**](ConfigurationStoresApi.md#configurationStoresList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/configurationStores |  |
| [**configurationStoresListByResourceGroup**](ConfigurationStoresApi.md#configurationStoresListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores |  |
| [**configurationStoresListKeyValue**](ConfigurationStoresApi.md#configurationStoresListKeyValue) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/listKeyValue |  |
| [**configurationStoresListKeys**](ConfigurationStoresApi.md#configurationStoresListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/ListKeys |  |
| [**configurationStoresRegenerateKey**](ConfigurationStoresApi.md#configurationStoresRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/RegenerateKey |  |
| [**configurationStoresUpdate**](ConfigurationStoresApi.md#configurationStoresUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} |  |


<a id="configurationStoresCreate"></a>
# **configurationStoresCreate**
> ConfigurationStore configurationStoresCreate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreCreationParameters)



Creates a configuration store with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    ConfigurationStore configStoreCreationParameters = new ConfigurationStore(); // ConfigurationStore | The parameters for creating a configuration store.
    try {
      ConfigurationStore result = apiInstance.configurationStoresCreate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreCreationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresCreate");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **configStoreCreationParameters** | [**ConfigurationStore**](ConfigurationStore.md)| The parameters for creating a configuration store. | |

### Return type

[**ConfigurationStore**](ConfigurationStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successfully accepted; the operation will complete asynchronously. The provisioning state of the resource should indicate the current state of the resource. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresDelete"></a>
# **configurationStoresDelete**
> configurationStoresDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Deletes a configuration store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.configurationStoresDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresDelete");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | The request was successful; the operation will complete asynchronously. |  -  |
| **204** | No Content - the specified resource was not found. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresGet"></a>
# **configurationStoresGet**
> ConfigurationStore configurationStoresGet(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Gets the properties of the specified configuration store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      ConfigurationStore result = apiInstance.configurationStoresGet(subscriptionId, resourceGroupName, configStoreName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresGet");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**ConfigurationStore**](ConfigurationStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresList"></a>
# **configurationStoresList**
> ConfigurationStoreListResult configurationStoresList(subscriptionId, apiVersion, $skipToken)



Lists the configuration stores for a given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String $skipToken = "$skipToken_example"; // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    try {
      ConfigurationStoreListResult result = apiInstance.configurationStoresList(subscriptionId, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresList");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **$skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**ConfigurationStoreListResult**](ConfigurationStoreListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresListByResourceGroup"></a>
# **configurationStoresListByResourceGroup**
> ConfigurationStoreListResult configurationStoresListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $skipToken)



Lists the configuration stores for a given resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String $skipToken = "$skipToken_example"; // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    try {
      ConfigurationStoreListResult result = apiInstance.configurationStoresListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresListByResourceGroup");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **apiVersion** | **String**| The client API version. | |
| **$skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**ConfigurationStoreListResult**](ConfigurationStoreListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresListKeyValue"></a>
# **configurationStoresListKeyValue**
> KeyValue configurationStoresListKeyValue(subscriptionId, resourceGroupName, configStoreName, apiVersion, listKeyValueParameters)



Lists a configuration store key-value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    ListKeyValueParameters listKeyValueParameters = new ListKeyValueParameters(); // ListKeyValueParameters | The parameters for retrieving a key-value.
    try {
      KeyValue result = apiInstance.configurationStoresListKeyValue(subscriptionId, resourceGroupName, configStoreName, apiVersion, listKeyValueParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresListKeyValue");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **listKeyValueParameters** | [**ListKeyValueParameters**](ListKeyValueParameters.md)| The parameters for retrieving a key-value. | |

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresListKeys"></a>
# **configurationStoresListKeys**
> ApiKeyListResult configurationStoresListKeys(subscriptionId, resourceGroupName, configStoreName, apiVersion, $skipToken)



Lists the access key for the specified configuration store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String $skipToken = "$skipToken_example"; // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    try {
      ApiKeyListResult result = apiInstance.configurationStoresListKeys(subscriptionId, resourceGroupName, configStoreName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresListKeys");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **$skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] |

### Return type

[**ApiKeyListResult**](ApiKeyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresRegenerateKey"></a>
# **configurationStoresRegenerateKey**
> ApiKey configurationStoresRegenerateKey(subscriptionId, resourceGroupName, configStoreName, apiVersion, regenerateKeyParameters)



Regenerates an access key for the specified configuration store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    RegenerateKeyParameters regenerateKeyParameters = new RegenerateKeyParameters(); // RegenerateKeyParameters | The parameters for regenerating an access key.
    try {
      ApiKey result = apiInstance.configurationStoresRegenerateKey(subscriptionId, resourceGroupName, configStoreName, apiVersion, regenerateKeyParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresRegenerateKey");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **regenerateKeyParameters** | [**RegenerateKeyParameters**](RegenerateKeyParameters.md)| The parameters for regenerating an access key. | |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="configurationStoresUpdate"></a>
# **configurationStoresUpdate**
> ConfigurationStore configurationStoresUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreUpdateParameters)



Updates a configuration store with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationStoresApi apiInstance = new ConfigurationStoresApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    ConfigurationStoreUpdateParameters configStoreUpdateParameters = new ConfigurationStoreUpdateParameters(); // ConfigurationStoreUpdateParameters | The parameters for updating a configuration store.
    try {
      ConfigurationStore result = apiInstance.configurationStoresUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationStoresApi#configurationStoresUpdate");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **configStoreUpdateParameters** | [**ConfigurationStoreUpdateParameters**](ConfigurationStoreUpdateParameters.md)| The parameters for updating a configuration store. | |

### Return type

[**ConfigurationStore**](ConfigurationStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successfully accepted; the operation will complete asynchronously. The provisioning state of the resource should indicate the current state of the resource. |  -  |
| **0** | Error response describing why the operation failed |  -  |

