# ImportApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**importSessionsGet**](ImportApi.md#importSessionsGet) | **GET** /import/sessions |  |
| [**importSessionsIdDelete**](ImportApi.md#importSessionsIdDelete) | **DELETE** /import/sessions/{id} |  |
| [**importSessionsIdGet**](ImportApi.md#importSessionsIdGet) | **GET** /import/sessions/{id} |  |
| [**importSessionsIdImagesGet**](ImportApi.md#importSessionsIdImagesGet) | **GET** /import/sessions/{id}/images |  |
| [**importSessionsIdImagesPost**](ImportApi.md#importSessionsIdImagesPost) | **POST** /import/sessions/{id}/images |  |
| [**importSessionsPost**](ImportApi.md#importSessionsPost) | **POST** /import/sessions |  |


<a id="importSessionsGet"></a>
# **importSessionsGet**
> List&lt;ImportSession&gt; importSessionsGet(startindex, count)



Returns a list of available import sessions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ImportApi apiInstance = new ImportApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of import sessions
    Long count = 20L; // Long | size of returned slice of import sessions
    try {
      List<ImportSession> result = apiInstance.importSessionsGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importSessionsGet");
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
| **startindex** | **Long**| start index of returned slice of import sessions | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of import sessions | [optional] [default to 20] |

### Return type

[**List&lt;ImportSession&gt;**](ImportSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | available import sessions |  -  |

<a id="importSessionsIdDelete"></a>
# **importSessionsIdDelete**
> importSessionsIdDelete(id)



deletes the import session with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ImportApi apiInstance = new ImportApi(defaultClient);
    Long id = 56L; // Long | ID of import session to delete
    try {
      apiInstance.importSessionsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importSessionsIdDelete");
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
| **id** | **Long**| ID of import session to delete | |

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
| **204** | import session deleted |  -  |

<a id="importSessionsIdGet"></a>
# **importSessionsIdGet**
> ImportSession importSessionsIdGet(id)



Returns the import sessions with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ImportApi apiInstance = new ImportApi(defaultClient);
    Long id = 56L; // Long | ID of session
    try {
      ImportSession result = apiInstance.importSessionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importSessionsIdGet");
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
| **id** | **Long**| ID of session | |

### Return type

[**ImportSession**](ImportSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the import session with the supplied ID |  -  |
| **404** | import session not found (invalid ID) |  -  |

<a id="importSessionsIdImagesGet"></a>
# **importSessionsIdImagesGet**
> List&lt;Image&gt; importSessionsIdImagesGet(id)



get the imported images corresponding to the import session with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ImportApi apiInstance = new ImportApi(defaultClient);
    Long id = 56L; // Long | ID of import session
    try {
      List<Image> result = apiInstance.importSessionsIdImagesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importSessionsIdImagesGet");
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
| **id** | **Long**| ID of import session | |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | images corresponding to the specified import session |  -  |
| **404** | import session not found (invalid ID) |  -  |

<a id="importSessionsIdImagesPost"></a>
# **importSessionsIdImagesPost**
> Image importSessionsIdImagesPost(id, imagesPostRequest)



add a DICOM dataset to the import session with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ImportApi apiInstance = new ImportApi(defaultClient);
    Long id = 56L; // Long | ID of session
    ImagesPostRequest imagesPostRequest = new ImagesPostRequest(); // ImagesPostRequest | 
    try {
      Image result = apiInstance.importSessionsIdImagesPost(id, imagesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importSessionsIdImagesPost");
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
| **id** | **Long**| ID of session | |
| **imagesPostRequest** | [**ImagesPostRequest**](ImagesPostRequest.md)|  | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | meta data for the imported dataset on the image level of the DICOM hierarchy. Status code 200 signifies that this image was already present in the slicebox database. |  -  |
| **201** | meta data for the imported dataset on the image level of the DICOM hierarchy |  -  |
| **404** | import session not found (invalid ID) |  -  |

<a id="importSessionsPost"></a>
# **importSessionsPost**
> ImportSession importSessionsPost(importSession)



create a new import sessions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ImportApi apiInstance = new ImportApi(defaultClient);
    ImportSession importSession = new ImportSession(); // ImportSession | The import session to create containing the user defined name of the session
    try {
      ImportSession result = apiInstance.importSessionsPost(importSession);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importSessionsPost");
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
| **importSession** | [**ImportSession**](ImportSession.md)| The import session to create containing the user defined name of the session | |

### Return type

[**ImportSession**](ImportSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the created import session |  -  |

