# ProductOptionValuesApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsIdOptionsOptionIdValuesCountJsonGet**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesCountJsonGet) | **GET** /products/{id}/options/{option_id}/values/count.json | Count all Product Option Values. |
| [**productsIdOptionsOptionIdValuesJsonGet**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonGet) | **GET** /products/{id}/options/{option_id}/values.json | Retrieve all Product Option Values. |
| [**productsIdOptionsOptionIdValuesJsonPost**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonPost) | **POST** /products/{id}/options/{option_id}/values.json | Create a new Product Option Value. |
| [**productsIdOptionsOptionIdValuesValueIdJsonDelete**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}/values/{value_id}.json | Delete a Product Option Value. |
| [**productsIdOptionsOptionIdValuesValueIdJsonGet**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonGet) | **GET** /products/{id}/options/{option_id}/values/{value_id}.json | Retrieve a single Product Option Value. |
| [**productsIdOptionsOptionIdValuesValueIdJsonPut**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonPut) | **PUT** /products/{id}/options/{option_id}/values/{value_id}.json | Modify an existing Product Option Value. |


<a id="productsIdOptionsOptionIdValuesCountJsonGet"></a>
# **productsIdOptionsOptionIdValuesCountJsonGet**
> Count productsIdOptionsOptionIdValuesCountJsonGet(login, authtoken, id, optionId)

Count all Product Option Values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionValuesApi apiInstance = new ProductOptionValuesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    Integer optionId = 56; // Integer | ID of the Product Option
    try {
      Count result = apiInstance.productsIdOptionsOptionIdValuesCountJsonGet(login, authtoken, id, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionValuesApi#productsIdOptionsOptionIdValuesCountJsonGet");
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
| **optionId** | **Integer**| ID of the Product Option | |

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

<a id="productsIdOptionsOptionIdValuesJsonGet"></a>
# **productsIdOptionsOptionIdValuesJsonGet**
> List&lt;ProductOptionValue&gt; productsIdOptionsOptionIdValuesJsonGet(login, authtoken, id, optionId)

Retrieve all Product Option Values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionValuesApi apiInstance = new ProductOptionValuesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    Integer optionId = 56; // Integer | ID of the Product Option
    try {
      List<ProductOptionValue> result = apiInstance.productsIdOptionsOptionIdValuesJsonGet(login, authtoken, id, optionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionValuesApi#productsIdOptionsOptionIdValuesJsonGet");
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
| **optionId** | **Integer**| ID of the Product Option | |

### Return type

[**List&lt;ProductOptionValue&gt;**](ProductOptionValue.md)

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

<a id="productsIdOptionsOptionIdValuesJsonPost"></a>
# **productsIdOptionsOptionIdValuesJsonPost**
> ProductOptionValue productsIdOptionsOptionIdValuesJsonPost(login, authtoken, id, optionId, productOptionValueEdit)

Create a new Product Option Value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionValuesApi apiInstance = new ProductOptionValuesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer optionId = 56; // Integer | Id of the Product Option
    ProductOptionValueEdit productOptionValueEdit = new ProductOptionValueEdit(); // ProductOptionValueEdit | Product Option Value parameters.
    try {
      ProductOptionValue result = apiInstance.productsIdOptionsOptionIdValuesJsonPost(login, authtoken, id, optionId, productOptionValueEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionValuesApi#productsIdOptionsOptionIdValuesJsonPost");
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
| **productOptionValueEdit** | [**ProductOptionValueEdit**](ProductOptionValueEdit.md)| Product Option Value parameters. | |

### Return type

[**ProductOptionValue**](ProductOptionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productsIdOptionsOptionIdValuesValueIdJsonDelete"></a>
# **productsIdOptionsOptionIdValuesValueIdJsonDelete**
> String productsIdOptionsOptionIdValuesValueIdJsonDelete(login, authtoken, id, optionId, valueId)

Delete a Product Option Value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionValuesApi apiInstance = new ProductOptionValuesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer optionId = 56; // Integer | Id of the Product Option
    Integer valueId = 56; // Integer | ID of the Product Option Value
    try {
      String result = apiInstance.productsIdOptionsOptionIdValuesValueIdJsonDelete(login, authtoken, id, optionId, valueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionValuesApi#productsIdOptionsOptionIdValuesValueIdJsonDelete");
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
| **valueId** | **Integer**| ID of the Product Option Value | |

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

<a id="productsIdOptionsOptionIdValuesValueIdJsonGet"></a>
# **productsIdOptionsOptionIdValuesValueIdJsonGet**
> ProductOptionValue productsIdOptionsOptionIdValuesValueIdJsonGet(login, authtoken, id, optionId, valueId)

Retrieve a single Product Option Value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionValuesApi apiInstance = new ProductOptionValuesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer optionId = 56; // Integer | Id of the Product Option
    Integer valueId = 56; // Integer | ID of the Product Option Value
    try {
      ProductOptionValue result = apiInstance.productsIdOptionsOptionIdValuesValueIdJsonGet(login, authtoken, id, optionId, valueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionValuesApi#productsIdOptionsOptionIdValuesValueIdJsonGet");
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
| **valueId** | **Integer**| ID of the Product Option Value | |

### Return type

[**ProductOptionValue**](ProductOptionValue.md)

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

<a id="productsIdOptionsOptionIdValuesValueIdJsonPut"></a>
# **productsIdOptionsOptionIdValuesValueIdJsonPut**
> ProductOptionValue productsIdOptionsOptionIdValuesValueIdJsonPut(login, authtoken, id, optionId, valueId, productOptionValueEdit)

Modify an existing Product Option Value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOptionValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductOptionValuesApi apiInstance = new ProductOptionValuesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer optionId = 56; // Integer | Id of the Product Option
    Integer valueId = 56; // Integer | Id of the Product Option Value
    ProductOptionValueEdit productOptionValueEdit = new ProductOptionValueEdit(); // ProductOptionValueEdit | Product option value parameters to change
    try {
      ProductOptionValue result = apiInstance.productsIdOptionsOptionIdValuesValueIdJsonPut(login, authtoken, id, optionId, valueId, productOptionValueEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOptionValuesApi#productsIdOptionsOptionIdValuesValueIdJsonPut");
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
| **valueId** | **Integer**| Id of the Product Option Value | |
| **productOptionValueEdit** | [**ProductOptionValueEdit**](ProductOptionValueEdit.md)| Product option value parameters to change | |

### Return type

[**ProductOptionValue**](ProductOptionValue.md)

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

