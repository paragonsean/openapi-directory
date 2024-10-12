# TeamMemberRoleCodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTeamMemberRoleCodeGetCollection**](TeamMemberRoleCodeApi.md#apiTeamMemberRoleCodeGetCollection) | **GET** /api/team-member-role-code | Retrieves the collection of TeamMemberRoleCode resources. |
| [**apiTeamMemberRoleCodeIdGet**](TeamMemberRoleCodeApi.md#apiTeamMemberRoleCodeIdGet) | **GET** /api/team-member-role-code/{id} | Retrieves a TeamMemberRoleCode resource. |


<a id="apiTeamMemberRoleCodeGetCollection"></a>
# **apiTeamMemberRoleCodeGetCollection**
> List&lt;TeamMemberRoleCodeGet&gt; apiTeamMemberRoleCodeGetCollection(page, properties)

Retrieves the collection of TeamMemberRoleCode resources.

Retrieves the collection of TeamMemberRoleCode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberRoleCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamMemberRoleCodeApi apiInstance = new TeamMemberRoleCodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TeamMemberRoleCodeGet> result = apiInstance.apiTeamMemberRoleCodeGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberRoleCodeApi#apiTeamMemberRoleCodeGetCollection");
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
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;TeamMemberRoleCodeGet&gt;**](TeamMemberRoleCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamMemberRoleCode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamMemberRoleCodeIdGet"></a>
# **apiTeamMemberRoleCodeIdGet**
> TeamMemberRoleCodeGet apiTeamMemberRoleCodeIdGet(id)

Retrieves a TeamMemberRoleCode resource.

Retrieves a TeamMemberRoleCode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberRoleCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamMemberRoleCodeApi apiInstance = new TeamMemberRoleCodeApi(defaultClient);
    String id = "id_example"; // String | TeamMemberRoleCode identifier
    try {
      TeamMemberRoleCodeGet result = apiInstance.apiTeamMemberRoleCodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberRoleCodeApi#apiTeamMemberRoleCodeIdGet");
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
| **id** | **String**| TeamMemberRoleCode identifier | |

### Return type

[**TeamMemberRoleCodeGet**](TeamMemberRoleCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamMemberRoleCode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

