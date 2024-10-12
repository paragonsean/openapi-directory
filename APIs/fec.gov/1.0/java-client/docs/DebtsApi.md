# DebtsApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schedulesScheduleDGet**](DebtsApi.md#schedulesScheduleDGet) | **GET** /schedules/schedule_d/ |  |
| [**schedulesScheduleDSubIdGet**](DebtsApi.md#schedulesScheduleDSubIdGet) | **GET** /schedules/schedule_d/{sub_id}/ |  |


<a id="schedulesScheduleDGet"></a>
# **schedulesScheduleDGet**
> SchedulesScheduleDGetDefaultResponse schedulesScheduleDGet(apiKey, maxPaymentPeriod, minDate, maxImageNumber, maxAmountOutstandingClose, minImageNumber, sortNullOnly, minPaymentPeriod, minAmountIncurred, creditorDebtorName, sortHideNull, candidateId, perPage, minAmountOutstandingBeginning, sort, minAmountOutstandingClose, natureOfDebt, maxAmountIncurred, sortNullsLast, page, committeeId, imageNumber, maxDate, maxAmountOutstandingBeginning)



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.   

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DebtsApi;

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

    DebtsApi apiInstance = new DebtsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Float maxPaymentPeriod = 3.4F; // Float | 
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum load date
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    Float maxAmountOutstandingClose = 3.4F; // Float | 
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Float minPaymentPeriod = 3.4F; // Float | 
    Float minAmountIncurred = 3.4F; // Float | 
    List<String> creditorDebtorName = Arrays.asList(); // List<String> | 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Float minAmountOutstandingBeginning = 3.4F; // Float | 
    String sort = "load_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    Float minAmountOutstandingClose = 3.4F; // Float | 
    String natureOfDebt = "natureOfDebt_example"; // String | 
    Float maxAmountIncurred = 3.4F; // Float | 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum load date
    Float maxAmountOutstandingBeginning = 3.4F; // Float | 
    try {
      SchedulesScheduleDGetDefaultResponse result = apiInstance.schedulesScheduleDGet(apiKey, maxPaymentPeriod, minDate, maxImageNumber, maxAmountOutstandingClose, minImageNumber, sortNullOnly, minPaymentPeriod, minAmountIncurred, creditorDebtorName, sortHideNull, candidateId, perPage, minAmountOutstandingBeginning, sort, minAmountOutstandingClose, natureOfDebt, maxAmountIncurred, sortNullsLast, page, committeeId, imageNumber, maxDate, maxAmountOutstandingBeginning);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DebtsApi#schedulesScheduleDGet");
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
| **maxPaymentPeriod** | **Float**|  | [optional] |
| **minDate** | **LocalDate**| Minimum load date | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **maxAmountOutstandingClose** | **Float**|  | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **minPaymentPeriod** | **Float**|  | [optional] |
| **minAmountIncurred** | **Float**|  | [optional] |
| **creditorDebtorName** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **minAmountOutstandingBeginning** | **Float**|  | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to load_date] |
| **minAmountOutstandingClose** | **Float**|  | [optional] |
| **natureOfDebt** | **String**|  | [optional] |
| **maxAmountIncurred** | **Float**|  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum load date | [optional] |
| **maxAmountOutstandingBeginning** | **Float**|  | [optional] |

### Return type

[**SchedulesScheduleDGetDefaultResponse**](SchedulesScheduleDGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleDSubIdGet"></a>
# **schedulesScheduleDSubIdGet**
> SchedulesScheduleDGetDefaultResponse schedulesScheduleDSubIdGet(apiKey, subId, page, sortHideNull, perPage, sortNullOnly, sort, sortNullsLast)



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.   

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DebtsApi;

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

    DebtsApi apiInstance = new DebtsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String subId = "subId_example"; // String | 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String sort = "load_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    try {
      SchedulesScheduleDGetDefaultResponse result = apiInstance.schedulesScheduleDSubIdGet(apiKey, subId, page, sortHideNull, perPage, sortNullOnly, sort, sortNullsLast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DebtsApi#schedulesScheduleDSubIdGet");
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
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to load_date] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |

### Return type

[**SchedulesScheduleDGetDefaultResponse**](SchedulesScheduleDGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

