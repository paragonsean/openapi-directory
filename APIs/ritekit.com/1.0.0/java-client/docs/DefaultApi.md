# DefaultApi

All URIs are relative to *https://api.ritekit.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**animateImage**](DefaultApi.md#animateImage) | **GET** /v1/images/animate | Animate Image |
| [**autoEmojify**](DefaultApi.md#autoEmojify) | **GET** /v1/emoji/auto-emojify | Auto-Emojify |
| [**autoHashtag**](DefaultApi.md#autoHashtag) | **GET** /v1/stats/auto-hashtag | Auto-Hashtag |
| [**companyLogo**](DefaultApi.md#companyLogo) | **GET** /v1/images/logo | Company Logo |
| [**emojiSuggestions**](DefaultApi.md#emojiSuggestions) | **GET** /v1/emoji/suggestions | Emoji Suggestions |
| [**hashtagHistory**](DefaultApi.md#hashtagHistory) | **GET** /v1/stats/history/{hashtag} | Hashtag History |
| [**hashtagStats**](DefaultApi.md#hashtagStats) | **GET** /v1/stats/multiple-hashtags | Hashtag Stats |
| [**hashtagSuggestions**](DefaultApi.md#hashtagSuggestions) | **GET** /v1/stats/hashtag-suggestions | Hashtag Suggestions |
| [**hashtagsCleaner**](DefaultApi.md#hashtagsCleaner) | **GET** /v2/instagram/hashtags-cleaner | Hashtags cleaner |
| [**listOfCTAs**](DefaultApi.md#listOfCTAs) | **GET** /v1/link/cta | List of CTAs |
| [**shortenLink**](DefaultApi.md#shortenLink) | **GET** /v1/link/short-link | Shorten Link |
| [**textToImage**](DefaultApi.md#textToImage) | **GET** /v1/images/quote | Text to Image |
| [**trendingHashtags**](DefaultApi.md#trendingHashtags) | **GET** /v1/search/trending | Trending Hashtags |


<a id="animateImage"></a>
# **animateImage**
> animateImage(url, type)

Animate Image

Returns URL of an animated GIF.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String url = "https://jpeg.org/images/jpeg-home.jpg"; // String | URL of the company
    String type = "glint"; // String | URL of the company
    try {
      apiInstance.animateImage(url, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#animateImage");
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
| **url** | **String**| URL of the company | |
| **type** | **String**| URL of the company | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="autoEmojify"></a>
# **autoEmojify**
> autoEmojify(text)

Auto-Emojify

Returns text of the post with emoji added

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String text = "Why robots may soon steal all manufacturing jobs – but it’s not all bad news"; // String | Text of the post
    try {
      apiInstance.autoEmojify(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#autoEmojify");
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
| **text** | **String**| Text of the post | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="autoHashtag"></a>
# **autoHashtag**
> autoHashtag(post, maxHashtags, hashtagPosition)

Auto-Hashtag

Returns auto-hashtagged text of the post.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String post = "Is artificial intelligence the future of customer service?"; // String | Text of the post
    Integer maxHashtags = 2; // Integer | Max number of hashtags.
    String hashtagPosition = "auto"; // String | Position of hashtags: end => at the end, auto => anywhere
    try {
      apiInstance.autoHashtag(post, maxHashtags, hashtagPosition);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#autoHashtag");
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
| **post** | **String**| Text of the post | |
| **maxHashtags** | **Integer**| Max number of hashtags. | [optional] [default to 2] |
| **hashtagPosition** | **String**| Position of hashtags: end &#x3D;&gt; at the end, auto &#x3D;&gt; anywhere | [optional] [default to auto] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="companyLogo"></a>
# **companyLogo**
> companyLogo(domain)

Company Logo

Returns a company logo based on website domain. If the logo is not in our database yet, it will be extracted from the site on the fly. White logo background is automatically removed to make the logo look better on color backgrounds.  Note: It is not possible to access our company logo API publicly without authentication. If you wish to do so, you have to create proxy on your own server that calls our API from the server side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "google.com"; // String | URL of the company
    try {
      apiInstance.companyLogo(domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyLogo");
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
| **domain** | **String**| URL of the company | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="emojiSuggestions"></a>
# **emojiSuggestions**
> emojiSuggestions(text)

Emoji Suggestions

Returns list of emoji suggestions for a given text of the post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String text = "Why robots may soon steal all manufacturing jobs – but it’s not all bad news"; // String | Text of the post
    try {
      apiInstance.emojiSuggestions(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#emojiSuggestions");
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
| **text** | **String**| Text of the post | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hashtagHistory"></a>
# **hashtagHistory**
> hashtagHistory(hashtag)

Hashtag History

Returns historical stats for a given hashtag from the last 30 days

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hashtag = "job"; // String | Hashtag without # mark
    try {
      apiInstance.hashtagHistory(hashtag);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hashtagHistory");
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
| **hashtag** | **String**| Hashtag without # mark | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hashtagStats"></a>
# **hashtagStats**
> hashtagStats(tags)

Hashtag Stats

Returns real-time stats for up to 100 hashtags (updated hourly).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<Object> tags = Arrays.asList(null); // List<Object> | Hashtag(s) without # mark
    try {
      apiInstance.hashtagStats(tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hashtagStats");
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
| **tags** | [**List&lt;Object&gt;**](Object.md)| Hashtag(s) without # mark | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hashtagSuggestions"></a>
# **hashtagSuggestions**
> hashtagSuggestions(text)

Hashtag Suggestions

Returns list of hashtag suggestions for a single-word topic or a shorter text up to 1000 characters. Takes into account both semantic relevancy and real-time hashtag popularity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String text = "seo"; // String | Topic
    try {
      apiInstance.hashtagSuggestions(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hashtagSuggestions");
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
| **text** | **String**| Topic | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hashtagsCleaner"></a>
# **hashtagsCleaner**
> hashtagsCleaner(post)

Hashtags cleaner

Remove banned hashtags before posting to Instagram

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String post = "#instaphotography #instabeauty #instagirls #instanature #instagirl #photography #beauty #girls #nature #girl #sky #water #lady #ladies #woman #women #photograph #photographs #beauties #sunlight #sitting #waters #skies #sit #photographies"; // String | post
    try {
      apiInstance.hashtagsCleaner(post);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hashtagsCleaner");
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
| **post** | **String**| post | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listOfCTAs"></a>
# **listOfCTAs**
> listOfCTAs()

List of CTAs

Returns list of available CTA for current user. Requires each user to authenticate with RiteKit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.listOfCTAs();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listOfCTAs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="shortenLink"></a>
# **shortenLink**
> shortenLink(url, cta)

Shorten Link

Returns a shorten link with a given CTA.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String url = "https://ritekit.com"; // String | URL
    Integer cta = 6530; // Integer | cta id
    try {
      apiInstance.shortenLink(url, cta);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#shortenLink");
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
| **url** | **String**| URL | |
| **cta** | **Integer**| cta id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="textToImage"></a>
# **textToImage**
> textToImage(quote, author, fontSize, quoteFont, quoteFontColor, authorFont, authorFontColor, enableHighlight, highlightColor, bgType, backgroundColor, gradientType, gradientColor1, gradientColor2, brandLogo, animation, showQuoteMark)

Text to Image

Returns URL of an image created from text according to given style parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String quote = "If you love life, don't waste time, for time is what life is made up of"; // String | Text of the quote
    String author = "Bruce Lee"; // String | Name of the author/source
    Integer fontSize = 60; // Integer | Font size for the quote (author font size is calculated automatically)
    String quoteFont = "Lora"; // String | Font-family used for quote text
    String quoteFontColor = "#4f4f4f"; // String | Font color of the quote text
    String authorFont = "Lato Black"; // String | Font-family used for author name
    String authorFontColor = "#e5e5e5"; // String | Font color of the author
    Integer enableHighlight = 1; // Integer | Enable highlight on quote text
    String highlightColor = "#f0ea66"; // String | Color used for highlight
    String bgType = "gradient"; // String | Background type (gradient/solid)
    String backgroundColor = "#000000"; // String | Background color for solid background type
    String gradientType = "linear"; // String | Type of gradient background (linear/radial)
    String gradientColor1 = "#1ee691"; // String | First color for gradient background type
    String gradientColor2 = "#1ddad6"; // String | Second color for gradient background type
    String brandLogo = "https://cdn.ritekit.com/assets/img/common/made-with-ritekit-white.png"; // String | URL of the brand logo
    String animation = "glint"; // String | Animation type: none, rays, glint, circle
    Integer showQuoteMark = 56; // Integer | showing/hiding quote mark
    try {
      apiInstance.textToImage(quote, author, fontSize, quoteFont, quoteFontColor, authorFont, authorFontColor, enableHighlight, highlightColor, bgType, backgroundColor, gradientType, gradientColor1, gradientColor2, brandLogo, animation, showQuoteMark);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#textToImage");
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
| **quote** | **String**| Text of the quote | |
| **author** | **String**| Name of the author/source | |
| **fontSize** | **Integer**| Font size for the quote (author font size is calculated automatically) | |
| **quoteFont** | **String**| Font-family used for quote text | |
| **quoteFontColor** | **String**| Font color of the quote text | |
| **authorFont** | **String**| Font-family used for author name | |
| **authorFontColor** | **String**| Font color of the author | |
| **enableHighlight** | **Integer**| Enable highlight on quote text | |
| **highlightColor** | **String**| Color used for highlight | |
| **bgType** | **String**| Background type (gradient/solid) | |
| **backgroundColor** | **String**| Background color for solid background type | |
| **gradientType** | **String**| Type of gradient background (linear/radial) | |
| **gradientColor1** | **String**| First color for gradient background type | |
| **gradientColor2** | **String**| Second color for gradient background type | |
| **brandLogo** | **String**| URL of the brand logo | |
| **animation** | **String**| Animation type: none, rays, glint, circle | |
| **showQuoteMark** | **Integer**| showing/hiding quote mark | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="trendingHashtags"></a>
# **trendingHashtags**
> trendingHashtags(green, latin)

Trending Hashtags

Returns list of hashtags currently trending on Twitter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritekit.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean green = false; // Boolean | Restrict results only to green hashtags. Hides overused (red) hashtags.
    Boolean latin = false; // Boolean | Restrict results only to hashtags with latin characters
    try {
      apiInstance.trendingHashtags(green, latin);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#trendingHashtags");
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
| **green** | **Boolean**| Restrict results only to green hashtags. Hides overused (red) hashtags. | [optional] [default to false] |
| **latin** | **Boolean**| Restrict results only to hashtags with latin characters | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

