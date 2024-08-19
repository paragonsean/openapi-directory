# UsageApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3UsageBatchesIdPut**](UsageApi.md#v3UsageBatchesIdPut) | **PUT** /v3/usage-batches/{id} | Report usage of assets via a batch format. |


<a id="v3UsageBatchesIdPut"></a>
# **v3UsageBatchesIdPut**
> ReportUsageBatchResponse v3UsageBatchesIdPut(id, reportUsageBatchRequest)

Report usage of assets via a batch format.

# Report Usage  Use this endpoint to report the usages of a set of assets. The count of assets submitted in a single batch to this endpoint is limited to 1000. Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded. In this case, you will need to remove the invalid asset Ids from the query request and re-submit the query.  ##  Quickstart  You&#39;ll need an API key and a [Resource Owner Grant](http://developers.gettyimages.com/en/authorization-faq.html) access token to use this resource. Please see our [Getting Started](http://developers.gettyimages.com/en/getting-started.html) page for more information on how to sign up for an API key.   _Note_: Date of use can be in any unambiguous date format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Api-Key
    ApiKeyAuth Api-Key = (ApiKeyAuth) defaultClient.getAuthentication("Api-Key");
    Api-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Api-Key.setApiKeyPrefix("Token");

    UsageApi apiInstance = new UsageApi(defaultClient);
    String id = "id_example"; // String | Specifies a unique batch transaction id to identify the report.
    ReportUsageBatchRequest reportUsageBatchRequest = new ReportUsageBatchRequest(); // ReportUsageBatchRequest | Specifies up to 1000 sets of asset Id, usage count, and date of use to submit usages for.               Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded.               All dates must be on or before this date and the format should be ISO 8601 (ex: YYYY-MM-DD), time is not needed.
    try {
      ReportUsageBatchResponse result = apiInstance.v3UsageBatchesIdPut(id, reportUsageBatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageApi#v3UsageBatchesIdPut");
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
| **id** | **String**| Specifies a unique batch transaction id to identify the report. | |
| **reportUsageBatchRequest** | [**ReportUsageBatchRequest**](ReportUsageBatchRequest.md)| Specifies up to 1000 sets of asset Id, usage count, and date of use to submit usages for.               Note that all asset Ids specified must be valid or the operation will fail causing no usages to be recorded.               All dates must be on or before this date and the format should be ISO 8601 (ex: YYYY-MM-DD), time is not needed. | [optional] |

### Return type

[**ReportUsageBatchResponse**](ReportUsageBatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success - All usages reported were successfully recorded. |  -  |
| **400** | InvalidRequest - The content of the request was invalid. Most commonly this is due to either too many assets specified, no assets or invalid JSON. |  -  |
| **401** | AuthorizationTokenRequired - Authorization token was missing or not valid. |  -  |
| **403** | UnauthorizedToReportUsage |  -  |
| **409** | TransactionIdDuplicated |  -  |

