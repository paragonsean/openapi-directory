# PrivateAtlasesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateAtlasesCreateOrUpdate**](PrivateAtlasesApi.md#privateAtlasesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} |  |
| [**privateAtlasesDelete**](PrivateAtlasesApi.md#privateAtlasesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} |  |
| [**privateAtlasesGet**](PrivateAtlasesApi.md#privateAtlasesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} |  |
| [**privateAtlasesListByAccount**](PrivateAtlasesApi.md#privateAtlasesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases |  |
| [**privateAtlasesUpdate**](PrivateAtlasesApi.md#privateAtlasesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} |  |


<a id="privateAtlasesCreateOrUpdate"></a>
# **privateAtlasesCreateOrUpdate**
> PrivateAtlas privateAtlasesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasCreateParameters)



Create or update a Private Atlas resource. Private Atlas resource will enable the usage of Azure resources to build a custom set of mapping data. It requires an account to exist before it can be created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateAtlasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateAtlasesApi apiInstance = new PrivateAtlasesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the Maps Account.
    String privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
    PrivateAtlasCreateParameters privateAtlasCreateParameters = new PrivateAtlasCreateParameters(); // PrivateAtlasCreateParameters | The new or updated parameters for the Private Atlas resource.
    try {
      PrivateAtlas result = apiInstance.privateAtlasesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasCreateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateAtlasesApi#privateAtlasesCreateOrUpdate");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **accountName** | **String**| The name of the Maps Account. | |
| **privateAtlasName** | **String**| The name of the Private Atlas instance. | |
| **privateAtlasCreateParameters** | [**PrivateAtlasCreateParameters**](PrivateAtlasCreateParameters.md)| The new or updated parameters for the Private Atlas resource. | |

### Return type

[**PrivateAtlas**](PrivateAtlas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Private Atlas was successfully updated. |  -  |
| **201** | The Private Atlas was successfully created. |  -  |
| **0** | An unexpected error occurred. |  -  |

<a id="privateAtlasesDelete"></a>
# **privateAtlasesDelete**
> privateAtlasesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName)



Delete a Private Atlas resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateAtlasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateAtlasesApi apiInstance = new PrivateAtlasesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the Maps Account.
    String privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
    try {
      apiInstance.privateAtlasesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateAtlasesApi#privateAtlasesDelete");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **accountName** | **String**| The name of the Maps Account. | |
| **privateAtlasName** | **String**| The name of the Private Atlas instance. | |

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
| **200** | The Private Atlas was deleted successfully. |  -  |
| **204** | The specified Private Atlas was not found. Nothing was deleted. |  -  |
| **0** | An unexpected error occurred. |  -  |

<a id="privateAtlasesGet"></a>
# **privateAtlasesGet**
> PrivateAtlas privateAtlasesGet(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName)



Get a Private Atlas resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateAtlasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateAtlasesApi apiInstance = new PrivateAtlasesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the Maps Account.
    String privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
    try {
      PrivateAtlas result = apiInstance.privateAtlasesGet(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateAtlasesApi#privateAtlasesGet");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **accountName** | **String**| The name of the Maps Account. | |
| **privateAtlasName** | **String**| The name of the Private Atlas instance. | |

### Return type

[**PrivateAtlas**](PrivateAtlas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |
| **0** | An unexpected error occurred. |  -  |

<a id="privateAtlasesListByAccount"></a>
# **privateAtlasesListByAccount**
> PrivateAtlasList privateAtlasesListByAccount(apiVersion, subscriptionId, resourceGroupName, accountName)



Get all Private Atlas instances for an Azure Map Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateAtlasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateAtlasesApi apiInstance = new PrivateAtlasesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the Maps Account.
    try {
      PrivateAtlasList result = apiInstance.privateAtlasesListByAccount(apiVersion, subscriptionId, resourceGroupName, accountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateAtlasesApi#privateAtlasesListByAccount");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **accountName** | **String**| The name of the Maps Account. | |

### Return type

[**PrivateAtlasList**](PrivateAtlasList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |
| **0** | An unexpected error occurred. |  -  |

<a id="privateAtlasesUpdate"></a>
# **privateAtlasesUpdate**
> PrivateAtlas privateAtlasesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasUpdateParameters)



Updates the Private Atlas resource. Only a subset of the parameters may be updated after creation, such as Tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateAtlasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateAtlasesApi apiInstance = new PrivateAtlasesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the Maps Account.
    String privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
    PrivateAtlasUpdateParameters privateAtlasUpdateParameters = new PrivateAtlasUpdateParameters(); // PrivateAtlasUpdateParameters | The updated parameters for the Private Atlas.
    try {
      PrivateAtlas result = apiInstance.privateAtlasesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateAtlasesApi#privateAtlasesUpdate");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **accountName** | **String**| The name of the Maps Account. | |
| **privateAtlasName** | **String**| The name of the Private Atlas instance. | |
| **privateAtlasUpdateParameters** | [**PrivateAtlasUpdateParameters**](PrivateAtlasUpdateParameters.md)| The updated parameters for the Private Atlas. | |

### Return type

[**PrivateAtlas**](PrivateAtlas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Private Atlas was successfully updated. |  -  |
| **0** | An unexpected error occurred. |  -  |

