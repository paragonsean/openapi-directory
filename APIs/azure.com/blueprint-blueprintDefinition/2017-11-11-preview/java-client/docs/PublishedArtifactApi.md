# PublishedArtifactApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishedArtifactsGet**](PublishedArtifactApi.md#publishedArtifactsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts/{artifactName} |  |
| [**publishedArtifactsList**](PublishedArtifactApi.md#publishedArtifactsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts |  |


<a id="publishedArtifactsGet"></a>
# **publishedArtifactsGet**
> Artifact publishedArtifactsGet(apiVersion, managementGroupName, blueprintName, versionId, artifactName)



Get an artifact for a published Blueprint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishedArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublishedArtifactApi apiInstance = new PublishedArtifactApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String versionId = "versionId_example"; // String | version of the published blueprint.
    String artifactName = "artifactName_example"; // String | name of the artifact.
    try {
      Artifact result = apiInstance.publishedArtifactsGet(apiVersion, managementGroupName, blueprintName, versionId, artifactName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishedArtifactApi#publishedArtifactsGet");
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
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |
| **versionId** | **String**| version of the published blueprint. | |
| **artifactName** | **String**| name of the artifact. | |

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- published artifact retrieved. |  -  |

<a id="publishedArtifactsList"></a>
# **publishedArtifactsList**
> ArtifactList publishedArtifactsList(apiVersion, managementGroupName, blueprintName, versionId)



List artifacts for a published Blueprint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishedArtifactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublishedArtifactApi apiInstance = new PublishedArtifactApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String versionId = "versionId_example"; // String | version of the published blueprint.
    try {
      ArtifactList result = apiInstance.publishedArtifactsList(apiVersion, managementGroupName, blueprintName, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishedArtifactApi#publishedArtifactsList");
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
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |
| **versionId** | **String**| version of the published blueprint. | |

### Return type

[**ArtifactList**](ArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- all published artifact retrieved. |  -  |

