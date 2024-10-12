# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaServiceCheckNameAvailability**](DefaultApi.md#mediaServiceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Media/CheckNameAvailability |  |
| [**mediaServiceCreate**](DefaultApi.md#mediaServiceCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} |  |
| [**mediaServiceDelete**](DefaultApi.md#mediaServiceDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} |  |
| [**mediaServiceGet**](DefaultApi.md#mediaServiceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} |  |
| [**mediaServiceListByResourceGroup**](DefaultApi.md#mediaServiceListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices |  |
| [**mediaServiceListKeys**](DefaultApi.md#mediaServiceListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName}/listKeys |  |
| [**mediaServiceRegenerateKey**](DefaultApi.md#mediaServiceRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName}/regenerateKey |  |
| [**mediaServiceSyncStorageKeys**](DefaultApi.md#mediaServiceSyncStorageKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName}/syncStorageKeys |  |
| [**mediaServiceUpdate**](DefaultApi.md#mediaServiceUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} |  |
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Media/operations |  |


<a id="mediaServiceCheckNameAvailability"></a>
# **mediaServiceCheckNameAvailability**
> CheckNameAvailabilityOutput mediaServiceCheckNameAvailability(subscriptionId, apiVersion, parameters)



Checks whether the Media Service resource name is available. The name must be globally unique.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    CheckNameAvailabilityInput parameters = new CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Properties needed to check the availability of a name.
    try {
      CheckNameAvailabilityOutput result = apiInstance.mediaServiceCheckNameAvailability(subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceCheckNameAvailability");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **parameters** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Properties needed to check the availability of a name. | |

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Returns details about whether a Media Service resource name is available. |  -  |
| **0** | CheckNameAvailability of a Media Service failed. |  -  |

<a id="mediaServiceCreate"></a>
# **mediaServiceCreate**
> MediaService mediaServiceCreate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Creates a Media Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
    MediaService parameters = new MediaService(); // MediaService | Media Service properties needed for creation.
    try {
      MediaService result = apiInstance.mediaServiceCreate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceCreate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **mediaServiceName** | **String**| Name of the Media Service. | |
| **parameters** | [**MediaService**](MediaService.md)| Media Service properties needed for creation. | |

### Return type

[**MediaService**](MediaService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success. Returns the new Media Services account. |  -  |
| **0** | Create Media Services failed. |  -  |

<a id="mediaServiceDelete"></a>
# **mediaServiceDelete**
> mediaServiceDelete(subscriptionId, apiVersion, resourceGroupName, mediaServiceName)



Deletes a Media Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
    try {
      apiInstance.mediaServiceDelete(subscriptionId, apiVersion, resourceGroupName, mediaServiceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **mediaServiceName** | **String**| Name of the Media Service. | |

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
| **200** | Success. The Media Services account was deleted. |  -  |
| **204** | No Content. The account name does not exist. |  -  |
| **0** | Delete Media Services failed. |  -  |

<a id="mediaServiceGet"></a>
# **mediaServiceGet**
> MediaService mediaServiceGet(subscriptionId, apiVersion, resourceGroupName, mediaServiceName)



Gets a Media Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
    try {
      MediaService result = apiInstance.mediaServiceGet(subscriptionId, apiVersion, resourceGroupName, mediaServiceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **mediaServiceName** | **String**| Name of the Media Service. | |

### Return type

[**MediaService**](MediaService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Returns the details of the Media Services account. |  -  |
| **0** | Get Media Services failed. |  -  |

<a id="mediaServiceListByResourceGroup"></a>
# **mediaServiceListByResourceGroup**
> MediaServiceCollection mediaServiceListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)



Lists all of the Media Services in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    try {
      MediaServiceCollection result = apiInstance.mediaServiceListByResourceGroup(subscriptionId, apiVersion, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceListByResourceGroup");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |

### Return type

[**MediaServiceCollection**](MediaServiceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Returns a list of all of the Media Services accounts in a resource group. |  -  |
| **0** | List Media Services failed. |  -  |

<a id="mediaServiceListKeys"></a>
# **mediaServiceListKeys**
> ServiceKeys mediaServiceListKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName)



Lists the keys for a Media Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
    try {
      ServiceKeys result = apiInstance.mediaServiceListKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceListKeys");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **mediaServiceName** | **String**| Name of the Media Service. | |

### Return type

[**ServiceKeys**](ServiceKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The keys for the Media Services account were listed. |  -  |
| **0** | List Media Service keys failed. |  -  |

<a id="mediaServiceRegenerateKey"></a>
# **mediaServiceRegenerateKey**
> RegenerateKeyOutput mediaServiceRegenerateKey(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Regenerates a primary or secondary key for a Media Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
    RegenerateKeyInput parameters = new RegenerateKeyInput(); // RegenerateKeyInput | Properties needed to regenerate the Media Service key.
    try {
      RegenerateKeyOutput result = apiInstance.mediaServiceRegenerateKey(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceRegenerateKey");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **mediaServiceName** | **String**| Name of the Media Service. | |
| **parameters** | [**RegenerateKeyInput**](RegenerateKeyInput.md)| Properties needed to regenerate the Media Service key. | |

### Return type

[**RegenerateKeyOutput**](RegenerateKeyOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The Media Services key specified in the input was regenerated. |  -  |
| **0** | Regenerate Media Service key failed. |  -  |

<a id="mediaServiceSyncStorageKeys"></a>
# **mediaServiceSyncStorageKeys**
> mediaServiceSyncStorageKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Synchronizes storage account keys for a storage account associated with the Media Service account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
    SyncStorageKeysInput parameters = new SyncStorageKeysInput(); // SyncStorageKeysInput | Properties needed to synchronize the keys for a storage account to the Media Service.
    try {
      apiInstance.mediaServiceSyncStorageKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceSyncStorageKeys");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **mediaServiceName** | **String**| Name of the Media Service. | |
| **parameters** | [**SyncStorageKeysInput**](SyncStorageKeysInput.md)| Properties needed to synchronize the keys for a storage account to the Media Service. | |

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
| **200** | Success. The keys for the storage account were synchronized. |  -  |
| **0** | Synch Media Service storage keys failed. |  -  |

<a id="mediaServiceUpdate"></a>
# **mediaServiceUpdate**
> MediaService mediaServiceUpdate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Updates a Media Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
    MediaService parameters = new MediaService(); // MediaService | Media Service properties needed for update.
    try {
      MediaService result = apiInstance.mediaServiceUpdate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mediaServiceUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **mediaServiceName** | **String**| Name of the Media Service. | |
| **parameters** | [**MediaService**](MediaService.md)| Media Service properties needed for update. | |

### Return type

[**MediaService**](MediaService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The Media Services account was updated. |  -  |
| **0** | Update Media Services failed. |  -  |

<a id="operationsList"></a>
# **operationsList**
> OperationListResult operationsList(apiVersion)



Lists all of the available Media Services REST API operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
    try {
      OperationListResult result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | |

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Returns a list of operations. |  -  |

