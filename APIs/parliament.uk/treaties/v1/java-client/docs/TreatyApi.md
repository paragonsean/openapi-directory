# TreatyApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBusinessItemsByTreatyId**](TreatyApi.md#getBusinessItemsByTreatyId) | **GET** /api/Treaty/{id}/BusinessItems | Returns business items belonging to the treaty with ID. |
| [**getTreaties**](TreatyApi.md#getTreaties) | **GET** /api/Treaty | Returns a list of treaties. |
| [**getTreatyById**](TreatyApi.md#getTreatyById) | **GET** /api/Treaty/{id} | Returns a treaty by ID. |


<a id="getBusinessItemsByTreatyId"></a>
# **getBusinessItemsByTreatyId**
> BusinessItemResourceCollection getBusinessItemsByTreatyId(id)

Returns business items belonging to the treaty with ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TreatyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TreatyApi apiInstance = new TreatyApi(defaultClient);
    String id = "id_example"; // String | Business items belonging to treaty with the ID specified
    try {
      BusinessItemResourceCollection result = apiInstance.getBusinessItemsByTreatyId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TreatyApi#getBusinessItemsByTreatyId");
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
| **id** | **String**| Business items belonging to treaty with the ID specified | |

### Return type

[**BusinessItemResourceCollection**](BusinessItemResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The business items for the requested treaty |  -  |
| **400** | Bad Request |  -  |
| **404** | If the treaty cannot be found |  -  |

<a id="getTreaties"></a>
# **getTreaties**
> TreatyResourceCollection getTreaties(searchText, governmentOrganisationId, series, parliamentaryProcess, debateScheduled, motionToNotRatify, recommendedNotRatify, house, skip, take)

Returns a list of treaties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TreatyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TreatyApi apiInstance = new TreatyApi(defaultClient);
    String searchText = "searchText_example"; // String | Treaties which contains the search text specified
    Integer governmentOrganisationId = 56; // Integer | Treaties with the government organisation id specified
    SeriesMembershipType series = SeriesMembershipType.fromValue("CountrySeriesMembership"); // SeriesMembershipType | Treaties with the series membership type specified
    ParliamentaryProcess parliamentaryProcess = ParliamentaryProcess.fromValue("NotConcluded"); // ParliamentaryProcess | Treaties where the parliamentary process is concluded or notconcluded
    Boolean debateScheduled = true; // Boolean | Treaties which contain a scheduled debate
    Boolean motionToNotRatify = true; // Boolean | Treaties which contain a motion to not ratify
    Boolean recommendedNotRatify = true; // Boolean | Treaties which are recommended to not ratify
    House house = House.fromValue("Commons"); // House | Treaties which are laid in the specified house
    Integer skip = 56; // Integer | The number of records to skip from the first, default is 0
    Integer take = 56; // Integer | The number of records to return, default is 20
    try {
      TreatyResourceCollection result = apiInstance.getTreaties(searchText, governmentOrganisationId, series, parliamentaryProcess, debateScheduled, motionToNotRatify, recommendedNotRatify, house, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TreatyApi#getTreaties");
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
| **searchText** | **String**| Treaties which contains the search text specified | [optional] |
| **governmentOrganisationId** | **Integer**| Treaties with the government organisation id specified | [optional] |
| **series** | [**SeriesMembershipType**](.md)| Treaties with the series membership type specified | [optional] [enum: CountrySeriesMembership, EuropeanUnionSeriesMembership, MiscellaneousSeriesMembership] |
| **parliamentaryProcess** | [**ParliamentaryProcess**](.md)| Treaties where the parliamentary process is concluded or notconcluded | [optional] [enum: NotConcluded, Concluded] |
| **debateScheduled** | **Boolean**| Treaties which contain a scheduled debate | [optional] |
| **motionToNotRatify** | **Boolean**| Treaties which contain a motion to not ratify | [optional] |
| **recommendedNotRatify** | **Boolean**| Treaties which are recommended to not ratify | [optional] |
| **house** | [**House**](.md)| Treaties which are laid in the specified house | [optional] [enum: Commons, Lords] |
| **skip** | **Integer**| The number of records to skip from the first, default is 0 | [optional] |
| **take** | **Integer**| The number of records to return, default is 20 | [optional] |

### Return type

[**TreatyResourceCollection**](TreatyResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of treaties |  -  |
| **400** | Bad Request |  -  |

<a id="getTreatyById"></a>
# **getTreatyById**
> TreatyResource getTreatyById(id)

Returns a treaty by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TreatyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TreatyApi apiInstance = new TreatyApi(defaultClient);
    String id = "id_example"; // String | Treaty with ID specified
    try {
      TreatyResource result = apiInstance.getTreatyById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TreatyApi#getTreatyById");
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
| **id** | **String**| Treaty with ID specified | |

### Return type

[**TreatyResource**](TreatyResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the requested treaty |  -  |
| **400** | Bad Request |  -  |
| **404** | If the treaty can&#39;t be found |  -  |

