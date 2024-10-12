# DefaultApi

All URIs are relative to *https://api.cisco.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**securityAdvisoriesCvrfAdvisoryAdvisoryIdGet**](DefaultApi.md#securityAdvisoriesCvrfAdvisoryAdvisoryIdGet) | **GET** /security/advisories/cvrf/advisory/{advisory_id} |  |
| [**securityAdvisoriesCvrfAllGet**](DefaultApi.md#securityAdvisoriesCvrfAllGet) | **GET** /security/advisories/cvrf/all |  |
| [**securityAdvisoriesCvrfCveCveIdGet**](DefaultApi.md#securityAdvisoriesCvrfCveCveIdGet) | **GET** /security/advisories/cvrf/cve/{cve_id} |  |
| [**securityAdvisoriesCvrfLatestNumberGet**](DefaultApi.md#securityAdvisoriesCvrfLatestNumberGet) | **GET** /security/advisories/cvrf/latest/{number} |  |
| [**securityAdvisoriesCvrfProductGet**](DefaultApi.md#securityAdvisoriesCvrfProductGet) | **GET** /security/advisories/cvrf/product |  |
| [**securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/firstpublished |  |
| [**securityAdvisoriesCvrfSeveritySeverityGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityGet) | **GET** /security/advisories/cvrf/severity/{severity} |  |
| [**securityAdvisoriesCvrfSeveritySeverityLastpublishedGet**](DefaultApi.md#securityAdvisoriesCvrfSeveritySeverityLastpublishedGet) | **GET** /security/advisories/cvrf/severity/{severity}/lastpublished |  |
| [**securityAdvisoriesCvrfYearYearGet**](DefaultApi.md#securityAdvisoriesCvrfYearYearGet) | **GET** /security/advisories/cvrf/year/{year} |  |
| [**securityAdvisoriesIosGet**](DefaultApi.md#securityAdvisoriesIosGet) | **GET** /security/advisories/ios |  |
| [**securityAdvisoriesIosxeGet**](DefaultApi.md#securityAdvisoriesIosxeGet) | **GET** /security/advisories/iosxe |  |
| [**securityAdvisoriesOvalAdvisoryAdvisoryIdGet**](DefaultApi.md#securityAdvisoriesOvalAdvisoryAdvisoryIdGet) | **GET** /security/advisories/oval/advisory/{advisory_id} |  |
| [**securityAdvisoriesOvalAllGet**](DefaultApi.md#securityAdvisoriesOvalAllGet) | **GET** /security/advisories/oval/all |  |
| [**securityAdvisoriesOvalCveCveIdGet**](DefaultApi.md#securityAdvisoriesOvalCveCveIdGet) | **GET** /security/advisories/oval/cve/{cve_id} |  |
| [**securityAdvisoriesOvalLatestNumberGet**](DefaultApi.md#securityAdvisoriesOvalLatestNumberGet) | **GET** /security/advisories/oval/latest/{number} |  |
| [**securityAdvisoriesOvalProductGet**](DefaultApi.md#securityAdvisoriesOvalProductGet) | **GET** /security/advisories/oval/product |  |
| [**securityAdvisoriesOvalSeveritySeverityFirstpublishedGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityFirstpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/firstpublished |  |
| [**securityAdvisoriesOvalSeveritySeverityGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityGet) | **GET** /security/advisories/oval/severity/{severity} |  |
| [**securityAdvisoriesOvalSeveritySeverityLastpublishedGet**](DefaultApi.md#securityAdvisoriesOvalSeveritySeverityLastpublishedGet) | **GET** /security/advisories/oval/severity/{severity}/lastpublished |  |


<a id="securityAdvisoriesCvrfAdvisoryAdvisoryIdGet"></a>
# **securityAdvisoriesCvrfAdvisoryAdvisoryIdGet**
> securityAdvisoriesCvrfAdvisoryAdvisoryIdGet(advisoryId)



Used to obtain an advisory in CVRF format for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String advisoryId = "advisoryId_example"; // String | advisory ID
    try {
      apiInstance.securityAdvisoriesCvrfAdvisoryAdvisoryIdGet(advisoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfAdvisoryAdvisoryIdGet");
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
| **advisoryId** | **String**| advisory ID | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfAllGet"></a>
# **securityAdvisoriesCvrfAllGet**
> securityAdvisoriesCvrfAllGet()



Used to obtain all advisories in Common Vulnerability Reporting Format (CVRF). For more information about CVRF go to https://communities.cisco.com/docs/DOC-63156 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/cvrf/all.xml 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.securityAdvisoriesCvrfAllGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfAllGet");
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

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfCveCveIdGet"></a>
# **securityAdvisoriesCvrfCveCveIdGet**
> securityAdvisoriesCvrfCveCveIdGet(cveId)



Used to obtain an advisory in CVRF format for a given Common Vulnerability Enumerator (CVE). The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/ 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cveId = "cveId_example"; // String | CVE Identifier (i.e., CVE-YYYY-NNNN)
    try {
      apiInstance.securityAdvisoriesCvrfCveCveIdGet(cveId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfCveCveIdGet");
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
| **cveId** | **String**| CVE Identifier (i.e., CVE-YYYY-NNNN) | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfLatestNumberGet"></a>
# **securityAdvisoriesCvrfLatestNumberGet**
> securityAdvisoriesCvrfLatestNumberGet(number)



Used to obtain all the latest security advisories in CVRF format given an absolute number. For instance, the latest 10 or latest 5. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer number = 56; // Integer | An absolute number to obtain the latest security advisories.
    try {
      apiInstance.securityAdvisoriesCvrfLatestNumberGet(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfLatestNumberGet");
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
| **number** | **Integer**| An absolute number to obtain the latest security advisories. | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfProductGet"></a>
# **securityAdvisoriesCvrfProductGet**
> securityAdvisoriesCvrfProductGet(product)



Used to obtain all the advisories that affects the given product name. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String product = "product_example"; // String | An product name to obtain security advisories that matches given product name.
    try {
      apiInstance.securityAdvisoriesCvrfProductGet(product);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfProductGet");
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
| **product** | **String**| An product name to obtain security advisories that matches given product name. | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet"></a>
# **securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet**
> securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format and additionally filter based of firstpublished start date and enddate 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String severity = "critical"; // String | Used to obtain all advisories that have a security impact rating of critical
    LocalDate startDate = LocalDate.now(); // LocalDate | 
    LocalDate endDate = LocalDate.now(); // LocalDate | 
    try {
      apiInstance.securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet(severity, startDate, endDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfSeveritySeverityFirstpublishedGet");
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
| **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical | [enum: critical, high, medium, low] |
| **startDate** | **LocalDate**|  | |
| **endDate** | **LocalDate**|  | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfSeveritySeverityGet"></a>
# **securityAdvisoriesCvrfSeveritySeverityGet**
> securityAdvisoriesCvrfSeveritySeverityGet(severity)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String severity = "critical"; // String | Critical, High, Medium, Low
    try {
      apiInstance.securityAdvisoriesCvrfSeveritySeverityGet(severity);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfSeveritySeverityGet");
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
| **severity** | **String**| Critical, High, Medium, Low | [enum: critical, high, medium, low] |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfSeveritySeverityLastpublishedGet"></a>
# **securityAdvisoriesCvrfSeveritySeverityLastpublishedGet**
> securityAdvisoriesCvrfSeveritySeverityLastpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String severity = "critical"; // String | Used to obtain all advisories that have a security impact rating of critical
    LocalDate startDate = LocalDate.now(); // LocalDate | 
    LocalDate endDate = LocalDate.now(); // LocalDate | 
    try {
      apiInstance.securityAdvisoriesCvrfSeveritySeverityLastpublishedGet(severity, startDate, endDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfSeveritySeverityLastpublishedGet");
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
| **severity** | **String**| Used to obtain all advisories that have a security impact rating of critical | [enum: critical, high, medium, low] |
| **startDate** | **LocalDate**|  | |
| **endDate** | **LocalDate**|  | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesCvrfYearYearGet"></a>
# **securityAdvisoriesCvrfYearYearGet**
> securityAdvisoriesCvrfYearYearGet(year)



Used to obtain all security advisories that have were orginally published in a specific year &#x60;YYYY&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String year = "year_example"; // String | The four digit year.
    try {
      apiInstance.securityAdvisoriesCvrfYearYearGet(year);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesCvrfYearYearGet");
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
| **year** | **String**| The four digit year. | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesIosGet"></a>
# **securityAdvisoriesIosGet**
> securityAdvisoriesIosGet(version)



Used to obtain all advisories that affects the given ios version 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String version = "version_example"; // String | IOS version to obtain security advisories
    try {
      apiInstance.securityAdvisoriesIosGet(version);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesIosGet");
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
| **version** | **String**| IOS version to obtain security advisories | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesIosxeGet"></a>
# **securityAdvisoriesIosxeGet**
> securityAdvisoriesIosxeGet(version)



Used to obtain all advisories that affects the given ios version 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String version = "version_example"; // String | IOS version to obtain security advisories
    try {
      apiInstance.securityAdvisoriesIosxeGet(version);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesIosxeGet");
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
| **version** | **String**| IOS version to obtain security advisories | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalAdvisoryAdvisoryIdGet"></a>
# **securityAdvisoriesOvalAdvisoryAdvisoryIdGet**
> securityAdvisoriesOvalAdvisoryAdvisoryIdGet(advisoryId)



Used to obtain OVAL definitions for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String advisoryId = "advisoryId_example"; // String | advisory ID
    try {
      apiInstance.securityAdvisoriesOvalAdvisoryAdvisoryIdGet(advisoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalAdvisoryAdvisoryIdGet");
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
| **advisoryId** | **String**| advisory ID | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalAllGet"></a>
# **securityAdvisoriesOvalAllGet**
> securityAdvisoriesOvalAllGet()



Used to obtain all Open Vulnerability and Assessment Language (OVAL) definitions available for Cisco security vulnerabilities. For more information about OVAL go to https://communities.cisco.com/docs/DOC-63158 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/oval/all.xml 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.securityAdvisoriesOvalAllGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalAllGet");
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

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalCveCveIdGet"></a>
# **securityAdvisoriesOvalCveCveIdGet**
> securityAdvisoriesOvalCveCveIdGet(cveId)



Used to obtain OVAL definitions for a given CVE Identifier. The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cveId = "cveId_example"; // String | CVE Identifier (i.e., CVE-YYYY-NNNN)
    try {
      apiInstance.securityAdvisoriesOvalCveCveIdGet(cveId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalCveCveIdGet");
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
| **cveId** | **String**| CVE Identifier (i.e., CVE-YYYY-NNNN) | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalLatestNumberGet"></a>
# **securityAdvisoriesOvalLatestNumberGet**
> securityAdvisoriesOvalLatestNumberGet(number)



Used to obtain all the latest OVAL definitions given an absolute number. For instance, the latest 10 or latest 5. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer number = 56; // Integer | The latest OVAL definitions (absolute number).
    try {
      apiInstance.securityAdvisoriesOvalLatestNumberGet(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalLatestNumberGet");
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
| **number** | **Integer**| The latest OVAL definitions (absolute number). | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalProductGet"></a>
# **securityAdvisoriesOvalProductGet**
> securityAdvisoriesOvalProductGet(product)



Used to obtain all the oval advisories that affects the given product name. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String product = "product_example"; // String | An product name to obtain security advisories that matches given product name.
    try {
      apiInstance.securityAdvisoriesOvalProductGet(product);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalProductGet");
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
| **product** | **String**| An product name to obtain security advisories that matches given product name. | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalSeveritySeverityFirstpublishedGet"></a>
# **securityAdvisoriesOvalSeveritySeverityFirstpublishedGet**
> securityAdvisoriesOvalSeveritySeverityFirstpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String severity = "critical"; // String | Critical, High, Medium, Low
    LocalDate startDate = LocalDate.now(); // LocalDate | 
    LocalDate endDate = LocalDate.now(); // LocalDate | 
    try {
      apiInstance.securityAdvisoriesOvalSeveritySeverityFirstpublishedGet(severity, startDate, endDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalSeveritySeverityFirstpublishedGet");
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
| **severity** | **String**| Critical, High, Medium, Low | [enum: critical, high, medium, low] |
| **startDate** | **LocalDate**|  | |
| **endDate** | **LocalDate**|  | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalSeveritySeverityGet"></a>
# **securityAdvisoriesOvalSeveritySeverityGet**
> securityAdvisoriesOvalSeveritySeverityGet(severity)



Used to obtain all OVAL definitions for a given security impact rating (critical, high, medium, or low). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String severity = "critical"; // String | Used to obtain all OVAL definitions for advisories that have a security impact rating of critical
    try {
      apiInstance.securityAdvisoriesOvalSeveritySeverityGet(severity);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalSeveritySeverityGet");
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
| **severity** | **String**| Used to obtain all OVAL definitions for advisories that have a security impact rating of critical | [enum: critical, high, medium, low] |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="securityAdvisoriesOvalSeveritySeverityLastpublishedGet"></a>
# **securityAdvisoriesOvalSeveritySeverityLastpublishedGet**
> securityAdvisoriesOvalSeveritySeverityLastpublishedGet(severity, startDate, endDate)



Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cisco.com");
    
    // Configure OAuth2 access token for authorization: psirt_openvuln_api_auth
    OAuth psirt_openvuln_api_auth = (OAuth) defaultClient.getAuthentication("psirt_openvuln_api_auth");
    psirt_openvuln_api_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String severity = "critical"; // String | Critical, High, Medium, Low
    LocalDate startDate = LocalDate.now(); // LocalDate | 
    LocalDate endDate = LocalDate.now(); // LocalDate | 
    try {
      apiInstance.securityAdvisoriesOvalSeveritySeverityLastpublishedGet(severity, startDate, endDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#securityAdvisoriesOvalSeveritySeverityLastpublishedGet");
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
| **severity** | **String**| Critical, High, Medium, Low | [enum: critical, high, medium, low] |
| **startDate** | **LocalDate**|  | |
| **endDate** | **LocalDate**|  | |

### Return type

null (empty response body)

### Authorization

[psirt_openvuln_api_auth](../README.md#psirt_openvuln_api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

