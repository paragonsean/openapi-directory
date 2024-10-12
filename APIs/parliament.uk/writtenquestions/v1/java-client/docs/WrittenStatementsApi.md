# WrittenStatementsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiWrittenstatementsStatementsDateUinGet**](WrittenStatementsApi.md#apiWrittenstatementsStatementsDateUinGet) | **GET** /api/writtenstatements/statements/{date}/{uin} | Returns a written statemnet |
| [**apiWrittenstatementsStatementsGet**](WrittenStatementsApi.md#apiWrittenstatementsStatementsGet) | **GET** /api/writtenstatements/statements | Returns a list of written statements |
| [**apiWrittenstatementsStatementsIdGet**](WrittenStatementsApi.md#apiWrittenstatementsStatementsIdGet) | **GET** /api/writtenstatements/statements/{id} | Returns a written statement |


<a id="apiWrittenstatementsStatementsDateUinGet"></a>
# **apiWrittenstatementsStatementsDateUinGet**
> StatementsViewModelItem apiWrittenstatementsStatementsDateUinGet(date, uin, expandMember)

Returns a written statemnet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WrittenStatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WrittenStatementsApi apiInstance = new WrittenStatementsApi(defaultClient);
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | Written statement on date specified
    String uin = "uin_example"; // String | Written statement with uid specified
    Boolean expandMember = true; // Boolean | Expand the details of Members in the results
    try {
      StatementsViewModelItem result = apiInstance.apiWrittenstatementsStatementsDateUinGet(date, uin, expandMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WrittenStatementsApi#apiWrittenstatementsStatementsDateUinGet");
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
| **date** | **OffsetDateTime**| Written statement on date specified | |
| **uin** | **String**| Written statement with uid specified | |
| **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] |

### Return type

[**StatementsViewModelItem**](StatementsViewModelItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiWrittenstatementsStatementsGet"></a>
# **apiWrittenstatementsStatementsGet**
> StatementsViewModelSearchResult apiWrittenstatementsStatementsGet(madeWhenFrom, madeWhenTo, searchTerm, uIN, answeringBodies, members, house, skip, take, expandMember)

Returns a list of written statements

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WrittenStatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WrittenStatementsApi apiInstance = new WrittenStatementsApi(defaultClient);
    OffsetDateTime madeWhenFrom = OffsetDateTime.now(); // OffsetDateTime | Written statements made on or after the date specified. Date format yyyy-mm-dd
    OffsetDateTime madeWhenTo = OffsetDateTime.now(); // OffsetDateTime | Written statements made on or before the date specified. Date format yyyy-mm-dd
    String searchTerm = "searchTerm_example"; // String | Written questions / statements containing the search term specified, searches item content
    String uIN = "uIN_example"; // String | Written questions / statements with the uin specified
    List<Integer> answeringBodies = Arrays.asList(); // List<Integer> | Written questions / statements relating to the answering bodies with the IDs specified
    List<Integer> members = Arrays.asList(); // List<Integer> | Written questions / statements relating to the members with the IDs specified
    HouseEnum house = HouseEnum.fromValue("Bicameral"); // HouseEnum | Written questions / statements relating to the House specified
    Integer skip = 56; // Integer | Number of records to skip, default is 0
    Integer take = 56; // Integer | Number of records to take, default is 20
    Boolean expandMember = true; // Boolean | Expand the details of Members in the results
    try {
      StatementsViewModelSearchResult result = apiInstance.apiWrittenstatementsStatementsGet(madeWhenFrom, madeWhenTo, searchTerm, uIN, answeringBodies, members, house, skip, take, expandMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WrittenStatementsApi#apiWrittenstatementsStatementsGet");
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
| **madeWhenFrom** | **OffsetDateTime**| Written statements made on or after the date specified. Date format yyyy-mm-dd | [optional] |
| **madeWhenTo** | **OffsetDateTime**| Written statements made on or before the date specified. Date format yyyy-mm-dd | [optional] |
| **searchTerm** | **String**| Written questions / statements containing the search term specified, searches item content | [optional] |
| **uIN** | **String**| Written questions / statements with the uin specified | [optional] |
| **answeringBodies** | [**List&lt;Integer&gt;**](Integer.md)| Written questions / statements relating to the answering bodies with the IDs specified | [optional] |
| **members** | [**List&lt;Integer&gt;**](Integer.md)| Written questions / statements relating to the members with the IDs specified | [optional] |
| **house** | [**HouseEnum**](.md)| Written questions / statements relating to the House specified | [optional] [enum: Bicameral, Commons, Lords] |
| **skip** | **Integer**| Number of records to skip, default is 0 | [optional] |
| **take** | **Integer**| Number of records to take, default is 20 | [optional] |
| **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] |

### Return type

[**StatementsViewModelSearchResult**](StatementsViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiWrittenstatementsStatementsIdGet"></a>
# **apiWrittenstatementsStatementsIdGet**
> StatementsViewModelSearchResult apiWrittenstatementsStatementsIdGet(id, expandMember)

Returns a written statement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WrittenStatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WrittenStatementsApi apiInstance = new WrittenStatementsApi(defaultClient);
    Integer id = 56; // Integer | Written statement with ID specified
    Boolean expandMember = true; // Boolean | Expand the details of Members in the results
    try {
      StatementsViewModelSearchResult result = apiInstance.apiWrittenstatementsStatementsIdGet(id, expandMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WrittenStatementsApi#apiWrittenstatementsStatementsIdGet");
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
| **id** | **Integer**| Written statement with ID specified | |
| **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] |

### Return type

[**StatementsViewModelSearchResult**](StatementsViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

