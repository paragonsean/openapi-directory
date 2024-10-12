# AgeRatingDeclarationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ageRatingDeclarationsUpdateInstance**](AgeRatingDeclarationsApi.md#ageRatingDeclarationsUpdateInstance) | **PATCH** /v1/ageRatingDeclarations/{id} |  |


<a id="ageRatingDeclarationsUpdateInstance"></a>
# **ageRatingDeclarationsUpdateInstance**
> AgeRatingDeclarationResponse ageRatingDeclarationsUpdateInstance(id, ageRatingDeclarationUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgeRatingDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AgeRatingDeclarationsApi apiInstance = new AgeRatingDeclarationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AgeRatingDeclarationUpdateRequest ageRatingDeclarationUpdateRequest = new AgeRatingDeclarationUpdateRequest(); // AgeRatingDeclarationUpdateRequest | AgeRatingDeclaration representation
    try {
      AgeRatingDeclarationResponse result = apiInstance.ageRatingDeclarationsUpdateInstance(id, ageRatingDeclarationUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgeRatingDeclarationsApi#ageRatingDeclarationsUpdateInstance");
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
| **ageRatingDeclarationUpdateRequest** | [**AgeRatingDeclarationUpdateRequest**](AgeRatingDeclarationUpdateRequest.md)| AgeRatingDeclaration representation | |

### Return type

[**AgeRatingDeclarationResponse**](AgeRatingDeclarationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AgeRatingDeclaration |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

