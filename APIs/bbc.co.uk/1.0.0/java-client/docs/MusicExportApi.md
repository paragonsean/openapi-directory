# MusicExportApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMusicPreferencesExport**](MusicExportApi.md#deleteMusicPreferencesExport) | **DELETE** /my/music/preferences/export | Music Export Preferences |
| [**deleteMusicPreferencesExportVendor**](MusicExportApi.md#deleteMusicPreferencesExportVendor) | **DELETE** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences |
| [**getMusicExport**](MusicExportApi.md#getMusicExport) | **GET** /my/music/export | Music Exports |
| [**getMusicExportJobs**](MusicExportApi.md#getMusicExportJobs) | **GET** /my/music/exports/jobs | Music Export Jobs |
| [**getMusicExportTracks**](MusicExportApi.md#getMusicExportTracks) | **GET** /my/music/exports/tracks | Music Export Tracks |
| [**getMusicPreferencesExport**](MusicExportApi.md#getMusicPreferencesExport) | **GET** /my/music/preferences/export | Music Export Preferences |
| [**getMusicPreferencesExportVendor**](MusicExportApi.md#getMusicPreferencesExportVendor) | **GET** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences |
| [**postMusicExportJob**](MusicExportApi.md#postMusicExportJob) | **POST** /my/music/exports/jobs | Music Export Jobs |
| [**postMusicPreferencesExport**](MusicExportApi.md#postMusicPreferencesExport) | **POST** /my/music/preferences/export | Music Export Preferences |
| [**postMusicPreferencesExportVendor**](MusicExportApi.md#postMusicPreferencesExportVendor) | **POST** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences |
| [**putMusicPreferencesExportVendor**](MusicExportApi.md#putMusicPreferencesExportVendor) | **PUT** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences |


<a id="deleteMusicPreferencesExport"></a>
# **deleteMusicPreferencesExport**
> MusicExportSuccess deleteMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey)

Music Export Preferences

Remove export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    try {
      MusicExportSuccess result = apiInstance.deleteMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#deleteMusicPreferencesExport");
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

### Return type

[**MusicExportSuccess**](MusicExportSuccess.md)

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

<a id="deleteMusicPreferencesExportVendor"></a>
# **deleteMusicPreferencesExportVendor**
> deleteMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor)

Music Export Vendor Preferences

Remove Vendor specific export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String vendor = "spotify"; // String | Supported 3rd Party Vendor
    try {
      apiInstance.deleteMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#deleteMusicPreferencesExportVendor");
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
| **vendor** | **String**| Supported 3rd Party Vendor | [enum: spotify, deezer, youtube, itunes] |

### Return type

null (empty response body)

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

<a id="getMusicExport"></a>
# **getMusicExport**
> MusicExportJob getMusicExport(authorization, xAuthenticationProvider, xAPIKey, offset, limit)

Music Exports

Returns status of all previous third party export actions for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      MusicExportJob result = apiInstance.getMusicExport(authorization, xAuthenticationProvider, xAPIKey, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#getMusicExport");
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

### Return type

[**MusicExportJob**](MusicExportJob.md)

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

<a id="getMusicExportJobs"></a>
# **getMusicExportJobs**
> MusicExportJob getMusicExportJobs(authorization, xAuthenticationProvider, xAPIKey, over16, vendor)

Music Export Jobs

All items associated to a users export request 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Boolean over16 = true; // Boolean | Boolean age check
    String vendor = "spotify"; // String | Specify Vendor Jobs
    try {
      MusicExportJob result = apiInstance.getMusicExportJobs(authorization, xAuthenticationProvider, xAPIKey, over16, vendor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#getMusicExportJobs");
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
| **over16** | **Boolean**| Boolean age check | |
| **vendor** | **String**| Specify Vendor Jobs | [optional] [enum: spotify, deezer, youtube, itunes] |

### Return type

[**MusicExportJob**](MusicExportJob.md)

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

<a id="getMusicExportTracks"></a>
# **getMusicExportTracks**
> MusicExportJob getMusicExportTracks(authorization, xAuthenticationProvider, xAPIKey, over16, offset, limit, vendor, status)

Music Export Tracks

Retrieves vendor and status specific tracks 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Boolean over16 = true; // Boolean | Boolean age check
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String vendor = "spotify"; // String | Specify Vendor Tracks
    String status = "failed"; // String | Specify Track status
    try {
      MusicExportJob result = apiInstance.getMusicExportTracks(authorization, xAuthenticationProvider, xAPIKey, over16, offset, limit, vendor, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#getMusicExportTracks");
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
| **over16** | **Boolean**| Boolean age check | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **vendor** | **String**| Specify Vendor Tracks | [optional] [enum: spotify, deezer, youtube, itunes] |
| **status** | **String**| Specify Track status | [optional] [enum: failed, done, pending] |

### Return type

[**MusicExportJob**](MusicExportJob.md)

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

<a id="getMusicPreferencesExport"></a>
# **getMusicPreferencesExport**
> MusicExportPreferencesResponse getMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey)

Music Export Preferences

Returns export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    try {
      MusicExportPreferencesResponse result = apiInstance.getMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#getMusicPreferencesExport");
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

### Return type

[**MusicExportPreferencesResponse**](MusicExportPreferencesResponse.md)

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

<a id="getMusicPreferencesExportVendor"></a>
# **getMusicPreferencesExportVendor**
> MusicExportPreferencesResponse getMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor)

Music Export Vendor Preferences

Returns vendor specific export preferences for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String vendor = "spotify"; // String | Supported 3rd Party Vendor
    try {
      MusicExportPreferencesResponse result = apiInstance.getMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#getMusicPreferencesExportVendor");
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
| **vendor** | **String**| Supported 3rd Party Vendor | [enum: spotify, deezer, youtube, itunes] |

### Return type

[**MusicExportPreferencesResponse**](MusicExportPreferencesResponse.md)

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

<a id="postMusicExportJob"></a>
# **postMusicExportJob**
> MusicExportSuccess postMusicExportJob(authorization, xAuthenticationProvider, xAPIKey, over16, body, vendor)

Music Export Jobs

Create Export Job for a user 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Boolean over16 = true; // Boolean | Boolean age check
    List<MusicExportJob> body = Arrays.asList(); // List<MusicExportJob> | 
    String vendor = "spotify"; // String | Specify Vendor Jobs
    try {
      MusicExportSuccess result = apiInstance.postMusicExportJob(authorization, xAuthenticationProvider, xAPIKey, over16, body, vendor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#postMusicExportJob");
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
| **over16** | **Boolean**| Boolean age check | |
| **body** | [**List&lt;MusicExportJob&gt;**](MusicExportJob.md)|  | |
| **vendor** | **String**| Specify Vendor Jobs | [optional] [enum: spotify, deezer, youtube, itunes] |

### Return type

[**MusicExportSuccess**](MusicExportSuccess.md)

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

<a id="postMusicPreferencesExport"></a>
# **postMusicPreferencesExport**
> MusicExportSuccess postMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey, body)

Music Export Preferences

Create export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    MusicExportPreferences body = new MusicExportPreferences(); // MusicExportPreferences | 
    try {
      MusicExportSuccess result = apiInstance.postMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#postMusicPreferencesExport");
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
| **body** | [**MusicExportPreferences**](MusicExportPreferences.md)|  | |

### Return type

[**MusicExportSuccess**](MusicExportSuccess.md)

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

<a id="postMusicPreferencesExportVendor"></a>
# **postMusicPreferencesExportVendor**
> postMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body)

Music Export Vendor Preferences

Create Vendor specific export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String vendor = "spotify"; // String | Supported 3rd Party Vendor
    MusicExportPreferences body = new MusicExportPreferences(); // MusicExportPreferences | 
    try {
      apiInstance.postMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#postMusicPreferencesExportVendor");
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
| **vendor** | **String**| Supported 3rd Party Vendor | [enum: spotify, deezer, youtube, itunes] |
| **body** | [**MusicExportPreferences**](MusicExportPreferences.md)|  | |

### Return type

null (empty response body)

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

<a id="putMusicPreferencesExportVendor"></a>
# **putMusicPreferencesExportVendor**
> putMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body)

Music Export Vendor Preferences

Update vendor specific export preferences for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicExportApi apiInstance = new MusicExportApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String vendor = "spotify"; // String | Supported 3rd Party Vendor
    MusicExportPreferences body = new MusicExportPreferences(); // MusicExportPreferences | 
    try {
      apiInstance.putMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicExportApi#putMusicPreferencesExportVendor");
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
| **vendor** | **String**| Supported 3rd Party Vendor | [enum: spotify, deezer, youtube, itunes] |
| **body** | [**MusicExportPreferences**](MusicExportPreferences.md)|  | |

### Return type

null (empty response body)

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

