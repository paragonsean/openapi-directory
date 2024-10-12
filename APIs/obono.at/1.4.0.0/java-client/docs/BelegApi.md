# BelegApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addBeleg**](BelegApi.md#addBeleg) | **PUT** /registrierkassen/{registrierkasseUuid}/belege/{belegUuid} |  |
| [**belegeBelegUuidGet**](BelegApi.md#belegeBelegUuidGet) | **GET** /belege/{belegUuid} |  |
| [**createAbschluss**](BelegApi.md#createAbschluss) | **POST** /registrierkassen/{registrierkasseUuid}/abschluss |  |
| [**getBeleg**](BelegApi.md#getBeleg) | **GET** /registrierkassen/{registrierkasseUuid}/belege/{belegUuid} |  |
| [**getBelege**](BelegApi.md#getBelege) | **GET** /registrierkassen/{registrierkasseUuid}/belege |  |


<a id="addBeleg"></a>
# **addBeleg**
> addBeleg(registrierkasseUuid, belegUuid, belegdaten)



Signs a receipt and stores it in the \&quot;Datenerfassungsprotokoll\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BelegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BelegApi apiInstance = new BelegApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to use for signing data.
    String belegUuid = "belegUuid_example"; // String | The `_uuid` of the `Beleg` to store.
    Belegdaten belegdaten = new Belegdaten(); // Belegdaten | An object that contains all data for a particular `Beleg` and is formatted according to RKSV \"Signaturformat\".
    try {
      apiInstance.addBeleg(registrierkasseUuid, belegUuid, belegdaten);
    } catch (ApiException e) {
      System.err.println("Exception when calling BelegApi#addBeleg");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to use for signing data. | |
| **belegUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to store. | |
| **belegdaten** | [**Belegdaten**](Belegdaten.md)| An object that contains all data for a particular &#x60;Beleg&#x60; and is formatted according to RKSV \&quot;Signaturformat\&quot;. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;Beleg&#x60; has been signed and added to the \&quot;Datenerfassungsprotokoll\&quot;. |  * Location - The URL (&#x60;_href&#x60;) of the newly created &#x60;Beleg&#x60; resource. <br>  |
| **400** | The provided request payload is invalid i.e. not conform the the JSON schema. |  -  |
| **403** | Access token is either missing or invalid. Be sure to include the Authorization HTTP header. |  -  |
| **409** | A &#x60;Beleg&#x60; with this particular &#x60;belegUuid&#x60; already exists. |  -  |
| **415** | The provided request payload is not JSON encoded. |  -  |
| **429** | Request limit exceeded. |  -  |
| **500** | The receipt could not be signed either because the HSM delivered invalid data or the request signing request timed out (currently after 10 seconds). |  -  |

<a id="belegeBelegUuidGet"></a>
# **belegeBelegUuidGet**
> Beleg belegeBelegUuidGet(belegUuid)



Retrieves a particular &#x60;Beleg&#x60; from the \&quot;Datenerfassungsprotokoll\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BelegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");

    BelegApi apiInstance = new BelegApi(defaultClient);
    String belegUuid = "belegUuid_example"; // String | The `_uuid` of the `Beleg` to fetch.
    try {
      Beleg result = apiInstance.belegeBelegUuidGet(belegUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BelegApi#belegeBelegUuidGet");
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
| **belegUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to fetch. | |

### Return type

[**Beleg**](Beleg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested &#x60;Beleg&#x60; resource. |  -  |
| **404** | The requested &#x60;Beleg&#x60; resource does not exist. |  -  |

<a id="createAbschluss"></a>
# **createAbschluss**
> createAbschluss(registrierkasseUuid, abschlussbelegdaten)



Generates an &#x60;Abschlussbeleg&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BelegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BelegApi apiInstance = new BelegApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to retrieve the `Beleg` collection.
    Abschlussbelegdaten abschlussbelegdaten = new Abschlussbelegdaten(); // Abschlussbelegdaten | An object that contains all data for a particular `Abschlussbeleg`.
    try {
      apiInstance.createAbschluss(registrierkasseUuid, abschlussbelegdaten);
    } catch (ApiException e) {
      System.err.println("Exception when calling BelegApi#createAbschluss");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the &#x60;Beleg&#x60; collection. | |
| **abschlussbelegdaten** | [**Abschlussbelegdaten**](Abschlussbelegdaten.md)| An object that contains all data for a particular &#x60;Abschlussbeleg&#x60;. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;Abschlussbeleg&#x60; has been created, signed and added to the \&quot;Datenerfassungsprotokoll\&quot;. |  * Location - The URL (&#x60;_href&#x60;) of the newly created &#x60;Beleg&#x60; resource. <br>  |

<a id="getBeleg"></a>
# **getBeleg**
> Beleg getBeleg(registrierkasseUuid, belegUuid)



Retrieves a particular &#x60;Beleg&#x60; from the \&quot;Datenerfassungsprotokoll\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BelegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BelegApi apiInstance = new BelegApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` that contains the requested `Beleg`.
    String belegUuid = "belegUuid_example"; // String | The `_uuid` of the `Beleg` to fetch.
    try {
      Beleg result = apiInstance.getBeleg(registrierkasseUuid, belegUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BelegApi#getBeleg");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; that contains the requested &#x60;Beleg&#x60;. | |
| **belegUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to fetch. | |

### Return type

[**Beleg**](Beleg.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested &#x60;Beleg&#x60; resource. |  -  |
| **404** | The requested &#x60;Beleg&#x60; resource does not exist. |  -  |

<a id="getBelege"></a>
# **getBelege**
> Belege getBelege(registrierkasseUuid, format, order, limit, offset, before, after, gte, lte)



Retrieves the &#x60;Beleg&#x60; collection from the \&quot;Datenerfassungsprotokoll\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BelegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BelegApi apiInstance = new BelegApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to retrieve the `Beleg` collection.
    String format = "export"; // String | Determines the format of the `Beleg` collection.
    String order = "asc"; // String | Determines the sorting order.
    Integer limit = 56; // Integer | Limits the number of returned results.
    Integer offset = 0; // Integer | Skips the specified number of results from the result set.
    String before = "before_example"; // String | Only return results that where saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
    String after = "after_example"; // String | Only return results that where saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
    Integer gte = 56; // Integer | Only return results that have at least a particular `Belegnummer`.
    Integer lte = 56; // Integer | Only return results that have at most a particular `Belegnummer`.
    try {
      Belege result = apiInstance.getBelege(registrierkasseUuid, format, order, limit, offset, before, after, gte, lte);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BelegApi#getBelege");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the &#x60;Beleg&#x60; collection. | |
| **format** | **String**| Determines the format of the &#x60;Beleg&#x60; collection. | [default to export] [enum: export, beleg, uuidlist] |
| **order** | **String**| Determines the sorting order. | [optional] [default to asc] [enum: asc, desc] |
| **limit** | **Integer**| Limits the number of returned results. | [optional] |
| **offset** | **Integer**| Skips the specified number of results from the result set. | [optional] [default to 0] |
| **before** | **String**| Only return results that where saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **after** | **String**| Only return results that where saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] |
| **gte** | **Integer**| Only return results that have at least a particular &#x60;Belegnummer&#x60;. | [optional] |
| **lte** | **Integer**| Only return results that have at most a particular &#x60;Belegnummer&#x60;. | [optional] |

### Return type

[**Belege**](Belege.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;Beleg&#x60; collection from the \&quot;Datenerfassungsprotokoll\&quot;. |  -  |

