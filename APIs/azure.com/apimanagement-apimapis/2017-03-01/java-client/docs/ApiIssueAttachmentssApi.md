# ApiIssueAttachmentssApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiIssuAttachmentHead**](ApiIssueAttachmentssApi.md#apiIssuAttachmentHead) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} |  |
| [**apiIssueAttachmentCreateOrUpdate**](ApiIssueAttachmentssApi.md#apiIssueAttachmentCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/issues/{issueId}/attachments/{attachmentId} |  |


<a id="apiIssuAttachmentHead"></a>
# **apiIssuAttachmentHead**
> apiIssuAttachmentHead(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the issue Attachment for an API specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiIssueAttachmentssApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiIssueAttachmentssApi apiInstance = new ApiIssueAttachmentssApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
    String attachmentId = "attachmentId_example"; // String | Attachment identifier within an Issue. Must be unique in the current Issue.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiIssuAttachmentHead(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiIssueAttachmentssApi#apiIssuAttachmentHead");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | |
| **attachmentId** | **String**| Attachment identifier within an Issue. Must be unique in the current Issue. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Operation completed successfully. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiIssueAttachmentCreateOrUpdate"></a>
# **apiIssueAttachmentCreateOrUpdate**
> IssueAttachmentContract apiIssueAttachmentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId, parameters, ifMatch)



Creates a new Attachment for the Issue in an API or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiIssueAttachmentssApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiIssueAttachmentssApi apiInstance = new ApiIssueAttachmentssApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String issueId = "issueId_example"; // String | Issue identifier. Must be unique in the current API Management service instance.
    String attachmentId = "attachmentId_example"; // String | Attachment identifier within an Issue. Must be unique in the current Issue.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    IssueAttachmentContract parameters = new IssueAttachmentContract(); // IssueAttachmentContract | Create parameters.
    String ifMatch = "ifMatch_example"; // String | ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    try {
      IssueAttachmentContract result = apiInstance.apiIssueAttachmentCreateOrUpdate(resourceGroupName, serviceName, apiId, issueId, attachmentId, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiIssueAttachmentssApi#apiIssueAttachmentCreateOrUpdate");
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
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **issueId** | **String**| Issue identifier. Must be unique in the current API Management service instance. | |
| **attachmentId** | **String**| Attachment identifier within an Issue. Must be unique in the current Issue. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**IssueAttachmentContract**](IssueAttachmentContract.md)| Create parameters. | |
| **ifMatch** | **String**| ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | [optional] |

### Return type

[**IssueAttachmentContract**](IssueAttachmentContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Issue Attachment was successfully updated. |  -  |
| **201** | Issue Attachment was successfully created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

