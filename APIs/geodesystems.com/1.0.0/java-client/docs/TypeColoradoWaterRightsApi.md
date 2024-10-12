# TypeColoradoWaterRightsApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchColoradoWaterRights**](TypeColoradoWaterRightsApi.md#searchColoradoWaterRights) | **GET** /repository/search/type/colorado_water_rights | Search API for &#39;Colorado Water Rights&#39; entry type |


<a id="searchColoradoWaterRights"></a>
# **searchColoradoWaterRights**
> searchColoradoWaterRights(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbColoradoWaterRightsStructureName, searchDbColoradoWaterRightsStructureType, searchDbColoradoWaterRightsWaterSource, searchDbColoradoWaterRightsCounty, searchDbColoradoWaterRightsAdjudicationDate, searchDbColoradoWaterRightsAppropriationDate, searchDbColoradoWaterRightsPriorityNo, searchDbColoradoWaterRightsDecreedUses, searchDbColoradoWaterRightsNetAbsolute, searchDbColoradoWaterRightsNetConditional, searchDbColoradoWaterRightsNetApexAbsolute, searchDbColoradoWaterRightsNetApexConditional, searchDbColoradoWaterRightsDecreedUnits, searchDbColoradoWaterRightsSeasonalLimits, searchDbColoradoWaterRightsComments, searchDbColoradoWaterRightsMoreInformation, searchDbColoradoWaterRightsLocation)

Search API for &#39;Colorado Water Rights&#39; entry type

API to search for entries of type Colorado Water Rights

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeColoradoWaterRightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeColoradoWaterRightsApi apiInstance = new TypeColoradoWaterRightsApi(defaultClient);
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
    String searchDbColoradoWaterRightsStructureName = "searchDbColoradoWaterRightsStructureName_example"; // String | Structure Name
    String searchDbColoradoWaterRightsStructureType = "searchDbColoradoWaterRightsStructureType_example"; // String | Structure Type
    String searchDbColoradoWaterRightsWaterSource = "searchDbColoradoWaterRightsWaterSource_example"; // String | Water Source
    String searchDbColoradoWaterRightsCounty = "searchDbColoradoWaterRightsCounty_example"; // String | County
    String searchDbColoradoWaterRightsAdjudicationDate = "searchDbColoradoWaterRightsAdjudicationDate_example"; // String | Adjudication Date
    String searchDbColoradoWaterRightsAppropriationDate = "searchDbColoradoWaterRightsAppropriationDate_example"; // String | Appropriation Date
    String searchDbColoradoWaterRightsPriorityNo = "searchDbColoradoWaterRightsPriorityNo_example"; // String | Priority No
    String searchDbColoradoWaterRightsDecreedUses = "searchDbColoradoWaterRightsDecreedUses_example"; // String | Decreed Uses
    Double searchDbColoradoWaterRightsNetAbsolute = 3.4D; // Double | Net Absolute
    Double searchDbColoradoWaterRightsNetConditional = 3.4D; // Double | Net Conditional
    Double searchDbColoradoWaterRightsNetApexAbsolute = 3.4D; // Double | Net Apex Absolute
    Double searchDbColoradoWaterRightsNetApexConditional = 3.4D; // Double | Net Apex Conditional
    String searchDbColoradoWaterRightsDecreedUnits = "searchDbColoradoWaterRightsDecreedUnits_example"; // String | Decreed Units
    String searchDbColoradoWaterRightsSeasonalLimits = "searchDbColoradoWaterRightsSeasonalLimits_example"; // String | Seasonal Limits
    String searchDbColoradoWaterRightsComments = "searchDbColoradoWaterRightsComments_example"; // String | Comments
    String searchDbColoradoWaterRightsMoreInformation = "searchDbColoradoWaterRightsMoreInformation_example"; // String | More Information
    String searchDbColoradoWaterRightsLocation = "searchDbColoradoWaterRightsLocation_example"; // String | Location
    try {
      apiInstance.searchColoradoWaterRights(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbColoradoWaterRightsStructureName, searchDbColoradoWaterRightsStructureType, searchDbColoradoWaterRightsWaterSource, searchDbColoradoWaterRightsCounty, searchDbColoradoWaterRightsAdjudicationDate, searchDbColoradoWaterRightsAppropriationDate, searchDbColoradoWaterRightsPriorityNo, searchDbColoradoWaterRightsDecreedUses, searchDbColoradoWaterRightsNetAbsolute, searchDbColoradoWaterRightsNetConditional, searchDbColoradoWaterRightsNetApexAbsolute, searchDbColoradoWaterRightsNetApexConditional, searchDbColoradoWaterRightsDecreedUnits, searchDbColoradoWaterRightsSeasonalLimits, searchDbColoradoWaterRightsComments, searchDbColoradoWaterRightsMoreInformation, searchDbColoradoWaterRightsLocation);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeColoradoWaterRightsApi#searchColoradoWaterRights");
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
| **searchDbColoradoWaterRightsStructureName** | **String**| Structure Name | [optional] |
| **searchDbColoradoWaterRightsStructureType** | **String**| Structure Type | [optional] |
| **searchDbColoradoWaterRightsWaterSource** | **String**| Water Source | [optional] |
| **searchDbColoradoWaterRightsCounty** | **String**| County | [optional] |
| **searchDbColoradoWaterRightsAdjudicationDate** | **String**| Adjudication Date | [optional] |
| **searchDbColoradoWaterRightsAppropriationDate** | **String**| Appropriation Date | [optional] |
| **searchDbColoradoWaterRightsPriorityNo** | **String**| Priority No | [optional] |
| **searchDbColoradoWaterRightsDecreedUses** | **String**| Decreed Uses | [optional] |
| **searchDbColoradoWaterRightsNetAbsolute** | **Double**| Net Absolute | [optional] |
| **searchDbColoradoWaterRightsNetConditional** | **Double**| Net Conditional | [optional] |
| **searchDbColoradoWaterRightsNetApexAbsolute** | **Double**| Net Apex Absolute | [optional] |
| **searchDbColoradoWaterRightsNetApexConditional** | **Double**| Net Apex Conditional | [optional] |
| **searchDbColoradoWaterRightsDecreedUnits** | **String**| Decreed Units | [optional] |
| **searchDbColoradoWaterRightsSeasonalLimits** | **String**| Seasonal Limits | [optional] |
| **searchDbColoradoWaterRightsComments** | **String**| Comments | [optional] |
| **searchDbColoradoWaterRightsMoreInformation** | **String**| More Information | [optional] |
| **searchDbColoradoWaterRightsLocation** | **String**| Location | [optional] |

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

