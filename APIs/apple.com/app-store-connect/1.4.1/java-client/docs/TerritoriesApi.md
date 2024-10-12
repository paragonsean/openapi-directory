# TerritoriesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**territoriesGetCollection**](TerritoriesApi.md#territoriesGetCollection) | **GET** /v1/territories |  |


<a id="territoriesGetCollection"></a>
# **territoriesGetCollection**
> TerritoriesResponse territoriesGetCollection(fieldsTerritories, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerritoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    TerritoriesApi apiInstance = new TerritoriesApi(defaultClient);
    List<String> fieldsTerritories = Arrays.asList(); // List<String> | the fields to include for returned resources of type territories
    Integer limit = 56; // Integer | maximum resources per page
    try {
      TerritoriesResponse result = apiInstance.territoriesGetCollection(fieldsTerritories, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerritoriesApi#territoriesGetCollection");
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
| **fieldsTerritories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type territories | [optional] [enum: currency] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**TerritoriesResponse**](TerritoriesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Territories |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

