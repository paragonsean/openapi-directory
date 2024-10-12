# ImagesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addIdDocumentImage**](ImagesApi.md#addIdDocumentImage) | **POST** /api/images/id-document | Add an id document image to the specified registration. |
| [**addLivenessImage**](ImagesApi.md#addLivenessImage) | **POST** /api/images/liveness | Add a liveness image (UAP) to the specified registration. |
| [**addSelfieImage**](ImagesApi.md#addSelfieImage) | **POST** /api/images/selfie | Add a selfie image to the registration. |
| [**getIdDocumentImages**](ImagesApi.md#getIdDocumentImages) | **GET** /api/images/id-document/{registrationId} | Get all id document images associated with a registration. |
| [**getLivenessImage**](ImagesApi.md#getLivenessImage) | **GET** /api/images/liveness/{registrationId} | Retrieve the liveness action image (UAP) associated with a registration. |
| [**getLivenessPerformedImage**](ImagesApi.md#getLivenessPerformedImage) | **GET** /api/images/liveness-performed/{registrationId} | Retrieve the liveness performed image associated with a registration. |
| [**getScanReportPdf**](ImagesApi.md#getScanReportPdf) | **GET** /api/images/scan-report-pdf/{scanId} | Returns a detailed report on the analysis that has taken place of a scanned document |
| [**getSelfieImage**](ImagesApi.md#getSelfieImage) | **GET** /api/images/selfie/{registrationId} | Retrieve the selfie image associated with a registration. |


<a id="addIdDocumentImage"></a>
# **addIdDocumentImage**
> CredasApiModelsImagesAddIdDocumentImageResponse addIdDocumentImage(apikey, credasApiModelsImagesAddIdDocumentImageRequest)

Add an id document image to the specified registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsImagesAddIdDocumentImageRequest credasApiModelsImagesAddIdDocumentImageRequest = new CredasApiModelsImagesAddIdDocumentImageRequest(); // CredasApiModelsImagesAddIdDocumentImageRequest | Object containing the id document image and registration id.
    try {
      CredasApiModelsImagesAddIdDocumentImageResponse result = apiInstance.addIdDocumentImage(apikey, credasApiModelsImagesAddIdDocumentImageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#addIdDocumentImage");
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
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsImagesAddIdDocumentImageRequest** | [**CredasApiModelsImagesAddIdDocumentImageRequest**](CredasApiModelsImagesAddIdDocumentImageRequest.md)| Object containing the id document image and registration id. | [optional] |

### Return type

[**CredasApiModelsImagesAddIdDocumentImageResponse**](CredasApiModelsImagesAddIdDocumentImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the processed id document. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | Error code meaning that the operation was aborted due to insufficient credits. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="addLivenessImage"></a>
# **addLivenessImage**
> addLivenessImage(apikey, credasApiModelsImagesAddLivenessImageRequest)

Add a liveness image (UAP) to the specified registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsImagesAddLivenessImageRequest credasApiModelsImagesAddLivenessImageRequest = new CredasApiModelsImagesAddLivenessImageRequest(); // CredasApiModelsImagesAddLivenessImageRequest | Object containing the liveness image and registration id.
    try {
      apiInstance.addLivenessImage(apikey, credasApiModelsImagesAddLivenessImageRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#addLivenessImage");
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
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsImagesAddLivenessImageRequest** | [**CredasApiModelsImagesAddLivenessImageRequest**](CredasApiModelsImagesAddLivenessImageRequest.md)| Object containing the liveness image and registration id. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response indicating a successful action. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="addSelfieImage"></a>
# **addSelfieImage**
> CredasApiModelsImagesAddSelfieImageResponse addSelfieImage(apikey, credasApiModelsImagesAddSelfieImageRequest)

Add a selfie image to the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsImagesAddSelfieImageRequest credasApiModelsImagesAddSelfieImageRequest = new CredasApiModelsImagesAddSelfieImageRequest(); // CredasApiModelsImagesAddSelfieImageRequest | Object containing the selfie image and registration id.
    try {
      CredasApiModelsImagesAddSelfieImageResponse result = apiInstance.addSelfieImage(apikey, credasApiModelsImagesAddSelfieImageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#addSelfieImage");
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
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsImagesAddSelfieImageRequest** | [**CredasApiModelsImagesAddSelfieImageRequest**](CredasApiModelsImagesAddSelfieImageRequest.md)| Object containing the selfie image and registration id. | [optional] |

### Return type

[**CredasApiModelsImagesAddSelfieImageResponse**](CredasApiModelsImagesAddSelfieImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of uploading selfie image; including liveness check indicator. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getIdDocumentImages"></a>
# **getIdDocumentImages**
> List&lt;CredasApiModelsImagesGetIdDocumentImageResponse&gt; getIdDocumentImages(registrationId, apikey)

Get all id document images associated with a registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID registrationId = UUID.randomUUID(); // UUID | The id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      List<CredasApiModelsImagesGetIdDocumentImageResponse> result = apiInstance.getIdDocumentImages(registrationId, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getIdDocumentImages");
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
| **registrationId** | **UUID**| The id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**List&lt;CredasApiModelsImagesGetIdDocumentImageResponse&gt;**](CredasApiModelsImagesGetIdDocumentImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the id documents associated with the registration. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getLivenessImage"></a>
# **getLivenessImage**
> CredasApiModelsImagesGetLivenessImageResponse getLivenessImage(registrationId, apikey)

Retrieve the liveness action image (UAP) associated with a registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID registrationId = UUID.randomUUID(); // UUID | The id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsImagesGetLivenessImageResponse result = apiInstance.getLivenessImage(registrationId, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getLivenessImage");
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
| **registrationId** | **UUID**| The id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsImagesGetLivenessImageResponse**](CredasApiModelsImagesGetLivenessImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response containing Liveness image details. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getLivenessPerformedImage"></a>
# **getLivenessPerformedImage**
> CredasApiModelsImagesGetLivenessPerformedImageResponse getLivenessPerformedImage(registrationId, apikey)

Retrieve the liveness performed image associated with a registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID registrationId = UUID.randomUUID(); // UUID | The id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsImagesGetLivenessPerformedImageResponse result = apiInstance.getLivenessPerformedImage(registrationId, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getLivenessPerformedImage");
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
| **registrationId** | **UUID**| The id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsImagesGetLivenessPerformedImageResponse**](CredasApiModelsImagesGetLivenessPerformedImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response containing Liveness performed image details. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If the liveness performed image doesn&#39;t exist. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getScanReportPdf"></a>
# **getScanReportPdf**
> byte[] getScanReportPdf(scanId, apikey)

Returns a detailed report on the analysis that has taken place of a scanned document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID scanId = UUID.randomUUID(); // UUID | Id of the individual scanned document
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      byte[] result = apiInstance.getScanReportPdf(scanId, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getScanReportPdf");
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
| **scanId** | **UUID**| Id of the individual scanned document | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

**byte[]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PDF document containing detail analysis of scanned documents as a byte stream. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If scan matching the scanId was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getSelfieImage"></a>
# **getSelfieImage**
> CredasApiModelsImagesGetSelfieImageResponse getSelfieImage(registrationId, apikey)

Retrieve the selfie image associated with a registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID registrationId = UUID.randomUUID(); // UUID | The id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsImagesGetSelfieImageResponse result = apiInstance.getSelfieImage(registrationId, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getSelfieImage");
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
| **registrationId** | **UUID**| The id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsImagesGetSelfieImageResponse**](CredasApiModelsImagesGetSelfieImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response containing the selfie image details. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

