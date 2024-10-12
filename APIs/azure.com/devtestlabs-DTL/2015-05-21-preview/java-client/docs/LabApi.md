# LabApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**labCreateEnvironment**](LabApi.md#labCreateEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name}/createEnvironment |  |
| [**labCreateOrUpdateResource**](LabApi.md#labCreateOrUpdateResource) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name} |  |
| [**labDeleteResource**](LabApi.md#labDeleteResource) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name} |  |
| [**labGenerateUploadUri**](LabApi.md#labGenerateUploadUri) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name}/generateUploadUri |  |
| [**labGetResource**](LabApi.md#labGetResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name} |  |
| [**labListByResourceGroup**](LabApi.md#labListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs |  |
| [**labListBySubscription**](LabApi.md#labListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DevTestLab/labs |  |
| [**labListVhds**](LabApi.md#labListVhds) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name}/listVhds |  |
| [**labPatchResource**](LabApi.md#labPatchResource) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{name} |  |


<a id="labCreateEnvironment"></a>
# **labCreateEnvironment**
> labCreateEnvironment(subscriptionId, resourceGroupName, name, apiVersion, labVirtualMachine)



Create virtual machines in a Lab. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String name = "name_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    LabVirtualMachine labVirtualMachine = new LabVirtualMachine(); // LabVirtualMachine | 
    try {
      apiInstance.labCreateEnvironment(subscriptionId, resourceGroupName, name, apiVersion, labVirtualMachine);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labCreateEnvironment");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **name** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **labVirtualMachine** | [**LabVirtualMachine**](LabVirtualMachine.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | BadRequest |  -  |

<a id="labCreateOrUpdateResource"></a>
# **labCreateOrUpdateResource**
> Lab labCreateOrUpdateResource(subscriptionId, resourceGroupName, name, apiVersion, lab)



Create or replace an existing Lab. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String name = "name_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    Lab lab = new Lab(); // Lab | 
    try {
      Lab result = apiInstance.labCreateOrUpdateResource(subscriptionId, resourceGroupName, name, apiVersion, lab);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labCreateOrUpdateResource");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **name** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **lab** | [**Lab**](Lab.md)|  | |

### Return type

[**Lab**](Lab.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="labDeleteResource"></a>
# **labDeleteResource**
> labDeleteResource(subscriptionId, resourceGroupName, name, apiVersion)



Delete lab. This operation can take a while to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String name = "name_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    try {
      apiInstance.labDeleteResource(subscriptionId, resourceGroupName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labDeleteResource");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **name** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="labGenerateUploadUri"></a>
# **labGenerateUploadUri**
> GenerateUploadUriResponse labGenerateUploadUri(subscriptionId, resourceGroupName, name, apiVersion, generateUploadUriParameter)



Generate a URI for uploading custom disk images to a Lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String name = "name_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    GenerateUploadUriParameter generateUploadUriParameter = new GenerateUploadUriParameter(); // GenerateUploadUriParameter | 
    try {
      GenerateUploadUriResponse result = apiInstance.labGenerateUploadUri(subscriptionId, resourceGroupName, name, apiVersion, generateUploadUriParameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labGenerateUploadUri");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **name** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **generateUploadUriParameter** | [**GenerateUploadUriParameter**](GenerateUploadUriParameter.md)|  | |

### Return type

[**GenerateUploadUriResponse**](GenerateUploadUriResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labGetResource"></a>
# **labGetResource**
> Lab labGetResource(subscriptionId, resourceGroupName, name, apiVersion)



Get lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String name = "name_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    try {
      Lab result = apiInstance.labGetResource(subscriptionId, resourceGroupName, name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labGetResource");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **name** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |

### Return type

[**Lab**](Lab.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labListByResourceGroup"></a>
# **labListByResourceGroup**
> ResponseWithContinuationLab labListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $orderBy)



List labs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $orderBy = "$orderBy_example"; // String | 
    try {
      ResponseWithContinuationLab result = apiInstance.labListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$orderBy** | **String**|  | [optional] |

### Return type

[**ResponseWithContinuationLab**](ResponseWithContinuationLab.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labListBySubscription"></a>
# **labListBySubscription**
> ResponseWithContinuationLab labListBySubscription(subscriptionId, apiVersion, $filter, $top, $orderBy)



List labs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $orderBy = "$orderBy_example"; // String | 
    try {
      ResponseWithContinuationLab result = apiInstance.labListBySubscription(subscriptionId, apiVersion, $filter, $top, $orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labListBySubscription");
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
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$orderBy** | **String**|  | [optional] |

### Return type

[**ResponseWithContinuationLab**](ResponseWithContinuationLab.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labListVhds"></a>
# **labListVhds**
> ResponseWithContinuationLabVhd labListVhds(subscriptionId, resourceGroupName, name, apiVersion)



List disk images available for custom image creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String name = "name_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    try {
      ResponseWithContinuationLabVhd result = apiInstance.labListVhds(subscriptionId, resourceGroupName, name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labListVhds");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **name** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |

### Return type

[**ResponseWithContinuationLabVhd**](ResponseWithContinuationLabVhd.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labPatchResource"></a>
# **labPatchResource**
> Lab labPatchResource(subscriptionId, resourceGroupName, name, apiVersion, lab)



Modify properties of labs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LabApi apiInstance = new LabApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String name = "name_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    Lab lab = new Lab(); // Lab | 
    try {
      Lab result = apiInstance.labPatchResource(subscriptionId, resourceGroupName, name, apiVersion, lab);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabApi#labPatchResource");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **name** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **lab** | [**Lab**](Lab.md)|  | |

### Return type

[**Lab**](Lab.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

