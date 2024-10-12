# OpportunitiesApi

All URIs are relative to *https://esi.evetech.net/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCharactersCharacterIdOpportunities**](OpportunitiesApi.md#getCharactersCharacterIdOpportunities) | **GET** /characters/{character_id}/opportunities/ | Get a character&#39;s completed tasks |
| [**getOpportunitiesGroups**](OpportunitiesApi.md#getOpportunitiesGroups) | **GET** /opportunities/groups/ | Get opportunities groups |
| [**getOpportunitiesGroupsGroupId**](OpportunitiesApi.md#getOpportunitiesGroupsGroupId) | **GET** /opportunities/groups/{group_id}/ | Get opportunities group |
| [**getOpportunitiesTasks**](OpportunitiesApi.md#getOpportunitiesTasks) | **GET** /opportunities/tasks/ | Get opportunities tasks |
| [**getOpportunitiesTasksTaskId**](OpportunitiesApi.md#getOpportunitiesTasksTaskId) | **GET** /opportunities/tasks/{task_id}/ | Get opportunities task |


<a id="getCharactersCharacterIdOpportunities"></a>
# **getCharactersCharacterIdOpportunities**
> List&lt;GetCharactersCharacterIdOpportunities200Ok&gt; getCharactersCharacterIdOpportunities(characterId, datasource, ifNoneMatch, token)

Get a character&#39;s completed tasks

Return a list of tasks finished by a character  --- Alternate route: &#x60;/dev/characters/{character_id}/opportunities/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/opportunities/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/opportunities/&#x60;  --- This route is cached for up to 3600 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    OpportunitiesApi apiInstance = new OpportunitiesApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      List<GetCharactersCharacterIdOpportunities200Ok> result = apiInstance.getCharactersCharacterIdOpportunities(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunitiesApi#getCharactersCharacterIdOpportunities");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**List&lt;GetCharactersCharacterIdOpportunities200Ok&gt;**](GetCharactersCharacterIdOpportunities200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of opportunities task ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getOpportunitiesGroups"></a>
# **getOpportunitiesGroups**
> List&lt;Integer&gt; getOpportunitiesGroups(datasource, ifNoneMatch)

Get opportunities groups

Return a list of opportunities groups  --- Alternate route: &#x60;/dev/opportunities/groups/&#x60;  Alternate route: &#x60;/legacy/opportunities/groups/&#x60;  Alternate route: &#x60;/v1/opportunities/groups/&#x60;  --- This route expires daily at 11:05

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");

    OpportunitiesApi apiInstance = new OpportunitiesApi(defaultClient);
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    try {
      List<Integer> result = apiInstance.getOpportunitiesGroups(datasource, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunitiesApi#getOpportunitiesGroups");
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
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of opportunities group ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getOpportunitiesGroupsGroupId"></a>
# **getOpportunitiesGroupsGroupId**
> GetOpportunitiesGroupsGroupIdOk getOpportunitiesGroupsGroupId(groupId, acceptLanguage, datasource, ifNoneMatch, language)

Get opportunities group

Return information of an opportunities group  --- Alternate route: &#x60;/dev/opportunities/groups/{group_id}/&#x60;  Alternate route: &#x60;/legacy/opportunities/groups/{group_id}/&#x60;  Alternate route: &#x60;/v1/opportunities/groups/{group_id}/&#x60;  --- This route expires daily at 11:05

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");

    OpportunitiesApi apiInstance = new OpportunitiesApi(defaultClient);
    Integer groupId = 56; // Integer | ID of an opportunities group
    String acceptLanguage = "de"; // String | Language to use in the response
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String language = "de"; // String | Language to use in the response, takes precedence over Accept-Language
    try {
      GetOpportunitiesGroupsGroupIdOk result = apiInstance.getOpportunitiesGroupsGroupId(groupId, acceptLanguage, datasource, ifNoneMatch, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunitiesApi#getOpportunitiesGroupsGroupId");
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
| **groupId** | **Integer**| ID of an opportunities group | |
| **acceptLanguage** | **String**| Language to use in the response | [optional] [default to en-us] [enum: de, en-us, fr, ja, ru, zh] |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **language** | **String**| Language to use in the response, takes precedence over Accept-Language | [optional] [default to en-us] [enum: de, en-us, fr, ja, ru, zh] |

### Return type

[**GetOpportunitiesGroupsGroupIdOk**](GetOpportunitiesGroupsGroupIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of an opportunities group |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  * Content-Language - The language used in the response <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getOpportunitiesTasks"></a>
# **getOpportunitiesTasks**
> List&lt;Integer&gt; getOpportunitiesTasks(datasource, ifNoneMatch)

Get opportunities tasks

Return a list of opportunities tasks  --- Alternate route: &#x60;/dev/opportunities/tasks/&#x60;  Alternate route: &#x60;/legacy/opportunities/tasks/&#x60;  Alternate route: &#x60;/v1/opportunities/tasks/&#x60;  --- This route expires daily at 11:05

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");

    OpportunitiesApi apiInstance = new OpportunitiesApi(defaultClient);
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    try {
      List<Integer> result = apiInstance.getOpportunitiesTasks(datasource, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunitiesApi#getOpportunitiesTasks");
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
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of opportunities task ids |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getOpportunitiesTasksTaskId"></a>
# **getOpportunitiesTasksTaskId**
> GetOpportunitiesTasksTaskIdOk getOpportunitiesTasksTaskId(taskId, datasource, ifNoneMatch)

Get opportunities task

Return information of an opportunities task  --- Alternate route: &#x60;/dev/opportunities/tasks/{task_id}/&#x60;  Alternate route: &#x60;/legacy/opportunities/tasks/{task_id}/&#x60;  Alternate route: &#x60;/v1/opportunities/tasks/{task_id}/&#x60;  --- This route expires daily at 11:05

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpportunitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");

    OpportunitiesApi apiInstance = new OpportunitiesApi(defaultClient);
    Integer taskId = 56; // Integer | ID of an opportunities task
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    try {
      GetOpportunitiesTasksTaskIdOk result = apiInstance.getOpportunitiesTasksTaskId(taskId, datasource, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpportunitiesApi#getOpportunitiesTasksTaskId");
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
| **taskId** | **Integer**| ID of an opportunities task | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |

### Return type

[**GetOpportunitiesTasksTaskIdOk**](GetOpportunitiesTasksTaskIdOk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of an opportunities task |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

