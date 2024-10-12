# AttachmentsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attachmentsIdDelete**](AttachmentsApi.md#attachmentsIdDelete) | **DELETE** /attachments/{id} | Delete attachment |
| [**mapsIdAttachmentsGet**](AttachmentsApi.md#mapsIdAttachmentsGet) | **GET** /maps/{id}/attachments | List attachments for a given map |
| [**mapsIdAttachmentsPost**](AttachmentsApi.md#mapsIdAttachmentsPost) | **POST** /maps/{id}/attachments | Upload map attachment |
| [**spotsIdAttachmentsGet**](AttachmentsApi.md#spotsIdAttachmentsGet) | **GET** /spots/{id}/attachments | List attachments for a given spot |
| [**spotsIdAttachmentsPost**](AttachmentsApi.md#spotsIdAttachmentsPost) | **POST** /spots/{id}/attachments | Upload spot attachment |


<a id="attachmentsIdDelete"></a>
# **attachmentsIdDelete**
> Attachment attachmentsIdDelete(id)

Delete attachment

Delete attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 56; // Integer | Attachment id
    try {
      Attachment result = apiInstance.attachmentsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#attachmentsIdDelete");
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
| **id** | **Integer**| Attachment id | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted attachment. |  -  |

<a id="mapsIdAttachmentsGet"></a>
# **mapsIdAttachmentsGet**
> List&lt;Attachment&gt; mapsIdAttachmentsGet(id)

List attachments for a given map

List attachments for a given map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 56; // Integer | Map id
    try {
      List<Attachment> result = apiInstance.mapsIdAttachmentsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#mapsIdAttachmentsGet");
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
| **id** | **Integer**| Map id | |

### Return type

[**List&lt;Attachment&gt;**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of attachments. |  -  |

<a id="mapsIdAttachmentsPost"></a>
# **mapsIdAttachmentsPost**
> Attachment mapsIdAttachmentsPost(id, image)

Upload map attachment

Upload map attachment. Wrap attachment parameters in [attachment]

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 56; // Integer | Map id
    String image = "image_example"; // String | Base64 encoded image
    try {
      Attachment result = apiInstance.mapsIdAttachmentsPost(id, image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#mapsIdAttachmentsPost");
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
| **id** | **Integer**| Map id | |
| **image** | **String**| Base64 encoded image | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains attachment data |  -  |

<a id="spotsIdAttachmentsGet"></a>
# **spotsIdAttachmentsGet**
> List&lt;Attachment&gt; spotsIdAttachmentsGet(id)

List attachments for a given spot

List attachments for a given spot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 56; // Integer | Spot id
    try {
      List<Attachment> result = apiInstance.spotsIdAttachmentsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#spotsIdAttachmentsGet");
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
| **id** | **Integer**| Spot id | |

### Return type

[**List&lt;Attachment&gt;**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of attachments. |  -  |

<a id="spotsIdAttachmentsPost"></a>
# **spotsIdAttachmentsPost**
> Attachment spotsIdAttachmentsPost(id, image)

Upload spot attachment

Upload spot attachment. Wrap attachment parameters in [attachment]

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 56; // Integer | Spot id
    String image = "image_example"; // String | Base64 encoded image
    try {
      Attachment result = apiInstance.spotsIdAttachmentsPost(id, image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#spotsIdAttachmentsPost");
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
| **id** | **Integer**| Spot id | |
| **image** | **String**| Base64 encoded image | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains attachment data |  -  |

