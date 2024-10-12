# MailApi

All URIs are relative to *https://esi.evetech.net/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCharactersCharacterIdMailLabelsLabelId**](MailApi.md#deleteCharactersCharacterIdMailLabelsLabelId) | **DELETE** /characters/{character_id}/mail/labels/{label_id}/ | Delete a mail label |
| [**deleteCharactersCharacterIdMailMailId**](MailApi.md#deleteCharactersCharacterIdMailMailId) | **DELETE** /characters/{character_id}/mail/{mail_id}/ | Delete a mail |
| [**getCharactersCharacterIdMail**](MailApi.md#getCharactersCharacterIdMail) | **GET** /characters/{character_id}/mail/ | Return mail headers |
| [**getCharactersCharacterIdMailLabels**](MailApi.md#getCharactersCharacterIdMailLabels) | **GET** /characters/{character_id}/mail/labels/ | Get mail labels and unread counts |
| [**getCharactersCharacterIdMailLists**](MailApi.md#getCharactersCharacterIdMailLists) | **GET** /characters/{character_id}/mail/lists/ | Return mailing list subscriptions |
| [**getCharactersCharacterIdMailMailId**](MailApi.md#getCharactersCharacterIdMailMailId) | **GET** /characters/{character_id}/mail/{mail_id}/ | Return a mail |
| [**postCharactersCharacterIdMail**](MailApi.md#postCharactersCharacterIdMail) | **POST** /characters/{character_id}/mail/ | Send a new mail |
| [**postCharactersCharacterIdMailLabels**](MailApi.md#postCharactersCharacterIdMailLabels) | **POST** /characters/{character_id}/mail/labels/ | Create a mail label |
| [**putCharactersCharacterIdMailMailId**](MailApi.md#putCharactersCharacterIdMailMailId) | **PUT** /characters/{character_id}/mail/{mail_id}/ | Update metadata about a mail |


<a id="deleteCharactersCharacterIdMailLabelsLabelId"></a>
# **deleteCharactersCharacterIdMailLabelsLabelId**
> deleteCharactersCharacterIdMailLabelsLabelId(characterId, labelId, datasource, token)

Delete a mail label

Delete a mail label  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/labels/{label_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/labels/{label_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/labels/{label_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    Integer labelId = 56; // Integer | An EVE label id
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.deleteCharactersCharacterIdMailLabelsLabelId(characterId, labelId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#deleteCharactersCharacterIdMailLabelsLabelId");
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
| **characterId** | **Integer**| An EVE character ID | |
| **labelId** | **Integer**| An EVE label id | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Label deleted |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **422** | Default labels cannot be deleted |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="deleteCharactersCharacterIdMailMailId"></a>
# **deleteCharactersCharacterIdMailMailId**
> deleteCharactersCharacterIdMailMailId(characterId, mailId, datasource, token)

Delete a mail

Delete a mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/{mail_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    Integer mailId = 56; // Integer | An EVE mail ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.deleteCharactersCharacterIdMailMailId(characterId, mailId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#deleteCharactersCharacterIdMailMailId");
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
| **characterId** | **Integer**| An EVE character ID | |
| **mailId** | **Integer**| An EVE mail ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Mail deleted |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getCharactersCharacterIdMail"></a>
# **getCharactersCharacterIdMail**
> List&lt;GetCharactersCharacterIdMail200Ok&gt; getCharactersCharacterIdMail(characterId, datasource, ifNoneMatch, labels, lastMailId, token)

Return mail headers

Return the 50 most recent mail headers belonging to the character that match the query criteria. Queries can be filtered by label, and last_mail_id can be used to paginate backwards  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/&#x60;  --- This route is cached for up to 30 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    Set<Integer> labels = Arrays.asList(); // Set<Integer> | Fetch only mails that match one or more of the given labels
    Integer lastMailId = 56; // Integer | List only mail with an ID lower than the given ID, if present
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      List<GetCharactersCharacterIdMail200Ok> result = apiInstance.getCharactersCharacterIdMail(characterId, datasource, ifNoneMatch, labels, lastMailId, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#getCharactersCharacterIdMail");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **labels** | [**Set&lt;Integer&gt;**](Integer.md)| Fetch only mails that match one or more of the given labels | [optional] |
| **lastMailId** | **Integer**| List only mail with an ID lower than the given ID, if present | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**List&lt;GetCharactersCharacterIdMail200Ok&gt;**](GetCharactersCharacterIdMail200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested mail |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getCharactersCharacterIdMailLabels"></a>
# **getCharactersCharacterIdMailLabels**
> GetCharactersCharacterIdMailLabelsOk getCharactersCharacterIdMailLabels(characterId, datasource, ifNoneMatch, token)

Get mail labels and unread counts

Return a list of the users mail labels, unread counts for each label and a total unread count.  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/labels/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/mail/labels/&#x60;  --- This route is cached for up to 30 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      GetCharactersCharacterIdMailLabelsOk result = apiInstance.getCharactersCharacterIdMailLabels(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#getCharactersCharacterIdMailLabels");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**GetCharactersCharacterIdMailLabelsOk**](GetCharactersCharacterIdMailLabelsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of mail labels and unread counts |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getCharactersCharacterIdMailLists"></a>
# **getCharactersCharacterIdMailLists**
> List&lt;GetCharactersCharacterIdMailLists200Ok&gt; getCharactersCharacterIdMailLists(characterId, datasource, ifNoneMatch, token)

Return mailing list subscriptions

Return all mailing lists that the character is subscribed to  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/lists/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/lists/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/lists/&#x60;  --- This route is cached for up to 120 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      List<GetCharactersCharacterIdMailLists200Ok> result = apiInstance.getCharactersCharacterIdMailLists(characterId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#getCharactersCharacterIdMailLists");
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
| **characterId** | **Integer**| An EVE character ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**List&lt;GetCharactersCharacterIdMailLists200Ok&gt;**](GetCharactersCharacterIdMailLists200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Mailing lists |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="getCharactersCharacterIdMailMailId"></a>
# **getCharactersCharacterIdMailMailId**
> GetCharactersCharacterIdMailMailIdOk getCharactersCharacterIdMailMailId(characterId, mailId, datasource, ifNoneMatch, token)

Return a mail

Return the contents of an EVE mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/{mail_id}/&#x60;  --- This route is cached for up to 30 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    Integer mailId = 56; // Integer | An EVE mail ID
    String datasource = "tranquility"; // String | The server name you would like data from
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      GetCharactersCharacterIdMailMailIdOk result = apiInstance.getCharactersCharacterIdMailMailId(characterId, mailId, datasource, ifNoneMatch, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#getCharactersCharacterIdMailMailId");
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
| **characterId** | **Integer**| An EVE character ID | |
| **mailId** | **Integer**| An EVE mail ID | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

[**GetCharactersCharacterIdMailMailIdOk**](GetCharactersCharacterIdMailMailIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contents of a mail |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Mail not found |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postCharactersCharacterIdMail"></a>
# **postCharactersCharacterIdMail**
> Integer postCharactersCharacterIdMail(characterId, mail, datasource, token)

Send a new mail

Create and send a new mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    PostCharactersCharacterIdMailMail mail = new PostCharactersCharacterIdMailMail(); // PostCharactersCharacterIdMailMail | The mail to send
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      Integer result = apiInstance.postCharactersCharacterIdMail(characterId, mail, datasource, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#postCharactersCharacterIdMail");
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
| **characterId** | **Integer**| An EVE character ID | |
| **mail** | [**PostCharactersCharacterIdMailMail**](PostCharactersCharacterIdMailMail.md)| The mail to send | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

**Integer**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Mail created |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |
| **520** | Internal error thrown from the EVE server. Most of the time this means you have hit an EVE server rate limit |  -  |

<a id="postCharactersCharacterIdMailLabels"></a>
# **postCharactersCharacterIdMailLabels**
> Integer postCharactersCharacterIdMailLabels(characterId, label, datasource, token)

Create a mail label

Create a mail label  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/labels/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/labels/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/mail/labels/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    PostCharactersCharacterIdMailLabelsLabel label = new PostCharactersCharacterIdMailLabelsLabel(); // PostCharactersCharacterIdMailLabelsLabel | Label to create
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      Integer result = apiInstance.postCharactersCharacterIdMailLabels(characterId, label, datasource, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#postCharactersCharacterIdMailLabels");
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
| **characterId** | **Integer**| An EVE character ID | |
| **label** | [**PostCharactersCharacterIdMailLabelsLabel**](PostCharactersCharacterIdMailLabelsLabel.md)| Label to create | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

**Integer**

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Label created |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="putCharactersCharacterIdMailMailId"></a>
# **putCharactersCharacterIdMailMailId**
> putCharactersCharacterIdMailMailId(characterId, mailId, contents, datasource, token)

Update metadata about a mail

Update metadata about a mail  --- Alternate route: &#x60;/dev/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/mail/{mail_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/mail/{mail_id}/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    MailApi apiInstance = new MailApi(defaultClient);
    Integer characterId = 56; // Integer | An EVE character ID
    Integer mailId = 56; // Integer | An EVE mail ID
    PutCharactersCharacterIdMailMailIdContents contents = new PutCharactersCharacterIdMailMailIdContents(); // PutCharactersCharacterIdMailMailIdContents | Data used to update the mail
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.putCharactersCharacterIdMailMailId(characterId, mailId, contents, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MailApi#putCharactersCharacterIdMailMailId");
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
| **characterId** | **Integer**| An EVE character ID | |
| **mailId** | **Integer**| An EVE mail ID | |
| **contents** | [**PutCharactersCharacterIdMailMailIdContents**](PutCharactersCharacterIdMailMailIdContents.md)| Data used to update the mail | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Mail updated |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

