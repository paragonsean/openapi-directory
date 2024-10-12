# VideosDelegatedUploadApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dELETEUploadTokensUploadToken**](VideosDelegatedUploadApi.md#dELETEUploadTokensUploadToken) | **DELETE** /upload-tokens/{uploadToken} | Delete an upload token |
| [**gETUploadTokens**](VideosDelegatedUploadApi.md#gETUploadTokens) | **GET** /upload-tokens | List all active upload tokens. |
| [**gETUploadTokensUploadToken**](VideosDelegatedUploadApi.md#gETUploadTokensUploadToken) | **GET** /upload-tokens/{uploadToken} | Show upload token |
| [**pOSTUpload**](VideosDelegatedUploadApi.md#pOSTUpload) | **POST** /upload | Upload with an upload token |
| [**pOSTUploadTokens**](VideosDelegatedUploadApi.md#pOSTUploadTokens) | **POST** /upload-tokens | Generate an upload token |


<a id="dELETEUploadTokensUploadToken"></a>
# **dELETEUploadTokensUploadToken**
> dELETEUploadTokensUploadToken(uploadToken)

Delete an upload token

Delete an existing upload token. This is especially useful for tokens you may have created that do not expire.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosDelegatedUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosDelegatedUploadApi apiInstance = new VideosDelegatedUploadApi(defaultClient);
    String uploadToken = "to1tcmSFHeYY5KzyhOqVKMKb"; // String | The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication.
    try {
      apiInstance.dELETEUploadTokensUploadToken(uploadToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosDelegatedUploadApi#dELETEUploadTokensUploadToken");
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
| **uploadToken** | **String**| The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication. | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="gETUploadTokens"></a>
# **gETUploadTokens**
> TokenListResponse gETUploadTokens().sortBy(sortBy).sortOrder(sortOrder).currentPage(currentPage).pageSize(pageSize).execute();

List all active upload tokens.

A delegated token is used to allow secure uploads without exposing your API key. Use this endpoint to retrieve a list of all currently active delegated tokens. Tutorials using [delegated upload](https://api.video/blog/endpoints/delegated-upload).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosDelegatedUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosDelegatedUploadApi apiInstance = new VideosDelegatedUploadApi(defaultClient);
    String sortBy = "createdAt"; // String | Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format.
    String sortOrder = "asc"; // String | Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      TokenListResponse result = apiInstance.gETUploadTokens()
            .sortBy(sortBy)
            .sortOrder(sortOrder)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosDelegatedUploadApi#gETUploadTokens");
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
| **sortBy** | **String**| Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format. | [optional] [enum: createdAt, ttl] |
| **sortOrder** | **String**| Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A. | [optional] [enum: asc, desc] |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**TokenListResponse**](TokenListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="gETUploadTokensUploadToken"></a>
# **gETUploadTokensUploadToken**
> UploadToken gETUploadTokensUploadToken(uploadToken)

Show upload token

You can retrieve details about a specific upload token if you have the unique identifier for the upload token. Add it in the path of the endpoint. Details include time-to-live (ttl), when the token was created, and when it will expire.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosDelegatedUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosDelegatedUploadApi apiInstance = new VideosDelegatedUploadApi(defaultClient);
    String uploadToken = "to1tcmSFHeYY5KzyhOqVKMKb"; // String | The unique identifier for the token you want information about.
    try {
      UploadToken result = apiInstance.gETUploadTokensUploadToken(uploadToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosDelegatedUploadApi#gETUploadTokensUploadToken");
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
| **uploadToken** | **String**| The unique identifier for the token you want information about. | |

### Return type

[**UploadToken**](UploadToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="pOSTUpload"></a>
# **pOSTUpload**
> Video pOSTUpload(token, _file, contentRange, videoId)

Upload with an upload token

When given a token, anyone can upload a file to the URI &#x60;https://ws.api.video/upload?token&#x3D;&lt;tokenId&gt;&#x60;.  Example with cURL:  &#x60;&#x60;&#x60;curl $ curl  --request POST --url &#39;https://ws.api.video/upload?token&#x3D;toXXX&#39;  --header &#39;content-type: multipart/form-data&#39;  -F file&#x3D;@video.mp4 &#x60;&#x60;&#x60;  Or in an HTML form, with a little JavaScript to convert the form into JSON: &#x60;&#x60;&#x60;html &lt;!--form for user interaction--&gt; &lt;form name&#x3D;\&quot;videoUploadForm\&quot; &gt;   &lt;label for&#x3D;video&gt;Video:&lt;/label&gt;   &lt;input type&#x3D;file name&#x3D;source/&gt;&lt;br/&gt;   &lt;input value&#x3D;\&quot;Submit\&quot; type&#x3D;\&quot;submit\&quot;&gt; &lt;/form&gt; &lt;div&gt;&lt;/div&gt; &lt;!--JS takes the form data      uses FormData to turn the response into JSON.     then uses POST to upload the video file.     Update the token parameter in the url to your upload token.     --&gt; &lt;script&gt;    var form &#x3D; document.forms.namedItem(\&quot;videoUploadForm\&quot;);     form.addEventListener(&#39;submit&#39;, function(ev) {   ev.preventDefault();      var oOutput &#x3D; document.querySelector(\&quot;div\&quot;),          oData &#x3D; new FormData(form);      var oReq &#x3D; new XMLHttpRequest();         oReq.open(\&quot;POST\&quot;, \&quot;https://ws.api.video/upload?token&#x3D;toXXX\&quot;, true);      oReq.send(oData);   oReq.onload &#x3D; function(oEvent) {        if (oReq.status &#x3D;&#x3D;201) {          oOutput.innerHTML &#x3D; \&quot;Your video is uploaded!&lt;br/&gt;\&quot;  + oReq.response;        } else {          oOutput.innerHTML &#x3D; \&quot;Error \&quot; + oReq.status + \&quot; occurred when trying to upload your file.&lt;br /&gt;\&quot;;        }      };    }, false);  &lt;/script&gt; &#x60;&#x60;&#x60;   ### Dealing with large files  We have created a &lt;a href&#x3D;&#39;https://api.video/blog/tutorials/uploading-large-files-with-javascript&#39;&gt;tutorial&lt;/a&gt; to walk through the steps required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosDelegatedUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");

    VideosDelegatedUploadApi apiInstance = new VideosDelegatedUploadApi(defaultClient);
    String token = "to1tcmSFHeYY5KzyhOqVKMKb"; // String | The unique identifier for the token you want to use to upload a video.
    File _file = new File("/path/to/file"); // File | The path to the video you want to upload.
    String contentRange = "Content-Range: bytes 200-100/5000"; // String | Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.
    String videoId = "videoId_example"; // String | The video id returned by the first call to this endpoint in a large video upload scenario.
    try {
      Video result = apiInstance.pOSTUpload(token, _file, contentRange, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosDelegatedUploadApi#pOSTUpload");
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
| **token** | **String**| The unique identifier for the token you want to use to upload a video. | |
| **_file** | **File**| The path to the video you want to upload. | |
| **contentRange** | **String**| Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object. | [optional] |
| **videoId** | **String**| The video id returned by the first call to this endpoint in a large video upload scenario. | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |

<a id="pOSTUploadTokens"></a>
# **pOSTUploadTokens**
> UploadToken pOSTUploadTokens(tokenCreatePayload)

Generate an upload token

Use this endpoint to generate an upload token. You can use this token to authenticate video uploads while keeping your API key safe. Tutorials using [delegated upload](https://api.video/blog/endpoints/delegated-upload).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosDelegatedUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosDelegatedUploadApi apiInstance = new VideosDelegatedUploadApi(defaultClient);
    TokenCreatePayload tokenCreatePayload = new TokenCreatePayload(); // TokenCreatePayload | 
    try {
      UploadToken result = apiInstance.pOSTUploadTokens(tokenCreatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosDelegatedUploadApi#pOSTUploadTokens");
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
| **tokenCreatePayload** | [**TokenCreatePayload**](TokenCreatePayload.md)|  | [optional] |

### Return type

[**UploadToken**](UploadToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

