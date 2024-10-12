# ProductModuleApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProductModule**](ProductModuleApi.md#createProductModule) | **POST** /productmodule | Create Product Module |
| [**deleteProductModule**](ProductModuleApi.md#deleteProductModule) | **DELETE** /productmodule/{productModuleNumber} | Delete Product Module |
| [**getProductModule**](ProductModuleApi.md#getProductModule) | **GET** /productmodule/{productModuleNumber} | Get Product Module |
| [**listProductModules**](ProductModuleApi.md#listProductModules) | **GET** /productmodule | List Product Modules |
| [**updateProductModule**](ProductModuleApi.md#updateProductModule) | **POST** /productmodule/{productModuleNumber} | Update Product Module |


<a id="createProductModule"></a>
# **createProductModule**
> Netlicensing createProductModule(active, licensingModel, name, productNumber, licenseTemplate, maxCheckoutValidity, nodeSecretMode, number, redThreshold, yellowThreshold)

Create Product Module

Creates a new Product Module

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductModuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductModuleApi apiInstance = new ProductModuleApi(defaultClient);
    Boolean active = true; // Boolean | If set to 'false', the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module.
    String licensingModel = "licensingModel_example"; // String | Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation.
    String name = "name_example"; // String | Product Module name that is visible to the end customers in NetLicensing Shop.
    String productNumber = "productNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    List<String> licenseTemplate = Arrays.asList("TIMEVOLUME"); // List<String> | License Template. Mandatory for 'Try &amp; Buy' licensing model.
    Integer maxCheckoutValidity = 56; // Integer | Maximum checkout validity (days). Mandatory for 'Floating' licensing model.
    List<String> nodeSecretMode = Arrays.asList("PREDEFINED"); // List<String> | Secret Mode. Mandatory for 'Node-Locked' licensing model.
    String number = "number_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    Integer redThreshold = 56; // Integer | Remaining time volume for red level. Mandatory for 'Rental' licensing model.
    Integer yellowThreshold = 56; // Integer | Remaining time volume for yellow level. Mandatory for 'Rental' licensing model.
    try {
      Netlicensing result = apiInstance.createProductModule(active, licensingModel, name, productNumber, licenseTemplate, maxCheckoutValidity, nodeSecretMode, number, redThreshold, yellowThreshold);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductModuleApi#createProductModule");
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
| **active** | **Boolean**| If set to &#39;false&#39;, the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module. | |
| **licensingModel** | **String**| Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation. | |
| **name** | **String**| Product Module name that is visible to the end customers in NetLicensing Shop. | |
| **productNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | |
| **licenseTemplate** | [**List&lt;String&gt;**](String.md)| License Template. Mandatory for &#39;Try &amp;amp; Buy&#39; licensing model. | [optional] [enum: TIMEVOLUME, FEATURE] |
| **maxCheckoutValidity** | **Integer**| Maximum checkout validity (days). Mandatory for &#39;Floating&#39; licensing model. | [optional] |
| **nodeSecretMode** | [**List&lt;String&gt;**](String.md)| Secret Mode. Mandatory for &#39;Node-Locked&#39; licensing model. | [optional] [enum: PREDEFINED, CLIENT] |
| **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | [optional] |
| **redThreshold** | **Integer**| Remaining time volume for red level. Mandatory for &#39;Rental&#39; licensing model. | [optional] |
| **yellowThreshold** | **Integer**| Remaining time volume for yellow level. Mandatory for &#39;Rental&#39; licensing model. | [optional] |

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

<a id="deleteProductModule"></a>
# **deleteProductModule**
> Netlicensing deleteProductModule(productModuleNumber, forceCascade)

Delete Product Module

Delete a Product Module by &#39;number&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductModuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductModuleApi apiInstance = new ProductModuleApi(defaultClient);
    String productModuleNumber = "productModuleNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module.
    Boolean forceCascade = true; // Boolean | Force object deletion and all descendants.
    try {
      Netlicensing result = apiInstance.deleteProductModule(productModuleNumber, forceCascade);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductModuleApi#deleteProductModule");
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
| **productModuleNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. | |
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

<a id="getProductModule"></a>
# **getProductModule**
> Netlicensing getProductModule(productModuleNumber)

Get Product Module

Return a Product Module by &#39;productModuleNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductModuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductModuleApi apiInstance = new ProductModuleApi(defaultClient);
    String productModuleNumber = "productModuleNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    try {
      Netlicensing result = apiInstance.getProductModule(productModuleNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductModuleApi#getProductModule");
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
| **productModuleNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | |

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

<a id="listProductModules"></a>
# **listProductModules**
> List&lt;Netlicensing&gt; listProductModules()

List Product Modules

Return a list of all Product Modules for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductModuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductModuleApi apiInstance = new ProductModuleApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listProductModules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductModuleApi#listProductModules");
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

<a id="updateProductModule"></a>
# **updateProductModule**
> Netlicensing updateProductModule(productModuleNumber, active, licenseTemplate, licensingModel, maxCheckoutValidity, name, nodeSecretMode, number, redThreshold, yellowThreshold)

Update Product Module

Sets the provided properties to a Product Module. Return an updated Product Module

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductModuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProductModuleApi apiInstance = new ProductModuleApi(defaultClient);
    String productModuleNumber = "productModuleNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    Boolean active = true; // Boolean | If set to 'false', the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module.
    List<String> licenseTemplate = Arrays.asList("TIMEVOLUME"); // List<String> | License Template. Mandatory for 'Try &amp; Buy' licensing model.
    String licensingModel = "licensingModel_example"; // String | Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation.
    Integer maxCheckoutValidity = 56; // Integer | Maximum checkout validity (days). Mandatory for 'Floating' licensing model.
    String name = "name_example"; // String | Product Module name that is visible to the end customers in NetLicensing Shop.
    List<String> nodeSecretMode = Arrays.asList("PREDEFINED"); // List<String> | Secret Mode. Mandatory for 'Node-Locked' licensing model.
    String number = "number_example"; // String | New Product Module number (update).
    Integer redThreshold = 56; // Integer | Remaining time volume for red level. Mandatory for 'Rental' licensing model.
    Integer yellowThreshold = 56; // Integer | Remaining time volume for yellow level. Mandatory for 'Rental' licensing model.
    try {
      Netlicensing result = apiInstance.updateProductModule(productModuleNumber, active, licenseTemplate, licensingModel, maxCheckoutValidity, name, nodeSecretMode, number, redThreshold, yellowThreshold);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductModuleApi#updateProductModule");
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
| **productModuleNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | |
| **active** | **Boolean**| If set to &#39;false&#39;, the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module. | [optional] |
| **licenseTemplate** | [**List&lt;String&gt;**](String.md)| License Template. Mandatory for &#39;Try &amp;amp; Buy&#39; licensing model. | [optional] [enum: TIMEVOLUME, FEATURE] |
| **licensingModel** | **String**| Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation. | [optional] |
| **maxCheckoutValidity** | **Integer**| Maximum checkout validity (days). Mandatory for &#39;Floating&#39; licensing model. | [optional] |
| **name** | **String**| Product Module name that is visible to the end customers in NetLicensing Shop. | [optional] |
| **nodeSecretMode** | [**List&lt;String&gt;**](String.md)| Secret Mode. Mandatory for &#39;Node-Locked&#39; licensing model. | [optional] [enum: PREDEFINED, CLIENT] |
| **number** | **String**| New Product Module number (update). | [optional] |
| **redThreshold** | **Integer**| Remaining time volume for red level. Mandatory for &#39;Rental&#39; licensing model. | [optional] |
| **yellowThreshold** | **Integer**| Remaining time volume for yellow level. Mandatory for &#39;Rental&#39; licensing model. | [optional] |

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

