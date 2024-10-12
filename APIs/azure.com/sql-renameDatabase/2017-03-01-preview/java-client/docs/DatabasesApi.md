# DatabasesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databasesRename**](DatabasesApi.md#databasesRename) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/move |  |


<a id="databasesRename"></a>
# **databasesRename**
> databasesRename(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, parameters)



Renames a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database to rename.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ResourceMoveDefinition parameters = new ResourceMoveDefinition(); // ResourceMoveDefinition | The resource move definition for renaming this database.
    try {
      apiInstance.databasesRename(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesRename");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database to rename. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ResourceMoveDefinition**](ResourceMoveDefinition.md)| The resource move definition for renaming this database. | |

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
| **200** | Successfully renamed the database. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceMoveRequest - The resource move request is invalid.   * 400 InvalidMoveTargetResourceId - The target resource identifier in move request is invalid.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 UnsupportedServiceName - The specified name is an invalid name because it contains one or more unsupported unicode characters.   * 400 CannotMoveOrDropSyncMetadataDatabase - Cannot drop database used as sync metadata database.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 TokenTooLong - The provided token is too long.   * 400 CannotMoveOrDropJobAccountDatabase - Cannot drop database associated with job account.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 404 SourceDatabaseNotFound - The source database does not exist. |  -  |

