# EstimateApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**estimateGet**](EstimateApi.md#estimateGet) | **GET** /api/Estimate | Gets list of Estimates |
| [**estimateGetByID**](EstimateApi.md#estimateGetByID) | **GET** /api/Estimate/{id} | Gets Estimate by Estimate ID |
| [**estimatePost**](EstimateApi.md#estimatePost) | **POST** /api/Estimate | Create a new draft Estimate |


<a id="estimateGet"></a>
# **estimateGet**
> EstimateList estimateGet(updatedAfter, pageSize, pageNumber, sort, companyIDFK)

Gets list of Estimates

EstimateStatusCode values are: \&quot;Draft\&quot;, \&quot;Sent\&quot;, \&quot;Accepted\&quot;, \&quot;Converted\&quot;, \&quot;Expired\&quot;, \&quot;Rejected\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EstimateApi apiInstance = new EstimateApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | 
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String sort = "sort_example"; // String | 
    Integer companyIDFK = 56; // Integer | 
    try {
      EstimateList result = apiInstance.estimateGet(updatedAfter, pageSize, pageNumber, sort, companyIDFK);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimateApi#estimateGet");
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
| **updatedAfter** | **OffsetDateTime**|  | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **sort** | **String**|  | [optional] |
| **companyIDFK** | **Integer**|  | [optional] |

### Return type

[**EstimateList**](EstimateList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="estimateGetByID"></a>
# **estimateGetByID**
> estimateGetByID(id)

Gets Estimate by Estimate ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EstimateApi apiInstance = new EstimateApi(defaultClient);
    Long id = 56L; // Long | Estimate Estimate ID number
    try {
      apiInstance.estimateGetByID(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimateApi#estimateGetByID");
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
| **id** | **Long**| Estimate Estimate ID number | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="estimatePost"></a>
# **estimatePost**
> EstimateDetails estimatePost(model)

Create a new draft Estimate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EstimateApi apiInstance = new EstimateApi(defaultClient);
    NewEstimate model = new NewEstimate(); // NewEstimate | 
    try {
      EstimateDetails result = apiInstance.estimatePost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimateApi#estimatePost");
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
| **model** | [**NewEstimate**](NewEstimate.md)|  | |

### Return type

[**EstimateDetails**](EstimateDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

