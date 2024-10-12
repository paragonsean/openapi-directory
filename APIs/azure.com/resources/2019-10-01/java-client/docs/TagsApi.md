# TagsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tagsCreateOrUpdate**](TagsApi.md#tagsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/tagNames/{tagName} | Creates a predefined tag name. |
| [**tagsCreateOrUpdateAtScope**](TagsApi.md#tagsCreateOrUpdateAtScope) | **PUT** /{scope}/providers/Microsoft.Resources/tags/default | Creates or updates the entire set of tags on a resource or subscription. |
| [**tagsCreateOrUpdateValue**](TagsApi.md#tagsCreateOrUpdateValue) | **PUT** /subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue} | Creates a predefined value for a predefined tag name. |
| [**tagsDelete**](TagsApi.md#tagsDelete) | **DELETE** /subscriptions/{subscriptionId}/tagNames/{tagName} | Deletes a predefined tag name. |
| [**tagsDeleteAtScope**](TagsApi.md#tagsDeleteAtScope) | **DELETE** /{scope}/providers/Microsoft.Resources/tags/default | Deletes the entire set of tags on a resource or subscription. |
| [**tagsDeleteValue**](TagsApi.md#tagsDeleteValue) | **DELETE** /subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue} | Deletes a predefined tag value for a predefined tag name. |
| [**tagsGetAtScope**](TagsApi.md#tagsGetAtScope) | **GET** /{scope}/providers/Microsoft.Resources/tags/default | Gets the entire set of tags on a resource or subscription. |
| [**tagsList**](TagsApi.md#tagsList) | **GET** /subscriptions/{subscriptionId}/tagNames | Gets a summary of tag usage under the subscription. |
| [**tagsUpdateAtScope**](TagsApi.md#tagsUpdateAtScope) | **PATCH** /{scope}/providers/Microsoft.Resources/tags/default | Selectively updates the set of tags on a resource or subscription. |


<a id="tagsCreateOrUpdate"></a>
# **tagsCreateOrUpdate**
> TagDetails tagsCreateOrUpdate(tagName, apiVersion, subscriptionId)

Creates a predefined tag name.

This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: &#39;microsoft&#39;, &#39;azure&#39;, &#39;windows&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String tagName = "tagName_example"; // String | The name of the tag to create.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      TagDetails result = apiInstance.tagsCreateOrUpdate(tagName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsCreateOrUpdate");
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
| **tagName** | **String**| The name of the tag to create. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**TagDetails**](TagDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Predefined tag name already exists. Returns information about the predefined tag name. |  -  |
| **201** | Predefined tag name successfully created. Returns information about the predefined tag name. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsCreateOrUpdateAtScope"></a>
# **tagsCreateOrUpdateAtScope**
> TagsResource tagsCreateOrUpdateAtScope(scope, apiVersion, parameters)

Creates or updates the entire set of tags on a resource or subscription.

This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String scope = "scope_example"; // String | The resource scope.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    TagsResource parameters = new TagsResource(); // TagsResource | 
    try {
      TagsResource result = apiInstance.tagsCreateOrUpdateAtScope(scope, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsCreateOrUpdateAtScope");
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
| **scope** | **String**| The resource scope. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**TagsResource**](TagsResource.md)|  | |

### Return type

[**TagsResource**](TagsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tags updated successfully. Returns tags from the specified object. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsCreateOrUpdateValue"></a>
# **tagsCreateOrUpdateValue**
> TagValue tagsCreateOrUpdateValue(tagName, tagValue, apiVersion, subscriptionId)

Creates a predefined value for a predefined tag name.

This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String tagName = "tagName_example"; // String | The name of the tag.
    String tagValue = "tagValue_example"; // String | The value of the tag to create.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      TagValue result = apiInstance.tagsCreateOrUpdateValue(tagName, tagValue, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsCreateOrUpdateValue");
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
| **tagName** | **String**| The name of the tag. | |
| **tagValue** | **String**| The value of the tag to create. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**TagValue**](TagValue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Predefined tag value already exists. Returns information about the predefined tag value. |  -  |
| **201** | Predefined tag value successfully created. Returns information about the predefined tag value. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsDelete"></a>
# **tagsDelete**
> tagsDelete(tagName, apiVersion, subscriptionId)

Deletes a predefined tag name.

This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String tagName = "tagName_example"; // String | The name of the tag.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.tagsDelete(tagName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsDelete");
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
| **tagName** | **String**| The name of the tag. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Predefined tag name successfully deleted. |  -  |
| **204** | Predefined tag name did not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsDeleteAtScope"></a>
# **tagsDeleteAtScope**
> tagsDeleteAtScope(scope, apiVersion)

Deletes the entire set of tags on a resource or subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String scope = "scope_example"; // String | The resource scope.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.tagsDeleteAtScope(scope, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsDeleteAtScope");
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
| **scope** | **String**| The resource scope. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tags successfully deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsDeleteValue"></a>
# **tagsDeleteValue**
> tagsDeleteValue(tagName, tagValue, apiVersion, subscriptionId)

Deletes a predefined tag value for a predefined tag name.

This operation allows deleting a value from the list of predefined values for an existing predefined tag name. The value being deleted must not be in use as a tag value for the given tag name for any resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String tagName = "tagName_example"; // String | The name of the tag.
    String tagValue = "tagValue_example"; // String | The value of the tag to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.tagsDeleteValue(tagName, tagValue, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsDeleteValue");
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
| **tagName** | **String**| The name of the tag. | |
| **tagValue** | **String**| The value of the tag to delete. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Predefined tag value successfully deleted. |  -  |
| **204** | Predefined tag value did not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsGetAtScope"></a>
# **tagsGetAtScope**
> TagsResource tagsGetAtScope(scope, apiVersion)

Gets the entire set of tags on a resource or subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String scope = "scope_example"; // String | The resource scope.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      TagsResource result = apiInstance.tagsGetAtScope(scope, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGetAtScope");
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
| **scope** | **String**| The resource scope. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**TagsResource**](TagsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns tags from the specified object. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsList"></a>
# **tagsList**
> TagsListResult tagsList(apiVersion, subscriptionId)

Gets a summary of tag usage under the subscription.

This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      TagsListResult result = apiInstance.tagsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**TagsListResult**](TagsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of tag names and values. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tagsUpdateAtScope"></a>
# **tagsUpdateAtScope**
> TagsResource tagsUpdateAtScope(scope, apiVersion, parameters)

Selectively updates the set of tags on a resource or subscription.

This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The &#39;replace&#39; option replaces the entire set of existing tags with a new set. The &#39;merge&#39; option allows adding tags with new names and updating the values of tags with existing names. The &#39;delete&#39; option allows selectively deleting tags based on given names or name/value pairs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String scope = "scope_example"; // String | The resource scope.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    TagsPatchResource parameters = new TagsPatchResource(); // TagsPatchResource | 
    try {
      TagsResource result = apiInstance.tagsUpdateAtScope(scope, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsUpdateAtScope");
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
| **scope** | **String**| The resource scope. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**TagsPatchResource**](TagsPatchResource.md)|  | |

### Return type

[**TagsResource**](TagsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tags updated successfully. Returns tags from the specified object. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

