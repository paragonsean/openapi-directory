# EmailTemplatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**emailTemplateCreateOrUpdate**](EmailTemplatesApi.md#emailTemplateCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName} |  |
| [**emailTemplateDelete**](EmailTemplatesApi.md#emailTemplateDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName} |  |
| [**emailTemplateGet**](EmailTemplatesApi.md#emailTemplateGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName} |  |
| [**emailTemplateGetEntityTag**](EmailTemplatesApi.md#emailTemplateGetEntityTag) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName} |  |
| [**emailTemplateUpdate**](EmailTemplatesApi.md#emailTemplateUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/templates/{templateName} |  |


<a id="emailTemplateCreateOrUpdate"></a>
# **emailTemplateCreateOrUpdate**
> EmailTemplateGet200Response emailTemplateCreateOrUpdate(resourceGroupName, serviceName, templateName, apiVersion, subscriptionId, parameters, ifMatch)



Updates an Email Template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String templateName = "applicationApprovedNotificationMessage"; // String | Email Template Name Identifier.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    EmailTemplateCreateOrUpdateRequest parameters = new EmailTemplateCreateOrUpdateRequest(); // EmailTemplateCreateOrUpdateRequest | Email Template update parameters.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    try {
      EmailTemplateGet200Response result = apiInstance.emailTemplateCreateOrUpdate(resourceGroupName, serviceName, templateName, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#emailTemplateCreateOrUpdate");
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
| **templateName** | **String**| Email Template Name Identifier. | [enum: applicationApprovedNotificationMessage, accountClosedDeveloper, quotaLimitApproachingDeveloperNotificationMessage, newDeveloperNotificationMessage, emailChangeIdentityDefault, inviteUserNotificationMessage, newCommentNotificationMessage, confirmSignUpIdentityDefault, newIssueNotificationMessage, purchaseDeveloperNotificationMessage, passwordResetIdentityDefault, passwordResetByAdminNotificationMessage, rejectDeveloperNotificationMessage, requestDeveloperNotificationMessage] |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**EmailTemplateCreateOrUpdateRequest**](EmailTemplateCreateOrUpdateRequest.md)| Email Template update parameters. | |
| **ifMatch** | **String**| ETag of the Entity. Not required when creating an entity, but required when updating an entity. | [optional] |

### Return type

[**EmailTemplateGet200Response**](EmailTemplateGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Email Template was successfully updated. |  -  |
| **201** | Email Template was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="emailTemplateDelete"></a>
# **emailTemplateDelete**
> emailTemplateDelete(resourceGroupName, serviceName, templateName, ifMatch, apiVersion, subscriptionId)



Reset the Email Template to default template provided by the API Management service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String templateName = "applicationApprovedNotificationMessage"; // String | Email Template Name Identifier.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.emailTemplateDelete(resourceGroupName, serviceName, templateName, ifMatch, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#emailTemplateDelete");
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
| **templateName** | **String**| Email Template Name Identifier. | [enum: applicationApprovedNotificationMessage, accountClosedDeveloper, quotaLimitApproachingDeveloperNotificationMessage, newDeveloperNotificationMessage, emailChangeIdentityDefault, inviteUserNotificationMessage, newCommentNotificationMessage, confirmSignUpIdentityDefault, newIssueNotificationMessage, purchaseDeveloperNotificationMessage, passwordResetIdentityDefault, passwordResetByAdminNotificationMessage, rejectDeveloperNotificationMessage, requestDeveloperNotificationMessage] |
| **ifMatch** | **String**| ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
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
| **200** | Email Template was successfully reset to default. |  -  |
| **204** | Email Template was successfully reset to default. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="emailTemplateGet"></a>
# **emailTemplateGet**
> EmailTemplateGet200Response emailTemplateGet(resourceGroupName, serviceName, templateName, apiVersion, subscriptionId)



Gets the details of the email template specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String templateName = "applicationApprovedNotificationMessage"; // String | Email Template Name Identifier.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      EmailTemplateGet200Response result = apiInstance.emailTemplateGet(resourceGroupName, serviceName, templateName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#emailTemplateGet");
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
| **templateName** | **String**| Email Template Name Identifier. | [enum: applicationApprovedNotificationMessage, accountClosedDeveloper, quotaLimitApproachingDeveloperNotificationMessage, newDeveloperNotificationMessage, emailChangeIdentityDefault, inviteUserNotificationMessage, newCommentNotificationMessage, confirmSignUpIdentityDefault, newIssueNotificationMessage, purchaseDeveloperNotificationMessage, passwordResetIdentityDefault, passwordResetByAdminNotificationMessage, rejectDeveloperNotificationMessage, requestDeveloperNotificationMessage] |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**EmailTemplateGet200Response**](EmailTemplateGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the specified Email template. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="emailTemplateGetEntityTag"></a>
# **emailTemplateGetEntityTag**
> emailTemplateGetEntityTag(resourceGroupName, serviceName, templateName, apiVersion, subscriptionId)



Gets the entity state (Etag) version of the email template specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String templateName = "applicationApprovedNotificationMessage"; // String | Email Template Name Identifier.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.emailTemplateGetEntityTag(resourceGroupName, serviceName, templateName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#emailTemplateGetEntityTag");
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
| **templateName** | **String**| Email Template Name Identifier. | [enum: applicationApprovedNotificationMessage, accountClosedDeveloper, quotaLimitApproachingDeveloperNotificationMessage, newDeveloperNotificationMessage, emailChangeIdentityDefault, inviteUserNotificationMessage, newCommentNotificationMessage, confirmSignUpIdentityDefault, newIssueNotificationMessage, purchaseDeveloperNotificationMessage, passwordResetIdentityDefault, passwordResetByAdminNotificationMessage, rejectDeveloperNotificationMessage, requestDeveloperNotificationMessage] |
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
| **200** | Specified email template entity exists and current entity state version is present in the ETag header. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="emailTemplateUpdate"></a>
# **emailTemplateUpdate**
> emailTemplateUpdate(resourceGroupName, serviceName, templateName, ifMatch, apiVersion, subscriptionId, parameters)



Updates the specific Email Template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String templateName = "applicationApprovedNotificationMessage"; // String | Email Template Name Identifier.
    String ifMatch = "ifMatch_example"; // String | ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    EmailTemplateCreateOrUpdateRequest parameters = new EmailTemplateCreateOrUpdateRequest(); // EmailTemplateCreateOrUpdateRequest | Update parameters.
    try {
      apiInstance.emailTemplateUpdate(resourceGroupName, serviceName, templateName, ifMatch, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#emailTemplateUpdate");
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
| **templateName** | **String**| Email Template Name Identifier. | [enum: applicationApprovedNotificationMessage, accountClosedDeveloper, quotaLimitApproachingDeveloperNotificationMessage, newDeveloperNotificationMessage, emailChangeIdentityDefault, inviteUserNotificationMessage, newCommentNotificationMessage, confirmSignUpIdentityDefault, newIssueNotificationMessage, purchaseDeveloperNotificationMessage, passwordResetIdentityDefault, passwordResetByAdminNotificationMessage, rejectDeveloperNotificationMessage, requestDeveloperNotificationMessage] |
| **ifMatch** | **String**| ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**EmailTemplateCreateOrUpdateRequest**](EmailTemplateCreateOrUpdateRequest.md)| Update parameters. | |

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
| **204** | Email Template was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

