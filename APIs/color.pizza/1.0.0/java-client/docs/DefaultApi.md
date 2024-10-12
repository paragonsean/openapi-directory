# DefaultApi

All URIs are relative to *https://api.color.pizza/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listsGet**](DefaultApi.md#listsGet) | **GET** /lists/ | Get all colors of the default color name list |
| [**namesGet**](DefaultApi.md#namesGet) | **GET** /names/ | Get all colors of the default color name list |
| [**rootGet**](DefaultApi.md#rootGet) | **GET** / | Get all colors of the default color name list |
| [**swatchGet**](DefaultApi.md#swatchGet) | **GET** /swatch/ | Generate a color swatch for any color |


<a id="listsGet"></a>
# **listsGet**
> ListsGet200Response listsGet()

Get all colors of the default color name list

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
    defaultClient.setBasePath("https://api.color.pizza/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      ListsGet200Response result = apiInstance.listsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listsGet");
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

[**ListsGet200Response**](ListsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="namesGet"></a>
# **namesGet**
> Get200Response namesGet(name, _list)

Get all colors of the default color name list

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
    defaultClient.setBasePath("https://api.color.pizza/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | The name of the color to retrieve (min 3 characters)
    PossibleLists _list = PossibleLists.fromValue("default"); // PossibleLists | The name of the color name list to use
    try {
      Get200Response result = apiInstance.namesGet(name, _list);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#namesGet");
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
| **name** | **String**| The name of the color to retrieve (min 3 characters) | |
| **_list** | [**PossibleLists**](.md)| The name of the color name list to use | [optional] [enum: default, bestOf, wikipedia, french, ridgway, risograph, basic, chineseTraditional, html, japaneseTraditional, leCorbusier, nbsIscc, ntc, osxcrayons, ral, sanzoWadaI, thesaurus, werner, windows, x11, xkcd] |

### Return type

[**Get200Response**](Get200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="rootGet"></a>
# **rootGet**
> Get200Response rootGet(_list, values, noduplicates)

Get all colors of the default color name list

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
    defaultClient.setBasePath("https://api.color.pizza/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PossibleLists _list = PossibleLists.fromValue("default"); // PossibleLists | The name of the color name list to use
    String values = "values_example"; // String | The hex values of the colors to retrieve without '#'
    Boolean noduplicates = true; // Boolean | Allow duplicate names or not
    try {
      Get200Response result = apiInstance.rootGet(_list, values, noduplicates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rootGet");
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
| **_list** | [**PossibleLists**](.md)| The name of the color name list to use | [optional] [enum: default, bestOf, wikipedia, french, ridgway, risograph, basic, chineseTraditional, html, japaneseTraditional, leCorbusier, nbsIscc, ntc, osxcrayons, ral, sanzoWadaI, thesaurus, werner, windows, x11, xkcd] |
| **values** | **String**| The hex values of the colors to retrieve without &#39;#&#39; | [optional] |
| **noduplicates** | **Boolean**| Allow duplicate names or not | [optional] |

### Return type

[**Get200Response**](Get200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="swatchGet"></a>
# **swatchGet**
> String swatchGet(color, name)

Generate a color swatch for any color

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
    defaultClient.setBasePath("https://api.color.pizza/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String color = "color_example"; // String | The hex value of the color to retrieve without '#'
    String name = "name_example"; // String | The name of the color
    try {
      String result = apiInstance.swatchGet(color, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#swatchGet");
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
| **color** | **String**| The hex value of the color to retrieve without &#39;#&#39; | |
| **name** | **String**| The name of the color | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

