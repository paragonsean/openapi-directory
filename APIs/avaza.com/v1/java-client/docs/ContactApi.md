# ContactApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contactGet**](ContactApi.md#contactGet) | **GET** /api/Contact | Gets list of Contacts |
| [**contactGetByID**](ContactApi.md#contactGetByID) | **GET** /api/Contact/{id} | Gets Contact by Contact ID |
| [**contactPost**](ContactApi.md#contactPost) | **POST** /api/Contact | Create a Contact |


<a id="contactGet"></a>
# **contactGet**
> ContactList contactGet(updatedAfter, pageSize, pageNumber, sort, companyIDFK)

Gets list of Contacts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ContactApi apiInstance = new ContactApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | 
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String sort = "sort_example"; // String | 
    Integer companyIDFK = 56; // Integer | 
    try {
      ContactList result = apiInstance.contactGet(updatedAfter, pageSize, pageNumber, sort, companyIDFK);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactApi#contactGet");
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

[**ContactList**](ContactList.md)

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

<a id="contactGetByID"></a>
# **contactGetByID**
> CompanyContact contactGetByID(id)

Gets Contact by Contact ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ContactApi apiInstance = new ContactApi(defaultClient);
    Long id = 56L; // Long | Contact ID number
    try {
      CompanyContact result = apiInstance.contactGetByID(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactApi#contactGetByID");
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
| **id** | **Long**| Contact ID number | |

### Return type

[**CompanyContact**](CompanyContact.md)

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
| **404** | Not Found |  -  |

<a id="contactPost"></a>
# **contactPost**
> CompanyContact contactPost(model)

Create a Contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ContactApi apiInstance = new ContactApi(defaultClient);
    NewCompanyContact model = new NewCompanyContact(); // NewCompanyContact | 
    try {
      CompanyContact result = apiInstance.contactPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactApi#contactPost");
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
| **model** | [**NewCompanyContact**](NewCompanyContact.md)|  | |

### Return type

[**CompanyContact**](CompanyContact.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

