# LicenseActivationsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**licenseActivationsPost**](LicenseActivationsApi.md#licenseActivationsPost) | **POST** /api/v2/LicenseActivations | Create a license activation. |
| [**licenseActivationsPostRegisterEDTLite**](LicenseActivationsApi.md#licenseActivationsPostRegisterEDTLite) | **POST** /api/v2/LicenseActivations/RegisterEDTLite | Register an EDT Lite with the Server |
| [**licenseActivationsPut**](LicenseActivationsApi.md#licenseActivationsPut) | **PUT** /api/v2/LicenseActivations/{ID} | Update a license activiation. |
| [**licenseActivationsPutConfirm**](LicenseActivationsApi.md#licenseActivationsPutConfirm) | **PUT** /api/v2/LicenseActivations/{ID}/Confirm | Confirm that the client has applied the updated license. |


<a id="licenseActivationsPost"></a>
# **licenseActivationsPost**
> DealerDBModelsLicenseActivation licenseActivationsPost(dealerDBModelsLicenseActivationCreate)

Create a license activation.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LicenseActivationsApi apiInstance = new LicenseActivationsApi(defaultClient);
    DealerDBModelsLicenseActivationCreate dealerDBModelsLicenseActivationCreate = new DealerDBModelsLicenseActivationCreate(); // DealerDBModelsLicenseActivationCreate | The data required for creating the license.
    try {
      DealerDBModelsLicenseActivation result = apiInstance.licenseActivationsPost(dealerDBModelsLicenseActivationCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseActivationsApi#licenseActivationsPost");
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
| **dealerDBModelsLicenseActivationCreate** | [**DealerDBModelsLicenseActivationCreate**](DealerDBModelsLicenseActivationCreate.md)| The data required for creating the license. | |

### Return type

[**DealerDBModelsLicenseActivation**](DealerDBModelsLicenseActivation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="licenseActivationsPostRegisterEDTLite"></a>
# **licenseActivationsPostRegisterEDTLite**
> Boolean licenseActivationsPostRegisterEDTLite(dealerDBModelsEDTLiteRegistration)

Register an EDT Lite with the Server

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LicenseActivationsApi apiInstance = new LicenseActivationsApi(defaultClient);
    DealerDBModelsEDTLiteRegistration dealerDBModelsEDTLiteRegistration = new DealerDBModelsEDTLiteRegistration(); // DealerDBModelsEDTLiteRegistration | The information required for registration.
    try {
      Boolean result = apiInstance.licenseActivationsPostRegisterEDTLite(dealerDBModelsEDTLiteRegistration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseActivationsApi#licenseActivationsPostRegisterEDTLite");
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
| **dealerDBModelsEDTLiteRegistration** | [**DealerDBModelsEDTLiteRegistration**](DealerDBModelsEDTLiteRegistration.md)| The information required for registration. | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="licenseActivationsPut"></a>
# **licenseActivationsPut**
> DealerDBModelsLicenseActivation licenseActivationsPut(ID, dealerDBModelsLicenseActivationUpdate)

Update a license activiation.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LicenseActivationsApi apiInstance = new LicenseActivationsApi(defaultClient);
    String ID = "ID_example"; // String | The ID of the license.
    DealerDBModelsLicenseActivationUpdate dealerDBModelsLicenseActivationUpdate = new DealerDBModelsLicenseActivationUpdate(); // DealerDBModelsLicenseActivationUpdate | The data required for updating the license.
    try {
      DealerDBModelsLicenseActivation result = apiInstance.licenseActivationsPut(ID, dealerDBModelsLicenseActivationUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseActivationsApi#licenseActivationsPut");
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
| **ID** | **String**| The ID of the license. | |
| **dealerDBModelsLicenseActivationUpdate** | [**DealerDBModelsLicenseActivationUpdate**](DealerDBModelsLicenseActivationUpdate.md)| The data required for updating the license. | |

### Return type

[**DealerDBModelsLicenseActivation**](DealerDBModelsLicenseActivation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="licenseActivationsPutConfirm"></a>
# **licenseActivationsPutConfirm**
> licenseActivationsPutConfirm(ID, dealerDBModelsLicenseActivationConfirm)

Confirm that the client has applied the updated license.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseActivationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LicenseActivationsApi apiInstance = new LicenseActivationsApi(defaultClient);
    String ID = "ID_example"; // String | The ID of the license
    DealerDBModelsLicenseActivationConfirm dealerDBModelsLicenseActivationConfirm = new DealerDBModelsLicenseActivationConfirm(); // DealerDBModelsLicenseActivationConfirm | The license data.
    try {
      apiInstance.licenseActivationsPutConfirm(ID, dealerDBModelsLicenseActivationConfirm);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseActivationsApi#licenseActivationsPutConfirm");
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
| **ID** | **String**| The ID of the license | |
| **dealerDBModelsLicenseActivationConfirm** | [**DealerDBModelsLicenseActivationConfirm**](DealerDBModelsLicenseActivationConfirm.md)| The license data. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

