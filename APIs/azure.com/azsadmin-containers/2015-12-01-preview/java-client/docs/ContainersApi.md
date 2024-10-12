# ContainersApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containersCancelMigration**](ContainersApi.md#containersCancelMigration) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/operationresults/{operationId} |  |
| [**containersList**](ContainersApi.md#containersList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/containers |  |
| [**containersListDestinationShares**](ContainersApi.md#containersListDestinationShares) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/destinationshares |  |
| [**containersMigrate**](ContainersApi.md#containersMigrate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/migrate |  |
| [**containersMigrationStatus**](ContainersApi.md#containersMigrationStatus) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/operationresults/{operationId} |  |


<a id="containersCancelMigration"></a>
# **containersCancelMigration**
> MigrationResult containersCancelMigration(subscriptionId, resourceGroupName, farmId, operationId, apiVersion)



Cancel a container migration job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContainersApi apiInstance = new ContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String operationId = "operationId_example"; // String | Operation Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      MigrationResult result = apiInstance.containersCancelMigration(subscriptionId, resourceGroupName, farmId, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainersApi#containersCancelMigration");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **operationId** | **String**| Operation Id. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**MigrationResult**](MigrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Operation has been accepted and processed |  -  |
| **202** | ACCEPTED - Operation has been accepted will be processed asynchronously |  -  |

<a id="containersList"></a>
# **containersList**
> List&lt;Container&gt; containersList(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, intent, maxCount, startIndex)



Returns the list of containers which can be migrated in the specified share.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContainersApi apiInstance = new ContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String shareName = "shareName_example"; // String | Share name.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    String intent = "intent_example"; // String | The container migration intent.
    Integer maxCount = 56; // Integer | The maximum number of containers.
    Integer startIndex = 56; // Integer | The starting index the resource provider uses.
    try {
      List<Container> result = apiInstance.containersList(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, intent, maxCount, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainersApi#containersList");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **shareName** | **String**| Share name. | |
| **apiVersion** | **String**| REST Api Version. | |
| **intent** | **String**| The container migration intent. | |
| **maxCount** | **Integer**| The maximum number of containers. | [optional] |
| **startIndex** | **Integer**| The starting index the resource provider uses. | [optional] |

### Return type

[**List&lt;Container&gt;**](Container.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of containers has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm or share was not found. |  -  |

<a id="containersListDestinationShares"></a>
# **containersListDestinationShares**
> List&lt;ContainersListDestinationShares200ResponseInner&gt; containersListDestinationShares(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a list of destination shares that the system considers as best candidates for migration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContainersApi apiInstance = new ContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String shareName = "shareName_example"; // String | Share name.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      List<ContainersListDestinationShares200ResponseInner> result = apiInstance.containersListDestinationShares(subscriptionId, resourceGroupName, farmId, shareName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainersApi#containersListDestinationShares");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **shareName** | **String**| Share name. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**List&lt;ContainersListDestinationShares200ResponseInner&gt;**](ContainersListDestinationShares200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of shares has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm or share was not found. |  -  |

<a id="containersMigrate"></a>
# **containersMigrate**
> MigrationResult containersMigrate(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, migrationParameters)



Starts a container migration job to migrate containers to the specified destination share.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContainersApi apiInstance = new ContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String shareName = "shareName_example"; // String | Share name.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    MigrationParameters migrationParameters = new MigrationParameters(); // MigrationParameters | The parameters of container migration job.
    try {
      MigrationResult result = apiInstance.containersMigrate(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, migrationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainersApi#containersMigrate");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **shareName** | **String**| Share name. | |
| **apiVersion** | **String**| REST Api Version. | |
| **migrationParameters** | [**MigrationParameters**](MigrationParameters.md)| The parameters of container migration job. | |

### Return type

[**MigrationResult**](MigrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Container has been migrated |  -  |
| **202** | ACCEPTED -- Operation accepted and will be performed asynchronously |  -  |

<a id="containersMigrationStatus"></a>
# **containersMigrationStatus**
> MigrationResult containersMigrationStatus(subscriptionId, resourceGroupName, farmId, operationId, apiVersion)



Returns the status of a container migration job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContainersApi apiInstance = new ContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String operationId = "operationId_example"; // String | Operation Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      MigrationResult result = apiInstance.containersMigrationStatus(subscriptionId, resourceGroupName, farmId, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainersApi#containersMigrationStatus");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **operationId** | **String**| Operation Id. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**MigrationResult**](MigrationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Operation has been accepted and processed |  -  |

