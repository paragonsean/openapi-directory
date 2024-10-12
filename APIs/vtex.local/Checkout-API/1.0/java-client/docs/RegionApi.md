# RegionApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSellersByRegion**](RegionApi.md#getSellersByRegion) | **GET** /api/checkout/pub/regions/{regionId} | Get sellers by region or address |


<a id="getSellersByRegion"></a>
# **getSellersByRegion**
> GetSellersByRegion200Response getSellersByRegion(contentType, accept, regionId, country, postalCode, geoCoordinates)

Get sellers by region or address

Retrieve a list of sellers that cater to a specific region or address, according to your set up of our [regionalization feature](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc#). Learn more about [Region v2](https://developers.vtex.com/vtex-developer-docs/changelog/region-v2).    To access the list of sellers, you must choose one of the following methods:    1. Send the identification of the list of sellers (&#x60;regionId&#x60;) as a path parameter through the URL. Or;  2. Send the &#x60;country&#x60; (3-digit ISO code) and at least one of the two values (&#x60;postal Code&#x60; or &#x60;geo Coordinates&#x60;) as query parameters through the URL. For this method, it is also allowed to send both values (&#x60;postalCode&#x60; or &#x60;geoCoordinates&#x60;) in the same request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    RegionApi apiInstance = new RegionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String regionId = "v2.1BB18CE648B5111D0933734ED83EC783"; // String | ID of the region corresponding to the shopper's location.
    String country = "BRA"; // String | Three letter country code refering to the `postalCode` field.
    String postalCode = "1234000"; // String | Postal code corresponding to the shopper's location.
    List<BigDecimal> geoCoordinates = Arrays.asList(); // List<BigDecimal> | Geocoordinates (first longitude, semicolon, then latitude) corresponding to the shopper's location.
    try {
      GetSellersByRegion200Response result = apiInstance.getSellersByRegion(contentType, accept, regionId, country, postalCode, geoCoordinates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionApi#getSellersByRegion");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **regionId** | **String**| ID of the region corresponding to the shopper&#39;s location. | |
| **country** | **String**| Three letter country code refering to the &#x60;postalCode&#x60; field. | [default to BRA] |
| **postalCode** | **String**| Postal code corresponding to the shopper&#39;s location. | [optional] [default to 1234000] |
| **geoCoordinates** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Geocoordinates (first longitude, semicolon, then latitude) corresponding to the shopper&#39;s location. | [optional] |

### Return type

[**GetSellersByRegion200Response**](GetSellersByRegion200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

