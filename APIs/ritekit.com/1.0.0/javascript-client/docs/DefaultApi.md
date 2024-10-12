# RiteKitApi.DefaultApi

All URIs are relative to *https://api.ritekit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**animateImage**](DefaultApi.md#animateImage) | **GET** /v1/images/animate | Animate Image
[**autoEmojify**](DefaultApi.md#autoEmojify) | **GET** /v1/emoji/auto-emojify | Auto-Emojify
[**autoHashtag**](DefaultApi.md#autoHashtag) | **GET** /v1/stats/auto-hashtag | Auto-Hashtag
[**companyLogo**](DefaultApi.md#companyLogo) | **GET** /v1/images/logo | Company Logo
[**emojiSuggestions**](DefaultApi.md#emojiSuggestions) | **GET** /v1/emoji/suggestions | Emoji Suggestions
[**hashtagHistory**](DefaultApi.md#hashtagHistory) | **GET** /v1/stats/history/{hashtag} | Hashtag History
[**hashtagStats**](DefaultApi.md#hashtagStats) | **GET** /v1/stats/multiple-hashtags | Hashtag Stats
[**hashtagSuggestions**](DefaultApi.md#hashtagSuggestions) | **GET** /v1/stats/hashtag-suggestions | Hashtag Suggestions
[**hashtagsCleaner**](DefaultApi.md#hashtagsCleaner) | **GET** /v2/instagram/hashtags-cleaner | Hashtags cleaner
[**listOfCTAs**](DefaultApi.md#listOfCTAs) | **GET** /v1/link/cta | List of CTAs
[**shortenLink**](DefaultApi.md#shortenLink) | **GET** /v1/link/short-link | Shorten Link
[**textToImage**](DefaultApi.md#textToImage) | **GET** /v1/images/quote | Text to Image
[**trendingHashtags**](DefaultApi.md#trendingHashtags) | **GET** /v1/search/trending | Trending Hashtags



## animateImage

> animateImage(url, type)

Animate Image

Returns URL of an animated GIF.

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let url = "https://jpeg.org/images/jpeg-home.jpg"; // String | URL of the company
let type = "glint"; // String | URL of the company
apiInstance.animateImage(url, type, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **String**| URL of the company | 
 **type** | **String**| URL of the company | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/gif


## autoEmojify

> autoEmojify(text)

Auto-Emojify

Returns text of the post with emoji added

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let text = "Why robots may soon steal all manufacturing jobs – but it’s not all bad news"; // String | Text of the post
apiInstance.autoEmojify(text, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Text of the post | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## autoHashtag

> autoHashtag(post, opts)

Auto-Hashtag

Returns auto-hashtagged text of the post.

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let post = "Is artificial intelligence the future of customer service?"; // String | Text of the post
let opts = {
  'maxHashtags': 2, // Number | Max number of hashtags.
  'hashtagPosition': "'auto'" // String | Position of hashtags: end => at the end, auto => anywhere
};
apiInstance.autoHashtag(post, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post** | **String**| Text of the post | 
 **maxHashtags** | **Number**| Max number of hashtags. | [optional] [default to 2]
 **hashtagPosition** | **String**| Position of hashtags: end &#x3D;&gt; at the end, auto &#x3D;&gt; anywhere | [optional] [default to &#39;auto&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## companyLogo

> companyLogo(domain)

Company Logo

Returns a company logo based on website domain. If the logo is not in our database yet, it will be extracted from the site on the fly. White logo background is automatically removed to make the logo look better on color backgrounds.  Note: It is not possible to access our company logo API publicly without authentication. If you wish to do so, you have to create proxy on your own server that calls our API from the server side.

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let domain = "google.com"; // String | URL of the company
apiInstance.companyLogo(domain, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **String**| URL of the company | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png


## emojiSuggestions

> emojiSuggestions(text)

Emoji Suggestions

Returns list of emoji suggestions for a given text of the post

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let text = "Why robots may soon steal all manufacturing jobs – but it’s not all bad news"; // String | Text of the post
apiInstance.emojiSuggestions(text, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Text of the post | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## hashtagHistory

> hashtagHistory(hashtag)

Hashtag History

Returns historical stats for a given hashtag from the last 30 days

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let hashtag = "job"; // String | Hashtag without # mark
apiInstance.hashtagHistory(hashtag, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashtag** | **String**| Hashtag without # mark | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## hashtagStats

> hashtagStats(tags)

Hashtag Stats

Returns real-time stats for up to 100 hashtags (updated hourly).

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let tags = [null]; // [Object] | Hashtag(s) without # mark
apiInstance.hashtagStats(tags, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**[Object]**](Object.md)| Hashtag(s) without # mark | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## hashtagSuggestions

> hashtagSuggestions(text)

Hashtag Suggestions

Returns list of hashtag suggestions for a single-word topic or a shorter text up to 1000 characters. Takes into account both semantic relevancy and real-time hashtag popularity.

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let text = "seo"; // String | Topic
apiInstance.hashtagSuggestions(text, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Topic | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## hashtagsCleaner

> hashtagsCleaner(post)

Hashtags cleaner

Remove banned hashtags before posting to Instagram

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let post = "#instaphotography #instabeauty #instagirls #instanature #instagirl #photography #beauty #girls #nature #girl #sky #water #lady #ladies #woman #women #photograph #photographs #beauties #sunlight #sitting #waters #skies #sit #photographies"; // String | post
apiInstance.hashtagsCleaner(post, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post** | **String**| post | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listOfCTAs

> listOfCTAs()

List of CTAs

Returns list of available CTA for current user. Requires each user to authenticate with RiteKit

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
apiInstance.listOfCTAs((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## shortenLink

> shortenLink(url, cta)

Shorten Link

Returns a shorten link with a given CTA.

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let url = "https://ritekit.com"; // String | URL
let cta = 6530; // Number | cta id
apiInstance.shortenLink(url, cta, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **String**| URL | 
 **cta** | **Number**| cta id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## textToImage

> textToImage(quote, author, fontSize, quoteFont, quoteFontColor, authorFont, authorFontColor, enableHighlight, highlightColor, bgType, backgroundColor, gradientType, gradientColor1, gradientColor2, brandLogo, animation, opts)

Text to Image

Returns URL of an image created from text according to given style parameters

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let quote = "If you love life, don't waste time, for time is what life is made up of"; // String | Text of the quote
let author = "Bruce Lee"; // String | Name of the author/source
let fontSize = 60; // Number | Font size for the quote (author font size is calculated automatically)
let quoteFont = "Lora"; // String | Font-family used for quote text
let quoteFontColor = "#4f4f4f"; // String | Font color of the quote text
let authorFont = "Lato Black"; // String | Font-family used for author name
let authorFontColor = "#e5e5e5"; // String | Font color of the author
let enableHighlight = 1; // Number | Enable highlight on quote text
let highlightColor = "#f0ea66"; // String | Color used for highlight
let bgType = "gradient"; // String | Background type (gradient/solid)
let backgroundColor = "#000000"; // String | Background color for solid background type
let gradientType = "linear"; // String | Type of gradient background (linear/radial)
let gradientColor1 = "#1ee691"; // String | First color for gradient background type
let gradientColor2 = "#1ddad6"; // String | Second color for gradient background type
let brandLogo = "https://cdn.ritekit.com/assets/img/common/made-with-ritekit-white.png"; // String | URL of the brand logo
let animation = "glint"; // String | Animation type: none, rays, glint, circle
let opts = {
  'showQuoteMark': 56 // Number | showing/hiding quote mark
};
apiInstance.textToImage(quote, author, fontSize, quoteFont, quoteFontColor, authorFont, authorFontColor, enableHighlight, highlightColor, bgType, backgroundColor, gradientType, gradientColor1, gradientColor2, brandLogo, animation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote** | **String**| Text of the quote | 
 **author** | **String**| Name of the author/source | 
 **fontSize** | **Number**| Font size for the quote (author font size is calculated automatically) | 
 **quoteFont** | **String**| Font-family used for quote text | 
 **quoteFontColor** | **String**| Font color of the quote text | 
 **authorFont** | **String**| Font-family used for author name | 
 **authorFontColor** | **String**| Font color of the author | 
 **enableHighlight** | **Number**| Enable highlight on quote text | 
 **highlightColor** | **String**| Color used for highlight | 
 **bgType** | **String**| Background type (gradient/solid) | 
 **backgroundColor** | **String**| Background color for solid background type | 
 **gradientType** | **String**| Type of gradient background (linear/radial) | 
 **gradientColor1** | **String**| First color for gradient background type | 
 **gradientColor2** | **String**| Second color for gradient background type | 
 **brandLogo** | **String**| URL of the brand logo | 
 **animation** | **String**| Animation type: none, rays, glint, circle | 
 **showQuoteMark** | **Number**| showing/hiding quote mark | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## trendingHashtags

> trendingHashtags(opts)

Trending Hashtags

Returns list of hashtags currently trending on Twitter

### Example

```javascript
import RiteKitApi from 'rite_kit_api';

let apiInstance = new RiteKitApi.DefaultApi();
let opts = {
  'green': false, // Boolean | Restrict results only to green hashtags. Hides overused (red) hashtags.
  'latin': false // Boolean | Restrict results only to hashtags with latin characters
};
apiInstance.trendingHashtags(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **green** | **Boolean**| Restrict results only to green hashtags. Hides overused (red) hashtags. | [optional] [default to false]
 **latin** | **Boolean**| Restrict results only to hashtags with latin characters | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

