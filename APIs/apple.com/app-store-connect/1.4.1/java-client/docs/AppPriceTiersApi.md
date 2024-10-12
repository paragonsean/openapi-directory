# AppPriceTiersApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appPriceTiersGetCollection**](AppPriceTiersApi.md#appPriceTiersGetCollection) | **GET** /v1/appPriceTiers |  |
| [**appPriceTiersGetInstance**](AppPriceTiersApi.md#appPriceTiersGetInstance) | **GET** /v1/appPriceTiers/{id} |  |
| [**appPriceTiersPricePointsGetToManyRelated**](AppPriceTiersApi.md#appPriceTiersPricePointsGetToManyRelated) | **GET** /v1/appPriceTiers/{id}/pricePoints |  |


<a id="appPriceTiersGetCollection"></a>
# **appPriceTiersGetCollection**
> AppPriceTiersResponse appPriceTiersGetCollection(filterId, fieldsAppPriceTiers, limit, include, fieldsAppPricePoints, limitPricePoints)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPriceTiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPriceTiersApi apiInstance = new AppPriceTiersApi(defaultClient);
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> fieldsAppPriceTiers = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPriceTiers
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppPricePoints = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPricePoints
    Integer limitPricePoints = 56; // Integer | maximum number of related pricePoints returned (when they are included)
    try {
      AppPriceTiersResponse result = apiInstance.appPriceTiersGetCollection(filterId, fieldsAppPriceTiers, limit, include, fieldsAppPricePoints, limitPricePoints);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPriceTiersApi#appPriceTiersGetCollection");
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
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **fieldsAppPriceTiers** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPriceTiers | [optional] [enum: pricePoints] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: pricePoints] |
| **fieldsAppPricePoints** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] [enum: customerPrice, priceTier, proceeds, territory] |
| **limitPricePoints** | **Integer**| maximum number of related pricePoints returned (when they are included) | [optional] |

### Return type

[**AppPriceTiersResponse**](AppPriceTiersResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of AppPriceTiers |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="appPriceTiersGetInstance"></a>
# **appPriceTiersGetInstance**
> AppPriceTierResponse appPriceTiersGetInstance(id, fieldsAppPriceTiers, include, fieldsAppPricePoints, limitPricePoints)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPriceTiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPriceTiersApi apiInstance = new AppPriceTiersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppPriceTiers = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPriceTiers
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppPricePoints = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPricePoints
    Integer limitPricePoints = 56; // Integer | maximum number of related pricePoints returned (when they are included)
    try {
      AppPriceTierResponse result = apiInstance.appPriceTiersGetInstance(id, fieldsAppPriceTiers, include, fieldsAppPricePoints, limitPricePoints);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPriceTiersApi#appPriceTiersGetInstance");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsAppPriceTiers** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPriceTiers | [optional] [enum: pricePoints] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: pricePoints] |
| **fieldsAppPricePoints** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] [enum: customerPrice, priceTier, proceeds, territory] |
| **limitPricePoints** | **Integer**| maximum number of related pricePoints returned (when they are included) | [optional] |

### Return type

[**AppPriceTierResponse**](AppPriceTierResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppPriceTier |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appPriceTiersPricePointsGetToManyRelated"></a>
# **appPriceTiersPricePointsGetToManyRelated**
> AppPricePointsResponse appPriceTiersPricePointsGetToManyRelated(id, fieldsAppPricePoints, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPriceTiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPriceTiersApi apiInstance = new AppPriceTiersApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppPricePoints = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPricePoints
    Integer limit = 56; // Integer | maximum resources per page
    try {
      AppPricePointsResponse result = apiInstance.appPriceTiersPricePointsGetToManyRelated(id, fieldsAppPricePoints, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPriceTiersApi#appPriceTiersPricePointsGetToManyRelated");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsAppPricePoints** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] [enum: customerPrice, priceTier, proceeds, territory] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**AppPricePointsResponse**](AppPricePointsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

