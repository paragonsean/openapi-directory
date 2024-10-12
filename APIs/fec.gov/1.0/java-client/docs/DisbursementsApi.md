# DisbursementsApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schedulesScheduleBByPurposeGet**](DisbursementsApi.md#schedulesScheduleBByPurposeGet) | **GET** /schedules/schedule_b/by_purpose/ |  |
| [**schedulesScheduleBByRecipientGet**](DisbursementsApi.md#schedulesScheduleBByRecipientGet) | **GET** /schedules/schedule_b/by_recipient/ |  |
| [**schedulesScheduleBByRecipientIdGet**](DisbursementsApi.md#schedulesScheduleBByRecipientIdGet) | **GET** /schedules/schedule_b/by_recipient_id/ |  |
| [**schedulesScheduleBEfileGet**](DisbursementsApi.md#schedulesScheduleBEfileGet) | **GET** /schedules/schedule_b/efile/ |  |
| [**schedulesScheduleBGet**](DisbursementsApi.md#schedulesScheduleBGet) | **GET** /schedules/schedule_b/ |  |
| [**schedulesScheduleBSubIdGet**](DisbursementsApi.md#schedulesScheduleBSubIdGet) | **GET** /schedules/schedule_b/{sub_id}/ |  |


<a id="schedulesScheduleBByPurposeGet"></a>
# **schedulesScheduleBByPurposeGet**
> ScheduleBByPurposePage schedulesScheduleBByPurposeGet(apiKey, purpose, cycle, sortNullOnly, page, committeeId, sortNullsLast, sortHideNull, perPage, sort)



 Schedule B disbursements aggregated by disbursement purpose category. To avoid double counting, memoed items are not included. Purpose is a combination of transaction codes, category codes and disbursement description. Inspect the &#x60;disbursement_purpose&#x60; sql function within the migrations for more details. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisbursementsApi;

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

    DisbursementsApi apiInstance = new DisbursementsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> purpose = Arrays.asList(); // List<String> | Disbursement purpose category
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleBByPurposePage result = apiInstance.schedulesScheduleBByPurposeGet(apiKey, purpose, cycle, sortNullOnly, page, committeeId, sortNullsLast, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisbursementsApi#schedulesScheduleBByPurposeGet");
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
| **purpose** | [**List&lt;String&gt;**](String.md)| Disbursement purpose category | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleBByPurposePage**](ScheduleBByPurposePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleBByRecipientGet"></a>
# **schedulesScheduleBByRecipientGet**
> ScheduleBByRecipientPage schedulesScheduleBByRecipientGet(apiKey, recipientName, cycle, sortNullOnly, page, committeeId, sortNullsLast, sortHideNull, perPage, sort)



 Schedule B disbursements aggregated by recipient name. To avoid double counting, memoed items are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisbursementsApi;

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

    DisbursementsApi apiInstance = new DisbursementsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> recipientName = Arrays.asList(); // List<String> | Name of the entity receiving the disbursement
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleBByRecipientPage result = apiInstance.schedulesScheduleBByRecipientGet(apiKey, recipientName, cycle, sortNullOnly, page, committeeId, sortNullsLast, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisbursementsApi#schedulesScheduleBByRecipientGet");
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
| **recipientName** | [**List&lt;String&gt;**](String.md)| Name of the entity receiving the disbursement | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleBByRecipientPage**](ScheduleBByRecipientPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleBByRecipientIdGet"></a>
# **schedulesScheduleBByRecipientIdGet**
> ScheduleBByRecipientIDPage schedulesScheduleBByRecipientIdGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, recipientId, sortHideNull, perPage, sort)



 Schedule B disbursements aggregated by recipient committee ID, if applicable. To avoid double counting, memoed items are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisbursementsApi;

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

    DisbursementsApi apiInstance = new DisbursementsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    List<String> recipientId = Arrays.asList(); // List<String> | The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleBByRecipientIDPage result = apiInstance.schedulesScheduleBByRecipientIdGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, recipientId, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisbursementsApi#schedulesScheduleBByRecipientIdGet");
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
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **recipientId** | [**List&lt;String&gt;**](String.md)| The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleBByRecipientIDPage**](ScheduleBByRecipientIDPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleBEfileGet"></a>
# **schedulesScheduleBEfileGet**
> ScheduleBEfilePage schedulesScheduleBEfileGet(apiKey, minDate, disbursementDescription, sortNullOnly, page, committeeId, sortNullsLast, imageNumber, sortHideNull, maxDate, perPage, minAmount, maxAmount, sort, recipientCity, recipientState)



 Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisbursementsApi;

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

    DisbursementsApi apiInstance = new DisbursementsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minDate = LocalDate.now(); // LocalDate | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
    List<String> disbursementDescription = Arrays.asList(); // List<String> | Description of disbursement
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    LocalDate maxDate = LocalDate.now(); // LocalDate | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String minAmount = "minAmount_example"; // String | Filter for all amounts less than a value.
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    String sort = "-disbursement_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> recipientCity = Arrays.asList(); // List<String> | City of recipient
    List<String> recipientState = Arrays.asList(); // List<String> | State of recipient
    try {
      ScheduleBEfilePage result = apiInstance.schedulesScheduleBEfileGet(apiKey, minDate, disbursementDescription, sortNullOnly, page, committeeId, sortNullsLast, imageNumber, sortHideNull, maxDate, perPage, minAmount, maxAmount, sort, recipientCity, recipientState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisbursementsApi#schedulesScheduleBEfileGet");
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
| **minDate** | **LocalDate**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **disbursementDescription** | [**List&lt;String&gt;**](String.md)| Description of disbursement | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **maxDate** | **LocalDate**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **minAmount** | **String**| Filter for all amounts less than a value. | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -disbursement_date] |
| **recipientCity** | [**List&lt;String&gt;**](String.md)| City of recipient | [optional] |
| **recipientState** | [**List&lt;String&gt;**](String.md)| State of recipient | [optional] |

### Return type

[**ScheduleBEfilePage**](ScheduleBEfilePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleBGet"></a>
# **schedulesScheduleBGet**
> ScheduleBPage schedulesScheduleBGet(apiKey, minDate, spenderCommitteeDesignation, recipientCommitteeId, lastDisbursementDate, maxImageNumber, disbursementDescription, disbursementPurposeCategory, minImageNumber, sortNullOnly, lastIndex, sortHideNull, minAmount, perPage, lineNumber, sort, recipientCity, spenderCommitteeType, lastDisbursementAmount, spenderCommitteeOrgType, twoYearTransactionPeriod, committeeId, imageNumber, maxDate, recipientName, maxAmount, recipientState)



 Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called &#x60;two_year_transaction_period&#x60;, which is derived from the &#x60;report_year&#x60; submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;disbursement_date&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60; pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \&quot;230906248\&quot;,         last_disbursement_date: \&quot;2014-07-04\&quot;     } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;230906248&#x60; and &#x60;last_disbursement_date&#x3D;2014-07-04&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisbursementsApi;

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

    DisbursementsApi apiInstance = new DisbursementsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum date
    List<String> spenderCommitteeDesignation = Arrays.asList(); // List<String> | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    List<String> recipientCommitteeId = Arrays.asList(); // List<String> | The FEC identifier should be represented here if the contributor is registered with the FEC.
    LocalDate lastDisbursementDate = LocalDate.now(); // LocalDate | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    List<String> disbursementDescription = Arrays.asList(); // List<String> | Description of disbursement
    List<String> disbursementPurposeCategory = Arrays.asList(); // List<String> | Disbursement purpose category
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer lastIndex = 56; // Integer | Index of last result from previous page
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    String minAmount = "minAmount_example"; // String | Filter for all amounts greater than a value.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String lineNumber = "lineNumber_example"; // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
    String sort = "-disbursement_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> recipientCity = Arrays.asList(); // List<String> | City of recipient
    List<String> spenderCommitteeType = Arrays.asList(); // List<String> | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    Float lastDisbursementAmount = 3.4F; // Float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page.
    List<String> spenderCommitteeOrgType = Arrays.asList(); // List<String> | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    List<Integer> twoYearTransactionPeriod = Arrays.asList(); // List<Integer> |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum date
    List<String> recipientName = Arrays.asList(); // List<String> | Name of the entity receiving the disbursement
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    List<String> recipientState = Arrays.asList(); // List<String> | State of recipient
    try {
      ScheduleBPage result = apiInstance.schedulesScheduleBGet(apiKey, minDate, spenderCommitteeDesignation, recipientCommitteeId, lastDisbursementDate, maxImageNumber, disbursementDescription, disbursementPurposeCategory, minImageNumber, sortNullOnly, lastIndex, sortHideNull, minAmount, perPage, lineNumber, sort, recipientCity, spenderCommitteeType, lastDisbursementAmount, spenderCommitteeOrgType, twoYearTransactionPeriod, committeeId, imageNumber, maxDate, recipientName, maxAmount, recipientState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisbursementsApi#schedulesScheduleBGet");
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
| **spenderCommitteeDesignation** | [**List&lt;String&gt;**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] [enum: , A, J, P, U, B, D] |
| **recipientCommitteeId** | [**List&lt;String&gt;**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] |
| **lastDisbursementDate** | **LocalDate**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **disbursementDescription** | [**List&lt;String&gt;**](String.md)| Description of disbursement | [optional] |
| **disbursementPurposeCategory** | [**List&lt;String&gt;**](String.md)| Disbursement purpose category | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **lastIndex** | **Integer**| Index of last result from previous page | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -disbursement_date] |
| **recipientCity** | [**List&lt;String&gt;**](String.md)| City of recipient | [optional] |
| **spenderCommitteeType** | [**List&lt;String&gt;**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] [enum: , C, D, E, H, I, N, O, P, Q, S, U, V, W, X, Y, Z] |
| **lastDisbursementAmount** | **Float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **spenderCommitteeOrgType** | [**List&lt;String&gt;**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] [enum: , C, L, M, T, V, W] |
| **twoYearTransactionPeriod** | [**List&lt;Integer&gt;**](Integer.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum date | [optional] |
| **recipientName** | [**List&lt;String&gt;**](String.md)| Name of the entity receiving the disbursement | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |
| **recipientState** | [**List&lt;String&gt;**](String.md)| State of recipient | [optional] |

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleBSubIdGet"></a>
# **schedulesScheduleBSubIdGet**
> ScheduleBPage schedulesScheduleBSubIdGet(apiKey, subId, minDate, spenderCommitteeDesignation, recipientCommitteeId, lastDisbursementDate, maxImageNumber, disbursementDescription, disbursementPurposeCategory, minImageNumber, sortNullOnly, lastIndex, sortHideNull, minAmount, perPage, lineNumber, sort, recipientCity, spenderCommitteeType, lastDisbursementAmount, spenderCommitteeOrgType, twoYearTransactionPeriod, committeeId, imageNumber, maxDate, recipientName, maxAmount, recipientState)



 Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called &#x60;two_year_transaction_period&#x60;, which is derived from the &#x60;report_year&#x60; submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;disbursement_date&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60; pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \&quot;230906248\&quot;,         last_disbursement_date: \&quot;2014-07-04\&quot;     } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;230906248&#x60; and &#x60;last_disbursement_date&#x3D;2014-07-04&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisbursementsApi;

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

    DisbursementsApi apiInstance = new DisbursementsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String subId = "subId_example"; // String | 
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum date
    List<String> spenderCommitteeDesignation = Arrays.asList(); // List<String> | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    List<String> recipientCommitteeId = Arrays.asList(); // List<String> | The FEC identifier should be represented here if the contributor is registered with the FEC.
    LocalDate lastDisbursementDate = LocalDate.now(); // LocalDate | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    List<String> disbursementDescription = Arrays.asList(); // List<String> | Description of disbursement
    List<String> disbursementPurposeCategory = Arrays.asList(); // List<String> | Disbursement purpose category
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer lastIndex = 56; // Integer | Index of last result from previous page
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    String minAmount = "minAmount_example"; // String | Filter for all amounts greater than a value.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String lineNumber = "lineNumber_example"; // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
    String sort = "-disbursement_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    List<String> recipientCity = Arrays.asList(); // List<String> | City of recipient
    List<String> spenderCommitteeType = Arrays.asList(); // List<String> | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    Float lastDisbursementAmount = 3.4F; // Float | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page.
    List<String> spenderCommitteeOrgType = Arrays.asList(); // List<String> | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    List<Integer> twoYearTransactionPeriod = Arrays.asList(); // List<Integer> |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum date
    List<String> recipientName = Arrays.asList(); // List<String> | Name of the entity receiving the disbursement
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    List<String> recipientState = Arrays.asList(); // List<String> | State of recipient
    try {
      ScheduleBPage result = apiInstance.schedulesScheduleBSubIdGet(apiKey, subId, minDate, spenderCommitteeDesignation, recipientCommitteeId, lastDisbursementDate, maxImageNumber, disbursementDescription, disbursementPurposeCategory, minImageNumber, sortNullOnly, lastIndex, sortHideNull, minAmount, perPage, lineNumber, sort, recipientCity, spenderCommitteeType, lastDisbursementAmount, spenderCommitteeOrgType, twoYearTransactionPeriod, committeeId, imageNumber, maxDate, recipientName, maxAmount, recipientState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisbursementsApi#schedulesScheduleBSubIdGet");
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
| **minDate** | **LocalDate**| Minimum date | [optional] |
| **spenderCommitteeDesignation** | [**List&lt;String&gt;**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] [enum: , A, J, P, U, B, D] |
| **recipientCommitteeId** | [**List&lt;String&gt;**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] |
| **lastDisbursementDate** | **LocalDate**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **disbursementDescription** | [**List&lt;String&gt;**](String.md)| Description of disbursement | [optional] |
| **disbursementPurposeCategory** | [**List&lt;String&gt;**](String.md)| Disbursement purpose category | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **lastIndex** | **Integer**| Index of last result from previous page | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -disbursement_date] |
| **recipientCity** | [**List&lt;String&gt;**](String.md)| City of recipient | [optional] |
| **spenderCommitteeType** | [**List&lt;String&gt;**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] [enum: , C, D, E, H, I, N, O, P, Q, S, U, V, W, X, Y, Z] |
| **lastDisbursementAmount** | **Float**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **spenderCommitteeOrgType** | [**List&lt;String&gt;**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] [enum: , C, L, M, T, V, W] |
| **twoYearTransactionPeriod** | [**List&lt;Integer&gt;**](Integer.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum date | [optional] |
| **recipientName** | [**List&lt;String&gt;**](String.md)| Name of the entity receiving the disbursement | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |
| **recipientState** | [**List&lt;String&gt;**](String.md)| State of recipient | [optional] |

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

