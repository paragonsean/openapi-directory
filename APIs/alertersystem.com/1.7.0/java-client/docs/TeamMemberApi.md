# TeamMemberApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTeamMemberGetCollection**](TeamMemberApi.md#apiTeamMemberGetCollection) | **GET** /api/team-member | Retrieves the collection of TeamMember resources. |
| [**apiTeamMemberIdDelete**](TeamMemberApi.md#apiTeamMemberIdDelete) | **DELETE** /api/team-member/{id} | Removes the TeamMember resource. |
| [**apiTeamMemberIdGet**](TeamMemberApi.md#apiTeamMemberIdGet) | **GET** /api/team-member/{id} | Retrieves a TeamMember resource. |
| [**apiTeamMemberIdPatch**](TeamMemberApi.md#apiTeamMemberIdPatch) | **PATCH** /api/team-member/{id} | Updates the TeamMember resource. |
| [**apiTeamMemberIdPut**](TeamMemberApi.md#apiTeamMemberIdPut) | **PUT** /api/team-member/{id} | Replaces the TeamMember resource. |


<a id="apiTeamMemberGetCollection"></a>
# **apiTeamMemberGetCollection**
> List&lt;TeamMemberGet&gt; apiTeamMemberGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, userAccount, userAccount2, properties)

Retrieves the collection of TeamMember resources.

Retrieves the collection of TeamMember resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    String userAccount = "userAccount_example"; // String | 
    List<String> userAccount2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TeamMemberGet> result = apiInstance.apiTeamMemberGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, userAccount, userAccount2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#apiTeamMemberGetCollection");
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
| **userAccount** | **String**|  | [optional] |
| **userAccount2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;TeamMemberGet&gt;**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamMember collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamMemberIdDelete"></a>
# **apiTeamMemberIdDelete**
> apiTeamMemberIdDelete(id)

Removes the TeamMember resource.

Removes the TeamMember resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String id = "id_example"; // String | TeamMember identifier
    try {
      apiInstance.apiTeamMemberIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#apiTeamMemberIdDelete");
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
| **id** | **String**| TeamMember identifier | |

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
| **204** | TeamMember resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamMemberIdGet"></a>
# **apiTeamMemberIdGet**
> TeamMemberGet apiTeamMemberIdGet(id)

Retrieves a TeamMember resource.

Retrieves a TeamMember resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String id = "id_example"; // String | TeamMember identifier
    try {
      TeamMemberGet result = apiInstance.apiTeamMemberIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#apiTeamMemberIdGet");
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
| **id** | **String**| TeamMember identifier | |

### Return type

[**TeamMemberGet**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamMember resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamMemberIdPatch"></a>
# **apiTeamMemberIdPatch**
> TeamMemberGet apiTeamMemberIdPatch(id, teamMemberPatch)

Updates the TeamMember resource.

Updates the TeamMember resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String id = "id_example"; // String | TeamMember identifier
    TeamMemberPatch teamMemberPatch = new TeamMemberPatch(); // TeamMemberPatch | The updated TeamMember resource
    try {
      TeamMemberGet result = apiInstance.apiTeamMemberIdPatch(id, teamMemberPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#apiTeamMemberIdPatch");
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
| **id** | **String**| TeamMember identifier | |
| **teamMemberPatch** | [**TeamMemberPatch**](TeamMemberPatch.md)| The updated TeamMember resource | |

### Return type

[**TeamMemberGet**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamMember resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTeamMemberIdPut"></a>
# **apiTeamMemberIdPut**
> TeamMemberGet apiTeamMemberIdPut(id, teamMemberPut)

Replaces the TeamMember resource.

Replaces the TeamMember resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeamMemberApi apiInstance = new TeamMemberApi(defaultClient);
    String id = "id_example"; // String | TeamMember identifier
    TeamMemberPut teamMemberPut = new TeamMemberPut(); // TeamMemberPut | The updated TeamMember resource
    try {
      TeamMemberGet result = apiInstance.apiTeamMemberIdPut(id, teamMemberPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMemberApi#apiTeamMemberIdPut");
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
| **id** | **String**| TeamMember identifier | |
| **teamMemberPut** | [**TeamMemberPut**](TeamMemberPut.md)| The updated TeamMember resource | |

### Return type

[**TeamMemberGet**](TeamMemberGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TeamMember resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

