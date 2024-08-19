# DownloadsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3DownloadsGet**](DownloadsApi.md#v3DownloadsGet) | **GET** /v3/downloads | Returns information about a customer&#39;s downloaded assets. |
| [**v3DownloadsImagesIdPost**](DownloadsApi.md#v3DownloadsImagesIdPost) | **POST** /v3/downloads/images/{id} | Download an image |
| [**v3DownloadsVideosIdPost**](DownloadsApi.md#v3DownloadsVideosIdPost) | **POST** /v3/downloads/videos/{id} | Download a video |


<a id="v3DownloadsGet"></a>
# **v3DownloadsGet**
> GetDownloadsResponse v3DownloadsGet(acceptLanguage, dateFrom, dateTo, useTime, page, pageSize, productType, companyDownloads)

Returns information about a customer&#39;s downloaded assets.

Returns information about a customer&#39;s previously downloaded assets.  You&#39;ll need an API key and access token to use this resource.     This endpoint requires being a Getty Images customer to limit your results to only assets that you have a license to use,  you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

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

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | If specified, selects assets downloaded on or after this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD).   Any hour, minute, second values in the request are not used, unless useTimePart parameter is included.  Date/times in the response are UTC. Default is 30 days prior to date_to
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | If specified, selects assets downloaded on or before this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD)  Any hour, minute, second values in the request are not used, unless useTimePart parameter is included.  Date/times in the response are UTC. Default is current date or 30 days after specified start date, whichever one is earlier.
    Boolean useTime = false; // Boolean | If specified, time values provided with date_to or date_from will be used. Time values should be appended to the date value in ISO 8601 format  i.e.: 2019-09-19T19:30:37 or 2019-09-19 19:30:37.  Time zone can be specified as optional.  Default value is false
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 30; // Integer | Specifies page size. Default is 30, maximum page_size is 100.
    ProductTypeForDownloads productType = ProductTypeForDownloads.fromValue("easyaccess"); // ProductTypeForDownloads | Specifies product type to be included in the previous download results. Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. To get previous iStockPhoto credit downloads, creditpack must be selected.
    Boolean companyDownloads = false; // Boolean | If specified, returns the list of previously downloaded images for all users in your company. Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false.
    try {
      GetDownloadsResponse result = apiInstance.v3DownloadsGet(acceptLanguage, dateFrom, dateTo, useTime, page, pageSize, productType, companyDownloads);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#v3DownloadsGet");
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
| **dateFrom** | **OffsetDateTime**| If specified, selects assets downloaded on or after this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD).   Any hour, minute, second values in the request are not used, unless useTimePart parameter is included.  Date/times in the response are UTC. Default is 30 days prior to date_to | [optional] |
| **dateTo** | **OffsetDateTime**| If specified, selects assets downloaded on or before this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD)  Any hour, minute, second values in the request are not used, unless useTimePart parameter is included.  Date/times in the response are UTC. Default is current date or 30 days after specified start date, whichever one is earlier. | [optional] |
| **useTime** | **Boolean**| If specified, time values provided with date_to or date_from will be used. Time values should be appended to the date value in ISO 8601 format  i.e.: 2019-09-19T19:30:37 or 2019-09-19 19:30:37.  Time zone can be specified as optional.  Default value is false | [optional] [default to false] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30] |
| **productType** | [**ProductTypeForDownloads**](.md)| Specifies product type to be included in the previous download results. Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. To get previous iStockPhoto credit downloads, creditpack must be selected. | [optional] [enum: easyaccess, editorialsubscription, imagepack, premiumaccess, royaltyfreesubscription, creditpack] |
| **companyDownloads** | **Boolean**| If specified, returns the list of previously downloaded images for all users in your company. Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false. | [optional] [default to false] |

### Return type

[**GetDownloadsResponse**](GetDownloadsResponse.md)

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
| **403** | Forbidden |  -  |

<a id="v3DownloadsImagesIdPost"></a>
# **v3DownloadsImagesIdPost**
> v3DownloadsImagesIdPost(id, acceptLanguage, autoDownload, fileType, height, productId, productType, useTeamCredits, premiumAccessDownloadData)

Download an image

