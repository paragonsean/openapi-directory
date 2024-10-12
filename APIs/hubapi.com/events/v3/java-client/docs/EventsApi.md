# EventsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEventsV3EventsGetPage**](EventsApi.md#getEventsV3EventsGetPage) | **GET** /events/v3/events/ |  |


<a id="getEventsV3EventsGetPage"></a>
# **getEventsV3EventsGetPage**
> CollectionResponseExternalUnifiedEvent getEventsV3EventsGetPage(objectType, eventType, occurredAfter, occurredBefore, objectId, indexTableName, indexSpecificMetadata, after, before, limit, sort, objectPropertyLeftCurlyBracketPropnameRightCurlyBracket, propertyLeftCurlyBracketPropnameRightCurlyBracket, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String objectType = "objectType_example"; // String | 
    String eventType = "eventType_example"; // String | 
    OffsetDateTime occurredAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime occurredBefore = OffsetDateTime.now(); // OffsetDateTime | 
    Long objectId = 56L; // Long | 
    String indexTableName = "indexTableName_example"; // String | 
    String indexSpecificMetadata = "indexSpecificMetadata_example"; // String | 
    String after = "after_example"; // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
    String before = "before_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of results to display per page.
    List<String> sort = Arrays.asList(); // List<String> | 
    Object objectPropertyLeftCurlyBracketPropnameRightCurlyBracket = null; // Object | 
    Object propertyLeftCurlyBracketPropnameRightCurlyBracket = null; // Object | 
    List<String> id = Arrays.asList(); // List<String> | 
    try {
      CollectionResponseExternalUnifiedEvent result = apiInstance.getEventsV3EventsGetPage(objectType, eventType, occurredAfter, occurredBefore, objectId, indexTableName, indexSpecificMetadata, after, before, limit, sort, objectPropertyLeftCurlyBracketPropnameRightCurlyBracket, propertyLeftCurlyBracketPropnameRightCurlyBracket, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getEventsV3EventsGetPage");
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
| **objectType** | **String**|  | [optional] |
| **eventType** | **String**|  | [optional] |
| **occurredAfter** | **OffsetDateTime**|  | [optional] |
| **occurredBefore** | **OffsetDateTime**|  | [optional] |
| **objectId** | **Long**|  | [optional] |
| **indexTableName** | **String**|  | [optional] |
| **indexSpecificMetadata** | **String**|  | [optional] |
| **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] |
| **before** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of results to display per page. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **objectPropertyLeftCurlyBracketPropnameRightCurlyBracket** | [**Object**](.md)|  | [optional] |
| **propertyLeftCurlyBracketPropnameRightCurlyBracket** | [**Object**](.md)|  | [optional] |
| **id** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**CollectionResponseExternalUnifiedEvent**](CollectionResponseExternalUnifiedEvent.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

