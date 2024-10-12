# DistrictAdminsApi

All URIs are relative to *https://api.clever.com/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDistrictAdmin**](DistrictAdminsApi.md#getDistrictAdmin) | **GET** /district_admins/{id} |  |
| [**getDistrictAdmins**](DistrictAdminsApi.md#getDistrictAdmins) | **GET** /district_admins |  |


<a id="getDistrictAdmin"></a>
# **getDistrictAdmin**
> DistrictAdminResponse getDistrictAdmin(id)



Returns a specific district admin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistrictAdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DistrictAdminsApi apiInstance = new DistrictAdminsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      DistrictAdminResponse result = apiInstance.getDistrictAdmin(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistrictAdminsApi#getDistrictAdmin");
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

[**DistrictAdminResponse**](DistrictAdminResponse.md)

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

<a id="getDistrictAdmins"></a>
# **getDistrictAdmins**
> DistrictAdminsResponse getDistrictAdmins(startingAfter, endingBefore, showLinks)



Returns a list of district admins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistrictAdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever.com/v1.2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DistrictAdminsApi apiInstance = new DistrictAdminsApi(defaultClient);
    String startingAfter = "startingAfter_example"; // String | 
    String endingBefore = "endingBefore_example"; // String | 
    String showLinks = "showLinks_example"; // String | 
    try {
      DistrictAdminsResponse result = apiInstance.getDistrictAdmins(startingAfter, endingBefore, showLinks);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistrictAdminsApi#getDistrictAdmins");
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
| **startingAfter** | **String**|  | [optional] |
| **endingBefore** | **String**|  | [optional] |
| **showLinks** | **String**|  | [optional] |

### Return type

[**DistrictAdminsResponse**](DistrictAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK Response |  -  |

