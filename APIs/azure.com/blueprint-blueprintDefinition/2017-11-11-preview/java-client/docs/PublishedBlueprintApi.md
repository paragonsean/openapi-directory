# PublishedBlueprintApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishedBlueprintsCreate**](PublishedBlueprintApi.md#publishedBlueprintsCreate) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} |  |
| [**publishedBlueprintsDelete**](PublishedBlueprintApi.md#publishedBlueprintsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} |  |
| [**publishedBlueprintsGet**](PublishedBlueprintApi.md#publishedBlueprintsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} |  |
| [**publishedBlueprintsList**](PublishedBlueprintApi.md#publishedBlueprintsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions |  |


<a id="publishedBlueprintsCreate"></a>
# **publishedBlueprintsCreate**
> PublishedBlueprint publishedBlueprintsCreate(apiVersion, managementGroupName, blueprintName, versionId)



Publish a new version of the Blueprint with the latest artifacts. Published Blueprints are immutable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishedBlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublishedBlueprintApi apiInstance = new PublishedBlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String versionId = "versionId_example"; // String | version of the published blueprint.
    try {
      PublishedBlueprint result = apiInstance.publishedBlueprintsCreate(apiVersion, managementGroupName, blueprintName, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishedBlueprintApi#publishedBlueprintsCreate");
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created -- published Blueprint. |  -  |

<a id="publishedBlueprintsDelete"></a>
# **publishedBlueprintsDelete**
> PublishedBlueprint publishedBlueprintsDelete(apiVersion, managementGroupName, blueprintName, versionId)



Delete a published Blueprint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishedBlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublishedBlueprintApi apiInstance = new PublishedBlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String versionId = "versionId_example"; // String | version of the published blueprint.
    try {
      PublishedBlueprint result = apiInstance.publishedBlueprintsDelete(apiVersion, managementGroupName, blueprintName, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishedBlueprintApi#publishedBlueprintsDelete");
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- published Blueprint deleted. |  -  |
| **204** | No Content |  -  |

<a id="publishedBlueprintsGet"></a>
# **publishedBlueprintsGet**
> PublishedBlueprint publishedBlueprintsGet(apiVersion, managementGroupName, blueprintName, versionId)



Get a published Blueprint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishedBlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublishedBlueprintApi apiInstance = new PublishedBlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    String versionId = "versionId_example"; // String | version of the published blueprint.
    try {
      PublishedBlueprint result = apiInstance.publishedBlueprintsGet(apiVersion, managementGroupName, blueprintName, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishedBlueprintApi#publishedBlueprintsGet");
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- published Blueprint retrieved. |  -  |

<a id="publishedBlueprintsList"></a>
# **publishedBlueprintsList**
> PublishedBlueprintList publishedBlueprintsList(apiVersion, managementGroupName, blueprintName)



List published versions of given Blueprint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishedBlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublishedBlueprintApi apiInstance = new PublishedBlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    try {
      PublishedBlueprintList result = apiInstance.publishedBlueprintsList(apiVersion, managementGroupName, blueprintName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishedBlueprintApi#publishedBlueprintsList");
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

[**PublishedBlueprintList**](PublishedBlueprintList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- all published Blueprint retrieved. |  -  |

