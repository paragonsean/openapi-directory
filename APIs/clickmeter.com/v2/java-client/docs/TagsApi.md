# TagsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tagsCount**](TagsApi.md#tagsCount) | **GET** /tags/count | List of all the groups associated to the user filtered by this tag. |
| [**tagsDelete**](TagsApi.md#tagsDelete) | **DELETE** /tags/{tagId} | Delete a tag |
| [**tagsDeleteRelatedDatapoints**](TagsApi.md#tagsDeleteRelatedDatapoints) | **DELETE** /tags/{tagId}/datapoints | Delete the association of this tag with all datapoints |
| [**tagsDeleteRelatedGroups**](TagsApi.md#tagsDeleteRelatedGroups) | **DELETE** /tags/{tagId}/groups | Delete the association of this tag with all groups |
| [**tagsGet**](TagsApi.md#tagsGet) | **GET** /tags | List of all the groups associated to the user filtered by this tag. |
| [**tagsGetDatapoints**](TagsApi.md#tagsGetDatapoints) | **GET** /tags/{tagId}/datapoints | List of all the datapoints associated to the user filtered by this tag |
| [**tagsGetDatapointsCount**](TagsApi.md#tagsGetDatapointsCount) | **GET** /tags/{tagId}/datapoints/count | Count the datapoints associated to the user filtered by this tag |
| [**tagsGetGroups**](TagsApi.md#tagsGetGroups) | **GET** /tags/{tagId}/groups | List of all the groups associated to the user filtered by this tag. |
| [**tagsGetGroupsCount**](TagsApi.md#tagsGetGroupsCount) | **GET** /tags/{tagId}/groups/count | Count the groups associated to the user filtered by this tag |
| [**tagsPatchDataPoint**](TagsApi.md#tagsPatchDataPoint) | **PUT** /tags/{tagId}/datapoints/patch | Associate/Deassociate a tag with a datapoint |
| [**tagsPatchGroup**](TagsApi.md#tagsPatchGroup) | **PUT** /tags/{tagId}/groups/patch | Associate/Deassociate a tag with a group |
| [**tagsPatchTagName**](TagsApi.md#tagsPatchTagName) | **PUT** /tags/{tagId}/name | Fast patch a tag name |
| [**tagsPut**](TagsApi.md#tagsPut) | **POST** /tags | Create a tag |
| [**tagsTagIdGet**](TagsApi.md#tagsTagIdGet) | **GET** /tags/{tagId} | Retrieve a tag |


<a id="tagsCount"></a>
# **tagsCount**
> Object tagsCount(name, datapoints, groups, type)

List of all the groups associated to the user filtered by this tag.

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String name = "name_example"; // String | Name of the tag
    String datapoints = "datapoints_example"; // String | Comma separated list of datapoints id to filter by
    String groups = "groups_example"; // String | Comma separated list of groups id to filter by
    String type = "tp"; // String | Type of entity related to the tag
    try {
      Object result = apiInstance.tagsCount(name, datapoints, groups, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsCount");
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
| **name** | **String**| Name of the tag | [optional] |
| **datapoints** | **String**| Comma separated list of datapoints id to filter by | [optional] |
| **groups** | **String**| Comma separated list of groups id to filter by | [optional] |
| **type** | **String**| Type of entity related to the tag | [optional] [enum: tp, tl, dp, gr] |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsDelete"></a>
# **tagsDelete**
> Object tagsDelete(tagId)

Delete a tag

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag
    try {
      Object result = apiInstance.tagsDelete(tagId);
      System.out.println(result);
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
| **tagId** | **Long**| Id of the tag | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsDeleteRelatedDatapoints"></a>
# **tagsDeleteRelatedDatapoints**
> ApiCoreResponsesEntityUriSystemInt64 tagsDeleteRelatedDatapoints(tagId)

Delete the association of this tag with all datapoints

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsDeleteRelatedDatapoints(tagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsDeleteRelatedDatapoints");
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
| **tagId** | **Long**| Id of the tag | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsDeleteRelatedGroups"></a>
# **tagsDeleteRelatedGroups**
> ApiCoreResponsesEntityUriSystemInt64 tagsDeleteRelatedGroups(tagId)

Delete the association of this tag with all groups

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsDeleteRelatedGroups(tagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsDeleteRelatedGroups");
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
| **tagId** | **Long**| Id of the tag | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsGet"></a>
# **tagsGet**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 tagsGet(offset, limit, name, datapoints, groups, type)

List of all the groups associated to the user filtered by this tag.

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Integer offset = 0; // Integer | Where to start when retrieving elements. Default is 0 if not specified.
    Integer limit = 20; // Integer | Maximum elements to retrieve. Default to 20 if not specified.
    String name = "name_example"; // String | Name of the tag
    String datapoints = "datapoints_example"; // String | Comma separated list of datapoints id to filter by
    String groups = "groups_example"; // String | Comma separated list of groups id to filter by
    String type = "tp"; // String | Type of entity related to the tag
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsGet(offset, limit, name, datapoints, groups, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGet");
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
| **offset** | **Integer**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0] |
| **limit** | **Integer**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20] |
| **name** | **String**| Name of the tag | [optional] |
| **datapoints** | **String**| Comma separated list of datapoints id to filter by | [optional] |
| **groups** | **String**| Comma separated list of groups id to filter by | [optional] |
| **type** | **String**| Type of entity related to the tag | [optional] [enum: tp, tl, dp, gr] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsGetDatapoints"></a>
# **tagsGetDatapoints**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 tagsGetDatapoints(tagId, offset, limit, type, status, textSearch, createdAfter, createdBefore)

List of all the datapoints associated to the user filtered by this tag

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag.
    Integer offset = 0; // Integer | Where to start when retrieving elements. Default is 0 if not specified.
    Integer limit = 20; // Integer | Maximum elements to retrieve. Default to 20 if not specified.
    String type = "tp"; // String | Type of the datapoint (\"tp\"/\"tl\")
    String status = "deleted"; // String | Status of the datapoint
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsGetDatapoints(tagId, offset, limit, type, status, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGetDatapoints");
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
| **tagId** | **Long**| Id of the tag. | |
| **offset** | **Integer**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0] |
| **limit** | **Integer**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20] |
| **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] [enum: tp, tl] |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active, paused, spam] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsGetDatapointsCount"></a>
# **tagsGetDatapointsCount**
> ApiCoreResponsesCountResponce tagsGetDatapointsCount(tagId, type, status, textSearch, createdAfter, createdBefore)

Count the datapoints associated to the user filtered by this tag

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag.
    String type = "tp"; // String | Type of the datapoint (\"tp\"/\"tl\")
    String status = "deleted"; // String | Status of the datapoint
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesCountResponce result = apiInstance.tagsGetDatapointsCount(tagId, type, status, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGetDatapointsCount");
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
| **tagId** | **Long**| Id of the tag. | |
| **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] [enum: tp, tl] |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active, paused, spam] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsGetGroups"></a>
# **tagsGetGroups**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 tagsGetGroups(tagId, offset, limit, status, textSearch, createdAfter, createdBefore)

List of all the groups associated to the user filtered by this tag.

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag.
    Integer offset = 0; // Integer | Where to start when retrieving elements. Default is 0 if not specified.
    Integer limit = 20; // Integer | Maximum elements to retrieve. Default to 20 if not specified.
    String status = "deleted"; // String | Status of the datapoint
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude groups created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude groups created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsGetGroups(tagId, offset, limit, status, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGetGroups");
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
| **tagId** | **Long**| Id of the tag. | |
| **offset** | **Integer**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0] |
| **limit** | **Integer**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20] |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsGetGroupsCount"></a>
# **tagsGetGroupsCount**
> ApiCoreResponsesCountResponce tagsGetGroupsCount(tagId, status, textSearch, createdAfter, createdBefore)

Count the groups associated to the user filtered by this tag

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag.
    String status = "deleted"; // String | Status of the datapoint
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude groups created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude groups created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesCountResponce result = apiInstance.tagsGetGroupsCount(tagId, status, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGetGroupsCount");
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
| **tagId** | **Long**| Id of the tag. | |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsPatchDataPoint"></a>
# **tagsPatchDataPoint**
> ApiCoreResponsesEntityUriSystemInt64 tagsPatchDataPoint(tagId, apiCoreRequestsPatchBody)

Associate/Deassociate a tag with a datapoint

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag
    ApiCoreRequestsPatchBody apiCoreRequestsPatchBody = new ApiCoreRequestsPatchBody(); // ApiCoreRequestsPatchBody | The body patch
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsPatchDataPoint(tagId, apiCoreRequestsPatchBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsPatchDataPoint");
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
| **tagId** | **Long**| Id of the tag | |
| **apiCoreRequestsPatchBody** | [**ApiCoreRequestsPatchBody**](ApiCoreRequestsPatchBody.md)| The body patch | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsPatchGroup"></a>
# **tagsPatchGroup**
> ApiCoreResponsesEntityUriSystemInt64 tagsPatchGroup(tagId, apiCoreRequestsPatchBody)

Associate/Deassociate a tag with a group

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag
    ApiCoreRequestsPatchBody apiCoreRequestsPatchBody = new ApiCoreRequestsPatchBody(); // ApiCoreRequestsPatchBody | The body patch
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsPatchGroup(tagId, apiCoreRequestsPatchBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsPatchGroup");
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
| **tagId** | **Long**| Id of the tag | |
| **apiCoreRequestsPatchBody** | [**ApiCoreRequestsPatchBody**](ApiCoreRequestsPatchBody.md)| The body patch | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsPatchTagName"></a>
# **tagsPatchTagName**
> ApiCoreResponsesEntityUriSystemInt64 tagsPatchTagName(tagId, apiCoreRequestsGenericTextPatch)

Fast patch a tag name

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag
    ApiCoreRequestsGenericTextPatch apiCoreRequestsGenericTextPatch = new ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | The body patch
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsPatchTagName(tagId, apiCoreRequestsGenericTextPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsPatchTagName");
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
| **tagId** | **Long**| Id of the tag | |
| **apiCoreRequestsGenericTextPatch** | [**ApiCoreRequestsGenericTextPatch**](ApiCoreRequestsGenericTextPatch.md)| The body patch | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsPut"></a>
# **tagsPut**
> ApiCoreResponsesEntityUriSystemInt64 tagsPut(apiCoreDtoTagsTag)

Create a tag

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    ApiCoreDtoTagsTag apiCoreDtoTagsTag = new ApiCoreDtoTagsTag(); // ApiCoreDtoTagsTag | The body of the tag
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.tagsPut(apiCoreDtoTagsTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsPut");
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
| **apiCoreDtoTagsTag** | [**ApiCoreDtoTagsTag**](ApiCoreDtoTagsTag.md)| The body of the tag | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="tagsTagIdGet"></a>
# **tagsTagIdGet**
> ApiCoreDtoTagsTag tagsTagIdGet(tagId)

Retrieve a tag

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long tagId = 56L; // Long | Id of the tag
    try {
      ApiCoreDtoTagsTag result = apiInstance.tagsTagIdGet(tagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsTagIdGet");
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
| **tagId** | **Long**| Id of the tag | |

### Return type

[**ApiCoreDtoTagsTag**](ApiCoreDtoTagsTag.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

