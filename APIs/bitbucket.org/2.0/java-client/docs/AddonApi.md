# AddonApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addonDelete**](AddonApi.md#addonDelete) | **DELETE** /addon | Delete an app |
| [**addonLinkersGet**](AddonApi.md#addonLinkersGet) | **GET** /addon/linkers | List linkers for an app |
| [**addonLinkersLinkerKeyGet**](AddonApi.md#addonLinkersLinkerKeyGet) | **GET** /addon/linkers/{linker_key} | Get a linker for an app |
| [**addonLinkersLinkerKeyValuesDelete**](AddonApi.md#addonLinkersLinkerKeyValuesDelete) | **DELETE** /addon/linkers/{linker_key}/values | Delete all linker values |
| [**addonLinkersLinkerKeyValuesGet**](AddonApi.md#addonLinkersLinkerKeyValuesGet) | **GET** /addon/linkers/{linker_key}/values | List linker values for a linker |
| [**addonLinkersLinkerKeyValuesPost**](AddonApi.md#addonLinkersLinkerKeyValuesPost) | **POST** /addon/linkers/{linker_key}/values | Create a linker value |
| [**addonLinkersLinkerKeyValuesPut**](AddonApi.md#addonLinkersLinkerKeyValuesPut) | **PUT** /addon/linkers/{linker_key}/values | Update a linker value |
| [**addonLinkersLinkerKeyValuesValueIdDelete**](AddonApi.md#addonLinkersLinkerKeyValuesValueIdDelete) | **DELETE** /addon/linkers/{linker_key}/values/{value_id} | Delete a linker value |
| [**addonLinkersLinkerKeyValuesValueIdGet**](AddonApi.md#addonLinkersLinkerKeyValuesValueIdGet) | **GET** /addon/linkers/{linker_key}/values/{value_id} | Get a linker value |
| [**addonPut**](AddonApi.md#addonPut) | **PUT** /addon | Update an installed app |


<a id="addonDelete"></a>
# **addonDelete**
> addonDelete()

Delete an app

Deletes the application for the user.  This endpoint is intended to be used by Bitbucket Connect apps and only supports JWT authentication -- that is how Bitbucket identifies the particular installation of the app. Developers with applications registered in the \&quot;Develop Apps\&quot; section of Bitbucket Marketplace need not use this endpoint as updates for those applications can be sent out via the UI of that section.  &#x60;&#x60;&#x60; $ curl -X DELETE https://api.bitbucket.org/2.0/addon \\   -H \&quot;Authorization: JWT &lt;JWT Token&gt;\&quot; &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    try {
      apiInstance.addonDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request has succeeded. The application has been deleted for the user. |  -  |
| **401** | No authorization. |  -  |
| **403** | Improper authentication. |  -  |

<a id="addonLinkersGet"></a>
# **addonLinkersGet**
> addonLinkersGet()

List linkers for an app

Gets a list of all [linkers](/cloud/bitbucket/modules/linker/) for the authenticated application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    try {
      apiInstance.addonLinkersGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **401** | Authentication must use app JWT |  -  |

<a id="addonLinkersLinkerKeyGet"></a>
# **addonLinkersLinkerKeyGet**
> addonLinkersLinkerKeyGet(linkerKey)

Get a linker for an app

Gets a [linker](/cloud/bitbucket/modules/linker/) specified by &#x60;linker_key&#x60; for the authenticated application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    String linkerKey = "linkerKey_example"; // String | The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor.
    try {
      apiInstance.addonLinkersLinkerKeyGet(linkerKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersLinkerKeyGet");
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
| **linkerKey** | **String**| The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **401** | Authentication must use app JWT |  -  |
| **404** | The linker does not exist. |  -  |

<a id="addonLinkersLinkerKeyValuesDelete"></a>
# **addonLinkersLinkerKeyValuesDelete**
> addonLinkersLinkerKeyValuesDelete(linkerKey)

Delete all linker values

Delete all [linker](/cloud/bitbucket/modules/linker/) values for the specified linker of the authenticated application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    String linkerKey = "linkerKey_example"; // String | The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor.
    try {
      apiInstance.addonLinkersLinkerKeyValuesDelete(linkerKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersLinkerKeyValuesDelete");
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
| **linkerKey** | **String**| The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted the linker values. |  -  |
| **401** | Authentication must use app JWT |  -  |
| **404** | The linker does not exist. |  -  |

<a id="addonLinkersLinkerKeyValuesGet"></a>
# **addonLinkersLinkerKeyValuesGet**
> addonLinkersLinkerKeyValuesGet(linkerKey)

List linker values for a linker

Gets a list of all [linker](/cloud/bitbucket/modules/linker/) values for the specified linker of the authenticated application.  A linker value lets applications supply values to modify its regular expression.  The base regular expression must use a Bitbucket-specific match group &#x60;(?K)&#x60; which will be translated to &#x60;([\\w\\-]+)&#x60;. A value must match this pattern.  [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    String linkerKey = "linkerKey_example"; // String | The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor.
    try {
      apiInstance.addonLinkersLinkerKeyValuesGet(linkerKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersLinkerKeyValuesGet");
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
| **linkerKey** | **String**| The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **401** | Authentication must use app JWT |  -  |
| **404** | The linker does not exist. |  -  |

<a id="addonLinkersLinkerKeyValuesPost"></a>
# **addonLinkersLinkerKeyValuesPost**
> addonLinkersLinkerKeyValuesPost(linkerKey)

Create a linker value

Creates a [linker](/cloud/bitbucket/modules/linker/) value for the specified linker of authenticated application.  A linker value lets applications supply values to modify its regular expression.  The base regular expression must use a Bitbucket-specific match group &#x60;(?K)&#x60; which will be translated to &#x60;([\\w\\-]+)&#x60;. A value must match this pattern.  [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    String linkerKey = "linkerKey_example"; // String | The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor.
    try {
      apiInstance.addonLinkersLinkerKeyValuesPost(linkerKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersLinkerKeyValuesPost");
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
| **linkerKey** | **String**| The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully created the linker value. |  -  |
| **401** | Authentication must use app JWT |  -  |
| **404** | The linker does not exist. |  -  |
| **409** | The linker already has the value being added. |  -  |

<a id="addonLinkersLinkerKeyValuesPut"></a>
# **addonLinkersLinkerKeyValuesPut**
> addonLinkersLinkerKeyValuesPut(linkerKey)

Update a linker value

Bulk update [linker](/cloud/bitbucket/modules/linker/) values for the specified linker of the authenticated application.  A linker value lets applications supply values to modify its regular expression.  The base regular expression must use a Bitbucket-specific match group &#x60;(?K)&#x60; which will be translated to &#x60;([\\w\\-]+)&#x60;. A value must match this pattern.  [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    String linkerKey = "linkerKey_example"; // String | The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor.
    try {
      apiInstance.addonLinkersLinkerKeyValuesPut(linkerKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersLinkerKeyValuesPut");
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
| **linkerKey** | **String**| The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully updated the linker values. |  -  |
| **400** | Invalid input. |  -  |
| **401** | Authentication must use app JWT |  -  |
| **404** | The linker does not exist. |  -  |

<a id="addonLinkersLinkerKeyValuesValueIdDelete"></a>
# **addonLinkersLinkerKeyValuesValueIdDelete**
> addonLinkersLinkerKeyValuesValueIdDelete(linkerKey, valueId)

Delete a linker value

Delete a single [linker](/cloud/bitbucket/modules/linker/) value of the authenticated application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    String linkerKey = "linkerKey_example"; // String | The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor.
    Integer valueId = 56; // Integer | The numeric ID of the linker value.
    try {
      apiInstance.addonLinkersLinkerKeyValuesValueIdDelete(linkerKey, valueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersLinkerKeyValuesValueIdDelete");
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
| **linkerKey** | **String**| The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor. | |
| **valueId** | **Integer**| The numeric ID of the linker value. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted the linker value. |  -  |
| **401** | Authentication must use app JWT |  -  |
| **404** | The linker value does not exist. |  -  |

<a id="addonLinkersLinkerKeyValuesValueIdGet"></a>
# **addonLinkersLinkerKeyValuesValueIdGet**
> addonLinkersLinkerKeyValuesValueIdGet(linkerKey, valueId)

Get a linker value

Get a single [linker](/cloud/bitbucket/modules/linker/) value of the authenticated application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    String linkerKey = "linkerKey_example"; // String | The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor.
    Integer valueId = 56; // Integer | The numeric ID of the linker value.
    try {
      apiInstance.addonLinkersLinkerKeyValuesValueIdGet(linkerKey, valueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonLinkersLinkerKeyValuesValueIdGet");
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
| **linkerKey** | **String**| The unique key of a [linker module](/cloud/bitbucket/modules/linker/) as defined in an application descriptor. | |
| **valueId** | **Integer**| The numeric ID of the linker value. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **401** | Authentication must use app JWT |  -  |
| **404** | The linker value does not exist. |  -  |

<a id="addonPut"></a>
# **addonPut**
> addonPut()

Update an installed app

Updates the application installation for the user.  This endpoint is intended to be used by Bitbucket Connect apps and only supports JWT authentication -- that is how Bitbucket identifies the particular installation of the app. Developers with applications registered in the \&quot;Develop Apps\&quot; section of Bitbucket need not use this endpoint as updates for those applications can be sent out via the UI of that section.  Passing an empty body will update the installation using the existing descriptor URL.  &#x60;&#x60;&#x60; $ curl -X PUT https://api.bitbucket.org/2.0/addon \\   -H \&quot;Authorization: JWT &lt;JWT Token&gt;\&quot; \\   --header \&quot;Content-Type: application/json\&quot; \\   --data &#39;{}&#39; &#x60;&#x60;&#x60;  The new &#x60;descriptor&#x60; for the installation can be also provided in the body directly.  &#x60;&#x60;&#x60; $ curl -X PUT https://api.bitbucket.org/2.0/addon \\   -H \&quot;Authorization: JWT &lt;JWT Token&gt;\&quot; \\   --header \&quot;Content-Type: application/json\&quot; \\   --data &#39;{\&quot;descriptor\&quot;: $NEW_DESCRIPTOR}&#39; &#x60;&#x60;&#x60;  In both these modes the URL of the descriptor cannot be changed. To change the descriptor location and upgrade an installation the request must be made exclusively with a &#x60;descriptor_url&#x60;.   &#x60;&#x60;&#x60; $ curl -X PUT https://api.bitbucket.org/2.0/addon \\   -H \&quot;Authorization: JWT &lt;JWT Token&gt;\&quot; \\   --header \&quot;Content-Type: application/json\&quot; \\   --data &#39;{\&quot;descriptor_url\&quot;: $NEW_URL}&#39; &#x60;&#x60;&#x60;  The &#x60;descriptor_url&#x60; must exactly match the marketplace registration that Atlassian has for the application. Contact your Atlassian developer advocate to update this registration. Once the registration has been updated you may call this resource for each installation.  Note that the scopes of the application cannot be increased in the new descriptor nor reduced to none.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    AddonApi apiInstance = new AddonApi(defaultClient);
    try {
      apiInstance.addonPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonApi#addonPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request has succeeded. The installation has been updated to the new descriptor. |  -  |
| **400** | Scopes have increased or decreased to none. |  -  |
| **401** | No authorization. |  -  |
| **403** | Improper authentication. |  -  |

