# ProductOptionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsIdOptionsCountJsonGet**](ProductOptionsApi.md#productsIdOptionsCountJsonGet) | **GET** /products/{id}/options/count.json | Count all Product Options. |
| [**productsIdOptionsJsonGet**](ProductOptionsApi.md#productsIdOptionsJsonGet) | **GET** /products/{id}/options.json | Retrieve all Product Options. |
| [**productsIdOptionsJsonPost**](ProductOptionsApi.md#productsIdOptionsJsonPost) | **POST** /products/{id}/options.json | Create a new Product Option. |
| [**productsIdOptionsOptionIdJsonDelete**](ProductOptionsApi.md#productsIdOptionsOptionIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}.json | Delete a Product Option. |
| [**productsIdOptionsOptionIdJsonGet**](ProductOptionsApi.md#productsIdOptionsOptionIdJsonGet) | **GET** /products/{id}/options/{option_id}.json | Retrieve a single Product Option. |
| [**productsIdOptionsOptionIdJsonPut**](ProductOptionsApi.md#productsIdOptionsOptionIdJsonPut) | **PUT** /products/{id}/options/{option_id}.json | Modify an existing Product Option. |


<a id="productsIdOptionsCountJsonGet"></a>
# **productsIdOptionsCountJsonGet**
> Count productsIdOptionsCountJsonGet(login, authtoken, id)

Count all Product Options.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionsApi apiInstance = new ProductOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      Count result = apiInstance.productsIdOptionsCountJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionsApi#productsIdOptionsCountJsonGet");
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
| **id** | **Integer**| ID of the Product | |

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
| **404** | Product Not Found. |  -  |

<a id="productsIdOptionsJsonGet"></a>
# **productsIdOptionsJsonGet**
> List&lt;ProductOption&gt; productsIdOptionsJsonGet(login, authtoken, id)

Retrieve all Product Options.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionsApi apiInstance = new ProductOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      List<ProductOption> result = apiInstance.productsIdOptionsJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionsApi#productsIdOptionsJsonGet");
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
| **id** | **Integer**| ID of the Product | |

### Return type

[**List&lt;ProductOption&gt;**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdOptionsJsonPost"></a>
# **productsIdOptionsJsonPost**
> ProductOption productsIdOptionsJsonPost(login, authtoken, id, productOptionEdit)

Create a new Product Option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionsApi apiInstance = new ProductOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    ProductOptionEdit productOptionEdit = new ProductOptionEdit(); // ProductOptionEdit | Product Option parameters.
    try {
      ProductOption result = apiInstance.productsIdOptionsJsonPost(login, authtoken, id, productOptionEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionsApi#productsIdOptionsJsonPost");
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
| **id** | **Integer**| Id of the Product | |
| **productOptionEdit** | [**ProductOptionEdit**](ProductOptionEdit.md)| Product Option parameters. | |

### Return type

[**ProductOption**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productsIdOptionsOptionIdJsonDelete"></a>
# **productsIdOptionsOptionIdJsonDelete**
> String productsIdOptionsOptionIdJsonDelete(login, authtoken, id, optionId)

Delete a Product Option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionsApi apiInstance = new ProductOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer optionId = 56; // Integer | Id of the Product Option
    try {
      String result = apiInstance.productsIdOptionsOptionIdJsonDelete(login, authtoken, id, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionsApi#productsIdOptionsOptionIdJsonDelete");
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
| **id** | **Integer**| Id of the Product | |
| **optionId** | **Integer**| Id of the Product Option | |

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
| **404** | Product Not Found. |  -  |

<a id="productsIdOptionsOptionIdJsonGet"></a>
# **productsIdOptionsOptionIdJsonGet**
> ProductOption productsIdOptionsOptionIdJsonGet(login, authtoken, id, optionId)

Retrieve a single Product Option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionsApi apiInstance = new ProductOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer optionId = 56; // Integer | Id of the Product Option
    try {
      ProductOption result = apiInstance.productsIdOptionsOptionIdJsonGet(login, authtoken, id, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionsApi#productsIdOptionsOptionIdJsonGet");
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
| **id** | **Integer**| Id of the Product | |
| **optionId** | **Integer**| Id of the Product Option | |

### Return type

[**ProductOption**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdOptionsOptionIdJsonPut"></a>
# **productsIdOptionsOptionIdJsonPut**
> ProductOption productsIdOptionsOptionIdJsonPut(login, authtoken, id, optionId, productOptionEdit)

Modify an existing Product Option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionsApi apiInstance = new ProductOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer optionId = 56; // Integer | Id of the Product Option
    ProductOptionEdit productOptionEdit = new ProductOptionEdit(); // ProductOptionEdit | Product option parameters to change
    try {
      ProductOption result = apiInstance.productsIdOptionsOptionIdJsonPut(login, authtoken, id, optionId, productOptionEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionsApi#productsIdOptionsOptionIdJsonPut");
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
| **id** | **Integer**| Id of the Product | |
| **optionId** | **Integer**| Id of the Product Option | |
| **productOptionEdit** | [**ProductOptionEdit**](ProductOptionEdit.md)| Product option parameters to change | |

### Return type

[**ProductOption**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

