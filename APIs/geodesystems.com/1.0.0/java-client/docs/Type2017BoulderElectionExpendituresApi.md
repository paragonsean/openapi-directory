# Type2017BoulderElectionExpendituresApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**search2017BoulderElectionExpenditures**](Type2017BoulderElectionExpendituresApi.md#search2017BoulderElectionExpenditures) | **GET** /repository/search/type/2017_boulder_election_expenditures | Search API for &#39;2017 Boulder Election Expenditures&#39; entry type |


<a id="search2017BoulderElectionExpenditures"></a>
# **search2017BoulderElectionExpenditures**
> search2017BoulderElectionExpenditures(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDb2017BoulderElectionExpendituresCommittee, searchDb2017BoulderElectionExpendituresTransactionDate, searchDb2017BoulderElectionExpendituresName, searchDb2017BoulderElectionExpendituresStreet, searchDb2017BoulderElectionExpendituresCity, searchDb2017BoulderElectionExpendituresState, searchDb2017BoulderElectionExpendituresZip, searchDb2017BoulderElectionExpendituresExpenditure, searchDb2017BoulderElectionExpendituresPurpose)

Search API for &#39;2017 Boulder Election Expenditures&#39; entry type

API to search for entries of type 2017 Boulder Election Expenditures

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Type2017BoulderElectionExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    Type2017BoulderElectionExpendituresApi apiInstance = new Type2017BoulderElectionExpendituresApi(defaultClient);
    String text = "text_example"; // String | Search text
    String name = "name_example"; // String | Search name
    String description = "description_example"; // String | Search description
    OffsetDateTime fromdate = OffsetDateTime.now(); // OffsetDateTime | From date
    OffsetDateTime todate = OffsetDateTime.now(); // OffsetDateTime | To date
    OffsetDateTime createdateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive create date from
    OffsetDateTime createdateTo = OffsetDateTime.now(); // OffsetDateTime | Archive create date to
    OffsetDateTime changedateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive change date from
    OffsetDateTime changedateTo = OffsetDateTime.now(); // OffsetDateTime | Archive change date to
    String group = "group_example"; // String | Parent entry
    String filesuffix = "filesuffix_example"; // String | File suffix
    Float maxlatitude = 3.4F; // Float | Northern bounds of search
    Float minlongitude = 3.4F; // Float | Western bounds of search
    Float minlatitude = 3.4F; // Float | Southern bounds of search
    Float maxlongitude = 3.4F; // Float | Eastern bounds of search
    Integer max = 56; // Integer | Max number of results
    Integer skip = 56; // Integer | Number to skip
    String searchDb2017BoulderElectionExpendituresCommittee = "searchDb2017BoulderElectionExpendituresCommittee_example"; // String | Committee
    String searchDb2017BoulderElectionExpendituresTransactionDate = "searchDb2017BoulderElectionExpendituresTransactionDate_example"; // String | Transaction Date
    String searchDb2017BoulderElectionExpendituresName = "searchDb2017BoulderElectionExpendituresName_example"; // String | Name
    String searchDb2017BoulderElectionExpendituresStreet = "searchDb2017BoulderElectionExpendituresStreet_example"; // String | Street
    String searchDb2017BoulderElectionExpendituresCity = "searchDb2017BoulderElectionExpendituresCity_example"; // String | City
    String searchDb2017BoulderElectionExpendituresState = "searchDb2017BoulderElectionExpendituresState_example"; // String | State
    String searchDb2017BoulderElectionExpendituresZip = "searchDb2017BoulderElectionExpendituresZip_example"; // String | Zip
    Double searchDb2017BoulderElectionExpendituresExpenditure = 3.4D; // Double | Expenditure
    String searchDb2017BoulderElectionExpendituresPurpose = "searchDb2017BoulderElectionExpendituresPurpose_example"; // String | Purpose
    try {
      apiInstance.search2017BoulderElectionExpenditures(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDb2017BoulderElectionExpendituresCommittee, searchDb2017BoulderElectionExpendituresTransactionDate, searchDb2017BoulderElectionExpendituresName, searchDb2017BoulderElectionExpendituresStreet, searchDb2017BoulderElectionExpendituresCity, searchDb2017BoulderElectionExpendituresState, searchDb2017BoulderElectionExpendituresZip, searchDb2017BoulderElectionExpendituresExpenditure, searchDb2017BoulderElectionExpendituresPurpose);
    } catch (ApiException e) {
      System.err.println("Exception when calling Type2017BoulderElectionExpendituresApi#search2017BoulderElectionExpenditures");
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
| **text** | **String**| Search text | [optional] |
| **name** | **String**| Search name | [optional] |
| **description** | **String**| Search description | [optional] |
| **fromdate** | **OffsetDateTime**| From date | [optional] |
| **todate** | **OffsetDateTime**| To date | [optional] |
| **createdateFrom** | **OffsetDateTime**| Archive create date from | [optional] |
| **createdateTo** | **OffsetDateTime**| Archive create date to | [optional] |
| **changedateFrom** | **OffsetDateTime**| Archive change date from | [optional] |
| **changedateTo** | **OffsetDateTime**| Archive change date to | [optional] |
| **group** | **String**| Parent entry | [optional] |
| **filesuffix** | **String**| File suffix | [optional] |
| **maxlatitude** | **Float**| Northern bounds of search | [optional] |
| **minlongitude** | **Float**| Western bounds of search | [optional] |
| **minlatitude** | **Float**| Southern bounds of search | [optional] |
| **maxlongitude** | **Float**| Eastern bounds of search | [optional] |
| **max** | **Integer**| Max number of results | [optional] |
| **skip** | **Integer**| Number to skip | [optional] |
| **searchDb2017BoulderElectionExpendituresCommittee** | **String**| Committee | [optional] |
| **searchDb2017BoulderElectionExpendituresTransactionDate** | **String**| Transaction Date | [optional] |
| **searchDb2017BoulderElectionExpendituresName** | **String**| Name | [optional] |
| **searchDb2017BoulderElectionExpendituresStreet** | **String**| Street | [optional] |
| **searchDb2017BoulderElectionExpendituresCity** | **String**| City | [optional] |
| **searchDb2017BoulderElectionExpendituresState** | **String**| State | [optional] |
| **searchDb2017BoulderElectionExpendituresZip** | **String**| Zip | [optional] |
| **searchDb2017BoulderElectionExpendituresExpenditure** | **Double**| Expenditure | [optional] |
| **searchDb2017BoulderElectionExpendituresPurpose** | **String**| Purpose | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

