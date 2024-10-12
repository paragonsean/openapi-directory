# SearchApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3SearchByImageUploadsFileNamePut**](SearchApi.md#v3SearchByImageUploadsFileNamePut) | **PUT** /v3/search/by-image/uploads/{file-name} | Upload image for use by the search creative images/videos operations |
| [**v3SearchEventsGet**](SearchApi.md#v3SearchEventsGet) | **GET** /v3/search/events | Search for events |
| [**v3SearchImagesCreativeByImageGet**](SearchApi.md#v3SearchImagesCreativeByImageGet) | **GET** /v3/search/images/creative/by-image | Search for creative images based on url |
| [**v3SearchImagesCreativeGet**](SearchApi.md#v3SearchImagesCreativeGet) | **GET** /v3/search/images/creative | Search for creative images only |
| [**v3SearchImagesEditorialGet**](SearchApi.md#v3SearchImagesEditorialGet) | **GET** /v3/search/images/editorial | Search for editorial images only |
| [**v3SearchImagesGet**](SearchApi.md#v3SearchImagesGet) | **GET** /v3/search/images | Search for both creative and editorial images - *** DEPRECATED *** |
| [**v3SearchVideosCreativeByImageGet**](SearchApi.md#v3SearchVideosCreativeByImageGet) | **GET** /v3/search/videos/creative/by-image | Search for creative videos based on url |
| [**v3SearchVideosCreativeGet**](SearchApi.md#v3SearchVideosCreativeGet) | **GET** /v3/search/videos/creative | Search for creative videos |
| [**v3SearchVideosEditorialGet**](SearchApi.md#v3SearchVideosEditorialGet) | **GET** /v3/search/videos/editorial | Search for editorial videos |


<a id="v3SearchByImageUploadsFileNamePut"></a>
# **v3SearchByImageUploadsFileNamePut**
> v3SearchByImageUploadsFileNamePut(fileName, body)

Upload image for use by the search creative images/videos operations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String fileName = "fileName_example"; // String | 
    byte[] body = null; // byte[] | 
    try {
      apiInstance.v3SearchByImageUploadsFileNamePut(fileName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchByImageUploadsFileNamePut");
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
| **fileName** | **String**|  | |
| **body** | **byte[]**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: image/jpeg, image/png
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |

<a id="v3SearchEventsGet"></a>
# **v3SearchEventsGet**
> EventsSearchResult v3SearchEventsGet(acceptLanguage, giCountryCode, editorialSegment, dateFrom, dateTo, fields, page, pageSize, phrase, sortOrder)

Search for events

Use this endpoint to search Getty Images news, sports and entertainment events. Getty Images photographers and videographers cover editorially relevant events occurring around the world.  All images or video clips produced in association with an event, are assigned the same EventID. EventIDs are part of the meta-data returned in Search Results. Only content produced under a Getty Images brand name (Getty Images News, Getty Images Sports, Getty Images Entertainment, Film Magic, Wire Image) will be consistently assigned an EventID. The Event framework may also be used to group similar content, such as \&quot;Hats from the Royal Wedding\&quot; or \&quot;Odd-ballOffbeat images of the week\&quot;.     You&#39;ll need an API key and access token to use this resource.   You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    EditorialSegmentContract editorialSegment = EditorialSegmentContract.fromValue("archival"); // EditorialSegmentContract | Filters to events with a matching editorial segment.
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | Filters to events that start on or after this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified.
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | Filters to events that start on or before this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified.
    List<EventFieldValues> fields = Arrays.asList(); // List<EventFieldValues> | Specifies fields to return. Default set is 'id','name','start_date'.
    Integer page = 1; // Integer | Request results starting at a page number (default is 1, maximum is 50).
    Integer pageSize = 30; // Integer | Request number of events to return in each page. Default is 30, maximum page_size is 100.
    String phrase = ""; // String | Filters to events related to this phrase
    EventSearchSortOrder sortOrder = EventSearchSortOrder.fromValue("newest"); // EventSearchSortOrder | Specifies the order in which to sort the results. Default is `newest`.
    try {
      EventsSearchResult result = apiInstance.v3SearchEventsGet(acceptLanguage, giCountryCode, editorialSegment, dateFrom, dateTo, fields, page, pageSize, phrase, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchEventsGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **editorialSegment** | [**EditorialSegmentContract**](.md)| Filters to events with a matching editorial segment. | [optional] [enum: archival, entertainment, news, publicity, royalty, sport] |
| **dateFrom** | **OffsetDateTime**| Filters to events that start on or after this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified. | [optional] |
| **dateTo** | **OffsetDateTime**| Filters to events that start on or before this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified. | [optional] |
| **fields** | [**List&lt;EventFieldValues&gt;**](EventFieldValues.md)| Specifies fields to return. Default set is &#39;id&#39;,&#39;name&#39;,&#39;start_date&#39;. | [optional] |
| **page** | **Integer**| Request results starting at a page number (default is 1, maximum is 50). | [optional] [default to 1] |
| **pageSize** | **Integer**| Request number of events to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **phrase** | **String**| Filters to events related to this phrase | [optional] [default to ] |
| **sortOrder** | [**EventSearchSortOrder**](.md)| Specifies the order in which to sort the results. Default is &#x60;newest&#x60;. | [optional] [enum: newest, oldest] |

### Return type

[**EventsSearchResult**](EventsSearchResult.md)

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

<a id="v3SearchImagesCreativeByImageGet"></a>
# **v3SearchImagesCreativeByImageGet**
> SearchByImageResourceResults v3SearchImagesCreativeByImageGet(acceptLanguage, giCountryCode, assetId, excludeEditorialUseOnly, facetFields, facetMaxCount, fields, imageUrl, includeFacets, page, pageSize, productTypes)

Search for creative images based on url

Search for **similar creative images** by passing an &#x60;image_url&#x60; to an uploaded image OR an &#x60;asset_id&#x60; of an asset in our catalog.  All responses will have the &#x60;exclude_nudity&#x60; filter automatically applied.  ## Searching by URL  Before calling the search by image endpoint, an image in JPEG format must be uploaded to &#x60;https://api.gettyimages.com/v3/search/by-image/uploads/{CLIENT_IMAGE.jpg}&#x60;, where the client defines the &#x60;{CLIENT_IMAGE.jpg}&#x60; portion of the URL.  For example, using cURL:  &#x60;&#x60;&#x60; sh curl -i -X PUT https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg -H &#39;Content-Type: image/jpeg&#39; -H &#39;Api-Key: API_KEY&#39; --data-binary \&quot;@testimage.jpg\&quot; &#x60;&#x60;&#x60;  Once the image has been uploaded, use the full URL in the &#x60;image_url&#x60; parameter, e.g. &#x60;image_url&#x3D;https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg&#x60;.  - Uploaded files must be 10MB or smaller. - Uploads to the same URL will overwrite each other, so ensure that the client application is handling naming uniqueness appropriately. - Uploads expire after 24 hours. - Uploads and searches must be performed using the _same_ API Key.  ## Searching by asset id  When searching by &#x60;asset_id&#x60;, any image or video asset id in the Getty/iStock catalog can be used as the source for similar images. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    String assetId = "assetId_example"; // String | Specifies the Getty image id to use in the search.
    Boolean excludeEditorialUseOnly = true; // Boolean | Exclude images that are only available for editorial (non-commercial) use. Default value is false.
    List<CreateImageSearchFacetsFields> facetFields = Arrays.asList(); // List<CreateImageSearchFacetsFields> | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \"true\" for facets to be returned.
    Integer facetMaxCount = 300; // Integer | Specifies the maximum number of facets to return per type. Default is 300.
    List<CreativeImagesFieldValues> fields = Arrays.asList(); // List<CreativeImagesFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
    String imageUrl = "imageUrl_example"; // String | Specifies the location of the image to use in the search.
    Boolean includeFacets = true; // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
    Integer page = 1; // Integer | Request results starting at a page number (default is 1).
    Integer pageSize = 30; // Integer | Request number of images to return in each page. Default is 30, maximum page_size is 100.
    List<String> productTypes = Arrays.asList(); // List<String> | Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    try {
      SearchByImageResourceResults result = apiInstance.v3SearchImagesCreativeByImageGet(acceptLanguage, giCountryCode, assetId, excludeEditorialUseOnly, facetFields, facetMaxCount, fields, imageUrl, includeFacets, page, pageSize, productTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchImagesCreativeByImageGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **assetId** | **String**| Specifies the Getty image id to use in the search. | [optional] |
| **excludeEditorialUseOnly** | **Boolean**| Exclude images that are only available for editorial (non-commercial) use. Default value is false. | [optional] |
| **facetFields** | [**List&lt;CreateImageSearchFacetsFields&gt;**](CreateImageSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] |
| **facetMaxCount** | **Integer**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300] |
| **fields** | [**List&lt;CreativeImagesFieldValues&gt;**](CreativeImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] |
| **imageUrl** | **String**| Specifies the location of the image to use in the search. | [optional] |
| **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] |
| **page** | **Integer**| Request results starting at a page number (default is 1). | [optional] [default to 1] |
| **pageSize** | **Integer**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] |

### Return type

[**SearchByImageResourceResults**](SearchByImageResourceResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | AssetNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3SearchImagesCreativeGet"></a>
# **v3SearchImagesCreativeGet**
> CreativeImageSearchResults v3SearchImagesCreativeGet(acceptLanguage, giCountryCode, ageOfPeople, artists, collectionCodes, collectionsFilterType, color, compositions, downloadProduct, embedContentOnly, ethnicity, excludeKeywordIds, excludeNudity, excludeEditorialUseOnly, fields, fileTypes, graphicalStyles, graphicalStylesFilterType, includeRelatedSearches, keywordIds, minimumSize, numberOfPeople, orientations, page, pageSize, phrase, safeSearch, sortOrder, facetFields, includeFacets, facetMaxCount)

Search for creative images only

Use this endpoint to search our contemporary stock photos, illustrations and archival images.  You&#39;ll need an API key and access token to use this resource.   You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to  build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to  build a detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image  in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    List<AgeOfPeopleFilterType> ageOfPeople = Arrays.asList(); // List<AgeOfPeopleFilterType> | Filter based on the age of individuals in an image.
    String artists = "artists_example"; // String | Search for images by specific artists (free-text, comma-separated list of artists).
    List<String> collectionCodes = Arrays.asList(); // List<String> | Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type.
    CollectionsFilterType collectionsFilterType = CollectionsFilterType.fromValue("include"); // CollectionsFilterType | Use to include or exclude collections from search. The default is include
    String color = "color_example"; // String | Filter based on predominant color in an image. Use 6 character hexadecimal format (e.g., #002244).
    List<CompositionsFilterType> compositions = Arrays.asList(); // List<CompositionsFilterType> | Filter based on image composition.
    String downloadProduct = "downloadProduct_example"; // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    Boolean embedContentOnly = false; // Boolean | Restrict search results to embeddable images. The default is false.
    List<EthnicityFilterType> ethnicity = Arrays.asList(); // List<EthnicityFilterType> | Filter search results based on the ethnicity of individuals in an image.
    List<Integer> excludeKeywordIds = Arrays.asList(); // List<Integer> | Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned.
    Boolean excludeNudity = false; // Boolean | Excludes images containing nudity. The default is false.
    Boolean excludeEditorialUseOnly = true; // Boolean | Exclude images that are only available for editorial (non-commercial) use. Default value is false.
    List<CreativeImagesFieldValues> fields = Arrays.asList(); // List<CreativeImagesFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
    List<SearchFileType> fileTypes = Arrays.asList(); // List<SearchFileType> | Return only images having a specific file type.
    List<GraphicalStyle> graphicalStyles = Arrays.asList(); // List<GraphicalStyle> | Filter based on graphical style of the image.
    GraphicalStylesFilterType graphicalStylesFilterType = GraphicalStylesFilterType.fromValue("include"); // GraphicalStylesFilterType | Provides searching based on specified graphical style(s). The default is include.
    Boolean includeRelatedSearches = false; // Boolean | Specifies whether or not to include related searches in the response. The default is false.
    List<Integer> keywordIds = Arrays.asList(); // List<Integer> | Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
    TeeShirtSize minimumSize = TeeShirtSize.fromValue("x_small"); // TeeShirtSize | Filter based on minimum size requested. The default is x-small.
    List<NumberOfPeopleFilterType> numberOfPeople = Arrays.asList(); // List<NumberOfPeopleFilterType> | Filter based on the number of people in the image.
    List<ImageOrientationRequest> orientations = Arrays.asList(); // List<ImageOrientationRequest> | Return only images with selected aspect ratios.
    Integer page = 1; // Integer | Request results starting at a page number (default is 1).
    Integer pageSize = 30; // Integer | Request number of images to return in each page. Default is 30, maximum page_size is 100.
    String phrase = ""; // String | Search images using a search phrase.
    Boolean safeSearch = false; // Boolean | Setting safe_search to \"true\" excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it's possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative.
    CreativeImageSortOrder sortOrder = CreativeImageSortOrder.fromValue("best_match"); // CreativeImageSortOrder | Select sort order of results.  The default is best_match
    List<CreateImageSearchFacetsFields> facetFields = Arrays.asList(); // List<CreateImageSearchFacetsFields> | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
    Boolean includeFacets = true; // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
    Integer facetMaxCount = 300; // Integer | Specifies the maximum number of facets to return per type. Default is 300.
    try {
      CreativeImageSearchResults result = apiInstance.v3SearchImagesCreativeGet(acceptLanguage, giCountryCode, ageOfPeople, artists, collectionCodes, collectionsFilterType, color, compositions, downloadProduct, embedContentOnly, ethnicity, excludeKeywordIds, excludeNudity, excludeEditorialUseOnly, fields, fileTypes, graphicalStyles, graphicalStylesFilterType, includeRelatedSearches, keywordIds, minimumSize, numberOfPeople, orientations, page, pageSize, phrase, safeSearch, sortOrder, facetFields, includeFacets, facetMaxCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchImagesCreativeGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **ageOfPeople** | [**List&lt;AgeOfPeopleFilterType&gt;**](AgeOfPeopleFilterType.md)| Filter based on the age of individuals in an image. | [optional] |
| **artists** | **String**| Search for images by specific artists (free-text, comma-separated list of artists). | [optional] |
| **collectionCodes** | [**List&lt;String&gt;**](String.md)| Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type. | [optional] |
| **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] [enum: include, exclude] |
| **color** | **String**| Filter based on predominant color in an image. Use 6 character hexadecimal format (e.g., #002244). | [optional] |
| **compositions** | [**List&lt;CompositionsFilterType&gt;**](CompositionsFilterType.md)| Filter based on image composition. | [optional] |
| **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] |
| **embedContentOnly** | **Boolean**| Restrict search results to embeddable images. The default is false. | [optional] [default to false] |
| **ethnicity** | [**List&lt;EthnicityFilterType&gt;**](EthnicityFilterType.md)| Filter search results based on the ethnicity of individuals in an image. | [optional] |
| **excludeKeywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned. | [optional] |
| **excludeNudity** | **Boolean**| Excludes images containing nudity. The default is false. | [optional] [default to false] |
| **excludeEditorialUseOnly** | **Boolean**| Exclude images that are only available for editorial (non-commercial) use. Default value is false. | [optional] |
| **fields** | [**List&lt;CreativeImagesFieldValues&gt;**](CreativeImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] |
| **fileTypes** | [**List&lt;SearchFileType&gt;**](SearchFileType.md)| Return only images having a specific file type. | [optional] |
| **graphicalStyles** | [**List&lt;GraphicalStyle&gt;**](GraphicalStyle.md)| Filter based on graphical style of the image. | [optional] |
| **graphicalStylesFilterType** | [**GraphicalStylesFilterType**](.md)| Provides searching based on specified graphical style(s). The default is include. | [optional] [enum: include, exclude] |
| **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false] |
| **keywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned. | [optional] |
| **minimumSize** | [**TeeShirtSize**](.md)| Filter based on minimum size requested. The default is x-small. | [optional] [enum: x_small, small, medium, large, x_large, xx_large, vector] |
| **numberOfPeople** | [**List&lt;NumberOfPeopleFilterType&gt;**](NumberOfPeopleFilterType.md)| Filter based on the number of people in the image. | [optional] |
| **orientations** | [**List&lt;ImageOrientationRequest&gt;**](ImageOrientationRequest.md)| Return only images with selected aspect ratios. | [optional] |
| **page** | **Integer**| Request results starting at a page number (default is 1). | [optional] [default to 1] |
| **pageSize** | **Integer**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **phrase** | **String**| Search images using a search phrase. | [optional] [default to ] |
| **safeSearch** | **Boolean**| Setting safe_search to \&quot;true\&quot; excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it&#39;s possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative. | [optional] [default to false] |
| **sortOrder** | [**CreativeImageSortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] [enum: best_match, most_popular, newest, random] |
| **facetFields** | [**List&lt;CreateImageSearchFacetsFields&gt;**](CreateImageSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] |
| **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] |
| **facetMaxCount** | **Integer**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300] |

### Return type

[**CreativeImageSearchResults**](CreativeImageSearchResults.md)

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
| **500** | InvalidIStockCollection |  -  |

<a id="v3SearchImagesEditorialGet"></a>
# **v3SearchImagesEditorialGet**
> EditorialImageSearchResults v3SearchImagesEditorialGet(acceptLanguage, giCountryCode, ageOfPeople, artists, collectionCodes, collectionsFilterType, compositions, dateFrom, dateTo, downloadProduct, editorialSegments, embedContentOnly, ethnicity, eventIds, excludeKeywordIds, fields, fileTypes, graphicalStyles, graphicalStylesFilterType, includeRelatedSearches, keywordIds, minimumSize, numberOfPeople, orientations, page, pageSize, phrase, sortOrder, specificPeople, minimumQualityRank, facetFields, includeFacets, facetMaxCount)

Search for editorial images only

Use this endpoint to search our editorial stock photos, illustrations and archival images.  Editorial images represent newsworthy events or illustrate matters of general interest, such as news, sport and entertainment and are generally intended for editorial use.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token. To include your API token in the search request, add it to the headers as a Bearer token (example in curl):   -H \&quot;Authorization: Bearer &lt;your-token&gt;\&quot;  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    List<AgeOfPeopleFilterType> ageOfPeople = Arrays.asList(); // List<AgeOfPeopleFilterType> | Filter based on the age of individuals in an image.
    String artists = "artists_example"; // String | Search for images by specific artists (free-text, comma-separated list of artists).
    List<String> collectionCodes = Arrays.asList(); // List<String> | Filter by collections (comma-separated list of collection codes). Include or exclude based on collections_filter_type.
    CollectionsFilterType collectionsFilterType = CollectionsFilterType.fromValue("include"); // CollectionsFilterType | Use to include or exclude collections from search. The default is include
    List<CompositionsFilterType> compositions = Arrays.asList(); // List<CompositionsFilterType> | Filter based on image composition.
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31).
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31).
    String downloadProduct = "downloadProduct_example"; // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    List<EditorialSegmentContract> editorialSegments = Arrays.asList(); // List<EditorialSegmentContract> | Return only events with a matching editorial segment.
    Boolean embedContentOnly = false; // Boolean | Restrict search results to embeddable images. The default is false.
    List<EthnicityFilterType> ethnicity = Arrays.asList(); // List<EthnicityFilterType> | Filter search results based on the ethnicity of individuals in an image.
    List<Integer> eventIds = Arrays.asList(); // List<Integer> | Filter based on specific events
    List<Integer> excludeKeywordIds = Arrays.asList(); // List<Integer> | Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned.
    List<EditorialImagesFieldValues> fields = Arrays.asList(); // List<EditorialImagesFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
    List<SearchFileType> fileTypes = Arrays.asList(); // List<SearchFileType> | Return only images having a specific file type.
    List<EditorialGraphicalStyle> graphicalStyles = Arrays.asList(); // List<EditorialGraphicalStyle> | Filter based on graphical style of the image.
    GraphicalStylesFilterType graphicalStylesFilterType = GraphicalStylesFilterType.fromValue("include"); // GraphicalStylesFilterType | Provides searching based on specified graphical style(s). The default is include.
    Boolean includeRelatedSearches = false; // Boolean | Specifies whether or not to include related searches in the response. The default is false.
    List<Integer> keywordIds = Arrays.asList(); // List<Integer> | Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
    TeeShirtSize minimumSize = TeeShirtSize.fromValue("x_small"); // TeeShirtSize | Filter based on minimum size requested. The default is x-small.
    List<NumberOfPeopleFilterType> numberOfPeople = Arrays.asList(); // List<NumberOfPeopleFilterType> | Filter based on the number of people in the image.
    List<ImageOrientationRequest> orientations = Arrays.asList(); // List<ImageOrientationRequest> | Return only images with selected aspect ratios.
    Integer page = 1; // Integer | Request results starting at a page number (default is 1).
    Integer pageSize = 30; // Integer | Request number of images to return in each page. Default is 30, maximum page_size is 100.
    String phrase = "phrase_example"; // String | Search images using a search phrase.
    SortOrder sortOrder = SortOrder.fromValue("best_match"); // SortOrder | Select sort order of results.  The default is best_match
    List<String> specificPeople = Arrays.asList(); // List<String> | Return only images associated with specific people (using a comma-delimited list).
    Integer minimumQualityRank = 56; // Integer | Filter search results based on minimum quality ranking. Possible values 1, 2, 3 with 1 being best.
    List<EditorialImageSearchFacetsFields> facetFields = Arrays.asList(); // List<EditorialImageSearchFacetsFields> | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
    Boolean includeFacets = true; // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
    Integer facetMaxCount = 300; // Integer | Specifies the maximum number of facets to return per type. Default is 300.
    try {
      EditorialImageSearchResults result = apiInstance.v3SearchImagesEditorialGet(acceptLanguage, giCountryCode, ageOfPeople, artists, collectionCodes, collectionsFilterType, compositions, dateFrom, dateTo, downloadProduct, editorialSegments, embedContentOnly, ethnicity, eventIds, excludeKeywordIds, fields, fileTypes, graphicalStyles, graphicalStylesFilterType, includeRelatedSearches, keywordIds, minimumSize, numberOfPeople, orientations, page, pageSize, phrase, sortOrder, specificPeople, minimumQualityRank, facetFields, includeFacets, facetMaxCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchImagesEditorialGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **ageOfPeople** | [**List&lt;AgeOfPeopleFilterType&gt;**](AgeOfPeopleFilterType.md)| Filter based on the age of individuals in an image. | [optional] |
| **artists** | **String**| Search for images by specific artists (free-text, comma-separated list of artists). | [optional] |
| **collectionCodes** | [**List&lt;String&gt;**](String.md)| Filter by collections (comma-separated list of collection codes). Include or exclude based on collections_filter_type. | [optional] |
| **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] [enum: include, exclude] |
| **compositions** | [**List&lt;CompositionsFilterType&gt;**](CompositionsFilterType.md)| Filter based on image composition. | [optional] |
| **dateFrom** | **OffsetDateTime**| Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] |
| **dateTo** | **OffsetDateTime**| Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] |
| **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] |
| **editorialSegments** | [**List&lt;EditorialSegmentContract&gt;**](EditorialSegmentContract.md)| Return only events with a matching editorial segment. | [optional] |
| **embedContentOnly** | **Boolean**| Restrict search results to embeddable images. The default is false. | [optional] [default to false] |
| **ethnicity** | [**List&lt;EthnicityFilterType&gt;**](EthnicityFilterType.md)| Filter search results based on the ethnicity of individuals in an image. | [optional] |
| **eventIds** | [**List&lt;Integer&gt;**](Integer.md)| Filter based on specific events | [optional] |
| **excludeKeywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned. | [optional] |
| **fields** | [**List&lt;EditorialImagesFieldValues&gt;**](EditorialImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] |
| **fileTypes** | [**List&lt;SearchFileType&gt;**](SearchFileType.md)| Return only images having a specific file type. | [optional] |
| **graphicalStyles** | [**List&lt;EditorialGraphicalStyle&gt;**](EditorialGraphicalStyle.md)| Filter based on graphical style of the image. | [optional] |
| **graphicalStylesFilterType** | [**GraphicalStylesFilterType**](.md)| Provides searching based on specified graphical style(s). The default is include. | [optional] [enum: include, exclude] |
| **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false] |
| **keywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned. | [optional] |
| **minimumSize** | [**TeeShirtSize**](.md)| Filter based on minimum size requested. The default is x-small. | [optional] [enum: x_small, small, medium, large, x_large, xx_large, vector] |
| **numberOfPeople** | [**List&lt;NumberOfPeopleFilterType&gt;**](NumberOfPeopleFilterType.md)| Filter based on the number of people in the image. | [optional] |
| **orientations** | [**List&lt;ImageOrientationRequest&gt;**](ImageOrientationRequest.md)| Return only images with selected aspect ratios. | [optional] |
| **page** | **Integer**| Request results starting at a page number (default is 1). | [optional] [default to 1] |
| **pageSize** | **Integer**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **phrase** | **String**| Search images using a search phrase. | [optional] |
| **sortOrder** | [**SortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] [enum: best_match, most_popular, newest, oldest, random] |
| **specificPeople** | [**List&lt;String&gt;**](String.md)| Return only images associated with specific people (using a comma-delimited list). | [optional] |
| **minimumQualityRank** | **Integer**| Filter search results based on minimum quality ranking. Possible values 1, 2, 3 with 1 being best. | [optional] |
| **facetFields** | [**List&lt;EditorialImageSearchFacetsFields&gt;**](EditorialImageSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] |
| **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] |
| **facetMaxCount** | **Integer**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300] |

### Return type

[**EditorialImageSearchResults**](EditorialImageSearchResults.md)

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

<a id="v3SearchImagesGet"></a>
# **v3SearchImagesGet**
> ImageSearchItemSearchResults v3SearchImagesGet(acceptLanguage, giCountryCode, ageOfPeople, artists, collectionCodes, collectionsFilterType, color, compositions, downloadProduct, embedContentOnly, eventIds, ethnicity, excludeNudity, fields, fileTypes, graphicalStyles, graphicalStylesFilterType, includeRelatedSearches, keywordIds, minimumSize, numberOfPeople, orientations, page, pageSize, phrase, sortOrder, specificPeople)

Search for both creative and editorial images - *** DEPRECATED ***

## _This endpoint draws from such a large diversity of content, the results will not be as relevant as when the more specific Creative or Editorial endpoints are used. Additionally, the response time for this endpoint is slower compared to that for Creative and Editorial-specific endpoints. For these reasons,_ _**it is highly recommended that those endpoints are used instead of this blended endpoint.**_    You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.&lt;br&gt; To include your API token in the search request, add it to the headers as a Bearer token (example in curl):   -H \&quot;Authorization: Bearer &lt;your-token&gt;\&quot;  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of images.  The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most  frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    List<AgeOfPeopleFilterType> ageOfPeople = Arrays.asList(); // List<AgeOfPeopleFilterType> | Filter based on the age of individuals in an image.
    String artists = "artists_example"; // String | Search for images by specific artists (free-text, comma-separated list of artists).
    List<String> collectionCodes = Arrays.asList(); // List<String> | Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type.
    CollectionsFilterType collectionsFilterType = CollectionsFilterType.fromValue("include"); // CollectionsFilterType | Provides searching based on specified collection(s). The default is Include
    String color = "color_example"; // String | Filter based on predominant color in an image. Use 6 character hexidecimal format (e.g., #002244). Note: when specified, results will not contain editorial images.
    List<CompositionsFilterType> compositions = Arrays.asList(); // List<CompositionsFilterType> | Filter based on image composition.
    String downloadProduct = "downloadProduct_example"; // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    Boolean embedContentOnly = false; // Boolean | Restrict search results to embeddable images. The default is false.
    List<Integer> eventIds = Arrays.asList(); // List<Integer> | Filter based on specific events
    List<EthnicityFilterType> ethnicity = Arrays.asList(); // List<EthnicityFilterType> | Filter search results based on the ethnicity of individuals in an image.
    Boolean excludeNudity = false; // Boolean | Excludes images containing nudity. The default is false.
    List<ImagesFieldValues> fields = Arrays.asList(); // List<ImagesFieldValues> | Specifies fields to return. Defaults to 'summary_set'.
    List<SearchFileType> fileTypes = Arrays.asList(); // List<SearchFileType> | Return only images having a specific file type.
    List<GraphicalStyle> graphicalStyles = Arrays.asList(); // List<GraphicalStyle> | Filter based on graphical style of the image.
    GraphicalStylesFilterType graphicalStylesFilterType = GraphicalStylesFilterType.fromValue("include"); // GraphicalStylesFilterType | Provides searching based on specified graphical style(s). The default is Include
    Boolean includeRelatedSearches = false; // Boolean | Specifies whether or not to include related searches in the response. The default is false.
    List<Integer> keywordIds = Arrays.asList(); // List<Integer> | Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
    TeeShirtSize minimumSize = TeeShirtSize.fromValue("x_small"); // TeeShirtSize | Filter based on minimum size requested. The default is x-small
    List<NumberOfPeopleFilterType> numberOfPeople = Arrays.asList(); // List<NumberOfPeopleFilterType> | Filter based on the number of people in the image.
    List<ImageOrientationRequest> orientations = Arrays.asList(); // List<ImageOrientationRequest> | Return only images with selected aspect ratios.
    Integer page = 1; // Integer | Request results starting at a page number (default is 1).
    Integer pageSize = 30; // Integer | Request number of images to return in each page. Default is 30, maximum page_size is 100.
    String phrase = "phrase_example"; // String | Search images using a search phrase.
    BlendedImageSortOrder sortOrder = BlendedImageSortOrder.fromValue("best_match"); // BlendedImageSortOrder | Select sort order of results.  The default is best_match
    List<String> specificPeople = Arrays.asList(); // List<String> | Return only images associated with specific people (using a comma-delimited list).
    try {
      ImageSearchItemSearchResults result = apiInstance.v3SearchImagesGet(acceptLanguage, giCountryCode, ageOfPeople, artists, collectionCodes, collectionsFilterType, color, compositions, downloadProduct, embedContentOnly, eventIds, ethnicity, excludeNudity, fields, fileTypes, graphicalStyles, graphicalStylesFilterType, includeRelatedSearches, keywordIds, minimumSize, numberOfPeople, orientations, page, pageSize, phrase, sortOrder, specificPeople);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchImagesGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **ageOfPeople** | [**List&lt;AgeOfPeopleFilterType&gt;**](AgeOfPeopleFilterType.md)| Filter based on the age of individuals in an image. | [optional] |
| **artists** | **String**| Search for images by specific artists (free-text, comma-separated list of artists). | [optional] |
| **collectionCodes** | [**List&lt;String&gt;**](String.md)| Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type. | [optional] |
| **collectionsFilterType** | [**CollectionsFilterType**](.md)| Provides searching based on specified collection(s). The default is Include | [optional] [enum: include, exclude] |
| **color** | **String**| Filter based on predominant color in an image. Use 6 character hexidecimal format (e.g., #002244). Note: when specified, results will not contain editorial images. | [optional] |
| **compositions** | [**List&lt;CompositionsFilterType&gt;**](CompositionsFilterType.md)| Filter based on image composition. | [optional] |
| **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] |
| **embedContentOnly** | **Boolean**| Restrict search results to embeddable images. The default is false. | [optional] [default to false] |
| **eventIds** | [**List&lt;Integer&gt;**](Integer.md)| Filter based on specific events | [optional] |
| **ethnicity** | [**List&lt;EthnicityFilterType&gt;**](EthnicityFilterType.md)| Filter search results based on the ethnicity of individuals in an image. | [optional] |
| **excludeNudity** | **Boolean**| Excludes images containing nudity. The default is false. | [optional] [default to false] |
| **fields** | [**List&lt;ImagesFieldValues&gt;**](ImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. | [optional] |
| **fileTypes** | [**List&lt;SearchFileType&gt;**](SearchFileType.md)| Return only images having a specific file type. | [optional] |
| **graphicalStyles** | [**List&lt;GraphicalStyle&gt;**](GraphicalStyle.md)| Filter based on graphical style of the image. | [optional] |
| **graphicalStylesFilterType** | [**GraphicalStylesFilterType**](.md)| Provides searching based on specified graphical style(s). The default is Include | [optional] [enum: include, exclude] |
| **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false] |
| **keywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned. | [optional] |
| **minimumSize** | [**TeeShirtSize**](.md)| Filter based on minimum size requested. The default is x-small | [optional] [enum: x_small, small, medium, large, x_large, xx_large, vector] |
| **numberOfPeople** | [**List&lt;NumberOfPeopleFilterType&gt;**](NumberOfPeopleFilterType.md)| Filter based on the number of people in the image. | [optional] |
| **orientations** | [**List&lt;ImageOrientationRequest&gt;**](ImageOrientationRequest.md)| Return only images with selected aspect ratios. | [optional] |
| **page** | **Integer**| Request results starting at a page number (default is 1). | [optional] [default to 1] |
| **pageSize** | **Integer**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **phrase** | **String**| Search images using a search phrase. | [optional] |
| **sortOrder** | [**BlendedImageSortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] [enum: best_match, most_popular, newest, random] |
| **specificPeople** | [**List&lt;String&gt;**](String.md)| Return only images associated with specific people (using a comma-delimited list). | [optional] |

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

<a id="v3SearchVideosCreativeByImageGet"></a>
# **v3SearchVideosCreativeByImageGet**
> CreativeVideoSearchResults v3SearchVideosCreativeByImageGet(acceptLanguage, giCountryCode, assetId, excludeEditorialUseOnly, facetFields, facetMaxCount, fields, imageUrl, includeFacets, page, pageSize, productTypes)

Search for creative videos based on url

Search for **similar creative videos** by passing an &#x60;image_url&#x60; to an uploaded image/frame grab from a video OR an &#x60;asset_id&#x60; of an asset in our catalog.  All responses will have the &#x60;exclude_nudity&#x60; filter automatically applied.  ## Searching by URL  Before calling the search by image endpoint, an image or frame grab in JPEG format must be uploaded to &#x60;https://api.gettyimages.com/v3/search/by-image/uploads/{CLIENT_IMAGE.jpg}&#x60;, where the client defines the &#x60;{CLIENT_IMAGE.jpg}&#x60; portion of the URL.  For example, using cURL:  &#x60;&#x60;&#x60; sh curl -i -X PUT https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg -H &#39;Content-Type: image/jpeg&#39; -H &#39;Api-Key: API_KEY&#39; --data-binary \&quot;@testimage.jpg\&quot; &#x60;&#x60;&#x60;  Once the image has been uploaded, use the full URL in the &#x60;image_url&#x60; parameter, e.g. &#x60;image_url&#x3D;https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg&#x60;.  - Uploaded files must be 10MB or smaller - Uploads to the same URL will overwrite each other, so ensure that the client application is handling naming uniqueness appropriately. - Uploads expire after 24 hours. - Uploads and searches must be performed using the _same_ API Key.  ## Searching by asset id  When searching by &#x60;asset_id&#x60;, any image or video asset id in the Getty/iStock catalog can be used as the source for similar videos. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    String assetId = "assetId_example"; // String | Specifies the Getty video id to use in the search.
    Boolean excludeEditorialUseOnly = true; // Boolean | Exclude videos that are only available for editorial (non-commercial) use. Default value is false.
    List<CreateVideoSearchFacetsFields> facetFields = Arrays.asList(); // List<CreateVideoSearchFacetsFields> | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \"true\" for facets to be returned.
    Integer facetMaxCount = 300; // Integer | Specifies the maximum number of facets to return per type. Default is 300.
    List<CreativeVideosFieldValues> fields = Arrays.asList(); // List<CreativeVideosFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
    String imageUrl = "imageUrl_example"; // String | Specifies the location of the image to use in the search.
    Boolean includeFacets = true; // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
    Integer page = 1; // Integer | Request results starting at a page number (default is 1).
    Integer pageSize = 30; // Integer | Request number of images to return in each page. Default is 30, maximum page_size is 100.
    List<String> productTypes = Arrays.asList(); // List<String> | Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    try {
      CreativeVideoSearchResults result = apiInstance.v3SearchVideosCreativeByImageGet(acceptLanguage, giCountryCode, assetId, excludeEditorialUseOnly, facetFields, facetMaxCount, fields, imageUrl, includeFacets, page, pageSize, productTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchVideosCreativeByImageGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **assetId** | **String**| Specifies the Getty video id to use in the search. | [optional] |
| **excludeEditorialUseOnly** | **Boolean**| Exclude videos that are only available for editorial (non-commercial) use. Default value is false. | [optional] |
| **facetFields** | [**List&lt;CreateVideoSearchFacetsFields&gt;**](CreateVideoSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] |
| **facetMaxCount** | **Integer**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300] |
| **fields** | [**List&lt;CreativeVideosFieldValues&gt;**](CreativeVideosFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] |
| **imageUrl** | **String**| Specifies the location of the image to use in the search. | [optional] |
| **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] |
| **page** | **Integer**| Request results starting at a page number (default is 1). | [optional] [default to 1] |
| **pageSize** | **Integer**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] |

### Return type

[**CreativeVideoSearchResults**](CreativeVideoSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | UnauthorizedDisplaySize |  -  |
| **404** | AssetNotFound |  -  |
| **500** | InvalidIStockCollection |  -  |

<a id="v3SearchVideosCreativeGet"></a>
# **v3SearchVideosCreativeGet**
> CreativeVideoSearchResults v3SearchVideosCreativeGet(acceptLanguage, giCountryCode, ageOfPeople, artists, aspectRatios, collectionCodes, collectionsFilterType, compositions, downloadProduct, excludeNudity, excludeEditorialUseOnly, excludeKeywordIds, fields, formatAvailable, frameRates, imageTechniques, includeRelatedSearches, keywordIds, licenseModels, orientations, minClipLength, maxClipLength, page, pageSize, phrase, safeSearch, sortOrder, releaseStatus, facetFields, facetMaxCount, includeFacets, viewpoints)

Search for creative videos

Use this endpoint to search premium stock video, from archival film to contemporary 4K and HD footage.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only  assets that you have a license to use, you need to also include an authorization token in the header of your request. Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,          \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,    \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,          \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;era\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files  that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result  set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    List<AgeOfPeopleFilterType> ageOfPeople = Arrays.asList(); // List<AgeOfPeopleFilterType> | Provides filtering according to the age of individuals in a video.
    String artists = "artists_example"; // String | Search for videos by specific artists (free-text, comma-separated list of artists).
    List<VideoAspectRatioFilterType> aspectRatios = Arrays.asList(); // List<VideoAspectRatioFilterType> | Search for videos by specific aspect ratios.
    List<String> collectionCodes = Arrays.asList(); // List<String> | Provides filtering by collection code.
    CollectionsFilterType collectionsFilterType = CollectionsFilterType.fromValue("include"); // CollectionsFilterType | Use to include or exclude collections from search. The default is include
    List<CompositionsFilterType> compositions = Arrays.asList(); // List<CompositionsFilterType> | Filter based on video composition.
    String downloadProduct = "downloadProduct_example"; // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    Boolean excludeNudity = false; // Boolean | Excludes videos containing nudity. The default is false.
    Boolean excludeEditorialUseOnly = true; // Boolean | Exclude videos that are only available for editorial (non-commercial) use. Default value is false.
    List<Integer> excludeKeywordIds = Arrays.asList(); // List<Integer> | Return only videos not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also do not contain the requested keyword(s) are returned.
    List<CreativeVideosFieldValues> fields = Arrays.asList(); // List<CreativeVideosFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
    VideoFormatsRequest formatAvailable = VideoFormatsRequest.fromValue("sd"); // VideoFormatsRequest | Filters according to the digital video format available on a film asset.
    List<VideoFrameRates> frameRates = Arrays.asList(); // List<VideoFrameRates> | Provides filtering by video frame rate (frames/second).
    List<ImageTechniquesFilterType> imageTechniques = Arrays.asList(); // List<ImageTechniquesFilterType> | Filter based on image technique.
    Boolean includeRelatedSearches = false; // Boolean | Specifies whether or not to include related searches in the response. The default is false.
    List<Integer> keywordIds = Arrays.asList(); // List<Integer> | Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned.
    List<LicenseModelVideoRequest> licenseModels = Arrays.asList(); // List<LicenseModelVideoRequest> | Specifies the video licensing model(s).
    List<VideoOrientationRequest> orientations = Arrays.asList(); // List<VideoOrientationRequest> | Return only videos with selected orientations.
    Integer minClipLength = 0; // Integer | Provides filtering by minimum length of video clip, in seconds
    Integer maxClipLength = 0; // Integer | Provides filtering by maximum length of video, in seconds
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 30; // Integer | Specifies page size. Default is 30, maximum page_size is 100.
    String phrase = ""; // String | Free-text search query.
    Boolean safeSearch = false; // Boolean | Setting safe_search to \"true\" excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it's possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative.
    CreativeVideoSortOrder sortOrder = CreativeVideoSortOrder.fromValue("best_match"); // CreativeVideoSortOrder | Select sort order of results.  The default is best_match
    ReleaseStatus releaseStatus = ReleaseStatus.fromValue("release_not_important"); // ReleaseStatus | Allows filtering by type of model release.
    List<CreateVideoSearchFacetsFields> facetFields = Arrays.asList(); // List<CreateVideoSearchFacetsFields> | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
    Integer facetMaxCount = 300; // Integer | Specifies the maximum number of facets to return per type. Default is 300.
    Boolean includeFacets = true; // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
    List<ViewpointsFilterType> viewpoints = Arrays.asList(); // List<ViewpointsFilterType> | Filter based on viewpoint.
    try {
      CreativeVideoSearchResults result = apiInstance.v3SearchVideosCreativeGet(acceptLanguage, giCountryCode, ageOfPeople, artists, aspectRatios, collectionCodes, collectionsFilterType, compositions, downloadProduct, excludeNudity, excludeEditorialUseOnly, excludeKeywordIds, fields, formatAvailable, frameRates, imageTechniques, includeRelatedSearches, keywordIds, licenseModels, orientations, minClipLength, maxClipLength, page, pageSize, phrase, safeSearch, sortOrder, releaseStatus, facetFields, facetMaxCount, includeFacets, viewpoints);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchVideosCreativeGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **ageOfPeople** | [**List&lt;AgeOfPeopleFilterType&gt;**](AgeOfPeopleFilterType.md)| Provides filtering according to the age of individuals in a video. | [optional] |
| **artists** | **String**| Search for videos by specific artists (free-text, comma-separated list of artists). | [optional] |
| **aspectRatios** | [**List&lt;VideoAspectRatioFilterType&gt;**](VideoAspectRatioFilterType.md)| Search for videos by specific aspect ratios. | [optional] |
| **collectionCodes** | [**List&lt;String&gt;**](String.md)| Provides filtering by collection code. | [optional] |
| **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] [enum: include, exclude] |
| **compositions** | [**List&lt;CompositionsFilterType&gt;**](CompositionsFilterType.md)| Filter based on video composition. | [optional] |
| **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] |
| **excludeNudity** | **Boolean**| Excludes videos containing nudity. The default is false. | [optional] [default to false] |
| **excludeEditorialUseOnly** | **Boolean**| Exclude videos that are only available for editorial (non-commercial) use. Default value is false. | [optional] |
| **excludeKeywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only videos not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also do not contain the requested keyword(s) are returned. | [optional] |
| **fields** | [**List&lt;CreativeVideosFieldValues&gt;**](CreativeVideosFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] |
| **formatAvailable** | [**VideoFormatsRequest**](.md)| Filters according to the digital video format available on a film asset. | [optional] [enum: sd, hd, 4k, hd_web] |
| **frameRates** | [**List&lt;VideoFrameRates&gt;**](VideoFrameRates.md)| Provides filtering by video frame rate (frames/second). | [optional] |
| **imageTechniques** | [**List&lt;ImageTechniquesFilterType&gt;**](ImageTechniquesFilterType.md)| Filter based on image technique. | [optional] |
| **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false] |
| **keywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned. | [optional] |
| **licenseModels** | [**List&lt;LicenseModelVideoRequest&gt;**](LicenseModelVideoRequest.md)| Specifies the video licensing model(s). | [optional] |
| **orientations** | [**List&lt;VideoOrientationRequest&gt;**](VideoOrientationRequest.md)| Return only videos with selected orientations. | [optional] |
| **minClipLength** | **Integer**| Provides filtering by minimum length of video clip, in seconds | [optional] [default to 0] |
| **maxClipLength** | **Integer**| Provides filtering by maximum length of video, in seconds | [optional] [default to 0] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **phrase** | **String**| Free-text search query. | [optional] [default to ] |
| **safeSearch** | **Boolean**| Setting safe_search to \&quot;true\&quot; excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it&#39;s possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative. | [optional] [default to false] |
| **sortOrder** | [**CreativeVideoSortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] [enum: best_match, most_popular, newest, random] |
| **releaseStatus** | [**ReleaseStatus**](.md)| Allows filtering by type of model release. | [optional] [enum: release_not_important, fully_released] |
| **facetFields** | [**List&lt;CreateVideoSearchFacetsFields&gt;**](CreateVideoSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] |
| **facetMaxCount** | **Integer**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300] |
| **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] |
| **viewpoints** | [**List&lt;ViewpointsFilterType&gt;**](ViewpointsFilterType.md)| Filter based on viewpoint. | [optional] |

