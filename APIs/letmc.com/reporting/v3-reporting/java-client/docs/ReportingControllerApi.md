# ReportingControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportingControllerMortgagesByCreatedDate**](ReportingControllerApi.md#reportingControllerMortgagesByCreatedDate) | **GET** /v3/reporting/{shortName}/mortgagesbycreateddate | Return a collection of mortgages by created date from a specific date |
| [**reportingControllerMortgagesByUpdatedDate**](ReportingControllerApi.md#reportingControllerMortgagesByUpdatedDate) | **GET** /v3/reporting/{shortName}/mortgagesbyupdateddate | Return a collection of all mortgages updated from a specific date |
| [**reportingControllerRepossessionsByCreatedDate**](ReportingControllerApi.md#reportingControllerRepossessionsByCreatedDate) | **GET** /v3/reporting/{shortName}/repossesionsbycreateddate | Return a collection of repossessions by created date from a specific date |
| [**reportingControllerRepossessionsByUpdatedDate**](ReportingControllerApi.md#reportingControllerRepossessionsByUpdatedDate) | **GET** /v3/reporting/{shortName}/repossesionsbyupdateddate | Return a collection of all reposessions updated from a specific date |


<a id="reportingControllerMortgagesByCreatedDate"></a>
# **reportingControllerMortgagesByCreatedDate**
> ReportingPropertyMortgageModelResults reportingControllerMortgagesByCreatedDate(shortName, branchID, startDate, offset, count)

Return a collection of mortgages by created date from a specific date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    ReportingControllerApi apiInstance = new ReportingControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The date to search from.
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      ReportingPropertyMortgageModelResults result = apiInstance.reportingControllerMortgagesByCreatedDate(shortName, branchID, startDate, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingControllerApi#reportingControllerMortgagesByCreatedDate");
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
| **shortName** | **String**| The unique client short-name | |
| **branchID** | **String**| The unique ID of the Branch | |
| **startDate** | **OffsetDateTime**| The date to search from. | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**ReportingPropertyMortgageModelResults**](ReportingPropertyMortgageModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reportingControllerMortgagesByUpdatedDate"></a>
# **reportingControllerMortgagesByUpdatedDate**
> ReportingPropertyMortgageModelResults reportingControllerMortgagesByUpdatedDate(shortName, branchID, startDate, offset, count)

Return a collection of all mortgages updated from a specific date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    ReportingControllerApi apiInstance = new ReportingControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The date to search from.
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      ReportingPropertyMortgageModelResults result = apiInstance.reportingControllerMortgagesByUpdatedDate(shortName, branchID, startDate, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingControllerApi#reportingControllerMortgagesByUpdatedDate");
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
| **shortName** | **String**| The unique client short-name | |
| **branchID** | **String**| The unique ID of the Branch | |
| **startDate** | **OffsetDateTime**| The date to search from. | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**ReportingPropertyMortgageModelResults**](ReportingPropertyMortgageModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reportingControllerRepossessionsByCreatedDate"></a>
# **reportingControllerRepossessionsByCreatedDate**
> ReportingReceivershipCaseModelResults reportingControllerRepossessionsByCreatedDate(shortName, branchID, startDate, offset, count)

Return a collection of repossessions by created date from a specific date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    ReportingControllerApi apiInstance = new ReportingControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The date to search from.
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      ReportingReceivershipCaseModelResults result = apiInstance.reportingControllerRepossessionsByCreatedDate(shortName, branchID, startDate, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingControllerApi#reportingControllerRepossessionsByCreatedDate");
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
| **shortName** | **String**| The unique client short-name | |
| **branchID** | **String**| The unique ID of the Branch | |
| **startDate** | **OffsetDateTime**| The date to search from. | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**ReportingReceivershipCaseModelResults**](ReportingReceivershipCaseModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reportingControllerRepossessionsByUpdatedDate"></a>
# **reportingControllerRepossessionsByUpdatedDate**
> ReportingReceivershipCaseModelResults reportingControllerRepossessionsByUpdatedDate(shortName, branchID, startDate, offset, count)

Return a collection of all reposessions updated from a specific date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    ReportingControllerApi apiInstance = new ReportingControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The date to search from.
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      ReportingReceivershipCaseModelResults result = apiInstance.reportingControllerRepossessionsByUpdatedDate(shortName, branchID, startDate, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingControllerApi#reportingControllerRepossessionsByUpdatedDate");
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
| **shortName** | **String**| The unique client short-name | |
| **branchID** | **String**| The unique ID of the Branch | |
| **startDate** | **OffsetDateTime**| The date to search from. | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**ReportingReceivershipCaseModelResults**](ReportingReceivershipCaseModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

