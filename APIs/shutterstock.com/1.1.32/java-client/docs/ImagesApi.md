# ImagesApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addImageCollectionItems**](ImagesApi.md#addImageCollectionItems) | **POST** /v2/images/collections/{id}/items | Add images to collections |
| [**bulkSearchImages**](ImagesApi.md#bulkSearchImages) | **POST** /v2/bulk_search/images | Run multiple image searches |
| [**createImageCollection**](ImagesApi.md#createImageCollection) | **POST** /v2/images/collections | Create image collections |
| [**deleteImageCollection**](ImagesApi.md#deleteImageCollection) | **DELETE** /v2/images/collections/{id} | Delete image collections |
| [**deleteImageCollectionItems**](ImagesApi.md#deleteImageCollectionItems) | **DELETE** /v2/images/collections/{id}/items | Remove images from collections |
| [**downloadImage**](ImagesApi.md#downloadImage) | **POST** /v2/images/licenses/{id}/downloads | Download images |
| [**getFeaturedImageCollection**](ImagesApi.md#getFeaturedImageCollection) | **GET** /v2/images/collections/featured/{id} | Get the details of featured image collections |
| [**getFeaturedImageCollectionItems**](ImagesApi.md#getFeaturedImageCollectionItems) | **GET** /v2/images/collections/featured/{id}/items | Get the contents of featured image collections |
| [**getFeaturedImageCollectionList**](ImagesApi.md#getFeaturedImageCollectionList) | **GET** /v2/images/collections/featured | List featured image collections |
| [**getImage**](ImagesApi.md#getImage) | **GET** /v2/images/{id} | Get details about images |
| [**getImageCollection**](ImagesApi.md#getImageCollection) | **GET** /v2/images/collections/{id} | Get the details of image collections |
| [**getImageCollectionItems**](ImagesApi.md#getImageCollectionItems) | **GET** /v2/images/collections/{id}/items | Get the contents of image collections |
| [**getImageCollectionList**](ImagesApi.md#getImageCollectionList) | **GET** /v2/images/collections | List image collections |
| [**getImageKeywordSuggestions**](ImagesApi.md#getImageKeywordSuggestions) | **POST** /v2/images/search/suggestions | Get keywords from text |
| [**getImageLicenseList**](ImagesApi.md#getImageLicenseList) | **GET** /v2/images/licenses | List image licenses |
| [**getImageList**](ImagesApi.md#getImageList) | **GET** /v2/images | List images |
| [**getImageRecommendations**](ImagesApi.md#getImageRecommendations) | **GET** /v2/images/recommendations | List recommended images |
| [**getImageSuggestions**](ImagesApi.md#getImageSuggestions) | **GET** /v2/images/search/suggestions | Get suggestions for a search term |
| [**getUpdatedImages**](ImagesApi.md#getUpdatedImages) | **GET** /v2/images/updated | List updated images |
| [**licenseImages**](ImagesApi.md#licenseImages) | **POST** /v2/images/licenses | License images |
| [**listImageCategories**](ImagesApi.md#listImageCategories) | **GET** /v2/images/categories | List image categories |
| [**listSimilarImages**](ImagesApi.md#listSimilarImages) | **GET** /v2/images/{id}/similar | List similar images |
| [**renameImageCollection**](ImagesApi.md#renameImageCollection) | **POST** /v2/images/collections/{id} | Rename image collections |
| [**searchImages**](ImagesApi.md#searchImages) | **GET** /v2/images/search | Search for images |


<a id="addImageCollectionItems"></a>
# **addImageCollectionItems**
> addImageCollectionItems(id, collectionItemRequest)

Add images to collections

This endpoint adds one or more images to a collection by image IDs.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "126351027"; // String | Collection ID
    CollectionItemRequest collectionItemRequest = new CollectionItemRequest(); // CollectionItemRequest | Array of image IDs to add to the collection
    try {
      apiInstance.addImageCollectionItems(id, collectionItemRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#addImageCollectionItems");
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
| **id** | **String**| Collection ID | |
| **collectionItemRequest** | [**CollectionItemRequest**](CollectionItemRequest.md)| Array of image IDs to add to the collection | |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully added collection items |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="bulkSearchImages"></a>
# **bulkSearchImages**
> BulkImageSearchResults bulkSearchImages(searchImage, addedDate, addedDateStart, aspectRatioMin, aspectRatioMax, aspectRatio, addedDateEnd, category, color, contributor, contributorCountry, fields, height, heightFrom, heightTo, imageType, keywordSafeSearch, language, license, model, orientation, page, perPage, peopleModelReleased, peopleAge, peopleEthnicity, peopleGender, peopleNumber, region, safe, sort, spellcheckQuery, view, width, widthFrom, widthTo)

Run multiple image searches

This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You can provide global search parameters in the query parameters and override them for each search in the body parameter. The query and body parameters are the same as in the &#x60;GET /v2/images/search&#x60; endpoint.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<SearchImage> searchImage = Arrays.asList(); // List<SearchImage> | List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters
    LocalDate addedDate = LocalDate.parse("2021-03-29"); // LocalDate | Show images added on the specified date
    LocalDate addedDateStart = LocalDate.parse("2021-03-29"); // LocalDate | Show images added on or after the specified date
    BigDecimal aspectRatioMin = new BigDecimal("1.7778"); // BigDecimal | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    BigDecimal aspectRatioMax = new BigDecimal("1.7778"); // BigDecimal | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    BigDecimal aspectRatio = new BigDecimal("1.7778"); // BigDecimal | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    LocalDate addedDateEnd = LocalDate.parse("2021-03-29"); // LocalDate | Show images added before the specified date
    String category = "category_example"; // String | Show images with the specified Shutterstock-defined category; specify a category name or ID
    String color = "4F21EA"; // String | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors
    List<String> contributor = Arrays.asList(); // List<String> | Show images with the specified contributor names or IDs, allows multiple
    BulkSearchImagesContributorCountryParameter contributorCountry = new BulkSearchImagesContributorCountryParameter(); // BulkSearchImagesContributorCountryParameter | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search
    String fields = "fields_example"; // String | Fields to display in the response; see the documentation for the fields parameter in the overview section
    Integer height = 56; // Integer | (Deprecated; use height_from and height_to instead) Show images with the specified height
    Integer heightFrom = 1080; // Integer | Show images with the specified height or larger, in pixels
    Integer heightTo = 1080; // Integer | Show images with the specified height or smaller, in pixels
    List<String> imageType = Arrays.asList(); // List<String> | Show images of the specified type
    Boolean keywordSafeSearch = true; // Boolean | Hide results with potentially unsafe keywords
    Language language = Language.fromValue("ar"); // Language | Set query and result language (uses Accept-Language header if not set)
    List<String> license = Arrays.asList("commercial"); // List<String> | Show only images with the specified license
    List<String> model = Arrays.asList(); // List<String> | Show image results with the specified model IDs
    String orientation = "horizontal"; // String | Show image results with horizontal or vertical orientation
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    Boolean peopleModelReleased = true; // Boolean | Show images of people with a signed model release
    String peopleAge = "infants"; // String | Show images that feature people of the specified age category
    List<String> peopleEthnicity = Arrays.asList(); // List<String> | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities
    String peopleGender = "male"; // String | Show images with people of the specified gender
    Integer peopleNumber = 2; // Integer | Show images with the specified number of people
    BulkSearchImagesRegionParameter region = new BulkSearchImagesRegionParameter(); // BulkSearchImagesRegionParameter | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country
    Boolean safe = true; // Boolean | Enable or disable safe search
    String sort = "newest"; // String | Sort by
    Boolean spellcheckQuery = true; // Boolean | Spellcheck the search query and return results on suggested spellings
    String view = "minimal"; // String | Amount of detail to render in the response
    Integer width = 56; // Integer | (Deprecated; use width_from and width_to instead) Show images with the specified width
    Integer widthFrom = 1920; // Integer | Show images with the specified width or larger, in pixels
    Integer widthTo = 1920; // Integer | Show images with the specified width or smaller, in pixels
    try {
      BulkImageSearchResults result = apiInstance.bulkSearchImages(searchImage, addedDate, addedDateStart, aspectRatioMin, aspectRatioMax, aspectRatio, addedDateEnd, category, color, contributor, contributorCountry, fields, height, heightFrom, heightTo, imageType, keywordSafeSearch, language, license, model, orientation, page, perPage, peopleModelReleased, peopleAge, peopleEthnicity, peopleGender, peopleNumber, region, safe, sort, spellcheckQuery, view, width, widthFrom, widthTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#bulkSearchImages");
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
| **searchImage** | [**List&lt;SearchImage&gt;**](SearchImage.md)| List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters | |
| **addedDate** | **LocalDate**| Show images added on the specified date | [optional] |
| **addedDateStart** | **LocalDate**| Show images added on or after the specified date | [optional] |
| **aspectRatioMin** | **BigDecimal**| Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] |
| **aspectRatioMax** | **BigDecimal**| Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] |
| **aspectRatio** | **BigDecimal**| Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] |
| **addedDateEnd** | **LocalDate**| Show images added before the specified date | [optional] |
| **category** | **String**| Show images with the specified Shutterstock-defined category; specify a category name or ID | [optional] |
| **color** | **String**| Specify either a hexadecimal color in the format &#39;4F21EA&#39; or &#39;grayscale&#39;; the API returns images that use similar colors | [optional] |
| **contributor** | [**List&lt;String&gt;**](String.md)| Show images with the specified contributor names or IDs, allows multiple | [optional] |
| **contributorCountry** | [**BulkSearchImagesContributorCountryParameter**](.md)| Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search | [optional] |
| **fields** | **String**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] |
| **height** | **Integer**| (Deprecated; use height_from and height_to instead) Show images with the specified height | [optional] |
| **heightFrom** | **Integer**| Show images with the specified height or larger, in pixels | [optional] |
| **heightTo** | **Integer**| Show images with the specified height or smaller, in pixels | [optional] |
| **imageType** | [**List&lt;String&gt;**](String.md)| Show images of the specified type | [optional] [enum: photo, illustration, vector] |
| **keywordSafeSearch** | **Boolean**| Hide results with potentially unsafe keywords | [optional] [default to true] |
| **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **license** | [**List&lt;String&gt;**](String.md)| Show only images with the specified license | [optional] [enum: commercial, editorial, enhanced] |
| **model** | [**List&lt;String&gt;**](String.md)| Show image results with the specified model IDs | [optional] |
| **orientation** | **String**| Show image results with horizontal or vertical orientation | [optional] [enum: horizontal, vertical] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **peopleModelReleased** | **Boolean**| Show images of people with a signed model release | [optional] |
| **peopleAge** | **String**| Show images that feature people of the specified age category | [optional] [enum: infants, children, teenagers, 20s, 30s, 40s, 50s, 60s, older] |
| **peopleEthnicity** | [**List&lt;String&gt;**](String.md)| Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities | [optional] [enum: african, african_american, black, brazilian, chinese, caucasian, east_asian, hispanic, japanese, middle_eastern, native_american, pacific_islander, south_asian, southeast_asian, other, NOT african, NOT african_american, NOT black, NOT brazilian, NOT chinese, NOT caucasian, NOT east_asian, NOT hispanic, NOT japanese, NOT middle_eastern, NOT native_american, NOT pacific_islander, NOT south_asian, NOT southeast_asian, NOT other] |
| **peopleGender** | **String**| Show images with people of the specified gender | [optional] [enum: male, female, both] |
| **peopleNumber** | **Integer**| Show images with the specified number of people | [optional] |
| **region** | [**BulkSearchImagesRegionParameter**](.md)| Raise or lower search result rankings based on the result&#39;s relevance to a specified region; you can provide a country code or an IP address from which the API infers a country | [optional] |
| **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true] |
| **sort** | **String**| Sort by | [optional] [default to popular] [enum: newest, popular, relevance, random] |
| **spellcheckQuery** | **Boolean**| Spellcheck the search query and return results on suggested spellings | [optional] [default to true] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **width** | **Integer**| (Deprecated; use width_from and width_to instead) Show images with the specified width | [optional] |
| **widthFrom** | **Integer**| Show images with the specified width or larger, in pixels | [optional] |
| **widthTo** | **Integer**| Show images with the specified width or smaller, in pixels | [optional] |

### Return type

[**BulkImageSearchResults**](BulkImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="createImageCollection"></a>
# **createImageCollection**
> CollectionCreateResponse createImageCollection(collectionCreateRequest)

Create image collections

This endpoint creates one or more image collections (lightboxes). To add images to the collections, use &#x60;POST /v2/images/collections/{id}/items&#x60;.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    CollectionCreateRequest collectionCreateRequest = new CollectionCreateRequest(); // CollectionCreateRequest | The names of the new collections
    try {
      CollectionCreateResponse result = apiInstance.createImageCollection(collectionCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#createImageCollection");
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
| **collectionCreateRequest** | [**CollectionCreateRequest**](CollectionCreateRequest.md)| The names of the new collections | |

### Return type

[**CollectionCreateResponse**](CollectionCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully created image collection |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="deleteImageCollection"></a>
# **deleteImageCollection**
> deleteImageCollection(id)

Delete image collections

This endpoint deletes an image collection.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "136351027"; // String | Collection ID
    try {
      apiInstance.deleteImageCollection(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#deleteImageCollection");
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
| **id** | **String**| Collection ID | |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted collection |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="deleteImageCollectionItems"></a>
# **deleteImageCollectionItems**
> deleteImageCollectionItems(id, itemId)

Remove images from collections

This endpoint removes one or more images from a collection.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "126351027"; // String | Collection ID
    List<String> itemId = Arrays.asList(); // List<String> | One or more image IDs to remove from the collection
    try {
      apiInstance.deleteImageCollectionItems(id, itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#deleteImageCollectionItems");
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
| **id** | **String**| Collection ID | |
| **itemId** | [**List&lt;String&gt;**](String.md)| One or more image IDs to remove from the collection | [optional] |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully removed collection items |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="downloadImage"></a>
# **downloadImage**
> Url downloadImage(id, redownloadImage)

Download images

This endpoint redownloads images that you have already received a license for. The download links in the response are valid for 8 hours.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "e123"; // String | License ID
    RedownloadImage redownloadImage = new RedownloadImage(); // RedownloadImage | Information about the images to redownload
    try {
      Url result = apiInstance.downloadImage(id, redownloadImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#downloadImage");
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
| **id** | **String**| License ID | |
| **redownloadImage** | [**RedownloadImage**](RedownloadImage.md)| Information about the images to redownload | |

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getFeaturedImageCollection"></a>
# **getFeaturedImageCollection**
> FeaturedCollection getFeaturedImageCollection(id, embed, assetHint)

Get the details of featured image collections

This endpoint gets more detailed information about a featured collection, including its cover image and timestamps for its creation and most recent update. To get the images, use &#x60;GET /v2/images/collections/featured/{id}/items&#x60;.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "136351027"; // String | Collection ID
    String embed = "share_url"; // String | Which sharing information to include in the response, such as a URL to the collection
    String assetHint = "1x"; // String | Cover image size
    try {
      FeaturedCollection result = apiInstance.getFeaturedImageCollection(id, embed, assetHint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getFeaturedImageCollection");
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
| **id** | **String**| Collection ID | |
| **embed** | **String**| Which sharing information to include in the response, such as a URL to the collection | [optional] [enum: share_url] |
| **assetHint** | **String**| Cover image size | [optional] [default to 1x] [enum: 1x, 2x] |

### Return type

[**FeaturedCollection**](FeaturedCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Featured collection not found |  -  |

<a id="getFeaturedImageCollectionItems"></a>
# **getFeaturedImageCollectionItems**
> CollectionItemDataList getFeaturedImageCollectionItems(id, page, perPage)

Get the contents of featured image collections

This endpoint lists the IDs of images in a featured collection and the date that each was added.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "136351027"; // String | Collection ID
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    try {
      CollectionItemDataList result = apiInstance.getFeaturedImageCollectionItems(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getFeaturedImageCollectionItems");
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
| **id** | **String**| Collection ID | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Featured collection not found |  -  |

<a id="getFeaturedImageCollectionList"></a>
# **getFeaturedImageCollectionList**
> FeaturedCollectionDataList getFeaturedImageCollectionList(embed, type, assetHint)

List featured image collections

This endpoint lists featured collections of specific types and a name and cover image for each collection.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String embed = "share_url"; // String | Which sharing information to include in the response, such as a URL to the collection
    List<String> type = Arrays.asList(); // List<String> | The types of collections to return
    String assetHint = "1x"; // String | Cover image size
    try {
      FeaturedCollectionDataList result = apiInstance.getFeaturedImageCollectionList(embed, type, assetHint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getFeaturedImageCollectionList");
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
| **embed** | **String**| Which sharing information to include in the response, such as a URL to the collection | [optional] [enum: share_url] |
| **type** | [**List&lt;String&gt;**](String.md)| The types of collections to return | [optional] [enum: photo, editorial, vector] |
| **assetHint** | **String**| Cover image size | [optional] [default to 1x] [enum: 1x, 2x] |

### Return type

[**FeaturedCollectionDataList**](FeaturedCollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getImage"></a>
# **getImage**
> Image getImage(id, language, view, searchId)

Get details about images

This endpoint shows information about an image, including a URL to a preview image and the sizes that it is available in.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "465011609"; // String | Image ID
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    String view = "minimal"; // String | Amount of detail to render in the response
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      Image result = apiInstance.getImage(id, language, view, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImage");
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
| **id** | **String**| Image ID | |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to full] [enum: minimal, full] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**Image**](Image.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getImageCollection"></a>
# **getImageCollection**
> Collection getImageCollection(id, embed, shareCode)

Get the details of image collections

This endpoint gets more detailed information about a collection, including its cover image and timestamps for its creation and most recent update. To get the images in collections, use &#x60;GET /v2/images/collections/{id}/items&#x60;.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "126351027"; // String | Collection ID
    List<String> embed = Arrays.asList(); // List<String> | Which sharing information to include in the response, such as a URL to the collection
    String shareCode = "shareCode_example"; // String | Code to retrieve a shared collection
    try {
      Collection result = apiInstance.getImageCollection(id, embed, shareCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageCollection");
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
| **id** | **String**| Collection ID | |
| **embed** | [**List&lt;String&gt;**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] [enum: share_code, share_url] |
| **shareCode** | **String**| Code to retrieve a shared collection | [optional] |

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="getImageCollectionItems"></a>
# **getImageCollectionItems**
> CollectionItemDataList getImageCollectionItems(id, page, perPage, shareCode, sort)

Get the contents of image collections

This endpoint lists the IDs of images in a collection and the date that each was added.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "126351027"; // String | Collection ID
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    String shareCode = "shareCode_example"; // String | Code to retrieve the contents of a shared collection
    String sort = "newest"; // String | Sort order
    try {
      CollectionItemDataList result = apiInstance.getImageCollectionItems(id, page, perPage, shareCode, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageCollectionItems");
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
| **id** | **String**| Collection ID | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |
| **shareCode** | **String**| Code to retrieve the contents of a shared collection | [optional] |
| **sort** | **String**| Sort order | [optional] [default to oldest] [enum: newest, oldest] |

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="getImageCollectionList"></a>
# **getImageCollectionList**
> CollectionDataList getImageCollectionList(embed, page, perPage)

List image collections

This endpoint lists your collections of images and their basic attributes.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<String> embed = Arrays.asList(); // List<String> | Which sharing information to include in the response, such as a URL to the collection
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    try {
      CollectionDataList result = apiInstance.getImageCollectionList(embed, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageCollectionList");
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
| **embed** | [**List&lt;String&gt;**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] [enum: share_code, share_url] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getImageKeywordSuggestions"></a>
# **getImageKeywordSuggestions**
> SearchEntitiesResponse getImageKeywordSuggestions(searchEntitiesRequest)

Get keywords from text

This endpoint returns up to 10 important keywords from a block of plain text.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    SearchEntitiesRequest searchEntitiesRequest = new SearchEntitiesRequest(); // SearchEntitiesRequest | Plain text to extract keywords from
    try {
      SearchEntitiesResponse result = apiInstance.getImageKeywordSuggestions(searchEntitiesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageKeywordSuggestions");
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
| **searchEntitiesRequest** | [**SearchEntitiesRequest**](SearchEntitiesRequest.md)| Plain text to extract keywords from | |

### Return type

[**SearchEntitiesResponse**](SearchEntitiesResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getImageLicenseList"></a>
# **getImageLicenseList**
> DownloadHistoryDataList getImageLicenseList(imageId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory)

List image licenses

This endpoint lists existing licenses.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "12345678"; // String | Show licenses for the specified image ID
    String license = "standard"; // String | Show images that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort order
    String username = "aUniqueUsername"; // String | Filter licenses by username of licensee
    OffsetDateTime startDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created on or after the specified date
    OffsetDateTime endDate = OffsetDateTime.parse("2021-03-29T13:25:13.521Z"); // OffsetDateTime | Show licenses created before the specified date
    String downloadAvailability = "all"; // String | Filter licenses by download availability
    Boolean teamHistory = false; // Boolean | Set to true to see license history for all members of your team.
    try {
      DownloadHistoryDataList result = apiInstance.getImageLicenseList(imageId, license, page, perPage, sort, username, startDate, endDate, downloadAvailability, teamHistory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageLicenseList");
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
| **imageId** | **String**| Show licenses for the specified image ID | [optional] |
| **license** | **String**| Show images that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **sort** | **String**| Sort order | [optional] [default to newest] [enum: newest, oldest] |
| **username** | **String**| Filter licenses by username of licensee | [optional] |
| **startDate** | **OffsetDateTime**| Show licenses created on or after the specified date | [optional] |
| **endDate** | **OffsetDateTime**| Show licenses created before the specified date | [optional] |
| **downloadAvailability** | **String**| Filter licenses by download availability | [optional] [default to all] [enum: all, downloadable, non_downloadable] |
| **teamHistory** | **Boolean**| Set to true to see license history for all members of your team. | [optional] [default to false] |

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getImageList"></a>
# **getImageList**
> ImageDataList getImageList(id, view, searchId)

List images

This endpoint lists information about one or more images, including the available sizes.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | One or more image IDs
    String view = "minimal"; // String | Amount of detail to render in the response
    String searchId = "00000000-0000-0000-0000-000000000000"; // String | The ID of the search that is related to this request
    try {
      ImageDataList result = apiInstance.getImageList(id, view, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageList");
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
| **id** | [**List&lt;String&gt;**](String.md)| One or more image IDs | |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **searchId** | **String**| The ID of the search that is related to this request | [optional] |

### Return type

[**ImageDataList**](ImageDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getImageRecommendations"></a>
# **getImageRecommendations**
> RecommendationDataList getImageRecommendations(id, maxItems, safe)

List recommended images

This endpoint returns images that customers put in the same collection as the specified image IDs.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Image IDs
    Integer maxItems = 20; // Integer | Maximum number of results returned in the response
    Boolean safe = true; // Boolean | Restrict results to safe images
    try {
      RecommendationDataList result = apiInstance.getImageRecommendations(id, maxItems, safe);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageRecommendations");
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
| **id** | [**List&lt;String&gt;**](String.md)| Image IDs | |
| **maxItems** | **Integer**| Maximum number of results returned in the response | [optional] [default to 20] |
| **safe** | **Boolean**| Restrict results to safe images | [optional] [default to true] |

### Return type

[**RecommendationDataList**](RecommendationDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getImageSuggestions"></a>
# **getImageSuggestions**
> Suggestions getImageSuggestions(query, limit)

Get suggestions for a search term

This endpoint provides autocomplete suggestions for partial search terms.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String query = "cats"; // String | Search term for which you want keyword suggestions
    Integer limit = 10; // Integer | Limit the number of suggestions
    try {
      Suggestions result = apiInstance.getImageSuggestions(query, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageSuggestions");
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
| **query** | **String**| Search term for which you want keyword suggestions | |
| **limit** | **Integer**| Limit the number of suggestions | [optional] [default to 10] |

### Return type

[**Suggestions**](Suggestions.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getUpdatedImages"></a>
# **getUpdatedImages**
> UpdatedMediaDataList getUpdatedImages(type, startDate, endDate, interval, page, perPage, sort)

List updated images

This endpoint lists images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the &#x60;interval&#x60; parameter to show images that were updated recently, but you can also use the &#x60;start_date&#x60; and &#x60;end_date&#x60; parameters to specify a range of no more than three days. Do not use the &#x60;interval&#x60; parameter with either &#x60;start_date&#x60; or &#x60;end_date&#x60;.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<String> type = Arrays.asList(); // List<String> | Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways
    LocalDate startDate = LocalDate.parse("2021-03-29"); // LocalDate | Show images updated on or after the specified date
    LocalDate endDate = LocalDate.parse("2021-03-29"); // LocalDate | Show images updated before the specified date
    String interval = "1 HOUR"; // String | Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request
    Integer page = 1; // Integer | Page number
    Integer perPage = 100; // Integer | Number of results per page
    String sort = "newest"; // String | Sort order
    try {
      UpdatedMediaDataList result = apiInstance.getUpdatedImages(type, startDate, endDate, interval, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getUpdatedImages");
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
| **type** | [**List&lt;String&gt;**](String.md)| Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways | [optional] [enum: addition, deletion, edit] |
| **startDate** | **LocalDate**| Show images updated on or after the specified date | [optional] |
| **endDate** | **LocalDate**| Show images updated before the specified date | [optional] |
| **interval** | **String**| Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request | [optional] [default to 1 HOUR] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 100] |
| **sort** | **String**| Sort order | [optional] [default to newest] [enum: newest, oldest] |

### Return type

[**UpdatedMediaDataList**](UpdatedMediaDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="licenseImages"></a>
# **licenseImages**
> LicenseImageResultDataList licenseImages(licenseImageRequest, subscriptionId, format, size, searchId)

License images

This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and other details like the format, size, and subscription ID either in the query parameter or with each image ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    LicenseImageRequest licenseImageRequest = new LicenseImageRequest(); // LicenseImageRequest | List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID to use to license the image
    String format = "eps"; // String | (Deprecated) Image format
    String size = "small"; // String | Image size
    String searchId = "searchId_example"; // String | Search ID that was provided in the results of an image search
    try {
      LicenseImageResultDataList result = apiInstance.licenseImages(licenseImageRequest, subscriptionId, format, size, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#licenseImages");
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
| **licenseImageRequest** | [**LicenseImageRequest**](LicenseImageRequest.md)| List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters | |
| **subscriptionId** | **String**| Subscription ID to use to license the image | [optional] |
| **format** | **String**| (Deprecated) Image format | [optional] [enum: eps, jpg] |
| **size** | **String**| Image size | [optional] [default to huge] [enum: small, medium, huge, vector, custom] |
| **searchId** | **String**| Search ID that was provided in the results of an image search | [optional] |

### Return type

[**LicenseImageResultDataList**](LicenseImageResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="listImageCategories"></a>
# **listImageCategories**
> CategoryDataList listImageCategories(language)

List image categories

This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    try {
      CategoryDataList result = apiInstance.listImageCategories(language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#listImageCategories");
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
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |

### Return type

[**CategoryDataList**](CategoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="listSimilarImages"></a>
# **listSimilarImages**
> ImageSearchResults listSimilarImages(id, language, page, perPage, view)

List similar images

This endpoint returns images that are visually similar to an image that you specify.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "465011609"; // String | Image ID
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String view = "minimal"; // String | Amount of detail to render in the response
    try {
      ImageSearchResults result = apiInstance.listSimilarImages(id, language, page, perPage, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#listSimilarImages");
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
| **id** | **String**| Image ID | |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="renameImageCollection"></a>
# **renameImageCollection**
> renameImageCollection(id, collectionUpdateRequest)

Rename image collections

This endpoint sets a new name for an image collection.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "126351027"; // String | Collection ID
    CollectionUpdateRequest collectionUpdateRequest = new CollectionUpdateRequest(); // CollectionUpdateRequest | The new name for the collection
    try {
      apiInstance.renameImageCollection(id, collectionUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#renameImageCollection");
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
| **id** | **String**| Collection ID | |
| **collectionUpdateRequest** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| The new name for the collection | |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully updated collection |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Collection not found |  -  |

<a id="searchImages"></a>
# **searchImages**
> ImageSearchResults searchImages(addedDate, addedDateStart, aspectRatioMin, aspectRatioMax, aspectRatio, aiSearch, aiLabelsLimit, aiIndustry, aiObjective, addedDateEnd, category, color, contributor, contributorCountry, fields, height, heightFrom, heightTo, imageType, keywordSafeSearch, language, license, model, orientation, page, perPage, peopleModelReleased, peopleAge, peopleEthnicity, peopleGender, peopleNumber, query, region, safe, sort, spellcheckQuery, view, width, widthFrom, widthTo)

Search for images

This endpoint searches for images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media, not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

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
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    LocalDate addedDate = LocalDate.parse("2021-03-29"); // LocalDate | Show images added on the specified date
    LocalDate addedDateStart = LocalDate.parse("2021-03-29"); // LocalDate | Show images added on or after the specified date
    BigDecimal aspectRatioMin = new BigDecimal("1.7778"); // BigDecimal | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    BigDecimal aspectRatioMax = new BigDecimal("1.7778"); // BigDecimal | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    BigDecimal aspectRatio = new BigDecimal("1.7778"); // BigDecimal | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
    Boolean aiSearch = true; // Boolean | Set to true and specify the `ai_objective` and `ai_industry` parameters to use AI-powered search; the API returns information about how well images meet the objective for the industry 
    Integer aiLabelsLimit = 20; // Integer | For AI-powered search, specify the maximum number of labels to return
    String aiIndustry = "automotive"; // String | For AI-powered search, specify the industry to target; requires that the `ai_search` parameter is set to true
    String aiObjective = "awareness"; // String | For AI-powered search, specify the goal of the media; requires that the `ai_search` parameter is set to true
    LocalDate addedDateEnd = LocalDate.parse("2021-03-29"); // LocalDate | Show images added before the specified date
    String category = "category_example"; // String | Show images with the specified Shutterstock-defined category; specify a category name or ID
    String color = "4F21EA"; // String | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors
    List<String> contributor = Arrays.asList(); // List<String> | Show images with the specified contributor names or IDs, allows multiple
    BulkSearchImagesContributorCountryParameter contributorCountry = new BulkSearchImagesContributorCountryParameter(); // BulkSearchImagesContributorCountryParameter | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search
    String fields = "fields_example"; // String | Fields to display in the response; see the documentation for the fields parameter in the overview section
    Integer height = 56; // Integer | (Deprecated; use height_from and height_to instead) Show images with the specified height
    Integer heightFrom = 1080; // Integer | Show images with the specified height or larger, in pixels
    Integer heightTo = 1080; // Integer | Show images with the specified height or smaller, in pixels
    List<String> imageType = Arrays.asList(); // List<String> | Show images of the specified type
    Boolean keywordSafeSearch = true; // Boolean | Hide results with potentially unsafe keywords
    Language language = Language.fromValue("ar"); // Language | Set query and result language (uses Accept-Language header if not set)
    List<String> license = Arrays.asList("commercial"); // List<String> | Show only images with the specified license
    List<String> model = Arrays.asList(); // List<String> | Show image results with the specified model IDs
    String orientation = "horizontal"; // String | Show image results with horizontal or vertical orientation
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    Boolean peopleModelReleased = true; // Boolean | Show images of people with a signed model release
    String peopleAge = "infants"; // String | Show images that feature people of the specified age category
    List<String> peopleEthnicity = Arrays.asList(); // List<String> | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities
    String peopleGender = "male"; // String | Show images with people of the specified gender
    Integer peopleNumber = 2; // Integer | Show images with the specified number of people
    String query = "dogs on the beach"; // String | One or more search terms separated by spaces; you can use NOT to filter out images that match a term
    BulkSearchImagesRegionParameter region = new BulkSearchImagesRegionParameter(); // BulkSearchImagesRegionParameter | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country
    Boolean safe = true; // Boolean | Enable or disable safe search
    String sort = "newest"; // String | Sort by
    Boolean spellcheckQuery = true; // Boolean | Spellcheck the search query and return results on suggested spellings
    String view = "minimal"; // String | Amount of detail to render in the response
    Integer width = 56; // Integer | (Deprecated; use width_from and width_to instead) Show images with the specified width
    Integer widthFrom = 1920; // Integer | Show images with the specified width or larger, in pixels
    Integer widthTo = 1920; // Integer | Show images with the specified width or smaller, in pixels
    try {
      ImageSearchResults result = apiInstance.searchImages(addedDate, addedDateStart, aspectRatioMin, aspectRatioMax, aspectRatio, aiSearch, aiLabelsLimit, aiIndustry, aiObjective, addedDateEnd, category, color, contributor, contributorCountry, fields, height, heightFrom, heightTo, imageType, keywordSafeSearch, language, license, model, orientation, page, perPage, peopleModelReleased, peopleAge, peopleEthnicity, peopleGender, peopleNumber, query, region, safe, sort, spellcheckQuery, view, width, widthFrom, widthTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#searchImages");
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
| **addedDate** | **LocalDate**| Show images added on the specified date | [optional] |
| **addedDateStart** | **LocalDate**| Show images added on or after the specified date | [optional] |
| **aspectRatioMin** | **BigDecimal**| Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] |
| **aspectRatioMax** | **BigDecimal**| Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] |
| **aspectRatio** | **BigDecimal**| Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] |
| **aiSearch** | **Boolean**| Set to true and specify the &#x60;ai_objective&#x60; and &#x60;ai_industry&#x60; parameters to use AI-powered search; the API returns information about how well images meet the objective for the industry  | [optional] |
| **aiLabelsLimit** | **Integer**| For AI-powered search, specify the maximum number of labels to return | [optional] [default to 20] |
| **aiIndustry** | **String**| For AI-powered search, specify the industry to target; requires that the &#x60;ai_search&#x60; parameter is set to true | [optional] [enum: automotive, cpg, finance, healthcare, retail, technology] |
| **aiObjective** | **String**| For AI-powered search, specify the goal of the media; requires that the &#x60;ai_search&#x60; parameter is set to true | [optional] [enum: awareness, traffic, conversions] |
| **addedDateEnd** | **LocalDate**| Show images added before the specified date | [optional] |
| **category** | **String**| Show images with the specified Shutterstock-defined category; specify a category name or ID | [optional] |
| **color** | **String**| Specify either a hexadecimal color in the format &#39;4F21EA&#39; or &#39;grayscale&#39;; the API returns images that use similar colors | [optional] |
| **contributor** | [**List&lt;String&gt;**](String.md)| Show images with the specified contributor names or IDs, allows multiple | [optional] |
| **contributorCountry** | [**BulkSearchImagesContributorCountryParameter**](.md)| Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search | [optional] |
| **fields** | **String**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] |
| **height** | **Integer**| (Deprecated; use height_from and height_to instead) Show images with the specified height | [optional] |
| **heightFrom** | **Integer**| Show images with the specified height or larger, in pixels | [optional] |
| **heightTo** | **Integer**| Show images with the specified height or smaller, in pixels | [optional] |
| **imageType** | [**List&lt;String&gt;**](String.md)| Show images of the specified type | [optional] [enum: photo, illustration, vector] |
| **keywordSafeSearch** | **Boolean**| Hide results with potentially unsafe keywords | [optional] [default to true] |
| **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **license** | [**List&lt;String&gt;**](String.md)| Show only images with the specified license | [optional] [enum: commercial, editorial, enhanced] |
| **model** | [**List&lt;String&gt;**](String.md)| Show image results with the specified model IDs | [optional] |
| **orientation** | **String**| Show image results with horizontal or vertical orientation | [optional] [enum: horizontal, vertical] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **peopleModelReleased** | **Boolean**| Show images of people with a signed model release | [optional] |
| **peopleAge** | **String**| Show images that feature people of the specified age category | [optional] [enum: infants, children, teenagers, 20s, 30s, 40s, 50s, 60s, older] |
| **peopleEthnicity** | [**List&lt;String&gt;**](String.md)| Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities | [optional] [enum: african, african_american, black, brazilian, chinese, caucasian, east_asian, hispanic, japanese, middle_eastern, native_american, pacific_islander, south_asian, southeast_asian, other, NOT african, NOT african_american, NOT black, NOT brazilian, NOT chinese, NOT caucasian, NOT east_asian, NOT hispanic, NOT japanese, NOT middle_eastern, NOT native_american, NOT pacific_islander, NOT south_asian, NOT southeast_asian, NOT other] |
| **peopleGender** | **String**| Show images with people of the specified gender | [optional] [enum: male, female, both] |
| **peopleNumber** | **Integer**| Show images with the specified number of people | [optional] |
| **query** | **String**| One or more search terms separated by spaces; you can use NOT to filter out images that match a term | [optional] |
| **region** | [**BulkSearchImagesRegionParameter**](.md)| Raise or lower search result rankings based on the result&#39;s relevance to a specified region; you can provide a country code or an IP address from which the API infers a country | [optional] |
| **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true] |
| **sort** | **String**| Sort by | [optional] [default to popular] [enum: newest, popular, relevance, random] |
| **spellcheckQuery** | **Boolean**| Spellcheck the search query and return results on suggested spellings | [optional] [default to true] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |
| **width** | **Integer**| (Deprecated; use width_from and width_to instead) Show images with the specified width | [optional] |
| **widthFrom** | **Integer**| Show images with the specified width or larger, in pixels | [optional] |
| **widthTo** | **Integer**| Show images with the specified width or smaller, in pixels | [optional] |

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

