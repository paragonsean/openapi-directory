# ProductApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProduct**](ProductApi.md#createProduct) | **POST** /product | Create Product |
| [**deleteProduct**](ProductApi.md#deleteProduct) | **DELETE** /product/{productNumber} | Delete Product |
| [**listProducts**](ProductApi.md#listProducts) | **GET** /product | List Products |
| [**productNumber**](ProductApi.md#productNumber) | **GET** /product/{productNumber} | Get Product |
| [**updateProduct**](ProductApi.md#updateProduct) | **POST** /product/{productNumber} | Update Product |


<a id="createProduct"></a>
# **createProduct**
> Netlicensing createProduct(active, name, version, description, licenseeAutoCreate, licensingInfo, number, vatMode)

Create Product

Creates a new Product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductApi apiInstance = new ProductApi(defaultClient);
    Boolean active = true; // Boolean | If set to 'false', the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses.
    String name = "name_example"; // String | Product name. Together with the version identifies the Product for the end customer.
    String version = "version_example"; // String | Product version. Convenience parameter, additional to the Product name.
    String description = "description_example"; // String | Product description.
    Boolean licenseeAutoCreate = true; // Boolean | If set to 'true', non-existing Licensees will be created at first validation attempt.
    String licensingInfo = "licensingInfo_example"; // String | Licensing information.
    String number = "number_example"; // String | Unique number that identifies the Product. Vendor can assign this number when creating a Product or let NetLicensing generate one.
    String vatMode = "GROSS"; // String | Vat mode for Product. Supported types: GROSS, NET
    try {
      Netlicensing result = apiInstance.createProduct(active, name, version, description, licenseeAutoCreate, licensingInfo, number, vatMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#createProduct");
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
| **active** | **Boolean**| If set to &#39;false&#39;, the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses. | |
| **name** | **String**| Product name. Together with the version identifies the Product for the end customer. | |
| **version** | **String**| Product version. Convenience parameter, additional to the Product name. | |
| **description** | **String**| Product description. | [optional] |
| **licenseeAutoCreate** | **Boolean**| If set to &#39;true&#39;, non-existing Licensees will be created at first validation attempt. | [optional] |
| **licensingInfo** | **String**| Licensing information. | [optional] |
| **number** | **String**| Unique number that identifies the Product. Vendor can assign this number when creating a Product or let NetLicensing generate one. | [optional] |
| **vatMode** | **String**| Vat mode for Product. Supported types: GROSS, NET | [optional] [enum: GROSS, NET] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **402** | Quota exceeded |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="deleteProduct"></a>
# **deleteProduct**
> Netlicensing deleteProduct(productNumber, forceCascade)

Delete Product

Delete a Product by &#39;number&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productNumber = "productNumber_example"; // String | Unique number that identifies the Product.
    Boolean forceCascade = true; // Boolean | Force object deletion and all descendants.
    try {
      Netlicensing result = apiInstance.deleteProduct(productNumber, forceCascade);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#deleteProduct");
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
| **productNumber** | **String**| Unique number that identifies the Product. | |
| **forceCascade** | **Boolean**| Force object deletion and all descendants. | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="listProducts"></a>
# **listProducts**
> List&lt;Netlicensing&gt; listProducts()

List Products

Return a list of all configured Products for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductApi apiInstance = new ProductApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listProducts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#listProducts");
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

[**List&lt;Netlicensing&gt;**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="productNumber"></a>
# **productNumber**
> Netlicensing productNumber(productNumber)

Get Product

Return a Product by &#39;productNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productNumber = "productNumber_example"; // String | Unique number that identifies the Product.
    try {
      Netlicensing result = apiInstance.productNumber(productNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productNumber");
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
| **productNumber** | **String**| Unique number that identifies the Product. | |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="updateProduct"></a>
# **updateProduct**
> Netlicensing updateProduct(productNumber, active, description, licenseeAutoCreate, licensingInfo, name, number, vatMode, version)

Update Product

Sets the provided properties to a Product. Return an updated Product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productNumber = "productNumber_example"; // String | Unique number that identifies the Product.
    Boolean active = true; // Boolean | If set to 'false', the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses.
    String description = "description_example"; // String | Product description.
    Boolean licenseeAutoCreate = true; // Boolean | If set to 'true', non-existing Licensees will be created at first validation attempt.
    String licensingInfo = "licensingInfo_example"; // String | Licensing information.
    String name = "name_example"; // String | Product name. Together with the version identifies the Product for the end customer.
    String number = "number_example"; // String | New Product number (update)
    String vatMode = "GROSS"; // String | Vat mode for Product. Supported types: GROSS, NET
    String version = "version_example"; // String | Product version. Convenience parameter, additional to the Product name.
    try {
      Netlicensing result = apiInstance.updateProduct(productNumber, active, description, licenseeAutoCreate, licensingInfo, name, number, vatMode, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#updateProduct");
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
| **productNumber** | **String**| Unique number that identifies the Product. | |
| **active** | **Boolean**| If set to &#39;false&#39;, the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses. | [optional] |
| **description** | **String**| Product description. | [optional] |
| **licenseeAutoCreate** | **Boolean**| If set to &#39;true&#39;, non-existing Licensees will be created at first validation attempt. | [optional] |
| **licensingInfo** | **String**| Licensing information. | [optional] |
| **name** | **String**| Product name. Together with the version identifies the Product for the end customer. | [optional] |
| **number** | **String**| New Product number (update) | [optional] |
| **vatMode** | **String**| Vat mode for Product. Supported types: GROSS, NET | [optional] [enum: GROSS, NET] |
| **version** | **String**| Product version. Convenience parameter, additional to the Product name. | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **402** | Quota exceeded |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

