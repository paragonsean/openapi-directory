# TranslationKeysApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translationKeysCreateTranslationKey**](TranslationKeysApi.md#translationKeysCreateTranslationKey) | **POST** /api/v2/TranslationKeys | Create a translationKey object. |
| [**translationKeysGet**](TranslationKeysApi.md#translationKeysGet) | **GET** /api/v2/TranslationKeys | Get a paged response of TranslationKeys. |
| [**translationKeysGetTranslationKey**](TranslationKeysApi.md#translationKeysGetTranslationKey) | **GET** /api/v2/TranslationKeys/{ID} | Get TranslationKey by ID |
| [**translationKeysUpdateTranslationKey**](TranslationKeysApi.md#translationKeysUpdateTranslationKey) | **PUT** /api/v2/TranslationKeys/{ID} | Update the StringID of the translationKey object. |


<a id="translationKeysCreateTranslationKey"></a>
# **translationKeysCreateTranslationKey**
> Integer translationKeysCreateTranslationKey(oaSSupportSharedModelsTranslationKey)

Create a translationKey object.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationKeysApi apiInstance = new TranslationKeysApi(defaultClient);
    OASSupportSharedModelsTranslationKey oaSSupportSharedModelsTranslationKey = new OASSupportSharedModelsTranslationKey(); // OASSupportSharedModelsTranslationKey | 
    try {
      Integer result = apiInstance.translationKeysCreateTranslationKey(oaSSupportSharedModelsTranslationKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationKeysApi#translationKeysCreateTranslationKey");
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
| **oaSSupportSharedModelsTranslationKey** | [**OASSupportSharedModelsTranslationKey**](OASSupportSharedModelsTranslationKey.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationKeysGet"></a>
# **translationKeysGet**
> APIIPagedResponseOASSupportSharedModelsTranslationKey translationKeysGet(limit, offset, keyNames)

Get a paged response of TranslationKeys.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationKeysApi apiInstance = new TranslationKeysApi(defaultClient);
    Integer limit = 56; // Integer | 
    Integer offset = 56; // Integer | 
    String keyNames = "keyNames_example"; // String | Can filter by keyNames, a comma deliminated list.
    try {
      APIIPagedResponseOASSupportSharedModelsTranslationKey result = apiInstance.translationKeysGet(limit, offset, keyNames);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationKeysApi#translationKeysGet");
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
| **limit** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |
| **keyNames** | **String**| Can filter by keyNames, a comma deliminated list. | [optional] |

### Return type

[**APIIPagedResponseOASSupportSharedModelsTranslationKey**](APIIPagedResponseOASSupportSharedModelsTranslationKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationKeysGetTranslationKey"></a>
# **translationKeysGetTranslationKey**
> OASSupportSharedModelsTranslationKey translationKeysGetTranslationKey(ID)

Get TranslationKey by ID

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationKeysApi apiInstance = new TranslationKeysApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      OASSupportSharedModelsTranslationKey result = apiInstance.translationKeysGetTranslationKey(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationKeysApi#translationKeysGetTranslationKey");
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
| **ID** | **Integer**|  | |

### Return type

[**OASSupportSharedModelsTranslationKey**](OASSupportSharedModelsTranslationKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationKeysUpdateTranslationKey"></a>
# **translationKeysUpdateTranslationKey**
> translationKeysUpdateTranslationKey(ID, oaSSupportSharedModelsTranslationKey)

Update the StringID of the translationKey object.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationKeysApi apiInstance = new TranslationKeysApi(defaultClient);
    Integer ID = 56; // Integer | 
    OASSupportSharedModelsTranslationKey oaSSupportSharedModelsTranslationKey = new OASSupportSharedModelsTranslationKey(); // OASSupportSharedModelsTranslationKey | 
    try {
      apiInstance.translationKeysUpdateTranslationKey(ID, oaSSupportSharedModelsTranslationKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationKeysApi#translationKeysUpdateTranslationKey");
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
| **ID** | **Integer**|  | |
| **oaSSupportSharedModelsTranslationKey** | [**OASSupportSharedModelsTranslationKey**](OASSupportSharedModelsTranslationKey.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

