# CertificatesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificatesCreateInstance**](CertificatesApi.md#certificatesCreateInstance) | **POST** /v1/certificates |  |
| [**certificatesDeleteInstance**](CertificatesApi.md#certificatesDeleteInstance) | **DELETE** /v1/certificates/{id} |  |
| [**certificatesGetCollection**](CertificatesApi.md#certificatesGetCollection) | **GET** /v1/certificates |  |
| [**certificatesGetInstance**](CertificatesApi.md#certificatesGetInstance) | **GET** /v1/certificates/{id} |  |


<a id="certificatesCreateInstance"></a>
# **certificatesCreateInstance**
> CertificateResponse certificatesCreateInstance(certificateCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    CertificateCreateRequest certificateCreateRequest = new CertificateCreateRequest(); // CertificateCreateRequest | Certificate representation
    try {
      CertificateResponse result = apiInstance.certificatesCreateInstance(certificateCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesCreateInstance");
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
| **certificateCreateRequest** | [**CertificateCreateRequest**](CertificateCreateRequest.md)| Certificate representation | |

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single Certificate |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="certificatesDeleteInstance"></a>
# **certificatesDeleteInstance**
> certificatesDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.certificatesDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesDeleteInstance");
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
| **id** | **String**| the id of the requested resource | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="certificatesGetCollection"></a>
# **certificatesGetCollection**
> CertificatesResponse certificatesGetCollection(filterCertificateType, filterDisplayName, filterSerialNumber, filterId, sort, fieldsCertificates, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    List<String> filterCertificateType = Arrays.asList(); // List<String> | filter by attribute 'certificateType'
    List<String> filterDisplayName = Arrays.asList(); // List<String> | filter by attribute 'displayName'
    List<String> filterSerialNumber = Arrays.asList(); // List<String> | filter by attribute 'serialNumber'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsCertificates = Arrays.asList(); // List<String> | the fields to include for returned resources of type certificates
    Integer limit = 56; // Integer | maximum resources per page
    try {
      CertificatesResponse result = apiInstance.certificatesGetCollection(filterCertificateType, filterDisplayName, filterSerialNumber, filterId, sort, fieldsCertificates, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGetCollection");
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
| **filterCertificateType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;certificateType&#39; | [optional] [enum: IOS_DEVELOPMENT, IOS_DISTRIBUTION, MAC_APP_DISTRIBUTION, MAC_INSTALLER_DISTRIBUTION, MAC_APP_DEVELOPMENT, DEVELOPER_ID_KEXT, DEVELOPER_ID_APPLICATION, DEVELOPMENT, DISTRIBUTION] |
| **filterDisplayName** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;displayName&#39; | [optional] |
| **filterSerialNumber** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;serialNumber&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: certificateType, -certificateType, displayName, -displayName, id, -id, serialNumber, -serialNumber] |
| **fieldsCertificates** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type certificates | [optional] [enum: certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**CertificatesResponse**](CertificatesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Certificates |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="certificatesGetInstance"></a>
# **certificatesGetInstance**
> CertificateResponse certificatesGetInstance(id, fieldsCertificates)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsCertificates = Arrays.asList(); // List<String> | the fields to include for returned resources of type certificates
    try {
      CertificateResponse result = apiInstance.certificatesGetInstance(id, fieldsCertificates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGetInstance");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsCertificates** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type certificates | [optional] [enum: certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber] |

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single Certificate |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

