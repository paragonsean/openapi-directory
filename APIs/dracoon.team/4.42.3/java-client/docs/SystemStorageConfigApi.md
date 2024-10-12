# SystemStorageConfigApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createS3Config**](SystemStorageConfigApi.md#createS3Config) | **POST** /v4/system/config/storage/s3 | Create S3 storage configuration |
| [**createS3Tag**](SystemStorageConfigApi.md#createS3Tag) | **POST** /v4/system/config/storage/s3/tags | Create S3 tag |
| [**removeS3Tag**](SystemStorageConfigApi.md#removeS3Tag) | **DELETE** /v4/system/config/storage/s3/tags/{id} | Remove S3 tag |
| [**request3Config**](SystemStorageConfigApi.md#request3Config) | **GET** /v4/system/config/storage/s3 | Request S3 storage configuration |
| [**requestS3Tag**](SystemStorageConfigApi.md#requestS3Tag) | **GET** /v4/system/config/storage/s3/tags/{id} | Request S3 tag |
| [**requestS3TagList**](SystemStorageConfigApi.md#requestS3TagList) | **GET** /v4/system/config/storage/s3/tags | Request list of configured S3 tags |
| [**updateS3Config**](SystemStorageConfigApi.md#updateS3Config) | **PUT** /v4/system/config/storage/s3 | Update S3 storage configuration |


<a id="createS3Config"></a>
# **createS3Config**
> S3Config createS3Config(s3ConfigCreateRequest, xSdsAuthToken)

Create S3 storage configuration

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Create new S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New S3 configuration is created.  ### Further Information: Forbidden characters in bucket names: [&#x60;.&#x60;]   &#x60;bucketName&#x60; and &#x60;endpointUrl&#x60; are deprecated, use &#x60;bucketUrl&#x60; instead.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemStorageConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemStorageConfigApi apiInstance = new SystemStorageConfigApi(defaultClient);
    S3ConfigCreateRequest s3ConfigCreateRequest = new S3ConfigCreateRequest(); // S3ConfigCreateRequest | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      S3Config result = apiInstance.createS3Config(s3ConfigCreateRequest, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemStorageConfigApi#createS3Config");
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
| **s3ConfigCreateRequest** | [**S3ConfigCreateRequest**](S3ConfigCreateRequest.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**S3Config**](S3Config.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="createS3Tag"></a>
# **createS3Tag**
> S3Tag createS3Tag(s3TagCreateRequest, xSdsAuthToken)

Create S3 tag

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Create new S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New S3 tag is created.  ### Further Information: * Maximum key length: **128** characters.   * Maximum value length: **256** characters.   * Both S3 tag key and value are **case-sensitive** strings.   * Maximum of **20 mandatory S3 tags** is allowed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemStorageConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemStorageConfigApi apiInstance = new SystemStorageConfigApi(defaultClient);
    S3TagCreateRequest s3TagCreateRequest = new S3TagCreateRequest(); // S3TagCreateRequest | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      S3Tag result = apiInstance.createS3Tag(s3TagCreateRequest, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemStorageConfigApi#createS3Tag");
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
| **s3TagCreateRequest** | [**S3TagCreateRequest**](S3TagCreateRequest.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**S3Tag**](S3Tag.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |

<a id="removeS3Tag"></a>
# **removeS3Tag**
> removeS3Tag(id, xSdsAuthToken)

Remove S3 tag

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Delete S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tag gets deleted.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemStorageConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemStorageConfigApi apiInstance = new SystemStorageConfigApi(defaultClient);
    Long id = 56L; // Long | S3 tag ID
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.removeS3Tag(id, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemStorageConfigApi#removeS3Tag");
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
| **id** | **Long**| S3 tag ID | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="request3Config"></a>
# **request3Config**
> S3Config request3Config(xSdsAuthToken)

Request S3 storage configuration

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Retrieve S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 configuration is returned.  ### Further Information: None.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemStorageConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemStorageConfigApi apiInstance = new SystemStorageConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      S3Config result = apiInstance.request3Config(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemStorageConfigApi#request3Config");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**S3Config**](S3Config.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestS3Tag"></a>
# **requestS3Tag**
> S3Tag requestS3Tag(id, xSdsAuthToken)

Request S3 tag

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Retrieve single S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tag is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemStorageConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemStorageConfigApi apiInstance = new SystemStorageConfigApi(defaultClient);
    Long id = 56L; // Long | S3 tag ID
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      S3Tag result = apiInstance.requestS3Tag(id, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemStorageConfigApi#requestS3Tag");
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
| **id** | **Long**| S3 tag ID | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**S3Tag**](S3Tag.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestS3TagList"></a>
# **requestS3TagList**
> S3TagList requestS3TagList(xSdsAuthToken)

Request list of configured S3 tags

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Retrieve all configured S3 tags.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tags are returned.  ### Further Information: An empty list is returned if no S3 tags are found / configured.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemStorageConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemStorageConfigApi apiInstance = new SystemStorageConfigApi(defaultClient);
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      S3TagList result = apiInstance.requestS3TagList(xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemStorageConfigApi#requestS3TagList");
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
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**S3TagList**](S3TagList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="updateS3Config"></a>
# **updateS3Config**
> S3Config updateS3Config(s3ConfigUpdateRequest, xSdsAuthToken)

Update S3 storage configuration

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Update existing S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 configuration is updated.  ### Further Information: Forbidden characters in bucket names: [&#x60;.&#x60;]   &#x60;bucketName&#x60; and &#x60;endpointUrl&#x60; are deprecated, use &#x60;bucketUrl&#x60; instead.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemStorageConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SystemStorageConfigApi apiInstance = new SystemStorageConfigApi(defaultClient);
    S3ConfigUpdateRequest s3ConfigUpdateRequest = new S3ConfigUpdateRequest(); // S3ConfigUpdateRequest | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      S3Config result = apiInstance.updateS3Config(s3ConfigUpdateRequest, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemStorageConfigApi#updateS3Config");
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
| **s3ConfigUpdateRequest** | [**S3ConfigUpdateRequest**](S3ConfigUpdateRequest.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**S3Config**](S3Config.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

