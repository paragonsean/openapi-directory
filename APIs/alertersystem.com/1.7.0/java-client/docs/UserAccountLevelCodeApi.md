# UserAccountLevelCodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiUserAccountLevelCodeGetCollection**](UserAccountLevelCodeApi.md#apiUserAccountLevelCodeGetCollection) | **GET** /api/user-account-level-code | Retrieves the collection of UserAccountLevelCode resources. |
| [**apiUserAccountLevelCodeIdGet**](UserAccountLevelCodeApi.md#apiUserAccountLevelCodeIdGet) | **GET** /api/user-account-level-code/{id} | Retrieves a UserAccountLevelCode resource. |


<a id="apiUserAccountLevelCodeGetCollection"></a>
# **apiUserAccountLevelCodeGetCollection**
> List&lt;UserAccountLevelCodeGet&gt; apiUserAccountLevelCodeGetCollection(page, properties)

Retrieves the collection of UserAccountLevelCode resources.

Retrieves the collection of UserAccountLevelCode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountLevelCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UserAccountLevelCodeApi apiInstance = new UserAccountLevelCodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<UserAccountLevelCodeGet> result = apiInstance.apiUserAccountLevelCodeGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountLevelCodeApi#apiUserAccountLevelCodeGetCollection");
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

[**List&lt;UserAccountLevelCodeGet&gt;**](UserAccountLevelCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserAccountLevelCode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiUserAccountLevelCodeIdGet"></a>
# **apiUserAccountLevelCodeIdGet**
> UserAccountLevelCodeGet apiUserAccountLevelCodeIdGet(id)

Retrieves a UserAccountLevelCode resource.

Retrieves a UserAccountLevelCode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountLevelCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UserAccountLevelCodeApi apiInstance = new UserAccountLevelCodeApi(defaultClient);
    String id = "id_example"; // String | UserAccountLevelCode identifier
    try {
      UserAccountLevelCodeGet result = apiInstance.apiUserAccountLevelCodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountLevelCodeApi#apiUserAccountLevelCodeIdGet");
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
| **id** | **String**| UserAccountLevelCode identifier | |

### Return type

[**UserAccountLevelCodeGet**](UserAccountLevelCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserAccountLevelCode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

