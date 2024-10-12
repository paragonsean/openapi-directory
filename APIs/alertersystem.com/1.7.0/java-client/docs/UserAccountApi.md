# UserAccountApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiUserAccountGetCollection**](UserAccountApi.md#apiUserAccountGetCollection) | **GET** /api/user-account | Retrieves the collection of UserAccount resources. |
| [**apiUserAccountIdGet**](UserAccountApi.md#apiUserAccountIdGet) | **GET** /api/user-account/{id} | Retrieves a UserAccount resource. |
| [**apiUserAccountIdPatch**](UserAccountApi.md#apiUserAccountIdPatch) | **PATCH** /api/user-account/{id} | Updates the UserAccount resource. |
| [**apiUserAccountIdPut**](UserAccountApi.md#apiUserAccountIdPut) | **PUT** /api/user-account/{id} | Replaces the UserAccount resource. |


<a id="apiUserAccountGetCollection"></a>
# **apiUserAccountGetCollection**
> List&lt;UserAccountGet&gt; apiUserAccountGetCollection(page, properties)

Retrieves the collection of UserAccount resources.

Retrieves the collection of UserAccount resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UserAccountApi apiInstance = new UserAccountApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<UserAccountGet> result = apiInstance.apiUserAccountGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountApi#apiUserAccountGetCollection");
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

[**List&lt;UserAccountGet&gt;**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserAccount collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiUserAccountIdGet"></a>
# **apiUserAccountIdGet**
> UserAccountGet apiUserAccountIdGet(id)

Retrieves a UserAccount resource.

Retrieves a UserAccount resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UserAccountApi apiInstance = new UserAccountApi(defaultClient);
    String id = "id_example"; // String | UserAccount identifier
    try {
      UserAccountGet result = apiInstance.apiUserAccountIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountApi#apiUserAccountIdGet");
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
| **id** | **String**| UserAccount identifier | |

### Return type

[**UserAccountGet**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserAccount resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiUserAccountIdPatch"></a>
# **apiUserAccountIdPatch**
> UserAccountGet apiUserAccountIdPatch(id, userAccountPatch)

Updates the UserAccount resource.

Updates the UserAccount resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UserAccountApi apiInstance = new UserAccountApi(defaultClient);
    String id = "id_example"; // String | UserAccount identifier
    UserAccountPatch userAccountPatch = new UserAccountPatch(); // UserAccountPatch | The updated UserAccount resource
    try {
      UserAccountGet result = apiInstance.apiUserAccountIdPatch(id, userAccountPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountApi#apiUserAccountIdPatch");
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
| **id** | **String**| UserAccount identifier | |
| **userAccountPatch** | [**UserAccountPatch**](UserAccountPatch.md)| The updated UserAccount resource | |

### Return type

[**UserAccountGet**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserAccount resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiUserAccountIdPut"></a>
# **apiUserAccountIdPut**
> UserAccountGet apiUserAccountIdPut(id, userAccountPut)

Replaces the UserAccount resource.

Replaces the UserAccount resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    UserAccountApi apiInstance = new UserAccountApi(defaultClient);
    String id = "id_example"; // String | UserAccount identifier
    UserAccountPut userAccountPut = new UserAccountPut(); // UserAccountPut | The updated UserAccount resource
    try {
      UserAccountGet result = apiInstance.apiUserAccountIdPut(id, userAccountPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountApi#apiUserAccountIdPut");
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
| **id** | **String**| UserAccount identifier | |
| **userAccountPut** | [**UserAccountPut**](UserAccountPut.md)| The updated UserAccount resource | |

### Return type

[**UserAccountGet**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserAccount resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