### Return type

[**CreativeVideoSearchResults**](CreativeVideoSearchResults.md)

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
| **500** | InvalidIStockCollection |  -  |

<a id="v3SearchVideosEditorialGet"></a>
# **v3SearchVideosEditorialGet**
> EditorialVideoSearchResults v3SearchVideosEditorialGet(acceptLanguage, giCountryCode, ageOfPeople, artists, aspectRatios, collectionCodes, collectionsFilterType, compositions, dateFrom, dateTo, downloadProduct, editorialVideoTypes, fields, formatAvailable, frameRates, imageTechniques, includeRelatedSearches, keywordIds, minClipLength, maxClipLength, orientations, page, pageSize, phrase, sortOrder, specificPeople, releaseStatus, facetFields, includeFacets, facetMaxCount, viewpoints)

Search for editorial videos

Use this endpoint to search current and archival video clips of celebrities, newsmakers, and events.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,          \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,    \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,          \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;era\&quot;,         \&quot;event_ids\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String giCountryCode = "giCountryCode_example"; // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
    List<AgeOfPeopleFilterType> ageOfPeople = Arrays.asList(); // List<AgeOfPeopleFilterType> | Provides filtering according to the age of individuals in a video.
    String artists = "artists_example"; // String | Search for videos by specific artists (free-text, comma-separated list of artists).
    List<VideoAspectRatioFilterType> aspectRatios = Arrays.asList(); // List<VideoAspectRatioFilterType> | Search for videos by specific aspect ratios.
    List<String> collectionCodes = Arrays.asList(); // List<String> | Provides filtering by collection code.
    CollectionsFilterType collectionsFilterType = CollectionsFilterType.fromValue("include"); // CollectionsFilterType | Use to include or exclude collections from search. The default is include
    List<CompositionsFilterType> compositions = Arrays.asList(); // List<CompositionsFilterType> | Filter based on video composition.
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31).
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31).
    String downloadProduct = "downloadProduct_example"; // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
    List<EditorialVideoType> editorialVideoTypes = Arrays.asList(); // List<EditorialVideoType> | Allows filtering by types of video.
    List<EditorialVideosFieldValues> fields = Arrays.asList(); // List<EditorialVideosFieldValues> | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
    VideoFormatsRequest formatAvailable = VideoFormatsRequest.fromValue("sd"); // VideoFormatsRequest | Filters according to the digital video format available on a film asset.
    List<VideoFrameRates> frameRates = Arrays.asList(); // List<VideoFrameRates> | Provides filtering by video frame rate (frames/second).
    List<ImageTechniquesFilterType> imageTechniques = Arrays.asList(); // List<ImageTechniquesFilterType> | Filter based on image technique.
    Boolean includeRelatedSearches = false; // Boolean | Specifies whether or not to include related searches in the response. The default is false.
    List<Integer> keywordIds = Arrays.asList(); // List<Integer> | Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned.
    Integer minClipLength = 0; // Integer | Provides filtering by minimum length of video clip, in seconds
    Integer maxClipLength = 0; // Integer | Provides filtering by maximum length of video clip, in seconds
    List<VideoOrientationRequest> orientations = Arrays.asList(); // List<VideoOrientationRequest> | Return only videos with selected orientations.
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 30; // Integer | Specifies page size. Default is 30, maximum page_size is 100.
    String phrase = ""; // String | Free-text search query.
    SortOrder sortOrder = SortOrder.fromValue("best_match"); // SortOrder | Select sort order of results.  The default is best_match
    List<String> specificPeople = Arrays.asList(); // List<String> | Allows filtering by specific peoples' names.
    ReleaseStatus releaseStatus = ReleaseStatus.fromValue("release_not_important"); // ReleaseStatus | Allows filtering by type of model release.
    List<EditorialVideoSearchFacetsFields> facetFields = Arrays.asList(); // List<EditorialVideoSearchFacetsFields> | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
    Boolean includeFacets = true; // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
    Integer facetMaxCount = 300; // Integer | Specifies the maximum number of facets to return per type. Default is 300.
    List<ViewpointsFilterType> viewpoints = Arrays.asList(); // List<ViewpointsFilterType> | Filter based on viewpoint.
    try {
      EditorialVideoSearchResults result = apiInstance.v3SearchVideosEditorialGet(acceptLanguage, giCountryCode, ageOfPeople, artists, aspectRatios, collectionCodes, collectionsFilterType, compositions, dateFrom, dateTo, downloadProduct, editorialVideoTypes, fields, formatAvailable, frameRates, imageTechniques, includeRelatedSearches, keywordIds, minClipLength, maxClipLength, orientations, page, pageSize, phrase, sortOrder, specificPeople, releaseStatus, facetFields, includeFacets, facetMaxCount, viewpoints);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#v3SearchVideosEditorialGet");
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
| **giCountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] |
| **ageOfPeople** | [**List&lt;AgeOfPeopleFilterType&gt;**](AgeOfPeopleFilterType.md)| Provides filtering according to the age of individuals in a video. | [optional] |
| **artists** | **String**| Search for videos by specific artists (free-text, comma-separated list of artists). | [optional] |
| **aspectRatios** | [**List&lt;VideoAspectRatioFilterType&gt;**](VideoAspectRatioFilterType.md)| Search for videos by specific aspect ratios. | [optional] |
| **collectionCodes** | [**List&lt;String&gt;**](String.md)| Provides filtering by collection code. | [optional] |
| **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] [enum: include, exclude] |
| **compositions** | [**List&lt;CompositionsFilterType&gt;**](CompositionsFilterType.md)| Filter based on video composition. | [optional] |
| **dateFrom** | **OffsetDateTime**| Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] |
| **dateTo** | **OffsetDateTime**| Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] |
| **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] |
| **editorialVideoTypes** | [**List&lt;EditorialVideoType&gt;**](EditorialVideoType.md)| Allows filtering by types of video. | [optional] |
| **fields** | [**List&lt;EditorialVideosFieldValues&gt;**](EditorialVideosFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] |
| **formatAvailable** | [**VideoFormatsRequest**](.md)| Filters according to the digital video format available on a film asset. | [optional] [enum: sd, hd, 4k, hd_web] |
| **frameRates** | [**List&lt;VideoFrameRates&gt;**](VideoFrameRates.md)| Provides filtering by video frame rate (frames/second). | [optional] |
| **imageTechniques** | [**List&lt;ImageTechniquesFilterType&gt;**](ImageTechniquesFilterType.md)| Filter based on image technique. | [optional] |
| **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false] |
| **keywordIds** | [**List&lt;Integer&gt;**](Integer.md)| Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned. | [optional] |
| **minClipLength** | **Integer**| Provides filtering by minimum length of video clip, in seconds | [optional] [default to 0] |
| **maxClipLength** | **Integer**| Provides filtering by maximum length of video clip, in seconds | [optional] [default to 0] |
| **orientations** | [**List&lt;VideoOrientationRequest&gt;**](VideoOrientationRequest.md)| Return only videos with selected orientations. | [optional] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **phrase** | **String**| Free-text search query. | [optional] [default to ] |
| **sortOrder** | [**SortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] [enum: best_match, most_popular, newest, oldest, random] |
| **specificPeople** | [**List&lt;String&gt;**](String.md)| Allows filtering by specific peoples&#39; names. | [optional] |
| **releaseStatus** | [**ReleaseStatus**](.md)| Allows filtering by type of model release. | [optional] [enum: release_not_important, fully_released] |
| **facetFields** | [**List&lt;EditorialVideoSearchFacetsFields&gt;**](EditorialVideoSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] |
| **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] |
| **facetMaxCount** | **Integer**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300] |
| **viewpoints** | [**List&lt;ViewpointsFilterType&gt;**](ViewpointsFilterType.md)| Filter based on viewpoint. | [optional] |

### Return type

[**EditorialVideoSearchResults**](EditorialVideoSearchResults.md)

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

