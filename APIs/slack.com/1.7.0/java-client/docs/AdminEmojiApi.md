# AdminEmojiApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminEmojiAdd**](AdminEmojiApi.md#adminEmojiAdd) | **POST** /admin.emoji.add |  |
| [**adminEmojiAddAlias**](AdminEmojiApi.md#adminEmojiAddAlias) | **POST** /admin.emoji.addAlias |  |
| [**adminEmojiList**](AdminEmojiApi.md#adminEmojiList) | **GET** /admin.emoji.list |  |
| [**adminEmojiRemove**](AdminEmojiApi.md#adminEmojiRemove) | **POST** /admin.emoji.remove |  |
| [**adminEmojiRename**](AdminEmojiApi.md#adminEmojiRename) | **POST** /admin.emoji.rename |  |


<a id="adminEmojiAdd"></a>
# **adminEmojiAdd**
> DefaultSuccessTemplate adminEmojiAdd(name, token, url)



Add an emoji.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminEmojiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminEmojiApi apiInstance = new AdminEmojiApi(defaultClient);
    String name = "name_example"; // String | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    String url = "url_example"; // String | The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best.
    try {
      DefaultSuccessTemplate result = apiInstance.adminEmojiAdd(name, token, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminEmojiApi#adminEmojiAdd");
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
| **name** | **String**| The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |
| **url** | **String**| The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminEmojiAddAlias"></a>
# **adminEmojiAddAlias**
> DefaultSuccessTemplate adminEmojiAddAlias(aliasFor, name, token)



Add an emoji alias.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminEmojiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminEmojiApi apiInstance = new AdminEmojiApi(defaultClient);
    String aliasFor = "aliasFor_example"; // String | The alias of the emoji.
    String name = "name_example"; // String | The name of the emoji to be aliased. Colons (`:myemoji:`) around the value are not required, although they may be included.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    try {
      DefaultSuccessTemplate result = apiInstance.adminEmojiAddAlias(aliasFor, name, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminEmojiApi#adminEmojiAddAlias");
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
| **aliasFor** | **String**| The alias of the emoji. | |
| **name** | **String**| The name of the emoji to be aliased. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminEmojiList"></a>
# **adminEmojiList**
> DefaultSuccessTemplate adminEmojiList(token, cursor, limit)



List emoji for an Enterprise Grid organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminEmojiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminEmojiApi apiInstance = new AdminEmojiApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
    String cursor = "cursor_example"; // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page
    Integer limit = 56; // Integer | The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    try {
      DefaultSuccessTemplate result = apiInstance.adminEmojiList(token, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminEmojiApi#adminEmojiList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:read&#x60; | |
| **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Must be between 1 - 1000 both inclusive. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminEmojiRemove"></a>
# **adminEmojiRemove**
> DefaultSuccessTemplate adminEmojiRemove(name, token)



Remove an emoji across an Enterprise Grid organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminEmojiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminEmojiApi apiInstance = new AdminEmojiApi(defaultClient);
    String name = "name_example"; // String | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    try {
      DefaultSuccessTemplate result = apiInstance.adminEmojiRemove(name, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminEmojiApi#adminEmojiRemove");
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
| **name** | **String**| The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="adminEmojiRename"></a>
# **adminEmojiRename**
> DefaultSuccessTemplate adminEmojiRename(name, newName, token)



Rename an emoji.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminEmojiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminEmojiApi apiInstance = new AdminEmojiApi(defaultClient);
    String name = "name_example"; // String | The name of the emoji to be renamed. Colons (`:myemoji:`) around the value are not required, although they may be included.
    String newName = "newName_example"; // String | The new name of the emoji.
    String token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
    try {
      DefaultSuccessTemplate result = apiInstance.adminEmojiRename(name, newName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminEmojiApi#adminEmojiRename");
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
| **name** | **String**| The name of the emoji to be renamed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | |
| **newName** | **String**| The new name of the emoji. | |
| **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