Use this endpoint to generate download URLs and related data for images you are authorized to download.  Most product offerings have enforced periodic download limits such as monthly, weekly, and daily. When this operation executes, the count of allowed downloads is decremented by one for the product offering. Once the download limit is reached for a given product offering, no further downloads may be requested for that product offering until the next download period.  The download limit for a given download period is covered in your product agreement established with Getty Images.  You&#39;ll need an API key and a [Resource Owner Grant or Implicit Grant](http://developers.gettyimages.com/en/authorization-faq.html) access token to use this resource.  ## Auto Downloads The &#x60;auto_download&#x60; request query parameter specifies whether to automatically download the image.  If the &#x60;auto_download&#x60; request query parameter is set to _true_, the API will return an HTTP status code 303 *See Other*. Your client code will need to process this response and redirect to the URI specified in the *Location* header to enable you to automatically download the file. The redirection workflow follows the [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4.4).  Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/images/[asset_id]?auto_download&#x3D;true &#x60;&#x60;&#x60;  Server Response:  Your client code should follow redirect (3xx) status codes returned from the URI in the response Location header. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  &#x60;&#x60;&#x60; HTTP/1.1 303 See Other Location: https://delivery.gettyimages.com/... &#x60;&#x60;&#x60;  If the &#x60;auto_download&#x60; request query parameter is set to false, the API will return a HTTP status code 200, along with the URI in the response body which can be used to download the image.   Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/images/[asset_id]?auto_download&#x3D;false &#x60;&#x60;&#x60;  Server Response:  &#x60;&#x60;&#x60; HTTP/1.1 200 OK {  \&quot;uri\&quot;: \&quot;https://delivery.gettyimages.com/...\&quot; } &#x60;&#x60;&#x60; ## Downloading Via the Returned URI  Your client code should follow redirect (3xx) status codes returned from the URI in the response. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  The URI returned by this call should be considered opaque and the format could change at any time. In order to get the filename, length or file type, the response headers must be inspected. An example response follows:  &#x60;&#x60;&#x60; content-length: 33959979 content-type: image/jpeg content-disposition: attachment; filename&#x3D;GettyImages-1167612765.jpg &#x60;&#x60;&#x60;  The &#x60;content-disposition&#x60; header must be parsed to get a usable filename.  ## Download URI expiration  Download URIs are _**only valid for 24 hours**_, starting from the moment they are returned from this call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

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

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    String id = "id_example"; // String | <remarks>                      Id of image to download.                  </remarks>
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    Boolean autoDownload = true; // Boolean | <remarks>                      Specifies whether to auto-download the image. If true is specified, a 303 SeeOther status is returned with a                      Location header set to the location of the image.                      If false is specified, the download URI will be returned in the response message. Default is true.                  </remarks>
    DownloadFileType fileType = DownloadFileType.fromValue("eps"); // DownloadFileType | <remarks>                      File Type expressed with three character file extension.                  </remarks>
    String height = "height_example"; // String | <remarks>                      Specifies the pixel height of the particular image to download.                      Available heights can be found in the images/{ids} response for the specific image.                      If left blank, it will return the largest available size.                  </remarks>
    Integer productId = 56; // Integer | <remarks>                      Identifier of the instance for the selected product offering type.                  </remarks>
    ProductTypeForDownloads productType = ProductTypeForDownloads.fromValue("easyaccess"); // ProductTypeForDownloads | <remarks>                      Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. Default product type for iStock API keys is creditpack.                  </remarks>
    Boolean useTeamCredits = false; // Boolean | Specifies whether to download the image with iStock Team Credits. Only applicable to iStock API keys authenticated with a user that has Team Credits. Blank is the same as False.
    PremiumAccessDownloadData premiumAccessDownloadData = new PremiumAccessDownloadData(); // PremiumAccessDownloadData | <remarks>                      Additional information required from specific customers when downloading.                       Only users who have been set up with a project code by Getty Images Sales need to use this field.                  </remarks>
    try {
      apiInstance.v3DownloadsImagesIdPost(id, acceptLanguage, autoDownload, fileType, height, productId, productType, useTeamCredits, premiumAccessDownloadData);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#v3DownloadsImagesIdPost");
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
| **id** | **String**| &lt;remarks&gt;                      Id of image to download.                  &lt;/remarks&gt; | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **autoDownload** | **Boolean**| &lt;remarks&gt;                      Specifies whether to auto-download the image. If true is specified, a 303 SeeOther status is returned with a                      Location header set to the location of the image.                      If false is specified, the download URI will be returned in the response message. Default is true.                  &lt;/remarks&gt; | [optional] [default to true] |
| **fileType** | [**DownloadFileType**](.md)| &lt;remarks&gt;                      File Type expressed with three character file extension.                  &lt;/remarks&gt; | [optional] [enum: eps, jpg] |
| **height** | **String**| &lt;remarks&gt;                      Specifies the pixel height of the particular image to download.                      Available heights can be found in the images/{ids} response for the specific image.                      If left blank, it will return the largest available size.                  &lt;/remarks&gt; | [optional] |
| **productId** | **Integer**| &lt;remarks&gt;                      Identifier of the instance for the selected product offering type.                  &lt;/remarks&gt; | [optional] |
| **productType** | [**ProductTypeForDownloads**](.md)| &lt;remarks&gt;                      Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. Default product type for iStock API keys is creditpack.                  &lt;/remarks&gt; | [optional] [enum: easyaccess, editorialsubscription, imagepack, premiumaccess, royaltyfreesubscription, creditpack] |
| **useTeamCredits** | **Boolean**| Specifies whether to download the image with iStock Team Credits. Only applicable to iStock API keys authenticated with a user that has Team Credits. Blank is the same as False. | [optional] [default to false] |
| **premiumAccessDownloadData** | [**PremiumAccessDownloadData**](PremiumAccessDownloadData.md)| &lt;remarks&gt;                      Additional information required from specific customers when downloading.                       Only users who have been set up with a project code by Getty Images Sales need to use this field.                  &lt;/remarks&gt; | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **303** | See Other |  -  |
| **400** | MissingRequiredQueryParameters |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | OverageLimitReached |  -  |
| **404** | ImageNotFound |  -  |

<a id="v3DownloadsVideosIdPost"></a>
# **v3DownloadsVideosIdPost**
> v3DownloadsVideosIdPost(id, acceptLanguage, autoDownload, size, productId, productType, useTeamCredits, premiumAccessDownloadData)

Download a video

Use this endpoint to generate download URLs and related data for videos you are authorized to download.  Most product offerings have enforced periodic download limits such as monthly, weekly, and daily. When this operation executes, the count of allowed downloads is decremented by one for the product offering. Once the download limit is reached for a given product offering, no further downloads may be requested for that product offering until the next download period.  The download limit for a given download period is covered in your product agreement established with Getty Images.  You&#39;ll need an API key and a [Resource Owner Grant or Implicit Grant](http://developers.gettyimages.com/en/authorization-faq.html) access token to use this resource.  ## Auto Downloads The &#x60;auto_download&#x60; request query parameter specifies whether to automatically download the video.  If the &#x60;auto_download&#x60; request query parameter is set to _true_, the API will return an HTTP status code 303 *See Other*. Your client code will need to process this response and redirect to the URI specified in the *Location* header to enable you to automatically download the file. The redirection workflow follows the [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4.4).  Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/videos/[asset_id]?auto_download&#x3D;true &#x60;&#x60;&#x60;  Server Response:  Your client code should follow redirect (3xx) status codes returned from the URI in the response Location header. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  &#x60;&#x60;&#x60; HTTP/1.1 303 See Other Location: https://delivery.gettyimages.com/... &#x60;&#x60;&#x60;  If the &#x60;auto_download&#x60; request query parameter is set to false, the API will return a HTTP status code 200, along with the URI in the response body which can be used to download the video.   Client Request:  &#x60;&#x60;&#x60; https://api.gettyimages.com/v3/downloads/videos/[asset_id]?auto_download&#x3D;false &#x60;&#x60;&#x60;  Server Response:  &#x60;&#x60;&#x60; HTTP/1.1 200 OK {  \&quot;uri\&quot;: \&quot;https://delivery.gettyimages.com/...\&quot; } &#x60;&#x60;&#x60;  ## Downloading Via the Returned URI  Your client code should follow redirect (3xx) status codes returned from the URI in the response. More information here: [HTTP 1.1 protocol](https://tools.ietf.org/html/rfc7231#section-6.4).  The URI returned by this call should be considered opaque and the format could change at any time. In order to get the filename, length or file type, the response headers must be inspected. An example response follows:  &#x60;&#x60;&#x60; content-length: 283925783 content-type: video/quicktime content-disposition: attachment; filename&#x3D;GettyImages-690773579.mov &#x60;&#x60;&#x60;  The &#x60;content-disposition&#x60; header must be parsed to get a usable filename.  ## Download URI expiration  Download URIs are _**only valid for 24 hours**_, starting from the moment they are returned from this call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

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

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    String id = "id_example"; // String | <remarks>                      Id of video to download.                  </remarks>
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    Boolean autoDownload = false; // Boolean | <remarks>                      Specifies whether to auto-download the video. If true is specified, a 303 SeeOther status is returned with a                      Location header set to the location of the video.                      If false is specified, the download URI will be returned in the response message. Default is false.                  </remarks>
    String size = "size_example"; // String | Specifies the size to be downloaded.
    Integer productId = 56; // Integer | <remarks>                      Identifier of the instance for the selected product offering type.                  </remarks>
    ProductTypeForDownloads productType = ProductTypeForDownloads.fromValue("easyaccess"); // ProductTypeForDownloads | <remarks>                      Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. Default product type for iStock API keys is creditpack.                  </remarks>
    Boolean useTeamCredits = true; // Boolean | Specifies whether to download the image with iStock Team Credits. Only applicable to iStock API keys authenticated with a user that has Team Credits. Blank is the same as False.
    PremiumAccessDownloadData premiumAccessDownloadData = new PremiumAccessDownloadData(); // PremiumAccessDownloadData | <remarks>                      Additional information required from specific customers when downloading.                       Only users who have been set up with a project code by Getty Images Sales need to use this field.                  </remarks>
    try {
      apiInstance.v3DownloadsVideosIdPost(id, acceptLanguage, autoDownload, size, productId, productType, useTeamCredits, premiumAccessDownloadData);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#v3DownloadsVideosIdPost");
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
| **id** | **String**| &lt;remarks&gt;                      Id of video to download.                  &lt;/remarks&gt; | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **autoDownload** | **Boolean**| &lt;remarks&gt;                      Specifies whether to auto-download the video. If true is specified, a 303 SeeOther status is returned with a                      Location header set to the location of the video.                      If false is specified, the download URI will be returned in the response message. Default is false.                  &lt;/remarks&gt; | [optional] [default to false] |
| **size** | **String**| Specifies the size to be downloaded. | [optional] |
| **productId** | **Integer**| &lt;remarks&gt;                      Identifier of the instance for the selected product offering type.                  &lt;/remarks&gt; | [optional] |
| **productType** | [**ProductTypeForDownloads**](.md)| &lt;remarks&gt;                      Product types easyaccess, editorialsubscription, imagepack, and premiumaccess are for GettyImages API keys. Product types royaltyfreesubscription and creditpack are for iStock API keys. Default product type for iStock API keys is creditpack.                  &lt;/remarks&gt; | [optional] [enum: easyaccess, editorialsubscription, imagepack, premiumaccess, royaltyfreesubscription, creditpack] |
| **useTeamCredits** | **Boolean**| Specifies whether to download the image with iStock Team Credits. Only applicable to iStock API keys authenticated with a user that has Team Credits. Blank is the same as False. | [optional] |
| **premiumAccessDownloadData** | [**PremiumAccessDownloadData**](PremiumAccessDownloadData.md)| &lt;remarks&gt;                      Additional information required from specific customers when downloading.                       Only users who have been set up with a project code by Getty Images Sales need to use this field.                  &lt;/remarks&gt; | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **303** | See Other |  -  |
| **400** | MissingRequiredQueryParameters |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **403** | OverageLimitReached |  -  |
| **404** | VideoNotFound |  -  |

