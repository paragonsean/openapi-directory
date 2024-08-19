# InternalUserApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInternalUserEntity**](InternalUserApi.md#createInternalUserEntity) | **POST** /user | POST for internalUser |
| [**deleteInternalUserEntity**](InternalUserApi.md#deleteInternalUserEntity) | **DELETE** /user/{internal_user_id} | DELETE for internalUser |
| [**getInternalUserCollection**](InternalUserApi.md#getInternalUserCollection) | **GET** /user/list | GET for internalUser |
| [**getInternalUserCountCollection**](InternalUserApi.md#getInternalUserCountCollection) | **GET** /user/count | COUNT for internalUser |
| [**getInternalUserEntity**](InternalUserApi.md#getInternalUserEntity) | **GET** /user/{internal_user_id} | GET for internalUser |
| [**updateInternalUserEntity**](InternalUserApi.md#updateInternalUserEntity) | **PUT** /user/{internal_user_id} | PUT for internalUser |


<a id="createInternalUserEntity"></a>
# **createInternalUserEntity**
> InternalUserEntityRelation createInternalUserEntity(X_API2CRM_USER_KEY, body)

POST for internalUser

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    InternalUserApi apiInstance = new InternalUserApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    InternalUserEntity body = new InternalUserEntity(); // InternalUserEntity | 
    try {
      InternalUserEntityRelation result = apiInstance.createInternalUserEntity(X_API2CRM_USER_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalUserApi#createInternalUserEntity");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **body** | [**InternalUserEntity**](InternalUserEntity.md)|  | |

### Return type

[**InternalUserEntityRelation**](InternalUserEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Client Error |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="deleteInternalUserEntity"></a>
# **deleteInternalUserEntity**
> deleteInternalUserEntity(X_API2CRM_USER_KEY, internalUserId)

DELETE for internalUser

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    InternalUserApi apiInstance = new InternalUserApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String internalUserId = "internalUserId_example"; // String | Internal User Key
    try {
      apiInstance.deleteInternalUserEntity(X_API2CRM_USER_KEY, internalUserId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalUserApi#deleteInternalUserEntity");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **internalUserId** | **String**| Internal User Key | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="getInternalUserCollection"></a>
# **getInternalUserCollection**
> List&lt;InternalUserEntity&gt; getInternalUserCollection(X_API2CRM_USER_KEY, pageSize, page, filter, fields, sort, applicationRequestStart, applicationRequestEnd)

GET for internalUser

Returns all internal users from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    InternalUserApi apiInstance = new InternalUserApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    Integer pageSize = 56; // Integer | Amount of results (default: 25)
    Integer page = 56; // Integer | Page to show (default: 1)
    String filter = "filter_example"; // String | Filter
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    String sort = "sort_example"; // String | Specifies ascending or descending sort on existing fields
    LocalDate applicationRequestStart = LocalDate.now(); // LocalDate | All Application Requests from this date
    LocalDate applicationRequestEnd = LocalDate.now(); // LocalDate | All Application Requests until this date
    try {
      List<InternalUserEntity> result = apiInstance.getInternalUserCollection(X_API2CRM_USER_KEY, pageSize, page, filter, fields, sort, applicationRequestStart, applicationRequestEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalUserApi#getInternalUserCollection");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **pageSize** | **Integer**| Amount of results (default: 25) | [optional] |
| **page** | **Integer**| Page to show (default: 1) | [optional] |
| **filter** | **String**| Filter | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |
| **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] |
| **applicationRequestStart** | **LocalDate**| All Application Requests from this date | [optional] |
| **applicationRequestEnd** | **LocalDate**| All Application Requests until this date | [optional] |

### Return type

[**List&lt;InternalUserEntity&gt;**](InternalUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="getInternalUserCountCollection"></a>
# **getInternalUserCountCollection**
> Count getInternalUserCountCollection(X_API2CRM_USER_KEY, filter)

COUNT for internalUser

Count all internal users from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    InternalUserApi apiInstance = new InternalUserApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String filter = "filter_example"; // String | Filter
    try {
      Count result = apiInstance.getInternalUserCountCollection(X_API2CRM_USER_KEY, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalUserApi#getInternalUserCountCollection");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **filter** | **String**| Filter | [optional] |

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="getInternalUserEntity"></a>
# **getInternalUserEntity**
> InternalUserEntity getInternalUserEntity(X_API2CRM_USER_KEY, internalUserId, fields, applicationRequestStart, applicationRequestEnd)

GET for internalUser

Return internal user information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    InternalUserApi apiInstance = new InternalUserApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String internalUserId = "internalUserId_example"; // String | Internal User Key
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    LocalDate applicationRequestStart = LocalDate.now(); // LocalDate | All Application Requests from this date
    LocalDate applicationRequestEnd = LocalDate.now(); // LocalDate | All Application Requests until this date
    try {
      InternalUserEntity result = apiInstance.getInternalUserEntity(X_API2CRM_USER_KEY, internalUserId, fields, applicationRequestStart, applicationRequestEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalUserApi#getInternalUserEntity");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **internalUserId** | **String**| Internal User Key | |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |
| **applicationRequestStart** | **LocalDate**| All Application Requests from this date | [optional] |
| **applicationRequestEnd** | **LocalDate**| All Application Requests until this date | [optional] |

### Return type

[**InternalUserEntity**](InternalUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="updateInternalUserEntity"></a>
# **updateInternalUserEntity**
> InternalUserEntityRelation updateInternalUserEntity(X_API2CRM_USER_KEY, internalUserId, body)

PUT for internalUser

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InternalUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    InternalUserApi apiInstance = new InternalUserApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | User Key
    String internalUserId = "internalUserId_example"; // String | Internal User Key
    InternalUserEntity body = new InternalUserEntity(); // InternalUserEntity | 
    try {
      InternalUserEntityRelation result = apiInstance.updateInternalUserEntity(X_API2CRM_USER_KEY, internalUserId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InternalUserApi#updateInternalUserEntity");
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
| **X_API2CRM_USER_KEY** | **String**| User Key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **internalUserId** | **String**| Internal User Key | |
| **body** | [**InternalUserEntity**](InternalUserEntity.md)|  | |

### Return type

[**InternalUserEntityRelation**](InternalUserEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Client Error |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

