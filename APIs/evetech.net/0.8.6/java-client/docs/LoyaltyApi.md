# LoyaltyApi

All URIs are relative to *https://esi.evetech.net/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCharactersCharacterIdLoyaltyPoints**](LoyaltyApi.md#getCharactersCharacterIdLoyaltyPoints) | **GET** /characters/{character_id}/loyalty/points/ | Get loyalty points |
| [**getLoyaltyStoresCorporationIdOffers**](LoyaltyApi.md#getLoyaltyStoresCorporationIdOffers) | **GET** /loyalty/stores/{corporation_id}/offers/ | List loyalty store offers |


<a id="getCharactersCharacterIdLoyaltyPoints"></a>
# **getCharactersCharacterIdLoyaltyPoints**
> List&lt;GetCharactersCharacterIdLoyaltyPoints200Ok&gt; getCharactersCharacterIdLoyaltyPoints(characterId, datasource, ifNoneMatch, token)

Get loyalty points

Return a list of loyalty points for all corporations the character has worked for  --- Alternate route: &#x60;/dev/characters/{character_id}/loyalty/points/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/loyalty/points/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/loyalty/points/&#x60;  --- This route is cached for up to 3600 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoyaltyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    LoyaltyApi apiInstance = new LoyaltyApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      List<GetCharactersCharacterIdLoyaltyPoints200Ok> result = apiInstance.getCharactersCharacterIdLoyaltyPoints(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoyaltyApi#getCharactersCharacterIdLoyaltyPoints");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**List&lt;GetCharactersCharacterIdLoyaltyPoints200Ok&gt;**](GetCharactersCharacterIdLoyaltyPoints200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of loyalty points |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getLoyaltyStoresCorporationIdOffers"></a>
# **getLoyaltyStoresCorporationIdOffers**
> List&lt;GetLoyaltyStoresCorporationIdOffers200Ok&gt; getLoyaltyStoresCorporationIdOffers(corporationId, datasource, ifNoneMatch)

List loyalty store offers

Return a list of offers from a specific corporation&#39;s loyalty store  --- Alternate route: &#x60;/dev/loyalty/stores/{corporation_id}/offers/&#x60;  Alternate route: &#x60;/legacy/loyalty/stores/{corporation_id}/offers/&#x60;  Alternate route: &#x60;/v1/loyalty/stores/{corporation_id}/offers/&#x60;  --- This route expires daily at 11:05

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoyaltyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");

    LoyaltyApi apiInstance = new LoyaltyApi(defaultClient);
    Integer corporationId = 56; // Integer | An EVE corporation ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    try {
      List<GetLoyaltyStoresCorporationIdOffers200Ok> result = apiInstance.getLoyaltyStoresCorporationIdOffers(corporationId, datasource, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoyaltyApi#getLoyaltyStoresCorporationIdOffers");
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
| **corporationId** | **Integer**| An EVE corporation ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |

### Return type

[**List&lt;GetLoyaltyStoresCorporationIdOffers200Ok&gt;**](GetLoyaltyStoresCorporationIdOffers200Ok.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of offers |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **404** | No loyalty point store found for the provided corporation |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

