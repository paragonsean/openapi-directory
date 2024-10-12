# EfilingApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**efileFilingsGet**](EfilingApi.md#efileFilingsGet) | **GET** /efile/filings/ |  |
| [**efileReportsHouseSenateGet**](EfilingApi.md#efileReportsHouseSenateGet) | **GET** /efile/reports/house-senate/ |  |
| [**efileReportsPacPartyGet**](EfilingApi.md#efileReportsPacPartyGet) | **GET** /efile/reports/pac-party/ |  |
| [**efileReportsPresidentialGet**](EfilingApi.md#efileReportsPresidentialGet) | **GET** /efile/reports/presidential/ |  |


<a id="efileFilingsGet"></a>
# **efileFilingsGet**
> EFilingsPage efileFilingsGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler)



Basic information about electronic files coming into the FEC, posted as they are received.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EfilingApi;

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

    EfilingApi apiInstance = new EfilingApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    LocalDate maxReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<Integer> fileNumber = Arrays.asList(); // List<Integer> | Filing ID number
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "-receipt_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> qFiler = Arrays.asList(); // List<String> |  Keyword search for filer name or ID 
    try {
      EFilingsPage result = apiInstance.efileFilingsGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EfilingApi#efileFilingsGet");
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
| **minReceiptDate** | **LocalDate**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **maxReceiptDate** | **LocalDate**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **fileNumber** | [**List&lt;Integer&gt;**](Integer.md)| Filing ID number | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -receipt_date] |
| **qFiler** | [**List&lt;String&gt;**](String.md)|  Keyword search for filer name or ID  | [optional] |

### Return type

[**EFilingsPage**](EFilingsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="efileReportsHouseSenateGet"></a>
# **efileReportsHouseSenateGet**
> BaseF3FilingPage efileReportsHouseSenateGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EfilingApi;

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

    EfilingApi apiInstance = new EfilingApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    LocalDate maxReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<Integer> fileNumber = Arrays.asList(); // List<Integer> | Filing ID number
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "-receipt_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> qFiler = Arrays.asList(); // List<String> |  Keyword search for filer name or ID 
    try {
      BaseF3FilingPage result = apiInstance.efileReportsHouseSenateGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EfilingApi#efileReportsHouseSenateGet");
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
| **minReceiptDate** | **LocalDate**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **maxReceiptDate** | **LocalDate**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **fileNumber** | [**List&lt;Integer&gt;**](Integer.md)| Filing ID number | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -receipt_date] |
| **qFiler** | [**List&lt;String&gt;**](String.md)|  Keyword search for filer name or ID  | [optional] |

### Return type

[**BaseF3FilingPage**](BaseF3FilingPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="efileReportsPacPartyGet"></a>
# **efileReportsPacPartyGet**
> BaseF3XFilingPage efileReportsPacPartyGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EfilingApi;

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

    EfilingApi apiInstance = new EfilingApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    LocalDate maxReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<Integer> fileNumber = Arrays.asList(); // List<Integer> | Filing ID number
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "-receipt_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> qFiler = Arrays.asList(); // List<String> |  Keyword search for filer name or ID 
    try {
      BaseF3XFilingPage result = apiInstance.efileReportsPacPartyGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EfilingApi#efileReportsPacPartyGet");
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
| **minReceiptDate** | **LocalDate**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **maxReceiptDate** | **LocalDate**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **fileNumber** | [**List&lt;Integer&gt;**](Integer.md)| Filing ID number | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -receipt_date] |
| **qFiler** | [**List&lt;String&gt;**](String.md)|  Keyword search for filer name or ID  | [optional] |

### Return type

[**BaseF3XFilingPage**](BaseF3XFilingPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="efileReportsPresidentialGet"></a>
# **efileReportsPresidentialGet**
> BaseF3PFilingPage efileReportsPresidentialGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EfilingApi;

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

    EfilingApi apiInstance = new EfilingApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    LocalDate maxReceiptDate = LocalDate.now(); // LocalDate |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<Integer> fileNumber = Arrays.asList(); // List<Integer> | Filing ID number
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "-receipt_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> qFiler = Arrays.asList(); // List<String> |  Keyword search for filer name or ID 
    try {
      BaseF3PFilingPage result = apiInstance.efileReportsPresidentialGet(apiKey, minReceiptDate, sortNullsLast, page, committeeId, sortNullOnly, maxReceiptDate, sortHideNull, fileNumber, perPage, sort, qFiler);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EfilingApi#efileReportsPresidentialGet");
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
| **minReceiptDate** | **LocalDate**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **maxReceiptDate** | **LocalDate**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **fileNumber** | [**List&lt;Integer&gt;**](Integer.md)| Filing ID number | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -receipt_date] |
| **qFiler** | [**List&lt;String&gt;**](String.md)|  Keyword search for filer name or ID  | [optional] |

### Return type

[**BaseF3PFilingPage**](BaseF3PFilingPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

