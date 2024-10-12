# SslCertificateRequestsApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSslCertificateRequest**](SslCertificateRequestsApi.md#addSslCertificateRequest) | **POST** /sslcertificaterequests | Add a SSL certificate request |
| [**getSslCertificateRequest**](SslCertificateRequestsApi.md#getSslCertificateRequest) | **GET** /sslcertificaterequests/{id} | Detail of a SSL certificate request |
| [**getSslCertificateRequests**](SslCertificateRequestsApi.md#getSslCertificateRequests) | **GET** /sslcertificaterequests | Overview of SSL certificate requests |
| [**verifySslCertificateRequestDomainValidations**](SslCertificateRequestsApi.md#verifySslCertificateRequestDomainValidations) | **PUT** /sslcertificaterequests/{id} | Verify the SSL certificate request domain validations |


<a id="addSslCertificateRequest"></a>
# **addSslCertificateRequest**
> addSslCertificateRequest(createSslCertificateRequest)

Add a SSL certificate request

Executing this method causes the purchase of a paying product.&lt;br /&gt;  Log on to our website to see your current (renewal) prices or contact our Sales department.&lt;br /&gt;  Please note that promotional pricing does not apply for purchases made through our API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslCertificateRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SslCertificateRequestsApi apiInstance = new SslCertificateRequestsApi(defaultClient);
    CreateSslCertificateRequest createSslCertificateRequest = new CreateSslCertificateRequest(); // CreateSslCertificateRequest | 
    try {
      apiInstance.addSslCertificateRequest(createSslCertificateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslCertificateRequestsApi#addSslCertificateRequest");
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
| **createSslCertificateRequest** | [**CreateSslCertificateRequest**](CreateSslCertificateRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

<a id="getSslCertificateRequest"></a>
# **getSslCertificateRequest**
> SslCertificateRequestDetail getSslCertificateRequest(id)

Detail of a SSL certificate request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslCertificateRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SslCertificateRequestsApi apiInstance = new SslCertificateRequestsApi(defaultClient);
    Integer id = 56; // Integer | The id of the certificate request.
    try {
      SslCertificateRequestDetail result = apiInstance.getSslCertificateRequest(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslCertificateRequestsApi#getSslCertificateRequest");
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
| **id** | **Integer**| The id of the certificate request. | |

### Return type

[**SslCertificateRequestDetail**](SslCertificateRequestDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **303** | Redirect |  * Location - The location referring to a resource that replaced the original resource. <br>  |
| **410** | The resource existed in the past, but is no longer available. |  -  |

<a id="getSslCertificateRequests"></a>
# **getSslCertificateRequests**
> List&lt;SslCertificateRequest&gt; getSslCertificateRequests(skip, take)

Overview of SSL certificate requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslCertificateRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SslCertificateRequestsApi apiInstance = new SslCertificateRequestsApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    try {
      List<SslCertificateRequest> result = apiInstance.getSslCertificateRequests(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslCertificateRequestsApi#getSslCertificateRequests");
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |

### Return type

[**List&lt;SslCertificateRequest&gt;**](SslCertificateRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

<a id="verifySslCertificateRequestDomainValidations"></a>
# **verifySslCertificateRequestDomainValidations**
> verifySslCertificateRequestDomainValidations(id)

Verify the SSL certificate request domain validations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslCertificateRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SslCertificateRequestsApi apiInstance = new SslCertificateRequestsApi(defaultClient);
    Integer id = 56; // Integer | The id of the certificate request.
    try {
      apiInstance.verifySslCertificateRequestDomainValidations(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslCertificateRequestsApi#verifySslCertificateRequestDomainValidations");
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
| **id** | **Integer**| The id of the certificate request. | |

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
| **202** | Success |  -  |
| **303** | Redirect |  * Location - The location referring to a resource that replaced the original resource. <br>  |
| **410** | The resource existed in the past, but is no longer available. |  -  |

