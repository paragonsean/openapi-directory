# DealerApiApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dealerCarUkIdGet**](DealerApiApi.md#dealerCarUkIdGet) | **GET** /dealer/car/uk/{id} | Dealer by id |
| [**dealerHeavyEquipmentIdGet**](DealerApiApi.md#dealerHeavyEquipmentIdGet) | **GET** /dealer/heavy-equipment/{id} | Dealer by id |
| [**dealerMotorcycleIdGet**](DealerApiApi.md#dealerMotorcycleIdGet) | **GET** /dealer/motorcycle/{id} | Dealer by id |
| [**dealerRvIdGet**](DealerApiApi.md#dealerRvIdGet) | **GET** /dealer/rv/{id} | Dealer by id |
| [**dealerSearch**](DealerApiApi.md#dealerSearch) | **GET** /dealers/car | Find car dealers around |
| [**dealersCarUkGet**](DealerApiApi.md#dealersCarUkGet) | **GET** /dealers/car/uk | Find car dealers around |
| [**dealersHeavyEquipmentGet**](DealerApiApi.md#dealersHeavyEquipmentGet) | **GET** /dealers/heavy-equipment | Find car dealers around |
| [**dealersMotorcycleGet**](DealerApiApi.md#dealersMotorcycleGet) | **GET** /dealers/motorcycle | Find car dealers around |
| [**dealersRvGet**](DealerApiApi.md#dealersRvGet) | **GET** /dealers/rv | Find car dealers around |
| [**getDealer**](DealerApiApi.md#getDealer) | **GET** /dealer/car/{id} | Dealer by id |


<a id="dealerCarUkIdGet"></a>
# **dealerCarUkIdGet**
> Dealer dealerCarUkIdGet(id, apiKey, provider)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String id = "id_example"; // String | Dealer id to get all the dealer info attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    try {
      Dealer result = apiInstance.dealerCarUkIdGet(id, apiKey, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealerCarUkIdGet");
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
| **id** | **String**| Dealer id to get all the dealer info attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dealer for the given id |  -  |
| **0** | Error |  -  |

<a id="dealerHeavyEquipmentIdGet"></a>
# **dealerHeavyEquipmentIdGet**
> Dealer dealerHeavyEquipmentIdGet(id, apiKey, provider)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String id = "id_example"; // String | Dealer id to get all the dealer info attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    try {
      Dealer result = apiInstance.dealerHeavyEquipmentIdGet(id, apiKey, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealerHeavyEquipmentIdGet");
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
| **id** | **String**| Dealer id to get all the dealer info attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dealer for the given id |  -  |
| **0** | Error |  -  |

<a id="dealerMotorcycleIdGet"></a>
# **dealerMotorcycleIdGet**
> Dealer dealerMotorcycleIdGet(id, apiKey, provider)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String id = "id_example"; // String | Dealer id to get all the dealer info attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    try {
      Dealer result = apiInstance.dealerMotorcycleIdGet(id, apiKey, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealerMotorcycleIdGet");
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
| **id** | **String**| Dealer id to get all the dealer info attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dealer for the given id |  -  |
| **0** | Error |  -  |

<a id="dealerRvIdGet"></a>
# **dealerRvIdGet**
> Dealer dealerRvIdGet(id, apiKey, provider)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String id = "id_example"; // String | Dealer id to get all the dealer info attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    try {
      Dealer result = apiInstance.dealerRvIdGet(id, apiKey, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealerRvIdGet");
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
| **id** | **String**| Dealer id to get all the dealer info attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dealer for the given id |  -  |
| **0** | Error |  -  |

<a id="dealerSearch"></a>
# **dealerSearch**
> DealersResponse dealerSearch(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String country = "US"; // String | To filter listing on Country in which they are listed
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String listingCountRange = "listingCountRange_example"; // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    String inventoryUrl = "inventoryUrl_example"; // String | inventory_url of dealer to be searched
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    try {
      DealersResponse result = apiInstance.dealerSearch(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealerSearch");
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
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [enum: US, CA, us, ca, uk, england, scotland, northan ireland, wales] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] |
| **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of dealers for the search |  -  |
| **0** | Error |  -  |

<a id="dealersCarUkGet"></a>
# **dealersCarUkGet**
> DealersResponse dealersCarUkGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, county, listingCountRange, inventoryUrl, postalCode, sortBy, sortOrder, provider, facets, rangeFacets)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String country = "US"; // String | To filter listing on Country in which they are listed
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String county = "county_example"; // String | To filter listing on county in which they are listed
    String listingCountRange = "listingCountRange_example"; // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    String inventoryUrl = "inventoryUrl_example"; // String | inventory_url of dealer to be searched
    String postalCode = "postalCode_example"; // String | To filter listing on postal code around which they are listed
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    try {
      DealersResponse result = apiInstance.dealersCarUkGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, county, listingCountRange, inventoryUrl, postalCode, sortBy, sortOrder, provider, facets, rangeFacets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealersCarUkGet");
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
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [enum: US, CA, us, ca, uk, england, scotland, northan ireland, wales] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **county** | **String**| To filter listing on county in which they are listed | [optional] |
| **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] |
| **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] |
| **postalCode** | **String**| To filter listing on postal code around which they are listed | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of dealers for the search |  -  |
| **0** | Error |  -  |

<a id="dealersHeavyEquipmentGet"></a>
# **dealersHeavyEquipmentGet**
> DealersResponse dealersHeavyEquipmentGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String country = "US"; // String | To filter listing on Country in which they are listed
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String listingCountRange = "listingCountRange_example"; // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    String inventoryUrl = "inventoryUrl_example"; // String | inventory_url of dealer to be searched
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    try {
      DealersResponse result = apiInstance.dealersHeavyEquipmentGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealersHeavyEquipmentGet");
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
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [enum: US, CA, us, ca, uk, england, scotland, northan ireland, wales] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] |
| **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of dealers for the search |  -  |
| **0** | Error |  -  |

<a id="dealersMotorcycleGet"></a>
# **dealersMotorcycleGet**
> DealersResponse dealersMotorcycleGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String country = "US"; // String | To filter listing on Country in which they are listed
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String listingCountRange = "listingCountRange_example"; // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    String inventoryUrl = "inventoryUrl_example"; // String | inventory_url of dealer to be searched
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    try {
      DealersResponse result = apiInstance.dealersMotorcycleGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealersMotorcycleGet");
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
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [enum: US, CA, us, ca, uk, england, scotland, northan ireland, wales] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] |
| **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of dealers for the search |  -  |
| **0** | Error |  -  |

<a id="dealersRvGet"></a>
# **dealersRvGet**
> DealersResponse dealersRvGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String country = "US"; // String | To filter listing on Country in which they are listed
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String listingCountRange = "listingCountRange_example"; // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    String inventoryUrl = "inventoryUrl_example"; // String | inventory_url of dealer to be searched
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    try {
      DealersResponse result = apiInstance.dealersRvGet(apiKey, latitude, longitude, radius, rows, start, country, dealerType, city, state, listingCountRange, inventoryUrl, zip, sortBy, sortOrder, provider, facets, rangeFacets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#dealersRvGet");
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
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [enum: US, CA, us, ca, uk, england, scotland, northan ireland, wales] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] |
| **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of dealers for the search |  -  |
| **0** | Error |  -  |

<a id="getDealer"></a>
# **getDealer**
> Dealer getDealer(id, apiKey, provider)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    DealerApiApi apiInstance = new DealerApiApi(defaultClient);
    String id = "id_example"; // String | Dealer id to get all the dealer info attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean provider = false; // Boolean | boolean param to include site providers name in response
    try {
      Dealer result = apiInstance.getDealer(id, apiKey, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealerApiApi#getDealer");
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
| **id** | **String**| Dealer id to get all the dealer info attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false] |

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dealer for the given id |  -  |
| **0** | Error |  -  |

