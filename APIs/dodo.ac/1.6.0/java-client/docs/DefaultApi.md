# DefaultApi

All URIs are relative to *https://api.nookipedia.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nhArtArtworkGet**](DefaultApi.md#nhArtArtworkGet) | **GET** /nh/art/{artwork} | Single New Horizons artwork |
| [**nhArtGet**](DefaultApi.md#nhArtGet) | **GET** /nh/art | All New Horizons artwork |
| [**nhBugsBugGet**](DefaultApi.md#nhBugsBugGet) | **GET** /nh/bugs/{bug} | Single New Horizons bug |
| [**nhBugsGet**](DefaultApi.md#nhBugsGet) | **GET** /nh/bugs | All New Horizons bugs |
| [**nhClothingClothingGet**](DefaultApi.md#nhClothingClothingGet) | **GET** /nh/clothing/{clothing} | Single New Horizons clothing |
| [**nhClothingGet**](DefaultApi.md#nhClothingGet) | **GET** /nh/clothing | All New Horizons clothing |
| [**nhEventsGet**](DefaultApi.md#nhEventsGet) | **GET** /nh/events | All New Horizons events |
| [**nhFishFishGet**](DefaultApi.md#nhFishFishGet) | **GET** /nh/fish/{fish} | Single New Horizons fish |
| [**nhFishGet**](DefaultApi.md#nhFishGet) | **GET** /nh/fish | All New Horizons fish |
| [**nhFossilsAllFossilGet**](DefaultApi.md#nhFossilsAllFossilGet) | **GET** /nh/fossils/all/{fossil} | Single New Horizons fossil group with individual fossils |
| [**nhFossilsAllGet**](DefaultApi.md#nhFossilsAllGet) | **GET** /nh/fossils/all | All New Horizons fossil groups or individual fossil |
| [**nhFossilsGroupsFossilGroupGet**](DefaultApi.md#nhFossilsGroupsFossilGroupGet) | **GET** /nh/fossils/groups/{fossil_group} | Single New Horizons fossil group |
| [**nhFossilsGroupsGet**](DefaultApi.md#nhFossilsGroupsGet) | **GET** /nh/fossils/groups | All New Horizons fossil groups |
| [**nhFossilsIndividualsFossilGet**](DefaultApi.md#nhFossilsIndividualsFossilGet) | **GET** /nh/fossils/individuals/{fossil} | Single New Horizons fossil |
| [**nhFossilsIndividualsGet**](DefaultApi.md#nhFossilsIndividualsGet) | **GET** /nh/fossils/individuals | All New Horizons fossils |
| [**nhFurnitureFurnitureGet**](DefaultApi.md#nhFurnitureFurnitureGet) | **GET** /nh/furniture/{furniture} | Single New Horizons furniture |
| [**nhFurnitureGet**](DefaultApi.md#nhFurnitureGet) | **GET** /nh/furniture | All New Horizons furniture |
| [**nhInteriorGet**](DefaultApi.md#nhInteriorGet) | **GET** /nh/interior | All New Horizons interior items |
| [**nhInteriorItemGet**](DefaultApi.md#nhInteriorItemGet) | **GET** /nh/interior/{item} | Single New Horizons interior item |
| [**nhItemsGet**](DefaultApi.md#nhItemsGet) | **GET** /nh/items | Miscellaneous New Horizons items |
| [**nhItemsItemGet**](DefaultApi.md#nhItemsItemGet) | **GET** /nh/items/{item} | Single New Horizons miscellaneous item |
| [**nhPhotosGet**](DefaultApi.md#nhPhotosGet) | **GET** /nh/photos | All New Horizons photos and posters |
| [**nhPhotosItemGet**](DefaultApi.md#nhPhotosItemGet) | **GET** /nh/photos/{item} | Single New Horizons photo or poster |
| [**nhRecipesGet**](DefaultApi.md#nhRecipesGet) | **GET** /nh/recipes | All New Horizons recipes |
| [**nhRecipesItemGet**](DefaultApi.md#nhRecipesItemGet) | **GET** /nh/recipes/{item} | Single New Horizons recipe |
| [**nhSeaGet**](DefaultApi.md#nhSeaGet) | **GET** /nh/sea | All New Horizons sea creatures |
| [**nhSeaSeaCreatureGet**](DefaultApi.md#nhSeaSeaCreatureGet) | **GET** /nh/sea/{sea_creature} | Single New Horizons sea creature |
| [**nhToolsGet**](DefaultApi.md#nhToolsGet) | **GET** /nh/tools | All New Horizons tools |
| [**nhToolsToolGet**](DefaultApi.md#nhToolsToolGet) | **GET** /nh/tools/{tool} | Single New Horizons tool |
| [**villagersGet**](DefaultApi.md#villagersGet) | **GET** /villagers | Villagers |


<a id="nhArtArtworkGet"></a>
# **nhArtArtworkGet**
> NHArtwork nhArtArtworkGet(artwork, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons artwork

Retrieve information about a specific artwork in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String artwork = "artwork_example"; // String | The name of the artwork you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHArtwork result = apiInstance.nhArtArtworkGet(artwork, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhArtArtworkGet");
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
| **artwork** | **String**| The name of the artwork you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHArtwork**](NHArtwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the artwork. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhArtGet"></a>
# **nhArtGet**
> List&lt;NHArtwork&gt; nhArtGet(X_API_KEY, acceptVersion, hasfake, excludedetails, thumbsize)

All New Horizons artwork

Get a list of all artwork and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String hasfake = "hasfake_example"; // String | When set to `true`, only artwork that has a fake will be returned. When set to `false`, only artwork without fakes will be returned.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only artwork names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    try {
      List<NHArtwork> result = apiInstance.nhArtGet(X_API_KEY, acceptVersion, hasfake, excludedetails, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhArtGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **hasfake** | **String**| When set to &#x60;true&#x60;, only artwork that has a fake will be returned. When set to &#x60;false&#x60;, only artwork without fakes will be returned. | [optional] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only artwork names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] |

### Return type

[**List&lt;NHArtwork&gt;**](NHArtwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of artwork. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhBugsBugGet"></a>
# **nhBugsBugGet**
> NHBug nhBugsBugGet(bug, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons bug

Retrieve information about a specific bug in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String bug = "bug_example"; // String | The name of the bug you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHBug result = apiInstance.nhBugsBugGet(bug, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhBugsBugGet");
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
| **bug** | **String**| The name of the bug you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHBug**](NHBug.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the bug. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **404** | Could not find the specified bug. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhBugsGet"></a>
# **nhBugsGet**
> List&lt;NHBug&gt; nhBugsGet(X_API_KEY, acceptVersion, month, excludedetails, thumbsize)

All New Horizons bugs

Get a list of all bugs and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String month = "month_example"; // String | Retrive only the bug that are available in a specific month. Value may be the month's name (`jan`, `january`), the integer representing the month (`01`, `1`), or `current` for the current month. When `current` is specified, the return body will be an object with two arrays inside, one called `north` and the other `south` containing the bug available in each respective hemisphere. Note that the current month is calculated based off the API server's time, so it may be slightly off for you at the beginning or end of the month.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only bug names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the `month` filter, for users who want just a list of bugs in a given month but not all their respective details.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    try {
      List<NHBug> result = apiInstance.nhBugsGet(X_API_KEY, acceptVersion, month, excludedetails, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhBugsGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **month** | **String**| Retrive only the bug that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the bug available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month. | [optional] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only bug names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of bugs in a given month but not all their respective details. | [optional] |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] |

### Return type

[**List&lt;NHBug&gt;**](NHBug.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of bugs. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhClothingClothingGet"></a>
# **nhClothingClothingGet**
> NHClothing nhClothingClothingGet(clothing, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons clothing

Retrieve information about a specific clothing item in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String clothing = "clothing_example"; // String | The name of the clothing you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHClothing result = apiInstance.nhClothingClothingGet(clothing, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhClothingClothingGet");
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
| **clothing** | **String**| The name of the clothing you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHClothing**](NHClothing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the clothing. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhClothingGet"></a>
# **nhClothingGet**
> List&lt;NHClothing&gt; nhClothingGet(X_API_KEY, acceptVersion, category, color, style, labeltheme, excludedetails)

All New Horizons clothing

Get a list of all clothing items and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String category = "Tops"; // String | Specify the category of clothing to return.
    List<String> color = Arrays.asList(); // List<String> | Return clothing that matches the provided colors (may specify one or two colors). Colors are used for gifting villagers.
    List<String> style = Arrays.asList(); // List<String> | Return clothing that matches the provided styles (may specify one or two styles). Styles are used for gifting villagers.
    String labeltheme = "Comfy"; // String | Return clothing that have the specified Label theme. This is used for completing the requested outfit theme for [Label](https://nookipedia.com/wiki/Label) when she visits the player's island.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only clothing names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    try {
      List<NHClothing> result = apiInstance.nhClothingGet(X_API_KEY, acceptVersion, category, color, style, labeltheme, excludedetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhClothingGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **category** | **String**| Specify the category of clothing to return. | [optional] [enum: Tops, Bottoms, Dress-up, Headwear, Accessories, Socks, Shoes, Bags, Umbrellas] |
| **color** | [**List&lt;String&gt;**](String.md)| Return clothing that matches the provided colors (may specify one or two colors). Colors are used for gifting villagers. | [optional] [enum: Aqua, Beige, Black, Blue, Brown, Colorful, Gray, Green, Orange, Pink, Purple, Red, White, Yellow] |
| **style** | [**List&lt;String&gt;**](String.md)| Return clothing that matches the provided styles (may specify one or two styles). Styles are used for gifting villagers. | [optional] [enum: Active, Cool, Cute, Elegant, Gorgeous, Simple] |
| **labeltheme** | **String**| Return clothing that have the specified Label theme. This is used for completing the requested outfit theme for [Label](https://nookipedia.com/wiki/Label) when she visits the player&#39;s island. | [optional] [enum: Comfy, Everyday, Fairy tale, Formal, Goth, Outdoorsy, Party, Sporty, Theatrical, Vacation, Work] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only clothing names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |

### Return type

[**List&lt;NHClothing&gt;**](NHClothing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of clothing. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhEventsGet"></a>
# **nhEventsGet**
> List&lt;NHEvent&gt; nhEventsGet(X_API_KEY, acceptVersion, date, year, month, day)

All New Horizons events

Get a list of events and dates in *Animal Crossing: New Horizons*, filterable to specific years, months, or days. Data is available for the current and next year.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String date = "date_example"; // String | Specify a specific date (in the current or next year) to retrieve events for. Accepts many date formats, such as `YYYY-MM-DD` or `Month Day, Year`, as well as `today` to retrieve the current day's events (UTC time).
    String year = "year_example"; // String | Specify the year to retrieve events for. Must be the current or next year.
    String month = "month_example"; // String | Specify the month to retrieve events for (accepts multiple formats, such as `Oct`, `October`, or `10`). Most likely want to use alongside `year`, otherwise events in both the current and next year are returned.
    Integer day = 56; // Integer | Specify the day of the month to retrieve events for.
    try {
      List<NHEvent> result = apiInstance.nhEventsGet(X_API_KEY, acceptVersion, date, year, month, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhEventsGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **date** | **String**| Specify a specific date (in the current or next year) to retrieve events for. Accepts many date formats, such as &#x60;YYYY-MM-DD&#x60; or &#x60;Month Day, Year&#x60;, as well as &#x60;today&#x60; to retrieve the current day&#39;s events (UTC time). | [optional] |
| **year** | **String**| Specify the year to retrieve events for. Must be the current or next year. | [optional] |
| **month** | **String**| Specify the month to retrieve events for (accepts multiple formats, such as &#x60;Oct&#x60;, &#x60;October&#x60;, or &#x60;10&#x60;). Most likely want to use alongside &#x60;year&#x60;, otherwise events in both the current and next year are returned. | [optional] |
| **day** | **Integer**| Specify the day of the month to retrieve events for. | [optional] |

### Return type

[**List&lt;NHEvent&gt;**](NHEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of events. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFishFishGet"></a>
# **nhFishFishGet**
> NHFish nhFishFishGet(fish, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons fish

Retrieve information about a specific fish in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fish = "fish_example"; // String | The name of the fish you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHFish result = apiInstance.nhFishFishGet(fish, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFishFishGet");
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
| **fish** | **String**| The name of the fish you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHFish**](NHFish.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the fish. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **404** | Could not find the specified fish. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFishGet"></a>
# **nhFishGet**
> List&lt;NHFish&gt; nhFishGet(X_API_KEY, acceptVersion, month, excludedetails, thumbsize)

All New Horizons fish

Get a list of all fish and their details in *New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String month = "month_example"; // String | Retrive only the fish that are available in a specific month. Value may be the month's name (`jan`, `january`), the integer representing the month (`01`, `1`), or `current` for the current month. When `current` is specified, the return body will be an object with two arrays inside, one called `north` and the other `south` containing the fish available in each respective hemisphere. Note that the current month is calculated based off the API server's time, so it may be slightly off for you at the beginning or end of the month.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only fish names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the `month` filter, for users who want just a list of fish in a given month but not all their respective details.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    try {
      List<NHFish> result = apiInstance.nhFishGet(X_API_KEY, acceptVersion, month, excludedetails, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFishGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **month** | **String**| Retrive only the fish that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the fish available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month. | [optional] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only fish names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of fish in a given month but not all their respective details. | [optional] |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] |

### Return type

[**List&lt;NHFish&gt;**](NHFish.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of fish. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFossilsAllFossilGet"></a>
# **nhFossilsAllFossilGet**
> NHFossilGroupWithIndividualFossils nhFossilsAllFossilGet(fossil, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons fossil group with individual fossils

Retrieve information about a specific fossil group with their respective individual fossils in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fossil = "fossil_example"; // String | The name of the fossil OR fossil group you wish to retrieve information about. If a fossil is provided, a fossil group that the specified fossil belongs to will be returned.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHFossilGroupWithIndividualFossils result = apiInstance.nhFossilsAllFossilGet(fossil, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFossilsAllFossilGet");
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
| **fossil** | **String**| The name of the fossil OR fossil group you wish to retrieve information about. If a fossil is provided, a fossil group that the specified fossil belongs to will be returned. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHFossilGroupWithIndividualFossils**](NHFossilGroupWithIndividualFossils.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the fossil group. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFossilsAllGet"></a>
# **nhFossilsAllGet**
> List&lt;NHFossilGroupWithIndividualFossilsNoMatched&gt; nhFossilsAllGet(X_API_KEY, acceptVersion, thumbsize)

All New Horizons fossil groups or individual fossil

Get a list of all the fossil groups with their respective individual fossils in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      List<NHFossilGroupWithIndividualFossilsNoMatched> result = apiInstance.nhFossilsAllGet(X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFossilsAllGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**List&lt;NHFossilGroupWithIndividualFossilsNoMatched&gt;**](NHFossilGroupWithIndividualFossilsNoMatched.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of fossil groups. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFossilsGroupsFossilGroupGet"></a>
# **nhFossilsGroupsFossilGroupGet**
> NHFossilGroup nhFossilsGroupsFossilGroupGet(fossilGroup, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons fossil group

Retrieve information about a specific fossil group in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fossilGroup = "fossilGroup_example"; // String | The name of the fossil group you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHFossilGroup result = apiInstance.nhFossilsGroupsFossilGroupGet(fossilGroup, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFossilsGroupsFossilGroupGet");
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
| **fossilGroup** | **String**| The name of the fossil group you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHFossilGroup**](NHFossilGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the fossil group. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFossilsGroupsGet"></a>
# **nhFossilsGroupsGet**
> List&lt;NHFossilGroup&gt; nhFossilsGroupsGet(X_API_KEY, acceptVersion, thumbsize)

All New Horizons fossil groups

Get a list of all the fossil groups in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      List<NHFossilGroup> result = apiInstance.nhFossilsGroupsGet(X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFossilsGroupsGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**List&lt;NHFossilGroup&gt;**](NHFossilGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of fossil groups. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFossilsIndividualsFossilGet"></a>
# **nhFossilsIndividualsFossilGet**
> NHIndividualFossil nhFossilsIndividualsFossilGet(fossil, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons fossil

Retrieve information about a specific individual fossil in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fossil = "fossil_example"; // String | The name of the individual fossil you wish to retrieve fossil information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHIndividualFossil result = apiInstance.nhFossilsIndividualsFossilGet(fossil, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFossilsIndividualsFossilGet");
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
| **fossil** | **String**| The name of the individual fossil you wish to retrieve fossil information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHIndividualFossil**](NHIndividualFossil.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the individual fossil. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFossilsIndividualsGet"></a>
# **nhFossilsIndividualsGet**
> List&lt;NHIndividualFossil&gt; nhFossilsIndividualsGet(X_API_KEY, acceptVersion, thumbsize)

All New Horizons fossils

Get a list of all the individual fossils in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      List<NHIndividualFossil> result = apiInstance.nhFossilsIndividualsGet(X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFossilsIndividualsGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**List&lt;NHIndividualFossil&gt;**](NHIndividualFossil.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of individual fossils. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFurnitureFurnitureGet"></a>
# **nhFurnitureFurnitureGet**
> NHFurniture nhFurnitureFurnitureGet(furniture, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons furniture

Retrieve information about a specific furniture in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String furniture = "furniture_example"; // String | The name of the furniture you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHFurniture result = apiInstance.nhFurnitureFurnitureGet(furniture, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFurnitureFurnitureGet");
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
| **furniture** | **String**| The name of the furniture you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHFurniture**](NHFurniture.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the furniture. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhFurnitureGet"></a>
# **nhFurnitureGet**
> List&lt;NHFurniture&gt; nhFurnitureGet(X_API_KEY, acceptVersion, category, color, excludedetails)

All New Horizons furniture

Get a list of all furniture and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String category = "Housewares"; // String | Specify the category of furniture to return (houswares, miscellaneous, or wall-mounted).
    List<String> color = Arrays.asList(); // List<String> | Return furniture that matches the provided colors (may specify one or two colors).
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only furniture names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    try {
      List<NHFurniture> result = apiInstance.nhFurnitureGet(X_API_KEY, acceptVersion, category, color, excludedetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhFurnitureGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **category** | **String**| Specify the category of furniture to return (houswares, miscellaneous, or wall-mounted). | [optional] [enum: Housewares, Miscellaneous, Wall-mounted] |
| **color** | [**List&lt;String&gt;**](String.md)| Return furniture that matches the provided colors (may specify one or two colors). | [optional] [enum: Aqua, Beige, Black, Blue, Brown, Colorful, Gray, Green, Orange, Pink, Purple, Red, White, Yellow] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only furniture names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |

### Return type

[**List&lt;NHFurniture&gt;**](NHFurniture.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of furniture. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhInteriorGet"></a>
# **nhInteriorGet**
> List&lt;NHInterior&gt; nhInteriorGet(X_API_KEY, acceptVersion, color, excludedetails)

All New Horizons interior items

Get a list of all interior items (flooring, wallpaper, and rugs) and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    List<String> color = Arrays.asList(); // List<String> | Return furniture that matches the provided colors (may specify one or two colors).
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only interior item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    try {
      List<NHInterior> result = apiInstance.nhInteriorGet(X_API_KEY, acceptVersion, color, excludedetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhInteriorGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **color** | [**List&lt;String&gt;**](String.md)| Return furniture that matches the provided colors (may specify one or two colors). | [optional] [enum: Aqua, Beige, Black, Blue, Brown, Colorful, Gray, Green, Orange, Pink, Purple, Red, White, Yellow] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only interior item names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |

### Return type

[**List&lt;NHInterior&gt;**](NHInterior.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of interior items. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhInteriorItemGet"></a>
# **nhInteriorItemGet**
> NHInterior nhInteriorItemGet(item, X_API_KEY, acceptVersion, color, thumbsize)

Single New Horizons interior item

Retrieve information about a specific interior item in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String item = "item_example"; // String | The name of the interior item you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    List<String> color = Arrays.asList(); // List<String> | Return furniture that matches the provided colors (may specify one or two colors).
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHInterior result = apiInstance.nhInteriorItemGet(item, X_API_KEY, acceptVersion, color, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhInteriorItemGet");
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
| **item** | **String**| The name of the interior item you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **color** | [**List&lt;String&gt;**](String.md)| Return furniture that matches the provided colors (may specify one or two colors). | [optional] [enum: Aqua, Beige, Black, Blue, Brown, Colorful, Gray, Green, Orange, Pink, Purple, Red, White, Yellow] |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHInterior**](NHInterior.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the interior item. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhItemsGet"></a>
# **nhItemsGet**
> List&lt;NHItem&gt; nhItemsGet(X_API_KEY, acceptVersion, excludedetails)

Miscellaneous New Horizons items

Get a list of all miscellaneous items (such as materials, star fragments, fruits, fences, and plants) and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    try {
      List<NHItem> result = apiInstance.nhItemsGet(X_API_KEY, acceptVersion, excludedetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhItemsGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |

### Return type

[**List&lt;NHItem&gt;**](NHItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of items. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhItemsItemGet"></a>
# **nhItemsItemGet**
> NHItem nhItemsItemGet(item, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons miscellaneous item

Retrieve information about a miscellaneous item (such as materials, star fragments, fruits, fences, and plants) in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String item = "item_example"; // String | The name of the interior item you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHItem result = apiInstance.nhItemsItemGet(item, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhItemsItemGet");
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
| **item** | **String**| The name of the interior item you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHItem**](NHItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the item. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhPhotosGet"></a>
# **nhPhotosGet**
> List&lt;NHPhoto&gt; nhPhotosGet(X_API_KEY, acceptVersion, excludedetails)

All New Horizons photos and posters

Get a list of all character photos+posters and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    try {
      List<NHPhoto> result = apiInstance.nhPhotosGet(X_API_KEY, acceptVersion, excludedetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhPhotosGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |

### Return type

[**List&lt;NHPhoto&gt;**](NHPhoto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of photos and posters. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhPhotosItemGet"></a>
# **nhPhotosItemGet**
> NHPhoto nhPhotosItemGet(item, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons photo or poster

Retrieve information about a character photo or poster in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String item = "item_example"; // String | The name of the photo or poster you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHPhoto result = apiInstance.nhPhotosItemGet(item, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhPhotosItemGet");
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
| **item** | **String**| The name of the photo or poster you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHPhoto**](NHPhoto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the photo or poster. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhRecipesGet"></a>
# **nhRecipesGet**
> List&lt;NHRecipe&gt; nhRecipesGet(X_API_KEY, acceptVersion, material, excludedetails, thumbsize)

All New Horizons recipes

Get a list of all recipes and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String material = "material_example"; // String | Specify a material to only get recipes that use that material. You can specify `material` up to six times (no recipe uses more than six materials).
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only recipe names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    try {
      List<NHRecipe> result = apiInstance.nhRecipesGet(X_API_KEY, acceptVersion, material, excludedetails, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhRecipesGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **material** | **String**| Specify a material to only get recipes that use that material. You can specify &#x60;material&#x60; up to six times (no recipe uses more than six materials). | [optional] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only recipe names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] |

### Return type

[**List&lt;NHRecipe&gt;**](NHRecipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of recipes. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhRecipesItemGet"></a>
# **nhRecipesItemGet**
> NHRecipe nhRecipesItemGet(item, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons recipe

Retrieve information about a specific recipe in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String item = "item_example"; // String | The name of the item you wish to retrieve recipe information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHRecipe result = apiInstance.nhRecipesItemGet(item, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhRecipesItemGet");
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
| **item** | **String**| The name of the item you wish to retrieve recipe information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHRecipe**](NHRecipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the recipe. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhSeaGet"></a>
# **nhSeaGet**
> List&lt;NHSeaCreature&gt; nhSeaGet(X_API_KEY, acceptVersion, month, excludedetails, thumbsize)

All New Horizons sea creatures

Get a list of all sea creatures and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String month = "month_example"; // String | Retrive only the sea creature that are available in a specific month. Value may be the month's name (`jan`, `january`), the integer representing the month (`01`, `1`), or `current` for the current month. When `current` is specified, the return body will be an object with two arrays inside, one called `north` and the other `south` containing the sea creature available in each respective hemisphere. Note that the current month is calculated based off the API server's time, so it may be slightly off for you at the beginning or end of the month.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only sea creature names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the `month` filter, for users who want just a list of sea creatures in a given month but not all their respective details.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    try {
      List<NHSeaCreature> result = apiInstance.nhSeaGet(X_API_KEY, acceptVersion, month, excludedetails, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhSeaGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **month** | **String**| Retrive only the sea creature that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the sea creature available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month. | [optional] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only sea creature names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of sea creatures in a given month but not all their respective details. | [optional] |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] |

### Return type

[**List&lt;NHSeaCreature&gt;**](NHSeaCreature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of sea creatures. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhSeaSeaCreatureGet"></a>
# **nhSeaSeaCreatureGet**
> NHSeaCreature nhSeaSeaCreatureGet(seaCreature, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons sea creature

Retrieve information about a specific sea creature in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String seaCreature = "seaCreature_example"; // String | The name of the sea creature you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHSeaCreature result = apiInstance.nhSeaSeaCreatureGet(seaCreature, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhSeaSeaCreatureGet");
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
| **seaCreature** | **String**| The name of the sea creature you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHSeaCreature**](NHSeaCreature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the sea creature. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **404** | Could not find the specified sea creature. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhToolsGet"></a>
# **nhToolsGet**
> List&lt;NHTool&gt; nhToolsGet(X_API_KEY, acceptVersion, excludedetails)

All New Horizons tools

Get a list of all tools and their details in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only tool names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    try {
      List<NHTool> result = apiInstance.nhToolsGet(X_API_KEY, acceptVersion, excludedetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhToolsGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only tool names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |

### Return type

[**List&lt;NHTool&gt;**](NHTool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of interior items. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="nhToolsToolGet"></a>
# **nhToolsToolGet**
> NHTool nhToolsToolGet(tool, X_API_KEY, acceptVersion, thumbsize)

Single New Horizons tool

Retrieve information about a specific tool in *Animal Crossing: New Horizons*.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tool = "tool_example"; // String | The name of the interior item you wish to retrieve information about.
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    try {
      NHTool result = apiInstance.nhToolsToolGet(tool, X_API_KEY, acceptVersion, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nhToolsToolGet");
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
| **tool** | **String**| The name of the interior item you wish to retrieve information about. | |
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] |

### Return type

[**NHTool**](NHTool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object describing the tool. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

<a id="villagersGet"></a>
# **villagersGet**
> List&lt;Villager&gt; villagersGet(X_API_KEY, acceptVersion, name, species, personality, game, birthmonth, birthday, nhdetails, excludedetails, thumbsize)

Villagers

This endpoint retrieves villager information from the entire *Animal Crossing* series, with the option to filter by species, personality, game, and/or birthday. Filters use the AND operator (e.g. asking for villagers who have species &#x60;frog&#x60; and personality &#x60;smug&#x60; will return all smug frogs). Note that villagers only include the animals that act as residents. Special characters, such as Tom Nook and Isabelle, are not accessed through this endpoint.

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
    defaultClient.setBasePath("https://api.nookipedia.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID X_API_KEY = UUID.randomUUID(); // UUID | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    String acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    String name = "name_example"; // String | Villager name. For most names you will get back an array with one object, but note that names are not a unique identifier across the series, as there are 3 names that are shared by multiple villagers (Lulu, Petunia, Carmen). For those 3 names you will get back an array with 2 objects. How you disambiguate between these villagers is up to you.
    String species = "alligator"; // String | Retrieve villagers of a certain species.
    String personality = "big sister"; // String | Retrieve villagers with a certain personality. For 'sisterly', note that the community often also calls it 'uchi' or 'big sister'.
    List<String> game = Arrays.asList(); // List<String> | Retrieve villagers that appear in all listed games. For example, if you want only villagers that appear in both *New Horizons* and *Pocket Camp*, you would send in `?game=nh&game=pc`.
    String birthmonth = "birthmonth_example"; // String | Retrieve villagers born in a specific month. Value may be the month's name (`jan`, `january`) or the integer representing the month (`01`, `1`).
    String birthday = "birthday_example"; // String | Use with `birthmonth` to get villager(s) born on a specific day. Value should be an int, 1 through 31.
    String nhdetails = "nhdetails_example"; // String | When set to `true`, an `nh_details` object will be included that contains *New Horizons* details about the villager. If the villager does not appear in *New Horizons*, the returned `nh_details` field will be set to null.
    String excludedetails = "excludedetails_example"; // String | When set to `true`, only villager names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    Integer thumbsize = 56; // Integer | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    try {
      List<Villager> result = apiInstance.villagersGet(X_API_KEY, acceptVersion, name, species, personality, game, birthmonth, birthday, nhdetails, excludedetails, thumbsize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#villagersGet");
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
| **X_API_KEY** | **UUID**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | |
| **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | |
| **name** | **String**| Villager name. For most names you will get back an array with one object, but note that names are not a unique identifier across the series, as there are 3 names that are shared by multiple villagers (Lulu, Petunia, Carmen). For those 3 names you will get back an array with 2 objects. How you disambiguate between these villagers is up to you. | [optional] |
| **species** | **String**| Retrieve villagers of a certain species. | [optional] [enum: alligator, anteater, bear, bear cub, bird, bull, cat, cub, chicken, cow, deer, dog, duck, eagle, elephant, frog, goat, gorilla, hamster, hippo, horse, koala, kangaroo, lion, monkey, mouse, octopus, ostrich, penguin, pig, rabbit, rhino, rhinoceros, sheep, squirrel, tiger, wolf] |
| **personality** | **String**| Retrieve villagers with a certain personality. For &#39;sisterly&#39;, note that the community often also calls it &#39;uchi&#39; or &#39;big sister&#39;. | [optional] [enum: big sister, cranky, jock, lazy, normal, peppy, sisterly, smug, snooty] |
| **game** | [**List&lt;String&gt;**](String.md)| Retrieve villagers that appear in all listed games. For example, if you want only villagers that appear in both *New Horizons* and *Pocket Camp*, you would send in &#x60;?game&#x3D;nh&amp;game&#x3D;pc&#x60;. | [optional] [enum: DNM, AC, E_PLUS, WW, CF, NL, WA, NH, FILM, HHD, PC] |
| **birthmonth** | **String**| Retrieve villagers born in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;) or the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;). | [optional] |
| **birthday** | **String**| Use with &#x60;birthmonth&#x60; to get villager(s) born on a specific day. Value should be an int, 1 through 31. | [optional] |
| **nhdetails** | **String**| When set to &#x60;true&#x60;, an &#x60;nh_details&#x60; object will be included that contains *New Horizons* details about the villager. If the villager does not appear in *New Horizons*, the returned &#x60;nh_details&#x60; field will be set to null. | [optional] |
| **excludedetails** | **String**| When set to &#x60;true&#x60;, only villager names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] |
| **thumbsize** | **Integer**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] |

### Return type

[**List&lt;Villager&gt;**](Villager.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of villagers. |  -  |
| **400** | One of the inputs (usually query parameters) has an invalid value. |  -  |
| **401** | Failed to authenticate user from &#x60;X-API-KEY&#x60;. |  -  |
| **500** | There was an error fetching the requested data. |  -  |

