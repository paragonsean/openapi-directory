# DefaultApi

All URIs are relative to *https://api.bufferapp.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**infoConfigurationmediaTypeExtensionGet**](DefaultApi.md#infoConfigurationmediaTypeExtensionGet) | **GET** /info/configuration{mediaTypeExtension} |  |
| [**linksSharesmediaTypeExtensionGet**](DefaultApi.md#linksSharesmediaTypeExtensionGet) | **GET** /links/shares{mediaTypeExtension} |  |
| [**profilesIdSchedulesUpdatemediaTypeExtensionPost**](DefaultApi.md#profilesIdSchedulesUpdatemediaTypeExtensionPost) | **POST** /profiles/{id}/schedules/update{mediaTypeExtension} |  |
| [**profilesIdSchedulesmediaTypeExtensionGet**](DefaultApi.md#profilesIdSchedulesmediaTypeExtensionGet) | **GET** /profiles/{id}/schedules{mediaTypeExtension} |  |
| [**profilesIdUpdatesPendingmediaTypeExtensionGet**](DefaultApi.md#profilesIdUpdatesPendingmediaTypeExtensionGet) | **GET** /profiles/{id}/updates/pending{mediaTypeExtension} |  |
| [**profilesIdUpdatesReordermediaTypeExtensionPost**](DefaultApi.md#profilesIdUpdatesReordermediaTypeExtensionPost) | **POST** /profiles/{id}/updates/reorder{mediaTypeExtension} |  |
| [**profilesIdUpdatesSentmediaTypeExtensionGet**](DefaultApi.md#profilesIdUpdatesSentmediaTypeExtensionGet) | **GET** /profiles/{id}/updates/sent{mediaTypeExtension} |  |
| [**profilesIdUpdatesShufflemediaTypeExtensionPost**](DefaultApi.md#profilesIdUpdatesShufflemediaTypeExtensionPost) | **POST** /profiles/{id}/updates/shuffle{mediaTypeExtension} |  |
| [**profilesIdmediaTypeExtensionGet**](DefaultApi.md#profilesIdmediaTypeExtensionGet) | **GET** /profiles/{id}{mediaTypeExtension} |  |
| [**profilesmediaTypeExtensionGet**](DefaultApi.md#profilesmediaTypeExtensionGet) | **GET** /profiles{mediaTypeExtension} |  |
| [**updatesCreatemediaTypeExtensionPost**](DefaultApi.md#updatesCreatemediaTypeExtensionPost) | **POST** /updates/create{mediaTypeExtension} |  |
| [**updatesIdDestroymediaTypeExtensionPost**](DefaultApi.md#updatesIdDestroymediaTypeExtensionPost) | **POST** /updates/{id}/destroy{mediaTypeExtension} |  |
| [**updatesIdInteractionsmediaTypeExtensionGet**](DefaultApi.md#updatesIdInteractionsmediaTypeExtensionGet) | **GET** /updates/{id}/interactions{mediaTypeExtension} |  |
| [**updatesIdMoveToTopmediaTypeExtensionPost**](DefaultApi.md#updatesIdMoveToTopmediaTypeExtensionPost) | **POST** /updates/{id}/move_to_top{mediaTypeExtension} |  |
| [**updatesIdSharemediaTypeExtensionPost**](DefaultApi.md#updatesIdSharemediaTypeExtensionPost) | **POST** /updates/{id}/share{mediaTypeExtension} |  |
| [**updatesIdUpdatemediaTypeExtensionPost**](DefaultApi.md#updatesIdUpdatemediaTypeExtensionPost) | **POST** /updates/{id}/update{mediaTypeExtension} |  |
| [**updatesIdmediaTypeExtensionGet**](DefaultApi.md#updatesIdmediaTypeExtensionGet) | **GET** /updates/{id}{mediaTypeExtension} |  |
| [**usermediaTypeExtensionGet**](DefaultApi.md#usermediaTypeExtensionGet) | **GET** /user{mediaTypeExtension} |  |


<a id="infoConfigurationmediaTypeExtensionGet"></a>
# **infoConfigurationmediaTypeExtensionGet**
> ModelConfiguration infoConfigurationmediaTypeExtensionGet(mediaTypeExtension)



Returns an object with the current configuration that Buffer is using, including supported services, their icons and the varying limits of character and schedules.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | 
    try {
      ModelConfiguration result = apiInstance.infoConfigurationmediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#infoConfigurationmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**ModelConfiguration**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="linksSharesmediaTypeExtensionGet"></a>
# **linksSharesmediaTypeExtensionGet**
> Shares linksSharesmediaTypeExtensionGet(mediaTypeExtension, url)



Returns an object with a the numbers of shares a link has had using Buffer.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | 
    String url = "url_example"; // String | URL-encoded URL of the page for which the number of shares is requested.
    try {
      Shares result = apiInstance.linksSharesmediaTypeExtensionGet(mediaTypeExtension, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#linksSharesmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**|  | [enum: .json] |
| **url** | **String**| URL-encoded URL of the page for which the number of shares is requested. | |

### Return type

[**Shares**](Shares.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="profilesIdSchedulesUpdatemediaTypeExtensionPost"></a>
# **profilesIdSchedulesUpdatemediaTypeExtensionPost**
> Success profilesIdSchedulesUpdatemediaTypeExtensionPost(id, mediaTypeExtension)



\&quot;Set the posting schedules for the specified social media profile. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      Success result = apiInstance.profilesIdSchedulesUpdatemediaTypeExtensionPost(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesIdSchedulesUpdatemediaTypeExtensionPost");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="profilesIdSchedulesmediaTypeExtensionGet"></a>
# **profilesIdSchedulesmediaTypeExtensionGet**
> Schedules profilesIdSchedulesmediaTypeExtensionGet(id, mediaTypeExtension)



Returns details of the posting schedules associated with a social media profile.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      Schedules result = apiInstance.profilesIdSchedulesmediaTypeExtensionGet(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesIdSchedulesmediaTypeExtensionGet");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**Schedules**](Schedules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="profilesIdUpdatesPendingmediaTypeExtensionGet"></a>
# **profilesIdUpdatesPendingmediaTypeExtensionGet**
> UpdatesArray profilesIdUpdatesPendingmediaTypeExtensionGet(id, mediaTypeExtension, page, count, since, utc)



\&quot;Returns an array of updates that are currently in the buffer for an individual social media profile. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    Integer page = 56; // Integer | Specifies the page of status updates to receive. If not specified the first page of results will be returned.
    Integer count = 56; // Integer | Specifies the number of status updates to receive. If provided, must be between 1 and 100.
    LocalDate since = LocalDate.now(); // LocalDate | Specifies a unix timestamp which only status updates created after this time will be retrieved.
    Boolean utc = true; // Boolean | If utc is set times will be returned relative to UTC rather than the users associated timezone.
    try {
      UpdatesArray result = apiInstance.profilesIdUpdatesPendingmediaTypeExtensionGet(id, mediaTypeExtension, page, count, since, utc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesIdUpdatesPendingmediaTypeExtensionGet");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |
| **page** | **Integer**| Specifies the page of status updates to receive. If not specified the first page of results will be returned. | [optional] |
| **count** | **Integer**| Specifies the number of status updates to receive. If provided, must be between 1 and 100. | [optional] |
| **since** | **LocalDate**| Specifies a unix timestamp which only status updates created after this time will be retrieved. | [optional] |
| **utc** | **Boolean**| If utc is set times will be returned relative to UTC rather than the users associated timezone. | [optional] |

### Return type

[**UpdatesArray**](UpdatesArray.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="profilesIdUpdatesReordermediaTypeExtensionPost"></a>
# **profilesIdUpdatesReordermediaTypeExtensionPost**
> Shuffle profilesIdUpdatesReordermediaTypeExtensionPost(id, mediaTypeExtension)



Edit the order at which statuses for the specified social media profile will be sent out of the buffer. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      Shuffle result = apiInstance.profilesIdUpdatesReordermediaTypeExtensionPost(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesIdUpdatesReordermediaTypeExtensionPost");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**Shuffle**](Shuffle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="profilesIdUpdatesSentmediaTypeExtensionGet"></a>
# **profilesIdUpdatesSentmediaTypeExtensionGet**
> UpdatesArray profilesIdUpdatesSentmediaTypeExtensionGet(id, mediaTypeExtension, page, count, since, utc)



Returns an array of updates that have been sent from the buffer for an individual social media profile. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    Integer page = 56; // Integer | Specifies the page of status updates to receive. If not specified the first page of results will be returned.
    Integer count = 56; // Integer | Specifies the number of status updates to receive. If provided, must be between 1 and 100.
    LocalDate since = LocalDate.now(); // LocalDate | Specifies a unix timestamp which only status updates created after this time will be retrieved.
    Boolean utc = true; // Boolean | If utc is set times will be returned relative to UTC rather than the users associated timezone.
    try {
      UpdatesArray result = apiInstance.profilesIdUpdatesSentmediaTypeExtensionGet(id, mediaTypeExtension, page, count, since, utc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesIdUpdatesSentmediaTypeExtensionGet");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |
| **page** | **Integer**| Specifies the page of status updates to receive. If not specified the first page of results will be returned. | [optional] |
| **count** | **Integer**| Specifies the number of status updates to receive. If provided, must be between 1 and 100. | [optional] |
| **since** | **LocalDate**| Specifies a unix timestamp which only status updates created after this time will be retrieved. | [optional] |
| **utc** | **Boolean**| If utc is set times will be returned relative to UTC rather than the users associated timezone. | [optional] |

### Return type

[**UpdatesArray**](UpdatesArray.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="profilesIdUpdatesShufflemediaTypeExtensionPost"></a>
# **profilesIdUpdatesShufflemediaTypeExtensionPost**
> Shuffle profilesIdUpdatesShufflemediaTypeExtensionPost(id, mediaTypeExtension)



Randomize the order at which statuses for the specified social media profile will be sent out of the buffer. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      Shuffle result = apiInstance.profilesIdUpdatesShufflemediaTypeExtensionPost(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesIdUpdatesShufflemediaTypeExtensionPost");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**Shuffle**](Shuffle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="profilesIdmediaTypeExtensionGet"></a>
# **profilesIdmediaTypeExtensionGet**
> Profile profilesIdmediaTypeExtensionGet(mediaTypeExtension, id)



Returns details of the single specified social media profile.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | 
    String id = "id_example"; // String | 
    try {
      Profile result = apiInstance.profilesIdmediaTypeExtensionGet(mediaTypeExtension, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesIdmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**|  | [enum: .json] |
| **id** | **String**|  | |

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="profilesmediaTypeExtensionGet"></a>
# **profilesmediaTypeExtensionGet**
> List&lt;ProfilesInner&gt; profilesmediaTypeExtensionGet(mediaTypeExtension)



Returns an array of social media profiles connected to a users account.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | 
    try {
      List<ProfilesInner> result = apiInstance.profilesmediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profilesmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**List&lt;ProfilesInner&gt;**](ProfilesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="updatesCreatemediaTypeExtensionPost"></a>
# **updatesCreatemediaTypeExtensionPost**
> NewUpdate updatesCreatemediaTypeExtensionPost(mediaTypeExtension)



Create one or more new status updates. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | 
    try {
      NewUpdate result = apiInstance.updatesCreatemediaTypeExtensionPost(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatesCreatemediaTypeExtensionPost");
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
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**NewUpdate**](NewUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="updatesIdDestroymediaTypeExtensionPost"></a>
# **updatesIdDestroymediaTypeExtensionPost**
> Success updatesIdDestroymediaTypeExtensionPost(id, mediaTypeExtension)



Permanently delete an existing status update.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      Success result = apiInstance.updatesIdDestroymediaTypeExtensionPost(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatesIdDestroymediaTypeExtensionPost");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="updatesIdInteractionsmediaTypeExtensionGet"></a>
# **updatesIdInteractionsmediaTypeExtensionGet**
> Interactions updatesIdInteractionsmediaTypeExtensionGet(id, mediaTypeExtension, event, page, count)



Returns the detailed information on individual interactions with the social media update such as favorites, retweets and likes. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    String event = "event_example"; // String | Specifies a type of event to be retrieved, for example \"retweet\", \"like\", \"comment\", \"mention\" or \"reshare\". They can also be plural (e.g., \"reshares\"). Plurality has no effect other than visual semantics. See /info/configuration for more information on supported interaction events. 
    Integer page = 56; // Integer | Specifies the page of status updates to receive. If not specified the first page of results will be returned.
    Integer count = 56; // Integer | Specifies the number of status updates to receive. If provided, must be between 1 and 100.
    try {
      Interactions result = apiInstance.updatesIdInteractionsmediaTypeExtensionGet(id, mediaTypeExtension, event, page, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatesIdInteractionsmediaTypeExtensionGet");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |
| **event** | **String**| Specifies a type of event to be retrieved, for example \&quot;retweet\&quot;, \&quot;like\&quot;, \&quot;comment\&quot;, \&quot;mention\&quot; or \&quot;reshare\&quot;. They can also be plural (e.g., \&quot;reshares\&quot;). Plurality has no effect other than visual semantics. See /info/configuration for more information on supported interaction events.  | |
| **page** | **Integer**| Specifies the page of status updates to receive. If not specified the first page of results will be returned. | [optional] |
| **count** | **Integer**| Specifies the number of status updates to receive. If provided, must be between 1 and 100. | [optional] |

### Return type

[**Interactions**](Interactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="updatesIdMoveToTopmediaTypeExtensionPost"></a>
# **updatesIdMoveToTopmediaTypeExtensionPost**
> Update updatesIdMoveToTopmediaTypeExtensionPost(id, mediaTypeExtension)



Move an existing status update to the top of the queue and recalculate times for all updates in the queue. Returns the update with its new posting time.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      Update result = apiInstance.updatesIdMoveToTopmediaTypeExtensionPost(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatesIdMoveToTopmediaTypeExtensionPost");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**Update**](Update.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="updatesIdSharemediaTypeExtensionPost"></a>
# **updatesIdSharemediaTypeExtensionPost**
> Success updatesIdSharemediaTypeExtensionPost(id, mediaTypeExtension)



Immediately shares a single pending update and recalculates times for updates remaining in the queue.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      Success result = apiInstance.updatesIdSharemediaTypeExtensionPost(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatesIdSharemediaTypeExtensionPost");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="updatesIdUpdatemediaTypeExtensionPost"></a>
# **updatesIdUpdatemediaTypeExtensionPost**
> IndividualUpdate updatesIdUpdatemediaTypeExtensionPost(id, mediaTypeExtension)



Edit an existing, individual status update. 

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String mediaTypeExtension = ".json"; // String | 
    try {
      IndividualUpdate result = apiInstance.updatesIdUpdatemediaTypeExtensionPost(id, mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatesIdUpdatemediaTypeExtensionPost");
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
| **id** | **String**|  | |
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**IndividualUpdate**](IndividualUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred. |  -  |

<a id="updatesIdmediaTypeExtensionGet"></a>
# **updatesIdmediaTypeExtensionGet**
> Update updatesIdmediaTypeExtensionGet(mediaTypeExtension, id)



Returns a single social media update.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | 
    String id = "id_example"; // String | 
    try {
      Update result = apiInstance.updatesIdmediaTypeExtensionGet(mediaTypeExtension, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatesIdmediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**|  | [enum: .json] |
| **id** | **String**|  | |

### Return type

[**Update**](Update.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

<a id="usermediaTypeExtensionGet"></a>
# **usermediaTypeExtensionGet**
> User usermediaTypeExtensionGet(mediaTypeExtension)



Returns a single user.

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
    defaultClient.setBasePath("https://api.bufferapp.com/1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaTypeExtension = ".json"; // String | 
    try {
      User result = apiInstance.usermediaTypeExtensionGet(mediaTypeExtension);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#usermediaTypeExtensionGet");
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
| **mediaTypeExtension** | **String**|  | [enum: .json] |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | 1003  Parameter not recognized. 1004  Required parameter missing. 1006  Parameter value not within bounds. 1012  Profile did not save successfully. 1016  Profile buffer could not be emptied. 1022  Update did not save successfully. 1025  Update was recently posted, can&#39;t post duplicate content. 1026  Update must be in error status to requeue. 1027  Update must be in buffer and not custom scheduled in order to move to top. 1029  Event type not supported. 1030  Media filetype not supported. 1031  Media filesize out of acceptable range. 1032  Unable to post image to LinkedIn group(s). 1034  Cannot schedule updates in the past. 1033  Comments can only be posted to Facebook at this time. 1042  User did not save successfully.  |  -  |
| **403** | 403  Permission denied. 1001  Access token required. 1002  Not within application scope. 1011  No authorization to access profile. 1013  Profile schedule limit reached. 1014  Profile limit for user has been reached. 1015  Profile could not be destroyed. 1021  No authorization to access update. 1023  Update limit for profile has been reached. 1024  Update limit for team profile has been reached. 1028  Update soft limit for profile reached. 1051  No authorization to access client.  |  -  |
| **404** | 404  Endpoint not found. 1010  Profile could not be found. 1020  Update could not be found. 1050  Client could not be found.  |  -  |
| **405** | 405  Method not allowed.  |  -  |
| **406** | 1005  Unsupported response format.  |  -  |
| **500** | An unknown error occurred.  |  -  |

