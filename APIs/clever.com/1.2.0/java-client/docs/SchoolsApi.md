# SchoolsApi

All URIs are relative to *https://api.clever.com/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDistrictForSchool**](SchoolsApi.md#getDistrictForSchool) | **GET** /schools/{id}/district |  |
| [**getSchool**](SchoolsApi.md#getSchool) | **GET** /schools/{id} |  |
| [**getSchools**](SchoolsApi.md#getSchools) | **GET** /schools |  |
| [**getSectionsForSchool**](SchoolsApi.md#getSectionsForSchool) | **GET** /schools/{id}/sections |  |
| [**getStudentsForSchool**](SchoolsApi.md#getStudentsForSchool) | **GET** /schools/{id}/students |  |
| [**getTeachersForSchool**](SchoolsApi.md#getTeachersForSchool) | **GET** /schools/{id}/teachers |  |


<a id="getDistrictForSchool"></a>
# **getDistrictForSchool**
> DistrictResponse getDistrictForSchool(id)



Returns the district for a school

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      DistrictResponse result = apiInstance.getDistrictForSchool(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#getDistrictForSchool");
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

### Return type

[**DistrictResponse**](DistrictResponse.md)

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

<a id="getSchool"></a>
# **getSchool**
> SchoolResponse getSchool(id)



Returns a specific school

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      SchoolResponse result = apiInstance.getSchool(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#getSchool");
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

### Return type

[**SchoolResponse**](SchoolResponse.md)

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

<a id="getSchools"></a>
# **getSchools**
> SchoolsResponse getSchools(limit, startingAfter, endingBefore, where)



Returns a list of schools

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    String where = "where_example"; // String | 
    try {
      SchoolsResponse result = apiInstance.getSchools(limit, startingAfter, endingBefore, where);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#getSchools");
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

<a id="getSectionsForSchool"></a>
# **getSectionsForSchool**
> SectionsResponse getSectionsForSchool(id, limit, startingAfter, endingBefore, where)



Returns the sections for a school

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    String id = "id_example"; // String | 
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    String where = "where_example"; // String | 
    try {
      SectionsResponse result = apiInstance.getSectionsForSchool(id, limit, startingAfter, endingBefore, where);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#getSectionsForSchool");
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
| **where** | **String**|  | [optional] |

### Return type

[**SectionsResponse**](SectionsResponse.md)

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

<a id="getStudentsForSchool"></a>
# **getStudentsForSchool**
> StudentsResponse getStudentsForSchool(id, limit, startingAfter, endingBefore, where)



Returns the students for a school

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    String id = "id_example"; // String | 
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    String where = "where_example"; // String | 
    try {
      StudentsResponse result = apiInstance.getStudentsForSchool(id, limit, startingAfter, endingBefore, where);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#getStudentsForSchool");
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
| **where** | **String**|  | [optional] |

### Return type

[**StudentsResponse**](StudentsResponse.md)

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

<a id="getTeachersForSchool"></a>
# **getTeachersForSchool**
> TeachersResponse getTeachersForSchool(id, limit, startingAfter, endingBefore, where)



Returns the teachers for a school

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SchoolsApi apiInstance = new SchoolsApi(defaultClient);
    String id = "id_example"; // String | 
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    String where = "where_example"; // String | 
    try {
      TeachersResponse result = apiInstance.getTeachersForSchool(id, limit, startingAfter, endingBefore, where);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchoolsApi#getTeachersForSchool");
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
| **where** | **String**|  | [optional] |

### Return type

[**TeachersResponse**](TeachersResponse.md)

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

