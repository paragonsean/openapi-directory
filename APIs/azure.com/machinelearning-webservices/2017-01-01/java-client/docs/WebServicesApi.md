# WebServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webServicesCreateOrUpdate**](WebServicesApi.md#webServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} |  |
| [**webServicesCreateRegionalProperties**](WebServicesApi.md#webServicesCreateRegionalProperties) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName}/CreateRegionalBlob |  |
| [**webServicesGet**](WebServicesApi.md#webServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} |  |
| [**webServicesListByResourceGroup**](WebServicesApi.md#webServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices |  |
| [**webServicesListBySubscriptionId**](WebServicesApi.md#webServicesListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearning/webServices |  |
| [**webServicesListKeys**](WebServicesApi.md#webServicesListKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName}/listKeys |  |
| [**webServicesPatch**](WebServicesApi.md#webServicesPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} |  |
| [**webServicesRemove**](WebServicesApi.md#webServicesRemove) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} |  |


<a id="webServicesCreateOrUpdate"></a>
# **webServicesCreateOrUpdate**
> WebService webServicesCreateOrUpdate(resourceGroupName, webServiceName, apiVersion, subscriptionId, createOrUpdatePayload)



Create or update a web service. This call will overwrite an existing web service. Note that there is no warning or confirmation. This is a nonrecoverable operation. If your intent is to create a new web service, call the Get operation first to verify that it does not exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
    String webServiceName = "webServiceName_example"; // String | The name of the web service.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    WebService createOrUpdatePayload = new WebService(); // WebService | The payload that is used to create or update the web service.
    try {
      WebService result = apiInstance.webServicesCreateOrUpdate(resourceGroupName, webServiceName, apiVersion, subscriptionId, createOrUpdatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | |
| **webServiceName** | **String**| The name of the web service. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **createOrUpdatePayload** | [**WebService**](WebService.md)| The payload that is used to create or update the web service. | |

### Return type

[**WebService**](WebService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. This response is returned for an update web service operation. The response payload is identical to the response payload that is returned by the GET operation. The response includes the Provisioning State and the Azure-AsyncOperation header. To get the progress of the operation, call GET operation on the URL in Azure-AsyncOperation header field. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  -  |
| **201** | Created. This response is returned for a create web service operation. The response includes the Provisioning State and the Azure-AsyncOperation header. To get the progress of the operation, call GET operation on the URL in Azure-AsyncOperation header field. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  -  |

<a id="webServicesCreateRegionalProperties"></a>
# **webServicesCreateRegionalProperties**
> AsyncOperationStatus webServicesCreateRegionalProperties(resourceGroupName, webServiceName, region, apiVersion, subscriptionId)



Creates an encrypted credentials parameter blob for the specified region. To get the web service from a region other than the region in which it has been created, you must first call Create Regional Web Services Properties to create a copy of the encrypted credential parameter blob in that region. You only need to do this before the first time that you get the web service in the new region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
    String webServiceName = "webServiceName_example"; // String | The name of the web service.
    String region = "region_example"; // String | The region for which encrypted credential parameters are created.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    try {
      AsyncOperationStatus result = apiInstance.webServicesCreateRegionalProperties(resourceGroupName, webServiceName, region, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesCreateRegionalProperties");
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
| **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | |
| **webServiceName** | **String**| The name of the web service. | |
| **region** | **String**| The region for which encrypted credential parameters are created. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Internal use only. Used for SDK return values. |  -  |
| **202** | Accepted.  The response includes the Azure-AsyncOperation header. To get the progress of the operation, call the GET operation on the URL in the Azure-AsyncOperation header field. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  -  |

<a id="webServicesGet"></a>
# **webServicesGet**
> WebService webServicesGet(resourceGroupName, webServiceName, apiVersion, subscriptionId, region)



Gets the Web Service Definition as specified by a subscription, resource group, and name. Note that the storage credentials and web service keys are not returned by this call. To get the web service access keys, call List Keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
    String webServiceName = "webServiceName_example"; // String | The name of the web service.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String region = "region_example"; // String | The region for which encrypted credential parameters are valid.
    try {
      WebService result = apiInstance.webServicesGet(resourceGroupName, webServiceName, apiVersion, subscriptionId, region);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesGet");
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
| **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | |
| **webServiceName** | **String**| The name of the web service. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **region** | **String**| The region for which encrypted credential parameters are valid. | [optional] |

### Return type

[**WebService**](WebService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success.  The response includes the Provisioning State and the Azure-AsyncOperation header. To get the progress of the operation, call GET operation on the URL in Azure-AsyncOperation header field. For more informationFor more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  -  |

<a id="webServicesListByResourceGroup"></a>
# **webServicesListByResourceGroup**
> PaginatedWebServicesList webServicesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $skiptoken)



Gets the web services in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String $skiptoken = "$skiptoken_example"; // String | Continuation token for pagination.
    try {
      PaginatedWebServicesList result = apiInstance.webServicesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesListByResourceGroup");
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
| **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **$skiptoken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**PaginatedWebServicesList**](PaginatedWebServicesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The response includes a paginated array of web service objects and a URI to the next set of results, if any. For the more information the limits of the number of items in a resource group, see https://azure.microsoft.com/en-us/documentation/articles/azure-subscription-service-limits/. Note that the web service objects are sparsely populated to conserve space in the response content. To get the full web service object, call the GET operation on the web service. |  -  |

<a id="webServicesListBySubscriptionId"></a>
# **webServicesListBySubscriptionId**
> PaginatedWebServicesList webServicesListBySubscriptionId(apiVersion, subscriptionId, $skiptoken)



Gets the web services in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String $skiptoken = "$skiptoken_example"; // String | Continuation token for pagination.
    try {
      PaginatedWebServicesList result = apiInstance.webServicesListBySubscriptionId(apiVersion, subscriptionId, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesListBySubscriptionId");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **$skiptoken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**PaginatedWebServicesList**](PaginatedWebServicesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The response includes a paginated array of web service objects and a URI to the next set of results, if any. Note that the web service objects are sparsely populated to conserve space in the response content. To get the full web service object, call the GET operation on the web service. |  -  |

<a id="webServicesListKeys"></a>
# **webServicesListKeys**
> WebServiceKeys webServicesListKeys(resourceGroupName, webServiceName, apiVersion, subscriptionId)



Gets the access keys for the specified web service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
    String webServiceName = "webServiceName_example"; // String | The name of the web service.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    try {
      WebServiceKeys result = apiInstance.webServicesListKeys(resourceGroupName, webServiceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesListKeys");
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
| **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | |
| **webServiceName** | **String**| The name of the web service. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |

### Return type

[**WebServiceKeys**](WebServiceKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |

<a id="webServicesPatch"></a>
# **webServicesPatch**
> WebService webServicesPatch(resourceGroupName, webServiceName, apiVersion, subscriptionId, patchPayload)



Modifies an existing web service resource. The PATCH API call is an asynchronous operation. To determine whether it has completed successfully, you must perform a Get operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
    String webServiceName = "webServiceName_example"; // String | The name of the web service.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    PatchedWebService patchPayload = new PatchedWebService(); // PatchedWebService | The payload to use to patch the web service.
    try {
      WebService result = apiInstance.webServicesPatch(resourceGroupName, webServiceName, apiVersion, subscriptionId, patchPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesPatch");
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
| **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | |
| **webServiceName** | **String**| The name of the web service. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **patchPayload** | [**PatchedWebService**](PatchedWebService.md)| The payload to use to patch the web service. | |

### Return type

[**WebService**](WebService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The response payload is identical to the response payload that is returned by the GET operation. The response includes the Provisioning State and the Azure-AsyncOperation header. To get the progress of the operation, call GET operation on the URL in Azure-AsyncOperation header field. For more information about Asynchronous Operations, see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-async-operations. |  -  |

<a id="webServicesRemove"></a>
# **webServicesRemove**
> webServicesRemove(resourceGroupName, webServiceName, apiVersion, subscriptionId)



Deletes the specified web service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WebServicesApi apiInstance = new WebServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
    String webServiceName = "webServiceName_example"; // String | The name of the web service.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    try {
      apiInstance.webServicesRemove(resourceGroupName, webServiceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebServicesApi#webServicesRemove");
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
| **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | |
| **webServiceName** | **String**| The name of the web service. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. Note that a 202 status is returned even if the service did not exist. |  -  |
| **204** | No Content. |  -  |

