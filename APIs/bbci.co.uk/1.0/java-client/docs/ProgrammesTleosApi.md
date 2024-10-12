# ProgrammesTleosApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBroadcastsByChannel**](ProgrammesTleosApi.md#getBroadcastsByChannel) | **GET** /channels/{channel}/broadcasts | Get broadcasts by channel |
| [**getHighlightsByCategory**](ProgrammesTleosApi.md#getHighlightsByCategory) | **GET** /categories/{category}/highlights | List the highlights for a category. |
| [**getProgrammeHighlights**](ProgrammesTleosApi.md#getProgrammeHighlights) | **GET** /home/highlights | Get programme highlights |
| [**getProgrammesByCategory**](ProgrammesTleosApi.md#getProgrammesByCategory) | **GET** /categories/{category}/programmes | List all the programmes for a category. |
| [**getProgrammesByChannel**](ProgrammesTleosApi.md#getProgrammesByChannel) | **GET** /channels/{channel}/programmes | Get programmes by channel |
| [**getProgrammesByParentPID**](ProgrammesTleosApi.md#getProgrammesByParentPID) | **GET** /programmes/{pid} | Programme for a given pid. |


<a id="getBroadcastsByChannel"></a>
# **getBroadcastsByChannel**
> Object getBroadcastsByChannel(channel, lang, rights, availability, perPage, mixin, from)

Get broadcasts by channel

Get broadcasts by channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesTleosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ProgrammesTleosApi apiInstance = new ProgrammesTleosApi(defaultClient);
    String channel = "channel_example"; // String | The channel identifier to limit results to.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Long perPage = 56L; // Long | The number of results to return.
    List<String> mixin = Arrays.asList(); // List<String> | Request additional data in the output
    String from = "from_example"; // String | Time to return results from, e.g. -3h
    try {
      Object result = apiInstance.getBroadcastsByChannel(channel, lang, rights, availability, perPage, mixin, from);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesTleosApi#getBroadcastsByChannel");
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
| **channel** | **String**| The channel identifier to limit results to. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **perPage** | **Long**| The number of results to return. | |
| **mixin** | [**List&lt;String&gt;**](String.md)| Request additional data in the output | [optional] [enum: live, promotions] |
| **from** | **String**| Time to return results from, e.g. -3h | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getHighlightsByCategory"></a>
# **getHighlightsByCategory**
> Object getHighlightsByCategory(category, lang, rights, availability, mixin)

List the highlights for a category.

Get the editorial highlights of a given category in TV &amp; iPlayer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesTleosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ProgrammesTleosApi apiInstance = new ProgrammesTleosApi(defaultClient);
    String category = "category_example"; // String | The category identifier to return results from.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    List<String> mixin = Arrays.asList(); // List<String> | Request additional data in the output
    try {
      Object result = apiInstance.getHighlightsByCategory(category, lang, rights, availability, mixin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesTleosApi#getHighlightsByCategory");
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
| **category** | **String**| The category identifier to return results from. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Request additional data in the output | [optional] [enum: live, promotions] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getProgrammeHighlights"></a>
# **getProgrammeHighlights**
> Object getProgrammeHighlights(lang, rights, availability, mixin)

Get programme highlights

Get programme highlights

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesTleosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ProgrammesTleosApi apiInstance = new ProgrammesTleosApi(defaultClient);
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    List<String> mixin = Arrays.asList(); // List<String> | Request additional data in the output
    try {
      Object result = apiInstance.getProgrammeHighlights(lang, rights, availability, mixin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesTleosApi#getProgrammeHighlights");
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
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Request additional data in the output | [optional] [enum: live, promotions] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getProgrammesByCategory"></a>
# **getProgrammesByCategory**
> Object getProgrammesByCategory(category, lang, rights, availability, page, perPage)

List all the programmes for a category.

Get the list of all the Programmes (TLEOs) for a given category in TV &amp; iPlayer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesTleosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ProgrammesTleosApi apiInstance = new ProgrammesTleosApi(defaultClient);
    String category = "category_example"; // String | The category identifier to return results from.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Long page = 56L; // Long | The page index.
    Long perPage = 56L; // Long | The number of results to return.
    try {
      Object result = apiInstance.getProgrammesByCategory(category, lang, rights, availability, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesTleosApi#getProgrammesByCategory");
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
| **category** | **String**| The category identifier to return results from. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **page** | **Long**| The page index. | |
| **perPage** | **Long**| The number of results to return. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getProgrammesByChannel"></a>
# **getProgrammesByChannel**
> Object getProgrammesByChannel(channel, lang, rights, availability, page, perPage)

Get programmes by channel

Get programmes by channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesTleosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ProgrammesTleosApi apiInstance = new ProgrammesTleosApi(defaultClient);
    String channel = "channel_example"; // String | The channel identifier to limit results to.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Long page = 56L; // Long | The page index.
    Long perPage = 56L; // Long | The number of results to return.
    try {
      Object result = apiInstance.getProgrammesByChannel(channel, lang, rights, availability, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesTleosApi#getProgrammesByChannel");
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
| **channel** | **String**| The channel identifier to limit results to. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **page** | **Long**| The page index. | |
| **perPage** | **Long**| The number of results to return. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getProgrammesByParentPID"></a>
# **getProgrammesByParentPID**
> Object getProgrammesByParentPID(pid, rights, availability, initialChildCount)

Programme for a given pid.

Get the programme for a given programme identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesTleosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ProgrammesTleosApi apiInstance = new ProgrammesTleosApi(defaultClient);
    String pid = "pid_example"; // String | The programme identifier.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Integer initialChildCount = 4; // Integer | The depth to return child entities.
    try {
      Object result = apiInstance.getProgrammesByParentPID(pid, rights, availability, initialChildCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesTleosApi#getProgrammesByParentPID");
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
| **pid** | **String**| The programme identifier. | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **initialChildCount** | **Integer**| The depth to return child entities. | [default to 4] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

