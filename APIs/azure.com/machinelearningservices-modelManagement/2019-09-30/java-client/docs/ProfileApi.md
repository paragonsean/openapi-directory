# ProfileApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**profilesCreate**](ProfileApi.md#profilesCreate) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{imageId}/profiles | Create a Profile. |
| [**profilesListQuery**](ProfileApi.md#profilesListQuery) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{imageId}/profiles | Get a list of Image Profiles. |
| [**profilesQueryById**](ProfileApi.md#profilesQueryById) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/images/{imageId}/profiles/{id} | Get a Profile. |


<a id="profilesCreate"></a>
# **profilesCreate**
> profilesCreate(subscriptionId, resourceGroup, workspace, imageId, inputRequest)

Create a Profile.

Create a Profile for an Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String imageId = "imageId_example"; // String | The Image Id.
    ProfileRequestBase inputRequest = new ProfileRequestBase(); // ProfileRequestBase | The payload that is used to create the Profile.
    try {
      apiInstance.profilesCreate(subscriptionId, resourceGroup, workspace, imageId, inputRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#profilesCreate");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **imageId** | **String**| The Image Id. | |
| **inputRequest** | [**ProfileRequestBase**](ProfileRequestBase.md)| The payload that is used to create the Profile. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was accepted. The header &#39;Operation-Location&#39; contains the async operation location URL. Accessing this URL with a GET call will return the status of the background task. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="profilesListQuery"></a>
# **profilesListQuery**
> PaginatedProfileResponseList profilesListQuery(subscriptionId, resourceGroup, workspace, imageId, name, description, tags, properties, count, $skipToken, orderBy)

Get a list of Image Profiles.

If no filter is passed, the query lists all Profiles for the Image. The returned list is paginated and the count of items in each page is an optional parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String imageId = "imageId_example"; // String | The Image Id.
    String name = "name_example"; // String | The Profile name.
    String description = "description_example"; // String | The Profile description.
    String tags = "tags_example"; // String | A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
    String properties = "properties_example"; // String | A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
    Integer count = 56; // Integer | The number of items to retrieve in a page.
    String $skipToken = "$skipToken_example"; // String | The continuation token to retrieve the next page.
    String orderBy = "CreatedAtDesc"; // String | The option to order the response.
    try {
      PaginatedProfileResponseList result = apiInstance.profilesListQuery(subscriptionId, resourceGroup, workspace, imageId, name, description, tags, properties, count, $skipToken, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#profilesListQuery");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **imageId** | **String**| The Image Id. | |
| **name** | **String**| The Profile name. | [optional] |
| **description** | **String**| The Profile description. | [optional] |
| **tags** | **String**| A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3 | [optional] |
| **properties** | **String**| A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3 | [optional] |
| **count** | **Integer**| The number of items to retrieve in a page. | [optional] |
| **$skipToken** | **String**| The continuation token to retrieve the next page. | [optional] |
| **orderBy** | **String**| The option to order the response. | [optional] [default to CreatedAtDesc] [enum: CreatedAtDesc, CreatedAtAsc, UpdatedAtDesc, UpdatedAtAsc] |

### Return type

[**PaginatedProfileResponseList**](PaginatedProfileResponseList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="profilesQueryById"></a>
# **profilesQueryById**
> ProfileResponse profilesQueryById(subscriptionId, resourceGroup, workspace, imageId, id)

Get a Profile.

Get the Profile for an Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String imageId = "imageId_example"; // String | The Image Id.
    String id = "id_example"; // String | The Profile Id.
    try {
      ProfileResponse result = apiInstance.profilesQueryById(subscriptionId, resourceGroup, workspace, imageId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#profilesQueryById");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **imageId** | **String**| The Image Id. | |
| **id** | **String**| The Profile Id. | |

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |

