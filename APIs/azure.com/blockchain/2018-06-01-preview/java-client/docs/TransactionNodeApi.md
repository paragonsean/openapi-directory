# TransactionNodeApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transactionNodesCreate**](TransactionNodeApi.md#transactionNodesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} |  |
| [**transactionNodesDelete**](TransactionNodeApi.md#transactionNodesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} |  |
| [**transactionNodesGet**](TransactionNodeApi.md#transactionNodesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} |  |
| [**transactionNodesList**](TransactionNodeApi.md#transactionNodesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes |  |
| [**transactionNodesListApiKeys**](TransactionNodeApi.md#transactionNodesListApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}/listApiKeys |  |
| [**transactionNodesListRegenerateApiKeys**](TransactionNodeApi.md#transactionNodesListRegenerateApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}/regenerateApiKeys |  |
| [**transactionNodesUpdate**](TransactionNodeApi.md#transactionNodesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} |  |


<a id="transactionNodesCreate"></a>
# **transactionNodesCreate**
> TransactionNode transactionNodesCreate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, transactionNode)



Create or update the transaction node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionNodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionNodeApi apiInstance = new TransactionNodeApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    TransactionNode transactionNode = new TransactionNode(); // TransactionNode | Payload to create the transaction node.
    try {
      TransactionNode result = apiInstance.transactionNodesCreate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, transactionNode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionNodeApi#transactionNodesCreate");
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
| **transactionNodeName** | **String**| Transaction node name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **transactionNode** | [**TransactionNode**](TransactionNode.md)| Payload to create the transaction node. | [optional] |

### Return type

[**TransactionNode**](TransactionNode.md)

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

<a id="transactionNodesDelete"></a>
# **transactionNodesDelete**
> transactionNodesDelete(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName)



Delete the transaction node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionNodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionNodeApi apiInstance = new TransactionNodeApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      apiInstance.transactionNodesDelete(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionNodeApi#transactionNodesDelete");
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
| **transactionNodeName** | **String**| Transaction node name. | |
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

<a id="transactionNodesGet"></a>
# **transactionNodesGet**
> TransactionNode transactionNodesGet(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName)



Get the details of the transaction node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionNodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionNodeApi apiInstance = new TransactionNodeApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      TransactionNode result = apiInstance.transactionNodesGet(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionNodeApi#transactionNodesGet");
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
| **transactionNodeName** | **String**| Transaction node name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |

### Return type

[**TransactionNode**](TransactionNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="transactionNodesList"></a>
# **transactionNodesList**
> TransactionNodeCollection transactionNodesList(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Lists the transaction nodes for a blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionNodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionNodeApi apiInstance = new TransactionNodeApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      TransactionNodeCollection result = apiInstance.transactionNodesList(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionNodeApi#transactionNodesList");
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

[**TransactionNodeCollection**](TransactionNodeCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="transactionNodesListApiKeys"></a>
# **transactionNodesListApiKeys**
> ApiKeyCollection transactionNodesListApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName)



List the API keys for the transaction node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionNodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionNodeApi apiInstance = new TransactionNodeApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    try {
      ApiKeyCollection result = apiInstance.transactionNodesListApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionNodeApi#transactionNodesListApiKeys");
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
| **transactionNodeName** | **String**| Transaction node name. | |
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

<a id="transactionNodesListRegenerateApiKeys"></a>
# **transactionNodesListRegenerateApiKeys**
> ApiKeyCollection transactionNodesListRegenerateApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, apiKey)



Regenerate the API keys for the blockchain member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionNodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionNodeApi apiInstance = new TransactionNodeApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    ApiKey apiKey = new ApiKey(); // ApiKey | api key to be regenerated
    try {
      ApiKeyCollection result = apiInstance.transactionNodesListRegenerateApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionNodeApi#transactionNodesListRegenerateApiKeys");
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
| **transactionNodeName** | **String**| Transaction node name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **apiKey** | [**ApiKey**](ApiKey.md)| api key to be regenerated | [optional] |

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

<a id="transactionNodesUpdate"></a>
# **transactionNodesUpdate**
> TransactionNode transactionNodesUpdate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, transactionNode)



Update the transaction node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionNodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TransactionNodeApi apiInstance = new TransactionNodeApi(defaultClient);
    String blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
    String transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    TransactionNodeUpdate transactionNode = new TransactionNodeUpdate(); // TransactionNodeUpdate | Payload to create the transaction node.
    try {
      TransactionNode result = apiInstance.transactionNodesUpdate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, transactionNode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionNodeApi#transactionNodesUpdate");
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
| **transactionNodeName** | **String**| Transaction node name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **transactionNode** | [**TransactionNodeUpdate**](TransactionNodeUpdate.md)| Payload to create the transaction node. | [optional] |

### Return type

[**TransactionNode**](TransactionNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

