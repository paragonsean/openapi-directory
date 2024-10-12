# CheckoutCustomFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutCustomFieldsIdJsonDelete**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonDelete) | **DELETE** /checkout_custom_fields/{id}.json | Delete an existing CheckoutCustomField. |
| [**checkoutCustomFieldsIdJsonGet**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonGet) | **GET** /checkout_custom_fields/{id}.json | Retrieve a single CheckoutCustomField. |
| [**checkoutCustomFieldsIdJsonPut**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonPut) | **PUT** /checkout_custom_fields/{id}.json | Update a CheckoutCustomField. |
| [**checkoutCustomFieldsJsonGet**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonGet) | **GET** /checkout_custom_fields.json | Retrieve all Checkout Custom Fields. |
| [**checkoutCustomFieldsJsonPost**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonPost) | **POST** /checkout_custom_fields.json | Create a new CheckoutCustomField. |


<a id="checkoutCustomFieldsIdJsonDelete"></a>
# **checkoutCustomFieldsIdJsonDelete**
> String checkoutCustomFieldsIdJsonDelete(login, authtoken, id)

Delete an existing CheckoutCustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckoutCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CheckoutCustomFieldsApi apiInstance = new CheckoutCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CheckoutCustomField
    try {
      String result = apiInstance.checkoutCustomFieldsIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckoutCustomFieldsApi#checkoutCustomFieldsIdJsonDelete");
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
| **id** | **Integer**| Id of the CheckoutCustomField | |

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
| **404** | CheckoutCustomField Not Found. |  -  |

<a id="checkoutCustomFieldsIdJsonGet"></a>
# **checkoutCustomFieldsIdJsonGet**
> CheckoutCustomField checkoutCustomFieldsIdJsonGet(login, authtoken, id)

Retrieve a single CheckoutCustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckoutCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CheckoutCustomFieldsApi apiInstance = new CheckoutCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CheckoutCustomField
    try {
      CheckoutCustomField result = apiInstance.checkoutCustomFieldsIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckoutCustomFieldsApi#checkoutCustomFieldsIdJsonGet");
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
| **id** | **Integer**| Id of the CheckoutCustomField | |

### Return type

[**CheckoutCustomField**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CheckoutCustomField Not Found. |  -  |

<a id="checkoutCustomFieldsIdJsonPut"></a>
# **checkoutCustomFieldsIdJsonPut**
> CheckoutCustomField checkoutCustomFieldsIdJsonPut(login, authtoken, id, checkoutCustomFieldEdit)

Update a CheckoutCustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckoutCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CheckoutCustomFieldsApi apiInstance = new CheckoutCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CheckoutCustomField
    CheckoutCustomFieldEdit checkoutCustomFieldEdit = new CheckoutCustomFieldEdit(); // CheckoutCustomFieldEdit | CheckoutCustomField parameters.
    try {
      CheckoutCustomField result = apiInstance.checkoutCustomFieldsIdJsonPut(login, authtoken, id, checkoutCustomFieldEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckoutCustomFieldsApi#checkoutCustomFieldsIdJsonPut");
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
| **id** | **Integer**| Id of the CheckoutCustomField | |
| **checkoutCustomFieldEdit** | [**CheckoutCustomFieldEdit**](CheckoutCustomFieldEdit.md)| CheckoutCustomField parameters. | |

### Return type

[**CheckoutCustomField**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CheckoutCustomField Not Found. |  -  |

<a id="checkoutCustomFieldsJsonGet"></a>
# **checkoutCustomFieldsJsonGet**
> List&lt;CheckoutCustomField&gt; checkoutCustomFieldsJsonGet(login, authtoken, limit, page)

Retrieve all Checkout Custom Fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckoutCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CheckoutCustomFieldsApi apiInstance = new CheckoutCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer limit = 50; // Integer | List restriction
    Integer page = 1; // Integer | List page
    try {
      List<CheckoutCustomField> result = apiInstance.checkoutCustomFieldsJsonGet(login, authtoken, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckoutCustomFieldsApi#checkoutCustomFieldsJsonGet");
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
| **limit** | **Integer**| List restriction | [optional] [default to 50] |
| **page** | **Integer**| List page | [optional] [default to 1] |

### Return type

[**List&lt;CheckoutCustomField&gt;**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Checkout Custom Fields |  -  |

<a id="checkoutCustomFieldsJsonPost"></a>
# **checkoutCustomFieldsJsonPost**
> CheckoutCustomField checkoutCustomFieldsJsonPost(login, authtoken, checkoutCustomFieldEdit)

Create a new CheckoutCustomField.

Type values can be: input, selection, checkbox, date or text. Area values can be: contact, billing_shipping or other.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckoutCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CheckoutCustomFieldsApi apiInstance = new CheckoutCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    CheckoutCustomFieldEdit checkoutCustomFieldEdit = new CheckoutCustomFieldEdit(); // CheckoutCustomFieldEdit | CheckoutCustomField parameters.
    try {
      CheckoutCustomField result = apiInstance.checkoutCustomFieldsJsonPost(login, authtoken, checkoutCustomFieldEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckoutCustomFieldsApi#checkoutCustomFieldsJsonPost");
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
| **checkoutCustomFieldEdit** | [**CheckoutCustomFieldEdit**](CheckoutCustomFieldEdit.md)| CheckoutCustomField parameters. | |

### Return type

[**CheckoutCustomField**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CheckoutCustomField Not Found. |  -  |

