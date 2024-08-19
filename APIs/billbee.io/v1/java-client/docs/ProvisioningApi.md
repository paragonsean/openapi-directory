# ProvisioningApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**automaticProvisioningCreateAccount**](ProvisioningApi.md#automaticProvisioningCreateAccount) | **POST** /api/v1/automaticprovision/createaccount | Creates a new Billbee user account with the data passed |
| [**automaticProvisioningTermsInfo**](ProvisioningApi.md#automaticProvisioningTermsInfo) | **GET** /api/v1/automaticprovision/termsinfo | Returns infos about Billbee terms and conditions |


<a id="automaticProvisioningCreateAccount"></a>
# **automaticProvisioningCreateAccount**
> Object automaticProvisioningCreateAccount(rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer)

Creates a new Billbee user account with the data passed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer = new RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer(); // RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer | 
    try {
      Object result = apiInstance.automaticProvisioningCreateAccount(rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#automaticProvisioningCreateAccount");
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
| **rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer** | [**RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer**](RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="automaticProvisioningTermsInfo"></a>
# **automaticProvisioningTermsInfo**
> Object automaticProvisioningTermsInfo()

Returns infos about Billbee terms and conditions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvisioningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ProvisioningApi apiInstance = new ProvisioningApi(defaultClient);
    try {
      Object result = apiInstance.automaticProvisioningTermsInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvisioningApi#automaticProvisioningTermsInfo");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

