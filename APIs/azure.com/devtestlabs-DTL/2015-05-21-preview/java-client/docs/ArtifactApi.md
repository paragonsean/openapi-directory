# ArtifactApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artifactGenerateArmTemplate**](ArtifactApi.md#artifactGenerateArmTemplate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name}/generateArmTemplate |  |
| [**artifactGetResource**](ArtifactApi.md#artifactGetResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts/{name} |  |
| [**artifactList**](ArtifactApi.md#artifactList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/artifactsources/{artifactSourceName}/artifacts |  |


<a id="artifactGenerateArmTemplate"></a>
# **artifactGenerateArmTemplate**
> ArmTemplateInfo artifactGenerateArmTemplate(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, generateArmTemplateRequest)



Generates an ARM template for the given artifact, uploads the required files to a storage account, and validates the generated artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
    String name = "name_example"; // String | The name of the artifact.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    GenerateArmTemplateRequest generateArmTemplateRequest = new GenerateArmTemplateRequest(); // GenerateArmTemplateRequest | 
    try {
      ArmTemplateInfo result = apiInstance.artifactGenerateArmTemplate(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion, generateArmTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactGenerateArmTemplate");
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
| **name** | **String**| The name of the artifact. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **generateArmTemplateRequest** | [**GenerateArmTemplateRequest**](GenerateArmTemplateRequest.md)|  | |

### Return type

[**ArmTemplateInfo**](ArmTemplateInfo.md)

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

<a id="artifactGetResource"></a>
# **artifactGetResource**
> Artifact artifactGetResource(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion)



Get artifact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
    String name = "name_example"; // String | The name of the artifact.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    try {
      Artifact result = apiInstance.artifactGetResource(subscriptionId, resourceGroupName, labName, artifactSourceName, name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactGetResource");
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
| **name** | **String**| The name of the artifact. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |

### Return type

[**Artifact**](Artifact.md)

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

<a id="artifactList"></a>
# **artifactList**
> ResponseWithContinuationArtifact artifactList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, $filter, $top, $orderBy)



List artifacts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String artifactSourceName = "artifactSourceName_example"; // String | The name of the artifact source.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $orderBy = "$orderBy_example"; // String | 
    try {
      ResponseWithContinuationArtifact result = apiInstance.artifactList(subscriptionId, resourceGroupName, labName, artifactSourceName, apiVersion, $filter, $top, $orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactList");
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
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$orderBy** | **String**|  | [optional] |

### Return type

[**ResponseWithContinuationArtifact**](ResponseWithContinuationArtifact.md)

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

