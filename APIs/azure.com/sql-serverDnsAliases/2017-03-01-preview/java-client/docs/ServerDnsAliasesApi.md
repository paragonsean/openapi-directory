# ServerDnsAliasesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverDnsAliasesAcquire**](ServerDnsAliasesApi.md#serverDnsAliasesAcquire) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName}/acquire |  |
| [**serverDnsAliasesCreateOrUpdate**](ServerDnsAliasesApi.md#serverDnsAliasesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName} |  |
| [**serverDnsAliasesDelete**](ServerDnsAliasesApi.md#serverDnsAliasesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName} |  |
| [**serverDnsAliasesGet**](ServerDnsAliasesApi.md#serverDnsAliasesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName} |  |
| [**serverDnsAliasesListByServer**](ServerDnsAliasesApi.md#serverDnsAliasesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases |  |


<a id="serverDnsAliasesAcquire"></a>
# **serverDnsAliasesAcquire**
> serverDnsAliasesAcquire(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion, parameters)



Acquires server DNS alias from another server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerDnsAliasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerDnsAliasesApi apiInstance = new ServerDnsAliasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
    String dnsAliasName = "dnsAliasName_example"; // String | The name of the server dns alias.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ServerDnsAliasAcquisition parameters = new ServerDnsAliasAcquisition(); // ServerDnsAliasAcquisition | 
    try {
      apiInstance.serverDnsAliasesAcquire(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerDnsAliasesApi#serverDnsAliasesAcquire");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server that the alias is pointing to. | |
| **dnsAliasName** | **String**| The name of the server dns alias. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ServerDnsAliasAcquisition**](ServerDnsAliasAcquisition.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully acquired server DNS alias. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidServerDnsAliasAcquireRequest - The acquire server DNS alias request body is empty or invalid (it should contain the old server alias id, for example: /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/servers/dns-alias-old-server/dnsAliases/dns-alias-name-1).   * 400 ServerDnsAliasAcquireRequestInvalidOldServerDnsAliasId -    * 400 UnableToResolveRemoteServer -    * 400 ServerNotFound - The requested server was not found.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 TokenTooLong - The provided token is too long.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidServerName - Invalid server name specified.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ServerDnsAliasAlreadyExists -    * 409 ServerDnsAliasAlreadyExists -    * 409 ServerDnsAliasBusy -    * 409 ServerDnsAliasDnsRecordInUse -    * 409 InvalidServerDnsAliasName -    * 409 SubscriptionDisabled - Subscription is disabled.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 429 ConflictingServerOperation - An operation is currently in progress for the server.   * 429 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="serverDnsAliasesCreateOrUpdate"></a>
# **serverDnsAliasesCreateOrUpdate**
> ServerDnsAlias serverDnsAliasesCreateOrUpdate(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion)



Creates a server dns alias.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerDnsAliasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerDnsAliasesApi apiInstance = new ServerDnsAliasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
    String dnsAliasName = "dnsAliasName_example"; // String | The name of the server DNS alias.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ServerDnsAlias result = apiInstance.serverDnsAliasesCreateOrUpdate(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerDnsAliasesApi#serverDnsAliasesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server that the alias is pointing to. | |
| **dnsAliasName** | **String**| The name of the server DNS alias. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ServerDnsAlias**](ServerDnsAlias.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The server DNS alias already exists. |  -  |
| **201** | Successfully created a server DNS alias. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidServerDnsAliasAcquireRequest - The acquire server DNS alias request body is empty or invalid (it should contain the old server alias id, for example: /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default/providers/Microsoft.Sql/servers/dns-alias-old-server/dnsAliases/dns-alias-name-1).   * 400 ServerDnsAliasAcquireRequestInvalidOldServerDnsAliasId -    * 400 UnableToResolveRemoteServer -    * 400 ServerNotFound - The requested server was not found.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 TokenTooLong - The provided token is too long.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidServerName - Invalid server name specified.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 409 ServerDnsAliasAlreadyExists -    * 409 ServerDnsAliasAlreadyExists -    * 409 ServerDnsAliasBusy -    * 409 ServerDnsAliasDnsRecordInUse -    * 409 InvalidServerDnsAliasName -    * 409 SubscriptionDisabled - Subscription is disabled.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 429 ConflictingServerOperation - An operation is currently in progress for the server.   * 429 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="serverDnsAliasesDelete"></a>
# **serverDnsAliasesDelete**
> serverDnsAliasesDelete(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion)



Deletes the server DNS alias with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerDnsAliasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerDnsAliasesApi apiInstance = new ServerDnsAliasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
    String dnsAliasName = "dnsAliasName_example"; // String | The name of the server DNS alias.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.serverDnsAliasesDelete(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerDnsAliasesApi#serverDnsAliasesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server that the alias is pointing to. | |
| **dnsAliasName** | **String**| The name of the server DNS alias. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the server DNS alias. |  -  |
| **202** | Accepted |  -  |
| **204** | The specified server DNS alias does not exist. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="serverDnsAliasesGet"></a>
# **serverDnsAliasesGet**
> ServerDnsAlias serverDnsAliasesGet(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion)



Gets a server DNS alias.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerDnsAliasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerDnsAliasesApi apiInstance = new ServerDnsAliasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
    String dnsAliasName = "dnsAliasName_example"; // String | The name of the server DNS alias.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ServerDnsAlias result = apiInstance.serverDnsAliasesGet(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerDnsAliasesApi#serverDnsAliasesGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server that the alias is pointing to. | |
| **dnsAliasName** | **String**| The name of the server DNS alias. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ServerDnsAlias**](ServerDnsAlias.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified server DNS alias. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="serverDnsAliasesListByServer"></a>
# **serverDnsAliasesListByServer**
> ServerDnsAliasListResult serverDnsAliasesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of server DNS aliases for a server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerDnsAliasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerDnsAliasesApi apiInstance = new ServerDnsAliasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ServerDnsAliasListResult result = apiInstance.serverDnsAliasesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerDnsAliasesApi#serverDnsAliasesListByServer");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server that the alias is pointing to. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ServerDnsAliasListResult**](ServerDnsAliasListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of server DNS aliases. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

