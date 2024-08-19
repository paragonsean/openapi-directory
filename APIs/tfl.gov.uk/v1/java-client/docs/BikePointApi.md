# BikePointApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bikePointGet**](BikePointApi.md#bikePointGet) | **GET** /BikePoint/{id} | Gets the bike point with the given id. |
| [**bikePointGetAll**](BikePointApi.md#bikePointGetAll) | **GET** /BikePoint | Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces              numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) !&#x3D; 0 indicates broken docks. |
| [**bikePointSearch**](BikePointApi.md#bikePointSearch) | **GET** /BikePoint/Search | Search for bike stations by their name, a bike point&#39;s name often contains information about the name of the street              or nearby landmarks, for example. Note that the search result does not contain the PlaceProperties i.e. the status              or occupancy of the BikePoint, to get that information you should retrieve the BikePoint by its id on /BikePoint/id. |


<a id="bikePointGet"></a>
# **bikePointGet**
> TflApiPresentationEntitiesPlace bikePointGet(id)

Gets the bike point with the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BikePointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    BikePointApi apiInstance = new BikePointApi(defaultClient);
    String id = "id_example"; // String | A bike point id (a list of ids can be obtained from the above BikePoint call)
    try {
      TflApiPresentationEntitiesPlace result = apiInstance.bikePointGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BikePointApi#bikePointGet");
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
| **id** | **String**| A bike point id (a list of ids can be obtained from the above BikePoint call) | |

### Return type

[**TflApiPresentationEntitiesPlace**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bikePointGetAll"></a>
# **bikePointGetAll**
> List&lt;TflApiPresentationEntitiesPlace&gt; bikePointGetAll()

Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces              numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) !&#x3D; 0 indicates broken docks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BikePointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    BikePointApi apiInstance = new BikePointApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.bikePointGetAll();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BikePointApi#bikePointGetAll");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;TflApiPresentationEntitiesPlace&gt;**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bikePointSearch"></a>
# **bikePointSearch**
> List&lt;TflApiPresentationEntitiesPlace&gt; bikePointSearch(query)

Search for bike stations by their name, a bike point&#39;s name often contains information about the name of the street              or nearby landmarks, for example. Note that the search result does not contain the PlaceProperties i.e. the status              or occupancy of the BikePoint, to get that information you should retrieve the BikePoint by its id on /BikePoint/id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BikePointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    BikePointApi apiInstance = new BikePointApi(defaultClient);
    String query = "query_example"; // String | The search term e.g. \"St. James\"
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.bikePointSearch(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BikePointApi#bikePointSearch");
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
| **query** | **String**| The search term e.g. \&quot;St. James\&quot; | |

### Return type

[**List&lt;TflApiPresentationEntitiesPlace&gt;**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

