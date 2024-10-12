# AppPricePointsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appPricePointsGetCollection**](AppPricePointsApi.md#appPricePointsGetCollection) | **GET** /v1/appPricePoints |  |
| [**appPricePointsGetInstance**](AppPricePointsApi.md#appPricePointsGetInstance) | **GET** /v1/appPricePoints/{id} |  |
| [**appPricePointsTerritoryGetToOneRelated**](AppPricePointsApi.md#appPricePointsTerritoryGetToOneRelated) | **GET** /v1/appPricePoints/{id}/territory |  |


<a id="appPricePointsGetCollection"></a>
# **appPricePointsGetCollection**
> AppPricePointsResponse appPricePointsGetCollection(filterPriceTier, filterTerritory, fieldsAppPricePoints, limit, include, fieldsTerritories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPricePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPricePointsApi apiInstance = new AppPricePointsApi(defaultClient);
    List<String> filterPriceTier = Arrays.asList(); // List<String> | filter by id(s) of related 'priceTier'
    List<String> filterTerritory = Arrays.asList(); // List<String> | filter by id(s) of related 'territory'
    List<String> fieldsAppPricePoints = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPricePoints
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsTerritories = Arrays.asList(); // List<String> | the fields to include for returned resources of type territories
    try {
      AppPricePointsResponse result = apiInstance.appPricePointsGetCollection(filterPriceTier, filterTerritory, fieldsAppPricePoints, limit, include, fieldsTerritories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPricePointsApi#appPricePointsGetCollection");
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
| **filterPriceTier** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;priceTier&#39; | [optional] |
| **filterTerritory** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;territory&#39; | [optional] |
| **fieldsAppPricePoints** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPricePoints | [optional] [enum: customerPrice, priceTier, proceeds, territory] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: priceTier, territory] |
| **fieldsTerritories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type territories | [optional] [enum: currency] |

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
| **200** | List of AppPricePoints |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="appPricePointsGetInstance"></a>
# **appPricePointsGetInstance**
> AppPricePointResponse appPricePointsGetInstance(id, fieldsAppPricePoints, include, fieldsTerritories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPricePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPricePointsApi apiInstance = new AppPricePointsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppPricePoints = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPricePoints
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsTerritories = Arrays.asList(); // List<String> | the fields to include for returned resources of type territories
    try {
      AppPricePointResponse result = apiInstance.appPricePointsGetInstance(id, fieldsAppPricePoints, include, fieldsTerritories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPricePointsApi#appPricePointsGetInstance");
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
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: priceTier, territory] |
| **fieldsTerritories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type territories | [optional] [enum: currency] |

### Return type

[**AppPricePointResponse**](AppPricePointResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppPricePoint |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appPricePointsTerritoryGetToOneRelated"></a>
# **appPricePointsTerritoryGetToOneRelated**
> TerritoryResponse appPricePointsTerritoryGetToOneRelated(id, fieldsTerritories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPricePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppPricePointsApi apiInstance = new AppPricePointsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsTerritories = Arrays.asList(); // List<String> | the fields to include for returned resources of type territories
    try {
      TerritoryResponse result = apiInstance.appPricePointsTerritoryGetToOneRelated(id, fieldsTerritories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPricePointsApi#appPricePointsTerritoryGetToOneRelated");
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
| **fieldsTerritories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type territories | [optional] [enum: currency] |

### Return type

[**TerritoryResponse**](TerritoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

