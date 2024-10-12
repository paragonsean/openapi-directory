# LoansApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schedulesScheduleCGet**](LoansApi.md#schedulesScheduleCGet) | **GET** /schedules/schedule_c/ |  |
| [**schedulesScheduleCSubIdGet**](LoansApi.md#schedulesScheduleCSubIdGet) | **GET** /schedules/schedule_c/{sub_id}/ |  |


<a id="schedulesScheduleCGet"></a>
# **schedulesScheduleCGet**
> SchedulesScheduleCGetDefaultResponse schedulesScheduleCGet(apiKey, minPaymentToDate, maxImageNumber, minImageNumber, maxIncurredDate, sortNullOnly, lastIndex, sortHideNull, minAmount, perPage, loanSourceName, lineNumber, sort, maxPaymentToDate, candidateName, sortNullsLast, page, committeeId, imageNumber, minIncurredDate, maxAmount)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoansApi;

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

    LoansApi apiInstance = new LoansApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Integer minPaymentToDate = 56; // Integer |  Minimum payment to date 
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    LocalDate maxIncurredDate = LocalDate.now(); // LocalDate |  Maximum incurred date 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer lastIndex = 56; // Integer | Index of last result from previous page
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    String minAmount = "minAmount_example"; // String |  Filter for all amounts greater than a value. 
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> loanSourceName = Arrays.asList(); // List<String> | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate
    String lineNumber = "lineNumber_example"; // String |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. 
    String sort = "-incurred_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    Integer maxPaymentToDate = 56; // Integer |  Maximum payment to date 
    List<String> candidateName = Arrays.asList(); // List<String> | Name of candidate running for office
    Boolean sortNullsLast = true; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate minIncurredDate = LocalDate.now(); // LocalDate |  Minimum incurred date 
    String maxAmount = "maxAmount_example"; // String |  Filter for all amounts less than a value. 
    try {
      SchedulesScheduleCGetDefaultResponse result = apiInstance.schedulesScheduleCGet(apiKey, minPaymentToDate, maxImageNumber, minImageNumber, maxIncurredDate, sortNullOnly, lastIndex, sortHideNull, minAmount, perPage, loanSourceName, lineNumber, sort, maxPaymentToDate, candidateName, sortNullsLast, page, committeeId, imageNumber, minIncurredDate, maxAmount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoansApi#schedulesScheduleCGet");
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
| **minPaymentToDate** | **Integer**|  Minimum payment to date  | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **maxIncurredDate** | **LocalDate**|  Maximum incurred date  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **lastIndex** | **Integer**| Index of last result from previous page | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **minAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **loanSourceName** | [**List&lt;String&gt;**](String.md)| Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate | [optional] |
| **lineNumber** | **String**|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -incurred_date] |
| **maxPaymentToDate** | **Integer**|  Maximum payment to date  | [optional] |
| **candidateName** | [**List&lt;String&gt;**](String.md)| Name of candidate running for office | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to true] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **minIncurredDate** | **LocalDate**|  Minimum incurred date  | [optional] |
| **maxAmount** | **String**|  Filter for all amounts less than a value.  | [optional] |

### Return type

[**SchedulesScheduleCGetDefaultResponse**](SchedulesScheduleCGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleCSubIdGet"></a>
# **schedulesScheduleCSubIdGet**
> SchedulesScheduleCGetDefaultResponse schedulesScheduleCSubIdGet(apiKey, subId, page, sortHideNull, perPage, sortNullOnly, sort, sortNullsLast)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoansApi;

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

    LoansApi apiInstance = new LoansApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String subId = "subId_example"; // String | 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    try {
      SchedulesScheduleCGetDefaultResponse result = apiInstance.schedulesScheduleCSubIdGet(apiKey, subId, page, sortHideNull, perPage, sortNullOnly, sort, sortNullsLast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoansApi#schedulesScheduleCSubIdGet");
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
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |

### Return type

[**SchedulesScheduleCGetDefaultResponse**](SchedulesScheduleCGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

