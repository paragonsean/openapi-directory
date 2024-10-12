# LayersApi

All URIs are relative to *https://platform.climate.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v4LayersAsAppliedActivityIdContentsGet**](LayersApi.md#v4LayersAsAppliedActivityIdContentsGet) | **GET** /v4/layers/asApplied/{activityId}/contents | Retrieve the raw application activity |
| [**v4LayersAsAppliedGet**](LayersApi.md#v4LayersAsAppliedGet) | **GET** /v4/layers/asApplied | Retrieve a list of application activities |
| [**v4LayersAsHarvestedActivityIdContentsGet**](LayersApi.md#v4LayersAsHarvestedActivityIdContentsGet) | **GET** /v4/layers/asHarvested/{activityId}/contents | Retrieve the raw harvest activity |
| [**v4LayersAsHarvestedGet**](LayersApi.md#v4LayersAsHarvestedGet) | **GET** /v4/layers/asHarvested | Retrieve a list of harvest activities |
| [**v4LayersAsPlantedActivityIdContentsGet**](LayersApi.md#v4LayersAsPlantedActivityIdContentsGet) | **GET** /v4/layers/asPlanted/{activityId}/contents | Retrieve the raw planting activity |
| [**v4LayersAsPlantedGet**](LayersApi.md#v4LayersAsPlantedGet) | **GET** /v4/layers/asPlanted | Retrieve a list of planting activities |
| [**v4LayersScoutingObservationsGet**](LayersApi.md#v4LayersScoutingObservationsGet) | **GET** /v4/layers/scoutingObservations | Retrieve a list of scouting observations |
| [**v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet**](LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId}/attachments/{attachmentId}/contents | Retrieve the binary contents of a scouting observation’s attachment. |
| [**v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet**](LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId}/attachments | Retrieve attachments associated with a given scouting observation. |
| [**v4LayersScoutingObservationsScoutingObservationIdGet**](LayersApi.md#v4LayersScoutingObservationsScoutingObservationIdGet) | **GET** /v4/layers/scoutingObservations/{scoutingObservationId} | Retrieve individual scouting observation |


<a id="v4LayersAsAppliedActivityIdContentsGet"></a>
# **v4LayersAsAppliedActivityIdContentsGet**
> ApplicationActivityContents v4LayersAsAppliedActivityIdContentsGet(accept, activityId, range)

Retrieve the raw application activity

Retrieve an individual application activity by id.  Ids are retrieved via the  /layers/asApplied route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    UUID activityId = UUID.randomUUID(); // UUID | Unique identifier of the Application Activity.
    String range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    try {
      ApplicationActivityContents result = apiInstance.v4LayersAsAppliedActivityIdContentsGet(accept, activityId, range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersAsAppliedActivityIdContentsGet");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **activityId** | **UUID**| Unique identifier of the Application Activity. | |
| **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | |

### Return type

[**ApplicationActivityContents**](ApplicationActivityContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **206** | Partial Result |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **416** | Range Not Satisfiable |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersAsAppliedGet"></a>
# **v4LayersAsAppliedGet**
> ApplicationActivities v4LayersAsAppliedGet(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter)

Retrieve a list of application activities

Retrieve a list of application activities. The id in the response is used for  GET /v4/layers/asApplied/{activityId}/contents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    String xNextToken = "xNextToken_example"; // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    Integer xLimit = 56; // Integer | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    UUID resourceOwnerId = UUID.randomUUID(); // UUID | Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
    OffsetDateTime occurredAfter = OffsetDateTime.now(); // OffsetDateTime | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    OffsetDateTime occurredBefore = OffsetDateTime.now(); // OffsetDateTime | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
    try {
      ApplicationActivities result = apiInstance.v4LayersAsAppliedGet(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersAsAppliedGet");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] |
| **xLimit** | **Integer**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] |
| **resourceOwnerId** | **UUID**| Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. | [optional] |
| **occurredAfter** | **OffsetDateTime**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |
| **occurredBefore** | **OffsetDateTime**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |
| **updatedAfter** | **OffsetDateTime**| Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. | [optional] |

### Return type

[**ApplicationActivities**](ApplicationActivities.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **206** | Partial Result |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersAsHarvestedActivityIdContentsGet"></a>
# **v4LayersAsHarvestedActivityIdContentsGet**
> HarvestActivityContents v4LayersAsHarvestedActivityIdContentsGet(accept, activityId, range)

Retrieve the raw harvest activity

Retrieve an individual harvest activity by id.  Ids are retrieved via the  /layers/asHarvested route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    UUID activityId = UUID.randomUUID(); // UUID | Unique identifier of the Harvest Activity.
    String range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    try {
      HarvestActivityContents result = apiInstance.v4LayersAsHarvestedActivityIdContentsGet(accept, activityId, range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersAsHarvestedActivityIdContentsGet");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **activityId** | **UUID**| Unique identifier of the Harvest Activity. | |
| **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | |

### Return type

[**HarvestActivityContents**](HarvestActivityContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **206** | Partial Result |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **416** | Range Not Satisfiable |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersAsHarvestedGet"></a>
# **v4LayersAsHarvestedGet**
> HarvestActivities v4LayersAsHarvestedGet(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter)

Retrieve a list of harvest activities

Retrieve a list of harvest activities. The id in the response is used for  GET /v4/layers/asHarvested/{activityId}/contents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    String xNextToken = "xNextToken_example"; // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    Integer xLimit = 56; // Integer | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    UUID resourceOwnerId = UUID.randomUUID(); // UUID | Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
    OffsetDateTime occurredAfter = OffsetDateTime.now(); // OffsetDateTime | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    OffsetDateTime occurredBefore = OffsetDateTime.now(); // OffsetDateTime | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
    try {
      HarvestActivities result = apiInstance.v4LayersAsHarvestedGet(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersAsHarvestedGet");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] |
| **xLimit** | **Integer**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] |
| **resourceOwnerId** | **UUID**| Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. | [optional] |
| **occurredAfter** | **OffsetDateTime**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |
| **occurredBefore** | **OffsetDateTime**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |
| **updatedAfter** | **OffsetDateTime**| Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. | [optional] |

### Return type

[**HarvestActivities**](HarvestActivities.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **206** | Partial Result |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersAsPlantedActivityIdContentsGet"></a>
# **v4LayersAsPlantedActivityIdContentsGet**
> PlantingActivityContents v4LayersAsPlantedActivityIdContentsGet(accept, activityId, range)

Retrieve the raw planting activity

Retrieve an individual planting activity by id.  Ids are retrieved via the  /layers/asPlanted route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).  The data is compressed using .zip format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    UUID activityId = UUID.randomUUID(); // UUID | Unique identifier of the Planting Activity.
    String range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    try {
      PlantingActivityContents result = apiInstance.v4LayersAsPlantedActivityIdContentsGet(accept, activityId, range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersAsPlantedActivityIdContentsGet");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **activityId** | **UUID**| Unique identifier of the Planting Activity. | |
| **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | |

### Return type

[**PlantingActivityContents**](PlantingActivityContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **206** | Partial Result |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **416** | Range Not Satisfiable |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersAsPlantedGet"></a>
# **v4LayersAsPlantedGet**
> PlantingActivities v4LayersAsPlantedGet(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter)

Retrieve a list of planting activities

Retrieve a list of planting activities. The id in the response is used for  GET /v4/layers/asPlanted/{activityId}/contents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    String xNextToken = "xNextToken_example"; // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    Integer xLimit = 56; // Integer | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    UUID resourceOwnerId = UUID.randomUUID(); // UUID | Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
    OffsetDateTime occurredAfter = OffsetDateTime.now(); // OffsetDateTime | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    OffsetDateTime occurredBefore = OffsetDateTime.now(); // OffsetDateTime | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
    try {
      PlantingActivities result = apiInstance.v4LayersAsPlantedGet(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersAsPlantedGet");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] |
| **xLimit** | **Integer**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] |
| **resourceOwnerId** | **UUID**| Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. | [optional] |
| **occurredAfter** | **OffsetDateTime**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |
| **occurredBefore** | **OffsetDateTime**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |
| **updatedAfter** | **OffsetDateTime**| Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. | [optional] |

### Return type

[**PlantingActivities**](PlantingActivities.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **206** | Partial Result |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersScoutingObservationsGet"></a>
# **v4LayersScoutingObservationsGet**
> ScoutingObservations v4LayersScoutingObservationsGet(xNextToken, xLimit, occurredAfter, occurredBefore)

Retrieve a list of scouting observations

Retrieve a list of scouting observations created or updated by the user identified by the Authorization header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String xNextToken = "xNextToken_example"; // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    Integer xLimit = 56; // Integer | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    OffsetDateTime occurredAfter = OffsetDateTime.now(); // OffsetDateTime | Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    OffsetDateTime occurredBefore = OffsetDateTime.now(); // OffsetDateTime | Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
    try {
      ScoutingObservations result = apiInstance.v4LayersScoutingObservationsGet(xNextToken, xLimit, occurredAfter, occurredBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersScoutingObservationsGet");
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
| **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] |
| **xLimit** | **Integer**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] |
| **occurredAfter** | **OffsetDateTime**| Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |
| **occurredBefore** | **OffsetDateTime**| Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. | [optional] |

### Return type

[**ScoutingObservations**](ScoutingObservations.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **206** | Partial Result |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet"></a>
# **v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet**
> ScoutingObservationAttachmentContents v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(accept, scoutingObservationId, attachmentId, range)

Retrieve the binary contents of a scouting observation’s attachment.

Photos added to scouting notes in the FieldView app are capped to &#x60;20MiB&#x60; (&#x60;20971520 bytes&#x60;), and we won’t store photos larger than that in a scouting note. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    UUID scoutingObservationId = UUID.randomUUID(); // UUID | Unique identifier of the Scouting Observation.
    UUID attachmentId = UUID.randomUUID(); // UUID | Unique identifier of the attachment.
    String range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    try {
      ScoutingObservationAttachmentContents result = apiInstance.v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(accept, scoutingObservationId, attachmentId, range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **scoutingObservationId** | **UUID**| Unique identifier of the Scouting Observation. | |
| **attachmentId** | **UUID**| Unique identifier of the attachment. | |
| **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | |

### Return type

[**ScoutingObservationAttachmentContents**](ScoutingObservationAttachmentContents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **206** | Partial Result |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **416** | Range Not Satisfiable |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet"></a>
# **v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet**
> ScoutingObservationAttachments v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(scoutingObservationId, xNextToken, xLimit)

Retrieve attachments associated with a given scouting observation.

Retrieve attachments associated with a given scouting observation. Photos added to scouting notes in the FieldView app are capped to 20MB, and we won’t store photos larger than that in a scouting note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    UUID scoutingObservationId = UUID.randomUUID(); // UUID | Unique identifier of the Scouting Observation.
    String xNextToken = "xNextToken_example"; // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    Integer xLimit = 56; // Integer | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    try {
      ScoutingObservationAttachments result = apiInstance.v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(scoutingObservationId, xNextToken, xLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet");
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
| **scoutingObservationId** | **UUID**| Unique identifier of the Scouting Observation. | |
| **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] |
| **xLimit** | **Integer**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] |

### Return type

[**ScoutingObservationAttachments**](ScoutingObservationAttachments.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **206** | Partial Result |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="v4LayersScoutingObservationsScoutingObservationIdGet"></a>
# **v4LayersScoutingObservationsScoutingObservationIdGet**
> ScoutingObservation v4LayersScoutingObservationsScoutingObservationIdGet(scoutingObservationId)

Retrieve individual scouting observation

Retrieve an individual scouting observation by id.  Ids are retrieved via the /layers/scoutingObservations route.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    LayersApi apiInstance = new LayersApi(defaultClient);
    UUID scoutingObservationId = UUID.randomUUID(); // UUID | Unique identifier of the Scouting Observation.
    try {
      ScoutingObservation result = apiInstance.v4LayersScoutingObservationsScoutingObservationIdGet(scoutingObservationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayersApi#v4LayersScoutingObservationsScoutingObservationIdGet");
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
| **scoutingObservationId** | **UUID**| Unique identifier of the Scouting Observation. | |

### Return type

[**ScoutingObservation**](ScoutingObservation.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the requested scouting observation. |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

