# PlacesApi

All URIs are relative to *https://api2.lotadata.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**placesGet**](PlacesApi.md#placesGet) | **GET** /places | Venues, landmarks, regions, these are all places to search. |
| [**placesIdGet**](PlacesApi.md#placesIdGet) | **GET** /places/{id} | Get specific place details |


<a id="placesGet"></a>
# **placesGet**
> PlacesSearchResponse placesGet(fieldset, category, function, ambience, tag, type, name, exact, capacityMin, capacityMax, street, locality, region, postalCode, country, center, radius, bbox, polygon, within, offset, limit)

Venues, landmarks, regions, these are all places to search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.lotadata.com/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PlacesApi apiInstance = new PlacesApi(defaultClient);
    String fieldset = "summary"; // String | Return results starting at specified offset (summary, context, detail)
    List<String> category = Arrays.asList(); // List<String> | List of required PlaceCategory ids (Tier 1)
    List<String> function = Arrays.asList(); // List<String> | List of required PlaceFunction ids (Tier 2)
    List<String> ambience = Arrays.asList(); // List<String> | List of required ambience ids
    List<String> tag = Arrays.asList(); // List<String> | List of required tags
    String type = "type_example"; // String | Specific PlaceType to return
    String name = "name_example"; // String | Match on place names
    Boolean exact = true; // Boolean | Require an exact name match
    BigDecimal capacityMin = new BigDecimal(78); // BigDecimal | Min capacity at location
    BigDecimal capacityMax = new BigDecimal(78); // BigDecimal | Min capacity at location
    String street = "street_example"; // String | Address of the place or street component of the address
    String locality = "locality_example"; // String | city, town, or neighborhood of the place
    String region = "region_example"; // String | region or state
    String postalCode = "postalCode_example"; // String | Postal or zip code
    String country = "country_example"; // String | country component of the address
    String center = "center_example"; // String | latitude,longitude of the origin point
    Integer radius = 56; // Integer | Distance from origin in meters
    List<String> bbox = Arrays.asList(); // List<String> | Corner of a bounding box (lat,lng). Requires 0 or 2 pairs
    List<String> polygon = Arrays.asList(); // List<String> | Closed custom polygon. Ordered list of lat,lng pairs
    String within = "within_example"; // String | Search within specified geopolitical place id
    Integer offset = 56; // Integer | Return results starting at specified offset
    Integer limit = 56; // Integer | Max results to return
    try {
      PlacesSearchResponse result = apiInstance.placesGet(fieldset, category, function, ambience, tag, type, name, exact, capacityMin, capacityMax, street, locality, region, postalCode, country, center, radius, bbox, polygon, within, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacesApi#placesGet");
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
| **fieldset** | **String**| Return results starting at specified offset (summary, context, detail) | [default to context] [enum: summary, detail, context] |
| **category** | [**List&lt;String&gt;**](String.md)| List of required PlaceCategory ids (Tier 1) | [optional] |
| **function** | [**List&lt;String&gt;**](String.md)| List of required PlaceFunction ids (Tier 2) | [optional] |
| **ambience** | [**List&lt;String&gt;**](String.md)| List of required ambience ids | [optional] |
| **tag** | [**List&lt;String&gt;**](String.md)| List of required tags | [optional] |
| **type** | **String**| Specific PlaceType to return | [optional] |
| **name** | **String**| Match on place names | [optional] |
| **exact** | **Boolean**| Require an exact name match | [optional] |
| **capacityMin** | **BigDecimal**| Min capacity at location | [optional] |
| **capacityMax** | **BigDecimal**| Min capacity at location | [optional] |
| **street** | **String**| Address of the place or street component of the address | [optional] |
| **locality** | **String**| city, town, or neighborhood of the place | [optional] |
| **region** | **String**| region or state | [optional] |
| **postalCode** | **String**| Postal or zip code | [optional] |
| **country** | **String**| country component of the address | [optional] |
| **center** | **String**| latitude,longitude of the origin point | [optional] |
| **radius** | **Integer**| Distance from origin in meters | [optional] |
| **bbox** | [**List&lt;String&gt;**](String.md)| Corner of a bounding box (lat,lng). Requires 0 or 2 pairs | [optional] |
| **polygon** | [**List&lt;String&gt;**](String.md)| Closed custom polygon. Ordered list of lat,lng pairs | [optional] |
| **within** | **String**| Search within specified geopolitical place id | [optional] |
| **offset** | **Integer**| Return results starting at specified offset | [optional] |
| **limit** | **Integer**| Max results to return | [optional] |

### Return type

[**PlacesSearchResponse**](PlacesSearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of matching events |  -  |
| **400** | Unexpected error |  -  |

<a id="placesIdGet"></a>
# **placesIdGet**
> PlaceDetail placesIdGet(id, fieldset)

Get specific place details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.lotadata.com/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PlacesApi apiInstance = new PlacesApi(defaultClient);
    String id = "id_example"; // String | place @id
    String fieldset = "summary"; // String | 
    try {
      PlaceDetail result = apiInstance.placesIdGet(id, fieldset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacesApi#placesIdGet");
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
| **id** | **String**| place @id | |
| **fieldset** | **String**|  | [optional] [default to summary] [enum: summary, detail, context, minicontext] |

### Return type

[**PlaceDetail**](PlaceDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested place |  -  |
| **404** | Unexpected error |  -  |

