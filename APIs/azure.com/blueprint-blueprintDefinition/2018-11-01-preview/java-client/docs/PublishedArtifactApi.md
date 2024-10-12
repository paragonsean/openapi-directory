# PublishedArtifactApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishedArtifactsGet**](PublishedArtifactApi.md#publishedArtifactsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts/{artifactName} |  |
| [**publishedArtifactsList**](PublishedArtifactApi.md#publishedArtifactsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts |  |


<a id="publishedArtifactsGet"></a>
# **publishedArtifactsGet**
> Artifact publishedArtifactsGet(apiVersion, scope, blueprintName, versionId, artifactName)



Get an artifact for a published blueprint definition.

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
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String versionId = "versionId_example"; // String | Version of the published blueprint definition.
    String artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
    try {
      Artifact result = apiInstance.publishedArtifactsGet(apiVersion, scope, blueprintName, versionId, artifactName);
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **blueprintName** | **String**| Name of the blueprint definition. | |
| **versionId** | **String**| Version of the published blueprint definition. | |
| **artifactName** | **String**| Name of the blueprint artifact. | |

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
| **200** | OK -- artifact of published blueprint definition retrieved. |  -  |

<a id="publishedArtifactsList"></a>
# **publishedArtifactsList**
> ArtifactList publishedArtifactsList(apiVersion, scope, blueprintName, versionId)



List artifacts for a version of a published blueprint definition.

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
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String versionId = "versionId_example"; // String | Version of the published blueprint definition.
    try {
      ArtifactList result = apiInstance.publishedArtifactsList(apiVersion, scope, blueprintName, versionId);
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **blueprintName** | **String**| Name of the blueprint definition. | |
| **versionId** | **String**| Version of the published blueprint definition. | |

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
| **200** | OK -- artifacts of a version of published blueprint definition retrieved. |  -  |

