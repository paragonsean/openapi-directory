# CertificatesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificatesGet**](CertificatesApi.md#certificatesGet) | **GET** /certificates | Get all Certificates |
| [**certificatesIdDelete**](CertificatesApi.md#certificatesIdDelete) | **DELETE** /certificates/{id} | Delete a Certificate |
| [**certificatesIdGet**](CertificatesApi.md#certificatesIdGet) | **GET** /certificates/{id} | Get a Certificate |
| [**certificatesIdPut**](CertificatesApi.md#certificatesIdPut) | **PUT** /certificates/{id} | Update a Certificate |
| [**certificatesPost**](CertificatesApi.md#certificatesPost) | **POST** /certificates | Create a Certificate |


<a id="certificatesGet"></a>
# **certificatesGet**
> CertificatesResponse certificatesGet(sort, name, labelSelector, type)

Get all Certificates

Returns all Certificate objects.

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
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String sort = "id"; // String | Can be used multiple times.
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    String type = "uploaded"; // String | Can be used multiple times. The response will only contain Certificates matching the type.
    try {
      CertificatesResponse result = apiInstance.certificatesGet(sort, name, labelSelector, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGet");
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
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, name, name:asc, name:desc, created, created:asc, created:desc] |
| **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] |
| **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] |
| **type** | **String**| Can be used multiple times. The response will only contain Certificates matching the type. | [optional] [enum: uploaded, managed] |

### Return type

[**CertificatesResponse**](CertificatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;certificates&#x60; key contains an array of Certificate objects |  -  |

<a id="certificatesIdDelete"></a>
# **certificatesIdDelete**
> certificatesIdDelete(id)

Delete a Certificate

Deletes a Certificate.

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
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      apiInstance.certificatesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesIdDelete");
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
| **id** | **Integer**| ID of the resource | |

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
| **204** | Certificate deleted |  -  |

<a id="certificatesIdGet"></a>
# **certificatesIdGet**
> CertificateResponse certificatesIdGet(id)

Get a Certificate

Gets a specific Certificate object.

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
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      CertificateResponse result = apiInstance.certificatesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesIdGet");
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
| **id** | **Integer**| ID of the resource | |

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;certificate&#x60; key contains a Certificate object |  -  |

<a id="certificatesIdPut"></a>
# **certificatesIdPut**
> CertificateResponse certificatesIdPut(id, updateCertificateRequest)

Update a Certificate

Updates the Certificate properties.  Note that when updating labels, the Certificate’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Certificate object changes during the request, the response will be a “conflict” error. 

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
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    UpdateCertificateRequest updateCertificateRequest = new UpdateCertificateRequest(); // UpdateCertificateRequest | 
    try {
      CertificateResponse result = apiInstance.certificatesIdPut(id, updateCertificateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesIdPut");
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
| **id** | **Integer**| ID of the resource | |
| **updateCertificateRequest** | [**UpdateCertificateRequest**](UpdateCertificateRequest.md)|  | [optional] |

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;certificate&#x60; key contains the Certificate that was just updated |  -  |

<a id="certificatesPost"></a>
# **certificatesPost**
> CreateCertificateResponse certificatesPost(createCertificateRequest)

Create a Certificate

Creates a new Certificate.  The default type **uploaded** allows for uploading your existing &#x60;certificate&#x60; and &#x60;private_key&#x60; in PEM format. You have to monitor its expiration date and handle renewal yourself.  In contrast, type **managed** requests a new Certificate from *Let&#39;s Encrypt* for the specified &#x60;domain_names&#x60;. Only domains managed by *Hetzner DNS* are supported. We handle renewal and timely alert the project owner via email if problems occur.  For type &#x60;managed&#x60; Certificates the &#x60;action&#x60; key of the response contains the Action that allows for tracking the issuance process. For type &#x60;uploaded&#x60; Certificates the &#x60;action&#x60; is always null. 

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
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    CreateCertificateRequest createCertificateRequest = new CreateCertificateRequest(); // CreateCertificateRequest | 
    try {
      CreateCertificateResponse result = apiInstance.certificatesPost(createCertificateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesPost");
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
| **createCertificateRequest** | [**CreateCertificateRequest**](CreateCertificateRequest.md)|  | [optional] |

### Return type

[**CreateCertificateResponse**](CreateCertificateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;certificate&#x60; key contains the Certificate that was just created. For type &#x60;managed&#x60; Certificates the &#x60;action&#x60; key contains the Action that allows for tracking the issuance process. For type &#x60;uploaded&#x60; Certificates the &#x60;action&#x60; is always null. |  -  |

