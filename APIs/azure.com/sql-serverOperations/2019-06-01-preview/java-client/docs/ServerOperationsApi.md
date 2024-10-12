# ServerOperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverOperationsListByServer**](ServerOperationsApi.md#serverOperationsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/operations |  |


<a id="serverOperationsListByServer"></a>
# **serverOperationsListByServer**
> ServerOperationListResult serverOperationsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of operations performed on the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerOperationsApi apiInstance = new ServerOperationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ServerOperationListResult result = apiInstance.serverOperationsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerOperationsApi#serverOperationsListByServer");
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
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ServerOperationListResult**](ServerOperationListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request for getting server operations has been executed successfully. |  -  |
| **0** | *** Error Responses: ***   * 400 NameAlreadyExists - The provided name already exists.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 InvalidLoginName - The provided login name is invalid.   * 400 InvalidUsername - Supplied user name contains invalid characters.   * 400 PasswordTooShort - The provided password is too short   * 400 RegionDoesNotSupportVersion - A user attempted to create a server of a specified version in a location where that server version isn&#39;t supported.   * 400 PasswordTooLong - The provided password is too long.   * 400 PasswordNotComplex - The provided password is not complex enough.   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 400 InvalidLocation - An invalid location was specified.   * 400 InvalidServerName - Invalid server name specified.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 TokenTooLong - The provided token is too long.   * 400 ServerNotFound - The requested server was not found.   * 400 RegionDoesNotAllowProvisioning - The selected location is not accepting new Windows Azure SQL Database servers. This may change at a later time.   * 400 SubscriptionNotFound - The requested subscription was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ServerDisabled - Server is disabled.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 409 SubscriptionDisabled - Subscription is disabled.   * 409 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 409 ServerAlreadyExists - Duplicate server name.   * 409 ServerDisabled - Server is disabled.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 429 ConflictingSubscriptionOperation - An operation is currently in progress for the subscription.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources. |  -  |

