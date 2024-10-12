# VinDecoderApiApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**decode**](VinDecoderApiApi.md#decode) | **GET** /decode/car/{vin}/specs | VIN Decoder |
| [**decodeViaEPI**](VinDecoderApiApi.md#decodeViaEPI) | **GET** /decode/car/epi/{vin}/specs | EPI VIN Decoder |
| [**decodeViaNeoVIN**](VinDecoderApiApi.md#decodeViaNeoVIN) | **GET** /decode/car/neovin/{vin}/specs | NeoVIN Decoder |
| [**getTaxonomyTerms**](VinDecoderApiApi.md#getTaxonomyTerms) | **GET** /specs/car/terms | API for getting terms from taxonomy |
| [**specsCarAutoCompleteGet**](VinDecoderApiApi.md#specsCarAutoCompleteGet) | **GET** /specs/car/auto-complete | API for auto-completion of inputs based on taxonomy |


<a id="decode"></a>
# **decode**
> Build decode(vin, apiKey)

VIN Decoder

Get the basic information on specifications for a car identified by a valid VIN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VinDecoderApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    VinDecoderApiApi apiInstance = new VinDecoderApiApi(defaultClient);
    String vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      Build result = apiInstance.decode(vin, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VinDecoderApiApi#decode");
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
| **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**Build**](Build.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Basic sepcifications details about the car |  -  |
| **0** | Error |  -  |

<a id="decodeViaEPI"></a>
# **decodeViaEPI**
> Build decodeViaEPI(vin, apiKey)

EPI VIN Decoder

Get the basic information on specifications for a car identified by a valid VIN from EPI&#39;s decoder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VinDecoderApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    VinDecoderApiApi apiInstance = new VinDecoderApiApi(defaultClient);
    String vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      Build result = apiInstance.decodeViaEPI(vin, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VinDecoderApiApi#decodeViaEPI");
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
| **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**Build**](Build.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Basic sepcifications details about the car |  -  |
| **0** | Error |  -  |

<a id="decodeViaNeoVIN"></a>
# **decodeViaNeoVIN**
> NeoVIN decodeViaNeoVIN(vin, apiKey, includeGeneric, forceDecode)

NeoVIN Decoder

Get the basic information on specifications for a car identified by a valid VIN from NeoVIN decoder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VinDecoderApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    VinDecoderApiApi apiInstance = new VinDecoderApiApi(defaultClient);
    String vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean includeGeneric = false; // Boolean | Boolean variable to indicate wheather to include generic data as well in response
    Boolean forceDecode = false; // Boolean | Decode VIN on the fly instead of cached response
    try {
      NeoVIN result = apiInstance.decodeViaNeoVIN(vin, apiKey, includeGeneric, forceDecode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VinDecoderApiApi#decodeViaNeoVIN");
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
| **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **includeGeneric** | **Boolean**| Boolean variable to indicate wheather to include generic data as well in response | [optional] [default to false] |
| **forceDecode** | **Boolean**| Decode VIN on the fly instead of cached response | [optional] [default to false] |

### Return type

[**NeoVIN**](NeoVIN.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Basic sepcifications details about the car |  -  |
| **0** | Error |  -  |

<a id="getTaxonomyTerms"></a>
# **getTaxonomyTerms**
> SpecsAutoCompleteResponse getTaxonomyTerms(field, apiKey, year, make, model, trim, bodyType, bodySubtype, vehicleType, transmission, drivetrain, fuelType, engine, engineSize, engineBlock)

API for getting terms from taxonomy

Facets on taxonomy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VinDecoderApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    VinDecoderApiApi apiInstance = new VinDecoderApiApi(defaultClient);
    String field = "field_example"; // String | Comma separated list of fields to get terms for
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    try {
      SpecsAutoCompleteResponse result = apiInstance.getTaxonomyTerms(field, apiKey, year, make, model, trim, bodyType, bodySubtype, vehicleType, transmission, drivetrain, fuelType, engine, engineSize, engineBlock);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VinDecoderApiApi#getTaxonomyTerms");
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
| **field** | **String**| Comma separated list of fields to get terms for | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |

### Return type

[**SpecsAutoCompleteResponse**](SpecsAutoCompleteResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of unique terms for specified fields |  -  |
| **0** | Error |  -  |

<a id="specsCarAutoCompleteGet"></a>
# **specsCarAutoCompleteGet**
> SpecsAutoCompleteResponse specsCarAutoCompleteGet(field, input, apiKey, year, make, model, trim, bodyType, bodySubtype, vehicleType, transmission, drivetrain, fuelType, engine, engineSize, engineBlock, ignoreCase, facetMinCount)

API for auto-completion of inputs based on taxonomy

Auto-complete the inputs of your end users, not from active set but from taxonomy (decoder database)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VinDecoderApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    VinDecoderApiApi apiInstance = new VinDecoderApiApi(defaultClient);
    String field = "make"; // String | Field name for which you want auto-completion
    String input = "input_example"; // String | Input entered so far
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    Boolean ignoreCase = true; // Boolean | Boolean variable to indicate ignore case of current input
    BigDecimal facetMinCount = new BigDecimal("1"); // BigDecimal | Provide minimum count value for facets
    try {
      SpecsAutoCompleteResponse result = apiInstance.specsCarAutoCompleteGet(field, input, apiKey, year, make, model, trim, bodyType, bodySubtype, vehicleType, transmission, drivetrain, fuelType, engine, engineSize, engineBlock, ignoreCase, facetMinCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VinDecoderApiApi#specsCarAutoCompleteGet");
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
| **field** | **String**| Field name for which you want auto-completion | [enum: make, model, trim, body_type, body_subtype, vehicle_type, transmission, drivetrain, fuel_type, engine, engine_size, engine_block] |
| **input** | **String**| Input entered so far | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **ignoreCase** | **Boolean**| Boolean variable to indicate ignore case of current input | [optional] [default to true] |
| **facetMinCount** | **BigDecimal**| Provide minimum count value for facets | [optional] [default to 1] |

### Return type

[**SpecsAutoCompleteResponse**](SpecsAutoCompleteResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unique terms available in given field for auto completion |  -  |
| **0** | Error |  -  |

