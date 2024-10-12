# ArmTemplatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**armTemplatesGet**](ArmTemplatesApi.md#armTemplatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/armtemplates/{name} |  |
| [**armTemplatesList**](ArmTemplatesApi.md#armTemplatesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/armtemplates |  |


<a id="armTemplatesGet"></a>
# **armTemplatesGet**
> ArmTemplate armTemplatesGet(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, $expand)



Get azure resource manager template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArmTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArmTemplatesApi apiInstance = new ArmTemplatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
    String name = "name_example"; // String | The name of the azure Resource Manager template.
    String apiVersion = "2016-05-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=displayName)'
    try {
      ArmTemplate result = apiInstance.armTemplatesGet(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArmTemplatesApi#armTemplatesGet");
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
| **labName** | **String**| The name of the lab. | |
| **artifactSourceName** | **String**| The name of the artifact source. | |
| **name** | **String**| The name of the azure Resource Manager template. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39; | [optional] |

### Return type

[**ArmTemplate**](ArmTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="armTemplatesList"></a>
# **armTemplatesList**
> ResponseWithContinuationArmTemplate armTemplatesList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, $expand, $filter, $top, $orderby)



List azure resource manager templates in a given artifact source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArmTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArmTemplatesApi apiInstance = new ArmTemplatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
    String apiVersion = "2016-05-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=displayName)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationArmTemplate result = apiInstance.armTemplatesList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArmTemplatesApi#armTemplatesList");
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
| **labName** | **String**| The name of the lab. | |
| **artifactSourceName** | **String**| The name of the artifact source. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationArmTemplate**](ResponseWithContinuationArmTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

