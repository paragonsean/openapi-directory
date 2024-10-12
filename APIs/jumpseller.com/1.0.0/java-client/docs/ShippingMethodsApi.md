# ShippingMethodsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**shippingMethodsIdJsonDelete**](ShippingMethodsApi.md#shippingMethodsIdJsonDelete) | **DELETE** /shipping_methods/{id}.json | Delete an existing Shipping Method. |
| [**shippingMethodsIdJsonGet**](ShippingMethodsApi.md#shippingMethodsIdJsonGet) | **GET** /shipping_methods/{id}.json | Retrieve a single Shipping Method. |
| [**shippingMethodsIdJsonPut**](ShippingMethodsApi.md#shippingMethodsIdJsonPut) | **PUT** /shipping_methods/{id}.json | Update a Shipping Method. |
| [**shippingMethodsJsonGet**](ShippingMethodsApi.md#shippingMethodsJsonGet) | **GET** /shipping_methods.json | Retrieve all Store&#39;s Shipping Methods. |
| [**shippingMethodsJsonPost**](ShippingMethodsApi.md#shippingMethodsJsonPost) | **POST** /shipping_methods.json | Creates a Shipping Method. |


<a id="shippingMethodsIdJsonDelete"></a>
# **shippingMethodsIdJsonDelete**
> String shippingMethodsIdJsonDelete(login, authtoken, id)

Delete an existing Shipping Method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ShippingMethodsApi apiInstance = new ShippingMethodsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Shipping Method
    try {
      String result = apiInstance.shippingMethodsIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingMethodsApi#shippingMethodsIdJsonDelete");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Shipping Method | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Shipping Method Not Found. |  -  |

<a id="shippingMethodsIdJsonGet"></a>
# **shippingMethodsIdJsonGet**
> ShippingMethod shippingMethodsIdJsonGet(login, authtoken, id)

Retrieve a single Shipping Method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ShippingMethodsApi apiInstance = new ShippingMethodsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Shipping Method
    try {
      ShippingMethod result = apiInstance.shippingMethodsIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingMethodsApi#shippingMethodsIdJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Shipping Method | |

### Return type

[**ShippingMethod**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | ShippingMethod Not Found. |  -  |

<a id="shippingMethodsIdJsonPut"></a>
# **shippingMethodsIdJsonPut**
> ShippingMethod shippingMethodsIdJsonPut(login, authtoken, id, shippingMethodEdit)

Update a Shipping Method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ShippingMethodsApi apiInstance = new ShippingMethodsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Shipping Method
    ShippingMethodEdit shippingMethodEdit = new ShippingMethodEdit(); // ShippingMethodEdit | Shipping Method parameters.
    try {
      ShippingMethod result = apiInstance.shippingMethodsIdJsonPut(login, authtoken, id, shippingMethodEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingMethodsApi#shippingMethodsIdJsonPut");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Shipping Method | |
| **shippingMethodEdit** | [**ShippingMethodEdit**](ShippingMethodEdit.md)| Shipping Method parameters. | |

### Return type

[**ShippingMethod**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Shipping Method Not Found. |  -  |

<a id="shippingMethodsJsonGet"></a>
# **shippingMethodsJsonGet**
> List&lt;ShippingMethod&gt; shippingMethodsJsonGet(login, authtoken)

Retrieve all Store&#39;s Shipping Methods.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ShippingMethodsApi apiInstance = new ShippingMethodsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      List<ShippingMethod> result = apiInstance.shippingMethodsJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingMethodsApi#shippingMethodsJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |

### Return type

[**List&lt;ShippingMethod&gt;**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Shipping Methods |  -  |

<a id="shippingMethodsJsonPost"></a>
# **shippingMethodsJsonPost**
> ShippingMethod shippingMethodsJsonPost(login, authtoken, shippingMethodEdit)

Creates a Shipping Method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ShippingMethodsApi apiInstance = new ShippingMethodsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    ShippingMethodEdit shippingMethodEdit = new ShippingMethodEdit(); // ShippingMethodEdit | Shipping Method parameters.
    try {
      ShippingMethod result = apiInstance.shippingMethodsJsonPost(login, authtoken, shippingMethodEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShippingMethodsApi#shippingMethodsJsonPost");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **shippingMethodEdit** | [**ShippingMethodEdit**](ShippingMethodEdit.md)| Shipping Method parameters. | |

### Return type

[**ShippingMethod**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | ShippingMethod Not Found. |  -  |

