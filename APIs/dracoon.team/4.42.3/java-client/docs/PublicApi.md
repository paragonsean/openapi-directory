# PublicApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelFileUploadViaShare**](PublicApi.md#cancelFileUploadViaShare) | **DELETE** /v4/public/shares/uploads/{access_key}/{upload_id} | Cancel file upload |
| [**checkPublicDownloadSharePassword**](PublicApi.md#checkPublicDownloadSharePassword) | **HEAD** /v4/public/shares/downloads/{access_key} | Check public Download Share password |
| [**completeFileUploadViaShare**](PublicApi.md#completeFileUploadViaShare) | **PUT** /v4/public/shares/uploads/{access_key}/{upload_id} | Complete file upload |
| [**completeS3FileUploadViaShare**](PublicApi.md#completeS3FileUploadViaShare) | **PUT** /v4/public/shares/uploads/{access_key}/{upload_id}/s3 | Complete S3 file upload |
| [**createShareUploadChannel**](PublicApi.md#createShareUploadChannel) | **POST** /v4/public/shares/uploads/{access_key} | Create new file upload channel |
| [**downloadFileViaTokenPublic**](PublicApi.md#downloadFileViaTokenPublic) | **GET** /v4/public/shares/downloads/{access_key}/{token} | Download file with token |
| [**downloadFileViaTokenPublic1**](PublicApi.md#downloadFileViaTokenPublic1) | **HEAD** /v4/public/shares/downloads/{access_key}/{token} | Download file with token |
| [**generateDownloadUrlPublic**](PublicApi.md#generateDownloadUrlPublic) | **POST** /v4/public/shares/downloads/{access_key} | Generate download URL |
| [**generatePresignedUrlsPublic**](PublicApi.md#generatePresignedUrlsPublic) | **POST** /v4/public/shares/uploads/{access_key}/{upload_id}/s3_urls | Generate presigned URLs for S3 file upload |
| [**requestActiveDirectoryAuthInfo**](PublicApi.md#requestActiveDirectoryAuthInfo) | **GET** /v4/public/system/info/auth/ad | Request Active Directory authentication information |
| [**requestOpenIdAuthInfo**](PublicApi.md#requestOpenIdAuthInfo) | **GET** /v4/public/system/info/auth/openid | Request OpenID Connect provider authentication information |
| [**requestPublicDownloadShareInfo**](PublicApi.md#requestPublicDownloadShareInfo) | **GET** /v4/public/shares/downloads/{access_key} | Request public Download Share information |
| [**requestPublicUploadShareInfo**](PublicApi.md#requestPublicUploadShareInfo) | **GET** /v4/public/shares/uploads/{access_key} | Request public Upload Share information |
| [**requestSoftwareVersion**](PublicApi.md#requestSoftwareVersion) | **GET** /v4/public/software/version | Request software version information |
| [**requestSystemInfo**](PublicApi.md#requestSystemInfo) | **GET** /v4/public/system/info | Request system information |
| [**requestSystemTime**](PublicApi.md#requestSystemTime) | **GET** /v4/public/time | Request system time |
| [**requestThirdPartyDependencies**](PublicApi.md#requestThirdPartyDependencies) | **GET** /v4/public/software/third_party_dependencies | Request third-party software dependencies |
| [**requestUploadStatusPublic**](PublicApi.md#requestUploadStatusPublic) | **GET** /v4/public/shares/uploads/{access_key}/{upload_id} | Request status of S3 file upload |
| [**uploadFileAsMultipartPublic1**](PublicApi.md#uploadFileAsMultipartPublic1) | **POST** /v4/public/shares/uploads/{access_key}/{upload_id} | Upload file |


<a id="cancelFileUploadViaShare"></a>
# **cancelFileUploadViaShare**
> cancelFileUploadViaShare(accessKey, uploadId)

Cancel file upload

### Description: Abort (chunked) upload via Upload Share.  ### Precondition: Valid Upload ID.  ### Postcondition: Aborts upload and invalidates upload ID / token.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String uploadId = "uploadId_example"; // String | Upload channel ID
    try {
      apiInstance.cancelFileUploadViaShare(accessKey, uploadId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#cancelFileUploadViaShare");
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
| **accessKey** | **String**| Access key | |
| **uploadId** | **String**| Upload channel ID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **504** | Gateway Timeout |  -  |
| **507** | Insufficient Storage |  -  |

<a id="checkPublicDownloadSharePassword"></a>
# **checkPublicDownloadSharePassword**
> checkPublicDownloadSharePassword(accessKey, password)

Check public Download Share password

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Check password for a public Download Share  ### Precondition: None.  ### Postcondition: None.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String password = "password_example"; // String | Download share password
    try {
      apiInstance.checkPublicDownloadSharePassword(accessKey, password);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#checkPublicDownloadSharePassword");
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
| **accessKey** | **String**| Access key | |
| **password** | **String**| Download share password | [optional] |

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
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="completeFileUploadViaShare"></a>
# **completeFileUploadViaShare**
> PublicUploadedFileData completeFileUploadViaShare(accessKey, uploadId, xSdsDateFormat, userFileKeyList)

Complete file upload

### Description: Finalize (chunked) upload via Upload Share.  ### Precondition: Valid upload ID.   Only returns users that owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: Finalizes upload.  ### Further Information: Chunked uploads (range requests) are supported.    Please ensure that all chunks have been transferred correctly before finishing the upload.   If file hash has been created in time a &#x60;201 Created&#x60; will be responded and hash will be part of response, otherwise it will be a &#x60;202 Accepted&#x60; without it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String uploadId = "uploadId_example"; // String | Upload channel ID
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    UserFileKeyList userFileKeyList = new UserFileKeyList(); // UserFileKeyList | 
    try {
      PublicUploadedFileData result = apiInstance.completeFileUploadViaShare(accessKey, uploadId, xSdsDateFormat, userFileKeyList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#completeFileUploadViaShare");
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
| **accessKey** | **String**| Access key | |
| **uploadId** | **String**| Upload channel ID | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **userFileKeyList** | [**UserFileKeyList**](UserFileKeyList.md)|  | [optional] |

### Return type

[**PublicUploadedFileData**](PublicUploadedFileData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |
| **504** | Gateway Timeout |  -  |
| **507** | Insufficient Storage |  -  |

<a id="completeS3FileUploadViaShare"></a>
# **completeS3FileUploadViaShare**
> completeS3FileUploadViaShare(accessKey, uploadId, completeS3ShareUploadRequest)

Complete S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Finishes a S3 file upload and closes the corresponding upload channel.  ### Precondition: Valid upload ID.   Only returns users that owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: Upload channel is closed. S3 multipart upload request is completed.  ### Further Information: None. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String uploadId = "uploadId_example"; // String | Upload channel ID
    CompleteS3ShareUploadRequest completeS3ShareUploadRequest = new CompleteS3ShareUploadRequest(); // CompleteS3ShareUploadRequest | 
    try {
      apiInstance.completeS3FileUploadViaShare(accessKey, uploadId, completeS3ShareUploadRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#completeS3FileUploadViaShare");
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
| **accessKey** | **String**| Access key | |
| **uploadId** | **String**| Upload channel ID | |
| **completeS3ShareUploadRequest** | [**CompleteS3ShareUploadRequest**](CompleteS3ShareUploadRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="createShareUploadChannel"></a>
# **createShareUploadChannel**
> CreateShareUploadChannelResponse createShareUploadChannel(accessKey, createShareUploadChannelRequest)

Create new file upload channel

### Description:   Create a new upload channel.  ### Precondition: None.  ### Postcondition: Upload channel is created and corresponding upload URL, token &amp; upload ID are returned.  ### Further Information: Use &#x60;uploadUrl&#x60; the upload &#x60;token&#x60; is deprecated.    Please provide the size of the intended upload so that the quota can be checked in advanced and no data is transferred unnecessarily.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    CreateShareUploadChannelRequest createShareUploadChannelRequest = new CreateShareUploadChannelRequest(); // CreateShareUploadChannelRequest | 
    try {
      CreateShareUploadChannelResponse result = apiInstance.createShareUploadChannel(accessKey, createShareUploadChannelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#createShareUploadChannel");
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
| **accessKey** | **String**| Access key | |
| **createShareUploadChannelRequest** | [**CreateShareUploadChannelRequest**](CreateShareUploadChannelRequest.md)|  | |

### Return type

[**CreateShareUploadChannelResponse**](CreateShareUploadChannelResponse.md)

### Authorization

No authorization required

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
| **504** | Gateway Timeout |  -  |
| **507** | Insufficient Storage |  -  |

<a id="downloadFileViaTokenPublic"></a>
# **downloadFileViaTokenPublic**
> downloadFileViaTokenPublic(accessKey, token, range, genericMimetype, inline)

Download file with token

### Description:   Download a file (or zip archive if target is a folder or room).  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.   Range requests are illegal for zip archive download.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String token = "token_example"; // String | Download token
    String range = "range_example"; // String | Range   e.g. `bytes=0-999`
    Boolean genericMimetype = true; // Boolean | Always return `application/octet-stream` instead of specific mimetype
    Boolean inline = true; // Boolean | Use Content-Disposition: `inline` instead of `attachment`
    try {
      apiInstance.downloadFileViaTokenPublic(accessKey, token, range, genericMimetype, inline);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#downloadFileViaTokenPublic");
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
| **accessKey** | **String**| Access key | |
| **token** | **String**| Download token | |
| **range** | **String**| Range   e.g. &#x60;bytes&#x3D;0-999&#x60; | [optional] |
| **genericMimetype** | **Boolean**| Always return &#x60;application/octet-stream&#x60; instead of specific mimetype | [optional] |
| **inline** | **Boolean**| Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **206** | Partial Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **416** | Range Not Satisfiable |  -  |

<a id="downloadFileViaTokenPublic1"></a>
# **downloadFileViaTokenPublic1**
> downloadFileViaTokenPublic1(accessKey, token, range, genericMimetype, inline)

Download file with token

### Description:   Download a file (or zip archive if target is a folder or room).  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.   Range requests are illegal for zip archive download.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String token = "token_example"; // String | Download token
    String range = "range_example"; // String | Range   e.g. `bytes=0-999`
    Boolean genericMimetype = true; // Boolean | Always return `application/octet-stream` instead of specific mimetype
    Boolean inline = true; // Boolean | Use Content-Disposition: `inline` instead of `attachment`
    try {
      apiInstance.downloadFileViaTokenPublic1(accessKey, token, range, genericMimetype, inline);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#downloadFileViaTokenPublic1");
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
| **accessKey** | **String**| Access key | |
| **token** | **String**| Download token | |
| **range** | **String**| Range   e.g. &#x60;bytes&#x3D;0-999&#x60; | [optional] |
| **genericMimetype** | **Boolean**| Always return &#x60;application/octet-stream&#x60; instead of specific mimetype | [optional] |
| **inline** | **Boolean**| Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **206** | Partial Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **416** | Range Not Satisfiable |  -  |

<a id="generateDownloadUrlPublic"></a>
# **generateDownloadUrlPublic**
> PublicDownloadTokenGenerateResponse generateDownloadUrlPublic(accessKey, publicDownloadTokenGenerateRequest)

Generate download URL

### Description: Generate a download URL to retrieve a shared file.  ### Precondition: None.  ### Postcondition: Download URL and token are generated and returned.  ### Further Information: Use &#x60;downloadUrl&#x60; the download &#x60;token&#x60; is deprecated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    PublicDownloadTokenGenerateRequest publicDownloadTokenGenerateRequest = new PublicDownloadTokenGenerateRequest(); // PublicDownloadTokenGenerateRequest | 
    try {
      PublicDownloadTokenGenerateResponse result = apiInstance.generateDownloadUrlPublic(accessKey, publicDownloadTokenGenerateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#generateDownloadUrlPublic");
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
| **accessKey** | **String**| Access key | |
| **publicDownloadTokenGenerateRequest** | [**PublicDownloadTokenGenerateRequest**](PublicDownloadTokenGenerateRequest.md)|  | [optional] |

### Return type

[**PublicDownloadTokenGenerateResponse**](PublicDownloadTokenGenerateResponse.md)

### Authorization

No authorization required

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

<a id="generatePresignedUrlsPublic"></a>
# **generatePresignedUrlsPublic**
> PresignedUrlList generatePresignedUrlsPublic(accessKey, uploadId, generatePresignedUrlsRequest, xSdsDateFormat)

Generate presigned URLs for S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Generate presigned URLs for S3 file upload.  ### Precondition: Valid upload ID  ### Postcondition: List of presigned URLs is returned.  ### Further Information: The size for each part must be &gt;&#x3D; 5 MB, except for the last part.   The part number of the first part in S3 is 1 (not 0).   Use HTTP method &#x60;PUT&#x60; for uploading bytes via presigned URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String uploadId = "uploadId_example"; // String | Upload channel ID
    GeneratePresignedUrlsRequest generatePresignedUrlsRequest = new GeneratePresignedUrlsRequest(); // GeneratePresignedUrlsRequest | 
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    try {
      PresignedUrlList result = apiInstance.generatePresignedUrlsPublic(accessKey, uploadId, generatePresignedUrlsRequest, xSdsDateFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#generatePresignedUrlsPublic");
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
| **accessKey** | **String**| Access key | |
| **uploadId** | **String**| Upload channel ID | |
| **generatePresignedUrlsRequest** | [**GeneratePresignedUrlsRequest**](GeneratePresignedUrlsRequest.md)|  | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |

### Return type

[**PresignedUrlList**](PresignedUrlList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |
| **504** | Gateway Timeout |  -  |
| **507** | Insufficient Storage |  -  |

<a id="requestActiveDirectoryAuthInfo"></a>
# **requestActiveDirectoryAuthInfo**
> ActiveDirectoryAuthInfo requestActiveDirectoryAuthInfo(isGlobalAvailable)

Request Active Directory authentication information

### Description:   Provides information about Active Directory authentication options.  ### Precondition: None.  ### Postcondition: Active Directory authentication options information is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    Boolean isGlobalAvailable = true; // Boolean | Show only global available items
    try {
      ActiveDirectoryAuthInfo result = apiInstance.requestActiveDirectoryAuthInfo(isGlobalAvailable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestActiveDirectoryAuthInfo");
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
| **isGlobalAvailable** | **Boolean**| Show only global available items | [optional] |

### Return type

[**ActiveDirectoryAuthInfo**](ActiveDirectoryAuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestOpenIdAuthInfo"></a>
# **requestOpenIdAuthInfo**
> OpenIdAuthInfo requestOpenIdAuthInfo(isGlobalAvailable)

Request OpenID Connect provider authentication information

### Description:   Provides information about OpenID Connect authentication options.  ### Precondition: None.  ### Postcondition: OpenID Connect authentication options information is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    Boolean isGlobalAvailable = true; // Boolean | Show only global available items
    try {
      OpenIdAuthInfo result = apiInstance.requestOpenIdAuthInfo(isGlobalAvailable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestOpenIdAuthInfo");
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
| **isGlobalAvailable** | **Boolean**| Show only global available items | [optional] |

### Return type

[**OpenIdAuthInfo**](OpenIdAuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestPublicDownloadShareInfo"></a>
# **requestPublicDownloadShareInfo**
> PublicDownloadShare requestPublicDownloadShareInfo(accessKey, xSdsDateFormat)

Request public Download Share information

### Description:   Retrieve the public information of a Download Share.  ### Precondition: None.  ### Postcondition: Download Share information is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    try {
      PublicDownloadShare result = apiInstance.requestPublicDownloadShareInfo(accessKey, xSdsDateFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestPublicDownloadShareInfo");
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
| **accessKey** | **String**| Access key | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |

### Return type

[**PublicDownloadShare**](PublicDownloadShare.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestPublicUploadShareInfo"></a>
# **requestPublicUploadShareInfo**
> PublicUploadShare requestPublicUploadShareInfo(accessKey, xSdsSharePassword, xSdsDateFormat)

Request public Upload Share information

### Description:   Provides information about the desired Upload Share.  ### Precondition: Only &#x60;userUserPublicKeyList&#x60; is returned to the users who owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: None.  ### Further Information: If no password is set, the returned information is reduced to the following attributes (if available):  * &#x60;name&#x60; * &#x60;createdAt&#x60; * &#x60;isProtected&#x60; * &#x60;isEncrypted&#x60; * &#x60;showUploadedFiles&#x60; * &#x60;userUserPublicKeyList&#x60; (if parent is end-to-end encrypted)  Only if the password is transmitted as &#x60;X-Sds-Share-Password&#x60; header, all values are returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String xSdsSharePassword = "xSdsSharePassword_example"; // String | Upload share password. Should be base64-encoded.  Plain X-Sds-Share-Passwords are *deprecated* and will be removed in the future
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    try {
      PublicUploadShare result = apiInstance.requestPublicUploadShareInfo(accessKey, xSdsSharePassword, xSdsDateFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestPublicUploadShareInfo");
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
| **accessKey** | **String**| Access key | |
| **xSdsSharePassword** | **String**| Upload share password. Should be base64-encoded.  Plain X-Sds-Share-Passwords are *deprecated* and will be removed in the future | [optional] |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |

### Return type

[**PublicUploadShare**](PublicUploadShare.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestSoftwareVersion"></a>
# **requestSoftwareVersion**
> SoftwareVersionData requestSoftwareVersion(xSdsDateFormat)

Request software version information

### Description:   Public software version information.  ### Precondition: None.  ### Postcondition: Sofware version information is returned.  ### Further Information: The version of DRACOON Server consists of two components: * **API** * **Core** (referred to as _\&quot;Server\&quot;_)  which are versioned individually.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    try {
      SoftwareVersionData result = apiInstance.requestSoftwareVersion(xSdsDateFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestSoftwareVersion");
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

### Return type

[**SoftwareVersionData**](SoftwareVersionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestSystemInfo"></a>
# **requestSystemInfo**
> SystemInfo requestSystemInfo(isEnabled)

Request system information

### Description:   Provides information about system.  ### Precondition: None.  ### Postcondition: System information is returned.  ### Further Information: Authentication methods are sorted by **priority** attribute.   Smaller values have higher priority.   Authentication method with highest priority is considered as default.  ### System information: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;languageDefault&#x60; | Defines which language should be default. | &#x60;ISO 639-1 code&#x60; | | &#x60;hideLoginInputFields&#x60; | Defines if login fields should be hidden. | &#x60;true or false&#x60; | | &#x60;s3Hosts&#x60; | List of available S3 hosts. | &#x60;String array&#x60; | | &#x60;s3EnforceDirectUpload&#x60; | Determines whether S3 direct upload is enforced or not. | &#x60;true or false&#x60; | | &#x60;useS3Storage&#x60; | Determines whether S3 Storage enabled and used. | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Authentication methods: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Description | | :--- | :--- | | &#x60;basic&#x60; | **Basic** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their credentials stored in the database.&lt;br&gt;Formerly known as &#x60;sql&#x60;. | | &#x60;active_directory&#x60; | **Active Directory** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their Active Directory credentials. | | &#x60;radius&#x60; | **RADIUS** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their RADIUS username, their PIN and a token password. | | &#x60;openid&#x60; | **OpenID Connect** authentication globally allowed.This option **MUST** be activated to allow users to log in with their OpenID Connect identity. | | &#x60;hideLoginInputFields&#x60; | Determines whether input fields for login should be enabled | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    Boolean isEnabled = true; // Boolean | Show only enabled authentication methods
    try {
      SystemInfo result = apiInstance.requestSystemInfo(isEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestSystemInfo");
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
| **isEnabled** | **Boolean**| Show only enabled authentication methods | [optional] |

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestSystemTime"></a>
# **requestSystemTime**
> SdsServerTime requestSystemTime(xSdsDateFormat)

Request system time

### Description:   Retrieve the actual server time.  ### Precondition: None.  ### Postcondition: Server time is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    try {
      SdsServerTime result = apiInstance.requestSystemTime(xSdsDateFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestSystemTime");
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

### Return type

[**SdsServerTime**](SdsServerTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestThirdPartyDependencies"></a>
# **requestThirdPartyDependencies**
> List&lt;ThirdPartyDependenciesData&gt; requestThirdPartyDependencies()

Request third-party software dependencies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Provides information about used third-party software dependencies.  ### Precondition: None.  ### Postcondition: List of the third-party software dependencies used by **DRACOON Core** (referred to as _\&quot;Server\&quot;_) is returned.  ### Further Information: None.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    try {
      List<ThirdPartyDependenciesData> result = apiInstance.requestThirdPartyDependencies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestThirdPartyDependencies");
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

[**List&lt;ThirdPartyDependenciesData&gt;**](ThirdPartyDependenciesData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestUploadStatusPublic"></a>
# **requestUploadStatusPublic**
> S3ShareUploadStatus requestUploadStatusPublic(accessKey, uploadId)

Request status of S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Request status of a S3 file upload.  ### Precondition: An upload channel has been created and the user has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in the parent container (room or folder).  ### Postcondition: Status of S3 multipart upload request is returned.  ### Further Information: None.  ### Possible errors: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Http Status | Error Code | Description | | :--- | :--- | :--- | | &#x60;400 Bad Request&#x60; | &#x60;-80000&#x60; | Mandatory fields cannot be empty | | &#x60;400 Bad Request&#x60; | &#x60;-80001&#x60; | Invalid positive number | | &#x60;400 Bad Request&#x60; | &#x60;-80002&#x60; | Invalid number | | &#x60;400 Bad Request&#x60; | &#x60;-40001&#x60; | (Target) room is not encrypted | | &#x60;400 Bad Request&#x60; | &#x60;-40755&#x60; | Bad file name | | &#x60;400 Bad Request&#x60; | &#x60;-40763&#x60; | File key must be set for an upload into encrypted room | | &#x60;400 Bad Request&#x60; | &#x60;-50506&#x60; | Exceeds the number of files for this Upload Share | | &#x60;403 Forbidden&#x60; |  | Access denied | | &#x60;404 Not Found&#x60; | &#x60;-20501&#x60; | Upload not found | | &#x60;404 Not Found&#x60; | &#x60;-40000&#x60; | Container not found | | &#x60;404 Not Found&#x60; | &#x60;-41000&#x60; | Node not found | | &#x60;404 Not Found&#x60; | &#x60;-70501&#x60; | User not found | | &#x60;409 Conflict&#x60; | &#x60;-40010&#x60; | Container cannot be overwritten | | &#x60;409 Conflict&#x60; |  | File cannot be overwritten | | &#x60;500 Internal Server Error&#x60; |  | System Error | | &#x60;502 Bad Gateway&#x60; |  | S3 Error | | &#x60;502 Insufficient Storage&#x60; | &#x60;-50504&#x60; | Exceeds the quota for this Upload Share | | &#x60;502 Insufficient Storage&#x60; | &#x60;-40200&#x60; | Exceeds the free node quota in room | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90200&#x60; | Exceeds the free customer quota | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90201&#x60; | Exceeds the free customer physical disk space |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String uploadId = "uploadId_example"; // String | Upload channel ID
    try {
      S3ShareUploadStatus result = apiInstance.requestUploadStatusPublic(accessKey, uploadId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#requestUploadStatusPublic");
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
| **accessKey** | **String**| Access key | |
| **uploadId** | **String**| Upload channel ID | |

### Return type

[**S3ShareUploadStatus**](S3ShareUploadStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="uploadFileAsMultipartPublic1"></a>
# **uploadFileAsMultipartPublic1**
> ChunkUploadResponse uploadFileAsMultipartPublic1(accessKey, uploadId, _file, contentRange, xSdsDateFormat)

Upload file

### Description:   Chunked upload of files via Upload Share.  ### Precondition: Valid upload ID.  ### Postcondition: Chunk of file is uploaded.  ### Further Information: Chunked uploads (range requests) are supported.  Following &#x60;Content-Types&#x60; are supported by this API: * &#x60;multipart/form-data&#x60; * provided &#x60;Content-Type&#x60;    For both file upload types set the correct &#x60;Content-Type&#x60; header and body.    ### Examples:    * &#x60;multipart/form-data&#x60; &#x60;&#x60;&#x60; POST /api/v4/public/shares/uploads/{access_key}{upload_id} HTTP/1.1  Header: ... Content-Type: multipart/form-data; boundary&#x3D;----WebKitFormBoundary7MA4YWxkTrZu0gW ...  Body: ------WebKitFormBoundary7MA4YWxkTrZu0gW Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;file.txt\&quot; Content-Type: text/plain  Content of file.txt ------WebKitFormBoundary7MA4YWxkTrZu0gW-- &#x60;&#x60;&#x60;  * any other &#x60;Content-Type&#x60;   &#x60;&#x60;&#x60; POST /api/v4/public/shares/uploads/{access_key}{upload_id} HTTP/1.1  Header: ... Content-Type: { ... } ...  Body: raw content &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PublicApi apiInstance = new PublicApi(defaultClient);
    String accessKey = "accessKey_example"; // String | Access key
    String uploadId = "uploadId_example"; // String | Upload channel ID
    File _file = new File("/path/to/file"); // File | File
    String contentRange = "contentRange_example"; // String | Content-Range   e.g. `bytes 0-999/3980`
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    try {
      ChunkUploadResponse result = apiInstance.uploadFileAsMultipartPublic1(accessKey, uploadId, _file, contentRange, xSdsDateFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicApi#uploadFileAsMultipartPublic1");
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
| **accessKey** | **String**| Access key | |
| **uploadId** | **String**| Upload channel ID | |
| **_file** | **File**| File | |
| **contentRange** | **String**| Content-Range   e.g. &#x60;bytes 0-999/3980&#x60; | [optional] |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |

### Return type

[**ChunkUploadResponse**](ChunkUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |
| **507** | Insufficient Storage |  -  |

