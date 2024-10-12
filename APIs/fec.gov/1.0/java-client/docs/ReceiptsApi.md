# ReceiptsApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**schedulesScheduleAByEmployerGet**](ReceiptsApi.md#schedulesScheduleAByEmployerGet) | **GET** /schedules/schedule_a/by_employer/ |  |
| [**schedulesScheduleAByOccupationGet**](ReceiptsApi.md#schedulesScheduleAByOccupationGet) | **GET** /schedules/schedule_a/by_occupation/ |  |
| [**schedulesScheduleABySizeByCandidateGet**](ReceiptsApi.md#schedulesScheduleABySizeByCandidateGet) | **GET** /schedules/schedule_a/by_size/by_candidate/ |  |
| [**schedulesScheduleABySizeGet**](ReceiptsApi.md#schedulesScheduleABySizeGet) | **GET** /schedules/schedule_a/by_size/ |  |
| [**schedulesScheduleAByStateByCandidateGet**](ReceiptsApi.md#schedulesScheduleAByStateByCandidateGet) | **GET** /schedules/schedule_a/by_state/by_candidate/ |  |
| [**schedulesScheduleAByStateByCandidateTotalsGet**](ReceiptsApi.md#schedulesScheduleAByStateByCandidateTotalsGet) | **GET** /schedules/schedule_a/by_state/by_candidate/totals/ |  |
| [**schedulesScheduleAByStateGet**](ReceiptsApi.md#schedulesScheduleAByStateGet) | **GET** /schedules/schedule_a/by_state/ |  |
| [**schedulesScheduleAByStateTotalsGet**](ReceiptsApi.md#schedulesScheduleAByStateTotalsGet) | **GET** /schedules/schedule_a/by_state/totals/ |  |
| [**schedulesScheduleAByZipGet**](ReceiptsApi.md#schedulesScheduleAByZipGet) | **GET** /schedules/schedule_a/by_zip/ |  |
| [**schedulesScheduleAEfileGet**](ReceiptsApi.md#schedulesScheduleAEfileGet) | **GET** /schedules/schedule_a/efile/ |  |
| [**schedulesScheduleAGet**](ReceiptsApi.md#schedulesScheduleAGet) | **GET** /schedules/schedule_a/ |  |
| [**schedulesScheduleASubIdGet**](ReceiptsApi.md#schedulesScheduleASubIdGet) | **GET** /schedules/schedule_a/{sub_id}/ |  |


<a id="schedulesScheduleAByEmployerGet"></a>
# **schedulesScheduleAByEmployerGet**
> ScheduleAByEmployerPage schedulesScheduleAByEmployerGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, sortHideNull, employer, perPage, sort)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s employer name. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> employer = Arrays.asList(); // List<String> | Employer of contributor as reported on the committee's filing
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleAByEmployerPage result = apiInstance.schedulesScheduleAByEmployerGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, sortHideNull, employer, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAByEmployerGet");
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
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **employer** | [**List&lt;String&gt;**](String.md)| Employer of contributor as reported on the committee&#39;s filing | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleAByEmployerPage**](ScheduleAByEmployerPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAByOccupationGet"></a>
# **schedulesScheduleAByOccupationGet**
> ScheduleAByOccupationPage schedulesScheduleAByOccupationGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, occupation, sortHideNull, perPage, sort)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s occupation. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    List<String> occupation = Arrays.asList(); // List<String> | Occupation of contributor as reported on the committee's filing
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleAByOccupationPage result = apiInstance.schedulesScheduleAByOccupationGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, occupation, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAByOccupationGet");
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
| **occupation** | [**List&lt;String&gt;**](String.md)| Occupation of contributor as reported on the committee&#39;s filing | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleAByOccupationPage**](ScheduleAByOccupationPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleABySizeByCandidateGet"></a>
# **schedulesScheduleABySizeByCandidateGet**
> ScheduleABySizeCandidatePage schedulesScheduleABySizeByCandidateGet(apiKey, cycle, candidateId, electionFull, sortNullOnly, sortNullsLast, page, sortHideNull, perPage, sort)



 This endpoint provides itemized individual contributions received by a committee, aggregated by size of contribution and candidate. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleABySizeCandidatePage result = apiInstance.schedulesScheduleABySizeByCandidateGet(apiKey, cycle, candidateId, electionFull, sortNullOnly, sortNullsLast, page, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleABySizeByCandidateGet");
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
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleABySizeCandidatePage**](ScheduleABySizeCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleABySizeGet"></a>
# **schedulesScheduleABySizeGet**
> ScheduleABySizePage schedulesScheduleABySizeGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, size, sortHideNull, perPage, sort)



 This endpoint provides individual contributions received by a committee, aggregated by size:  &#x60;&#x60;&#x60;  - $200 and under  - $200.01 - $499.99  - $500 - $999.99  - $1000 - $1999.99  - $2000 + &#x60;&#x60;&#x60;  The $200.00 and under category includes contributions of $200 or less combined with unitemized individual contributions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    List<Integer> size = Arrays.asList(); // List<Integer> |  The total all contributions in the following ranges: ```   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + ``` Unitemized contributions are included in the `0` category. 
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleABySizePage result = apiInstance.schedulesScheduleABySizeGet(apiKey, cycle, sortNullsLast, page, committeeId, sortNullOnly, size, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleABySizeGet");
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
| **size** | [**List&lt;Integer&gt;**](Integer.md)|  The total all contributions in the following ranges: &#x60;&#x60;&#x60;   -0    $200 and under   -200  $200.01 - $499.99   -500  $500 - $999.99   -1000 $1000 - $1999.99   -2000 $2000 + &#x60;&#x60;&#x60; Unitemized contributions are included in the &#x60;0&#x60; category.  | [optional] [enum: 0, 200, 500, 1000, 2000] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleABySizePage**](ScheduleABySizePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAByStateByCandidateGet"></a>
# **schedulesScheduleAByStateByCandidateGet**
> ScheduleAByStateCandidatePage schedulesScheduleAByStateByCandidateGet(apiKey, cycle, candidateId, electionFull, sortNullOnly, sortNullsLast, page, sortHideNull, perPage, sort)



 This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state and candidate. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleAByStateCandidatePage result = apiInstance.schedulesScheduleAByStateByCandidateGet(apiKey, cycle, candidateId, electionFull, sortNullOnly, sortNullsLast, page, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAByStateByCandidateGet");
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
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleAByStateCandidatePage**](ScheduleAByStateCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAByStateByCandidateTotalsGet"></a>
# **schedulesScheduleAByStateByCandidateTotalsGet**
> ScheduleAByStateCandidatePage schedulesScheduleAByStateByCandidateTotalsGet(apiKey, cycle, candidateId, electionFull, sortNullOnly, sortNullsLast, page, sortHideNull, perPage, sort)



 Itemized individual contributions aggregated by contributor’s state, candidate, committee type and cycle. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    List<String> candidateId = Arrays.asList(); // List<String> |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
    Boolean electionFull = true; // Boolean | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleAByStateCandidatePage result = apiInstance.schedulesScheduleAByStateByCandidateTotalsGet(apiKey, cycle, candidateId, electionFull, sortNullOnly, sortNullsLast, page, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAByStateByCandidateTotalsGet");
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
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | |
| **candidateId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | |
| **electionFull** | **Boolean**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleAByStateCandidatePage**](ScheduleAByStateCandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAByStateGet"></a>
# **schedulesScheduleAByStateGet**
> ScheduleAByStatePage schedulesScheduleAByStateGet(apiKey, hideNull, cycle, sortNullOnly, page, state, committeeId, sortNullsLast, sortHideNull, perPage, sort)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s state. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Boolean hideNull = false; // Boolean | Exclude values with missing state
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | State of contributor
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "-total"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleAByStatePage result = apiInstance.schedulesScheduleAByStateGet(apiKey, hideNull, cycle, sortNullOnly, page, state, committeeId, sortNullsLast, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAByStateGet");
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
| **hideNull** | **Boolean**| Exclude values with missing state | [optional] [default to false] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| State of contributor | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -total] |

### Return type

[**ScheduleAByStatePage**](ScheduleAByStatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAByStateTotalsGet"></a>
# **schedulesScheduleAByStateTotalsGet**
> ScheduleAByStateRecipientTotalsPage schedulesScheduleAByStateTotalsGet(apiKey, committeeType, cycle, sortNullOnly, page, state, sortNullsLast, sortHideNull, perPage, sort)



 This endpoint provides itemized individual contributions received by a committee, aggregated by contributor’s state, committee type and cycle. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> committeeType = Arrays.asList(); // List<String> | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account         - all All Committee Types         - all_candidates All Candidate Committee Types (H, S, P)         - all_pacs All PAC Committee Types (N, O, Q, V, W) 
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | US state or territory
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "cycle"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleAByStateRecipientTotalsPage result = apiInstance.schedulesScheduleAByStateTotalsGet(apiKey, committeeType, cycle, sortNullOnly, page, state, sortNullsLast, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAByStateTotalsGet");
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
| **committeeType** | [**List&lt;String&gt;**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account         - all All Committee Types         - all_candidates All Candidate Committee Types (H, S, P)         - all_pacs All PAC Committee Types (N, O, Q, V, W)  | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| US state or territory | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to cycle] |

### Return type

[**ScheduleAByStateRecipientTotalsPage**](ScheduleAByStateRecipientTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAByZipGet"></a>
# **schedulesScheduleAByZipGet**
> ScheduleAByZipPage schedulesScheduleAByZipGet(apiKey, zip, cycle, sortNullOnly, page, state, committeeId, sortNullsLast, sortHideNull, perPage, sort)



 This endpoint provides itemized individual contributions received by a committee, aggregated by the contributor’s ZIP code. If you are interested in our “is_individual” methodology, review the [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology). Unitemized individual contributions are not included. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    List<String> zip = Arrays.asList(); // List<String> | Zip code of contributor
    List<Integer> cycle = Arrays.asList(); // List<Integer> |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> state = Arrays.asList(); // List<String> | State of contributor
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    try {
      ScheduleAByZipPage result = apiInstance.schedulesScheduleAByZipGet(apiKey, zip, cycle, sortNullOnly, page, state, committeeId, sortNullsLast, sortHideNull, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAByZipGet");
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
| **zip** | [**List&lt;String&gt;**](String.md)| Zip code of contributor | [optional] |
| **cycle** | [**List&lt;Integer&gt;**](Integer.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **state** | [**List&lt;String&gt;**](String.md)| State of contributor | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |

### Return type

[**ScheduleAByZipPage**](ScheduleAByZipPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAEfileGet"></a>
# **schedulesScheduleAEfileGet**
> ScheduleAEfilePage schedulesScheduleAEfileGet(apiKey, minDate, maxImageNumber, contributorEmployer, minImageNumber, sortNullOnly, sortHideNull, contributorName, minAmount, perPage, contributorState, sort, lineNumber, contributorOccupation, contributorCity, sortNullsLast, page, committeeId, imageNumber, maxDate, maxAmount)



 Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum date
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    List<String> contributorEmployer = Arrays.asList(); // List<String> | Employer of contributor, filers need to make an effort to gather this information
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> contributorName = Arrays.asList(); // List<String> | Name of contributor
    String minAmount = "minAmount_example"; // String | Filter for all amounts greater than a value.
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> contributorState = Arrays.asList(); // List<String> | State of contributor
    String sort = "-contribution_receipt_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    String lineNumber = "lineNumber_example"; // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
    List<String> contributorOccupation = Arrays.asList(); // List<String> | Occupation of contributor, filers need to make an effort to gather this information
    List<String> contributorCity = Arrays.asList(); // List<String> | City of contributor
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum date
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    try {
      ScheduleAEfilePage result = apiInstance.schedulesScheduleAEfileGet(apiKey, minDate, maxImageNumber, contributorEmployer, minImageNumber, sortNullOnly, sortHideNull, contributorName, minAmount, perPage, contributorState, sort, lineNumber, contributorOccupation, contributorCity, sortNullsLast, page, committeeId, imageNumber, maxDate, maxAmount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAEfileGet");
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
| **contributorEmployer** | [**List&lt;String&gt;**](String.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **contributorName** | [**List&lt;String&gt;**](String.md)| Name of contributor | [optional] |
| **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **contributorState** | [**List&lt;String&gt;**](String.md)| State of contributor | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -contribution_receipt_date] |
| **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] |
| **contributorOccupation** | [**List&lt;String&gt;**](String.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] |
| **contributorCity** | [**List&lt;String&gt;**](String.md)| City of contributor | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum date | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |

### Return type

[**ScheduleAEfilePage**](ScheduleAEfilePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleAGet"></a>
# **schedulesScheduleAGet**
> ScheduleAPage schedulesScheduleAGet(apiKey, isIndividual, minDate, maxImageNumber, minImageNumber, contributorType, contributorId, recipientCommitteeOrgType, contributorEmployer, sortNullOnly, lastIndex, contributorName, minAmount, sortHideNull, recipientCommitteeDesignation, maxLoadDate, recipientCommitteeType, sort, lastContributionReceiptDate, lastContributionReceiptAmount, lineNumber, contributorState, perPage, twoYearTransactionPeriod, contributorZip, minLoadDate, contributorOccupation, contributorCity, committeeId, imageNumber, maxDate, maxAmount)



 This description is for both ​&#x60;/schedules​/schedule_a​/&#x60; and ​ &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60;.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the &#x60;/schedules/schedule_a/&#x60; endpoint. For a more complete description of all Schedule A records visit [About receipts data](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/about-receipts-data/). If you are interested in our \&quot;is_individual\&quot; methodology visit our [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/).  ​The &#x60;/schedules​/schedule_a​/&#x60; endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the &#x60;last_indexes&#x60; object from pagination to the URL of your last request as additional parameters.  For example, when sorting by &#x60;contribution_receipt_date&#x60;, you might receive a page of results with the two scenarios of following pagination information:  case #1: &#x60;&#x60;&#x60; pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880619\&quot;,         last_contribution_receipt_date: \&quot;2014-01-01\&quot;     } } &#x60;&#x60;&#x60; &lt;br/&gt; case #2 (results which include contribution_receipt_date &#x3D; NULL):  &#x60;&#x60;&#x60; pagination: {     pages: 2152644,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880639\&quot;,         sort_null_only: True     } } &#x60;&#x60;&#x60; To fetch the next page of sorted results, append &#x60;last_index&#x3D;230880619&#x60; and &#x60;last_contribution_receipt_date&#x3D;2014-01-01&#x60; to the URL and when reaching &#x60;contribution_receipt_date&#x3D;NULL&#x60;, append &#x60;last_index&#x3D;230880639&#x60; and &#x60;sort_null_only&#x3D;True&#x60;. We strongly advise paging through these results using sort indices. The default sort is acending by &#x60;contribution_receipt_date&#x60; (&#x60;deprecated&#x60;, will be descending). If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​&#x60;/schedules​/schedule_a​/&#x60; may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  To avoid throwing the \&quot;out of range\&quot; exception on the last page, one recommandation is to use total count and &#x60;per_page&#x60; to control the traverse loop of results.  ​The &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60; endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Boolean isIndividual = true; // Boolean | Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals.
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum date
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    List<String> contributorType = Arrays.asList(); // List<String> | Filters individual or committee contributions based on line number
    List<String> contributorId = Arrays.asList(); // List<String> | The FEC identifier should be represented here if the contributor is registered with the FEC.
    List<String> recipientCommitteeOrgType = Arrays.asList(); // List<String> | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    List<String> contributorEmployer = Arrays.asList(); // List<String> | Employer of contributor, filers need to make an effort to gather this information
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer lastIndex = 56; // Integer | Index of last result from previous page
    List<String> contributorName = Arrays.asList(); // List<String> | Name of contributor
    String minAmount = "minAmount_example"; // String | Filter for all amounts greater than a value.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> recipientCommitteeDesignation = Arrays.asList(); // List<String> | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    LocalDate maxLoadDate = LocalDate.now(); // LocalDate | Maximum load date
    List<String> recipientCommitteeType = Arrays.asList(); // List<String> | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    String sort = "-contribution_receipt_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    LocalDate lastContributionReceiptDate = LocalDate.now(); // LocalDate | When sorting by `contribution_receipt_date`, this is populated with the         `contribution_receipt_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
    Float lastContributionReceiptAmount = 3.4F; // Float | When sorting by `contribution_receipt_amount`, this is populated with the         `contribution_receipt_amount` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
    String lineNumber = "lineNumber_example"; // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
    List<String> contributorState = Arrays.asList(); // List<String> | State of contributor
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> twoYearTransactionPeriod = Arrays.asList(); // List<Integer> |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    List<String> contributorZip = Arrays.asList(); // List<String> | Zip code of contributor
    LocalDate minLoadDate = LocalDate.now(); // LocalDate | Minimum load date
    List<String> contributorOccupation = Arrays.asList(); // List<String> | Occupation of contributor, filers need to make an effort to gather this information
    List<String> contributorCity = Arrays.asList(); // List<String> | City of contributor
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum date
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    try {
      ScheduleAPage result = apiInstance.schedulesScheduleAGet(apiKey, isIndividual, minDate, maxImageNumber, minImageNumber, contributorType, contributorId, recipientCommitteeOrgType, contributorEmployer, sortNullOnly, lastIndex, contributorName, minAmount, sortHideNull, recipientCommitteeDesignation, maxLoadDate, recipientCommitteeType, sort, lastContributionReceiptDate, lastContributionReceiptAmount, lineNumber, contributorState, perPage, twoYearTransactionPeriod, contributorZip, minLoadDate, contributorOccupation, contributorCity, committeeId, imageNumber, maxDate, maxAmount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleAGet");
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
| **isIndividual** | **Boolean**| Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. | [optional] |
| **minDate** | **LocalDate**| Minimum date | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **contributorType** | [**List&lt;String&gt;**](String.md)| Filters individual or committee contributions based on line number | [optional] [enum: individual, committee] |
| **contributorId** | [**List&lt;String&gt;**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] |
| **recipientCommitteeOrgType** | [**List&lt;String&gt;**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] [enum: , C, L, M, T, V, W] |
| **contributorEmployer** | [**List&lt;String&gt;**](String.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **lastIndex** | **Integer**| Index of last result from previous page | [optional] |
| **contributorName** | [**List&lt;String&gt;**](String.md)| Name of contributor | [optional] |
| **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **recipientCommitteeDesignation** | [**List&lt;String&gt;**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] [enum: , A, J, P, U, B, D] |
| **maxLoadDate** | **LocalDate**| Maximum load date | [optional] |
| **recipientCommitteeType** | [**List&lt;String&gt;**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] [enum: , C, D, E, H, I, N, O, P, Q, S, U, V, W, X, Y, Z] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -contribution_receipt_date] |
| **lastContributionReceiptDate** | **LocalDate**| When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **lastContributionReceiptAmount** | **Float**| When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] |
| **contributorState** | [**List&lt;String&gt;**](String.md)| State of contributor | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **twoYearTransactionPeriod** | [**List&lt;Integer&gt;**](Integer.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] |
| **contributorZip** | [**List&lt;String&gt;**](String.md)| Zip code of contributor | [optional] |
| **minLoadDate** | **LocalDate**| Minimum load date | [optional] |
| **contributorOccupation** | [**List&lt;String&gt;**](String.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] |
| **contributorCity** | [**List&lt;String&gt;**](String.md)| City of contributor | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum date | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |

### Return type

[**ScheduleAPage**](ScheduleAPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="schedulesScheduleASubIdGet"></a>
# **schedulesScheduleASubIdGet**
> ScheduleAPage schedulesScheduleASubIdGet(apiKey, subId, isIndividual, minDate, maxImageNumber, minImageNumber, contributorType, contributorId, recipientCommitteeOrgType, contributorEmployer, sortNullOnly, lastIndex, contributorName, minAmount, sortHideNull, recipientCommitteeDesignation, maxLoadDate, recipientCommitteeType, sort, lastContributionReceiptDate, lastContributionReceiptAmount, lineNumber, contributorState, perPage, twoYearTransactionPeriod, contributorZip, minLoadDate, contributorOccupation, contributorCity, committeeId, imageNumber, maxDate, maxAmount)



 This description is for both ​&#x60;/schedules​/schedule_a​/&#x60; and ​ &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60;.  This endpoint provides itemized receipts. Schedule A records describe itemized receipts, including contributions from individuals. If you are interested in contributions from an individual, use the &#x60;/schedules/schedule_a/&#x60; endpoint. For a more complete description of all Schedule A records visit [About receipts data](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/about-receipts-data/). If you are interested in our \&quot;is_individual\&quot; methodology visit our [methodology page](https://www.fec.gov/campaign-finance-data/about-campaign-finance-data/methodology/).  ​The &#x60;/schedules​/schedule_a​/&#x60; endpoint is not paginated by page number. This endpoint uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset. To request the next page, you should append the values found in the &#x60;last_indexes&#x60; object from pagination to the URL of your last request as additional parameters.  For example, when sorting by &#x60;contribution_receipt_date&#x60;, you might receive a page of results with the two scenarios of following pagination information:  case #1: &#x60;&#x60;&#x60; pagination: {     pages: 2152643,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880619\&quot;,         last_contribution_receipt_date: \&quot;2014-01-01\&quot;     } } &#x60;&#x60;&#x60; &lt;br/&gt; case #2 (results which include contribution_receipt_date &#x3D; NULL):  &#x60;&#x60;&#x60; pagination: {     pages: 2152644,     per_page: 20,     count: 43052850,     last_indexes: {         last_index: \&quot;230880639\&quot;,         sort_null_only: True     } } &#x60;&#x60;&#x60; To fetch the next page of sorted results, append &#x60;last_index&#x3D;230880619&#x60; and &#x60;last_contribution_receipt_date&#x3D;2014-01-01&#x60; to the URL and when reaching &#x60;contribution_receipt_date&#x3D;NULL&#x60;, append &#x60;last_index&#x3D;230880639&#x60; and &#x60;sort_null_only&#x3D;True&#x60;. We strongly advise paging through these results using sort indices. The default sort is acending by &#x60;contribution_receipt_date&#x60; (&#x60;deprecated&#x60;, will be descending). If you do not page using sort indices, some transactions may be unintentionally filtered out.  Calls to ​&#x60;/schedules​/schedule_a​/&#x60; may return many records. For large result sets, the record counts found in the pagination object are approximate; you will need to page through the records until no records are returned.  To avoid throwing the \&quot;out of range\&quot; exception on the last page, one recommandation is to use total count and &#x60;per_page&#x60; to control the traverse loop of results.  ​The &#x60;/schedules​/schedule_a​/{sub_id}​/&#x60; endpoint returns a single transaction, but it does include a pagination object class. Please ignore the information in that object class.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceiptsApi;

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

    ReceiptsApi apiInstance = new ReceiptsApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    String subId = "subId_example"; // String | 
    Boolean isIndividual = true; // Boolean | Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals.
    LocalDate minDate = LocalDate.now(); // LocalDate | Minimum date
    String maxImageNumber = "maxImageNumber_example"; // String | Maxium image number of the page where the schedule item is reported
    String minImageNumber = "minImageNumber_example"; // String | Minium image number of the page where the schedule item is reported
    List<String> contributorType = Arrays.asList(); // List<String> | Filters individual or committee contributions based on line number
    List<String> contributorId = Arrays.asList(); // List<String> | The FEC identifier should be represented here if the contributor is registered with the FEC.
    List<String> recipientCommitteeOrgType = Arrays.asList(); // List<String> | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
    List<String> contributorEmployer = Arrays.asList(); // List<String> | Employer of contributor, filers need to make an effort to gather this information
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer lastIndex = 56; // Integer | Index of last result from previous page
    List<String> contributorName = Arrays.asList(); // List<String> | Name of contributor
    String minAmount = "minAmount_example"; // String | Filter for all amounts greater than a value.
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> recipientCommitteeDesignation = Arrays.asList(); // List<String> | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
    LocalDate maxLoadDate = LocalDate.now(); // LocalDate | Maximum load date
    List<String> recipientCommitteeType = Arrays.asList(); // List<String> | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
    String sort = "-contribution_receipt_date"; // String | Provide a field to sort by. Use `-` for descending order. 
    LocalDate lastContributionReceiptDate = LocalDate.now(); // LocalDate | When sorting by `contribution_receipt_date`, this is populated with the         `contribution_receipt_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
    Float lastContributionReceiptAmount = 3.4F; // Float | When sorting by `contribution_receipt_amount`, this is populated with the         `contribution_receipt_amount` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
    String lineNumber = "lineNumber_example"; // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
    List<String> contributorState = Arrays.asList(); // List<String> | State of contributor
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<Integer> twoYearTransactionPeriod = Arrays.asList(); // List<Integer> |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
    List<String> contributorZip = Arrays.asList(); // List<String> | Zip code of contributor
    LocalDate minLoadDate = LocalDate.now(); // LocalDate | Minimum load date
    List<String> contributorOccupation = Arrays.asList(); // List<String> | Occupation of contributor, filers need to make an effort to gather this information
    List<String> contributorCity = Arrays.asList(); // List<String> | City of contributor
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    List<String> imageNumber = Arrays.asList(); // List<String> |  An unique identifier for each page where the electronic or paper filing is reported. 
    LocalDate maxDate = LocalDate.now(); // LocalDate | Maximum date
    String maxAmount = "maxAmount_example"; // String | Filter for all amounts less than a value.
    try {
      ScheduleAPage result = apiInstance.schedulesScheduleASubIdGet(apiKey, subId, isIndividual, minDate, maxImageNumber, minImageNumber, contributorType, contributorId, recipientCommitteeOrgType, contributorEmployer, sortNullOnly, lastIndex, contributorName, minAmount, sortHideNull, recipientCommitteeDesignation, maxLoadDate, recipientCommitteeType, sort, lastContributionReceiptDate, lastContributionReceiptAmount, lineNumber, contributorState, perPage, twoYearTransactionPeriod, contributorZip, minLoadDate, contributorOccupation, contributorCity, committeeId, imageNumber, maxDate, maxAmount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceiptsApi#schedulesScheduleASubIdGet");
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
| **isIndividual** | **Boolean**| Restrict to non-earmarked individual contributions where memo code is true. Filtering individuals is useful to make sure contributions are not double reported and in creating breakdowns of the amount of money coming from individuals. | [optional] |
| **minDate** | **LocalDate**| Minimum date | [optional] |
| **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] |
| **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] |
| **contributorType** | [**List&lt;String&gt;**](String.md)| Filters individual or committee contributions based on line number | [optional] [enum: individual, committee] |
| **contributorId** | [**List&lt;String&gt;**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] |
| **recipientCommitteeOrgType** | [**List&lt;String&gt;**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] [enum: , C, L, M, T, V, W] |
| **contributorEmployer** | [**List&lt;String&gt;**](String.md)| Employer of contributor, filers need to make an effort to gather this information | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **lastIndex** | **Integer**| Index of last result from previous page | [optional] |
| **contributorName** | [**List&lt;String&gt;**](String.md)| Name of contributor | [optional] |
| **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **recipientCommitteeDesignation** | [**List&lt;String&gt;**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] [enum: , A, J, P, U, B, D] |
| **maxLoadDate** | **LocalDate**| Maximum load date | [optional] |
| **recipientCommitteeType** | [**List&lt;String&gt;**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] [enum: , C, D, E, H, I, N, O, P, Q, S, U, V, W, X, Y, Z] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to -contribution_receipt_date] |
| **lastContributionReceiptDate** | **LocalDate**| When sorting by &#x60;contribution_receipt_date&#x60;, this is populated with the         &#x60;contribution_receipt_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **lastContributionReceiptAmount** | **Float**| When sorting by &#x60;contribution_receipt_amount&#x60;, this is populated with the         &#x60;contribution_receipt_amount&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] |
| **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] |
| **contributorState** | [**List&lt;String&gt;**](String.md)| State of contributor | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **twoYearTransactionPeriod** | [**List&lt;Integer&gt;**](Integer.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] |
| **contributorZip** | [**List&lt;String&gt;**](String.md)| Zip code of contributor | [optional] |
| **minLoadDate** | **LocalDate**| Minimum load date | [optional] |
| **contributorOccupation** | [**List&lt;String&gt;**](String.md)| Occupation of contributor, filers need to make an effort to gather this information | [optional] |
| **contributorCity** | [**List&lt;String&gt;**](String.md)| City of contributor | [optional] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **imageNumber** | [**List&lt;String&gt;**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] |
| **maxDate** | **LocalDate**| Maximum date | [optional] |
| **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] |

### Return type

[**ScheduleAPage**](ScheduleAPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

