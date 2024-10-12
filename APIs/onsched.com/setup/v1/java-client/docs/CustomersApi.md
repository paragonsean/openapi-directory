# CustomersApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1CustomersGet**](CustomersApi.md#setupV1CustomersGet) | **GET** /setup/v1/customers | List Customers |
| [**setupV1CustomersIdGet**](CustomersApi.md#setupV1CustomersIdGet) | **GET** /setup/v1/customers/{id} | Get Customer |
| [**setupV1CustomersIdPrivacyGet**](CustomersApi.md#setupV1CustomersIdPrivacyGet) | **GET** /setup/v1/customers/{id}/privacy | Get Customer Data |


<a id="setupV1CustomersGet"></a>
# **setupV1CustomersGet**
> CustomerListViewModel setupV1CustomersGet(locationId, groupId, email, lastname, deleted, offset, limit)

List Customers

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Customers&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    String groupId = "groupId_example"; // String | Filter by groupId
    String email = "email_example"; // String | Filter by email address.
    String lastname = "lastname_example"; // String | Search by lastname.
    Boolean deleted = true; // Boolean | Filter by deleted status.
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      CustomerListViewModel result = apiInstance.setupV1CustomersGet(locationId, groupId, email, lastname, deleted, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#setupV1CustomersGet");
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
| **locationId** | **String**| id of business location, defaults to primary business location | [optional] |
| **groupId** | **String**| Filter by groupId | [optional] |
| **email** | **String**| Filter by email address. | [optional] |
| **lastname** | **String**| Search by lastname. | [optional] |
| **deleted** | **Boolean**| Filter by deleted status. | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**CustomerListViewModel**](CustomerListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CustomersIdGet"></a>
# **setupV1CustomersIdGet**
> CustomerViewModel setupV1CustomersIdGet(id)

Get Customer

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s by using the &lt;i&gt;GET /setup/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String id = "id_example"; // String | id of customer object
    try {
      CustomerViewModel result = apiInstance.setupV1CustomersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#setupV1CustomersIdGet");
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
| **id** | **String**| id of customer object | |

### Return type

[**CustomerViewModel**](CustomerViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CustomersIdPrivacyGet"></a>
# **setupV1CustomersIdPrivacyGet**
> CustomerPrivacyViewModel setupV1CustomersIdPrivacyGet(id)

Get Customer Data

&lt;p&gt;Use this endpoint to return the &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s using the &lt;i&gt;GET /setup/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String id = "id_example"; // String | id of customer object
    try {
      CustomerPrivacyViewModel result = apiInstance.setupV1CustomersIdPrivacyGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#setupV1CustomersIdPrivacyGet");
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
| **id** | **String**| id of customer object | |

### Return type

[**CustomerPrivacyViewModel**](CustomerPrivacyViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

