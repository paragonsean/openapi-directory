# EntitiesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entitiesList**](EntitiesApi.md#entitiesList) | **POST** /providers/Microsoft.Management/getEntities |  |


<a id="entitiesList"></a>
# **entitiesList**
> EntityListResult entitiesList(apiVersion, $skiptoken, $skip, $top, $select, $search, $filter, $view, groupName, cacheControl)



List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    String $skiptoken = "$skiptoken_example"; // String | Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
    Integer $skip = 56; // Integer | Number of entities to skip over when retrieving results. Passing this in will override $skipToken.
    Integer $top = 56; // Integer | Number of elements to return when retrieving results. Passing this in will override $skipToken.
    String $select = "$select_example"; // String | This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. '$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain'. When specified the $select parameter can override select in $skipToken.
    String $search = "AllowedParents"; // String | The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. With $search=AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user's permissions.With $search=AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity.With $search=ParentAndFirstLevelChildren the API will return the parent and  first level of children that the user has either direct access to or indirect access via one of their descendants.With $search=ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group.With $search=ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter.  The user must have direct access to the children entities or one of it's descendants for it to show up in the results.
    String $filter = "$filter_example"; // String | The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq '{entityName}')  and you can check for substrings on either the name or display name fields(e.g. contains(name, '{substringToSearch}'), contains(displayName, '{substringToSearch')). Note that the '{entityName}' and '{substringToSearch}' fields are checked case insensitively.
    String $view = "FullHierarchy"; // String | The view parameter allows clients to filter the type of data that is returned by the getEntities call.
    String groupName = "groupName_example"; // String | A filter which allows the get entities call to focus on a particular group (i.e. \"$filter=name eq 'groupName'\")
    String cacheControl = "no-cache"; // String | Indicates that the request shouldn't utilize any caches.
    try {
      EntityListResult result = apiInstance.entitiesList(apiVersion, $skiptoken, $skip, $top, $select, $search, $filter, $view, groupName, cacheControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#entitiesList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | |
| **$skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$skip** | **Integer**| Number of entities to skip over when retrieving results. Passing this in will override $skipToken. | [optional] |
| **$top** | **Integer**| Number of elements to return when retrieving results. Passing this in will override $skipToken. | [optional] |
| **$select** | **String**| This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. &#39;$select&#x3D;Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain&#39;. When specified the $select parameter can override select in $skipToken. | [optional] |
| **$search** | **String**| The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. With $search&#x3D;AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user&#39;s permissions.With $search&#x3D;AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity.With $search&#x3D;ParentAndFirstLevelChildren the API will return the parent and  first level of children that the user has either direct access to or indirect access via one of their descendants.With $search&#x3D;ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group.With $search&#x3D;ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter.  The user must have direct access to the children entities or one of it&#39;s descendants for it to show up in the results. | [optional] [enum: AllowedParents, AllowedChildren, ParentAndFirstLevelChildren, ParentOnly, ChildrenOnly] |
| **$filter** | **String**| The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq &#39;{entityName}&#39;)  and you can check for substrings on either the name or display name fields(e.g. contains(name, &#39;{substringToSearch}&#39;), contains(displayName, &#39;{substringToSearch&#39;)). Note that the &#39;{entityName}&#39; and &#39;{substringToSearch}&#39; fields are checked case insensitively. | [optional] |
| **$view** | **String**| The view parameter allows clients to filter the type of data that is returned by the getEntities call. | [optional] [enum: FullHierarchy, GroupsOnly, SubscriptionsOnly, Audit] |
| **groupName** | **String**| A filter which allows the get entities call to focus on a particular group (i.e. \&quot;$filter&#x3D;name eq &#39;groupName&#39;\&quot;) | [optional] |
| **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to no-cache] |

### Return type

[**EntityListResult**](EntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

