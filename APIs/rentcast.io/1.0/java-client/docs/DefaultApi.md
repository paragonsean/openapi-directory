# DefaultApi

All URIs are relative to *https://api.rentcast.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketStatistics**](DefaultApi.md#marketStatistics) | **GET** /markets | Market Statistics |
| [**propertyRecordById**](DefaultApi.md#propertyRecordById) | **GET** /properties/{id} | Property Record by Id |
| [**propertyRecords**](DefaultApi.md#propertyRecords) | **GET** /properties | Property Records |
| [**propertyRecordsRandom**](DefaultApi.md#propertyRecordsRandom) | **GET** /properties/random | Random Property Records |
| [**rentEstimateLongTerm**](DefaultApi.md#rentEstimateLongTerm) | **GET** /avm/rent/long-term | Rent Estimate |
| [**rentalListingLongTermById**](DefaultApi.md#rentalListingLongTermById) | **GET** /listings/rental/long-term/{id} | Rental Listing by Id |
| [**rentalListingsLongTerm**](DefaultApi.md#rentalListingsLongTerm) | **GET** /listings/rental/long-term | Rental Listings |
| [**saleListingById**](DefaultApi.md#saleListingById) | **GET** /listings/sale/{id} | Sale Listing by Id |
| [**saleListings**](DefaultApi.md#saleListings) | **GET** /listings/sale | Sale Listings |
| [**valueEstimate**](DefaultApi.md#valueEstimate) | **GET** /avm/value | Value Estimate |


<a id="marketStatistics"></a>
# **marketStatistics**
> MarketStatistics200Response marketStatistics(zipCode, historyRange)

Market Statistics

Returns aggregate rental statistics and listing trends for a single US zip code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String zipCode = "29611"; // String | A valid 5-digit US zip code
    Integer historyRange = 6; // Integer | The time range for historical record entries, in months. Defaults to 12 if not provided
    try {
      MarketStatistics200Response result = apiInstance.marketStatistics(zipCode, historyRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketStatistics");
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
| **zipCode** | **String**| A valid 5-digit US zip code | [default to 29611] |
| **historyRange** | **Integer**| The time range for historical record entries, in months. Defaults to 12 if not provided | [optional] [default to 6] |

### Return type

[**MarketStatistics200Response**](MarketStatistics200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="propertyRecordById"></a>
# **propertyRecordById**
> PropertyRecords200ResponseInner propertyRecordById(id)

Property Record by Id

Returns a single property record matching the specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "5500-Grand-Lake-Dr,-San-Antonio,-TX-78244"; // String | The id of the property record to return
    try {
      PropertyRecords200ResponseInner result = apiInstance.propertyRecordById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#propertyRecordById");
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
| **id** | **String**| The id of the property record to return | [default to 5500-Grand-Lake-Dr,-San-Antonio,-TX-78244] |

### Return type

[**PropertyRecords200ResponseInner**](PropertyRecords200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="propertyRecords"></a>
# **propertyRecords**
> List&lt;PropertyRecords200ResponseInner&gt; propertyRecords(address, city, state, zipCode, latitude, longitude, radius, propertyType, bedrooms, bathrooms, limit, offset)

Property Records

Search for property records in a geographical area, or by a specific address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String address = "5500 Grand Lake Dr, San Antonio, TX, 78244"; // String | The full address of the property, in the format of `Street, City, State, Zip`. Used to retrieve data for a specific property, or together with the `radius` parameter to search for properties in a specific area
    String city = "city_example"; // String | The name of the city, used to search for properties in a specific city. This parameter is case-sensitive
    String state = "state_example"; // String | The 2-character state abbreviation, used to search for properties in a specific state. This parameter is case-sensitive
    String zipCode = "zipCode_example"; // String | The 5-digit zip code, used to search for properties in a specific zip code
    Float latitude = 3.4F; // Float | The latitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for properties in a specific area
    Float longitude = 3.4F; // Float | The longitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for properties in a specific area
    Float radius = 3.4F; // Float | The radius of the search area in miles, with a maximum of 100. Use in combination with the `latitude`/`longitude` or `address` parameters to search for properties in a specific area
    String propertyType = "Single Family"; // String | The type of the property, used to search for properties matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    Float bedrooms = 3.4F; // Float | The number of bedrooms, used to search for properties matching this criteria. Use `0` to indicate a studio layout
    Float bathrooms = 3.4F; // Float | The number of bathrooms, used to search for properties matching this criteria. Supports fractions to indicate partial bathrooms
    Integer limit = 56; // Integer | The maximum number of property records to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    Integer offset = 56; // Integer | The index of the first property record to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    try {
      List<PropertyRecords200ResponseInner> result = apiInstance.propertyRecords(address, city, state, zipCode, latitude, longitude, radius, propertyType, bedrooms, bathrooms, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#propertyRecords");
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
| **address** | **String**| The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for properties in a specific area | [optional] [default to 5500 Grand Lake Dr, San Antonio, TX, 78244] |
| **city** | **String**| The name of the city, used to search for properties in a specific city. This parameter is case-sensitive | [optional] |
| **state** | **String**| The 2-character state abbreviation, used to search for properties in a specific state. This parameter is case-sensitive | [optional] |
| **zipCode** | **String**| The 5-digit zip code, used to search for properties in a specific zip code | [optional] |
| **latitude** | **Float**| The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for properties in a specific area | [optional] |
| **longitude** | **Float**| The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for properties in a specific area | [optional] |
| **radius** | **Float**| The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for properties in a specific area | [optional] |
| **propertyType** | **String**| The type of the property, used to search for properties matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] [enum: Single Family, Condo, Townhouse, Manufactured, Multi-Family, Apartment, Land] |
| **bedrooms** | **Float**| The number of bedrooms, used to search for properties matching this criteria. Use &#x60;0&#x60; to indicate a studio layout | [optional] |
| **bathrooms** | **Float**| The number of bathrooms, used to search for properties matching this criteria. Supports fractions to indicate partial bathrooms | [optional] |
| **limit** | **Integer**| The maximum number of property records to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] |
| **offset** | **Integer**| The index of the first property record to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] |

### Return type

[**List&lt;PropertyRecords200ResponseInner&gt;**](PropertyRecords200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="propertyRecordsRandom"></a>
# **propertyRecordsRandom**
> List&lt;PropertyRecordsRandom200ResponseInner&gt; propertyRecordsRandom(limit)

Random Property Records

Returns a list of property records selected at random.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 5; // Integer | The number of records to return, between 1 and 500. Defaults to 50 if not provided
    try {
      List<PropertyRecordsRandom200ResponseInner> result = apiInstance.propertyRecordsRandom(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#propertyRecordsRandom");
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
| **limit** | **Integer**| The number of records to return, between 1 and 500. Defaults to 50 if not provided | [optional] [default to 5] |

### Return type

[**List&lt;PropertyRecordsRandom200ResponseInner&gt;**](PropertyRecordsRandom200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="rentEstimateLongTerm"></a>
# **rentEstimateLongTerm**
> RentEstimateLongTerm200Response rentEstimateLongTerm(address, latitude, longitude, propertyType, bedrooms, bathrooms, squareFootage, maxRadius, daysOld, compCount)

Rent Estimate

Returns a property rent estimate and comparable properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String address = "5500 Grand Lake Drive, San Antonio, TX, 78244"; // String | The full property address, in the format of `Street, City, State, Zip`. You need to provide either the `address` or the `latitude`/`longitude` parameters
    Float latitude = 3.4F; // Float | The latitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
    Float longitude = 3.4F; // Float | The longitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
    String propertyType = "Single Family"; // String | The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    Float bedrooms = 4F; // Float | The number of bedrooms in the property. Use `0` to indicate a studio layout
    Float bathrooms = 2F; // Float | The number of bathrooms in the property. Supports fractions to indicate partial bathrooms
    Float squareFootage = 1600F; // Float | The total living area size of the property, in square feet
    Float maxRadius = 3.4F; // Float | The maximum distance between comparable listings and the subject property, in miles
    Float daysOld = 3.4F; // Float | The maximum number of days since comparable listings were last seen on the market, with a minimum of 1
    Integer compCount = 5; // Integer | The number of comparable listings to use when calculating the rent estimate, between 5 and 25. Defaults to 10 if not provided
    try {
      RentEstimateLongTerm200Response result = apiInstance.rentEstimateLongTerm(address, latitude, longitude, propertyType, bedrooms, bathrooms, squareFootage, maxRadius, daysOld, compCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rentEstimateLongTerm");
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
| **address** | **String**| The full property address, in the format of &#x60;Street, City, State, Zip&#x60;. You need to provide either the &#x60;address&#x60; or the &#x60;latitude&#x60;/&#x60;longitude&#x60; parameters | [optional] [default to 5500 Grand Lake Drive, San Antonio, TX, 78244] |
| **latitude** | **Float**| The latitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] |
| **longitude** | **Float**| The longitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] |
| **propertyType** | **String**| The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] [default to Single Family] [enum: Single Family, Condo, Townhouse, Manufactured, Multi-Family, Apartment] |
| **bedrooms** | **Float**| The number of bedrooms in the property. Use &#x60;0&#x60; to indicate a studio layout | [optional] [default to 4] |
| **bathrooms** | **Float**| The number of bathrooms in the property. Supports fractions to indicate partial bathrooms | [optional] [default to 2] |
| **squareFootage** | **Float**| The total living area size of the property, in square feet | [optional] [default to 1600] |
| **maxRadius** | **Float**| The maximum distance between comparable listings and the subject property, in miles | [optional] |
| **daysOld** | **Float**| The maximum number of days since comparable listings were last seen on the market, with a minimum of 1 | [optional] |
| **compCount** | **Integer**| The number of comparable listings to use when calculating the rent estimate, between 5 and 25. Defaults to 10 if not provided | [optional] [default to 5] |

### Return type

[**RentEstimateLongTerm200Response**](RentEstimateLongTerm200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="rentalListingLongTermById"></a>
# **rentalListingLongTermById**
> RentalListingLongTermById200Response rentalListingLongTermById(id)

Rental Listing by Id

Returns a single rental listing matching the specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "1702-Cherry-Orchard-Dr,-Austin,-TX-78745"; // String | The id of the property listing to return
    try {
      RentalListingLongTermById200Response result = apiInstance.rentalListingLongTermById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rentalListingLongTermById");
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
| **id** | **String**| The id of the property listing to return | [default to 1702-Cherry-Orchard-Dr,-Austin,-TX-78745] |

### Return type

[**RentalListingLongTermById200Response**](RentalListingLongTermById200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="rentalListingsLongTerm"></a>
# **rentalListingsLongTerm**
> List&lt;RentalListingsLongTerm200ResponseInner&gt; rentalListingsLongTerm(address, city, state, zipCode, latitude, longitude, radius, propertyType, bedrooms, bathrooms, status, daysOld, limit, offset)

Rental Listings

Search for rental listings in a geographical area, or by a specific address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String address = "address_example"; // String | The full address of the property, in the format of `Street, City, State, Zip`. Used to retrieve data for a specific property, or together with the `radius` parameter to search for listings in a specific area
    String city = "Austin"; // String | The name of the city, used to search for listings in a specific city. This parameter is case-sensitive
    String state = "TX"; // String | The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive
    String zipCode = "zipCode_example"; // String | The 5-digit zip code, used to search for listings in a specific zip code
    Float latitude = 3.4F; // Float | The latitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
    Float longitude = 3.4F; // Float | The longitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
    Float radius = 3.4F; // Float | The radius of the search area in miles, with a maximum of 100. Use in combination with the `latitude`/`longitude` or `address` parameters to search for listings in a specific area
    String propertyType = "Single Family"; // String | The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    Float bedrooms = 3.4F; // Float | The number of bedrooms, used to search for listings matching this criteria. Use `0` to indicate a studio layout
    Float bathrooms = 3.4F; // Float | The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms
    String status = "Active"; // String | The current listing status, used to search for listings matching this criteria
    Float daysOld = 3.4F; // Float | The maximum number of days since a property was listed on the market, with a minimum of 1
    Integer limit = 5; // Integer | The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    Integer offset = 56; // Integer | The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    try {
      List<RentalListingsLongTerm200ResponseInner> result = apiInstance.rentalListingsLongTerm(address, city, state, zipCode, latitude, longitude, radius, propertyType, bedrooms, bathrooms, status, daysOld, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rentalListingsLongTerm");
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
| **address** | **String**| The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for listings in a specific area | [optional] |
| **city** | **String**| The name of the city, used to search for listings in a specific city. This parameter is case-sensitive | [optional] [default to Austin] |
| **state** | **String**| The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive | [optional] [default to TX] |
| **zipCode** | **String**| The 5-digit zip code, used to search for listings in a specific zip code | [optional] |
| **latitude** | **Float**| The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] |
| **longitude** | **Float**| The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] |
| **radius** | **Float**| The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for listings in a specific area | [optional] |
| **propertyType** | **String**| The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] [enum: Single Family, Condo, Townhouse, Manufactured, Multi-Family, Apartment] |
| **bedrooms** | **Float**| The number of bedrooms, used to search for listings matching this criteria. Use &#x60;0&#x60; to indicate a studio layout | [optional] |
| **bathrooms** | **Float**| The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms | [optional] |
| **status** | **String**| The current listing status, used to search for listings matching this criteria | [optional] [default to Active] [enum: Active, Inactive] |
| **daysOld** | **Float**| The maximum number of days since a property was listed on the market, with a minimum of 1 | [optional] |
| **limit** | **Integer**| The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] [default to 5] |
| **offset** | **Integer**| The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] |

### Return type

[**List&lt;RentalListingsLongTerm200ResponseInner&gt;**](RentalListingsLongTerm200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="saleListingById"></a>
# **saleListingById**
> SaleListingById200Response saleListingById(id)

Sale Listing by Id

Returns a single sale listing matching the specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "1702-Cherry-Orchard-Dr,-Austin,-TX-78745"; // String | The id of the property listing to return
    try {
      SaleListingById200Response result = apiInstance.saleListingById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#saleListingById");
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
| **id** | **String**| The id of the property listing to return | [default to 1702-Cherry-Orchard-Dr,-Austin,-TX-78745] |

### Return type

[**SaleListingById200Response**](SaleListingById200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="saleListings"></a>
# **saleListings**
> List&lt;SaleListings200ResponseInner&gt; saleListings(address, city, state, zipCode, latitude, longitude, radius, propertyType, bedrooms, bathrooms, status, daysOld, limit, offset)

Sale Listings

Search for sale listings in a geographical area, or by a specific address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String address = "address_example"; // String | The full address of the property, in the format of `Street, City, State, Zip`. Used to retrieve data for a specific property, or together with the `radius` parameter to search for listings in a specific area
    String city = "Austin"; // String | The name of the city, used to search for listings in a specific city. This parameter is case-sensitive
    String state = "TX"; // String | The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive
    String zipCode = "zipCode_example"; // String | The 5-digit zip code, used to search for listings in a specific zip code
    Float latitude = 3.4F; // Float | The latitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
    Float longitude = 3.4F; // Float | The longitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
    Float radius = 3.4F; // Float | The radius of the search area in miles, with a maximum of 100. Use in combination with the `latitude`/`longitude` or `address` parameters to search for listings in a specific area
    String propertyType = "Single Family"; // String | The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    Float bedrooms = 3.4F; // Float | The number of bedrooms, used to search for listings matching this criteria. Use `0` to indicate a studio layout
    Float bathrooms = 3.4F; // Float | The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms
    String status = "Active"; // String | The current listing status, used to search for listings matching this criteria
    Float daysOld = 3.4F; // Float | The maximum number of days since a property was listed on the market, with a minimum of 1
    Integer limit = 5; // Integer | The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    Integer offset = 56; // Integer | The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
    try {
      List<SaleListings200ResponseInner> result = apiInstance.saleListings(address, city, state, zipCode, latitude, longitude, radius, propertyType, bedrooms, bathrooms, status, daysOld, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#saleListings");
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
| **address** | **String**| The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for listings in a specific area | [optional] |
| **city** | **String**| The name of the city, used to search for listings in a specific city. This parameter is case-sensitive | [optional] [default to Austin] |
| **state** | **String**| The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive | [optional] [default to TX] |
| **zipCode** | **String**| The 5-digit zip code, used to search for listings in a specific zip code | [optional] |
| **latitude** | **Float**| The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] |
| **longitude** | **Float**| The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] |
| **radius** | **Float**| The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for listings in a specific area | [optional] |
| **propertyType** | **String**| The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] [enum: Single Family, Condo, Townhouse, Manufactured, Multi-Family, Apartment, Land] |
| **bedrooms** | **Float**| The number of bedrooms, used to search for listings matching this criteria. Use &#x60;0&#x60; to indicate a studio layout | [optional] |
| **bathrooms** | **Float**| The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms | [optional] |
| **status** | **String**| The current listing status, used to search for listings matching this criteria | [optional] [default to Active] [enum: Active, Inactive] |
| **daysOld** | **Float**| The maximum number of days since a property was listed on the market, with a minimum of 1 | [optional] |
| **limit** | **Integer**| The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] [default to 5] |
| **offset** | **Integer**| The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] |

### Return type

[**List&lt;SaleListings200ResponseInner&gt;**](SaleListings200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

<a id="valueEstimate"></a>
# **valueEstimate**
> ValueEstimate200Response valueEstimate(address, latitude, longitude, propertyType, bedrooms, bathrooms, squareFootage, maxRadius, daysOld, compCount)

Value Estimate

Returns a property value estimate and comparable properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.rentcast.io/v1");
    
    // Configure API key authorization: sec0
    ApiKeyAuth sec0 = (ApiKeyAuth) defaultClient.getAuthentication("sec0");
    sec0.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //sec0.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String address = "5500 Grand Lake Drive, San Antonio, TX, 78244"; // String | The full property address, in the format of `Street, City, State, Zip`. You need to provide either the `address` or the `latitude`/`longitude` parameters
    Float latitude = 3.4F; // Float | The latitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
    Float longitude = 3.4F; // Float | The longitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
    String propertyType = "Single Family"; // String | The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
    Float bedrooms = 4F; // Float | The number of bedrooms in the property. Use `0` to indicate a studio layout
    Float bathrooms = 2F; // Float | The number of bathrooms in the property. Supports fractions to indicate partial bathrooms
    Float squareFootage = 1600F; // Float | The total living area size of the property, in square feet
    Float maxRadius = 3.4F; // Float | The maximum distance between comparable listings and the subject property, in miles
    Float daysOld = 3.4F; // Float | The maximum number of days since comparable listings were last seen on the market, with a minimum of 1
    Integer compCount = 5; // Integer | The number of comparable listings to use when calculating the value estimate, between 5 and 25. Defaults to 10 if not provided
    try {
      ValueEstimate200Response result = apiInstance.valueEstimate(address, latitude, longitude, propertyType, bedrooms, bathrooms, squareFootage, maxRadius, daysOld, compCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#valueEstimate");
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
| **address** | **String**| The full property address, in the format of &#x60;Street, City, State, Zip&#x60;. You need to provide either the &#x60;address&#x60; or the &#x60;latitude&#x60;/&#x60;longitude&#x60; parameters | [optional] [default to 5500 Grand Lake Drive, San Antonio, TX, 78244] |
| **latitude** | **Float**| The latitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] |
| **longitude** | **Float**| The longitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] |
| **propertyType** | **String**| The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] [default to Single Family] [enum: Single Family, Condo, Townhouse, Manufactured, Multi-Family, Apartment, Land] |
| **bedrooms** | **Float**| The number of bedrooms in the property. Use &#x60;0&#x60; to indicate a studio layout | [optional] [default to 4] |
| **bathrooms** | **Float**| The number of bathrooms in the property. Supports fractions to indicate partial bathrooms | [optional] [default to 2] |
| **squareFootage** | **Float**| The total living area size of the property, in square feet | [optional] [default to 1600] |
| **maxRadius** | **Float**| The maximum distance between comparable listings and the subject property, in miles | [optional] |
| **daysOld** | **Float**| The maximum number of days since comparable listings were last seen on the market, with a minimum of 1 | [optional] |
| **compCount** | **Integer**| The number of comparable listings to use when calculating the value estimate, between 5 and 25. Defaults to 10 if not provided | [optional] [default to 5] |

### Return type

[**ValueEstimate200Response**](ValueEstimate200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

