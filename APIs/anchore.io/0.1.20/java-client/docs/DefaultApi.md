# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOauthToken**](DefaultApi.md#getOauthToken) | **POST** /oauth/token |  |
| [**healthCheck**](DefaultApi.md#healthCheck) | **GET** /health |  |
| [**listFileContentSearchResults**](DefaultApi.md#listFileContentSearchResults) | **GET** /images/{imageDigest}/artifacts/file_content_search | Return a list of analyzer artifacts of the specified type |
| [**listRetrievedFiles**](DefaultApi.md#listRetrievedFiles) | **GET** /images/{imageDigest}/artifacts/retrieved_files | Return a list of analyzer artifacts of the specified type |
| [**listSecretSearchResults**](DefaultApi.md#listSecretSearchResults) | **GET** /images/{imageDigest}/artifacts/secret_search | Return a list of analyzer artifacts of the specified type |
| [**ping**](DefaultApi.md#ping) | **GET** / |  |
| [**versionCheck**](DefaultApi.md#versionCheck) | **GET** /version |  |


<a id="getOauthToken"></a>
# **getOauthToken**
> TokenResponse getOauthToken(clientId, grantType, password, username)



Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth

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
    String clientId = "anonymous"; // String | The type of client used for the OAuth token
    String grantType = "password"; // String | OAuth Grant type for token
    String password = "password_example"; // String | Password for corresponding user
    String username = "username_example"; // String | User to assign OAuth token to
    try {
      TokenResponse result = apiInstance.getOauthToken(clientId, grantType, password, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOauthToken");
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
| **clientId** | **String**| The type of client used for the OAuth token | [optional] [default to anonymous] |
| **grantType** | **String**| OAuth Grant type for token | [optional] [default to password] |
| **password** | **String**| Password for corresponding user | [optional] |
| **username** | **String**| User to assign OAuth token to | [optional] |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resulting JWT token |  -  |
| **500** | Internal error |  -  |

<a id="healthCheck"></a>
# **healthCheck**
> healthCheck()



Health check, returns 200 and no body if service is running

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
      apiInstance.healthCheck();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#healthCheck");
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
| **200** | Empty body on success |  -  |

<a id="listFileContentSearchResults"></a>
# **listFileContentSearchResults**
> List&lt;FileContentSearchResult&gt; listFileContentSearchResults(imageDigest)

Return a list of analyzer artifacts of the specified type

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
    String imageDigest = "imageDigest_example"; // String | 
    try {
      List<FileContentSearchResult> result = apiInstance.listFileContentSearchResults(imageDigest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFileContentSearchResults");
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
| **imageDigest** | **String**|  | |

### Return type

[**List&lt;FileContentSearchResult&gt;**](FileContentSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of file metadata objects |  -  |
| **404** | Image not found in this service |  -  |

<a id="listRetrievedFiles"></a>
# **listRetrievedFiles**
> List&lt;RetrievedFile&gt; listRetrievedFiles(imageDigest)

Return a list of analyzer artifacts of the specified type

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
    String imageDigest = "imageDigest_example"; // String | 
    try {
      List<RetrievedFile> result = apiInstance.listRetrievedFiles(imageDigest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRetrievedFiles");
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
| **imageDigest** | **String**|  | |

### Return type

[**List&lt;RetrievedFile&gt;**](RetrievedFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of file metadata objects |  -  |
| **404** | Image not found in this service |  -  |

<a id="listSecretSearchResults"></a>
# **listSecretSearchResults**
> List&lt;SecretSearchResult&gt; listSecretSearchResults(imageDigest)

Return a list of analyzer artifacts of the specified type

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
    String imageDigest = "imageDigest_example"; // String | 
    try {
      List<SecretSearchResult> result = apiInstance.listSecretSearchResults(imageDigest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSecretSearchResults");
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
| **imageDigest** | **String**|  | |

### Return type

[**List&lt;SecretSearchResult&gt;**](SecretSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of file metadata objects |  -  |
| **404** | Image not found in this service |  -  |

<a id="ping"></a>
# **ping**
> String ping()



Simple status check

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
      String result = apiInstance.ping();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ping");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Version check response, returns the api version prefix (e.g. &#39;v1&#39;) |  -  |

<a id="versionCheck"></a>
# **versionCheck**
> ServiceVersion versionCheck()



Returns the version object for the service, including db schema version info

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
      ServiceVersion result = apiInstance.versionCheck();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionCheck");
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

[**ServiceVersion**](ServiceVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Version object describing version state |  -  |

