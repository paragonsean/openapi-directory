# TypeBoulderConsultingServicesApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchBoulderConsultingServices**](TypeBoulderConsultingServicesApi.md#searchBoulderConsultingServices) | **GET** /repository/search/type/boulder_consulting_services | Search API for &#39;Boulder Consulting Services Database&#39; entry type |


<a id="searchBoulderConsultingServices"></a>
# **searchBoulderConsultingServices**
> searchBoulderConsultingServices(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBoulderConsultingServicesFund, searchDbBoulderConsultingServicesDepartment, searchDbBoulderConsultingServicesOrganization, searchDbBoulderConsultingServicesObject, searchDbBoulderConsultingServicesProject, searchDbBoulderConsultingServicesAccountDescription, searchDbBoulderConsultingServicesDate, searchDbBoulderConsultingServicesAmount, searchDbBoulderConsultingServicesPurchaseOrder, searchDbBoulderConsultingServicesVendorName, searchDbBoulderConsultingServicesComment)

Search API for &#39;Boulder Consulting Services Database&#39; entry type

API to search for entries of type Boulder Consulting Services Database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeBoulderConsultingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeBoulderConsultingServicesApi apiInstance = new TypeBoulderConsultingServicesApi(defaultClient);
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
    String searchDbBoulderConsultingServicesFund = "searchDbBoulderConsultingServicesFund_example"; // String | Fund
    String searchDbBoulderConsultingServicesDepartment = "searchDbBoulderConsultingServicesDepartment_example"; // String | Department
    String searchDbBoulderConsultingServicesOrganization = "searchDbBoulderConsultingServicesOrganization_example"; // String | Organization
    String searchDbBoulderConsultingServicesObject = "searchDbBoulderConsultingServicesObject_example"; // String | Object
    String searchDbBoulderConsultingServicesProject = "searchDbBoulderConsultingServicesProject_example"; // String | Project
    String searchDbBoulderConsultingServicesAccountDescription = "searchDbBoulderConsultingServicesAccountDescription_example"; // String | Account Description
    String searchDbBoulderConsultingServicesDate = "searchDbBoulderConsultingServicesDate_example"; // String | Date
    Double searchDbBoulderConsultingServicesAmount = 3.4D; // Double | Amount
    String searchDbBoulderConsultingServicesPurchaseOrder = "searchDbBoulderConsultingServicesPurchaseOrder_example"; // String | Purchase Order
    String searchDbBoulderConsultingServicesVendorName = "searchDbBoulderConsultingServicesVendorName_example"; // String | Vendor Name
    String searchDbBoulderConsultingServicesComment = "searchDbBoulderConsultingServicesComment_example"; // String | Comment
    try {
      apiInstance.searchBoulderConsultingServices(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBoulderConsultingServicesFund, searchDbBoulderConsultingServicesDepartment, searchDbBoulderConsultingServicesOrganization, searchDbBoulderConsultingServicesObject, searchDbBoulderConsultingServicesProject, searchDbBoulderConsultingServicesAccountDescription, searchDbBoulderConsultingServicesDate, searchDbBoulderConsultingServicesAmount, searchDbBoulderConsultingServicesPurchaseOrder, searchDbBoulderConsultingServicesVendorName, searchDbBoulderConsultingServicesComment);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeBoulderConsultingServicesApi#searchBoulderConsultingServices");
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
| **searchDbBoulderConsultingServicesFund** | **String**| Fund | [optional] |
| **searchDbBoulderConsultingServicesDepartment** | **String**| Department | [optional] |
| **searchDbBoulderConsultingServicesOrganization** | **String**| Organization | [optional] |
| **searchDbBoulderConsultingServicesObject** | **String**| Object | [optional] |
| **searchDbBoulderConsultingServicesProject** | **String**| Project | [optional] |
| **searchDbBoulderConsultingServicesAccountDescription** | **String**| Account Description | [optional] |
| **searchDbBoulderConsultingServicesDate** | **String**| Date | [optional] |
| **searchDbBoulderConsultingServicesAmount** | **Double**| Amount | [optional] |
| **searchDbBoulderConsultingServicesPurchaseOrder** | **String**| Purchase Order | [optional] |
| **searchDbBoulderConsultingServicesVendorName** | **String**| Vendor Name | [optional] |
| **searchDbBoulderConsultingServicesComment** | **String**| Comment | [optional] |

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

