# LicenseApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLicense**](LicenseApi.md#createLicense) | **POST** /license | Create License |
| [**deleteLicense**](LicenseApi.md#deleteLicense) | **DELETE** /license/{licenseNumber} | Delete License |
| [**getLicense**](LicenseApi.md#getLicense) | **GET** /license/{licenseNumber} | Get License |
| [**listLicenses**](LicenseApi.md#listLicenses) | **GET** /license | List Licenses |
| [**updateLicense**](LicenseApi.md#updateLicense) | **POST** /license/{licenseNumber} | Update License |


<a id="createLicense"></a>
# **createLicense**
> Netlicensing createLicense(active, licenseTemplateNumber, licenseeNumber, currency, hidden, name, number, parentfeature, price, quantity, startDate, timeVolume, timeVolumePeriod, usedQuantity)

Create License

Creates a new License

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseApi apiInstance = new LicenseApi(defaultClient);
    Boolean active = true; // Boolean | 
    String licenseTemplateNumber = "licenseTemplateNumber_example"; // String | 
    String licenseeNumber = "licenseeNumber_example"; // String | 
    String currency = "currency_example"; // String | Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation
    Boolean hidden = true; // Boolean | If set to 'true', this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly
    String name = "name_example"; // String | Name for the Licensed item. Set from License Template on creation, if not specified explicitly.
    String number = "number_example"; // String | 
    String parentfeature = "parentfeature_example"; // String | Mandatory for 'TIMEVOLUME' License Type and 'RENTAL' licensing model
    Double price = 3.4D; // Double | Price for the License. If >0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation
    String quantity = "quantity_example"; // String | Mandatory for 'Pay-per-Use' License Model.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Mandatory for 'TIMEVOLUME' License Type.
    String timeVolume = "timeVolume_example"; // String | Mandatory for 'TIMEVOLUME' License Type.
    String timeVolumePeriod = "timeVolumePeriod_example"; // String | For 'TIMEVOLUME' License Type.
    String usedQuantity = "usedQuantity_example"; // String | Mandatory for 'Pay-per-Use' License Model.
    try {
      Netlicensing result = apiInstance.createLicense(active, licenseTemplateNumber, licenseeNumber, currency, hidden, name, number, parentfeature, price, quantity, startDate, timeVolume, timeVolumePeriod, usedQuantity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseApi#createLicense");
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
| **active** | **Boolean**|  | |
| **licenseTemplateNumber** | **String**|  | |
| **licenseeNumber** | **String**|  | |
| **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation | [optional] |
| **hidden** | **Boolean**| If set to &#39;true&#39;, this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly | [optional] |
| **name** | **String**| Name for the Licensed item. Set from License Template on creation, if not specified explicitly. | [optional] |
| **number** | **String**|  | [optional] |
| **parentfeature** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type and &#39;RENTAL&#39; licensing model | [optional] |
| **price** | **Double**| Price for the License. If &gt;0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation | [optional] |
| **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] |
| **startDate** | **OffsetDateTime**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] |
| **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] |
| **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] |
| **usedQuantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] |

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

<a id="deleteLicense"></a>
# **deleteLicense**
> Netlicensing deleteLicense(licenseNumber)

Delete License

Delete License by a &#39;licenseNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseApi apiInstance = new LicenseApi(defaultClient);
    String licenseNumber = "licenseNumber_example"; // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    try {
      Netlicensing result = apiInstance.deleteLicense(licenseNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseApi#deleteLicense");
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
| **licenseNumber** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | |

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

<a id="getLicense"></a>
# **getLicense**
> Netlicensing getLicense(licenseNumber)

Get License

Get License by a &#39;licenseNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseApi apiInstance = new LicenseApi(defaultClient);
    String licenseNumber = "licenseNumber_example"; // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    try {
      Netlicensing result = apiInstance.getLicense(licenseNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseApi#getLicense");
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
| **licenseNumber** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | |

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

<a id="listLicenses"></a>
# **listLicenses**
> List&lt;Netlicensing&gt; listLicenses()

List Licenses

Return a list of all Licenses for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseApi apiInstance = new LicenseApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listLicenses();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseApi#listLicenses");
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

<a id="updateLicense"></a>
# **updateLicense**
> Netlicensing updateLicense(licenseNumber, active, currency, hidden, name, number, parentfeature, price, quantity, startDate, timeVolume, timeVolumePeriod, usedQuantity)

Update License

Update License by a &#39;licenseNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseApi apiInstance = new LicenseApi(defaultClient);
    String licenseNumber = "licenseNumber_example"; // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    Boolean active = true; // Boolean | 
    String currency = "currency_example"; // String | Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation
    Boolean hidden = true; // Boolean | If set to 'true', this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly
    String name = "name_example"; // String | Name for the Licensed item. Set from License Template on creation, if not specified explicitly.
    String number = "number_example"; // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    String parentfeature = "parentfeature_example"; // String | 
    Double price = 3.4D; // Double | Price for the License. If > 0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation
    String quantity = "quantity_example"; // String | Mandatory for 'Pay-per-Use' License Model.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | For 'TIMEVOLUME' License type
    String timeVolume = "timeVolume_example"; // String | Mandatory for 'TIMEVOLUME' License Type.
    String timeVolumePeriod = "timeVolumePeriod_example"; // String | For 'TIMEVOLUME' License Type.
    String usedQuantity = "usedQuantity_example"; // String | Mandatory for 'Pay-per-Use' License Model.
    try {
      Netlicensing result = apiInstance.updateLicense(licenseNumber, active, currency, hidden, name, number, parentfeature, price, quantity, startDate, timeVolume, timeVolumePeriod, usedQuantity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseApi#updateLicense");
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
| **licenseNumber** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | |
| **active** | **Boolean**|  | [optional] |
| **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation | [optional] |
| **hidden** | **Boolean**| If set to &#39;true&#39;, this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly | [optional] |
| **name** | **String**| Name for the Licensed item. Set from License Template on creation, if not specified explicitly. | [optional] |
| **number** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | [optional] |
| **parentfeature** | **String**|  | [optional] |
| **price** | **Double**| Price for the License. If &gt; 0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation | [optional] |
| **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] |
| **startDate** | **OffsetDateTime**| For &#39;TIMEVOLUME&#39; License type | [optional] |
| **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] |
| **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] |
| **usedQuantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] |

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

