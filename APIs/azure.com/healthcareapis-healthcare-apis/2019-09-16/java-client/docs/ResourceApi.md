# ResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationResultsGet**](ResourceApi.md#operationResultsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HealthcareApis/locations/{locationName}/operationresults/{operationResultId} |  |
| [**servicesCreateOrUpdate**](ResourceApi.md#servicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} |  |
| [**servicesDelete**](ResourceApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} |  |
| [**servicesGet**](ResourceApi.md#servicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} |  |
| [**servicesUpdate**](ResourceApi.md#servicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services/{resourceName} |  |


<a id="operationResultsGet"></a>
# **operationResultsGet**
> OperationResultsDescription operationResultsGet(apiVersion, subscriptionId, locationName, operationResultId)



Get the operation result for a long running operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String locationName = "locationName_example"; // String | The location of the operation.
    String operationResultId = "operationResultId_example"; // String | The ID of the operation result to get.
    try {
      OperationResultsDescription result = apiInstance.operationResultsGet(apiVersion, subscriptionId, locationName, operationResultId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#operationResultsGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **locationName** | **String**| The location of the operation. | |
| **operationResultId** | **String**| The ID of the operation result to get. | |

### Return type

[**OperationResultsDescription**](OperationResultsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all of the properties of the operation result. |  -  |
| **404** | No operation result was found matching operationResultId. |  -  |
| **0** | Default error response |  -  |

<a id="servicesCreateOrUpdate"></a>
# **servicesCreateOrUpdate**
> ServicesDescription servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, serviceDescription)



Create or update the metadata of a service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
    String resourceName = "resourceName_example"; // String | The name of the service instance.
    ServicesDescription serviceDescription = new ServicesDescription(); // ServicesDescription | The service instance metadata.
    try {
      ServicesDescription result = apiInstance.servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, serviceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#servicesCreateOrUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | |
| **resourceName** | **String**| The name of the service instance. | |
| **serviceDescription** | [**ServicesDescription**](ServicesDescription.md)| The service instance metadata. | |

### Return type

[**ServicesDescription**](ServicesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated - Put request accepted and an existing resource is being updated; the operation will complete asynchronously. |  -  |
| **201** | Created - Put request accepted and a new resource was created; the operation will complete asynchronously. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="servicesDelete"></a>
# **servicesDelete**
> servicesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete a service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
    String resourceName = "resourceName_example"; // String | The name of the service instance.
    try {
      apiInstance.servicesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#servicesDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | |
| **resourceName** | **String**| The name of the service instance. | |

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
| **202** | Accepted - Delete request accepted; the operation will complete asynchronously. |  -  |
| **204** | The resource does not exist. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="servicesGet"></a>
# **servicesGet**
> ServicesDescription servicesGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the metadata of a service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
    String resourceName = "resourceName_example"; // String | The name of the service instance.
    try {
      ServicesDescription result = apiInstance.servicesGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#servicesGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | |
| **resourceName** | **String**| The name of the service instance. | |

### Return type

[**ServicesDescription**](ServicesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all of the properties of the service instance. |  -  |
| **0** | Default error response |  -  |

<a id="servicesUpdate"></a>
# **servicesUpdate**
> ServicesDescription servicesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, servicePatchDescription)



Update the metadata of a service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
    String resourceName = "resourceName_example"; // String | The name of the service instance.
    ServicesPatchDescription servicePatchDescription = new ServicesPatchDescription(); // ServicesPatchDescription | The service instance metadata and security metadata.
    try {
      ServicesDescription result = apiInstance.servicesUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, servicePatchDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#servicesUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | |
| **resourceName** | **String**| The name of the service instance. | |
| **servicePatchDescription** | [**ServicesPatchDescription**](ServicesPatchDescription.md)| The service instance metadata and security metadata. | |

### Return type

[**ServicesDescription**](ServicesDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tags for the resource were updated successfully. |  -  |
| **0** | DefaultErrorResponse |  -  |

