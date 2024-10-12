# CustomersApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1CustomersBookingfieldsGet**](CustomersApi.md#consumerV1CustomersBookingfieldsGet) | **GET** /consumer/v1/customers/bookingfields | Get Customer Booking Fields |
| [**consumerV1CustomersCountriesGet**](CustomersApi.md#consumerV1CustomersCountriesGet) | **GET** /consumer/v1/customers/countries | List Country Codes |
| [**consumerV1CustomersCustomfieldsGet**](CustomersApi.md#consumerV1CustomersCustomfieldsGet) | **GET** /consumer/v1/customers/customfields | Get Customer Custom Fields |
| [**consumerV1CustomersGet**](CustomersApi.md#consumerV1CustomersGet) | **GET** /consumer/v1/customers | List Customers |
| [**consumerV1CustomersIdDelete**](CustomersApi.md#consumerV1CustomersIdDelete) | **DELETE** /consumer/v1/customers/{id} | Delete Customer |
| [**consumerV1CustomersIdGet**](CustomersApi.md#consumerV1CustomersIdGet) | **GET** /consumer/v1/customers/{id} | Get Customer |
| [**consumerV1CustomersIdPut**](CustomersApi.md#consumerV1CustomersIdPut) | **PUT** /consumer/v1/customers/{id} | Update Customer |
| [**consumerV1CustomersPost**](CustomersApi.md#consumerV1CustomersPost) | **POST** /consumer/v1/customers | Create Customer |
| [**consumerV1CustomersStatesGet**](CustomersApi.md#consumerV1CustomersStatesGet) | **GET** /consumer/v1/customers/states | List Country States |


<a id="consumerV1CustomersBookingfieldsGet"></a>
# **consumerV1CustomersBookingfieldsGet**
> BookingFieldListViewModel consumerV1CustomersBookingfieldsGet(locationId)

Get Customer Booking Fields

&lt;p&gt;Use this endpoint to return &lt;b&gt;Customer Booking Fields&lt;/b&gt;. Customer booking fields are stored with each customer object. They are used when the information collected during the booking is for a particular customer. Customer Booking Fields include any custom customer fields you define and want to capture with the Booking.&lt;/p&gt;

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
    try {
      BookingFieldListViewModel result = apiInstance.consumerV1CustomersBookingfieldsGet(locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersBookingfieldsGet");
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

### Return type

[**BookingFieldListViewModel**](BookingFieldListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1CustomersCountriesGet"></a>
# **consumerV1CustomersCountriesGet**
> List&lt;CountryViewModel&gt; consumerV1CustomersCountriesGet()

List Country Codes

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Countries with their associated Country Code&lt;/b&gt;. Country codes are based on the 2-character ANSI standard. If your countries of operation are not currently listed, contact us at &lt;i&gt;&lt;b&gt;support@onsched.com&lt;/b&gt;&lt;/i&gt;.&lt;/p&gt;

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
    try {
      List<CountryViewModel> result = apiInstance.consumerV1CustomersCountriesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersCountriesGet");
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

[**List&lt;CountryViewModel&gt;**](CountryViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1CustomersCustomfieldsGet"></a>
# **consumerV1CustomersCustomfieldsGet**
> CustomFieldDefinitionListViewModel consumerV1CustomersCustomfieldsGet(locationId, leadQuestions)

Get Customer Custom Fields

&lt;p&gt;Use this endpoint to return &lt;b&gt;Customer Custom Fields&lt;/b&gt;. Customer custom fields are stored with the customer object. They are used when the information collected during the booking is specific to a particular customer.&lt;/p&gt;

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
    Boolean leadQuestions = true; // Boolean | A true/false indicator to filter on custom fields used for lead questions
    try {
      CustomFieldDefinitionListViewModel result = apiInstance.consumerV1CustomersCustomfieldsGet(locationId, leadQuestions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersCustomfieldsGet");
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
| **leadQuestions** | **Boolean**| A true/false indicator to filter on custom fields used for lead questions | [optional] |

### Return type

[**CustomFieldDefinitionListViewModel**](CustomFieldDefinitionListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1CustomersGet"></a>
# **consumerV1CustomersGet**
> CustomerListViewModel consumerV1CustomersGet(locationId, groupId, email, lastname, deleted, offset, limit)

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
    String email = "email_example"; // String | Filter by email address
    String lastname = "lastname_example"; // String | Filter by lastname
    Boolean deleted = true; // Boolean | Filter by deleted status
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      CustomerListViewModel result = apiInstance.consumerV1CustomersGet(locationId, groupId, email, lastname, deleted, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersGet");
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
| **email** | **String**| Filter by email address | [optional] |
| **lastname** | **String**| Filter by lastname | [optional] |
| **deleted** | **Boolean**| Filter by deleted status | [optional] |
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

<a id="consumerV1CustomersIdDelete"></a>
# **consumerV1CustomersIdDelete**
> consumerV1CustomersIdDelete(id)

Delete Customer

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Customer object. A valid &lt;b&gt;customer id&lt;/b&gt; is required.&lt;/p&gt;

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
      apiInstance.consumerV1CustomersIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersIdDelete");
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

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1CustomersIdGet"></a>
# **consumerV1CustomersIdGet**
> CustomerViewModel consumerV1CustomersIdGet(id)

Get Customer

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s by using the &lt;i&gt;GET /consumer/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

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
      CustomerViewModel result = apiInstance.consumerV1CustomersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersIdGet");
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

<a id="consumerV1CustomersIdPut"></a>
# **consumerV1CustomersIdPut**
> consumerV1CustomersIdPut(id, customerUpdateModel)

Update Customer

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Customer object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Note: Blank fields are not changed.&lt;/p&gt;

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
    CustomerUpdateModel customerUpdateModel = new CustomerUpdateModel(); // CustomerUpdateModel | 
    try {
      apiInstance.consumerV1CustomersIdPut(id, customerUpdateModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersIdPut");
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
| **customerUpdateModel** | [**CustomerUpdateModel**](CustomerUpdateModel.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1CustomersPost"></a>
# **consumerV1CustomersPost**
> CustomerViewModel consumerV1CustomersPost(customerInputModel)

Create Customer

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new Customer. A customer object is automatically created with the first appointment booking if it doesn&#39;t already exist. If not specified, the business location id defaults to the primary business location.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt; or &lt;b&gt;First and Lastname&lt;/b&gt; depending on customer type. Type 0 &#x3D; Person, Type 1 &#x3D; Business. For type 0, the firstname and lastname fields are used. For type 1, the Name field is used, and the name field is also used to populate the lastname.&lt;/p&gt;

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
    CustomerInputModel customerInputModel = new CustomerInputModel(); // CustomerInputModel | 
    try {
      CustomerViewModel result = apiInstance.consumerV1CustomersPost(customerInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersPost");
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
| **customerInputModel** | [**CustomerInputModel**](CustomerInputModel.md)|  | [optional] |

### Return type

[**CustomerViewModel**](CustomerViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1CustomersStatesGet"></a>
# **consumerV1CustomersStatesGet**
> List&lt;StateViewModel&gt; consumerV1CustomersStatesGet(country)

List Country States

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Countries with their associated State Codes&lt;/b&gt;. Supply a country code to filter results further. If states for your countries of operation are not currently listed, contact us at &lt;i&gt;&lt;b&gt;support@onsched.com&lt;/b&gt;&lt;/i&gt;.&lt;/p&gt;

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
    String country = "country_example"; // String | 
    try {
      List<StateViewModel> result = apiInstance.consumerV1CustomersStatesGet(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#consumerV1CustomersStatesGet");
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
| **country** | **String**|  | [optional] |

### Return type

[**List&lt;StateViewModel&gt;**](StateViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

