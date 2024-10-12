# DefaultApi

All URIs are relative to *http://,*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**loginAndGetBearerToken**](DefaultApi.md#loginAndGetBearerToken) | **POST** /api/login | Login and get bearer token |
| [**logout**](DefaultApi.md#logout) | **POST** /api/logout | Logout |
| [**register**](DefaultApi.md#register) | **POST** /api/register | Register |
| [**registerAndCreateStoreConnectionForWooCommerce**](DefaultApi.md#registerAndCreateStoreConnectionForWooCommerce) | **POST** /api/register_woocommerce | Register and Create Store Connection for WooCommerce |


<a id="loginAndGetBearerToken"></a>
# **loginAndGetBearerToken**
> loginAndGetBearerToken(email, password)

Login and get bearer token

Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String email = "{{email}}"; // String | The same email you use for our platform.
    String password = "{{password}}"; // String | The password email you use for our platform.
    try {
      apiInstance.loginAndGetBearerToken(email, password);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#loginAndGetBearerToken");
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
| **email** | **String**| The same email you use for our platform. | [optional] |
| **password** | **String**| The password email you use for our platform. | [optional] |

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
| **200** |  |  -  |

<a id="logout"></a>
# **logout**
> logout(email)

Logout

Once you are done, call this endpoint to lock your account!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String email = "{{email}}"; // String | The same email you use for our platform.
    try {
      apiInstance.logout(email);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#logout");
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
| **email** | **String**| The same email you use for our platform. | [optional] |

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
| **200** |  |  -  |

<a id="register"></a>
# **register**
> register(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser)

Register

Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String firstName = "Felix"; // String | required
    String lastName = "Weber"; // String | required
    String companyName = "Fiverr"; // String | required
    String shopUrl = "https;//www.fiverr.de"; // String | required
    String email = "fiverr2@fiverr.de"; // String | required
    String storeName = "Fiverr Store"; // String | required
    String storeUrl = "https;//www.fiverr.de"; // String | required
    String password = "12345678"; // String | required
    String fromuser = "1"; // String | required (always 1)
    try {
      apiInstance.register(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#register");
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
| **firstName** | **String**| required | [optional] |
| **lastName** | **String**| required | [optional] |
| **companyName** | **String**| required | [optional] |
| **shopUrl** | **String**| required | [optional] |
| **email** | **String**| required | [optional] |
| **storeName** | **String**| required | [optional] |
| **storeUrl** | **String**| required | [optional] |
| **password** | **String**| required | [optional] |
| **fromuser** | **String**| required (always 1) | [optional] |

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
| **200** |  |  -  |

<a id="registerAndCreateStoreConnectionForWooCommerce"></a>
# **registerAndCreateStoreConnectionForWooCommerce**
> registerAndCreateStoreConnectionForWooCommerce(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, apiUrl, consumerKey, consumerSecret)

Register and Create Store Connection for WooCommerce

Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String firstName = "Felix"; // String | required
    String lastName = "Weber"; // String | required
    String companyName = "Fiverr"; // String | required
    String shopUrl = "https;//www.fiverr.de"; // String | required
    String email = "fiver3r23@fiverr.de"; // String | required
    String storeName = "Fiverr Store"; // String | required
    String storeUrl = "https;//www.fiverr.de"; // String | required
    String password = "12345678"; // String | required
    String fromuser = "1"; // String | required (always 1)
    String apiUrl = "https://woocommerce-351439-1090797.cloudwaysapps.com/"; // String | required
    String consumerKey = "ck_59b23d313ae372feaf211652c318fbe4501abda2"; // String | required
    String consumerSecret = "cs_acc202d648bfa6b69efe553bb25086230ba116a7"; // String | required
    try {
      apiInstance.registerAndCreateStoreConnectionForWooCommerce(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, apiUrl, consumerKey, consumerSecret);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#registerAndCreateStoreConnectionForWooCommerce");
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
| **firstName** | **String**| required | [optional] |
| **lastName** | **String**| required | [optional] |
| **companyName** | **String**| required | [optional] |
| **shopUrl** | **String**| required | [optional] |
| **email** | **String**| required | [optional] |
| **storeName** | **String**| required | [optional] |
| **storeUrl** | **String**| required | [optional] |
| **password** | **String**| required | [optional] |
| **fromuser** | **String**| required (always 1) | [optional] |
| **apiUrl** | **String**| required | [optional] |
| **consumerKey** | **String**| required | [optional] |
| **consumerSecret** | **String**| required | [optional] |

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
| **200** |  |  -  |

