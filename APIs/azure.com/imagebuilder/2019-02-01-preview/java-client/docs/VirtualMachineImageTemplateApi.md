# VirtualMachineImageTemplateApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineImageTemplatesCreateOrUpdate**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} |  |
| [**virtualMachineImageTemplatesDelete**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} |  |
| [**virtualMachineImageTemplatesGet**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} |  |
| [**virtualMachineImageTemplatesGetRunOutput**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesGetRunOutput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/runOutputs/{runOutputName} |  |
| [**virtualMachineImageTemplatesList**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VirtualMachineImages/imageTemplates |  |
| [**virtualMachineImageTemplatesListByResourceGroup**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates |  |
| [**virtualMachineImageTemplatesListRunOutputs**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesListRunOutputs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/runOutputs |  |
| [**virtualMachineImageTemplatesRun**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/run |  |
| [**virtualMachineImageTemplatesUpdate**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} |  |


<a id="virtualMachineImageTemplatesCreateOrUpdate"></a>
# **virtualMachineImageTemplatesCreateOrUpdate**
> ImageTemplate virtualMachineImageTemplatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, parameters)



Create or update a virtual machine image template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
    ImageTemplate parameters = new ImageTemplate(); // ImageTemplate | Parameters supplied to the CreateImageTemplate operation
    try {
      ImageTemplate result = apiInstance.virtualMachineImageTemplatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **imageTemplateName** | **String**| The name of the image Template | |
| **parameters** | [**ImageTemplate**](ImageTemplate.md)| Parameters supplied to the CreateImageTemplate operation | |

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesDelete"></a>
# **virtualMachineImageTemplatesDelete**
> virtualMachineImageTemplatesDelete(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Delete a virtual machine image template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
    try {
      apiInstance.virtualMachineImageTemplatesDelete(apiVersion, subscriptionId, resourceGroupName, imageTemplateName);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **imageTemplateName** | **String**| The name of the image Template | |

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
| **200** | The operation was successful. |  -  |
| **202** | The operation will be completed asynchronously. |  -  |
| **204** | NoContent -- VM image template does not exist in the subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesGet"></a>
# **virtualMachineImageTemplatesGet**
> ImageTemplate virtualMachineImageTemplatesGet(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Get information about a virtual machine image template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
    try {
      ImageTemplate result = apiInstance.virtualMachineImageTemplatesGet(apiVersion, subscriptionId, resourceGroupName, imageTemplateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **imageTemplateName** | **String**| The name of the image Template | |

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesGetRunOutput"></a>
# **virtualMachineImageTemplatesGetRunOutput**
> RunOutput virtualMachineImageTemplatesGetRunOutput(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, runOutputName)



Get the specified run output for the specified image template resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
    String runOutputName = "runOutputName_example"; // String | The name of the run output
    try {
      RunOutput result = apiInstance.virtualMachineImageTemplatesGetRunOutput(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, runOutputName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesGetRunOutput");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **imageTemplateName** | **String**| The name of the image Template | |
| **runOutputName** | **String**| The name of the run output | |

### Return type

[**RunOutput**](RunOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesList"></a>
# **virtualMachineImageTemplatesList**
> ImageTemplateListResult virtualMachineImageTemplatesList(subscriptionId, apiVersion)



Gets information about the VM image templates associated with the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ImageTemplateListResult result = apiInstance.virtualMachineImageTemplatesList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ImageTemplateListResult**](ImageTemplateListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesListByResourceGroup"></a>
# **virtualMachineImageTemplatesListByResourceGroup**
> ImageTemplateListResult virtualMachineImageTemplatesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Gets information about the VM image templates associated with the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ImageTemplateListResult result = apiInstance.virtualMachineImageTemplatesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ImageTemplateListResult**](ImageTemplateListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesListRunOutputs"></a>
# **virtualMachineImageTemplatesListRunOutputs**
> RunOutputCollection virtualMachineImageTemplatesListRunOutputs(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



List all run outputs for the specified Image Template resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
    try {
      RunOutputCollection result = apiInstance.virtualMachineImageTemplatesListRunOutputs(apiVersion, subscriptionId, resourceGroupName, imageTemplateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesListRunOutputs");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **imageTemplateName** | **String**| The name of the image Template | |

### Return type

[**RunOutputCollection**](RunOutputCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesRun"></a>
# **virtualMachineImageTemplatesRun**
> virtualMachineImageTemplatesRun(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Create artifacts from a existing image template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
    try {
      apiInstance.virtualMachineImageTemplatesRun(apiVersion, subscriptionId, resourceGroupName, imageTemplateName);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesRun");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **imageTemplateName** | **String**| The name of the image Template | |

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
| **202** | The operation will be completed asynchronously. |  -  |
| **204** | The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="virtualMachineImageTemplatesUpdate"></a>
# **virtualMachineImageTemplatesUpdate**
> ImageTemplate virtualMachineImageTemplatesUpdate(subscriptionId, resourceGroupName, imageTemplateName, apiVersion, parameters)



Update the tags for this Virtual Machine Image Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineImageTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineImageTemplateApi apiInstance = new VirtualMachineImageTemplateApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ImageTemplateUpdateParameters parameters = new ImageTemplateUpdateParameters(); // ImageTemplateUpdateParameters | Additional parameters for Image Template update.
    try {
      ImageTemplate result = apiInstance.virtualMachineImageTemplatesUpdate(subscriptionId, resourceGroupName, imageTemplateName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineImageTemplateApi#virtualMachineImageTemplatesUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **imageTemplateName** | **String**| The name of the image Template | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**ImageTemplateUpdateParameters**](ImageTemplateUpdateParameters.md)| Additional parameters for Image Template update. | |

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

