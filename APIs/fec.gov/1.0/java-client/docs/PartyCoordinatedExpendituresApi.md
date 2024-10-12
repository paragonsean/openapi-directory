# PartyCoordinatedExpendituresApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schedulesScheduleFGet**](PartyCoordinatedExpendituresApi.md#schedulesScheduleFGet) | **GET** /schedules/schedule_f/ |  |
| [**schedulesScheduleFSubIdGet**](PartyCoordinatedExpendituresApi.md#schedulesScheduleFSubIdGet) | **GET** /schedules/schedule_f/{sub_id}/ |  |


<a id="schedulesScheduleFGet"></a>
# **schedulesScheduleFGet**
> SchedulesScheduleFGetDefaultResponse schedulesScheduleFGet(apiKey, minDate, maxImageNumber, cycle, minImageNumber, sortNullOnly, payeeName, minAmount, perPage, candidateId, sortHideNull, lineNumber, sort, sortNullsLast, page, committeeId, imageNumber, maxDate, maxAmount)



 Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartyCoordinatedExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PartyCoordinatedExpendituresApi apiInstance = new PartyCoordinatedExpendituresApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum date
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    List<String> payeeName = Arrays.asList(); // List<String> | 
    String minAmount = "minAmount_example"; // String | Filter for all amounts greater than a value.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    String lineNumber = "lineNumber_example"; // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
    String sort = "expenditure_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum date
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    try {
      SchedulesScheduleFGetDefaultResponse result = apiInstance.schedulesScheduleFGet(apiKey, minDate, maxImageNumber, cycle, minImageNumber, sortNullOnly, payeeName, minAmount, perPage, candidateId, sortHideNull, lineNumber, sort, sortNullsLast, page, committeeId, imageNumber, maxDate, maxAmount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartyCoordinatedExpendituresApi#schedulesScheduleFGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **minDate** | **LocalDate**| Minimum date | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **payeeName** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to expenditure_date] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum date | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |

### Return type

[**SchedulesScheduleFGetDefaultResponse**](SchedulesScheduleFGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleFSubIdGet"></a>
# **schedulesScheduleFSubIdGet**
> SchedulesScheduleFGetDefaultResponse schedulesScheduleFSubIdGet(apiKey, subId, page, perPage)



 Schedule F, it shows all special expenditures a national or state party committee makes in connection with the general election campaigns of federal candidates.  These coordinated party expenditures do not count against the contribution limits but are subject to other limits, these limits are detailed in Chapter 7 of the FEC Campaign Guide for Political Party Committees. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartyCoordinatedExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyHeaderAuth
    ApiKeyAuth ApiKeyHeaderAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyHeaderAuth");
    ApiKeyHeaderAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyHeaderAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: ApiKeyQueryAuth
    ApiKeyAuth ApiKeyQueryAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyQueryAuth");
    ApiKeyQueryAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyQueryAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PartyCoordinatedExpendituresApi apiInstance = new PartyCoordinatedExpendituresApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String subId = "subId_example"; // String | 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    try {
      SchedulesScheduleFGetDefaultResponse result = apiInstance.schedulesScheduleFSubIdGet(apiKey, subId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartyCoordinatedExpendituresApi#schedulesScheduleFSubIdGet");
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
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **subId** | **String**|  | |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |

### Return type

[**SchedulesScheduleFGetDefaultResponse**](SchedulesScheduleFGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

