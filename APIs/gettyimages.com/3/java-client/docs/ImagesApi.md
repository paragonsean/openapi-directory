# ImagesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3ImagesGet**](ImagesApi.md#v3ImagesGet) | **GET** /v3/images | Get metadata for multiple images by supplying multiple image ids |
| [**v3ImagesIdDownloadhistoryGet**](ImagesApi.md#v3ImagesIdDownloadhistoryGet) | **GET** /v3/images/{id}/downloadhistory | Returns information about a customer&#39;s download history for a specific asset |
| [**v3ImagesIdGet**](ImagesApi.md#v3ImagesIdGet) | **GET** /v3/images/{id} | Get metadata for a single image by supplying one image id |
| [**v3ImagesIdSameSeriesGet**](ImagesApi.md#v3ImagesIdSameSeriesGet) | **GET** /v3/images/{id}/same-series | Retrieve creative images from the same series |
| [**v3ImagesIdSimilarGet**](ImagesApi.md#v3ImagesIdSimilarGet) | **GET** /v3/images/{id}/similar | Retrieve similar images |


<a id="v3ImagesGet"></a>
# **v3ImagesGet**
> ImagesDetailResults v3ImagesGet(acceptLanguage, ids, fields)

Get metadata for multiple images by supplying multiple image ids

This endpoint returns the detailed image metadata for all specified images.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build  search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,          \&quot;artist_title\&quot;,          \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;city\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,          \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,          \&quot;copyright\&quot;,          \&quot;country\&quot;,          \&quot;credit_line\&quot;,          \&quot;date_created\&quot;,          \&quot;date_submitted\&quot;,         \&quot;download_sizes\&quot;,          \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;state_province\&quot;,          \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image  in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

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

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<String> ids = Arrays.asList(); // List<String> | Specifies one or more image ids to return. Use comma delimiter when requesting multiple ids.  Maximum of 100 ids.
    List<ImageDetailFieldValues> fields = Arrays.asList(); // List<ImageDetailFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
    try {
      ImagesDetailResults result = apiInstance.v3ImagesGet(acceptLanguage, ids, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#v3ImagesGet");
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
| **ids** | [**List&lt;String&gt;**](String.md)| Specifies one or more image ids to return. Use comma delimiter when requesting multiple ids.  Maximum of 100 ids. | [optional] |
| **fields** | [**List&lt;ImageDetailFieldValues&gt;**](ImageDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] |

### Return type

[**ImagesDetailResults**](ImagesDetailResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | ImageNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3ImagesIdDownloadhistoryGet"></a>
# **v3ImagesIdDownloadhistoryGet**
> AssetDownloadHistoryResults v3ImagesIdDownloadhistoryGet(id, acceptLanguage, companyDownloads)

Returns information about a customer&#39;s download history for a specific asset



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

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

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "id_example"; // String | An image id.
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    Boolean companyDownloads = true; // Boolean | If specified, returns the list of previously downloaded images for all users in your company.              Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false.
    try {
      AssetDownloadHistoryResults result = apiInstance.v3ImagesIdDownloadhistoryGet(id, acceptLanguage, companyDownloads);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#v3ImagesIdDownloadhistoryGet");
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
| **id** | **String**| An image id. | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **companyDownloads** | **Boolean**| If specified, returns the list of previously downloaded images for all users in your company.              Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false. | [optional] |

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
| **404** | ImageNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3ImagesIdGet"></a>
# **v3ImagesIdGet**
> ImagesDetailResults v3ImagesIdGet(id, acceptLanguage, fields)

Get metadata for a single image by supplying one image id

This endpoint returns the detailed image metadata for a specified image.  You&#39;ll need an API key and access token to use this resource.    ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are  often used to build a detailed view of images. The following fields are provided for every image in your  result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,          \&quot;artist_title\&quot;,          \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;city\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,          \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,          \&quot;copyright\&quot;,          \&quot;country\&quot;,          \&quot;credit_line\&quot;,          \&quot;date_created\&quot;,          \&quot;date_submitted\&quot;,         \&quot;download_sizes\&quot;,          \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;state_province\&quot;,          \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary.              \&quot;name\&quot;: \&quot;string\&quot;,           \&quot;uri\&quot;: \&quot;string\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

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

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "id_example"; // String | An image id. For more than one image please use the /v3/images endpoint.
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<ImageDetailFieldValues> fields = Arrays.asList(); // List<ImageDetailFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
    try {
      ImagesDetailResults result = apiInstance.v3ImagesIdGet(id, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#v3ImagesIdGet");
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
| **id** | **String**| An image id. For more than one image please use the /v3/images endpoint. | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **fields** | [**List&lt;ImageDetailFieldValues&gt;**](ImageDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] |

### Return type

[**ImagesDetailResults**](ImagesDetailResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | ImageNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3ImagesIdSameSeriesGet"></a>
# **v3ImagesIdSameSeriesGet**
> ImageSearchItemSearchResults v3ImagesIdSameSeriesGet(id, acceptLanguage, fields, page, pageSize)

Retrieve creative images from the same series

This endpoint will provide the list of images, if any exist, from the same series as the specified creative asset id. These images are typically from the same photo shoot. This functionality will not work for editorial assets.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ]         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files  that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

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

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "id_example"; // String | Identifies an existing image
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<ImagesFieldValues> fields = Arrays.asList(); // List<ImagesFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 30; // Integer | Specifies page size. Default is 30, maximum page_size is 100.
    try {
      ImageSearchItemSearchResults result = apiInstance.v3ImagesIdSameSeriesGet(id, acceptLanguage, fields, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#v3ImagesIdSameSeriesGet");
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
| **id** | **String**| Identifies an existing image | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **fields** | [**List&lt;ImagesFieldValues&gt;**](ImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30] |

### Return type

[**ImageSearchItemSearchResults**](ImageSearchItemSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | ImageNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3ImagesIdSimilarGet"></a>
# **v3ImagesIdSimilarGet**
> ImageSearchItemSearchResults v3ImagesIdSimilarGet(id, acceptLanguage, fields, page, pageSize)

Retrieve similar images

This endpoint will provide a list of images that are similar to the specified asset id.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ]         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files  that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.   The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

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

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "id_example"; // String | Identifies an existing image
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    List<ImagesFieldValues> fields = Arrays.asList(); // List<ImagesFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 30; // Integer | Specifies page size. Default is 30, maximum page_size is 100.
    try {
      ImageSearchItemSearchResults result = apiInstance.v3ImagesIdSimilarGet(id, acceptLanguage, fields, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#v3ImagesIdSimilarGet");
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
| **id** | **String**| Identifies an existing image | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **fields** | [**List&lt;ImagesFieldValues&gt;**](ImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30] |

### Return type

[**ImageSearchItemSearchResults**](ImageSearchItemSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | ImageNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

