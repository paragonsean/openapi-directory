# TeachersApi

All URIs are relative to *https://api.clever.com/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDistrictForTeacher**](TeachersApi.md#getDistrictForTeacher) | **GET** /teachers/{id}/district |  |
| [**getGradeLevelsForTeacher**](TeachersApi.md#getGradeLevelsForTeacher) | **GET** /teachers/{id}/grade_levels |  |
| [**getSchoolForTeacher**](TeachersApi.md#getSchoolForTeacher) | **GET** /teachers/{id}/school |  |
| [**getSectionsForTeacher**](TeachersApi.md#getSectionsForTeacher) | **GET** /teachers/{id}/sections |  |
| [**getStudentsForTeacher**](TeachersApi.md#getStudentsForTeacher) | **GET** /teachers/{id}/students |  |
| [**getTeacher**](TeachersApi.md#getTeacher) | **GET** /teachers/{id} |  |
| [**getTeachers**](TeachersApi.md#getTeachers) | **GET** /teachers |  |


<a id="getDistrictForTeacher"></a>
# **getDistrictForTeacher**
> DistrictResponse getDistrictForTeacher(id)



Returns the district for a teacher

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeachersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeachersApi apiInstance = new TeachersApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      DistrictResponse result = apiInstance.getDistrictForTeacher(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeachersApi#getDistrictForTeacher");
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

<a id="getGradeLevelsForTeacher"></a>
# **getGradeLevelsForTeacher**
> GradeLevelsResponse getGradeLevelsForTeacher(id)



Returns the grade levels for sections a teacher teaches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeachersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeachersApi apiInstance = new TeachersApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      GradeLevelsResponse result = apiInstance.getGradeLevelsForTeacher(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeachersApi#getGradeLevelsForTeacher");
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

[**GradeLevelsResponse**](GradeLevelsResponse.md)

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

<a id="getSchoolForTeacher"></a>
# **getSchoolForTeacher**
> SchoolResponse getSchoolForTeacher(id)



Retrieves school info for a teacher.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeachersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeachersApi apiInstance = new TeachersApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      SchoolResponse result = apiInstance.getSchoolForTeacher(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeachersApi#getSchoolForTeacher");
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

<a id="getSectionsForTeacher"></a>
# **getSectionsForTeacher**
> SectionsResponse getSectionsForTeacher(id, limit, startingAfter, endingBefore)



Returns the sections for a teacher

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeachersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeachersApi apiInstance = new TeachersApi(defaultClient);
    String id = "id_example"; // String | 
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    try {
      SectionsResponse result = apiInstance.getSectionsForTeacher(id, limit, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeachersApi#getSectionsForTeacher");
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

<a id="getStudentsForTeacher"></a>
# **getStudentsForTeacher**
> StudentsResponse getStudentsForTeacher(id, limit, startingAfter, endingBefore)



Returns the students for a teacher

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeachersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeachersApi apiInstance = new TeachersApi(defaultClient);
    String id = "id_example"; // String | 
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    try {
      StudentsResponse result = apiInstance.getStudentsForTeacher(id, limit, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeachersApi#getStudentsForTeacher");
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

<a id="getTeacher"></a>
# **getTeacher**
> TeacherResponse getTeacher(id, include)



Returns a specific teacher

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeachersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeachersApi apiInstance = new TeachersApi(defaultClient);
    String id = "id_example"; // String | 
    String include = "include_example"; // String | 
    try {
      TeacherResponse result = apiInstance.getTeacher(id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeachersApi#getTeacher");
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

[**TeacherResponse**](TeacherResponse.md)

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

<a id="getTeachers"></a>
# **getTeachers**
> TeachersResponse getTeachers(limit, startingAfter, endingBefore, where)



Returns a list of teachers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeachersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TeachersApi apiInstance = new TeachersApi(defaultClient);
    Integer limit = 56; // Integer | 
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    String where = "where_example"; // String | 
    try {
      TeachersResponse result = apiInstance.getTeachers(limit, startingAfter, endingBefore, where);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeachersApi#getTeachers");
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

