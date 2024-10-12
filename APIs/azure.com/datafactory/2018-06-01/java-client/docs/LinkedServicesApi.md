# LinkedServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**linkedServicesCreateOrUpdate**](LinkedServicesApi.md#linkedServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName} |  |
| [**linkedServicesDelete**](LinkedServicesApi.md#linkedServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName} |  |
| [**linkedServicesGet**](LinkedServicesApi.md#linkedServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName} |  |
| [**linkedServicesListByFactory**](LinkedServicesApi.md#linkedServicesListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices |  |


<a id="linkedServicesCreateOrUpdate"></a>
# **linkedServicesCreateOrUpdate**
> LinkedServiceResource linkedServicesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, linkedService, ifMatch)



Creates or updates a linked service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String linkedServiceName = "linkedServiceName_example"; // String | The linked service name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    LinkedServiceResource linkedService = new LinkedServiceResource(); // LinkedServiceResource | Linked service resource definition.
    String ifMatch = "ifMatch_example"; // String | ETag of the linkedService entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    try {
      LinkedServiceResource result = apiInstance.linkedServicesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, linkedService, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **linkedServiceName** | **String**| The linked service name. | |
| **apiVersion** | **String**| The API version. | |
| **linkedService** | [**LinkedServiceResource**](LinkedServiceResource.md)| Linked service resource definition. | |
| **ifMatch** | **String**| ETag of the linkedService entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] |

### Return type

[**LinkedServiceResource**](LinkedServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="linkedServicesDelete"></a>
# **linkedServicesDelete**
> linkedServicesDelete(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion)



Deletes a linked service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String linkedServiceName = "linkedServiceName_example"; // String | The linked service name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.linkedServicesDelete(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesDelete");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **linkedServiceName** | **String**| The linked service name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | OK. |  -  |
| **204** | No Content. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="linkedServicesGet"></a>
# **linkedServicesGet**
> LinkedServiceResource linkedServicesGet(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, ifNoneMatch)



Gets a linked service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String linkedServiceName = "linkedServiceName_example"; // String | The linked service name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag of the linked service entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    try {
      LinkedServiceResource result = apiInstance.linkedServicesGet(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesGet");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **linkedServiceName** | **String**| The linked service name. | |
| **apiVersion** | **String**| The API version. | |
| **ifNoneMatch** | **String**| ETag of the linked service entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. | [optional] |

### Return type

[**LinkedServiceResource**](LinkedServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **304** | Not modified. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="linkedServicesListByFactory"></a>
# **linkedServicesListByFactory**
> LinkedServiceListResponse linkedServicesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists linked services.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      LinkedServiceListResponse result = apiInstance.linkedServicesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesListByFactory");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**LinkedServiceListResponse**](LinkedServiceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

