# EarlyDayMotionsApi

All URIs are relative to *http://oralquestionsandmotions-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**earlyDayMotionsListGet**](EarlyDayMotionsApi.md#earlyDayMotionsListGet) | **GET** /EarlyDayMotions/list | Returns a list of Early Day Motions |
| [**publishedEarlyDayMotionGet**](EarlyDayMotionsApi.md#publishedEarlyDayMotionGet) | **GET** /EarlyDayMotion/{id} | Returns a single Early Day Motion by ID |


<a id="earlyDayMotionsListGet"></a>
# **earlyDayMotionsListGet**
> ApiResponseListPublishedWrittenQuestion earlyDayMotionsListGet(parametersEdmIds, parametersUINWithAmendmentSuffix, parametersSearchTerm, parametersCurrentStatusDateStart, parametersCurrentStatusDateEnd, parametersIsPrayer, parametersMemberId, parametersIncludeSponsoredByMember, parametersTabledStartDate, parametersTabledEndDate, parametersStatuses, parametersOrderBy, parametersSkip, parametersTake)

Returns a list of Early Day Motions

Get a list of Early Day Motions which meet the specified criteria. Only supports Published and Withdrawn status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EarlyDayMotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://oralquestionsandmotions-api.parliament.uk");

    EarlyDayMotionsApi apiInstance = new EarlyDayMotionsApi(defaultClient);
    List<Integer> parametersEdmIds = Arrays.asList(); // List<Integer> | Early Day Motions with an ID in the list provided.
    String parametersUINWithAmendmentSuffix = "parametersUINWithAmendmentSuffix_example"; // String | Early Day Motions with an UINWithAmendmentSuffix provided.
    String parametersSearchTerm = "parametersSearchTerm_example"; // String | Early Day Motions where the title includes the search term provided.
    OffsetDateTime parametersCurrentStatusDateStart = OffsetDateTime.now(); // OffsetDateTime | Early Day Motions where the current status has been set on or after the date provided. Date format YYYY-MM-DD.
    OffsetDateTime parametersCurrentStatusDateEnd = OffsetDateTime.now(); // OffsetDateTime | Early Day Motions where the current status has been set on or before the date provided. Date format YYYY-MM-DD.
    Boolean parametersIsPrayer = true; // Boolean | Early Day Motions which are a prayer against a Negative Statutory Instrument.
    Integer parametersMemberId = 56; // Integer | Return Early Day Motions tabled by Member with ID provided.
    Boolean parametersIncludeSponsoredByMember = true; // Boolean | Include Early Day Motions sponsored by Member specified
    OffsetDateTime parametersTabledStartDate = OffsetDateTime.now(); // OffsetDateTime | Early Day Motions where the date tabled is on or after the date provided. Date format YYYY-MM-DD.
    OffsetDateTime parametersTabledEndDate = OffsetDateTime.now(); // OffsetDateTime | Early Day Motions where the date tabled is on or before the date provided. Date format YYYY-MM-DD.
    List<String> parametersStatuses = Arrays.asList(); // List<String> | Early Day Motions where current status is in the selected list.
    String parametersOrderBy = "DateTabledAsc"; // String | Order results by date tabled, title or signature count. Default is date tabled.
    Integer parametersSkip = 56; // Integer | The number of records to skip from the first, default is 0.
    Integer parametersTake = 56; // Integer | The number of records to return, default is 25, maximum is 100.
    try {
      ApiResponseListPublishedWrittenQuestion result = apiInstance.earlyDayMotionsListGet(parametersEdmIds, parametersUINWithAmendmentSuffix, parametersSearchTerm, parametersCurrentStatusDateStart, parametersCurrentStatusDateEnd, parametersIsPrayer, parametersMemberId, parametersIncludeSponsoredByMember, parametersTabledStartDate, parametersTabledEndDate, parametersStatuses, parametersOrderBy, parametersSkip, parametersTake);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyDayMotionsApi#earlyDayMotionsListGet");
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
| **parametersEdmIds** | [**List&lt;Integer&gt;**](Integer.md)| Early Day Motions with an ID in the list provided. | [optional] |
| **parametersUINWithAmendmentSuffix** | **String**| Early Day Motions with an UINWithAmendmentSuffix provided. | [optional] |
| **parametersSearchTerm** | **String**| Early Day Motions where the title includes the search term provided. | [optional] |
| **parametersCurrentStatusDateStart** | **OffsetDateTime**| Early Day Motions where the current status has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersCurrentStatusDateEnd** | **OffsetDateTime**| Early Day Motions where the current status has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersIsPrayer** | **Boolean**| Early Day Motions which are a prayer against a Negative Statutory Instrument. | [optional] |
| **parametersMemberId** | **Integer**| Return Early Day Motions tabled by Member with ID provided. | [optional] |
| **parametersIncludeSponsoredByMember** | **Boolean**| Include Early Day Motions sponsored by Member specified | [optional] |
| **parametersTabledStartDate** | **OffsetDateTime**| Early Day Motions where the date tabled is on or after the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersTabledEndDate** | **OffsetDateTime**| Early Day Motions where the date tabled is on or before the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersStatuses** | [**List&lt;String&gt;**](String.md)| Early Day Motions where current status is in the selected list. | [optional] [enum: Published, Withdrawn] |
| **parametersOrderBy** | **String**| Order results by date tabled, title or signature count. Default is date tabled. | [optional] [enum: DateTabledAsc, DateTabledDesc, TitleAsc, TitleDesc, SignatureCountAsc, SignatureCountDesc] |
| **parametersSkip** | **Integer**| The number of records to skip from the first, default is 0. | [optional] |
| **parametersTake** | **Integer**| The number of records to return, default is 25, maximum is 100. | [optional] |

### Return type

[**ApiResponseListPublishedWrittenQuestion**](ApiResponseListPublishedWrittenQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |

<a id="publishedEarlyDayMotionGet"></a>
# **publishedEarlyDayMotionGet**
> ApiResponseListPublishedWrittenQuestion publishedEarlyDayMotionGet(id)

Returns a single Early Day Motion by ID

Get a single Early Day Motion which has the ID specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EarlyDayMotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://oralquestionsandmotions-api.parliament.uk");

    EarlyDayMotionsApi apiInstance = new EarlyDayMotionsApi(defaultClient);
    Integer id = 56; // Integer | Early Day Motion with the ID specified.
    try {
      ApiResponseListPublishedWrittenQuestion result = apiInstance.publishedEarlyDayMotionGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyDayMotionsApi#publishedEarlyDayMotionGet");
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
| **id** | **Integer**| Early Day Motion with the ID specified. | |

### Return type

[**ApiResponseListPublishedWrittenQuestion**](ApiResponseListPublishedWrittenQuestion.md)

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

