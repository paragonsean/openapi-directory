# ProductCustomFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsIdFieldsCountJsonGet**](ProductCustomFieldsApi.md#productsIdFieldsCountJsonGet) | **GET** /products/{id}/fields/count.json | Count all Product Custom Fields. |
| [**productsIdFieldsJsonGet**](ProductCustomFieldsApi.md#productsIdFieldsJsonGet) | **GET** /products/{id}/fields.json | Retrieve all Product Custom Fields |
| [**productsIdFieldsJsonPost**](ProductCustomFieldsApi.md#productsIdFieldsJsonPost) | **POST** /products/{id}/fields.json | Add an existing Custom Field to a Product. |
| [**productsProductIdFieldsFieldIdJsonDelete**](ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonDelete) | **DELETE** /products/{product_id}/fields/{field_id}.json | Delete value of Product Custom Field |
| [**productsProductIdFieldsFieldIdJsonPut**](ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonPut) | **PUT** /products/{product_id}/fields/{field_id}.json | Update value of Product Custom Field |


<a id="productsIdFieldsCountJsonGet"></a>
# **productsIdFieldsCountJsonGet**
> Count productsIdFieldsCountJsonGet(login, authtoken, id)

Count all Product Custom Fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductCustomFieldsApi apiInstance = new ProductCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      Count result = apiInstance.productsIdFieldsCountJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductCustomFieldsApi#productsIdFieldsCountJsonGet");
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

<a id="productsIdFieldsJsonGet"></a>
# **productsIdFieldsJsonGet**
> List&lt;ProductCustomField&gt; productsIdFieldsJsonGet(login, authtoken, id)

Retrieve all Product Custom Fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductCustomFieldsApi apiInstance = new ProductCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    try {
      List<ProductCustomField> result = apiInstance.productsIdFieldsJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductCustomFieldsApi#productsIdFieldsJsonGet");
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

### Return type

[**List&lt;ProductCustomField&gt;**](ProductCustomField.md)

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

<a id="productsIdFieldsJsonPost"></a>
# **productsIdFieldsJsonPost**
> Product productsIdFieldsJsonPost(login, authtoken, id, addProductCustomField)

Add an existing Custom Field to a Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductCustomFieldsApi apiInstance = new ProductCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    AddProductCustomField addProductCustomField = new AddProductCustomField(); // AddProductCustomField | Product Custom Field parameters.
    try {
      Product result = apiInstance.productsIdFieldsJsonPost(login, authtoken, id, addProductCustomField);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductCustomFieldsApi#productsIdFieldsJsonPost");
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
| **addProductCustomField** | [**AddProductCustomField**](AddProductCustomField.md)| Product Custom Field parameters. | |

### Return type

[**Product**](Product.md)

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

<a id="productsProductIdFieldsFieldIdJsonDelete"></a>
# **productsProductIdFieldsFieldIdJsonDelete**
> MessageObject productsProductIdFieldsFieldIdJsonDelete(login, authtoken, productId, fieldId)

Delete value of Product Custom Field

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductCustomFieldsApi apiInstance = new ProductCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer productId = 56; // Integer | Id of the Product.
    Integer fieldId = 56; // Integer | Id of the Custom Field Value.
    try {
      MessageObject result = apiInstance.productsProductIdFieldsFieldIdJsonDelete(login, authtoken, productId, fieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductCustomFieldsApi#productsProductIdFieldsFieldIdJsonDelete");
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
| **productId** | **Integer**| Id of the Product. | |
| **fieldId** | **Integer**| Id of the Custom Field Value. | |

### Return type

[**MessageObject**](MessageObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product or Custom Field Value Not Found. |  -  |

<a id="productsProductIdFieldsFieldIdJsonPut"></a>
# **productsProductIdFieldsFieldIdJsonPut**
> ProductCustomField productsProductIdFieldsFieldIdJsonPut(login, authtoken, productId, fieldId)

Update value of Product Custom Field

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductCustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductCustomFieldsApi apiInstance = new ProductCustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer productId = 56; // Integer | Id of the Product.
    Integer fieldId = 56; // Integer | Id of the Custom Field Value.
    try {
      ProductCustomField result = apiInstance.productsProductIdFieldsFieldIdJsonPut(login, authtoken, productId, fieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductCustomFieldsApi#productsProductIdFieldsFieldIdJsonPut");
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
| **productId** | **Integer**| Id of the Product. | |
| **fieldId** | **Integer**| Id of the Custom Field Value. | |

### Return type

[**ProductCustomField**](ProductCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product or Custom Field Value Not Found. |  -  |

