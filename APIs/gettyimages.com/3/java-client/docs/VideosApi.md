# VideosApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3VideosGet**](VideosApi.md#v3VideosGet) | **GET** /v3/videos | Get metadata for multiple videos by supplying multiple video ids |
| [**v3VideosIdDownloadhistoryGet**](VideosApi.md#v3VideosIdDownloadhistoryGet) | **GET** /v3/videos/{id}/downloadhistory | Returns information about a customer&#39;s download history for a specific asset |
| [**v3VideosIdGet**](VideosApi.md#v3VideosIdGet) | **GET** /v3/videos/{id} | Get metadata for a single video by supplying one video id |
| [**v3VideosIdSameSeriesGet**](VideosApi.md#v3VideosIdSameSeriesGet) | **GET** /v3/videos/{id}/same-series | Retrieve creative videos from the same series |
| [**v3VideosIdSimilarGet**](VideosApi.md#v3VideosIdSimilarGet) | **GET** /v3/videos/{id}/similar | Retrieve similar videos |


<a id="v3VideosGet"></a>
# **v3VideosGet**
> v3VideosGet(acceptLanguage, ids, fields)

Get metadata for multiple videos by supplying multiple video ids

Use this endpoint to return detailed video metadata for all the specified video ids.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,   \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;download_sizes\&quot;,         \&quot;era\&quot;,         \&quot;event_ids\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [       {         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ],         \&quot;key_frames\&quot;: [             {               \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {               \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {               \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {               \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {               \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]       }     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

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

    VideosApi apiInstance = new VideosApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<String> ids = Arrays.asList(); // List<String> | Specifies one or more video ids to return. Use comma delimiter when requesting multiple ids.  Maximum of 100 ids.
    List<VideoDetailFieldValues> fields = Arrays.asList(); // List<VideoDetailFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
    try {
      apiInstance.v3VideosGet(acceptLanguage, ids, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#v3VideosGet");
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
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **ids** | [**List&lt;String&gt;**](String.md)| Specifies one or more video ids to return. Use comma delimiter when requesting multiple ids.  Maximum of 100 ids. | [optional] |
| **fields** | [**List&lt;VideoDetailFieldValues&gt;**](VideoDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | VideosNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3VideosIdDownloadhistoryGet"></a>
# **v3VideosIdDownloadhistoryGet**
> AssetDownloadHistoryResults v3VideosIdDownloadhistoryGet(id, acceptLanguage, companyDownloads)

Returns information about a customer&#39;s download history for a specific asset



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

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

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "id_example"; // String | A video id.
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    Boolean companyDownloads = true; // Boolean | If specified, returns the list of previously downloaded videos for all users in your company.              Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false.
    try {
      AssetDownloadHistoryResults result = apiInstance.v3VideosIdDownloadhistoryGet(id, acceptLanguage, companyDownloads);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#v3VideosIdDownloadhistoryGet");
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
| **id** | **String**| A video id. | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **companyDownloads** | **Boolean**| If specified, returns the list of previously downloaded videos for all users in your company.              Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false. | [optional] |

### Return type

[**AssetDownloadHistoryResults**](AssetDownloadHistoryResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | VideosNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3VideosIdGet"></a>
# **v3VideosIdGet**
> v3VideosIdGet(id, acceptLanguage, fields)

Get metadata for a single video by supplying one video id

Use this endpoint to return detailed video metadata for the specified video id.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,   \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;download_sizes\&quot;,         \&quot;era\&quot;,         \&quot;event_ids\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;display_sizes\&quot;: [         {             \&quot;is_watermarked\&quot;: &lt;boolean&gt;,             \&quot;name\&quot;: \&quot;comp\&quot;,             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         },         {             \&quot;is_watermarked\&quot;: &lt;boolean&gt;,             \&quot;name\&quot;: \&quot;preview\&quot;,             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         },         {             \&quot;is_watermarked\&quot;: &lt;boolean&gt;,             \&quot;name\&quot;: \&quot;thumb\&quot;,             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         }     ],     \&quot;key_frames\&quot;: [         {             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         },         {             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         },         {             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         },         {             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         },         {             \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;         }     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

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

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "id_example"; // String | A video id. For more than one video please use the /v3/video endpoint.
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<VideoDetailFieldValues> fields = Arrays.asList(); // List<VideoDetailFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
    try {
      apiInstance.v3VideosIdGet(id, acceptLanguage, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#v3VideosIdGet");
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
| **id** | **String**| A video id. For more than one video please use the /v3/video endpoint. | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **fields** | [**List&lt;VideoDetailFieldValues&gt;**](VideoDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | VideosNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3VideosIdSameSeriesGet"></a>
# **v3VideosIdSameSeriesGet**
> v3VideosIdSameSeriesGet(id, acceptLanguage, fields, page, pageSize)

Retrieve creative videos from the same series

This endpoint will provide the list of videos, if any exist, from the same series as the specified creative asset id. These images are typically from the same photo shoot. This functionality will not work for editorial assets.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,   \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;download_sizes\&quot;,         \&quot;era\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

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

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "id_example"; // String | Identifies an existing video
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<AssociatedVideoDetailFieldValues> fields = Arrays.asList(); // List<AssociatedVideoDetailFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 30; // Integer | Specifies page size. Default is 30, maximum page_size is 100.
    try {
      apiInstance.v3VideosIdSameSeriesGet(id, acceptLanguage, fields, page, pageSize);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#v3VideosIdSameSeriesGet");
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
| **id** | **String**| Identifies an existing video | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **fields** | [**List&lt;AssociatedVideoDetailFieldValues&gt;**](AssociatedVideoDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | VideosNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3VideosIdSimilarGet"></a>
# **v3VideosIdSimilarGet**
> v3VideosIdSimilarGet(id, acceptLanguage, fields, page, pageSize)

Retrieve similar videos

This endpoint will provide a list of videos that are similar to the specified asset id.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,   \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;download_sizes\&quot;,         \&quot;era\&quot;,         \&quot;event_ids\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

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

    VideosApi apiInstance = new VideosApi(defaultClient);
    String id = "id_example"; // String | A video id.
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<AssociatedVideoDetailFieldValues> fields = Arrays.asList(); // List<AssociatedVideoDetailFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 30; // Integer | Specifies page size. Default is 30, maximum page_size is 100.
    try {
      apiInstance.v3VideosIdSimilarGet(id, acceptLanguage, fields, page, pageSize);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#v3VideosIdSimilarGet");
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
| **id** | **String**| A video id. | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **fields** | [**List&lt;AssociatedVideoDetailFieldValues&gt;**](AssociatedVideoDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | VideosNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

