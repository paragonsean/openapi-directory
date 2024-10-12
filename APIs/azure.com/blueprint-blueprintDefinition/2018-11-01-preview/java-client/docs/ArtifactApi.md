# ArtifactApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artifactsCreateOrUpdate**](ArtifactApi.md#artifactsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} |  |
| [**artifactsDelete**](ArtifactApi.md#artifactsDelete) | **DELETE** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} |  |
| [**artifactsGet**](ArtifactApi.md#artifactsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} |  |
| [**artifactsList**](ArtifactApi.md#artifactsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts |  |


<a id="artifactsCreateOrUpdate"></a>
# **artifactsCreateOrUpdate**
> Artifact artifactsCreateOrUpdate(apiVersion, scope, blueprintName, artifactName, artifact)



Create or update blueprint artifact.

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
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
    Artifact artifact = new Artifact(); // Artifact | Blueprint artifact to create or update.
    try {
      Artifact result = apiInstance.artifactsCreateOrUpdate(apiVersion, scope, blueprintName, artifactName, artifact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsCreateOrUpdate");
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
| **artifactName** | **String**| Name of the blueprint artifact. | |
| **artifact** | [**Artifact**](Artifact.md)| Blueprint artifact to create or update. | |

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created -- blueprint artifact created/updated. |  -  |

<a id="artifactsDelete"></a>
# **artifactsDelete**
> Artifact artifactsDelete(apiVersion, scope, blueprintName, artifactName)



Delete a blueprint artifact.

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
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
    try {
      Artifact result = apiInstance.artifactsDelete(apiVersion, scope, blueprintName, artifactName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsDelete");
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
| **200** | OK -- blueprint artifact deleted. |  -  |
| **204** | No Content |  -  |

<a id="artifactsGet"></a>
# **artifactsGet**
> Artifact artifactsGet(apiVersion, scope, blueprintName, artifactName)



Get a blueprint artifact.

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
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
    try {
      Artifact result = apiInstance.artifactsGet(apiVersion, scope, blueprintName, artifactName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsGet");
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
| **200** | OK -- blueprint artifact retrieved. |  -  |

<a id="artifactsList"></a>
# **artifactsList**
> ArtifactList artifactsList(apiVersion, scope, blueprintName)



List artifacts for a given blueprint definition.

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
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ArtifactApi apiInstance = new ArtifactApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    try {
      ArtifactList result = apiInstance.artifactsList(apiVersion, scope, blueprintName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactApi#artifactsList");
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
| **200** | OK -- blueprint artifacts retrieved. |  -  |

