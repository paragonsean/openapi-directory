# InAppPurchasesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**inAppPurchasesGetInstance**](InAppPurchasesApi.md#inAppPurchasesGetInstance) | **GET** /v1/inAppPurchases/{id} |  |


<a id="inAppPurchasesGetInstance"></a>
# **inAppPurchasesGetInstance**
> InAppPurchaseResponse inAppPurchasesGetInstance(id, fieldsInAppPurchases, include, limitApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InAppPurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    InAppPurchasesApi apiInstance = new InAppPurchasesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsInAppPurchases = Arrays.asList(); // List<String> | the fields to include for returned resources of type inAppPurchases
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    Integer limitApps = 56; // Integer | maximum number of related apps returned (when they are included)
    try {
      InAppPurchaseResponse result = apiInstance.inAppPurchasesGetInstance(id, fieldsInAppPurchases, include, limitApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InAppPurchasesApi#inAppPurchasesGetInstance");
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
| **fieldsInAppPurchases** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] [enum: apps, inAppPurchaseType, productId, referenceName, state] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: apps] |
| **limitApps** | **Integer**| maximum number of related apps returned (when they are included) | [optional] |

### Return type

[**InAppPurchaseResponse**](InAppPurchaseResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single InAppPurchase |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

