# ProductImagesApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsIdImagesCountJsonGet**](ProductImagesApi.md#productsIdImagesCountJsonGet) | **GET** /products/{id}/images/count.json | Count all Product Images. |
| [**productsIdImagesImageIdJsonDelete**](ProductImagesApi.md#productsIdImagesImageIdJsonDelete) | **DELETE** /products/{id}/images/{image_id}.json | Delete a Product Image. |
| [**productsIdImagesImageIdJsonGet**](ProductImagesApi.md#productsIdImagesImageIdJsonGet) | **GET** /products/{id}/images/{image_id}.json | Retrieve a single Product Image. |
| [**productsIdImagesJsonGet**](ProductImagesApi.md#productsIdImagesJsonGet) | **GET** /products/{id}/images.json | Retrieve all Product Images. |
| [**productsIdImagesJsonPost**](ProductImagesApi.md#productsIdImagesJsonPost) | **POST** /products/{id}/images.json | Create a new Product Image. |


<a id="productsIdImagesCountJsonGet"></a>
# **productsIdImagesCountJsonGet**
> Count productsIdImagesCountJsonGet(login, authtoken, id)

Count all Product Images.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductImagesApi apiInstance = new ProductImagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      Count result = apiInstance.productsIdImagesCountJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductImagesApi#productsIdImagesCountJsonGet");
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

<a id="productsIdImagesImageIdJsonDelete"></a>
# **productsIdImagesImageIdJsonDelete**
> String productsIdImagesImageIdJsonDelete(login, authtoken, id, imageId)

Delete a Product Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductImagesApi apiInstance = new ProductImagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer imageId = 56; // Integer | Id of the Product Image
    try {
      String result = apiInstance.productsIdImagesImageIdJsonDelete(login, authtoken, id, imageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductImagesApi#productsIdImagesImageIdJsonDelete");
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
| **imageId** | **Integer**| Id of the Product Image | |

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

<a id="productsIdImagesImageIdJsonGet"></a>
# **productsIdImagesImageIdJsonGet**
> Image productsIdImagesImageIdJsonGet(login, authtoken, id, imageId)

Retrieve a single Product Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductImagesApi apiInstance = new ProductImagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer imageId = 56; // Integer | Id of the Product Image
    try {
      Image result = apiInstance.productsIdImagesImageIdJsonGet(login, authtoken, id, imageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductImagesApi#productsIdImagesImageIdJsonGet");
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
| **imageId** | **Integer**| Id of the Product Image | |

### Return type

[**Image**](Image.md)

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

<a id="productsIdImagesJsonGet"></a>
# **productsIdImagesJsonGet**
> List&lt;Image&gt; productsIdImagesJsonGet(login, authtoken, id)

Retrieve all Product Images.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductImagesApi apiInstance = new ProductImagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      List<Image> result = apiInstance.productsIdImagesJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductImagesApi#productsIdImagesJsonGet");
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

[**List&lt;Image&gt;**](Image.md)

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

<a id="productsIdImagesJsonPost"></a>
# **productsIdImagesJsonPost**
> Image productsIdImagesJsonPost(login, authtoken, id, imageEdit)

Create a new Product Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductImagesApi apiInstance = new ProductImagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    ImageEdit imageEdit = new ImageEdit(); // ImageEdit | Product Image parameters.
    try {
      Image result = apiInstance.productsIdImagesJsonPost(login, authtoken, id, imageEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductImagesApi#productsIdImagesJsonPost");
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
| **imageEdit** | [**ImageEdit**](ImageEdit.md)| Product Image parameters. | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

