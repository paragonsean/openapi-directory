# ApplicationsApi

All URIs are relative to *http://vmware.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addApplication**](ApplicationsApi.md#addApplication) | **POST** /groups/applications | Create an application |
| [**addTier**](ApplicationsApi.md#addTier) | **POST** /groups/applications/{id}/tiers | Create tier in application |
| [**deleteApplication**](ApplicationsApi.md#deleteApplication) | **DELETE** /groups/applications/{id} | Delete an application |
| [**deleteTier**](ApplicationsApi.md#deleteTier) | **DELETE** /groups/applications/{id}/tiers/{tier-id} | Delete tier |
| [**getApplication**](ApplicationsApi.md#getApplication) | **GET** /groups/applications/{id} | Show application details |
| [**getApplicationTier**](ApplicationsApi.md#getApplicationTier) | **GET** /groups/applications/{id}/tiers/{tier-id} | Show tier details |
| [**getTier**](ApplicationsApi.md#getTier) | **GET** /groups/tiers/{tier-id} | Show tier details |
| [**listApplicationTiers**](ApplicationsApi.md#listApplicationTiers) | **GET** /groups/applications/{id}/tiers | List tiers of an application |
| [**listApplications**](ApplicationsApi.md#listApplications) | **GET** /groups/applications | List applications |


<a id="addApplication"></a>
# **addApplication**
> Application addApplication(applicationRequest)

Create an application

Application is a group of tiers. A tier is a group of virtual machines based on membership criteria. Tiers are bound to single application. An application name is unique and should not conflict with another application name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    ApplicationRequest applicationRequest = new ApplicationRequest(); // ApplicationRequest | 
    try {
      Application result = apiInstance.addApplication(applicationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#addApplication");
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
| **applicationRequest** | [**ApplicationRequest**](ApplicationRequest.md)|  | |

### Return type

[**Application**](Application.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, create_time, created_by, entity_id, entity_type, last_modified_by, last_modified_time, name

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="addTier"></a>
# **addTier**
> addTier(id, tierRequest)

Create tier in application

Create a tier of an application by with specified membership criteria. The membership criteria id defined in terms of virtual machines or ip addresses/subnet. Please refer to API Guide on how to construct membership criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String id = "id_example"; // String | entity id
    TierRequest tierRequest = new TierRequest(); // TierRequest | 
    try {
      apiInstance.addTier(id, tierRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#addTier");
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
| **id** | **String**| entity id | |
| **tierRequest** | [**TierRequest**](TierRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application, application/json, entity_id, entity_type, group_membership_criteria, name

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="deleteApplication"></a>
# **deleteApplication**
> deleteApplication(id)

Delete an application

Deleting an application deletes all the tiers of the application along with the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String id = "id_example"; // String | entity id
    try {
      apiInstance.deleteApplication(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#deleteApplication");
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
| **id** | **String**| entity id | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="deleteTier"></a>
# **deleteTier**
> deleteTier(id, tierId)

Delete tier

Delete tier of an application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String id = "id_example"; // String | entity id
    String tierId = "tierId_example"; // String | 
    try {
      apiInstance.deleteTier(id, tierId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#deleteTier");
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
| **id** | **String**| entity id | |
| **tierId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="getApplication"></a>
# **getApplication**
> Application getApplication(id)

Show application details

Show application details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String id = "id_example"; // String | entity id
    try {
      Application result = apiInstance.getApplication(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#getApplication");
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
| **id** | **String**| entity id | |

### Return type

[**Application**](Application.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, create_time, created_by, entity_id, entity_type, last_modified_by, last_modified_time, name

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getApplicationTier"></a>
# **getApplicationTier**
> getApplicationTier(id, tierId)

Show tier details

Show tier details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String id = "id_example"; // String | entity id
    String tierId = "tierId_example"; // String | 
    try {
      apiInstance.getApplicationTier(id, tierId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#getApplicationTier");
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
| **id** | **String**| entity id | |
| **tierId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application, application/json, entity_id, entity_type, group_membership_criteria, name

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="getTier"></a>
# **getTier**
> getTier(tierId, authorization)

Show tier details

Show tier details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String tierId = "tierId_example"; // String | 
    String authorization = "authorization_example"; // String | Authorization Header
    try {
      apiInstance.getTier(tierId, authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#getTier");
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
| **tierId** | **String**|  | |
| **authorization** | **String**| Authorization Header | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application, application/json, entity_id, entity_type, group_membership_criteria, name

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="listApplicationTiers"></a>
# **listApplicationTiers**
> TierListResponse listApplicationTiers(id)

List tiers of an application

List tiers of an application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    String id = "id_example"; // String | entity id
    try {
      TierListResponse result = apiInstance.listApplicationTiers(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#listApplicationTiers");
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
| **id** | **String**| entity id | |

### Return type

[**TierListResponse**](TierListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, results

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="listApplications"></a>
# **listApplications**
> PagedListResponse listApplications(size, cursor, startTime, endTime)

List applications

List applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ApplicationsApi apiInstance = new ApplicationsApi(defaultClient);
    BigDecimal size = new BigDecimal("10"); // BigDecimal | page size of results
    String cursor = "cursor_example"; // String | cursor from previous response
    BigDecimal startTime = new BigDecimal(78); // BigDecimal | start time for query in epoch seconds
    BigDecimal endTime = new BigDecimal(78); // BigDecimal | end time for query in epoch seconds
    try {
      PagedListResponse result = apiInstance.listApplications(size, cursor, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApi#listApplications");
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
| **size** | **BigDecimal**| page size of results | [optional] [default to 10] |
| **cursor** | **String**| cursor from previous response | [optional] |
| **startTime** | **BigDecimal**| start time for query in epoch seconds | [optional] |
| **endTime** | **BigDecimal**| end time for query in epoch seconds | [optional] |

### Return type

[**PagedListResponse**](PagedListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, results, total_count

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

