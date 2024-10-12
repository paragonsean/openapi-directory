# ModelApi

All URIs are relative to */api/2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**modelGet**](ModelApi.md#modelGet) | **GET** /model | Retrieve the models you&#39;ve created.  |
| [**modelModelIdGet**](ModelApi.md#modelModelIdGet) | **GET** /model/{model_id} | Retrieve a previously created model by its id.  |
| [**modelPost**](ModelApi.md#modelPost) | **POST** /model | Models represent 3D design files that you&#39;d like to produce. Creating models is generally the first step in creating an order.  |
| [**modelQuoteAttrsGet**](ModelApi.md#modelQuoteAttrsGet) | **GET** /model/quote_attrs | Get a quote for a model with the given attributes.  |
| [**modelQuoteGet**](ModelApi.md#modelQuoteGet) | **GET** /model/quote | Get a quote a given model id.  |


<a id="modelGet"></a>
# **modelGet**
> List&lt;Model&gt; modelGet()

Retrieve the models you&#39;ve created. 

Lists all of the models you&#39;ve created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    ModelApi apiInstance = new ModelApi(defaultClient);
    try {
      List<Model> result = apiInstance.modelGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#modelGet");
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

[**List&lt;Model&gt;**](Model.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of models |  -  |

<a id="modelModelIdGet"></a>
# **modelModelIdGet**
> Model modelModelIdGet(modelId)

Retrieve a previously created model by its id. 

In cases where you&#39;re ordering models you&#39;ve created previously, you can fetch a specific model by its id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    ModelApi apiInstance = new ModelApi(defaultClient);
    Integer modelId = 56; // Integer | 
    try {
      Model result = apiInstance.modelModelIdGet(modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#modelModelIdGet");
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
| **modelId** | **Integer**|  | |

### Return type

[**Model**](Model.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Model object |  -  |

<a id="modelPost"></a>
# **modelPost**
> Model modelPost(body)

Models represent 3D design files that you&#39;d like to produce. Creating models is generally the first step in creating an order. 

Downloads the model data from the URL specified by file_url and saves it as a model. As a part of the model upload process, the file is run through a program that repairs the mesh (closing holes, flipping inverted normals, etc). In some cases, this may alter the geometry of your model. If you&#39;re noticing bad results for your created models, you might consider repairing your files before submitting them. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    ModelApi apiInstance = new ModelApi(defaultClient);
    CreateModelBody body = new CreateModelBody(); // CreateModelBody | 
    try {
      Model result = apiInstance.modelPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#modelPost");
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
| **body** | [**CreateModelBody**](CreateModelBody.md)|  | |

### Return type

[**Model**](Model.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Model object |  -  |

<a id="modelQuoteAttrsGet"></a>
# **modelQuoteAttrsGet**
> ModelQuote modelQuoteAttrsGet(x, y, z, volume, surfaceArea, materialId, quantity, units, optionsOrientation)

Get a quote for a model with the given attributes. 

This endpoint will provide a quote for a model matching the submitted parameters. Note that this quote may be different than the quote provided by /model/quote in the case that your attribute calculations differ from the ones used by Voodoo Manufacturing. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    ModelApi apiInstance = new ModelApi(defaultClient);
    BigDecimal x = new BigDecimal(78); // BigDecimal | The calculated unitless x dimension of this model's bounding box.
    BigDecimal y = new BigDecimal(78); // BigDecimal | The calculated unitless y dimension of this model's bounding box.
    BigDecimal z = new BigDecimal(78); // BigDecimal | The calculated unitless z dimension of this model's bounding box.
    BigDecimal volume = new BigDecimal(78); // BigDecimal | The calculated unitless volume of the model.
    BigDecimal surfaceArea = new BigDecimal(78); // BigDecimal | The calculated unitless surface area of the model.
    BigDecimal materialId = new BigDecimal(78); // BigDecimal | The unique id of the desired material.
    BigDecimal quantity = new BigDecimal(78); // BigDecimal | The number of units in this quote.
    String units = "units_example"; // String | The units of the model file. Either \"mm\", \"cm\", or \"in\". The correct value to pass here depends on which design program you're using. Defaults to \"mm\".
    Boolean optionsOrientation = true; // Boolean | Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you're not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.
    try {
      ModelQuote result = apiInstance.modelQuoteAttrsGet(x, y, z, volume, surfaceArea, materialId, quantity, units, optionsOrientation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#modelQuoteAttrsGet");
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
| **x** | **BigDecimal**| The calculated unitless x dimension of this model&#39;s bounding box. | |
| **y** | **BigDecimal**| The calculated unitless y dimension of this model&#39;s bounding box. | |
| **z** | **BigDecimal**| The calculated unitless z dimension of this model&#39;s bounding box. | |
| **volume** | **BigDecimal**| The calculated unitless volume of the model. | |
| **surfaceArea** | **BigDecimal**| The calculated unitless surface area of the model. | |
| **materialId** | **BigDecimal**| The unique id of the desired material. | |
| **quantity** | **BigDecimal**| The number of units in this quote. | |
| **units** | **String**| The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;. | |
| **optionsOrientation** | **Boolean**| Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you&#39;re not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation. | [optional] |

### Return type

[**ModelQuote**](ModelQuote.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quote for model with attributes |  -  |

<a id="modelQuoteGet"></a>
# **modelQuoteGet**
> ModelQuote modelQuoteGet(modelId, materialId, quantity, units, optionsOrientation)

Get a quote a given model id. 

Calculates a quote for the given model in the given material and quantity. This endpoint required that you&#39;ve already uploaded the model to our servers -- to get a quote for a model you haven&#39;t yet uploaded, you can try /model/quote_attrs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    ModelApi apiInstance = new ModelApi(defaultClient);
    Integer modelId = 56; // Integer | The unique id of the model you'd like to quote.
    BigDecimal materialId = new BigDecimal(78); // BigDecimal | The unique id of the desired material.
    BigDecimal quantity = new BigDecimal(78); // BigDecimal | The number of units in this quote.
    String units = "units_example"; // String | The units of the model file. Either \"mm\", \"cm\", or \"in\". The correct value to pass here depends on which design program you're using. Defaults to \"mm\".
    Boolean optionsOrientation = true; // Boolean | Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you're not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.
    try {
      ModelQuote result = apiInstance.modelQuoteGet(modelId, materialId, quantity, units, optionsOrientation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#modelQuoteGet");
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
| **modelId** | **Integer**| The unique id of the model you&#39;d like to quote. | |
| **materialId** | **BigDecimal**| The unique id of the desired material. | |
| **quantity** | **BigDecimal**| The number of units in this quote. | |
| **units** | **String**| The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;. | |
| **optionsOrientation** | **Boolean**| Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you&#39;re not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation. | [optional] |

### Return type

[**ModelQuote**](ModelQuote.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quote for model with attributes |  -  |

