# UserConfirmationPasswordSendApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userConfirmationPasswordSend**](UserConfirmationPasswordSendApi.md#userConfirmationPasswordSend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/users/{userId}/confirmations/password/send |  |


<a id="userConfirmationPasswordSend"></a>
# **userConfirmationPasswordSend**
> userConfirmationPasswordSend(resourceGroupName, serviceName, userId, apiVersion, subscriptionId, appType)



Sends confirmation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserConfirmationPasswordSendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UserConfirmationPasswordSendApi apiInstance = new UserConfirmationPasswordSendApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String userId = "userId_example"; // String | User identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String appType = "portal"; // String | Determines the type of application which send the create user request. Default is legacy publisher portal.
    try {
      apiInstance.userConfirmationPasswordSend(resourceGroupName, serviceName, userId, apiVersion, subscriptionId, appType);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserConfirmationPasswordSendApi#userConfirmationPasswordSend");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **userId** | **String**| User identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **appType** | **String**| Determines the type of application which send the create user request. Default is legacy publisher portal. | [optional] [default to portal] [enum: portal, developerPortal] |

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
| **204** | Notification successfully sent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

