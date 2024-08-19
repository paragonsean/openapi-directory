# SchoolAdminsApi

All URIs are relative to *https://api.clever.com/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSchoolAdmin**](SchoolAdminsApi.md#getSchoolAdmin) | **GET** /school_admins/{id} |  |
| [**getSchoolAdmins**](SchoolAdminsApi.md#getSchoolAdmins) | **GET** /school_admins |  |
| [**getSchoolsForSchoolAdmin**](SchoolAdminsApi.md#getSchoolsForSchoolAdmin) | **GET** /school_admins/{id}/schools |  |


<a id="getSchoolAdmin"></a>
# **getSchoolAdmin**
> SchoolAdminResponse getSchoolAdmin(id, include)



Returns a specific school admin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolAdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolAdminsApi apiInstance = new SchoolAdminsApi(defaultClient);
    String id = "id_example"; // String | 
    String include = "include_example"; // String | 
    try {
      SchoolAdminResponse result = apiInstance.getSchoolAdmin(id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolAdminsApi#getSchoolAdmin");
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
| **id** | **String**|  | |
| **include** | **String**|  | [optional] |

### Return type

[**SchoolAdminResponse**](SchoolAdminResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK Response |  -  |
| **404** | Entity Not Found |  -  |

<a id="getSchoolAdmins"></a>
# **getSchoolAdmins**
> SchoolAdminsResponse getSchoolAdmins(limit, startingAfter, endingBefore, where)



Returns a list of school admins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolAdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolAdminsApi apiInstance = new SchoolAdminsApi(defaultClient);
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    String where = "where_example"; // String | 
    try {
      SchoolAdminsResponse result = apiInstance.getSchoolAdmins(limit, startingAfter, endingBefore, where);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolAdminsApi#getSchoolAdmins");
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
| **limit** | **Integer**|  | [optional] |
| **startingAfter** | **String**|  | [optional] |
| **endingBefore** | **String**|  | [optional] |
| **where** | **String**|  | [optional] |

### Return type

[**SchoolAdminsResponse**](SchoolAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK Response |  -  |

<a id="getSchoolsForSchoolAdmin"></a>
# **getSchoolsForSchoolAdmin**
> SchoolsResponse getSchoolsForSchoolAdmin(id, limit, startingAfter, endingBefore)



Returns the schools for a school admin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolAdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolAdminsApi apiInstance = new SchoolAdminsApi(defaultClient);
    String id = "id_example"; // String | 
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    try {
      SchoolsResponse result = apiInstance.getSchoolsForSchoolAdmin(id, limit, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolAdminsApi#getSchoolsForSchoolAdmin");
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
| **id** | **String**|  | |
| **limit** | **Integer**|  | [optional] |
| **startingAfter** | **String**|  | [optional] |
| **endingBefore** | **String**|  | [optional] |

### Return type

[**SchoolsResponse**](SchoolsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK Response |  -  |
| **404** | Entity Not Found |  -  |

