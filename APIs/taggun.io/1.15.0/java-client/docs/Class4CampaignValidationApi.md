# Class4CampaignValidationApi

All URIs are relative to *https://api.taggun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteApiValidationV1CampaignSettingsDeleteCampaignid**](Class4CampaignValidationApi.md#deleteApiValidationV1CampaignSettingsDeleteCampaignid) | **DELETE** /api/validation/v1/campaign/settings/delete/{campaignId} | delete campaign settings for a client |
| [**getApiValidationV1CampaignSettingsCampaignid**](Class4CampaignValidationApi.md#getApiValidationV1CampaignSettingsCampaignid) | **GET** /api/validation/v1/campaign/settings/{campaignId} | get campaign settings for a client |
| [**getApiValidationV1CampaignSettingsList**](Class4CampaignValidationApi.md#getApiValidationV1CampaignSettingsList) | **GET** /api/validation/v1/campaign/settings/list | list all campaign setting IDs for a client |
| [**postApiValidationV1CampaignFile**](Class4CampaignValidationApi.md#postApiValidationV1CampaignFile) | **POST** /api/validation/v1/campaign/file | validate and match a receipt against a campaign validation settings by uploading an image file |
| [**postApiValidationV1CampaignProductvalidationFile**](Class4CampaignValidationApi.md#postApiValidationV1CampaignProductvalidationFile) | **POST** /api/validation/v1/campaign/product-validation/file | validate if user-submitted info like serial number are detected an image file |
| [**postApiValidationV1CampaignSettingsCreateCampaignid**](Class4CampaignValidationApi.md#postApiValidationV1CampaignSettingsCreateCampaignid) | **POST** /api/validation/v1/campaign/settings/create/{campaignId} | create campaign settings for a client |
| [**putApiValidationV1CampaignSettingsUpdateCampaignid**](Class4CampaignValidationApi.md#putApiValidationV1CampaignSettingsUpdateCampaignid) | **PUT** /api/validation/v1/campaign/settings/update/{campaignId} | update campaign settings for a client |


<a id="deleteApiValidationV1CampaignSettingsDeleteCampaignid"></a>
# **deleteApiValidationV1CampaignSettingsDeleteCampaignid**
> deleteApiValidationV1CampaignSettingsDeleteCampaignid(apikey, campaignId)

delete campaign settings for a client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4CampaignValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4CampaignValidationApi apiInstance = new Class4CampaignValidationApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    String campaignId = "campaignId_example"; // String | Remove campaign settings with a campaign ID
    try {
      apiInstance.deleteApiValidationV1CampaignSettingsDeleteCampaignid(apikey, campaignId);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4CampaignValidationApi#deleteApiValidationV1CampaignSettingsDeleteCampaignid");
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
| **apikey** | **String**| API authentication key. | |
| **campaignId** | **String**| Remove campaign settings with a campaign ID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |

<a id="getApiValidationV1CampaignSettingsCampaignid"></a>
# **getApiValidationV1CampaignSettingsCampaignid**
> getApiValidationV1CampaignSettingsCampaignid(apikey, campaignId)

get campaign settings for a client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4CampaignValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4CampaignValidationApi apiInstance = new Class4CampaignValidationApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    String campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
    try {
      apiInstance.getApiValidationV1CampaignSettingsCampaignid(apikey, campaignId);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4CampaignValidationApi#getApiValidationV1CampaignSettingsCampaignid");
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
| **apikey** | **String**| API authentication key. | |
| **campaignId** | **String**| The ID of the campaign to validate the receipt | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |

<a id="getApiValidationV1CampaignSettingsList"></a>
# **getApiValidationV1CampaignSettingsList**
> getApiValidationV1CampaignSettingsList(apikey)

list all campaign setting IDs for a client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4CampaignValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4CampaignValidationApi apiInstance = new Class4CampaignValidationApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    try {
      apiInstance.getApiValidationV1CampaignSettingsList(apikey);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4CampaignValidationApi#getApiValidationV1CampaignSettingsList");
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
| **apikey** | **String**| API authentication key. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |

<a id="postApiValidationV1CampaignFile"></a>
# **postApiValidationV1CampaignFile**
> String postApiValidationV1CampaignFile(apikey, campaignId, _file, incognito, ipAddress, near, referenceId)

validate and match a receipt against a campaign validation settings by uploading an image file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4CampaignValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4CampaignValidationApi apiInstance = new Class4CampaignValidationApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    String campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
    File _file = new File("/path/to/file"); // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    Boolean incognito = false; // Boolean | Set true to avoid saving the receipt in storage
    String ipAddress = "ipAddress_example"; // String | IP Address of the end user
    String near = "near_example"; // String | A geo location to search for merchant. Typically in the format of city, state, country.
    String referenceId = "referenceId_example"; // String | Tag a request with a unique reference ID for feedback and training purposes
    try {
      String result = apiInstance.postApiValidationV1CampaignFile(apikey, campaignId, _file, incognito, ipAddress, near, referenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4CampaignValidationApi#postApiValidationV1CampaignFile");
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
| **apikey** | **String**| API authentication key. | |
| **campaignId** | **String**| The ID of the campaign to validate the receipt | |
| **_file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] |
| **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false] |
| **ipAddress** | **String**| IP Address of the end user | [optional] |
| **near** | **String**| A geo location to search for merchant. Typically in the format of city, state, country. | [optional] |
| **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiValidationV1CampaignProductvalidationFile"></a>
# **postApiValidationV1CampaignProductvalidationFile**
> String postApiValidationV1CampaignProductvalidationFile(apikey, productVerificationNumber, _file, incognito, subAccountId, referenceId)

validate if user-submitted info like serial number are detected an image file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4CampaignValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4CampaignValidationApi apiInstance = new Class4CampaignValidationApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    String productVerificationNumber = "productVerificationNumber_example"; // String | The number of the product to validate the receipt
    File _file = new File("/path/to/file"); // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    Boolean incognito = false; // Boolean | Set true to avoid saving the receipt in storage
    String subAccountId = "subAccountId_example"; // String | Tag a request with sub-account ID for billing purposes
    String referenceId = "referenceId_example"; // String | Tag a request with a unique reference ID for feedback and training purposes
    try {
      String result = apiInstance.postApiValidationV1CampaignProductvalidationFile(apikey, productVerificationNumber, _file, incognito, subAccountId, referenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4CampaignValidationApi#postApiValidationV1CampaignProductvalidationFile");
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
| **apikey** | **String**| API authentication key. | |
| **productVerificationNumber** | **String**| The number of the product to validate the receipt | |
| **_file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] |
| **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false] |
| **subAccountId** | **String**| Tag a request with sub-account ID for billing purposes | [optional] |
| **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiValidationV1CampaignSettingsCreateCampaignid"></a>
# **postApiValidationV1CampaignSettingsCreateCampaignid**
> postApiValidationV1CampaignSettingsCreateCampaignid(apikey, campaignId, body)

create campaign settings for a client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4CampaignValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4CampaignValidationApi apiInstance = new Class4CampaignValidationApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    String campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
    Model9 body = new Model9(); // Model9 | 
    try {
      apiInstance.postApiValidationV1CampaignSettingsCreateCampaignid(apikey, campaignId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4CampaignValidationApi#postApiValidationV1CampaignSettingsCreateCampaignid");
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
| **apikey** | **String**| API authentication key. | |
| **campaignId** | **String**| The ID of the campaign to validate the receipt | |
| **body** | [**Model9**](Model9.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |

<a id="putApiValidationV1CampaignSettingsUpdateCampaignid"></a>
# **putApiValidationV1CampaignSettingsUpdateCampaignid**
> putApiValidationV1CampaignSettingsUpdateCampaignid(apikey, campaignId, body)

update campaign settings for a client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4CampaignValidationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4CampaignValidationApi apiInstance = new Class4CampaignValidationApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    String campaignId = "campaignId_example"; // String | The ID of the campaign to validate the receipt
    Model9 body = new Model9(); // Model9 | 
    try {
      apiInstance.putApiValidationV1CampaignSettingsUpdateCampaignid(apikey, campaignId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4CampaignValidationApi#putApiValidationV1CampaignSettingsUpdateCampaignid");
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
| **apikey** | **String**| API authentication key. | |
| **campaignId** | **String**| The ID of the campaign to validate the receipt | |
| **body** | [**Model9**](Model9.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request |  -  |

