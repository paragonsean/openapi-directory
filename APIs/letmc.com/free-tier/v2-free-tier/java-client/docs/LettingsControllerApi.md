# LettingsControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lettingsControllerGetAdvertised**](LettingsControllerApi.md#lettingsControllerGetAdvertised) | **GET** /v2/tier1/{shortName}/lettings/advertised | Search all properties available for rent given a range of search criteria. |
| [**lettingsControllerGetAdvertisedBetweenDates**](LettingsControllerApi.md#lettingsControllerGetAdvertisedBetweenDates) | **GET** /v2/tier1/{shortName}/lettings/advertisedbetweendates | Search all properties available for rent given a range of search criteria and dates. |
| [**lettingsControllerGetTenancyBrochure**](LettingsControllerApi.md#lettingsControllerGetTenancyBrochure) | **GET** /v2/tier1/{shortName}/lettings/tenancies/{tenancyID}/brochure | Downloads the brochure relating to the latest advertised rental of a property |
| [**v2Tier1ShortNameLettingsTenanciesGet**](LettingsControllerApi.md#v2Tier1ShortNameLettingsTenanciesGet) | **GET** /v2/tier1/{shortName}/lettings/tenancies | A collection of all the company&#39;s tenancies |
| [**v2Tier1ShortNameLettingsTenanciesTenancyIDGet**](LettingsControllerApi.md#v2Tier1ShortNameLettingsTenanciesTenancyIDGet) | **GET** /v2/tier1/{shortName}/lettings/tenancies/{tenancyID} | Get a specific tenancy given its unique Object ID (OID) |


<a id="lettingsControllerGetAdvertised"></a>
# **lettingsControllerGetAdvertised**
> TenancyModelResults lettingsControllerGetAdvertised(shortName, branchID, offset, count, areaID, rentMinimum, rentMaximum, maximumTenants, wantSharedProperties, wantStudentProperties)

Search all properties available for rent given a range of search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LettingsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LettingsControllerApi apiInstance = new LettingsControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    String areaID = "areaID_example"; // String | The unique ID of the Area
    Double rentMinimum = 3.4D; // Double | The minimum advertised rent to search for
    Double rentMaximum = 3.4D; // Double | The maximum advertised rent to search for
    Integer maximumTenants = 56; // Integer | The maximum number of tenants a property can accommodate
    Boolean wantSharedProperties = true; // Boolean | Search for shared properties?
    Boolean wantStudentProperties = true; // Boolean | Search for student properties?
    try {
      TenancyModelResults result = apiInstance.lettingsControllerGetAdvertised(shortName, branchID, offset, count, areaID, rentMinimum, rentMaximum, maximumTenants, wantSharedProperties, wantStudentProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LettingsControllerApi#lettingsControllerGetAdvertised");
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
| **shortName** | **String**| The unique client short-name | |
| **branchID** | **String**| The unique ID of the Branch | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |
| **areaID** | **String**| The unique ID of the Area | [optional] |
| **rentMinimum** | **Double**| The minimum advertised rent to search for | [optional] |
| **rentMaximum** | **Double**| The maximum advertised rent to search for | [optional] |
| **maximumTenants** | **Integer**| The maximum number of tenants a property can accommodate | [optional] |
| **wantSharedProperties** | **Boolean**| Search for shared properties? | [optional] |
| **wantStudentProperties** | **Boolean**| Search for student properties? | [optional] |

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lettingsControllerGetAdvertisedBetweenDates"></a>
# **lettingsControllerGetAdvertisedBetweenDates**
> TenancyModelResults lettingsControllerGetAdvertisedBetweenDates(shortName, branchID, offset, count, rangeStartDate, rangeEndDate, areaID, rentMinimum, rentMaximum, maximumTenants, wantSharedProperties, wantStudentProperties)

Search all properties available for rent given a range of search criteria and dates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LettingsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LettingsControllerApi apiInstance = new LettingsControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    OffsetDateTime rangeStartDate = OffsetDateTime.now(); // OffsetDateTime | The date to search from
    OffsetDateTime rangeEndDate = OffsetDateTime.now(); // OffsetDateTime | The date to search to
    String areaID = "areaID_example"; // String | The unique ID of the Area
    Double rentMinimum = 3.4D; // Double | The minimum advertised rent to search for
    Double rentMaximum = 3.4D; // Double | The maximum advertised rent to search for
    Integer maximumTenants = 56; // Integer | The maximum number of tenants a property can accommodate
    Boolean wantSharedProperties = true; // Boolean | Search for shared properties?
    Boolean wantStudentProperties = true; // Boolean | Search for student properties?
    try {
      TenancyModelResults result = apiInstance.lettingsControllerGetAdvertisedBetweenDates(shortName, branchID, offset, count, rangeStartDate, rangeEndDate, areaID, rentMinimum, rentMaximum, maximumTenants, wantSharedProperties, wantStudentProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LettingsControllerApi#lettingsControllerGetAdvertisedBetweenDates");
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
| **shortName** | **String**| The unique client short-name | |
| **branchID** | **String**| The unique ID of the Branch | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |
| **rangeStartDate** | **OffsetDateTime**| The date to search from | |
| **rangeEndDate** | **OffsetDateTime**| The date to search to | |
| **areaID** | **String**| The unique ID of the Area | [optional] |
| **rentMinimum** | **Double**| The minimum advertised rent to search for | [optional] |
| **rentMaximum** | **Double**| The maximum advertised rent to search for | [optional] |
| **maximumTenants** | **Integer**| The maximum number of tenants a property can accommodate | [optional] |
| **wantSharedProperties** | **Boolean**| Search for shared properties? | [optional] |
| **wantStudentProperties** | **Boolean**| Search for student properties? | [optional] |

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lettingsControllerGetTenancyBrochure"></a>
# **lettingsControllerGetTenancyBrochure**
> Object lettingsControllerGetTenancyBrochure(shortName, tenancyID)

Downloads the brochure relating to the latest advertised rental of a property

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LettingsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LettingsControllerApi apiInstance = new LettingsControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String tenancyID = "tenancyID_example"; // String | The unique ID of the tenancy
    try {
      Object result = apiInstance.lettingsControllerGetTenancyBrochure(shortName, tenancyID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LettingsControllerApi#lettingsControllerGetTenancyBrochure");
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
| **shortName** | **String**| The unique client short-name | |
| **tenancyID** | **String**| The unique ID of the tenancy | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameLettingsTenanciesGet"></a>
# **v2Tier1ShortNameLettingsTenanciesGet**
> TenancyModelResults v2Tier1ShortNameLettingsTenanciesGet(shortName, offset, count)

A collection of all the company&#39;s tenancies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LettingsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LettingsControllerApi apiInstance = new LettingsControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      TenancyModelResults result = apiInstance.v2Tier1ShortNameLettingsTenanciesGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LettingsControllerApi#v2Tier1ShortNameLettingsTenanciesGet");
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
| **shortName** | **String**| The unique client short-name | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameLettingsTenanciesTenancyIDGet"></a>
# **v2Tier1ShortNameLettingsTenanciesTenancyIDGet**
> TenancyModel v2Tier1ShortNameLettingsTenanciesTenancyIDGet(shortName, tenancyID)

Get a specific tenancy given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LettingsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LettingsControllerApi apiInstance = new LettingsControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String tenancyID = "tenancyID_example"; // String | The unique ID of the Tenancy
    try {
      TenancyModel result = apiInstance.v2Tier1ShortNameLettingsTenanciesTenancyIDGet(shortName, tenancyID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LettingsControllerApi#v2Tier1ShortNameLettingsTenanciesTenancyIDGet");
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
| **shortName** | **String**| The unique client short-name | |
| **tenancyID** | **String**| The unique ID of the Tenancy | |

### Return type

[**TenancyModel**](TenancyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

