# LicenseeApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLicensee**](LicenseeApi.md#createLicensee) | **POST** /licensee | Create Licensee |
| [**deleteLicensee**](LicenseeApi.md#deleteLicensee) | **DELETE** /licensee/{licenseeNumber} | Delete Licensee |
| [**getLicensee**](LicenseeApi.md#getLicensee) | **GET** /licensee/{licenseeNumber} | Get Licensee |
| [**listLicensees**](LicenseeApi.md#listLicensees) | **GET** /licensee | List Licensees |
| [**transferLicenses**](LicenseeApi.md#transferLicenses) | **POST** /licensee/{licenseeNumber}/transfer | Transfer Licenses |
| [**updateLicensee**](LicenseeApi.md#updateLicensee) | **POST** /licensee/{licenseeNumber} | Update Licensee |
| [**validateLicensee**](LicenseeApi.md#validateLicensee) | **POST** /licensee/{licenseeNumber}/validate | Validate Licensee |


<a id="createLicensee"></a>
# **createLicensee**
> Netlicensing createLicensee(active, productNumber, markedForTransfer, name, number)

Create Licensee

Creates a new Licensee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseeApi apiInstance = new LicenseeApi(defaultClient);
    Boolean active = true; // Boolean | If set to 'false', the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled
    String productNumber = "productNumber_example"; // String | 'productNumber' to assign new Licensee object
    Boolean markedForTransfer = true; // Boolean | Mark Licensee for transfer.
    String name = "name_example"; // String | 
    String number = "number_example"; // String | Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee
    try {
      Netlicensing result = apiInstance.createLicensee(active, productNumber, markedForTransfer, name, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseeApi#createLicensee");
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
| **active** | **Boolean**| If set to &#39;false&#39;, the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled | |
| **productNumber** | **String**| &#39;productNumber&#39; to assign new Licensee object | |
| **markedForTransfer** | **Boolean**| Mark Licensee for transfer. | [optional] |
| **name** | **String**|  | [optional] |
| **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **402** | Quota exceeded |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="deleteLicensee"></a>
# **deleteLicensee**
> Netlicensing deleteLicensee(licenseeNumber, forceCascade)

Delete Licensee

Delete a Licensee by &#39;number&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseeApi apiInstance = new LicenseeApi(defaultClient);
    String licenseeNumber = "licenseeNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Licensee.
    Boolean forceCascade = true; // Boolean | Force object deletion and all descendants.
    try {
      Netlicensing result = apiInstance.deleteLicensee(licenseeNumber, forceCascade);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseeApi#deleteLicensee");
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
| **licenseeNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. | |
| **forceCascade** | **Boolean**| Force object deletion and all descendants. | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="getLicensee"></a>
# **getLicensee**
> Netlicensing getLicensee(licenseeNumber)

Get Licensee

Return a Licensee by &#39;licenseeNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseeApi apiInstance = new LicenseeApi(defaultClient);
    String licenseeNumber = "licenseeNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee.
    try {
      Netlicensing result = apiInstance.getLicensee(licenseeNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseeApi#getLicensee");
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
| **licenseeNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee. | |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="listLicensees"></a>
# **listLicensees**
> List&lt;Netlicensing&gt; listLicensees()

List Licensees

Return a list of all Licensees for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseeApi apiInstance = new LicenseeApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listLicensees();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseeApi#listLicensees");
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

[**List&lt;Netlicensing&gt;**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="transferLicenses"></a>
# **transferLicenses**
> Netlicensing transferLicenses(licenseeNumber, sourceLicenseeNumber)

Transfer Licenses

Licenses transfer between Licensees

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseeApi apiInstance = new LicenseeApi(defaultClient);
    String licenseeNumber = "licenseeNumber_example"; // String | Licensee number with a maximum length of 1000 characters
    String sourceLicenseeNumber = "sourceLicenseeNumber_example"; // String | Licensee number which Licenses to be transferred
    try {
      Netlicensing result = apiInstance.transferLicenses(licenseeNumber, sourceLicenseeNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseeApi#transferLicenses");
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
| **licenseeNumber** | **String**| Licensee number with a maximum length of 1000 characters | |
| **sourceLicenseeNumber** | **String**| Licensee number which Licenses to be transferred | |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="updateLicensee"></a>
# **updateLicensee**
> Netlicensing updateLicensee(licenseeNumber, active, markedForTransfer, name, number)

Update Licensee

Sets the provided properties to a Licensee. Return an updated Licensee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseeApi apiInstance = new LicenseeApi(defaultClient);
    String licenseeNumber = "licenseeNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee.
    Boolean active = true; // Boolean | If set to 'false', the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled
    Boolean markedForTransfer = true; // Boolean | Mark Licensee for transfer.
    String name = "name_example"; // String | 
    String number = "number_example"; // String | New Licensee number (update).
    try {
      Netlicensing result = apiInstance.updateLicensee(licenseeNumber, active, markedForTransfer, name, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseeApi#updateLicensee");
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
| **licenseeNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee. | |
| **active** | **Boolean**| If set to &#39;false&#39;, the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled | [optional] |
| **markedForTransfer** | **Boolean**| Mark Licensee for transfer. | [optional] |
| **name** | **String**|  | [optional] |
| **number** | **String**| New Licensee number (update). | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **402** | Quota exceeded |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="validateLicensee"></a>
# **validateLicensee**
> Netlicensing validateLicensee(licenseeNumber, action, licenseeName, nodeSecret, productModuleNumber, productNumber, sessionId)

Validate Licensee

Validates active Licenses of the Licensee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseeApi apiInstance = new LicenseeApi(defaultClient);
    String licenseeNumber = "licenseeNumber_example"; // String | Licensee number with a maximum length of 1000 characters
    String action = "checkOut"; // String | 'Floating' licensing model: check-out or check-in session action, to allocate or return it from/to the pool of available sessions
    String licenseeName = "licenseeName_example"; // String | Human-readable name for the auto-created Licensee (will be set as custom Licensee property)
    String nodeSecret = "nodeSecret_example"; // String | 'Node-Locked' licensing model: specifies unique secret
    String productModuleNumber = "productModuleNumber_example"; // String | 'Node-Locked' licensing model: product module number
    String productNumber = "productNumber_example"; // String | Product number, must be provided when 'Licensee auto-create' is enabled (see also Product JavaDoc). Identifies the Product to which new Licensee should be added
    String sessionId = "sessionId_example"; // String | 'Floating' licensing model: specifies unique session identifier
    try {
      Netlicensing result = apiInstance.validateLicensee(licenseeNumber, action, licenseeName, nodeSecret, productModuleNumber, productNumber, sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseeApi#validateLicensee");
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
| **licenseeNumber** | **String**| Licensee number with a maximum length of 1000 characters | |
| **action** | **String**| &#39;Floating&#39; licensing model: check-out or check-in session action, to allocate or return it from/to the pool of available sessions | [optional] [enum: checkOut, checkIn] |
| **licenseeName** | **String**| Human-readable name for the auto-created Licensee (will be set as custom Licensee property) | [optional] |
| **nodeSecret** | **String**| &#39;Node-Locked&#39; licensing model: specifies unique secret | [optional] |
| **productModuleNumber** | **String**| &#39;Node-Locked&#39; licensing model: product module number | [optional] |
| **productNumber** | **String**| Product number, must be provided when &#39;Licensee auto-create&#39; is enabled (see also Product JavaDoc). Identifies the Product to which new Licensee should be added | [optional] |
| **sessionId** | **String**| &#39;Floating&#39; licensing model: specifies unique session identifier | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

