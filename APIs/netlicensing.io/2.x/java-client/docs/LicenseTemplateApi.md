# LicenseTemplateApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLicenseTemplate**](LicenseTemplateApi.md#createLicenseTemplate) | **POST** /licensetemplate | Create License Template |
| [**deleteLicenseTemplate**](LicenseTemplateApi.md#deleteLicenseTemplate) | **DELETE** /licensetemplate/{licenseTemplateNumber} | Delete License Template |
| [**getLicenseTemplate**](LicenseTemplateApi.md#getLicenseTemplate) | **GET** /licensetemplate/{licenseTemplateNumber} | Get License Template |
| [**listLicenseTemplates**](LicenseTemplateApi.md#listLicenseTemplates) | **GET** /licensetemplate | List License Templates |
| [**updateLicenseTemplate**](LicenseTemplateApi.md#updateLicenseTemplate) | **POST** /licensetemplate/{licenseTemplateNumber} | Update License Template |


<a id="createLicenseTemplate"></a>
# **createLicenseTemplate**
> Netlicensing createLicenseTemplate(active, licenseType, name, productModuleNumber, automatic, currency, hidden, hideLicenses, maxSessions, number, price, quantity, quota, timeVolume, timeVolumePeriod)

Create License Template

Creates a new License Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseTemplateApi apiInstance = new LicenseTemplateApi(defaultClient);
    Boolean active = true; // Boolean | If set to 'false', the License Template is disabled. Licensee can not obtain any new Licenses off this License Template.
    String licenseType = "licenseType_example"; // String | Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY
    String name = "name_example"; // String | License Template name to create License Template object
    String productModuleNumber = "productModuleNumber_example"; // String | Number of Product Module to create License Template object
    Boolean automatic = true; // Boolean | If set to 'true', every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0.
    String currency = "currency_example"; // String | Specifies currency for the License price. Check data types to discover which currencies are supported.
    Boolean hidden = true; // Boolean | If set to 'true', this License Template is not shown in NetLicensing Shop as offered for purchase.
    Boolean hideLicenses = true; // Boolean | If set to 'true', Licenses from this License Template are not visible to the end customer, but participate in validation.
    String maxSessions = "maxSessions_example"; // String | Mandatory for 'FLOATING' License Type.
    String number = "number_example"; // String | Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
    Double price = 3.4D; // Double | Price for the License. If >0, it must always be accompanied by the currency specification.
    String quantity = "quantity_example"; // String | Mandatory for 'Pay-per-Use' and 'Node-Locked' License Model.
    String quota = "quota_example"; // String | Mandatory for 'Quota' License Model.
    String timeVolume = "timeVolume_example"; // String | Mandatory for 'TIMEVOLUME' License Type.
    String timeVolumePeriod = "timeVolumePeriod_example"; // String | For 'TIMEVOLUME' License Type.
    try {
      Netlicensing result = apiInstance.createLicenseTemplate(active, licenseType, name, productModuleNumber, automatic, currency, hidden, hideLicenses, maxSessions, number, price, quantity, quota, timeVolume, timeVolumePeriod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseTemplateApi#createLicenseTemplate");
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
| **active** | **Boolean**| If set to &#39;false&#39;, the License Template is disabled. Licensee can not obtain any new Licenses off this License Template. | |
| **licenseType** | **String**| Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY | |
| **name** | **String**| License Template name to create License Template object | |
| **productModuleNumber** | **String**| Number of Product Module to create License Template object | |
| **automatic** | **Boolean**| If set to &#39;true&#39;, every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0. | [optional] |
| **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. | [optional] |
| **hidden** | **Boolean**| If set to &#39;true&#39;, this License Template is not shown in NetLicensing Shop as offered for purchase. | [optional] |
| **hideLicenses** | **Boolean**| If set to &#39;true&#39;, Licenses from this License Template are not visible to the end customer, but participate in validation. | [optional] |
| **maxSessions** | **String**| Mandatory for &#39;FLOATING&#39; License Type. | [optional] |
| **number** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template. | [optional] |
| **price** | **Double**| Price for the License. If &gt;0, it must always be accompanied by the currency specification. | [optional] |
| **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; and &#39;Node-Locked&#39; License Model. | [optional] |
| **quota** | **String**| Mandatory for &#39;Quota&#39; License Model. | [optional] |
| **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] |
| **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] |

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

<a id="deleteLicenseTemplate"></a>
# **deleteLicenseTemplate**
> Netlicensing deleteLicenseTemplate(licenseTemplateNumber, forceCascade)

Delete License Template

Delete a License Template by &#39;number&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseTemplateApi apiInstance = new LicenseTemplateApi(defaultClient);
    String licenseTemplateNumber = "licenseTemplateNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the License Template.
    Boolean forceCascade = true; // Boolean | Force object deletion and all descendants.
    try {
      Netlicensing result = apiInstance.deleteLicenseTemplate(licenseTemplateNumber, forceCascade);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseTemplateApi#deleteLicenseTemplate");
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
| **licenseTemplateNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. | |
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

<a id="getLicenseTemplate"></a>
# **getLicenseTemplate**
> Netlicensing getLicenseTemplate(licenseTemplateNumber)

Get License Template

Return a License Template by &#39;licenseTemplateNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseTemplateApi apiInstance = new LicenseTemplateApi(defaultClient);
    String licenseTemplateNumber = "licenseTemplateNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
    try {
      Netlicensing result = apiInstance.getLicenseTemplate(licenseTemplateNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseTemplateApi#getLicenseTemplate");
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
| **licenseTemplateNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template. | |

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

<a id="listLicenseTemplates"></a>
# **listLicenseTemplates**
> List&lt;Netlicensing&gt; listLicenseTemplates()

List License Templates

Return a list of all License Templates for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseTemplateApi apiInstance = new LicenseTemplateApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listLicenseTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseTemplateApi#listLicenseTemplates");
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

<a id="updateLicenseTemplate"></a>
# **updateLicenseTemplate**
> Netlicensing updateLicenseTemplate(licenseTemplateNumber, active, automatic, currency, hidden, hideLicenses, licenseType, maxSessions, name, number, price, quantity, quota, timeVolume, timeVolumePeriod)

Update License Template

Sets the provided properties to a License Template. Return an updated License Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    LicenseTemplateApi apiInstance = new LicenseTemplateApi(defaultClient);
    String licenseTemplateNumber = "licenseTemplateNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
    Boolean active = true; // Boolean | If set to 'false', the License Template is disabled. Licensee can not obtain any new Licenses off this License Template.
    Boolean automatic = true; // Boolean | If set to 'true', every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0.
    String currency = "currency_example"; // String | Specifies currency for the License price. Check data types to discover which currencies are supported.
    Boolean hidden = true; // Boolean | If set to 'true', this License Template is not shown in NetLicensing Shop as offered for purchase.
    Boolean hideLicenses = true; // Boolean | If set to 'true', Licenses from this License Template are not visible to the end customer, but participate in validation.
    String licenseType = "licenseType_example"; // String | Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY
    String maxSessions = "maxSessions_example"; // String | Mandatory for 'FLOATING' License Type.
    String name = "name_example"; // String | Name for the Licensed item
    String number = "number_example"; // String | New License Template number (update).
    Double price = 3.4D; // Double | Price for the License. If >0, it must always be accompanied by the currency specification.
    String quantity = "quantity_example"; // String | Mandatory for 'Pay-per-Use' and 'Node-Locked' License Model.
    String quota = "quota_example"; // String | Mandatory for 'Quota' License Model.
    String timeVolume = "timeVolume_example"; // String | Mandatory for 'TIMEVOLUME' License Type.
    String timeVolumePeriod = "timeVolumePeriod_example"; // String | For 'TIMEVOLUME' License Type.
    try {
      Netlicensing result = apiInstance.updateLicenseTemplate(licenseTemplateNumber, active, automatic, currency, hidden, hideLicenses, licenseType, maxSessions, name, number, price, quantity, quota, timeVolume, timeVolumePeriod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseTemplateApi#updateLicenseTemplate");
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
| **licenseTemplateNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template. | |
| **active** | **Boolean**| If set to &#39;false&#39;, the License Template is disabled. Licensee can not obtain any new Licenses off this License Template. | [optional] |
| **automatic** | **Boolean**| If set to &#39;true&#39;, every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0. | [optional] |
| **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. | [optional] |
| **hidden** | **Boolean**| If set to &#39;true&#39;, this License Template is not shown in NetLicensing Shop as offered for purchase. | [optional] |
| **hideLicenses** | **Boolean**| If set to &#39;true&#39;, Licenses from this License Template are not visible to the end customer, but participate in validation. | [optional] |
| **licenseType** | **String**| Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY | [optional] |
| **maxSessions** | **String**| Mandatory for &#39;FLOATING&#39; License Type. | [optional] |
| **name** | **String**| Name for the Licensed item | [optional] |
| **number** | **String**| New License Template number (update). | [optional] |
| **price** | **Double**| Price for the License. If &gt;0, it must always be accompanied by the currency specification. | [optional] |
| **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; and &#39;Node-Locked&#39; License Model. | [optional] |
| **quota** | **String**| Mandatory for &#39;Quota&#39; License Model. | [optional] |
| **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] |
| **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] |

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

