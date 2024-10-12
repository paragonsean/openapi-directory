# TransportMicrosoftTeamsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMicrosoftTeamsGetCollection**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsGetCollection) | **GET** /api/transport-microsoft-teams | Retrieves the collection of TransportMicrosoftTeams resources. |
| [**apiTransportMicrosoftTeamsIdDelete**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdDelete) | **DELETE** /api/transport-microsoft-teams/{id} | Removes the TransportMicrosoftTeams resource. |
| [**apiTransportMicrosoftTeamsIdGet**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdGet) | **GET** /api/transport-microsoft-teams/{id} | Retrieves a TransportMicrosoftTeams resource. |
| [**apiTransportMicrosoftTeamsIdPatch**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdPatch) | **PATCH** /api/transport-microsoft-teams/{id} | Updates the TransportMicrosoftTeams resource. |
| [**apiTransportMicrosoftTeamsIdPut**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdPut) | **PUT** /api/transport-microsoft-teams/{id} | Replaces the TransportMicrosoftTeams resource. |
| [**apiTransportMicrosoftTeamsPost**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsPost) | **POST** /api/transport-microsoft-teams | Creates a TransportMicrosoftTeams resource. |


<a id="apiTransportMicrosoftTeamsGetCollection"></a>
# **apiTransportMicrosoftTeamsGetCollection**
> List&lt;TransportMicrosoftTeamsGet&gt; apiTransportMicrosoftTeamsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMicrosoftTeams resources.

Retrieves the collection of TransportMicrosoftTeams resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMicrosoftTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMicrosoftTeamsApi apiInstance = new TransportMicrosoftTeamsApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMicrosoftTeamsGet> result = apiInstance.apiTransportMicrosoftTeamsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMicrosoftTeamsApi#apiTransportMicrosoftTeamsGetCollection");
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
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;TransportMicrosoftTeamsGet&gt;**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMicrosoftTeams collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMicrosoftTeamsIdDelete"></a>
# **apiTransportMicrosoftTeamsIdDelete**
> apiTransportMicrosoftTeamsIdDelete(id)

Removes the TransportMicrosoftTeams resource.

Removes the TransportMicrosoftTeams resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMicrosoftTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMicrosoftTeamsApi apiInstance = new TransportMicrosoftTeamsApi(defaultClient);
    String id = "id_example"; // String | TransportMicrosoftTeams identifier
    try {
      apiInstance.apiTransportMicrosoftTeamsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMicrosoftTeamsApi#apiTransportMicrosoftTeamsIdDelete");
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
| **id** | **String**| TransportMicrosoftTeams identifier | |

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
| **204** | TransportMicrosoftTeams resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMicrosoftTeamsIdGet"></a>
# **apiTransportMicrosoftTeamsIdGet**
> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsIdGet(id)

Retrieves a TransportMicrosoftTeams resource.

Retrieves a TransportMicrosoftTeams resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMicrosoftTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMicrosoftTeamsApi apiInstance = new TransportMicrosoftTeamsApi(defaultClient);
    String id = "id_example"; // String | TransportMicrosoftTeams identifier
    try {
      TransportMicrosoftTeamsGet result = apiInstance.apiTransportMicrosoftTeamsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMicrosoftTeamsApi#apiTransportMicrosoftTeamsIdGet");
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
| **id** | **String**| TransportMicrosoftTeams identifier | |

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMicrosoftTeams resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMicrosoftTeamsIdPatch"></a>
# **apiTransportMicrosoftTeamsIdPatch**
> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsIdPatch(id, transportMicrosoftTeamsPatch)

Updates the TransportMicrosoftTeams resource.

Updates the TransportMicrosoftTeams resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMicrosoftTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMicrosoftTeamsApi apiInstance = new TransportMicrosoftTeamsApi(defaultClient);
    String id = "id_example"; // String | TransportMicrosoftTeams identifier
    TransportMicrosoftTeamsPatch transportMicrosoftTeamsPatch = new TransportMicrosoftTeamsPatch(); // TransportMicrosoftTeamsPatch | The updated TransportMicrosoftTeams resource
    try {
      TransportMicrosoftTeamsGet result = apiInstance.apiTransportMicrosoftTeamsIdPatch(id, transportMicrosoftTeamsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMicrosoftTeamsApi#apiTransportMicrosoftTeamsIdPatch");
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
| **id** | **String**| TransportMicrosoftTeams identifier | |
| **transportMicrosoftTeamsPatch** | [**TransportMicrosoftTeamsPatch**](TransportMicrosoftTeamsPatch.md)| The updated TransportMicrosoftTeams resource | |

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMicrosoftTeams resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMicrosoftTeamsIdPut"></a>
# **apiTransportMicrosoftTeamsIdPut**
> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsIdPut(id, transportMicrosoftTeamsPut)

Replaces the TransportMicrosoftTeams resource.

Replaces the TransportMicrosoftTeams resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMicrosoftTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMicrosoftTeamsApi apiInstance = new TransportMicrosoftTeamsApi(defaultClient);
    String id = "id_example"; // String | TransportMicrosoftTeams identifier
    TransportMicrosoftTeamsPut transportMicrosoftTeamsPut = new TransportMicrosoftTeamsPut(); // TransportMicrosoftTeamsPut | The updated TransportMicrosoftTeams resource
    try {
      TransportMicrosoftTeamsGet result = apiInstance.apiTransportMicrosoftTeamsIdPut(id, transportMicrosoftTeamsPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMicrosoftTeamsApi#apiTransportMicrosoftTeamsIdPut");
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
| **id** | **String**| TransportMicrosoftTeams identifier | |
| **transportMicrosoftTeamsPut** | [**TransportMicrosoftTeamsPut**](TransportMicrosoftTeamsPut.md)| The updated TransportMicrosoftTeams resource | |

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMicrosoftTeams resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMicrosoftTeamsPost"></a>
# **apiTransportMicrosoftTeamsPost**
> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsPost(transportMicrosoftTeamsPost)

Creates a TransportMicrosoftTeams resource.

Creates a TransportMicrosoftTeams resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMicrosoftTeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMicrosoftTeamsApi apiInstance = new TransportMicrosoftTeamsApi(defaultClient);
    TransportMicrosoftTeamsPost transportMicrosoftTeamsPost = new TransportMicrosoftTeamsPost(); // TransportMicrosoftTeamsPost | The new TransportMicrosoftTeams resource
    try {
      TransportMicrosoftTeamsGet result = apiInstance.apiTransportMicrosoftTeamsPost(transportMicrosoftTeamsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMicrosoftTeamsApi#apiTransportMicrosoftTeamsPost");
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
| **transportMicrosoftTeamsPost** | [**TransportMicrosoftTeamsPost**](TransportMicrosoftTeamsPost.md)| The new TransportMicrosoftTeams resource | |

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMicrosoftTeams resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

