# ApiDiagnosticLoggersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDiagnosticLoggerCheckEntityExists**](ApiDiagnosticLoggersApi.md#apiDiagnosticLoggerCheckEntityExists) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/diagnostics/{diagnosticId}/loggers/{loggerid} |  |
| [**apiDiagnosticLoggerCreateOrUpdate**](ApiDiagnosticLoggersApi.md#apiDiagnosticLoggerCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/diagnostics/{diagnosticId}/loggers/{loggerid} |  |
| [**apiDiagnosticLoggerDelete**](ApiDiagnosticLoggersApi.md#apiDiagnosticLoggerDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/diagnostics/{diagnosticId}/loggers/{loggerid} |  |
| [**apiDiagnosticLoggerListByService**](ApiDiagnosticLoggersApi.md#apiDiagnosticLoggerListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/apis/{apiId}/diagnostics/{diagnosticId}/loggers |  |


<a id="apiDiagnosticLoggerCheckEntityExists"></a>
# **apiDiagnosticLoggerCheckEntityExists**
> apiDiagnosticLoggerCheckEntityExists(resourceGroupName, serviceName, apiId, diagnosticId, loggerid, apiVersion, subscriptionId)



Checks that logger entity specified by identifier is associated with the diagnostics entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiDiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiDiagnosticLoggersApi apiInstance = new ApiDiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiDiagnosticLoggerCheckEntityExists(resourceGroupName, serviceName, apiId, diagnosticId, loggerid, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiDiagnosticLoggersApi#apiDiagnosticLoggerCheckEntityExists");
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
| **204** | Entity exists |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiDiagnosticLoggerCreateOrUpdate"></a>
# **apiDiagnosticLoggerCreateOrUpdate**
> ApiDiagnosticLoggerCreateOrUpdate200Response apiDiagnosticLoggerCreateOrUpdate(resourceGroupName, serviceName, apiId, diagnosticId, loggerid, apiVersion, subscriptionId)



Attaches a logger to a diagnostic for an API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiDiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiDiagnosticLoggersApi apiInstance = new ApiDiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiDiagnosticLoggerCreateOrUpdate200Response result = apiInstance.apiDiagnosticLoggerCreateOrUpdate(resourceGroupName, serviceName, apiId, diagnosticId, loggerid, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiDiagnosticLoggersApi#apiDiagnosticLoggerCreateOrUpdate");
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
| **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | |
| **loggerid** | **String**| Logger identifier. Must be unique in the API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiDiagnosticLoggerCreateOrUpdate200Response**](ApiDiagnosticLoggerCreateOrUpdate200Response.md)

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

<a id="apiDiagnosticLoggerDelete"></a>
# **apiDiagnosticLoggerDelete**
> apiDiagnosticLoggerDelete(resourceGroupName, serviceName, apiId, diagnosticId, loggerid, apiVersion, subscriptionId)



Deletes the specified Logger from Diagnostic for an API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiDiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiDiagnosticLoggersApi apiInstance = new ApiDiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiDiagnosticLoggerDelete(resourceGroupName, serviceName, apiId, diagnosticId, loggerid, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiDiagnosticLoggersApi#apiDiagnosticLoggerDelete");
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
| **204** | The Logger was successfully detached from Diagnostic. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiDiagnosticLoggerListByService"></a>
# **apiDiagnosticLoggerListByService**
> ApiDiagnosticLoggerListByService200Response apiDiagnosticLoggerListByService(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, diagnosticId, $filter, $top, $skip)



Lists all loggers associated with the specified Diagnostic of an API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiDiagnosticLoggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiDiagnosticLoggersApi apiInstance = new ApiDiagnosticLoggersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
    String $filter = "$filter_example"; // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | type        | eq                     |                                   |
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ApiDiagnosticLoggerListByService200Response result = apiInstance.apiDiagnosticLoggerListByService(resourceGroupName, serviceName, apiId, apiVersion, subscriptionId, diagnosticId, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiDiagnosticLoggersApi#apiDiagnosticLoggerListByService");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | |
| **$filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | type        | eq                     |                                   | | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ApiDiagnosticLoggerListByService200Response**](ApiDiagnosticLoggerListByService200Response.md)

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

