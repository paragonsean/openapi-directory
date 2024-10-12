# TagApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tagsGet**](TagApi.md#tagsGet) | **GET** /tags | List tags |
| [**tagsIdGet**](TagApi.md#tagsIdGet) | **GET** /tags/{id} | Retrieve a single tag by id |
| [**tagsPost**](TagApi.md#tagsPost) | **POST** /tags | Create a new tag |
| [**tagsetsGet**](TagApi.md#tagsetsGet) | **GET** /tagsets | List tag sets |
| [**tagsetsIdGet**](TagApi.md#tagsetsIdGet) | **GET** /tagsets/{id} | Retrieve a single tag set by id |
| [**tagsetsPost**](TagApi.md#tagsetsPost) | **POST** /tagsets | Create a new tag set |


<a id="tagsGet"></a>
# **tagsGet**
> List&lt;Tag&gt; tagsGet(ownedBy, tagSet, urlWords)

List tags

Retrieve tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    TagApi apiInstance = new TagApi(defaultClient);
    String ownedBy = "ownedBy_example"; // String | Restrict results to those owned by this user.
    String tagSet = "tagSet_example"; // String | Restrict results to tags belonging to this tag set.
    String urlWords = "urlWords_example"; // String | Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.
    try {
      List<Tag> result = apiInstance.tagsGet(ownedBy, tagSet, urlWords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagApi#tagsGet");
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
| **ownedBy** | **String**| Restrict results to those owned by this user. | [optional] |
| **tagSet** | **String**| Restrict results to tags belonging to this tag set. | [optional] |
| **urlWords** | **String**| Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags. | [optional] |

### Return type

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of tags |  * X-total-count - Total number of matching users <br>  |

<a id="tagsIdGet"></a>
# **tagsIdGet**
> Tag tagsIdGet(id)

Retrieve a single tag by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    TagApi apiInstance = new TagApi(defaultClient);
    String id = "id_example"; // String | Id of the tag to return
    try {
      Tag result = apiInstance.tagsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagApi#tagsIdGet");
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
| **id** | **String**| Id of the tag to return | |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tag |  -  |
| **404** | Not found |  -  |

<a id="tagsPost"></a>
# **tagsPost**
> Tag tagsPost(tagSubmission)

Create a new tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    TagApi apiInstance = new TagApi(defaultClient);
    TagSubmission tagSubmission = new TagSubmission(); // TagSubmission | Tag object to be created
    try {
      Tag result = apiInstance.tagsPost(tagSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagApi#tagsPost");
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
| **tagSubmission** | [**TagSubmission**](TagSubmission.md)| Tag object to be created | |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag created |  -  |
| **400** | The new tag submission failed to validate. Check the response body for details. |  -  |
| **500** | Failed to create the new tag due to an unexcepted error. |  -  |

<a id="tagsetsGet"></a>
# **tagsetsGet**
> List&lt;TagSet&gt; tagsetsGet(ownedBy, urlWords)

List tag sets

Retrieve tag sets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    TagApi apiInstance = new TagApi(defaultClient);
    String ownedBy = "ownedBy_example"; // String | Restrict results to those owned by this user.
    String urlWords = "urlWords_example"; // String | Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.
    try {
      List<TagSet> result = apiInstance.tagsetsGet(ownedBy, urlWords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagApi#tagsetsGet");
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
| **ownedBy** | **String**| Restrict results to those owned by this user. | [optional] |
| **urlWords** | **String**| Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets. | [optional] |

### Return type

[**List&lt;TagSet&gt;**](TagSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of tag sets |  * X-total-count - Total number of matching users <br>  |

<a id="tagsetsIdGet"></a>
# **tagsetsIdGet**
> TagSet tagsetsIdGet(id)

Retrieve a single tag set by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    TagApi apiInstance = new TagApi(defaultClient);
    String id = "id_example"; // String | Id of the tag set to return
    try {
      TagSet result = apiInstance.tagsetsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagApi#tagsetsIdGet");
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
| **id** | **String**| Id of the tag set to return | |

### Return type

[**TagSet**](TagSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tag set |  -  |
| **404** | Not found |  -  |

<a id="tagsetsPost"></a>
# **tagsetsPost**
> TagSet tagsetsPost(tagSetSubmission)

Create a new tag set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    TagApi apiInstance = new TagApi(defaultClient);
    TagSetSubmission tagSetSubmission = new TagSetSubmission(); // TagSetSubmission | Tag set to be created
    try {
      TagSet result = apiInstance.tagsetsPost(tagSetSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagApi#tagsetsPost");
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
| **tagSetSubmission** | [**TagSetSubmission**](TagSetSubmission.md)| Tag set to be created | |

### Return type

[**TagSet**](TagSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tagset created |  -  |

