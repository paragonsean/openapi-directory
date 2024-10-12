# BadgesApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminListBadges**](BadgesApi.md#adminListBadges) | **GET** /admin/badges.json | List badges |
| [**createBadge**](BadgesApi.md#createBadge) | **POST** /admin/badges.json | Create badge |
| [**deleteBadge**](BadgesApi.md#deleteBadge) | **DELETE** /admin/badges/{id}.json | Delete badge |
| [**listUserBadges**](BadgesApi.md#listUserBadges) | **GET** /user-badges/{username}.json | List badges for a user |
| [**updateBadge**](BadgesApi.md#updateBadge) | **PUT** /admin/badges/{id}.json | Update badge |


<a id="adminListBadges"></a>
# **adminListBadges**
> AdminListBadges200Response adminListBadges()

List badges

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    try {
      AdminListBadges200Response result = apiInstance.adminListBadges();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#adminListBadges");
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

[**AdminListBadges200Response**](AdminListBadges200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="createBadge"></a>
# **createBadge**
> CreateBadge200Response createBadge(createBadgeRequest)

Create badge

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    CreateBadgeRequest createBadgeRequest = new CreateBadgeRequest(); // CreateBadgeRequest | 
    try {
      CreateBadge200Response result = apiInstance.createBadge(createBadgeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#createBadge");
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
| **createBadgeRequest** | [**CreateBadgeRequest**](CreateBadgeRequest.md)|  | [optional] |

### Return type

[**CreateBadge200Response**](CreateBadge200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="deleteBadge"></a>
# **deleteBadge**
> deleteBadge(id)

Delete badge

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      apiInstance.deleteBadge(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#deleteBadge");
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
| **id** | **Integer**|  | |

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
| **200** | success response |  -  |

<a id="listUserBadges"></a>
# **listUserBadges**
> ListUserBadges200Response listUserBadges(username)

List badges for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      ListUserBadges200Response result = apiInstance.listUserBadges(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#listUserBadges");
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
| **username** | **String**|  | |

### Return type

[**ListUserBadges200Response**](ListUserBadges200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="updateBadge"></a>
# **updateBadge**
> CreateBadge200Response updateBadge(id, createBadgeRequest)

Update badge

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    Integer id = 56; // Integer | 
    CreateBadgeRequest createBadgeRequest = new CreateBadgeRequest(); // CreateBadgeRequest | 
    try {
      CreateBadge200Response result = apiInstance.updateBadge(id, createBadgeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#updateBadge");
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
| **id** | **Integer**|  | |
| **createBadgeRequest** | [**CreateBadgeRequest**](CreateBadgeRequest.md)|  | [optional] |

### Return type

[**CreateBadge200Response**](CreateBadge200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

