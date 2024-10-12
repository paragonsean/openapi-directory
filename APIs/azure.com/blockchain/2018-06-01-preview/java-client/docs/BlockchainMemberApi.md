# BlockchainMemberApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blockchainMembersCreate**](BlockchainMemberApi.md#blockchainMembersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} |  |
| [**blockchainMembersDelete**](BlockchainMemberApi.md#blockchainMembersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} |  |
| [**blockchainMembersGet**](BlockchainMemberApi.md#blockchainMembersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} |  |
| [**blockchainMembersList**](BlockchainMemberApi.md#blockchainMembersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers |  |
| [**blockchainMembersListAll**](BlockchainMemberApi.md#blockchainMembersListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/blockchainMembers |  |
| [**blockchainMembersListApiKeys**](BlockchainMemberApi.md#blockchainMembersListApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/listApiKeys |  |
| [**blockchainMembersListConsortiumMembers**](BlockchainMemberApi.md#blockchainMembersListConsortiumMembers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/consortiumMembers |  |
| [**blockchainMembersListRegenerateApiKeys**](BlockchainMemberApi.md#blockchainMembersListRegenerateApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/regenerateApiKeys |  |
| [**blockchainMembersUpdate**](BlockchainMemberApi.md#blockchainMembersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} |  |


<a id="blockchainMembersCreate"></a>
# **blockchainMembersCreate**
> BlockchainMember blockchainMembersCreate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, blockchainMember)



Create a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    BlockchainMember blockchainMember = new BlockchainMember(); // BlockchainMember | Payload to create a blockchain member.
    try {
      BlockchainMember result = apiInstance.blockchainMembersCreate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, blockchainMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersCreate");
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
| **blockchainMemberName** | **String**| Blockchain member name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **blockchainMember** | [**BlockchainMember**](BlockchainMember.md)| Payload to create a blockchain member. | [optional] |

### Return type

[**BlockchainMember**](BlockchainMember.md)

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

<a id="blockchainMembersDelete"></a>
# **blockchainMembersDelete**
> blockchainMembersDelete(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Delete a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      apiInstance.blockchainMembersDelete(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersDelete");
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
| **blockchainMemberName** | **String**| Blockchain member name | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |

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
| **202** | Success |  -  |
| **204** | Success |  -  |

<a id="blockchainMembersGet"></a>
# **blockchainMembersGet**
> BlockchainMember blockchainMembersGet(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Get details about a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      BlockchainMember result = apiInstance.blockchainMembersGet(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersGet");
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
| **blockchainMemberName** | **String**| Blockchain member name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |

### Return type

[**BlockchainMember**](BlockchainMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="blockchainMembersList"></a>
# **blockchainMembersList**
> BlockchainMemberCollection blockchainMembersList(apiVersion, subscriptionId, resourceGroupName)



Lists the blockchain members for a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      BlockchainMemberCollection result = apiInstance.blockchainMembersList(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersList");
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
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |

### Return type

[**BlockchainMemberCollection**](BlockchainMemberCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="blockchainMembersListAll"></a>
# **blockchainMembersListAll**
> BlockchainMemberCollection blockchainMembersListAll(apiVersion, subscriptionId)



Lists the blockchain members for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    try {
      BlockchainMemberCollection result = apiInstance.blockchainMembersListAll(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersListAll");
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
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |

### Return type

[**BlockchainMemberCollection**](BlockchainMemberCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="blockchainMembersListApiKeys"></a>
# **blockchainMembersListApiKeys**
> ApiKeyCollection blockchainMembersListApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Lists the API keys for a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      ApiKeyCollection result = apiInstance.blockchainMembersListApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersListApiKeys");
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
| **blockchainMemberName** | **String**| Blockchain member name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |

### Return type

[**ApiKeyCollection**](ApiKeyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="blockchainMembersListConsortiumMembers"></a>
# **blockchainMembersListConsortiumMembers**
> ConsortiumMemberCollection blockchainMembersListConsortiumMembers(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Lists the consortium members for a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      ConsortiumMemberCollection result = apiInstance.blockchainMembersListConsortiumMembers(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersListConsortiumMembers");
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
| **blockchainMemberName** | **String**| Blockchain member name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |

### Return type

[**ConsortiumMemberCollection**](ConsortiumMemberCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="blockchainMembersListRegenerateApiKeys"></a>
# **blockchainMembersListRegenerateApiKeys**
> ApiKeyCollection blockchainMembersListRegenerateApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, apiKey)



Regenerate the API keys for a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    ApiKey apiKey = new ApiKey(); // ApiKey | api key to be regenerate
    try {
      ApiKeyCollection result = apiInstance.blockchainMembersListRegenerateApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersListRegenerateApiKeys");
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
| **blockchainMemberName** | **String**| Blockchain member name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **apiKey** | [**ApiKey**](ApiKey.md)| api key to be regenerate | [optional] |

### Return type

[**ApiKeyCollection**](ApiKeyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="blockchainMembersUpdate"></a>
# **blockchainMembersUpdate**
> BlockchainMember blockchainMembersUpdate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, blockchainMember)



Update a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberApi apiInstance = new BlockchainMemberApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    BlockchainMemberUpdate blockchainMember = new BlockchainMemberUpdate(); // BlockchainMemberUpdate | Payload to update the blockchain member.
    try {
      BlockchainMember result = apiInstance.blockchainMembersUpdate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, blockchainMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberApi#blockchainMembersUpdate");
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
| **blockchainMemberName** | **String**| Blockchain member name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **blockchainMember** | [**BlockchainMemberUpdate**](BlockchainMemberUpdate.md)| Payload to update the blockchain member. | [optional] |

### Return type

[**BlockchainMember**](BlockchainMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

