# MaterialRentalsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**materialsMaterialIdRentalsCheckoutPost**](MaterialRentalsApi.md#materialsMaterialIdRentalsCheckoutPost) | **POST** /materials/{material_id}/rentals/checkout/ | Checkout material rental |
| [**materialsMaterialIdRentalsGet**](MaterialRentalsApi.md#materialsMaterialIdRentalsGet) | **GET** /materials/{material_id}/rentals/ | Show list of rentals for specific material |
| [**materialsMaterialIdRentalsMaterialRentalIdDelete**](MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdDelete) | **DELETE** /materials/{material_id}/rentals/{material_rental_id}/ | Delete material rental |
| [**materialsMaterialIdRentalsMaterialRentalIdGet**](MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdGet) | **GET** /materials/{material_id}/rentals/{material_rental_id}/ | Show rental foor materi |
| [**materialsMaterialIdRentalsMaterialRentalIdPut**](MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdPut) | **PUT** /materials/{material_id}/rentals/{material_rental_id}/ | Edit material rental |
| [**materialsMaterialIdRentalsPost**](MaterialRentalsApi.md#materialsMaterialIdRentalsPost) | **POST** /materials/{material_id}/rentals/ | Add material rental |


<a id="materialsMaterialIdRentalsCheckoutPost"></a>
# **materialsMaterialIdRentalsCheckoutPost**
> ClockingRecordsPost201Response materialsMaterialIdRentalsCheckoutPost(materialId, materialsMaterialIdRentalsCheckoutPostRequest)

Checkout material rental

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialRentalsApi apiInstance = new MaterialRentalsApi(defaultClient);
    String materialId = "materialId_example"; // String | 
    MaterialsMaterialIdRentalsCheckoutPostRequest materialsMaterialIdRentalsCheckoutPostRequest = new MaterialsMaterialIdRentalsCheckoutPostRequest(); // MaterialsMaterialIdRentalsCheckoutPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.materialsMaterialIdRentalsCheckoutPost(materialId, materialsMaterialIdRentalsCheckoutPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialRentalsApi#materialsMaterialIdRentalsCheckoutPost");
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
| **materialId** | **String**|  | |
| **materialsMaterialIdRentalsCheckoutPostRequest** | [**MaterialsMaterialIdRentalsCheckoutPostRequest**](MaterialsMaterialIdRentalsCheckoutPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

<a id="materialsMaterialIdRentalsGet"></a>
# **materialsMaterialIdRentalsGet**
> MaterialsMaterialIdRentalsGet200Response materialsMaterialIdRentalsGet(materialId)

Show list of rentals for specific material

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialRentalsApi apiInstance = new MaterialRentalsApi(defaultClient);
    String materialId = "materialId_example"; // String | 
    try {
      MaterialsMaterialIdRentalsGet200Response result = apiInstance.materialsMaterialIdRentalsGet(materialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialRentalsApi#materialsMaterialIdRentalsGet");
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
| **materialId** | **String**|  | |

### Return type

[**MaterialsMaterialIdRentalsGet200Response**](MaterialsMaterialIdRentalsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="materialsMaterialIdRentalsMaterialRentalIdDelete"></a>
# **materialsMaterialIdRentalsMaterialRentalIdDelete**
> ExpenseFilesExpenseFileIdPut200Response materialsMaterialIdRentalsMaterialRentalIdDelete(materialId, materialRentalId)

Delete material rental

Delete rental for material

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialRentalsApi apiInstance = new MaterialRentalsApi(defaultClient);
    UUID materialId = UUID.randomUUID(); // UUID | 
    UUID materialRentalId = UUID.randomUUID(); // UUID | 
    try {
      ExpenseFilesExpenseFileIdPut200Response result = apiInstance.materialsMaterialIdRentalsMaterialRentalIdDelete(materialId, materialRentalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialRentalsApi#materialsMaterialIdRentalsMaterialRentalIdDelete");
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
| **materialId** | **UUID**|  | |
| **materialRentalId** | **UUID**|  | |

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="materialsMaterialIdRentalsMaterialRentalIdGet"></a>
# **materialsMaterialIdRentalsMaterialRentalIdGet**
> MaterialsMaterialIdRentalsMaterialRentalIdGet200Response materialsMaterialIdRentalsMaterialRentalIdGet(materialId, materialRentalId)

Show rental foor materi

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialRentalsApi apiInstance = new MaterialRentalsApi(defaultClient);
    String materialId = "materialId_example"; // String | 
    String materialRentalId = "materialRentalId_example"; // String | 
    try {
      MaterialsMaterialIdRentalsMaterialRentalIdGet200Response result = apiInstance.materialsMaterialIdRentalsMaterialRentalIdGet(materialId, materialRentalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialRentalsApi#materialsMaterialIdRentalsMaterialRentalIdGet");
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
| **materialId** | **String**|  | |
| **materialRentalId** | **String**|  | |

### Return type

[**MaterialsMaterialIdRentalsMaterialRentalIdGet200Response**](MaterialsMaterialIdRentalsMaterialRentalIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="materialsMaterialIdRentalsMaterialRentalIdPut"></a>
# **materialsMaterialIdRentalsMaterialRentalIdPut**
> ExpenseFilesExpenseFileIdPut200Response materialsMaterialIdRentalsMaterialRentalIdPut(materialId, materialRentalId)

Edit material rental

Edit material rental

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialRentalsApi apiInstance = new MaterialRentalsApi(defaultClient);
    UUID materialId = UUID.randomUUID(); // UUID | 
    UUID materialRentalId = UUID.randomUUID(); // UUID | 
    try {
      ExpenseFilesExpenseFileIdPut200Response result = apiInstance.materialsMaterialIdRentalsMaterialRentalIdPut(materialId, materialRentalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialRentalsApi#materialsMaterialIdRentalsMaterialRentalIdPut");
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
| **materialId** | **UUID**|  | |
| **materialRentalId** | **UUID**|  | |

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="materialsMaterialIdRentalsPost"></a>
# **materialsMaterialIdRentalsPost**
> ClockingRecordsPost201Response materialsMaterialIdRentalsPost(materialId, materialsMaterialIdRentalsPostRequest)

Add material rental

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialRentalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MaterialRentalsApi apiInstance = new MaterialRentalsApi(defaultClient);
    String materialId = "materialId_example"; // String | 
    MaterialsMaterialIdRentalsPostRequest materialsMaterialIdRentalsPostRequest = new MaterialsMaterialIdRentalsPostRequest(); // MaterialsMaterialIdRentalsPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.materialsMaterialIdRentalsPost(materialId, materialsMaterialIdRentalsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialRentalsApi#materialsMaterialIdRentalsPost");
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
| **materialId** | **String**|  | |
| **materialsMaterialIdRentalsPostRequest** | [**MaterialsMaterialIdRentalsPostRequest**](MaterialsMaterialIdRentalsPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

