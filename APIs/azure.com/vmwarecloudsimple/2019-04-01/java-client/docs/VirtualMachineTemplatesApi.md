# VirtualMachineTemplatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineTemplatesGet**](VirtualMachineTemplatesApi.md#virtualMachineTemplatesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualMachineTemplates/{virtualMachineTemplateName} | Implements virtual machine template GET method |
| [**virtualMachineTemplatesList**](VirtualMachineTemplatesApi.md#virtualMachineTemplatesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualMachineTemplates | Implements list of available VM templates |


<a id="virtualMachineTemplatesGet"></a>
# **virtualMachineTemplatesGet**
> VirtualMachineTemplate virtualMachineTemplatesGet(subscriptionId, regionId, pcName, virtualMachineTemplateName, apiVersion)

Implements virtual machine template GET method

Returns virtual machine templates by its name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineTemplatesApi apiInstance = new VirtualMachineTemplatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String pcName = "pcName_example"; // String | The private cloud name
    String virtualMachineTemplateName = "virtualMachineTemplateName_example"; // String | virtual machine template id (vsphereId)
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VirtualMachineTemplate result = apiInstance.virtualMachineTemplatesGet(subscriptionId, regionId, pcName, virtualMachineTemplateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineTemplatesApi#virtualMachineTemplatesGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **pcName** | **String**| The private cloud name | |
| **virtualMachineTemplateName** | **String**| virtual machine template id (vsphereId) | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**VirtualMachineTemplate**](VirtualMachineTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="virtualMachineTemplatesList"></a>
# **virtualMachineTemplatesList**
> VirtualMachineTemplateListResponse virtualMachineTemplatesList(subscriptionId, apiVersion, pcName, regionId, resourcePoolName)

Implements list of available VM templates

Returns list of virtual machine templates in region for private cloud

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineTemplatesApi apiInstance = new VirtualMachineTemplatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String pcName = "pcName_example"; // String | The private cloud name
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String resourcePoolName = "resourcePoolName_example"; // String | Resource pool used to derive vSphere cluster which contains VM templates
    try {
      VirtualMachineTemplateListResponse result = apiInstance.virtualMachineTemplatesList(subscriptionId, apiVersion, pcName, regionId, resourcePoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineTemplatesApi#virtualMachineTemplatesList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **apiVersion** | **String**| Client API version. | |
| **pcName** | **String**| The private cloud name | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **resourcePoolName** | **String**| Resource pool used to derive vSphere cluster which contains VM templates | |

### Return type

[**VirtualMachineTemplateListResponse**](VirtualMachineTemplateListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

