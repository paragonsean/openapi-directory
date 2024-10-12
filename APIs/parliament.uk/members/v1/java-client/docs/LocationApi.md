# LocationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiLocationBrowseLocationTypeLocationNameGet**](LocationApi.md#apiLocationBrowseLocationTypeLocationNameGet) | **GET** /api/Location/Browse/{locationType}/{locationName} | Returns a list of locations, both parent and child |
| [**apiLocationConstituencyIdElectionResultElectionIdGet**](LocationApi.md#apiLocationConstituencyIdElectionResultElectionIdGet) | **GET** /api/Location/Constituency/{id}/ElectionResult/{electionId} | Returns an election result by constituency and election id |
| [**apiLocationConstituencyIdElectionResultLatestGet**](LocationApi.md#apiLocationConstituencyIdElectionResultLatestGet) | **GET** /api/Location/Constituency/{id}/ElectionResult/Latest | Returns latest election result by constituency id |
| [**apiLocationConstituencyIdElectionResultsGet**](LocationApi.md#apiLocationConstituencyIdElectionResultsGet) | **GET** /api/Location/Constituency/{id}/ElectionResults | Returns a list of election results by constituency ID |
| [**apiLocationConstituencyIdGeometryGet**](LocationApi.md#apiLocationConstituencyIdGeometryGet) | **GET** /api/Location/Constituency/{id}/Geometry | Returns geometry by constituency ID |
| [**apiLocationConstituencyIdGet**](LocationApi.md#apiLocationConstituencyIdGet) | **GET** /api/Location/Constituency/{id} | Returns a constituency by ID |
| [**apiLocationConstituencyIdRepresentationsGet**](LocationApi.md#apiLocationConstituencyIdRepresentationsGet) | **GET** /api/Location/Constituency/{id}/Representations | Returns a list of representations by constituency ID |
| [**apiLocationConstituencyIdSynopsisGet**](LocationApi.md#apiLocationConstituencyIdSynopsisGet) | **GET** /api/Location/Constituency/{id}/Synopsis | Returns a synopsis by constituency ID |
| [**apiLocationConstituencySearchGet**](LocationApi.md#apiLocationConstituencySearchGet) | **GET** /api/Location/Constituency/Search | Returns a list of constituencies |


<a id="apiLocationBrowseLocationTypeLocationNameGet"></a>
# **apiLocationBrowseLocationTypeLocationNameGet**
> LocationItem apiLocationBrowseLocationTypeLocationNameGet(locationType, locationName)

Returns a list of locations, both parent and child

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    LocationType locationType = LocationType.fromValue("0"); // LocationType | Location by type of location
    String locationName = "locationName_example"; // String | Location by name specified
    try {
      LocationItem result = apiInstance.apiLocationBrowseLocationTypeLocationNameGet(locationType, locationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationBrowseLocationTypeLocationNameGet");
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
| **locationType** | [**LocationType**](.md)| Location by type of location | [enum: 0, 1, 2, 3] |
| **locationName** | **String**| Location by name specified | |

### Return type

[**LocationItem**](LocationItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencyIdElectionResultElectionIdGet"></a>
# **apiLocationConstituencyIdElectionResultElectionIdGet**
> ElectionResultItem apiLocationConstituencyIdElectionResultElectionIdGet(id, electionId)

Returns an election result by constituency and election id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Integer id = 56; // Integer | Election result by constituency id
    Integer electionId = 56; // Integer | Election result by election id
    try {
      ElectionResultItem result = apiInstance.apiLocationConstituencyIdElectionResultElectionIdGet(id, electionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencyIdElectionResultElectionIdGet");
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
| **id** | **Integer**| Election result by constituency id | |
| **electionId** | **Integer**| Election result by election id | |

### Return type

[**ElectionResultItem**](ElectionResultItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencyIdElectionResultLatestGet"></a>
# **apiLocationConstituencyIdElectionResultLatestGet**
> ElectionResultItem apiLocationConstituencyIdElectionResultLatestGet(id)

Returns latest election result by constituency id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Integer id = 56; // Integer | Latest election result by constituency id
    try {
      ElectionResultItem result = apiInstance.apiLocationConstituencyIdElectionResultLatestGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencyIdElectionResultLatestGet");
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
| **id** | **Integer**| Latest election result by constituency id | |

### Return type

[**ElectionResultItem**](ElectionResultItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencyIdElectionResultsGet"></a>
# **apiLocationConstituencyIdElectionResultsGet**
> ElectionResultListItem apiLocationConstituencyIdElectionResultsGet(id)

Returns a list of election results by constituency ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Integer id = 56; // Integer | Elections results by constituency ID
    try {
      ElectionResultListItem result = apiInstance.apiLocationConstituencyIdElectionResultsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencyIdElectionResultsGet");
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
| **id** | **Integer**| Elections results by constituency ID | |

### Return type

[**ElectionResultListItem**](ElectionResultListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencyIdGeometryGet"></a>
# **apiLocationConstituencyIdGeometryGet**
> StringItem apiLocationConstituencyIdGeometryGet(id)

Returns geometry by constituency ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Integer id = 56; // Integer | Geometry by constituency ID
    try {
      StringItem result = apiInstance.apiLocationConstituencyIdGeometryGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencyIdGeometryGet");
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
| **id** | **Integer**| Geometry by constituency ID | |

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencyIdGet"></a>
# **apiLocationConstituencyIdGet**
> ConstituencyItem apiLocationConstituencyIdGet(id)

Returns a constituency by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Integer id = 56; // Integer | Constituency by ID
    try {
      ConstituencyItem result = apiInstance.apiLocationConstituencyIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencyIdGet");
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
| **id** | **Integer**| Constituency by ID | |

### Return type

[**ConstituencyItem**](ConstituencyItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencyIdRepresentationsGet"></a>
# **apiLocationConstituencyIdRepresentationsGet**
> ConstituencyRepresentationListItem apiLocationConstituencyIdRepresentationsGet(id)

Returns a list of representations by constituency ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Integer id = 56; // Integer | Representations by constituency ID
    try {
      ConstituencyRepresentationListItem result = apiInstance.apiLocationConstituencyIdRepresentationsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencyIdRepresentationsGet");
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
| **id** | **Integer**| Representations by constituency ID | |

### Return type

[**ConstituencyRepresentationListItem**](ConstituencyRepresentationListItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencyIdSynopsisGet"></a>
# **apiLocationConstituencyIdSynopsisGet**
> StringItem apiLocationConstituencyIdSynopsisGet(id)

Returns a synopsis by constituency ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    Integer id = 56; // Integer | Synopsis by constituency ID
    try {
      StringItem result = apiInstance.apiLocationConstituencyIdSynopsisGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencyIdSynopsisGet");
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
| **id** | **Integer**| Synopsis by constituency ID | |

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiLocationConstituencySearchGet"></a>
# **apiLocationConstituencySearchGet**
> ConstituencyMembersServiceSearchResult apiLocationConstituencySearchGet(searchText, skip, take)

Returns a list of constituencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LocationApi apiInstance = new LocationApi(defaultClient);
    String searchText = "searchText_example"; // String | Constituencies containing serach term in their name
    Integer skip = 0; // Integer | The number of records to skip from the first, default is 0
    Integer take = 20; // Integer | The number of records to return, default is 20. Maximum is 20
    try {
      ConstituencyMembersServiceSearchResult result = apiInstance.apiLocationConstituencySearchGet(searchText, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#apiLocationConstituencySearchGet");
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
| **searchText** | **String**| Constituencies containing serach term in their name | [optional] |
| **skip** | **Integer**| The number of records to skip from the first, default is 0 | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return, default is 20. Maximum is 20 | [optional] [default to 20] |

### Return type

[**ConstituencyMembersServiceSearchResult**](ConstituencyMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

