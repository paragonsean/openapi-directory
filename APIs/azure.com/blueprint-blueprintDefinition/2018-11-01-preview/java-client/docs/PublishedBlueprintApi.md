# PublishedBlueprintApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishedBlueprintsCreate**](PublishedBlueprintApi.md#publishedBlueprintsCreate) | **PUT** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} |  |
| [**publishedBlueprintsDelete**](PublishedBlueprintApi.md#publishedBlueprintsDelete) | **DELETE** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} |  |
| [**publishedBlueprintsGet**](PublishedBlueprintApi.md#publishedBlueprintsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} |  |
| [**publishedBlueprintsList**](PublishedBlueprintApi.md#publishedBlueprintsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions |  |


<a id="publishedBlueprintsCreate"></a>
# **publishedBlueprintsCreate**
> PublishedBlueprint publishedBlueprintsCreate(apiVersion, scope, blueprintName, versionId, publishedBlueprint)



Publish a new version of the blueprint definition with the latest artifacts. Published blueprint definitions are immutable.

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
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String versionId = "versionId_example"; // String | Version of the published blueprint definition.
    PublishedBlueprint publishedBlueprint = new PublishedBlueprint(); // PublishedBlueprint | Published Blueprint to create or update.
    try {
      PublishedBlueprint result = apiInstance.publishedBlueprintsCreate(apiVersion, scope, blueprintName, versionId, publishedBlueprint);
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **blueprintName** | **String**| Name of the blueprint definition. | |
| **versionId** | **String**| Version of the published blueprint definition. | |
| **publishedBlueprint** | [**PublishedBlueprint**](PublishedBlueprint.md)| Published Blueprint to create or update. | [optional] |

### Return type

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created -- blueprint definition published. |  -  |

<a id="publishedBlueprintsDelete"></a>
# **publishedBlueprintsDelete**
> PublishedBlueprint publishedBlueprintsDelete(apiVersion, scope, blueprintName, versionId)



Delete a published version of a blueprint definition.

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
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String versionId = "versionId_example"; // String | Version of the published blueprint definition.
    try {
      PublishedBlueprint result = apiInstance.publishedBlueprintsDelete(apiVersion, scope, blueprintName, versionId);
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **blueprintName** | **String**| Name of the blueprint definition. | |
| **versionId** | **String**| Version of the published blueprint definition. | |

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
| **200** | OK -- published version of blueprint definition deleted. |  -  |
| **204** | No Content |  -  |

<a id="publishedBlueprintsGet"></a>
# **publishedBlueprintsGet**
> PublishedBlueprint publishedBlueprintsGet(apiVersion, scope, blueprintName, versionId)



Get a published version of a blueprint definition.

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
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    String versionId = "versionId_example"; // String | Version of the published blueprint definition.
    try {
      PublishedBlueprint result = apiInstance.publishedBlueprintsGet(apiVersion, scope, blueprintName, versionId);
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **blueprintName** | **String**| Name of the blueprint definition. | |
| **versionId** | **String**| Version of the published blueprint definition. | |

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
| **200** | OK -- published blueprint definition retrieved. |  -  |

<a id="publishedBlueprintsList"></a>
# **publishedBlueprintsList**
> PublishedBlueprintList publishedBlueprintsList(apiVersion, scope, blueprintName)



List published versions of given blueprint definition.

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
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
    try {
      PublishedBlueprintList result = apiInstance.publishedBlueprintsList(apiVersion, scope, blueprintName);
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **blueprintName** | **String**| Name of the blueprint definition. | |

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
| **200** | OK -- all published versions of blueprint definition retrieved. |  -  |

