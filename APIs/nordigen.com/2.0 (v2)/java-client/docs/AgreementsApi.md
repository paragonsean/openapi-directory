# AgreementsApi

All URIs are relative to *https://ob.nordigen.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acceptEUA**](AgreementsApi.md#acceptEUA) | **PUT** /api/v2/agreements/enduser/{id}/accept/ |  |
| [**createEUAV2**](AgreementsApi.md#createEUAV2) | **POST** /api/v2/agreements/enduser/ |  |
| [**deleteEUAByIdV2**](AgreementsApi.md#deleteEUAByIdV2) | **DELETE** /api/v2/agreements/enduser/{id}/ |  |
| [**retrieveAllEUAsForAnEndUserV2**](AgreementsApi.md#retrieveAllEUAsForAnEndUserV2) | **GET** /api/v2/agreements/enduser/ |  |
| [**retrieveEUAByIdV2**](AgreementsApi.md#retrieveEUAByIdV2) | **GET** /api/v2/agreements/enduser/{id}/ |  |


<a id="acceptEUA"></a>
# **acceptEUA**
> EndUserAgreement acceptEUA(id, enduserAcceptanceDetailsRequest)



Accept an end-user agreement via the API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AgreementsApi apiInstance = new AgreementsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | A UUID string identifying this end user agreement.
    EnduserAcceptanceDetailsRequest enduserAcceptanceDetailsRequest = new EnduserAcceptanceDetailsRequest(); // EnduserAcceptanceDetailsRequest | 
    try {
      EndUserAgreement result = apiInstance.acceptEUA(id, enduserAcceptanceDetailsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgreementsApi#acceptEUA");
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
| **id** | **UUID**| A UUID string identifying this end user agreement. | |
| **enduserAcceptanceDetailsRequest** | [**EnduserAcceptanceDetailsRequest**](EnduserAcceptanceDetailsRequest.md)|  | |

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accept end user agreement |  -  |
| **400** | Invalid ID |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **405** | EUA accepted |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="createEUAV2"></a>
# **createEUAV2**
> EndUserAgreement createEUAV2(endUserAgreementRequest)



API endpoints related to end-user agreements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AgreementsApi apiInstance = new AgreementsApi(defaultClient);
    EndUserAgreementRequest endUserAgreementRequest = new EndUserAgreementRequest(); // EndUserAgreementRequest | 
    try {
      EndUserAgreement result = apiInstance.createEUAV2(endUserAgreementRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgreementsApi#createEUAV2");
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
| **endUserAgreementRequest** | [**EndUserAgreementRequest**](EndUserAgreementRequest.md)|  | |

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create enduser agreement |  -  |
| **400** | Agreement field errors |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="deleteEUAByIdV2"></a>
# **deleteEUAByIdV2**
> deleteEUAByIdV2(id)



Delete an end user agreement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AgreementsApi apiInstance = new AgreementsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | A UUID string identifying this end user agreement.
    try {
      apiInstance.deleteEUAByIdV2(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgreementsApi#deleteEUAByIdV2");
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
| **id** | **UUID**| A UUID string identifying this end user agreement. | |

### Return type

null (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Invalid ID |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="retrieveAllEUAsForAnEndUserV2"></a>
# **retrieveAllEUAsForAnEndUserV2**
> PaginatedEndUserAgreementList retrieveAllEUAsForAnEndUserV2(limit, offset)



API endpoints related to end-user agreements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AgreementsApi apiInstance = new AgreementsApi(defaultClient);
    Integer limit = 100; // Integer | Number of results to return per page.
    Integer offset = 1; // Integer | The initial index from which to return the results.
    try {
      PaginatedEndUserAgreementList result = apiInstance.retrieveAllEUAsForAnEndUserV2(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgreementsApi#retrieveAllEUAsForAnEndUserV2");
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
| **limit** | **Integer**| Number of results to return per page. | [optional] [default to 100] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] [default to 1] |

### Return type

[**PaginatedEndUserAgreementList**](PaginatedEndUserAgreementList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve all end user agreements |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="retrieveEUAByIdV2"></a>
# **retrieveEUAByIdV2**
> EndUserAgreement retrieveEUAByIdV2(id)



Retrieve end user agreement by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    AgreementsApi apiInstance = new AgreementsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | A UUID string identifying this end user agreement.
    try {
      EndUserAgreement result = apiInstance.retrieveEUAByIdV2(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgreementsApi#retrieveEUAByIdV2");
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
| **id** | **UUID**| A UUID string identifying this end user agreement. | |

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve end user agreement by ID |  -  |
| **400** | Invalid ID |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

