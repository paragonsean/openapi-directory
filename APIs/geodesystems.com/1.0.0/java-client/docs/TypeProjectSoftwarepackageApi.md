# TypeProjectSoftwarepackageApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchProjectSoftwarepackage**](TypeProjectSoftwarepackageApi.md#searchProjectSoftwarepackage) | **GET** /repository/search/type/project_softwarepackage | Search API for &#39;Software Tool&#39; entry type |


<a id="searchProjectSoftwarepackage"></a>
# **searchProjectSoftwarepackage**
> searchProjectSoftwarepackage(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchProjectSoftwarepackageSoftwareUse, searchProjectSoftwarepackageSoftwareType, searchProjectSoftwarepackageDomain, searchProjectSoftwarepackagePlatform, searchProjectSoftwarepackageLicense, searchProjectSoftwarepackageStatus, searchProjectSoftwarepackageCapabilities)

Search API for &#39;Software Tool&#39; entry type

API to search for entries of type Software Tool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeProjectSoftwarepackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeProjectSoftwarepackageApi apiInstance = new TypeProjectSoftwarepackageApi(defaultClient);
    String text = "text_example"; // String | Search text
    String name = "name_example"; // String | Search name
    String description = "description_example"; // String | Search description
    OffsetDateTime fromdate = OffsetDateTime.now(); // OffsetDateTime | From date
    OffsetDateTime todate = OffsetDateTime.now(); // OffsetDateTime | To date
    OffsetDateTime createdateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive create date from
    OffsetDateTime createdateTo = OffsetDateTime.now(); // OffsetDateTime | Archive create date to
    OffsetDateTime changedateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive change date from
    OffsetDateTime changedateTo = OffsetDateTime.now(); // OffsetDateTime | Archive change date to
    String group = "group_example"; // String | Parent entry
    String filesuffix = "filesuffix_example"; // String | File suffix
    Float maxlatitude = 3.4F; // Float | Northern bounds of search
    Float minlongitude = 3.4F; // Float | Western bounds of search
    Float minlatitude = 3.4F; // Float | Southern bounds of search
    Float maxlongitude = 3.4F; // Float | Eastern bounds of search
    Integer max = 56; // Integer | Max number of results
    Integer skip = 56; // Integer | Number to skip
    String searchProjectSoftwarepackageSoftwareUse = "searchProjectSoftwarepackageSoftwareUse_example"; // String | Software Use
    String searchProjectSoftwarepackageSoftwareType = "searchProjectSoftwarepackageSoftwareType_example"; // String | Software Type
    String searchProjectSoftwarepackageDomain = "searchProjectSoftwarepackageDomain_example"; // String | Science Domain
    String searchProjectSoftwarepackagePlatform = "searchProjectSoftwarepackagePlatform_example"; // String | Platform
    String searchProjectSoftwarepackageLicense = "searchProjectSoftwarepackageLicense_example"; // String | License
    String searchProjectSoftwarepackageStatus = "searchProjectSoftwarepackageStatus_example"; // String | Development Status
    String searchProjectSoftwarepackageCapabilities = "searchProjectSoftwarepackageCapabilities_example"; // String | Capabilities
    try {
      apiInstance.searchProjectSoftwarepackage(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchProjectSoftwarepackageSoftwareUse, searchProjectSoftwarepackageSoftwareType, searchProjectSoftwarepackageDomain, searchProjectSoftwarepackagePlatform, searchProjectSoftwarepackageLicense, searchProjectSoftwarepackageStatus, searchProjectSoftwarepackageCapabilities);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeProjectSoftwarepackageApi#searchProjectSoftwarepackage");
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
| **text** | **String**| Search text | [optional] |
| **name** | **String**| Search name | [optional] |
| **description** | **String**| Search description | [optional] |
| **fromdate** | **OffsetDateTime**| From date | [optional] |
| **todate** | **OffsetDateTime**| To date | [optional] |
| **createdateFrom** | **OffsetDateTime**| Archive create date from | [optional] |
| **createdateTo** | **OffsetDateTime**| Archive create date to | [optional] |
| **changedateFrom** | **OffsetDateTime**| Archive change date from | [optional] |
| **changedateTo** | **OffsetDateTime**| Archive change date to | [optional] |
| **group** | **String**| Parent entry | [optional] |
| **filesuffix** | **String**| File suffix | [optional] |
| **maxlatitude** | **Float**| Northern bounds of search | [optional] |
| **minlongitude** | **Float**| Western bounds of search | [optional] |
| **minlatitude** | **Float**| Southern bounds of search | [optional] |
| **maxlongitude** | **Float**| Eastern bounds of search | [optional] |
| **max** | **Integer**| Max number of results | [optional] |
| **skip** | **Integer**| Number to skip | [optional] |
| **searchProjectSoftwarepackageSoftwareUse** | **String**| Software Use | [optional] |
| **searchProjectSoftwarepackageSoftwareType** | **String**| Software Type | [optional] |
| **searchProjectSoftwarepackageDomain** | **String**| Science Domain | [optional] |
| **searchProjectSoftwarepackagePlatform** | **String**| Platform | [optional] |
| **searchProjectSoftwarepackageLicense** | **String**| License | [optional] |
| **searchProjectSoftwarepackageStatus** | **String**| Development Status | [optional] |
| **searchProjectSoftwarepackageCapabilities** | **String**| Capabilities | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

