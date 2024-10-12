# SharesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDownloadShare**](SharesApi.md#createDownloadShare) | **POST** /v4/shares/downloads | Create new Download Share |
| [**createUploadShare**](SharesApi.md#createUploadShare) | **POST** /v4/shares/uploads | Create new Upload Share |
| [**deleteDownloadShares**](SharesApi.md#deleteDownloadShares) | **DELETE** /v4/shares/downloads | Remove Download Shares |
| [**deleteUploadShares**](SharesApi.md#deleteUploadShares) | **DELETE** /v4/shares/uploads | Remove Upload Shares |
| [**removeDownloadShare**](SharesApi.md#removeDownloadShare) | **DELETE** /v4/shares/downloads/{share_id} | Remove Download Share |
| [**removeUploadShare**](SharesApi.md#removeUploadShare) | **DELETE** /v4/shares/uploads/{share_id} | Remove Upload Share |
| [**requestDownloadShare**](SharesApi.md#requestDownloadShare) | **GET** /v4/shares/downloads/{share_id} | Request Download Share |
| [**requestDownloadShareQr**](SharesApi.md#requestDownloadShareQr) | **GET** /v4/shares/downloads/{share_id}/qr | Request Download Share via QR Code |
| [**requestDownloadShares**](SharesApi.md#requestDownloadShares) | **GET** /v4/shares/downloads | Request list of Download Shares |
| [**requestUploadShare**](SharesApi.md#requestUploadShare) | **GET** /v4/shares/uploads/{share_id} | Request Upload Share |
| [**requestUploadShareQr**](SharesApi.md#requestUploadShareQr) | **GET** /v4/shares/uploads/{share_id}/qr | Request Upload Share via QR Code |
| [**requestUploadShares**](SharesApi.md#requestUploadShares) | **GET** /v4/shares/uploads | Request list of Upload Shares |
| [**sendDownloadShareLinkViaEmail**](SharesApi.md#sendDownloadShareLinkViaEmail) | **POST** /v4/shares/downloads/{share_id}/email | Send an existing Download Share link via email |
| [**sendUploadShareLinkViaEmail**](SharesApi.md#sendUploadShareLinkViaEmail) | **POST** /v4/shares/uploads/{share_id}/email | Send an existing Upload Share link via email |
| [**updateDownloadShare**](SharesApi.md#updateDownloadShare) | **PUT** /v4/shares/downloads/{share_id} | Update Download Share |
| [**updateDownloadShares**](SharesApi.md#updateDownloadShares) | **PUT** /v4/shares/downloads | Update a list of Download Shares |
| [**updateUploadShare**](SharesApi.md#updateUploadShare) | **PUT** /v4/shares/uploads/{share_id} | Update Upload Share |
| [**updateUploadShares**](SharesApi.md#updateUploadShares) | **PUT** /v4/shares/uploads | Update List of Upload Shares |


<a id="createDownloadShare"></a>
# **createDownloadShare**
> DownloadShare createDownloadShare(createDownloadShareRequest, xSdsDateFormat, xSdsAuthToken)

Create new Download Share

### Description: Create a new Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is created.  ### Further Information:  If the target node is a room: subordinary rooms are excluded from a Download Share.  * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Use &#x60;POST /shares/downloads/{share_id}/email&#x60; API for sending emails.    Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    CreateDownloadShareRequest createDownloadShareRequest = new CreateDownloadShareRequest(); // CreateDownloadShareRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      DownloadShare result = apiInstance.createDownloadShare(createDownloadShareRequest, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#createDownloadShare");
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
| **createDownloadShareRequest** | [**CreateDownloadShareRequest**](CreateDownloadShareRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**DownloadShare**](DownloadShare.md)

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
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |
| **502** | Bad Gateway |  -  |

<a id="createUploadShare"></a>
# **createUploadShare**
> UploadShare createUploadShare(createUploadShareRequest, xSdsDateFormat, xSdsAuthToken)

Create new Upload Share

### Description: Create a new Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is created.  ### Further Information:  * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]    Use &#x60;POST /shares/uploads/{share_id}/email&#x60; API for sending emails.  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    CreateUploadShareRequest createUploadShareRequest = new CreateUploadShareRequest(); // CreateUploadShareRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      UploadShare result = apiInstance.createUploadShare(createUploadShareRequest, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#createUploadShare");
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
| **createUploadShareRequest** | [**CreateUploadShareRequest**](CreateUploadShareRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**UploadShare**](UploadShare.md)

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
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |
| **502** | Bad Gateway |  -  |

<a id="deleteDownloadShares"></a>
# **deleteDownloadShares**
> deleteDownloadShares(deleteDownloadSharesRequest, xSdsAuthToken)

Remove Download Shares

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.21.0&lt;/h3&gt;  ### Functional Description: Delete multiple Download Shares.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target nodes.  ### Postcondition: Download Shares are deleted.  ### Further Information: Only the Download Shares are removed; the referenced files or containers persists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    DeleteDownloadSharesRequest deleteDownloadSharesRequest = new DeleteDownloadSharesRequest(); // DeleteDownloadSharesRequest | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.deleteDownloadShares(deleteDownloadSharesRequest, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#deleteDownloadShares");
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
| **deleteDownloadSharesRequest** | [**DeleteDownloadSharesRequest**](DeleteDownloadSharesRequest.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
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

<a id="deleteUploadShares"></a>
# **deleteUploadShares**
> deleteUploadShares(deleteUploadSharesRequest, xSdsAuthToken)

Remove Upload Shares

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.21.0&lt;/h3&gt;  ### Functional Description: Delete multiple Upload Shares (aka Upload Accounts).  ### Precondition: User has _\&quot;manage upload share\&quot;_ permissions on target containers.  ### Postcondition: Upload Shares are deleted.  ### Further Information: Only the Upload Shares are removed; already uploaded files and the target container persist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    DeleteUploadSharesRequest deleteUploadSharesRequest = new DeleteUploadSharesRequest(); // DeleteUploadSharesRequest | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.deleteUploadShares(deleteUploadSharesRequest, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#deleteUploadShares");
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
| **deleteUploadSharesRequest** | [**DeleteUploadSharesRequest**](DeleteUploadSharesRequest.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
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

<a id="removeDownloadShare"></a>
# **removeDownloadShare**
> removeDownloadShare(shareId, xSdsAuthToken)

Remove Download Share

### Description: Delete a Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is deleted.  ### Further Information: Only the Download Share is removed; the referenced file or container persists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.removeDownloadShare(shareId, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#removeDownloadShare");
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
| **shareId** | **Long**| Share ID | |
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

<a id="removeUploadShare"></a>
# **removeUploadShare**
> removeUploadShare(shareId, xSdsAuthToken)

Remove Upload Share

### Description: Delete an Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is deleted.  ### Further Information: Only the Upload Share is removed; already uploaded files and the target container persist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.removeUploadShare(shareId, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#removeUploadShare");
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
| **shareId** | **Long**| Share ID | |
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

<a id="requestDownloadShare"></a>
# **requestDownloadShare**
> DownloadShare requestDownloadShare(shareId, xSdsDateFormat, xSdsAuthToken)

Request Download Share

### Description:   Retrieve detailed information about one Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is returned  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      DownloadShare result = apiInstance.requestDownloadShare(shareId, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#requestDownloadShare");
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
| **shareId** | **Long**| Share ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**DownloadShare**](DownloadShare.md)

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

<a id="requestDownloadShareQr"></a>
# **requestDownloadShareQr**
> DownloadShare requestDownloadShareQr(shareId, xSdsDateFormat, xSdsAuthToken)

Request Download Share via QR Code

### Description:   Retrieve detailed information about one Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is returned  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      DownloadShare result = apiInstance.requestDownloadShareQr(shareId, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#requestDownloadShareQr");
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
| **shareId** | **Long**| Share ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**DownloadShare**](DownloadShare.md)

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

<a id="requestDownloadShares"></a>
# **requestDownloadShares**
> DownloadShareList requestDownloadShares(xSdsDateFormat, filter, sort, offset, limit, xSdsAuthToken)

Request list of Download Shares

### Description:   Retrieve a list of Download Shares.  ### Precondition: Authenticated user.  ### Postcondition: List of available Download Shares is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical (**AND**). createdBy and updatedBy searches several user-related attributes.  Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:searchString_1|createdBy:cn:searchString_2&#x60; Filter by file name contains &#x60;searchString_1&#x60; **AND** creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Alias or node name filter | &#x60;cn&#x60; | Alias or node name contains value. | &#x60;search String&#x60; | | &#x60;createdAt&#x60; | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;createdBy&#x60; | Creator info filter | &#x60;cn, eq&#x60; | Creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;createdById&#x60; | Creator ID filter | &#x60;eq&#x60; | Creator ID equals value. | &#x60;positive Integer&#x60; | | &#x60;accessKey&#x60; | Share access key filter | &#x60;cn&#x60; | Share access key contains values. | &#x60;search String&#x60; | | &#x60;nodeId&#x60; | Source node ID | &#x60;eq&#x60; | Source node (room, folder, file) ID equals value. | &#x60;positive Integer&#x60; | | &#x60;updatedBy&#x60; | Modifier info filter | &#x60;cn, eq&#x60; | Modifier info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;updatedById&#x60; | Modifier ID filter | &#x60;eq&#x60; | Modifier ID equals value. | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;userId&#x60;&lt;/del&gt;  | Creator user ID | &#x60;eq&#x60; | Creator user ID equals value. Use &#x60;createdById&#x60; instead | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:asc|expireAt:desc&#x60;   Sort by &#x60;name&#x60; ascending **AND** by &#x60;expireAt&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Alias or node name | | &#x60;notifyCreator&#x60; | Notify creator on every download | | &#x60;expireAt&#x60; | Expiration date | | &#x60;createdAt&#x60; | Creation date | | &#x60;createdBy&#x60; | Creator first name, last name | | &#x60;classification&#x60; | Classification ID:&lt;ul&gt;&lt;li&gt;1 - public&lt;/li&gt;&lt;li&gt;2 - internal&lt;/li&gt;&lt;li&gt;3 - confidential&lt;/li&gt;&lt;li&gt;4 - strictly confidential&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      DownloadShareList result = apiInstance.requestDownloadShares(xSdsDateFormat, filter, sort, offset, limit, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#requestDownloadShares");
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
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**DownloadShareList**](DownloadShareList.md)

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
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestUploadShare"></a>
# **requestUploadShare**
> UploadShare requestUploadShare(shareId, xSdsDateFormat, xSdsAuthToken)

Request Upload Share

### Description:   Retrieve detailed information about one Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      UploadShare result = apiInstance.requestUploadShare(shareId, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#requestUploadShare");
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
| **shareId** | **Long**| Share ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**UploadShare**](UploadShare.md)

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

<a id="requestUploadShareQr"></a>
# **requestUploadShareQr**
> UploadShare requestUploadShareQr(shareId, xSdsDateFormat, xSdsAuthToken)

Request Upload Share via QR Code

### Description:   Retrieve detailed information about one Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      UploadShare result = apiInstance.requestUploadShareQr(shareId, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#requestUploadShareQr");
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
| **shareId** | **Long**| Share ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**UploadShare**](UploadShare.md)

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

<a id="requestUploadShares"></a>
# **requestUploadShares**
> UploadShareList requestUploadShares(xSdsDateFormat, filter, sort, offset, limit, xSdsAuthToken)

Request list of Upload Shares

### Description:   Retrieve a list of Upload Shares (aka File Requests).  ### Precondition: Authenticated user.  ### Postcondition: List of available Upload Shares is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical (**AND**). createdBy and updatedBy searches several user-related attributes. Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:searchString_1|createdBy:cn:searchString_2&#x60;   Filter by alias name contains &#x60;searchString_1&#x60; **AND** creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Alias name filter | &#x60;cn&#x60; | Alias name contains value. | &#x60;search String&#x60; | | &#x60;createdAt&#x60; | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;createdBy&#x60; | Creator info filter | &#x60;cn, eq&#x60; | Creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;createdById&#x60; | Creator ID filter | &#x60;eq&#x60; | Creator ID equals value. | &#x60;positive Integer&#x60; | | &#x60;accessKey&#x60; | Share access key filter | &#x60;cn&#x60; | Share access key contains values. | &#x60;search String&#x60; | | &#x60;userId&#x60; | Creator user ID | &#x60;eq&#x60; | Creator user ID equals value. | &#x60;positive Integer&#x60; | | &#x60;targetId&#x60; | Target node ID | &#x60;eq&#x60; | Target node (room, folder) ID equals value. | &#x60;positive Integer&#x60; | | &#x60;updatedBy&#x60; | Modifier info filter | &#x60;cn, eq&#x60; | Modifier info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;updatedById&#x60; | Modifier ID filter | &#x60;eq&#x60; | Modifier ID equals value. | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;targetId&#x60;&lt;/del&gt; | Target node ID | &#x60;cn&#x60; | Target node (room, folder) ID equals value. | &#x60;positive Integer&#x60; | | &lt;del&gt;&#x60;userId&#x60; &lt;/del&gt;| Creator user ID | &#x60;eq&#x60; | Creator user ID equals value. Use &#x60;createdById&#x60; instead. | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ---  Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:asc|expireAt:desc&#x60;   Sort by &#x60;name&#x60; ascending **AND** by &#x60;expireAt&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Alias name | | &#x60;notifyCreator&#x60; | Notify creator on every upload | | &#x60;expireAt&#x60; | Expiration date | | &#x60;createdAt&#x60; | Creation date | | &#x60;createdBy&#x60; | Creator first name, last name |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      UploadShareList result = apiInstance.requestUploadShares(xSdsDateFormat, filter, sort, offset, limit, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#requestUploadShares");
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
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**UploadShareList**](UploadShareList.md)

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
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="sendDownloadShareLinkViaEmail"></a>
# **sendDownloadShareLinkViaEmail**
> sendDownloadShareLinkViaEmail(shareId, downloadShareLinkEmail, xSdsAuthToken)

Send an existing Download Share link via email

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Send an email to specific recipients for existing Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share link successfully sent.  ### Further Information:  * Forbidden characters in the email body: [&#x60;&lt;&#x60;, &#x60;&gt;&#x60;] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    DownloadShareLinkEmail downloadShareLinkEmail = new DownloadShareLinkEmail(); // DownloadShareLinkEmail | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.sendDownloadShareLinkViaEmail(shareId, downloadShareLinkEmail, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sendDownloadShareLinkViaEmail");
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
| **shareId** | **Long**| Share ID | |
| **downloadShareLinkEmail** | [**DownloadShareLinkEmail**](DownloadShareLinkEmail.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
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

<a id="sendUploadShareLinkViaEmail"></a>
# **sendUploadShareLinkViaEmail**
> sendUploadShareLinkViaEmail(shareId, uploadShareLinkEmail, xSdsAuthToken)

Send an existing Upload Share link via email

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Send an email to specific recipients for existing Upload Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share link successfully sent.  ### Further Information:  * Forbidden characters in the email body: [&#x60;&lt;&#x60;, &#x60;&gt;&#x60;] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    UploadShareLinkEmail uploadShareLinkEmail = new UploadShareLinkEmail(); // UploadShareLinkEmail | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.sendUploadShareLinkViaEmail(shareId, uploadShareLinkEmail, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#sendUploadShareLinkViaEmail");
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
| **shareId** | **Long**| Share ID | |
| **uploadShareLinkEmail** | [**UploadShareLinkEmail**](UploadShareLinkEmail.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
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

<a id="updateDownloadShare"></a>
# **updateDownloadShare**
> DownloadShare updateDownloadShare(shareId, updateDownloadShareRequest, xSdsDateFormat, xSdsAuthToken)

Update Download Share

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Update an existing Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is successfully updated.  ### Further Information: * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    UpdateDownloadShareRequest updateDownloadShareRequest = new UpdateDownloadShareRequest(); // UpdateDownloadShareRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      DownloadShare result = apiInstance.updateDownloadShare(shareId, updateDownloadShareRequest, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#updateDownloadShare");
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
| **shareId** | **Long**| Share ID | |
| **updateDownloadShareRequest** | [**UpdateDownloadShareRequest**](UpdateDownloadShareRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**DownloadShare**](DownloadShare.md)

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
| **502** | Bad Gateway |  -  |

<a id="updateDownloadShares"></a>
# **updateDownloadShares**
> updateDownloadShares(updateDownloadSharesBulkRequest, xSdsAuthToken)

Update a list of Download Shares

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description: Update a list of existing Download Shares.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Shares are successfully updated.  ### Further Information: Maximum number of shares is 200

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    UpdateDownloadSharesBulkRequest updateDownloadSharesBulkRequest = new UpdateDownloadSharesBulkRequest(); // UpdateDownloadSharesBulkRequest | 
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.updateDownloadShares(updateDownloadSharesBulkRequest, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#updateDownloadShares");
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
| **updateDownloadSharesBulkRequest** | [**UpdateDownloadSharesBulkRequest**](UpdateDownloadSharesBulkRequest.md)|  | |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No Content |  -  |
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |
| **502** | Bad Gateway |  -  |

<a id="updateUploadShare"></a>
# **updateUploadShare**
> UploadShare updateUploadShare(shareId, updateUploadShareRequest, xSdsDateFormat, xSdsAuthToken)

Update Upload Share

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Update existing Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share successfully updated.  ### Further Information:  * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    Long shareId = 56L; // Long | Share ID
    UpdateUploadShareRequest updateUploadShareRequest = new UpdateUploadShareRequest(); // UpdateUploadShareRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      UploadShare result = apiInstance.updateUploadShare(shareId, updateUploadShareRequest, xSdsDateFormat, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#updateUploadShare");
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
| **shareId** | **Long**| Share ID | |
| **updateUploadShareRequest** | [**UpdateUploadShareRequest**](UpdateUploadShareRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**UploadShare**](UploadShare.md)

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
| **502** | Bad Gateway |  -  |

<a id="updateUploadShares"></a>
# **updateUploadShares**
> updateUploadShares(updateUploadSharesBulkRequest, xSdsDateFormat, xSdsAuthToken)

Update List of Upload Shares

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description: Update a list of existing Upload Shares (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Shares successfully updated.  ### Further Information: Maximum number of shares is 200

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SharesApi apiInstance = new SharesApi(defaultClient);
    UpdateUploadSharesBulkRequest updateUploadSharesBulkRequest = new UpdateUploadSharesBulkRequest(); // UpdateUploadSharesBulkRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      apiInstance.updateUploadShares(updateUploadSharesBulkRequest, xSdsDateFormat, xSdsAuthToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharesApi#updateUploadShares");
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
| **updateUploadSharesBulkRequest** | [**UpdateUploadSharesBulkRequest**](UpdateUploadSharesBulkRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

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
| **502** | Bad Gateway |  -  |

