# ConferenceApi

All URIs are relative to *https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v01ConferenceDeafPost**](ConferenceApi.md#v01ConferenceDeafPost) | **POST** /v0.1/ConferenceDeaf/ | /v0.1/ConferenceDeaf/ |
| [**v01ConferenceHangupPost**](ConferenceApi.md#v01ConferenceHangupPost) | **POST** /v0.1/ConferenceHangup/ | /v0.1/ConferenceHangup/ |
| [**v01ConferenceKickPost**](ConferenceApi.md#v01ConferenceKickPost) | **POST** /v0.1/ConferenceKick/ | /v0.1/ConferenceKick/ |
| [**v01ConferenceListMembersPost**](ConferenceApi.md#v01ConferenceListMembersPost) | **POST** /v0.1/ConferenceListMembers/ | /v0.1/ConferenceListMembers/ |
| [**v01ConferenceListPost**](ConferenceApi.md#v01ConferenceListPost) | **POST** /v0.1/ConferenceList/ | /v0.1/ConferenceList/ |
| [**v01ConferenceMutePost**](ConferenceApi.md#v01ConferenceMutePost) | **POST** /v0.1/ConferenceMute/ | /v0.1/ConferenceMute/ |
| [**v01ConferencePlayPost**](ConferenceApi.md#v01ConferencePlayPost) | **POST** /v0.1/ConferencePlay/ | /v0.1/ConferencePlay/ |
| [**v01ConferenceRecordStartPost**](ConferenceApi.md#v01ConferenceRecordStartPost) | **POST** /v0.1/ConferenceRecordStart/ | /v0.1/ConferenceRecordStart/ |
| [**v01ConferenceRecordStopPost**](ConferenceApi.md#v01ConferenceRecordStopPost) | **POST** /v0.1/ConferenceRecordStop/ | /v0.1/ConferenceRecordStop/ |
| [**v01ConferenceSpeakPost**](ConferenceApi.md#v01ConferenceSpeakPost) | **POST** /v0.1/ConferenceSpeak/ | /v0.1/ConferenceSpeak/ |
| [**v01ConferenceUndeafPost**](ConferenceApi.md#v01ConferenceUndeafPost) | **POST** /v0.1/ConferenceUndeaf/ | /v0.1/ConferenceUndeaf/ |
| [**v01ConferenceUnmutePost**](ConferenceApi.md#v01ConferenceUnmutePost) | **POST** /v0.1/ConferenceUnmute/ | /v0.1/ConferenceUnmute/ |


<a id="v01ConferenceDeafPost"></a>
# **v01ConferenceDeafPost**
> ConferenceDeafResponse v01ConferenceDeafPost(conferenceName, memberID)

/v0.1/ConferenceDeaf/

Blocks audio to one or more conference members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    try {
      ConferenceDeafResponse result = apiInstance.v01ConferenceDeafPost(conferenceName, memberID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceDeafPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |

### Return type

[**ConferenceDeafResponse**](ConferenceDeafResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceHangupPost"></a>
# **v01ConferenceHangupPost**
> ConferenceHangupResponse v01ConferenceHangupPost(conferenceName, memberID)

/v0.1/ConferenceHangup/

Kicks one or more conference members, without playing the kick sound

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    try {
      ConferenceHangupResponse result = apiInstance.v01ConferenceHangupPost(conferenceName, memberID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceHangupPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |

### Return type

[**ConferenceHangupResponse**](ConferenceHangupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceKickPost"></a>
# **v01ConferenceKickPost**
> ConferenceKickResponse v01ConferenceKickPost(conferenceName, memberID)

/v0.1/ConferenceKick/

Kicks one or more conference members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    try {
      ConferenceKickResponse result = apiInstance.v01ConferenceKickPost(conferenceName, memberID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceKickPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |

### Return type

[**ConferenceKickResponse**](ConferenceKickResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceListMembersPost"></a>
# **v01ConferenceListMembersPost**
> ConferenceListMembersResponse v01ConferenceListMembersPost(conferenceName, callUUIDFilter, deafFilter, memberFilter, mutedFilter)

/v0.1/ConferenceListMembers/

Retrieves the member list for a given conference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference
    String callUUIDFilter = "callUUIDFilter_example"; // String | Restricts listed calls to the provided values (comma separated call UUID list)
    Boolean deafFilter = false; // Boolean | Restricts listed members to deaf ones
    String memberFilter = "memberFilter_example"; // String | Restricts listed members to the provided values (comma separated member ID list)
    Boolean mutedFilter = false; // Boolean | Restricts listed members to muted ones
    try {
      ConferenceListMembersResponse result = apiInstance.v01ConferenceListMembersPost(conferenceName, callUUIDFilter, deafFilter, memberFilter, mutedFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceListMembersPost");
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
| **conferenceName** | **String**| Name of the conference | |
| **callUUIDFilter** | **String**| Restricts listed calls to the provided values (comma separated call UUID list) | [optional] |
| **deafFilter** | **Boolean**| Restricts listed members to deaf ones | [optional] [default to false] |
| **memberFilter** | **String**| Restricts listed members to the provided values (comma separated member ID list) | [optional] |
| **mutedFilter** | **Boolean**| Restricts listed members to muted ones | [optional] [default to false] |

### Return type

[**ConferenceListMembersResponse**](ConferenceListMembersResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceListPost"></a>
# **v01ConferenceListPost**
> ConferenceListResponse v01ConferenceListPost(callUUIDFilter, deafFilter, memberFilter, mutedFilter)

/v0.1/ConferenceList/

Returns a list of all established conferences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String callUUIDFilter = "callUUIDFilter_example"; // String | Restricts listed calls to the provided values (comma separated call UUID list)
    Boolean deafFilter = false; // Boolean | Restricts listed members to deaf ones
    String memberFilter = "memberFilter_example"; // String | Restricts listed members to the provided values (comma separated member ID list)
    Boolean mutedFilter = false; // Boolean | Restricts listed members to muted ones
    try {
      ConferenceListResponse result = apiInstance.v01ConferenceListPost(callUUIDFilter, deafFilter, memberFilter, mutedFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceListPost");
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
| **callUUIDFilter** | **String**| Restricts listed calls to the provided values (comma separated call UUID list) | [optional] |
| **deafFilter** | **Boolean**| Restricts listed members to deaf ones | [optional] [default to false] |
| **memberFilter** | **String**| Restricts listed members to the provided values (comma separated member ID list) | [optional] |
| **mutedFilter** | **Boolean**| Restricts listed members to muted ones | [optional] [default to false] |

### Return type

[**ConferenceListResponse**](ConferenceListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceMutePost"></a>
# **v01ConferenceMutePost**
> ConferenceMuteResponse v01ConferenceMutePost(conferenceName, memberID)

/v0.1/ConferenceMute/

Blocks audio from one or more conference members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    try {
      ConferenceMuteResponse result = apiInstance.v01ConferenceMutePost(conferenceName, memberID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceMutePost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |

### Return type

[**ConferenceMuteResponse**](ConferenceMuteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferencePlayPost"></a>
# **v01ConferencePlayPost**
> ConferencePlayResponse v01ConferencePlayPost(conferenceName, filePath, memberID)

/v0.1/ConferencePlay/

Plays media to one or more conference members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String filePath = "filePath_example"; // String | Path/URI of the media file to be played
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    try {
      ConferencePlayResponse result = apiInstance.v01ConferencePlayPost(conferenceName, filePath, memberID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferencePlayPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **filePath** | **String**| Path/URI of the media file to be played | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |

### Return type

[**ConferencePlayResponse**](ConferencePlayResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceRecordStartPost"></a>
# **v01ConferenceRecordStartPost**
> ConferenceRecordStartResponse v01ConferenceRecordStartPost(conferenceName, fileFormat, fileName, filePath)

/v0.1/ConferenceRecordStart/

Initiates a conference recording

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String fileFormat = "wav"; // String | File format (extension)
    String fileName = ""; // String | Recording file name (without extension); if empty, a timestamp based file name will be generated
    String filePath = ""; // String | Directory path/URI where the recording file will be saved
    try {
      ConferenceRecordStartResponse result = apiInstance.v01ConferenceRecordStartPost(conferenceName, fileFormat, fileName, filePath);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceRecordStartPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **fileFormat** | **String**| File format (extension) | [optional] [default to mp3] [enum: wav, mp3] |
| **fileName** | **String**| Recording file name (without extension); if empty, a timestamp based file name will be generated | [optional] [default to ] |
| **filePath** | **String**| Directory path/URI where the recording file will be saved | [optional] [default to ] |

### Return type

[**ConferenceRecordStartResponse**](ConferenceRecordStartResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceRecordStopPost"></a>
# **v01ConferenceRecordStopPost**
> ConferenceRecordStopResponse v01ConferenceRecordStopPost(conferenceName, recordFile)

/v0.1/ConferenceRecordStop/

Stops a conference recording

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String recordFile = "recordFile_example"; // String | Full path to recording file, as returned by ConferenceRecordStart; `all` shorthand is also available
    try {
      ConferenceRecordStopResponse result = apiInstance.v01ConferenceRecordStopPost(conferenceName, recordFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceRecordStopPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **recordFile** | **String**| Full path to recording file, as returned by ConferenceRecordStart; &#x60;all&#x60; shorthand is also available | |

### Return type

[**ConferenceRecordStopResponse**](ConferenceRecordStopResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceSpeakPost"></a>
# **v01ConferenceSpeakPost**
> ConferenceSpeakResponse v01ConferenceSpeakPost(conferenceName, memberID, text)

/v0.1/ConferenceSpeak/

Plays synthesized speech into a conference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    String text = "text_example"; // String | Text to be synthesized
    try {
      ConferenceSpeakResponse result = apiInstance.v01ConferenceSpeakPost(conferenceName, memberID, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceSpeakPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |
| **text** | **String**| Text to be synthesized | |

### Return type

[**ConferenceSpeakResponse**](ConferenceSpeakResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceUndeafPost"></a>
# **v01ConferenceUndeafPost**
> ConferenceUndeafResponse v01ConferenceUndeafPost(conferenceName, memberID)

/v0.1/ConferenceUndeaf/

Restores audio to one or more conference members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    try {
      ConferenceUndeafResponse result = apiInstance.v01ConferenceUndeafPost(conferenceName, memberID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceUndeafPost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |

### Return type

[**ConferenceUndeafResponse**](ConferenceUndeafResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ConferenceUnmutePost"></a>
# **v01ConferenceUnmutePost**
> ConferenceUnmuteResponse v01ConferenceUnmutePost(conferenceName, memberID)

/v0.1/ConferenceUnmute/

Restores audio from one or more conference members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ConferenceApi apiInstance = new ConferenceApi(defaultClient);
    String conferenceName = "conferenceName_example"; // String | Name of the conference in question
    String memberID = "memberID_example"; // String | List of comma separated member IDs to be affected; `all` shorthand is available too.
    try {
      ConferenceUnmuteResponse result = apiInstance.v01ConferenceUnmutePost(conferenceName, memberID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferenceApi#v01ConferenceUnmutePost");
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
| **conferenceName** | **String**| Name of the conference in question | |
| **memberID** | **String**| List of comma separated member IDs to be affected; &#x60;all&#x60; shorthand is available too. | |

### Return type

[**ConferenceUnmuteResponse**](ConferenceUnmuteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

