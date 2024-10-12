# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChildren**](DefaultApi.md#getChildren) | **GET** /children/{sha1}/{count}/{cursor} |  |
| [**getInfo**](DefaultApi.md#getInfo) | **GET** /info |  |
| [**getLookupMd5**](DefaultApi.md#getLookupMd5) | **GET** /lookup/md5/{md5} |  |
| [**getLookupSha1**](DefaultApi.md#getLookupSha1) | **GET** /lookup/sha1/{sha1} |  |
| [**getLookupSha256**](DefaultApi.md#getLookupSha256) | **GET** /lookup/sha256/{sha256} |  |
| [**getParents**](DefaultApi.md#getParents) | **GET** /parents/{sha1}/{count}/{cursor} |  |
| [**getSessionCreate**](DefaultApi.md#getSessionCreate) | **GET** /session/create/{name} |  |
| [**getSessionMatches**](DefaultApi.md#getSessionMatches) | **GET** /session/get/{name} |  |
| [**getStattop**](DefaultApi.md#getStattop) | **GET** /stats/top |  |
| [**postBulkmd5**](DefaultApi.md#postBulkmd5) | **POST** /bulk/md5 |  |
| [**postBulksha1**](DefaultApi.md#postBulksha1) | **POST** /bulk/sha1 |  |


<a id="getChildren"></a>
# **getChildren**
> getChildren(sha1, count, cursor)



Return children from a given SHA1.  A number of element to return and an offset must be given. If not set it will be the 100 first elements. A cursor must be given to paginate over. The starting cursor is 0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sha1 = "sha1_example"; // String | 
    Integer count = 56; // Integer | 
    String cursor = "cursor_example"; // String | 
    try {
      apiInstance.getChildren(sha1, count, cursor);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChildren");
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
| **sha1** | **String**|  | |
| **count** | **Integer**|  | |
| **cursor** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | SHA1 value incorrect, expecting a SHA1 value in hex format |  -  |
| **404** | The SHA1 value has no known child. |  -  |

<a id="getInfo"></a>
# **getInfo**
> getInfo()



Info about the hashlookup database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getInfo();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getInfo");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getLookupMd5"></a>
# **getLookupMd5**
> getLookupMd5(md5)



Lookup MD5.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String md5 = "md5_example"; // String | 
    try {
      apiInstance.getLookupMd5(md5);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLookupMd5");
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
| **md5** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | MD5 value incorrect, expecting a MD5 value in hex format |  -  |
| **404** | Non existing MD5 |  -  |

<a id="getLookupSha1"></a>
# **getLookupSha1**
> getLookupSha1(sha1)



Lookup SHA-1.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sha1 = "sha1_example"; // String | 
    try {
      apiInstance.getLookupSha1(sha1);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLookupSha1");
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
| **sha1** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | SHA1 value incorrect, expecting a SHA1 value in hex format |  -  |
| **404** | Non existing SHA1 |  -  |

<a id="getLookupSha256"></a>
# **getLookupSha256**
> getLookupSha256(sha256)



Lookup SHA-256.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sha256 = "sha256_example"; // String | 
    try {
      apiInstance.getLookupSha256(sha256);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLookupSha256");
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
| **sha256** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | SHA-256 value incorrect, expecting a SHA-256 value in hex format |  -  |
| **404** | Non existing SHA-256 |  -  |

<a id="getParents"></a>
# **getParents**
> getParents(sha1, count, cursor)



Return parents from a given SHA1. A number of element to return and an offset must be given. If not set it will be the 100 first elements. A cursor must be given to paginate over. The starting cursor is 0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sha1 = "sha1_example"; // String | 
    Integer count = 56; // Integer | 
    String cursor = "cursor_example"; // String | 
    try {
      apiInstance.getParents(sha1, count, cursor);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getParents");
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
| **sha1** | **String**|  | |
| **count** | **Integer**|  | |
| **cursor** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | SHA1 value incorrect, expecting a SHA1 value in hex format |  -  |
| **404** | The SHA1 value has no known parent. |  -  |

<a id="getSessionCreate"></a>
# **getSessionCreate**
> getSessionCreate(name)



Create a session key to keep search context. The session is attached to a name. After the session is created, the header &#x60;hashlookup_session&#x60; can be set to the session name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      apiInstance.getSessionCreate(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSessionCreate");
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
| **name** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Expecting a name for the session |  -  |
| **500** | Session feature is not enabled |  -  |

<a id="getSessionMatches"></a>
# **getSessionMatches**
> getSessionMatches(name)



Return set of matching and non-matching hashes from a session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      apiInstance.getSessionMatches(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSessionMatches");
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
| **name** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Expecting a name for the session |  -  |
| **500** | Session feature is not enabled |  -  |

<a id="getStattop"></a>
# **getStattop**
> getStattop()



Return the top 100 of most queried values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getStattop();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStattop");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Public statistics not enabled |  -  |

<a id="postBulkmd5"></a>
# **postBulkmd5**
> postBulkmd5()



Bulk search of MD5 hashes in a JSON array with the key &#39;hashes&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.postBulkmd5();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postBulkmd5");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | JSON format incorrect. An array of hashes in the key &#39;hashes&#39; is expected. |  -  |

<a id="postBulksha1"></a>
# **postBulksha1**
> postBulksha1()



Bulk search of SHA1 hashes in a JSON array with the &#39;hashes&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.postBulksha1();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postBulksha1");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | JSON format incorrect. An array of hashes in the key &#39;hashes&#39; is expected. |  -  |

