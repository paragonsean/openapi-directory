# ArtifactApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artifactsCreateOrUpdate**](ArtifactApi.md#artifactsCreateOrUpdate) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} |  |
| [**artifactsDelete**](ArtifactApi.md#artifactsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} |  |
| [**artifactsGet**](ArtifactApi.md#artifactsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} |  |
| [**artifactsList**](ArtifactApi.md#artifactsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts |  |


<a id="artifactsCreateOrUpdate"></a>
# **artifactsCreateOrUpdate**
> Artifact artifactsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, artifactName, artifact)



Create or update Blueprint artifact.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String artifactName = "artifactName_example"; // String | name of the artifact.
    Artifact artifact = new Artifact(); // Artifact | Blueprint artifact to save.
    try {
      Artifact result = apiInstance.artifactsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, artifactName, artifact);
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |
| **artifactName** | **String**| name of the artifact. | |
| **artifact** | [**Artifact**](Artifact.md)| Blueprint artifact to save. | |

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
| **201** | Created -- Blueprint artifact created/updated. |  -  |

<a id="artifactsDelete"></a>
# **artifactsDelete**
> Artifact artifactsDelete(apiVersion, managementGroupName, blueprintName, artifactName)



Delete a Blueprint artifact.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String artifactName = "artifactName_example"; // String | name of the artifact.
    try {
      Artifact result = apiInstance.artifactsDelete(apiVersion, managementGroupName, blueprintName, artifactName);
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |
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
| **200** | OK -- Blueprint artifact deleted. |  -  |
| **204** | No Content |  -  |

<a id="artifactsGet"></a>
# **artifactsGet**
> Artifact artifactsGet(apiVersion, managementGroupName, blueprintName, artifactName)



Get a Blueprint artifact.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String artifactName = "artifactName_example"; // String | name of the artifact.
    try {
      Artifact result = apiInstance.artifactsGet(apiVersion, managementGroupName, blueprintName, artifactName);
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |
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
| **200** | OK -- Blueprint artifact retrieved. |  -  |

<a id="artifactsList"></a>
# **artifactsList**
> ArtifactList artifactsList(apiVersion, managementGroupName, blueprintName)



List artifacts for a given Blueprint.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    try {
      ArtifactList result = apiInstance.artifactsList(apiVersion, managementGroupName, blueprintName);
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |

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
| **200** | OK -- Blueprint artifacts retrieved. |  -  |

