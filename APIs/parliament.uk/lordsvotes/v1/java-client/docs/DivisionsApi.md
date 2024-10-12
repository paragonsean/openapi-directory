# DivisionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataDivisionsDivisionIdGet**](DivisionsApi.md#dataDivisionsDivisionIdGet) | **GET** /data/Divisions/{divisionId} | Return a Division |
| [**dataDivisionsGroupedbypartyGet**](DivisionsApi.md#dataDivisionsGroupedbypartyGet) | **GET** /data/Divisions/groupedbyparty | Return Divisions results grouped by party |
| [**dataDivisionsMembervotingGet**](DivisionsApi.md#dataDivisionsMembervotingGet) | **GET** /data/Divisions/membervoting | Return voting records for a Member |
| [**dataDivisionsSearchGet**](DivisionsApi.md#dataDivisionsSearchGet) | **GET** /data/Divisions/search | Return a list of Divisions |
| [**dataDivisionsSearchTotalResultsGet**](DivisionsApi.md#dataDivisionsSearchTotalResultsGet) | **GET** /data/Divisions/searchTotalResults | Return total results count |


<a id="dataDivisionsDivisionIdGet"></a>
# **dataDivisionsDivisionIdGet**
> DivisionViewModel dataDivisionsDivisionIdGet(divisionId)

Return a Division

Get a single Division which has the Id specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DivisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    Integer divisionId = 56; // Integer | Division with ID specified
    try {
      DivisionViewModel result = apiInstance.dataDivisionsDivisionIdGet(divisionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#dataDivisionsDivisionIdGet");
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
| **divisionId** | **Integer**| Division with ID specified | |

### Return type

[**DivisionViewModel**](DivisionViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Division with id matching given divisionId |  -  |
| **400** | divisionId was not valid |  -  |
| **404** | Division with given divisionId was not found |  -  |
| **503** | Temporary error occured when trying to get division |  -  |

<a id="dataDivisionsGroupedbypartyGet"></a>
# **dataDivisionsGroupedbypartyGet**
> DivisionGroupByPartyViewModel dataDivisionsGroupedbypartyGet(searchTerm, memberId, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare)

Return Divisions results grouped by party

Get a list of Divisions which contain grouped by party

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DivisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Divisions containing search term within title or number
    Integer memberId = 56; // Integer | Divisions returning Member with Member ID voting records
    Boolean includeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer divisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    Comparators totalVotesCastComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer totalVotesCastValueToCompare = 56; // Integer | value to compare to with the operator provided
    Comparators majorityComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer majorityValueToCompare = 56; // Integer | value to compare to with the operator provided
    try {
      DivisionGroupByPartyViewModel result = apiInstance.dataDivisionsGroupedbypartyGet(searchTerm, memberId, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#dataDivisionsGroupedbypartyGet");
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
| **searchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **memberId** | **Integer**| Divisions returning Member with Member ID voting records | [optional] |
| **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **startDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **endDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **divisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |
| **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **totalVotesCastValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |
| **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **majorityValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |

### Return type

[**DivisionGroupByPartyViewModel**](DivisionGroupByPartyViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of divisions with votes grouped by party |  -  |
| **400** | A parameter was not valid |  -  |

<a id="dataDivisionsMembervotingGet"></a>
# **dataDivisionsMembervotingGet**
> MemberVotingRecordViewModel dataDivisionsMembervotingGet(memberId, searchTerm, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare, skip, take)

Return voting records for a Member

Get a list of voting records for a Member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DivisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    Integer memberId = 56; // Integer | Id number of a Member whose voting records are to be returned
    String searchTerm = "searchTerm_example"; // String | Divisions containing search term within title or number
    Boolean includeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer divisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    Comparators totalVotesCastComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer totalVotesCastValueToCompare = 56; // Integer | value to compare to with the operator provided
    Comparators majorityComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer majorityValueToCompare = 56; // Integer | value to compare to with the operator provided
    Integer skip = 0; // Integer | The number of records to skip. Must be a positive integer. Default is 0
    Integer take = 25; // Integer | The number of records to return per page. Must be more than 0. Default is 25
    try {
      MemberVotingRecordViewModel result = apiInstance.dataDivisionsMembervotingGet(memberId, searchTerm, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#dataDivisionsMembervotingGet");
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
| **memberId** | **Integer**| Id number of a Member whose voting records are to be returned | |
| **searchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **startDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **endDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **divisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |
| **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **totalVotesCastValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |
| **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **majorityValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |
| **skip** | **Integer**| The number of records to skip. Must be a positive integer. Default is 0 | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return per page. Must be more than 0. Default is 25 | [optional] [default to 25] |

### Return type

[**MemberVotingRecordViewModel**](MemberVotingRecordViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of voting records for a member |  -  |
| **400** | A parameter was not valid |  -  |
| **503** | Temporary error occured when trying to get division |  -  |

<a id="dataDivisionsSearchGet"></a>
# **dataDivisionsSearchGet**
> List&lt;DivisionViewModel&gt; dataDivisionsSearchGet(searchTerm, memberId, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare, skip, take)

Return a list of Divisions

Get a list of Divisions which meet the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DivisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Divisions containing search term within title or number
    Integer memberId = 56; // Integer | Divisions returning Member with Member ID voting records
    Boolean includeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer divisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    Comparators totalVotesCastComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer totalVotesCastValueToCompare = 56; // Integer | value to compare to with the operator provided
    Comparators majorityComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer majorityValueToCompare = 56; // Integer | value to compare to with the operator provided
    Integer skip = 0; // Integer | The number of records to skip. Must be a positive integer. Default is 0
    Integer take = 25; // Integer | The number of records to return per page. Must be more than 0. Default is 25
    try {
      List<DivisionViewModel> result = apiInstance.dataDivisionsSearchGet(searchTerm, memberId, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#dataDivisionsSearchGet");
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
| **searchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **memberId** | **Integer**| Divisions returning Member with Member ID voting records | [optional] |
| **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **startDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **endDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **divisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |
| **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **totalVotesCastValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |
| **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **majorityValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |
| **skip** | **Integer**| The number of records to skip. Must be a positive integer. Default is 0 | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return per page. Must be more than 0. Default is 25 | [optional] [default to 25] |

### Return type

[**List&lt;DivisionViewModel&gt;**](DivisionViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of divisions matching specified parameters |  -  |
| **400** | A parameter was not valid |  -  |
| **503** | Temporary error occured when trying to get division |  -  |

<a id="dataDivisionsSearchTotalResultsGet"></a>
# **dataDivisionsSearchTotalResultsGet**
> Integer dataDivisionsSearchTotalResultsGet(searchTerm, memberId, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare)

Return total results count

Get total count of Divisions meeting the specified query, useful for paging lists etc...

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DivisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Divisions containing search term within title or number
    Integer memberId = 56; // Integer | Divisions returning Member with Member ID voting records
    Boolean includeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer divisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    Comparators totalVotesCastComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer totalVotesCastValueToCompare = 56; // Integer | value to compare to with the operator provided
    Comparators majorityComparator = Comparators.fromValue("LessThan"); // Comparators | comparison operator to use
    Integer majorityValueToCompare = 56; // Integer | value to compare to with the operator provided
    try {
      Integer result = apiInstance.dataDivisionsSearchTotalResultsGet(searchTerm, memberId, includeWhenMemberWasTeller, startDate, endDate, divisionNumber, totalVotesCastComparator, totalVotesCastValueToCompare, majorityComparator, majorityValueToCompare);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#dataDivisionsSearchTotalResultsGet");
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
| **searchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **memberId** | **Integer**| Divisions returning Member with Member ID voting records | [optional] |
| **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **startDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **endDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **divisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |
| **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **totalVotesCastValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |
| **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] [enum: LessThan, LessThanOrEqualTo, EqualTo, GreaterThanOrEqualTo, GreaterThan] |
| **majorityValueToCompare** | **Integer**| value to compare to with the operator provided | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Division with id matching given divisionId |  -  |
| **400** | divisionId was not valid |  -  |

