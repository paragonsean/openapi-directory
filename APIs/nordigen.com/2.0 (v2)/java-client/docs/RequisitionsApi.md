# RequisitionsApi

All URIs are relative to *https://ob.nordigen.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRequisitionByIdV2**](RequisitionsApi.md#deleteRequisitionByIdV2) | **DELETE** /api/v2/requisitions/{id}/ |  |
| [**requisitionById**](RequisitionsApi.md#requisitionById) | **GET** /api/v2/requisitions/{id}/ |  |
| [**requisitionCreated**](RequisitionsApi.md#requisitionCreated) | **POST** /api/v2/requisitions/ |  |
| [**retrieveAllRequisitions**](RequisitionsApi.md#retrieveAllRequisitions) | **GET** /api/v2/requisitions/ |  |


<a id="deleteRequisitionByIdV2"></a>
# **deleteRequisitionByIdV2**
> deleteRequisitionByIdV2(id)



Delete requisition and its end user agreement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequisitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    RequisitionsApi apiInstance = new RequisitionsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | A UUID string identifying this requisition.
    try {
      apiInstance.deleteRequisitionByIdV2(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequisitionsApi#deleteRequisitionByIdV2");
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
| **id** | **UUID**| A UUID string identifying this requisition. | |

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

<a id="requisitionById"></a>
# **requisitionById**
> Requisition requisitionById(id)



Retrieve a requisition by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequisitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    RequisitionsApi apiInstance = new RequisitionsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | A UUID string identifying this requisition.
    try {
      Requisition result = apiInstance.requisitionById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequisitionsApi#requisitionById");
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
| **id** | **UUID**| A UUID string identifying this requisition. | |

### Return type

[**Requisition**](Requisition.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get requisition by ID |  -  |
| **400** | Invalid ID |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="requisitionCreated"></a>
# **requisitionCreated**
> SpectacularRequisition requisitionCreated(requisitionRequest)



Create a new requisition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequisitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    RequisitionsApi apiInstance = new RequisitionsApi(defaultClient);
    RequisitionRequest requisitionRequest = new RequisitionRequest(); // RequisitionRequest | 
    try {
      SpectacularRequisition result = apiInstance.requisitionCreated(requisitionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequisitionsApi#requisitionCreated");
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
| **requisitionRequest** | [**RequisitionRequest**](RequisitionRequest.md)|  | |

### Return type

[**SpectacularRequisition**](SpectacularRequisition.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Requisition has been successfully created |  -  |
| **400** | Fields required |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Agreement not found errors |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="retrieveAllRequisitions"></a>
# **retrieveAllRequisitions**
> PaginatedRequisitionList retrieveAllRequisitions(limit, offset)



Retrieve all requisitions belonging to the company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequisitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    RequisitionsApi apiInstance = new RequisitionsApi(defaultClient);
    Integer limit = 100; // Integer | Number of results to return per page.
    Integer offset = 1; // Integer | The initial index from which to return the results.
    try {
      PaginatedRequisitionList result = apiInstance.retrieveAllRequisitions(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequisitionsApi#retrieveAllRequisitions");
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

[**PaginatedRequisitionList**](PaginatedRequisitionList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve all requisitions |  -  |
| **400** | Unknown Fields |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **404** | Not found error |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

