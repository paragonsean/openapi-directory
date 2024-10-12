# DivisionsApi

All URIs are relative to *http://commonsvotes-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**divisionsGetDivisionById**](DivisionsApi.md#divisionsGetDivisionById) | **GET** /data/division/{divisionId}.{format} | Return a Division |
| [**divisionsGetDivisionsGroupsByParty**](DivisionsApi.md#divisionsGetDivisionsGroupsByParty) | **GET** /data/divisions.{format}/groupedbyparty | Return Divisions results grouped by party |
| [**divisionsGetVotingRecordsForMember**](DivisionsApi.md#divisionsGetVotingRecordsForMember) | **GET** /data/divisions.{format}/membervoting | Return voting records for a Member |
| [**divisionsSearchDivisions**](DivisionsApi.md#divisionsSearchDivisions) | **GET** /data/divisions.{format}/search | Return a list of Divisions |
| [**divisionsSearchTotalResults**](DivisionsApi.md#divisionsSearchTotalResults) | **GET** /data/divisions.{format}/searchTotalResults | Return total results count |


<a id="divisionsGetDivisionById"></a>
# **divisionsGetDivisionById**
> PublishedDivision divisionsGetDivisionById(divisionId, format)

Return a Division

Single Division which has the specified Id

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
    defaultClient.setBasePath("http://commonsvotes-api.parliament.uk");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    Integer divisionId = 56; // Integer | Id number of a Division whose records are to be returned
    String format = "format_example"; // String | xml or json
    try {
      PublishedDivision result = apiInstance.divisionsGetDivisionById(divisionId, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#divisionsGetDivisionById");
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
| **divisionId** | **Integer**| Id number of a Division whose records are to be returned | |
| **format** | **String**| xml or json | |

### Return type

[**PublishedDivision**](PublishedDivision.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **404** | NotFound |  -  |

<a id="divisionsGetDivisionsGroupsByParty"></a>
# **divisionsGetDivisionsGroupsByParty**
> List&lt;DivisionGroupedByParty&gt; divisionsGetDivisionsGroupsByParty(format, queryParametersSearchTerm, queryParametersMemberId, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber)

Return Divisions results grouped by party

Division results which meet the specified criteria grouped by parties

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
    defaultClient.setBasePath("http://commonsvotes-api.parliament.uk");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    String format = "format_example"; // String | xml or json
    String queryParametersSearchTerm = "queryParametersSearchTerm_example"; // String | Divisions containing search term within title or number
    Integer queryParametersMemberId = 56; // Integer | Divisions returning Member with Member ID voting records
    Boolean queryParametersIncludeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime queryParametersStartDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime queryParametersEndDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer queryParametersDivisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    try {
      List<DivisionGroupedByParty> result = apiInstance.divisionsGetDivisionsGroupsByParty(format, queryParametersSearchTerm, queryParametersMemberId, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#divisionsGetDivisionsGroupsByParty");
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
| **format** | **String**| xml or json | |
| **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **queryParametersMemberId** | **Integer**| Divisions returning Member with Member ID voting records | [optional] |
| **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **queryParametersStartDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersEndDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersDivisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |

### Return type

[**List&lt;DivisionGroupedByParty&gt;**](DivisionGroupedByParty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |

<a id="divisionsGetVotingRecordsForMember"></a>
# **divisionsGetVotingRecordsForMember**
> List&lt;MemberVotingRecord&gt; divisionsGetVotingRecordsForMember(format, queryParametersMemberId, queryParametersSkip, queryParametersTake, queryParametersSearchTerm, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber)

Return voting records for a Member

List of voting records for a member which meet the specified criteria.

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
    defaultClient.setBasePath("http://commonsvotes-api.parliament.uk");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    String format = "format_example"; // String | xml or json
    Integer queryParametersMemberId = 56; // Integer | Id number of a Member whose voting records are to be returned
    Integer queryParametersSkip = 56; // Integer | The number of records to skip. Default is 0
    Integer queryParametersTake = 56; // Integer | The number of records to return per page. Default is 25
    String queryParametersSearchTerm = "queryParametersSearchTerm_example"; // String | Divisions containing search term within title or number
    Boolean queryParametersIncludeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime queryParametersStartDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime queryParametersEndDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer queryParametersDivisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    try {
      List<MemberVotingRecord> result = apiInstance.divisionsGetVotingRecordsForMember(format, queryParametersMemberId, queryParametersSkip, queryParametersTake, queryParametersSearchTerm, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#divisionsGetVotingRecordsForMember");
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
| **format** | **String**| xml or json | |
| **queryParametersMemberId** | **Integer**| Id number of a Member whose voting records are to be returned | |
| **queryParametersSkip** | **Integer**| The number of records to skip. Default is 0 | [optional] |
| **queryParametersTake** | **Integer**| The number of records to return per page. Default is 25 | [optional] |
| **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **queryParametersStartDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersEndDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersDivisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |

### Return type

[**List&lt;MemberVotingRecord&gt;**](MemberVotingRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |

<a id="divisionsSearchDivisions"></a>
# **divisionsSearchDivisions**
> List&lt;PublishedDivision&gt; divisionsSearchDivisions(format, queryParametersSkip, queryParametersTake, queryParametersSearchTerm, queryParametersMemberId, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber)

Return a list of Divisions

List of Divisions which meet the specified criteria

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
    defaultClient.setBasePath("http://commonsvotes-api.parliament.uk");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    String format = "format_example"; // String | json or xml
    Integer queryParametersSkip = 56; // Integer | The number of records to skip. Default is 0
    Integer queryParametersTake = 56; // Integer | The number of records to return per page. Default is 25
    String queryParametersSearchTerm = "queryParametersSearchTerm_example"; // String | Divisions containing search term within title or number
    Integer queryParametersMemberId = 56; // Integer | Divisions returning Member with Member ID voting records
    Boolean queryParametersIncludeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime queryParametersStartDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime queryParametersEndDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer queryParametersDivisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    try {
      List<PublishedDivision> result = apiInstance.divisionsSearchDivisions(format, queryParametersSkip, queryParametersTake, queryParametersSearchTerm, queryParametersMemberId, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#divisionsSearchDivisions");
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
| **format** | **String**| json or xml | |
| **queryParametersSkip** | **Integer**| The number of records to skip. Default is 0 | [optional] |
| **queryParametersTake** | **Integer**| The number of records to return per page. Default is 25 | [optional] |
| **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **queryParametersMemberId** | **Integer**| Divisions returning Member with Member ID voting records | [optional] |
| **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **queryParametersStartDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersEndDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersDivisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |

### Return type

[**List&lt;PublishedDivision&gt;**](PublishedDivision.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |

<a id="divisionsSearchTotalResults"></a>
# **divisionsSearchTotalResults**
> Integer divisionsSearchTotalResults(format, queryParametersSearchTerm, queryParametersMemberId, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber)

Return total results count

Total count of Divisions meeting the specified criteria

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
    defaultClient.setBasePath("http://commonsvotes-api.parliament.uk");

    DivisionsApi apiInstance = new DivisionsApi(defaultClient);
    String format = "format_example"; // String | json or xml
    String queryParametersSearchTerm = "queryParametersSearchTerm_example"; // String | Divisions containing search term within title or number
    Integer queryParametersMemberId = 56; // Integer | Divisions returning Member with Member ID voting records
    Boolean queryParametersIncludeWhenMemberWasTeller = true; // Boolean | Divisions where member was a teller as well as if they actually voted
    OffsetDateTime queryParametersStartDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
    OffsetDateTime queryParametersEndDate = OffsetDateTime.now(); // OffsetDateTime | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
    Integer queryParametersDivisionNumber = 56; // Integer | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
    try {
      Integer result = apiInstance.divisionsSearchTotalResults(format, queryParametersSearchTerm, queryParametersMemberId, queryParametersIncludeWhenMemberWasTeller, queryParametersStartDate, queryParametersEndDate, queryParametersDivisionNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DivisionsApi#divisionsSearchTotalResults");
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
| **format** | **String**| json or xml | |
| **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] |
| **queryParametersMemberId** | **Integer**| Divisions returning Member with Member ID voting records | [optional] |
| **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] |
| **queryParametersStartDate** | **OffsetDateTime**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersEndDate** | **OffsetDateTime**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] |
| **queryParametersDivisionNumber** | **Integer**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |

