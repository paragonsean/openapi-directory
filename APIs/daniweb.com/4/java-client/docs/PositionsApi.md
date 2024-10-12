# PositionsApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**positionsIDDelete**](PositionsApi.md#positionsIDDelete) | **DELETE** /positions/{ID} |  |
| [**positionsIDPatch**](PositionsApi.md#positionsIDPatch) | **PATCH** /positions/{ID} |  |
| [**positionsPost**](PositionsApi.md#positionsPost) | **POST** /positions |  |


<a id="positionsIDDelete"></a>
# **positionsIDDelete**
> EndpointDeletePositionsID positionsIDDelete(ID)



Remove an item from the OAuth&#39;ed end user&#39;s Curriculum Vitae.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    PositionsApi apiInstance = new PositionsApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointDeletePositionsID result = apiInstance.positionsIDDelete(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionsApi#positionsIDDelete");
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
| **ID** | **Integer**|  | |

### Return type

[**EndpointDeletePositionsID**](EndpointDeletePositionsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="positionsIDPatch"></a>
# **positionsIDPatch**
> EndpointPatchPositionsID positionsIDPatch(ID, category, organization, role, startDate, endDate, organizationSize, position, summary, url)



Update the OAuth&#39;ed end user&#39;s Curriculum Vitae by modifying an existing position.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    PositionsApi apiInstance = new PositionsApi(defaultClient);
    Integer ID = 56; // Integer | 
    String category = "Experience"; // String | 
    String organization = "organization_example"; // String | 
    String role = "role_example"; // String | 
    String startDate = "startDate_example"; // String | 
    String endDate = "endDate_example"; // String | 
    String organizationSize = "Self-employed"; // String | 
    String position = "Executive Management (C-level)"; // String | 
    String summary = "summary_example"; // String | 
    String url = "url_example"; // String | 
    try {
      EndpointPatchPositionsID result = apiInstance.positionsIDPatch(ID, category, organization, role, startDate, endDate, organizationSize, position, summary, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionsApi#positionsIDPatch");
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
| **ID** | **Integer**|  | |
| **category** | **String**|  | [enum: Experience, Education, Awards, Affiliations, Portfolio] |
| **organization** | **String**|  | |
| **role** | **String**|  | |
| **startDate** | **String**|  | |
| **endDate** | **String**|  | [optional] |
| **organizationSize** | **String**|  | [optional] [enum: Self-employed, 2 - 9 Employees, 10 - 49 Employees, 50 - 99 Employees, 100 - 499 Employees, 500 - 999 Employees, 1000 - 4999 Employees, 5000+ Employees, Don't Know] |
| **position** | **String**|  | [optional] [enum: Executive Management (C-level), VP-level Executive, Manager / Director / Supervisor, Systems Development, Software Development, Web Developer, IT Consultant, Technical Support, Sales, Other technology related, Other non-technology related, Student, Retired] |
| **summary** | **String**|  | [optional] |
| **url** | **String**|  | [optional] |

### Return type

[**EndpointPatchPositionsID**](EndpointPatchPositionsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="positionsPost"></a>
# **positionsPost**
> EndpointPostPositions positionsPost(category, organization, role, startDate, endDate, organizationSize, position, summary, url)



Update the OAuth&#39;ed end user&#39;s Curriculum Vitae by adding a position.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    PositionsApi apiInstance = new PositionsApi(defaultClient);
    String category = "Experience"; // String | 
    String organization = "organization_example"; // String | 
    String role = "role_example"; // String | 
    String startDate = "startDate_example"; // String | 
    String endDate = "endDate_example"; // String | 
    String organizationSize = "Self-employed"; // String | 
    String position = "Executive Management (C-level)"; // String | 
    String summary = "summary_example"; // String | 
    String url = "url_example"; // String | 
    try {
      EndpointPostPositions result = apiInstance.positionsPost(category, organization, role, startDate, endDate, organizationSize, position, summary, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionsApi#positionsPost");
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
| **category** | **String**|  | [enum: Experience, Education, Awards, Affiliations, Portfolio] |
| **organization** | **String**|  | |
| **role** | **String**|  | |
| **startDate** | **String**|  | |
| **endDate** | **String**|  | [optional] |
| **organizationSize** | **String**|  | [optional] [enum: Self-employed, 2 - 9 Employees, 10 - 49 Employees, 50 - 99 Employees, 100 - 499 Employees, 500 - 999 Employees, 1000 - 4999 Employees, 5000+ Employees, Don't Know] |
| **position** | **String**|  | [optional] [enum: Executive Management (C-level), VP-level Executive, Manager / Director / Supervisor, Systems Development, Software Development, Web Developer, IT Consultant, Technical Support, Sales, Other technology related, Other non-technology related, Student, Retired] |
| **summary** | **String**|  | [optional] |
| **url** | **String**|  | [optional] |

### Return type

[**EndpointPostPositions**](EndpointPostPositions.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

