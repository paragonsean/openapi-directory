# DiagnosticLoggersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diagnosticLoggerCheckEntityExists**](DiagnosticLoggersApi.md#diagnosticLoggerCheckEntityExists) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers/{loggerid} |  |
| [**diagnosticLoggerCreateOrUpdate**](DiagnosticLoggersApi.md#diagnosticLoggerCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers/{loggerid} |  |
| [**diagnosticLoggerDelete**](DiagnosticLoggersApi.md#diagnosticLoggerDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers/{loggerid} |  |
| [**diagnosticLoggerListByService**](DiagnosticLoggersApi.md#diagnosticLoggerListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers |  |


<a id="diagnosticLoggerCheckEntityExists"></a>
# **diagnosticLoggerCheckEntityExists**
> diagnosticLoggerCheckEntityExists(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId)



Checks that logger entity specified by identifier is associated with the diagnostics entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticLoggersApi apiInstance = new DiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.diagnosticLoggerCheckEntityExists(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticLoggersApi#diagnosticLoggerCheckEntityExists");
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
| **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | |
| **loggerid** | **String**| Logger identifier. Must be unique in the API Management service instance. | |
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
| **204** | The logger is associated with the diagnostic entity. |  -  |
| **404** | The logger is not associated with the diagnostic entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="diagnosticLoggerCreateOrUpdate"></a>
# **diagnosticLoggerCreateOrUpdate**
> DiagnosticLoggerCreateOrUpdate200Response diagnosticLoggerCreateOrUpdate(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId)



Attaches a logger to a diagnostic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticLoggersApi apiInstance = new DiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DiagnosticLoggerCreateOrUpdate200Response result = apiInstance.diagnosticLoggerCreateOrUpdate(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticLoggersApi#diagnosticLoggerCreateOrUpdate");
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
| **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | |
| **loggerid** | **String**| Logger identifier. Must be unique in the API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DiagnosticLoggerCreateOrUpdate200Response**](DiagnosticLoggerCreateOrUpdate200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Logger to Diagnostic link was successfully updated. |  -  |
| **201** | Logger was successfully attached to Diagnostic. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="diagnosticLoggerDelete"></a>
# **diagnosticLoggerDelete**
> diagnosticLoggerDelete(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId)



Deletes the specified Logger from Diagnostic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticLoggersApi apiInstance = new DiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.diagnosticLoggerDelete(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticLoggersApi#diagnosticLoggerDelete");
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
| **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | |
| **loggerid** | **String**| Logger identifier. Must be unique in the API Management service instance. | |
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
| **200** | The Logger was successfully detached from Diagnostic. |  -  |
| **204** | The Logger was successfully detached from Diagnostic. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="diagnosticLoggerListByService"></a>
# **diagnosticLoggerListByService**
> DiagnosticLoggerListByService200Response diagnosticLoggerListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, diagnosticId, $filter, $top, $skip)



Lists all loggers associated with the specified Diagnostic of the API Management service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiagnosticLoggersApi apiInstance = new DiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String $filter = "$filter_example"; // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | type        | eq                     |                                   |
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      DiagnosticLoggerListByService200Response result = apiInstance.diagnosticLoggerListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, diagnosticId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosticLoggersApi#diagnosticLoggerListByService");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | |
| **$filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | type        | eq                     |                                   | | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**DiagnosticLoggerListByService200Response**](DiagnosticLoggerListByService200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paged Result response of loggers assigned to the specified Diagnostic. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

