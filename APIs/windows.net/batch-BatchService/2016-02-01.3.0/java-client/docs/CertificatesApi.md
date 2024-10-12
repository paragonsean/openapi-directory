# CertificatesApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificateAdd**](CertificatesApi.md#certificateAdd) | **POST** /certificates |  |
| [**certificateCancelDeletion**](CertificatesApi.md#certificateCancelDeletion) | **POST** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint})/canceldelete |  |
| [**certificateDelete**](CertificatesApi.md#certificateDelete) | **DELETE** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint}) |  |
| [**certificateGet**](CertificatesApi.md#certificateGet) | **GET** /certificates(thumbprintAlgorithm&#x3D;{thumbprintAlgorithm},thumbprint&#x3D;{thumbprint}) |  |
| [**certificateList**](CertificatesApi.md#certificateList) | **GET** /certificates |  |


<a id="certificateAdd"></a>
# **certificateAdd**
> certificateAdd(apiVersion, certificateAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Adds a certificate to the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    CertificateAddParameter certificateAddParameter = new CertificateAddParameter(); // CertificateAddParameter | The certificate to be added.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.certificateAdd(apiVersion, certificateAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificateAdd");
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
| **apiVersion** | **String**| Client API Version. | |
| **certificateAddParameter** | [**CertificateAddParameter**](CertificateAddParameter.md)| The certificate to be added. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Initial response |  * DataServiceId - The OData id of the resource to which the request applied. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="certificateCancelDeletion"></a>
# **certificateCancelDeletion**
> certificateCancelDeletion(thumbprintAlgorithm, thumbprint, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)



Cancels a failed deletion of a certificate from the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String thumbprintAlgorithm = "thumbprintAlgorithm_example"; // String | The algorithm used to derive the thumbprint parameter. This must be sha1.
    String thumbprint = "thumbprint_example"; // String | The thumbprint of the certificate being deleted.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.certificateCancelDeletion(thumbprintAlgorithm, thumbprint, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificateCancelDeletion");
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
| **thumbprintAlgorithm** | **String**| The algorithm used to derive the thumbprint parameter. This must be sha1. | |
| **thumbprint** | **String**| The thumbprint of the certificate being deleted. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

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
| **204** |  |  * DataServiceId - The OData id of the resource to which the request applied. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="certificateDelete"></a>
# **certificateDelete**
> certificateDelete(thumbprintAlgorithm, thumbprint, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)



Deletes a certificate from the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String thumbprintAlgorithm = "thumbprintAlgorithm_example"; // String | The algorithm used to derive the thumbprint parameter. This must be sha1.
    String thumbprint = "thumbprint_example"; // String | The thumbprint of the certificate to be deleted.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.certificateDelete(thumbprintAlgorithm, thumbprint, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificateDelete");
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
| **thumbprintAlgorithm** | **String**| The algorithm used to derive the thumbprint parameter. This must be sha1. | |
| **thumbprint** | **String**| The thumbprint of the certificate to be deleted. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

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
| **202** |  |  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="certificateGet"></a>
# **certificateGet**
> Certificate certificateGet(thumbprintAlgorithm, thumbprint, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate)



Gets information about the specified certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String thumbprintAlgorithm = "thumbprintAlgorithm_example"; // String | The algorithm used to derive the thumbprint parameter. This must be sha1.
    String thumbprint = "thumbprint_example"; // String | The thumbprint of the certificate to get.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | An OData $select clause.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      Certificate result = apiInstance.certificateGet(thumbprintAlgorithm, thumbprint, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificateGet");
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
| **thumbprintAlgorithm** | **String**| The algorithm used to derive the thumbprint parameter. This must be sha1. | |
| **thumbprint** | **String**| The thumbprint of the certificate to get. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| An OData $select clause. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="certificateList"></a>
# **certificateList**
> CertificateListResult certificateList(apiVersion, $filter, $select, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the certificates that have been added to the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause.
    String $select = "$select_example"; // String | An OData $select clause.
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      CertificateListResult result = apiInstance.certificateList(apiVersion, $filter, $select, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificateList");
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
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. | [optional] |
| **$select** | **String**| An OData $select clause. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CertificateListResult**](CertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the list of certificates. |  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

