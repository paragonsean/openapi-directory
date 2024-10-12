# StatutoryInstrumentApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBusinessItemsByStatutoryInstrumentId**](StatutoryInstrumentApi.md#getBusinessItemsByStatutoryInstrumentId) | **GET** /api/v1/StatutoryInstrument/{id}/BusinessItems | Returns business items belonging to statutory instrument with ID. |
| [**getStatutoryInstrumentById**](StatutoryInstrumentApi.md#getStatutoryInstrumentById) | **GET** /api/v1/StatutoryInstrument/{id} | Returns a statutory instrument by ID. |
| [**getStatutoryInstruments**](StatutoryInstrumentApi.md#getStatutoryInstruments) | **GET** /api/v1/StatutoryInstrument | Returns a list of statutory instruments. |


<a id="getBusinessItemsByStatutoryInstrumentId"></a>
# **getBusinessItemsByStatutoryInstrumentId**
> BusinessItemResourceCollection getBusinessItemsByStatutoryInstrumentId(id)

Returns business items belonging to statutory instrument with ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatutoryInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StatutoryInstrumentApi apiInstance = new StatutoryInstrumentApi(defaultClient);
    String id = "id_example"; // String | Business items belonging to statutory instrument with the ID specified
    try {
      BusinessItemResourceCollection result = apiInstance.getBusinessItemsByStatutoryInstrumentId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatutoryInstrumentApi#getBusinessItemsByStatutoryInstrumentId");
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
| **id** | **String**| Business items belonging to statutory instrument with the ID specified | |

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
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="getStatutoryInstrumentById"></a>
# **getStatutoryInstrumentById**
> StatutoryInstrumentResource getStatutoryInstrumentById(id)

Returns a statutory instrument by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatutoryInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StatutoryInstrumentApi apiInstance = new StatutoryInstrumentApi(defaultClient);
    String id = "id_example"; // String | Statutory instrument with the ID specified
    try {
      StatutoryInstrumentResource result = apiInstance.getStatutoryInstrumentById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatutoryInstrumentApi#getStatutoryInstrumentById");
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
| **id** | **String**| Statutory instrument with the ID specified | |

### Return type

[**StatutoryInstrumentResource**](StatutoryInstrumentResource.md)

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

<a id="getStatutoryInstruments"></a>
# **getStatutoryInstruments**
> StatutoryInstrumentResourceCollection getStatutoryInstruments(name, statutoryInstrumentType, scheduledDebate, motionToStop, concernsRaisedByCommittee, parliamentaryProcessConcluded, departmentId, layingBodyId, house, skip, take)

Returns a list of statutory instruments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatutoryInstrumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StatutoryInstrumentApi apiInstance = new StatutoryInstrumentApi(defaultClient);
    String name = "name_example"; // String | Statutory instruments with the name specified
    StatutoryInstrumentType statutoryInstrumentType = StatutoryInstrumentType.fromValue("DraftAffirmative"); // StatutoryInstrumentType | Statutory instruments where the statutory instrument type is the type provided
    Boolean scheduledDebate = true; // Boolean | Statutory instrument which contains a scheduled debate
    Boolean motionToStop = true; // Boolean | Statutory instruments which contains a motion to stop
    Boolean concernsRaisedByCommittee = true; // Boolean | Statutory instruments which contains concerns raised by committee
    ParliamentaryProcess parliamentaryProcessConcluded = ParliamentaryProcess.fromValue("NotConcluded"); // ParliamentaryProcess | Statutory instruments where the parliamentary process is concluded or notconcluded
    Integer departmentId = 56; // Integer | Statutory instruments with the department ID specified
    String layingBodyId = "layingBodyId_example"; // String | Statutory instruments with the laying body ID specified
    House house = House.fromValue("Commons"); // House | Statutory instruments laid in the house specified
    Integer skip = 56; // Integer | The number of records to skip from the first, default is 0
    Integer take = 56; // Integer | The number of records to return, default is 20
    try {
      StatutoryInstrumentResourceCollection result = apiInstance.getStatutoryInstruments(name, statutoryInstrumentType, scheduledDebate, motionToStop, concernsRaisedByCommittee, parliamentaryProcessConcluded, departmentId, layingBodyId, house, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatutoryInstrumentApi#getStatutoryInstruments");
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
| **name** | **String**| Statutory instruments with the name specified | [optional] |
| **statutoryInstrumentType** | [**StatutoryInstrumentType**](.md)| Statutory instruments where the statutory instrument type is the type provided | [optional] [enum: DraftAffirmative, DraftNegative, MadeAffirmative, MadeNegative] |
| **scheduledDebate** | **Boolean**| Statutory instrument which contains a scheduled debate | [optional] |
| **motionToStop** | **Boolean**| Statutory instruments which contains a motion to stop | [optional] |
| **concernsRaisedByCommittee** | **Boolean**| Statutory instruments which contains concerns raised by committee | [optional] |
| **parliamentaryProcessConcluded** | [**ParliamentaryProcess**](.md)| Statutory instruments where the parliamentary process is concluded or notconcluded | [optional] [enum: NotConcluded, Concluded] |
| **departmentId** | **Integer**| Statutory instruments with the department ID specified | [optional] |
| **layingBodyId** | **String**| Statutory instruments with the laying body ID specified | [optional] |
| **house** | [**House**](.md)| Statutory instruments laid in the house specified | [optional] [enum: Commons, Lords] |
| **skip** | **Integer**| The number of records to skip from the first, default is 0 | [optional] |
| **take** | **Integer**| The number of records to return, default is 20 | [optional] |

### Return type

[**StatutoryInstrumentResourceCollection**](StatutoryInstrumentResourceCollection.md)

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

