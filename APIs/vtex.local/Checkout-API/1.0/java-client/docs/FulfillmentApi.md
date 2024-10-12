# FulfillmentApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAddressByPostalCode**](FulfillmentApi.md#getAddressByPostalCode) | **GET** /api/checkout/pub/postal-code/{countryCode}/{postalCode} | Get address by postal code |
| [**listPickupPpointsByLocation**](FulfillmentApi.md#listPickupPpointsByLocation) | **GET** /api/checkout/pub/pickup-points | List pickup points by location |


<a id="getAddressByPostalCode"></a>
# **getAddressByPostalCode**
> getAddressByPostalCode(contentType, accept, countryCode, postalCode)

Get address by postal code

Retrieves address information for a given postal code and country.    This request can be used to implement auto complete functionality when a customer needs to fill in an address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FulfillmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    FulfillmentApi apiInstance = new FulfillmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String countryCode = "BRA"; // String | Three letter country code refering to the `postalCode` field.
    String postalCode = "1234000"; // String | Postal code.
    try {
      apiInstance.getAddressByPostalCode(contentType, accept, countryCode, postalCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling FulfillmentApi#getAddressByPostalCode");
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
| **countryCode** | **String**| Three letter country code refering to the &#x60;postalCode&#x60; field. | [default to BRA] |
| **postalCode** | **String**| Postal code. | [default to 1234000] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listPickupPpointsByLocation"></a>
# **listPickupPpointsByLocation**
> listPickupPpointsByLocation(contentType, accept, geoCoordinates, postalCode, countryCode)

List pickup points by location

Retrieves information on pickup points close to a given location determined by geocoordinates or postal code.    The pickup points returned are not necessarily all active ones. Make sure to validate the information consumed by integrations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FulfillmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    FulfillmentApi apiInstance = new FulfillmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    List<BigDecimal> geoCoordinates = Arrays.asList(); // List<BigDecimal> | Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes.
    String postalCode = "1234000"; // String | Postal code around which to search for pickup points. If you use this type of search, make sure to pass a `countryCode` and do not pass `geoCoordinates`.
    String countryCode = "BRA"; // String | Three letter country code refering to the `postalCode` field. Pass the country code only if you are searching pickup points by postal code.
    try {
      apiInstance.listPickupPpointsByLocation(contentType, accept, geoCoordinates, postalCode, countryCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling FulfillmentApi#listPickupPpointsByLocation");
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
| **geoCoordinates** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes. | [optional] |
| **postalCode** | **String**| Postal code around which to search for pickup points. If you use this type of search, make sure to pass a &#x60;countryCode&#x60; and do not pass &#x60;geoCoordinates&#x60;. | [optional] [default to 1234000] |
| **countryCode** | **String**| Three letter country code refering to the &#x60;postalCode&#x60; field. Pass the country code only if you are searching pickup points by postal code. | [optional] [default to BRA] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

