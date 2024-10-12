# TeamInvitationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTeamInvitationGetCollection**](TeamInvitationApi.md#apiTeamInvitationGetCollection) | **GET** /api/team-invitation | Retrieves the collection of TeamInvitation resources. |
| [**apiTeamInvitationIdDelete**](TeamInvitationApi.md#apiTeamInvitationIdDelete) | **DELETE** /api/team-invitation/{id} | Removes the TeamInvitation resource. |
| [**apiTeamInvitationIdGet**](TeamInvitationApi.md#apiTeamInvitationIdGet) | **GET** /api/team-invitation/{id} | Retrieves a TeamInvitation resource. |
| [**apiTeamInvitationPost**](TeamInvitationApi.md#apiTeamInvitationPost) | **POST** /api/team-invitation | Creates a TeamInvitation resource. |


<a id="apiTeamInvitationGetCollection"></a>
# **apiTeamInvitationGetCollection**
> List&lt;TeamInvitationGet&gt; apiTeamInvitationGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, inviteeEmail, inviteeEmail2, properties)

Retrieves the collection of TeamInvitation resources.

Retrieves the collection of TeamInvitation resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamInvitationApi apiInstance = new TeamInvitationApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    String inviteeEmail = "inviteeEmail_example"; // String | 
    List<String> inviteeEmail2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TeamInvitationGet> result = apiInstance.apiTeamInvitationGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, inviteeEmail, inviteeEmail2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamInvitationApi#apiTeamInvitationGetCollection");
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
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **dataSegmentCode** | **String**|  | [optional] |
| **dataSegmentCode2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **partition** | **String**|  | [optional] |
| **partition2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **inviteeEmail** | **String**|  | [optional] |
| **inviteeEmail2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;TeamInvitationGet&gt;**](TeamInvitationGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamInvitation collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamInvitationIdDelete"></a>
# **apiTeamInvitationIdDelete**
> apiTeamInvitationIdDelete(id)

Removes the TeamInvitation resource.

Removes the TeamInvitation resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamInvitationApi apiInstance = new TeamInvitationApi(defaultClient);
    String id = "id_example"; // String | TeamInvitation identifier
    try {
      apiInstance.apiTeamInvitationIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamInvitationApi#apiTeamInvitationIdDelete");
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
| **id** | **String**| TeamInvitation identifier | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | TeamInvitation resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamInvitationIdGet"></a>
# **apiTeamInvitationIdGet**
> TeamInvitationGet apiTeamInvitationIdGet(id)

Retrieves a TeamInvitation resource.

Retrieves a TeamInvitation resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamInvitationApi apiInstance = new TeamInvitationApi(defaultClient);
    String id = "id_example"; // String | TeamInvitation identifier
    try {
      TeamInvitationGet result = apiInstance.apiTeamInvitationIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamInvitationApi#apiTeamInvitationIdGet");
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
| **id** | **String**| TeamInvitation identifier | |

### Return type

[**TeamInvitationGet**](TeamInvitationGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamInvitation resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamInvitationPost"></a>
# **apiTeamInvitationPost**
> TeamInvitationGet apiTeamInvitationPost(teamInvitationPost)

Creates a TeamInvitation resource.

Creates a TeamInvitation resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamInvitationApi apiInstance = new TeamInvitationApi(defaultClient);
    TeamInvitationPost teamInvitationPost = new TeamInvitationPost(); // TeamInvitationPost | The new TeamInvitation resource
    try {
      TeamInvitationGet result = apiInstance.apiTeamInvitationPost(teamInvitationPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamInvitationApi#apiTeamInvitationPost");
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
| **teamInvitationPost** | [**TeamInvitationPost**](TeamInvitationPost.md)| The new TeamInvitation resource | |

### Return type

[**TeamInvitationGet**](TeamInvitationGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TeamInvitation resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

