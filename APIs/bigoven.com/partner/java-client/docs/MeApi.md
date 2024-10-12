# MeApi

All URIs are relative to *https://api2.bigoven.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meGetOptions**](MeApi.md#meGetOptions) | **GET** /me/preferences/options | Gets the options. |
| [**meIndex**](MeApi.md#meIndex) | **GET** /me | Indexes this instance. |
| [**meProfilePut**](MeApi.md#meProfilePut) | **PUT** /me/profile | Puts me. |
| [**mePutMe**](MeApi.md#mePutMe) | **PUT** /me | Puts me. |
| [**mePutMePersonal**](MeApi.md#mePutMePersonal) | **PUT** /me/personal | Puts me personal. |
| [**mePutMePreferences**](MeApi.md#mePutMePreferences) | **PUT** /me/preferences | Puts me preferences. |
| [**meSkinny**](MeApi.md#meSkinny) | **GET** /me/skinny | Skinnies this instance. |


<a id="meGetOptions"></a>
# **meGetOptions**
> API2ControllersWebAPIMeControllerPreferenceOptions meGetOptions()

Gets the options.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      API2ControllersWebAPIMeControllerPreferenceOptions result = apiInstance.meGetOptions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#meGetOptions");
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

[**API2ControllersWebAPIMeControllerPreferenceOptions**](API2ControllersWebAPIMeControllerPreferenceOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="meIndex"></a>
# **meIndex**
> API2ModelsBigOvenUser meIndex()

Indexes this instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      API2ModelsBigOvenUser result = apiInstance.meIndex();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#meIndex");
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

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="meProfilePut"></a>
# **meProfilePut**
> API2ModelsBigOvenUser meProfilePut(apI2ModelsProfile)

Puts me.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    MeApi apiInstance = new MeApi(defaultClient);
    API2ModelsProfile apI2ModelsProfile = new API2ModelsProfile(); // API2ModelsProfile | The req.
    try {
      API2ModelsBigOvenUser result = apiInstance.meProfilePut(apI2ModelsProfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#meProfilePut");
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
| **apI2ModelsProfile** | [**API2ModelsProfile**](API2ModelsProfile.md)| The req. | |

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="mePutMe"></a>
# **mePutMe**
> API2ModelsBigOvenUser mePutMe(apI2ModelsBigOvenUser)

Puts me.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    MeApi apiInstance = new MeApi(defaultClient);
    API2ModelsBigOvenUser apI2ModelsBigOvenUser = new API2ModelsBigOvenUser(); // API2ModelsBigOvenUser | The req.
    try {
      API2ModelsBigOvenUser result = apiInstance.mePutMe(apI2ModelsBigOvenUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#mePutMe");
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
| **apI2ModelsBigOvenUser** | [**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)| The req. | |

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="mePutMePersonal"></a>
# **mePutMePersonal**
> API2ModelsBigOvenUser mePutMePersonal(apI2ModelsPersonal)

Puts me personal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    MeApi apiInstance = new MeApi(defaultClient);
    API2ModelsPersonal apI2ModelsPersonal = new API2ModelsPersonal(); // API2ModelsPersonal | The req.
    try {
      API2ModelsBigOvenUser result = apiInstance.mePutMePersonal(apI2ModelsPersonal);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#mePutMePersonal");
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
| **apI2ModelsPersonal** | [**API2ModelsPersonal**](API2ModelsPersonal.md)| The req. | |

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="mePutMePreferences"></a>
# **mePutMePreferences**
> API2ModelsBigOvenUser mePutMePreferences(apI2ModelsPreference)

Puts me preferences.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    MeApi apiInstance = new MeApi(defaultClient);
    API2ModelsPreference apI2ModelsPreference = new API2ModelsPreference(); // API2ModelsPreference | The req.
    try {
      API2ModelsBigOvenUser result = apiInstance.mePutMePreferences(apI2ModelsPreference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#mePutMePreferences");
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
| **apI2ModelsPreference** | [**API2ModelsPreference**](API2ModelsPreference.md)| The req. | |

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="meSkinny"></a>
# **meSkinny**
> API2ModelsBigOvenUser meSkinny()

Skinnies this instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      API2ModelsBigOvenUser result = apiInstance.meSkinny();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#meSkinny");
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

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

