# RadioApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePersonalisedRadioByActivityTypeById**](RadioApi.md#deletePersonalisedRadioByActivityTypeById) | **DELETE** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip |
| [**deletePersonalisedRadioFollowsByTypeById**](RadioApi.md#deletePersonalisedRadioFollowsByTypeById) | **DELETE** /my/radio/follows/{type}/{pid} | Followed Brand or Series |
| [**getPersonalisedRadioByActivityTypeById**](RadioApi.md#getPersonalisedRadioByActivityTypeById) | **GET** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip |
| [**getPersonalisedRadioFavourites**](RadioApi.md#getPersonalisedRadioFavourites) | **GET** /my/radio/favourites | Favourite Episodes and Clips |
| [**getPersonalisedRadioFavouritesByType**](RadioApi.md#getPersonalisedRadioFavouritesByType) | **GET** /my/radio/favourites/{type} | Favourite Episodes and Clips by Type |
| [**getPersonalisedRadioFollows**](RadioApi.md#getPersonalisedRadioFollows) | **GET** /my/radio/follows | Followed Brands and Series |
| [**getPersonalisedRadioFollowsByType**](RadioApi.md#getPersonalisedRadioFollowsByType) | **GET** /my/radio/follows/{type} | Followed Brands or Series by Type |
| [**getPersonalisedRadioFollowsByTypeById**](RadioApi.md#getPersonalisedRadioFollowsByTypeById) | **GET** /my/radio/follows/{type}/{pid} | Followed Brand or Series |
| [**getPersonalisedRadioPlays**](RadioApi.md#getPersonalisedRadioPlays) | **GET** /my/radio/plays | Played Episode or Clip |
| [**postPersonalisedRadioBatch**](RadioApi.md#postPersonalisedRadioBatch) | **POST** /my/radio/favourites | Favourite Episodes and Clips |
| [**postPersonalisedRadioByActivityTypeById**](RadioApi.md#postPersonalisedRadioByActivityTypeById) | **POST** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip |
| [**postPersonalisedRadioFollowsBatch**](RadioApi.md#postPersonalisedRadioFollowsBatch) | **POST** /my/radio/follows | Followed Brands and Series |
| [**postPersonalisedRadioFollowsByTypeById**](RadioApi.md#postPersonalisedRadioFollowsByTypeById) | **POST** /my/radio/follows/{type}/{pid} | Followed Brand or Series |
| [**putPersonalisedRadioBatch**](RadioApi.md#putPersonalisedRadioBatch) | **PUT** /my/radio/favourites | Favourite Episodes and Clips |
| [**putPersonalisedRadioByActivityTypeById**](RadioApi.md#putPersonalisedRadioByActivityTypeById) | **PUT** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip |
| [**putPersonalisedRadioFollowsBatch**](RadioApi.md#putPersonalisedRadioFollowsBatch) | **PUT** /my/radio/follows | Followed Brands and Series |
| [**putPersonalisedRadioFollowsByTypeById**](RadioApi.md#putPersonalisedRadioFollowsByTypeById) | **PUT** /my/radio/follows/{type}/{pid} | Followed Brand or Series |


<a id="deletePersonalisedRadioByActivityTypeById"></a>
# **deletePersonalisedRadioByActivityTypeById**
> PersonalisedRadioSuccessResponse deletePersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid)

Favourite Episode or Clip

Remove User favourite 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Radio favourite types: Clips or Episodes
    String pid = "pid_example"; // String | pid
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.deletePersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#deletePersonalisedRadioByActivityTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio favourite types: Clips or Episodes | [enum: clips, episodes] |
| **pid** | **String**| pid | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="deletePersonalisedRadioFollowsByTypeById"></a>
# **deletePersonalisedRadioFollowsByTypeById**
> PersonalisedRadioSuccessResponse deletePersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid)

Followed Brand or Series

Remove &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "brands"; // String | Supported Radio follows types: Brands or Series
    String pid = "pid_example"; // String | pid
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.deletePersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#deletePersonalisedRadioFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio follows types: Brands or Series | [enum: brands, series] |
| **pid** | **String**| pid | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedRadioByActivityTypeById"></a>
# **getPersonalisedRadioByActivityTypeById**
> PersonalisedRadioResponse getPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, showAllActivity)

Favourite Episode or Clip

Check to see if a single clip or episode entity is in a users favourites - determines UX of add button.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Radio favourite types: Clips or Episodes
    String pid = "pid_example"; // String | pid
    Boolean showAllActivity = true; // Boolean | Include items which have been 'soft' unfavourited in response. I.e items with UAS type of 'unfavourited'
    try {
      PersonalisedRadioResponse result = apiInstance.getPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, showAllActivity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getPersonalisedRadioByActivityTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio favourite types: Clips or Episodes | [enum: clips, episodes] |
| **pid** | **String**| pid | |
| **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39; | [optional] |

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedRadioFavourites"></a>
# **getPersonalisedRadioFavourites**
> PersonalisedRadioResponse getPersonalisedRadioFavourites(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity)

Favourite Episodes and Clips

List of favourited episodes and clips for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String sort = "programme_titles"; // String | Sort order for Personalised Radio results
    Boolean showAllActivity = true; // Boolean | Include items which have been 'soft' unfavourited in response. I.e items with UAS type of 'unfavourited'
    try {
      PersonalisedRadioResponse result = apiInstance.getPersonalisedRadioFavourites(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getPersonalisedRadioFavourites");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **sort** | **String**| Sort order for Personalised Radio results | [optional] [enum: programme_titles, available_from_date, available_to_date] |
| **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39; | [optional] |

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedRadioFavouritesByType"></a>
# **getPersonalisedRadioFavouritesByType**
> PersonalisedRadioResponse getPersonalisedRadioFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, sort, showAllActivity, offset, limit)

Favourite Episodes and Clips by Type

List of followed &#39;clips&#39; or &#39;episode&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Radio favourite types: Clips or Episodes
    String sort = "programme_titles"; // String | Sort order for Personalised Radio results
    Boolean showAllActivity = true; // Boolean | Include items which have been 'soft' unfavourited in response. I.e items with UAS type of 'unfavourited'
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PersonalisedRadioResponse result = apiInstance.getPersonalisedRadioFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, sort, showAllActivity, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getPersonalisedRadioFavouritesByType");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio favourite types: Clips or Episodes | [enum: clips, episodes] |
| **sort** | **String**| Sort order for Personalised Radio results | [optional] [enum: programme_titles, available_from_date, available_to_date] |
| **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39; | [optional] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedRadioFollows"></a>
# **getPersonalisedRadioFollows**
> PersonalisedRadioResponse getPersonalisedRadioFollows(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity)

Followed Brands and Series

List of favourited brands and series for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String sort = "programme_titles"; // String | Sort order for Personalised Radio results
    Boolean showAllActivity = true; // Boolean | Include items which have been 'soft' unfollowed in response. I.e items with UAS type of 'unfollowed'
    try {
      PersonalisedRadioResponse result = apiInstance.getPersonalisedRadioFollows(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getPersonalisedRadioFollows");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **sort** | **String**| Sort order for Personalised Radio results | [optional] [enum: programme_titles, available_from_date, available_to_date] |
| **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfollowed in response. I.e items with UAS type of &#39;unfollowed&#39; | [optional] |

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedRadioFollowsByType"></a>
# **getPersonalisedRadioFollowsByType**
> PersonalisedRadioResponse getPersonalisedRadioFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, sort, offset, limit, showAllActivity)

Followed Brands or Series by Type

List of followed &#39;brand&#39; or &#39;series&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "brands"; // String | Supported Radio follows types: Brands or Series
    String sort = "programme_titles"; // String | Sort order for Personalised Radio results
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    Boolean showAllActivity = true; // Boolean | Include items which have been 'soft' unfollowed in response. I.e items with UAS type of 'unfollowed'
    try {
      PersonalisedRadioResponse result = apiInstance.getPersonalisedRadioFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, sort, offset, limit, showAllActivity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getPersonalisedRadioFollowsByType");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio follows types: Brands or Series | [enum: brands, series] |
| **sort** | **String**| Sort order for Personalised Radio results | [optional] [enum: programme_titles, available_from_date, available_to_date] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfollowed in response. I.e items with UAS type of &#39;unfollowed&#39; | [optional] |

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedRadioFollowsByTypeById"></a>
# **getPersonalisedRadioFollowsByTypeById**
> PersonalisedRadioResponse getPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid)

Followed Brand or Series

Check to see if a single brand or series entity is in a users follows - determines UX of add button. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "brands"; // String | Supported Radio follows types: Brands or Series
    String pid = "pid_example"; // String | pid
    try {
      PersonalisedRadioResponse result = apiInstance.getPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getPersonalisedRadioFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio follows types: Brands or Series | [enum: brands, series] |
| **pid** | **String**| pid | |

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedRadioPlays"></a>
# **getPersonalisedRadioPlays**
> PersonalisedRadioResponse getPersonalisedRadioPlays(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity)

Played Episode or Clip

Returns mixed episode and clip plays for a given BBC iPlayer radio user.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String sort = "programme_titles"; // String | Sort order for Personalised Radio results
    Boolean showAllActivity = true; // Boolean | Include expired/unavailable items
    try {
      PersonalisedRadioResponse result = apiInstance.getPersonalisedRadioPlays(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getPersonalisedRadioPlays");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **sort** | **String**| Sort order for Personalised Radio results | [optional] [enum: programme_titles, available_from_date, available_to_date] |
| **showAllActivity** | **Boolean**| Include expired/unavailable items | [optional] |

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedRadioBatch"></a>
# **postPersonalisedRadioBatch**
> PersonalisedRadioSuccessResponse postPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Episodes and Clips

Add User favourites  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedRadioBatchRequest> body = Arrays.asList(); // List<PersonalisedRadioBatchRequest> | Action favourited or unfavourited
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.postPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#postPersonalisedRadioBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedRadioBatchRequest&gt;**](PersonalisedRadioBatchRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedRadioByActivityTypeById"></a>
# **postPersonalisedRadioByActivityTypeById**
> PersonalisedRadioSuccessResponse postPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Favourite Episode or Clip

Add User favourite  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Radio favourite types: Clips or Episodes
    String pid = "pid_example"; // String | pid
    PersonalisedRadioRequest body = new PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action favourited or unfavourited
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.postPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#postPersonalisedRadioByActivityTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio favourite types: Clips or Episodes | [enum: clips, episodes] |
| **pid** | **String**| pid | |
| **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedRadioFollowsBatch"></a>
# **postPersonalisedRadioFollowsBatch**
> PersonalisedRadioSuccessResponse postPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Followed Brands and Series

Add &#39;brand&#39; or &#39;series&#39; items to a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedRadioBatchRequest> body = Arrays.asList(); // List<PersonalisedRadioBatchRequest> | Action followed or unfollowed
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.postPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#postPersonalisedRadioFollowsBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedRadioBatchRequest&gt;**](PersonalisedRadioBatchRequest.md)| Action followed or unfollowed | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedRadioFollowsByTypeById"></a>
# **postPersonalisedRadioFollowsByTypeById**
> PersonalisedRadioSuccessResponse postPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Followed Brand or Series

Add &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "brands"; // String | Supported Radio follows types: Brands or Series
    String pid = "pid_example"; // String | pid
    PersonalisedRadioRequest body = new PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action followed or unfollowed
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.postPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#postPersonalisedRadioFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio follows types: Brands or Series | [enum: brands, series] |
| **pid** | **String**| pid | |
| **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action followed or unfollowed | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedRadioBatch"></a>
# **putPersonalisedRadioBatch**
> PersonalisedRadioSuccessResponse putPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Episodes and Clips

Update user favourites  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedRadioBatchRequest> body = Arrays.asList(); // List<PersonalisedRadioBatchRequest> | Action favourited or unfavourited
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.putPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#putPersonalisedRadioBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedRadioBatchRequest&gt;**](PersonalisedRadioBatchRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedRadioByActivityTypeById"></a>
# **putPersonalisedRadioByActivityTypeById**
> PersonalisedRadioSuccessResponse putPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Favourite Episode or Clip

Update user favourite  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Radio favourite types: Clips or Episodes
    String pid = "pid_example"; // String | pid
    PersonalisedRadioRequest body = new PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action favourited or unfavourited
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.putPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#putPersonalisedRadioByActivityTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio favourite types: Clips or Episodes | [enum: clips, episodes] |
| **pid** | **String**| pid | |
| **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedRadioFollowsBatch"></a>
# **putPersonalisedRadioFollowsBatch**
> PersonalisedRadioSuccessResponse putPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Followed Brands and Series

Update &#39;brands&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedRadioBatchRequest> body = Arrays.asList(); // List<PersonalisedRadioBatchRequest> | Action followed or unfollowed
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.putPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#putPersonalisedRadioFollowsBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedRadioBatchRequest&gt;**](PersonalisedRadioBatchRequest.md)| Action followed or unfollowed | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedRadioFollowsByTypeById"></a>
# **putPersonalisedRadioFollowsByTypeById**
> PersonalisedRadioSuccessResponse putPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Followed Brand or Series

Update &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "brands"; // String | Supported Radio follows types: Brands or Series
    String pid = "pid_example"; // String | pid
    PersonalisedRadioRequest body = new PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action followed or unfollowed
    try {
      PersonalisedRadioSuccessResponse result = apiInstance.putPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#putPersonalisedRadioFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Radio follows types: Brands or Series | [enum: brands, series] |
| **pid** | **String**| pid | |
| **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action followed or unfollowed | |

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

