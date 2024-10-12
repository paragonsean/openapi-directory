# CreditApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCredit**](CreditApi.md#getCredit) | **GET** /credit | Interrogation credit |


<a id="getCredit"></a>
# **getCredit**
> CreditResponse getCredit(keyid, credit)

Interrogation credit

Retourne le credit existant associe au compte. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    CreditApi apiInstance = new CreditApi(defaultClient);
    String keyid = "keyid_example"; // String | Clé API
    String credit = "1"; // String | Type de reponse demandée, 1 pour euro, 2 pour euro + estimation quantité
    try {
      CreditResponse result = apiInstance.getCredit(keyid, credit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditApi#getCredit");
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
| **keyid** | **String**| Clé API | |
| **credit** | **String**| Type de reponse demandée, 1 pour euro, 2 pour euro + estimation quantité | [enum: 1, 2] |

### Return type

[**CreditResponse**](CreditResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Erreur |  -  |

