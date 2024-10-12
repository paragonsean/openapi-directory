# FilerResourcesApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**radAnalystGet**](FilerResourcesApi.md#radAnalystGet) | **GET** /rad-analyst/ |  |
| [**stateElectionOfficeGet**](FilerResourcesApi.md#stateElectionOfficeGet) | **GET** /state-election-office/ |  |


<a id="radAnalystGet"></a>
# **radAnalystGet**
> RadAnalystPage radAnalystGet(apiKey, minAssignmentUpdateDate, telephoneExt, analystId, sortNullOnly, page, committeeId, sortNullsLast, sortHideNull, name, perPage, email, title, sort, maxAssignmentUpdateDate, analystShortId)



 Use this endpoint to look up the RAD Analyst for a committee.  The mission of the Reports Analysis Division (RAD) is to ensure that campaigns and political committees file timely and accurate reports that fully disclose their financial activities.  RAD is responsible for reviewing statements and financial reports filed by political committees participating in federal elections, providing assistance and guidance to the committees to properly file their reports, and for taking appropriate action to ensure compliance with the Federal Election Campaign Act (FECA). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilerResourcesApi;

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

    FilerResourcesApi apiInstance = new FilerResourcesApi(defaultClient);
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    LocalDate minAssignmentUpdateDate = LocalDate.now(); // LocalDate | Filter results for assignment updates made after this date
    List<Integer> telephoneExt = Arrays.asList(); // List<Integer> | Telephone extension of RAD analyst
    List<Integer> analystId = Arrays.asList(); // List<Integer> | ID of RAD analyst
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    List<String> committeeId = Arrays.asList(); // List<String> |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    List<String> name = Arrays.asList(); // List<String> | Name of RAD analyst
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    List<String> email = Arrays.asList(); // List<String> | Email of RAD analyst
    List<String> title = Arrays.asList(); // List<String> | Title of RAD analyst
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    LocalDate maxAssignmentUpdateDate = LocalDate.now(); // LocalDate | Filter results for assignment updates made before this date
    List<Integer> analystShortId = Arrays.asList(); // List<Integer> | Short ID of RAD analyst
    try {
      RadAnalystPage result = apiInstance.radAnalystGet(apiKey, minAssignmentUpdateDate, telephoneExt, analystId, sortNullOnly, page, committeeId, sortNullsLast, sortHideNull, name, perPage, email, title, sort, maxAssignmentUpdateDate, analystShortId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilerResourcesApi#radAnalystGet");
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
| **minAssignmentUpdateDate** | **LocalDate**| Filter results for assignment updates made after this date | [optional] |
| **telephoneExt** | [**List&lt;Integer&gt;**](Integer.md)| Telephone extension of RAD analyst | [optional] |
| **analystId** | [**List&lt;Integer&gt;**](Integer.md)| ID of RAD analyst | [optional] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **committeeId** | [**List&lt;String&gt;**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **name** | [**List&lt;String&gt;**](String.md)| Name of RAD analyst | [optional] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **email** | [**List&lt;String&gt;**](String.md)| Email of RAD analyst | [optional] |
| **title** | [**List&lt;String&gt;**](String.md)| Title of RAD analyst | [optional] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |
| **maxAssignmentUpdateDate** | **LocalDate**| Filter results for assignment updates made before this date | [optional] |
| **analystShortId** | [**List&lt;Integer&gt;**](Integer.md)| Short ID of RAD analyst | [optional] |

### Return type

[**RadAnalystPage**](RadAnalystPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

<a id="stateElectionOfficeGet"></a>
# **stateElectionOfficeGet**
> StateElectionOfficeInfoPage stateElectionOfficeGet(state, apiKey, page, sortHideNull, perPage, sortNullOnly, sort, sortNullsLast)



 State laws and procedures govern elections for state or local offices as well as how candidates appear on election ballots. Contact the appropriate state election office for more information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilerResourcesApi;

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

    FilerResourcesApi apiInstance = new FilerResourcesApi(defaultClient);
    String state = "state_example"; // String |  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.  
    String apiKey = "DEMO_KEY"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
    Integer page = 1; // Integer | For paginating through results, starting at page 1
    Boolean sortHideNull = false; // Boolean | Hide null values on sorted column(s).
    Integer perPage = 20; // Integer | The number of results returned per page. Defaults to 20.
    Boolean sortNullOnly = false; // Boolean | Toggle that filters out all rows having sort column that is non-null
    String sort = "sort_example"; // String | Provide a field to sort by. Use `-` for descending order. 
    Boolean sortNullsLast = false; // Boolean | Toggle that sorts null values last
    try {
      StateElectionOfficeInfoPage result = apiInstance.stateElectionOfficeGet(state, apiKey, page, sortHideNull, perPage, sortNullOnly, sort, sortNullsLast);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilerResourcesApi#stateElectionOfficeGet");
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
| **state** | **String**|  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.   | |
| **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY] |
| **page** | **Integer**| For paginating through results, starting at page 1 | [optional] [default to 1] |
| **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false] |
| **perPage** | **Integer**| The number of results returned per page. Defaults to 20. | [optional] [default to 20] |
| **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false] |
| **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] |
| **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false] |

### Return type

[**StateElectionOfficeInfoPage**](StateElectionOfficeInfoPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

