# GetApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dpsCertificateGet**](GetApi.md#dpsCertificateGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName} |  |
| [**dpsCertificateList**](GetApi.md#dpsCertificateList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates |  |
| [**iotDpsResourceGet**](GetApi.md#iotDpsResourceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} | Get the non-security related metadata of the provisioning service. |
| [**iotDpsResourceGetOperationResult**](GetApi.md#iotDpsResourceGetOperationResult) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/operationresults/{operationId} |  |
| [**iotDpsResourceListByResourceGroup**](GetApi.md#iotDpsResourceListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices |  |
| [**iotDpsResourceListBySubscription**](GetApi.md#iotDpsResourceListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/provisioningServices | Get all the provisioning services in a subscription. |
| [**iotDpsResourceListValidSkus**](GetApi.md#iotDpsResourceListValidSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/skus | Get the list of valid SKUs for a provisioning service. |


<a id="dpsCertificateGet"></a>
# **dpsCertificateGet**
> CertificateResponse dpsCertificateGet(certificateName, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, ifMatch)



Get the certificate from the provisioning service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String certificateName = "certificateName_example"; // String | Name of the certificate to retrieve.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of the provisioning service the certificate is associated with.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String ifMatch = "ifMatch_example"; // String | ETag of the certificate.
    try {
      CertificateResponse result = apiInstance.dpsCertificateGet(certificateName, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#dpsCertificateGet");
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
| **certificateName** | **String**| Name of the certificate to retrieve. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Resource group identifier. | |
| **provisioningServiceName** | **String**| Name of the provisioning service the certificate is associated with. | |
| **apiVersion** | **String**| The version of the API. | |
| **ifMatch** | **String**| ETag of the certificate. | [optional] |

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadata for the specified certificate. |  -  |
| **0** | Default error response. |  -  |

<a id="dpsCertificateList"></a>
# **dpsCertificateList**
> CertificateListDescription dpsCertificateList(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion)



Get all the certificates tied to the provisioning service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group.
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to retrieve certificates for.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      CertificateListDescription result = apiInstance.dpsCertificateList(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#dpsCertificateList");
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
| **resourceGroupName** | **String**| Name of resource group. | |
| **provisioningServiceName** | **String**| Name of provisioning service to retrieve certificates for. | |
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**CertificateListDescription**](CertificateListDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of certificate descriptions in a JSON-serialized array. |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceGet"></a>
# **iotDpsResourceGet**
> ProvisioningServiceDescription iotDpsResourceGet(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)

Get the non-security related metadata of the provisioning service.

Get the metadata of the provisioning service without SAS keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of the provisioning service to retrieve.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      ProvisioningServiceDescription result = apiInstance.iotDpsResourceGet(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotDpsResourceGet");
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
| **provisioningServiceName** | **String**| Name of the provisioning service to retrieve. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Provisioning service description with no keys is included in the response. |  -  |
| **0** | Default error response |  -  |

<a id="iotDpsResourceGetOperationResult"></a>
# **iotDpsResourceGetOperationResult**
> AsyncOperationResult iotDpsResourceGetOperationResult(operationId, subscriptionId, resourceGroupName, provisioningServiceName, asyncinfo, apiVersion)



Gets the status of a long running operation, such as create, update or delete a provisioning service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String operationId = "operationId_example"; // String | Operation id corresponding to long running operation. Use this to poll for the status.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service that the operation is running on.
    String asyncinfo = "true"; // String | Async header used to poll on the status of the operation, obtained while creating the long running operation.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      AsyncOperationResult result = apiInstance.iotDpsResourceGetOperationResult(operationId, subscriptionId, resourceGroupName, provisioningServiceName, asyncinfo, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotDpsResourceGetOperationResult");
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
| **operationId** | **String**| Operation id corresponding to long running operation. Use this to poll for the status. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Resource group identifier. | |
| **provisioningServiceName** | **String**| Name of provisioning service that the operation is running on. | |
| **asyncinfo** | **String**| Async header used to poll on the status of the operation, obtained while creating the long running operation. | [default to true] |
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**AsyncOperationResult**](AsyncOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The status of the long running operation. |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceListByResourceGroup"></a>
# **iotDpsResourceListByResourceGroup**
> ProvisioningServiceDescriptionListResult iotDpsResourceListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get a list of all provisioning services in the given resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      ProvisioningServiceDescriptionListResult result = apiInstance.iotDpsResourceListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotDpsResourceListByResourceGroup");
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
| **resourceGroupName** | **String**| Resource group identifier. | |
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**ProvisioningServiceDescriptionListResult**](ProvisioningServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of provisioning services in the resource group. |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceListBySubscription"></a>
# **iotDpsResourceListBySubscription**
> ProvisioningServiceDescriptionListResult iotDpsResourceListBySubscription(subscriptionId, apiVersion)

Get all the provisioning services in a subscription.

List all the provisioning services for a given subscription id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      ProvisioningServiceDescriptionListResult result = apiInstance.iotDpsResourceListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotDpsResourceListBySubscription");
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
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**ProvisioningServiceDescriptionListResult**](ProvisioningServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the metadata from all the provisioning services in the subscription. |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceListValidSkus"></a>
# **iotDpsResourceListValidSkus**
> IotDpsSkuDefinitionListResult iotDpsResourceListValidSkus(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)

Get the list of valid SKUs for a provisioning service.

Gets the list of valid SKUs and tiers for a provisioning service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      IotDpsSkuDefinitionListResult result = apiInstance.iotDpsResourceListValidSkus(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#iotDpsResourceListValidSkus");
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
| **provisioningServiceName** | **String**| Name of provisioning service. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Name of resource group. | |
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**IotDpsSkuDefinitionListResult**](IotDpsSkuDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of the valid SKUs for this provisioning service. |  -  |
| **0** | Default error response. |  -  |

