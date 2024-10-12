# TypeBolderRentalHousingApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchBolderRentalHousing**](TypeBolderRentalHousingApi.md#searchBolderRentalHousing) | **GET** /repository/search/type/bolder_rental_housing | Search API for &#39;Boulder Rental Housing&#39; entry type |


<a id="searchBolderRentalHousing"></a>
# **searchBolderRentalHousing**
> searchBolderRentalHousing(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBolderRentalHousingPropaddr1, searchDbBolderRentalHousingRentaltype, searchDbBolderRentalHousingBldgtype, searchDbBolderRentalHousingDwellunits, searchDbBolderRentalHousingRoomunits, searchDbBolderRentalHousingNeighbrhd, searchDbBolderRentalHousingComplexnm, searchDbBolderRentalHousingName, searchDbBolderRentalHousingPersontype, searchDbBolderRentalHousingCompany, searchDbBolderRentalHousingEngcompl, searchDbBolderRentalHousingLicenseexp, searchDbBolderRentalHousingLicensenum, searchDbBolderRentalHousingPpl1Coname, searchDbBolderRentalHousingPerson1, searchDbBolderRentalHousingPpl1Role, searchDbBolderRentalHousingPpl2Coname, searchDbBolderRentalHousingPerson2, searchDbBolderRentalHousingPpl2Role, searchDbBolderRentalHousingLocation)

Search API for &#39;Boulder Rental Housing&#39; entry type

API to search for entries of type Boulder Rental Housing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeBolderRentalHousingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeBolderRentalHousingApi apiInstance = new TypeBolderRentalHousingApi(defaultClient);
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
    String searchDbBolderRentalHousingPropaddr1 = "searchDbBolderRentalHousingPropaddr1_example"; // String | Property Address
    String searchDbBolderRentalHousingRentaltype = "searchDbBolderRentalHousingRentaltype_example"; // String | Rental Type
    String searchDbBolderRentalHousingBldgtype = "searchDbBolderRentalHousingBldgtype_example"; // String | Building Type
    Integer searchDbBolderRentalHousingDwellunits = 56; // Integer | Dwelling Units
    Integer searchDbBolderRentalHousingRoomunits = 56; // Integer | Room Units
    String searchDbBolderRentalHousingNeighbrhd = "searchDbBolderRentalHousingNeighbrhd_example"; // String | Neighborhood
    String searchDbBolderRentalHousingComplexnm = "searchDbBolderRentalHousingComplexnm_example"; // String | Complex Name
    String searchDbBolderRentalHousingName = "searchDbBolderRentalHousingName_example"; // String | Name
    String searchDbBolderRentalHousingPersontype = "searchDbBolderRentalHousingPersontype_example"; // String | Person Type
    String searchDbBolderRentalHousingCompany = "searchDbBolderRentalHousingCompany_example"; // String | Company
    String searchDbBolderRentalHousingEngcompl = "searchDbBolderRentalHousingEngcompl_example"; // String | Engcompl
    String searchDbBolderRentalHousingLicenseexp = "searchDbBolderRentalHousingLicenseexp_example"; // String | Expiration Date
    String searchDbBolderRentalHousingLicensenum = "searchDbBolderRentalHousingLicensenum_example"; // String | Licensenum
    String searchDbBolderRentalHousingPpl1Coname = "searchDbBolderRentalHousingPpl1Coname_example"; // String | Ppl1 Coname
    String searchDbBolderRentalHousingPerson1 = "searchDbBolderRentalHousingPerson1_example"; // String | Person 1
    String searchDbBolderRentalHousingPpl1Role = "searchDbBolderRentalHousingPpl1Role_example"; // String | Ppl1 Role
    String searchDbBolderRentalHousingPpl2Coname = "searchDbBolderRentalHousingPpl2Coname_example"; // String | Ppl2 Coname
    String searchDbBolderRentalHousingPerson2 = "searchDbBolderRentalHousingPerson2_example"; // String | Person 2
    String searchDbBolderRentalHousingPpl2Role = "searchDbBolderRentalHousingPpl2Role_example"; // String | Ppl2 Role
    String searchDbBolderRentalHousingLocation = "searchDbBolderRentalHousingLocation_example"; // String | Location
    try {
      apiInstance.searchBolderRentalHousing(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBolderRentalHousingPropaddr1, searchDbBolderRentalHousingRentaltype, searchDbBolderRentalHousingBldgtype, searchDbBolderRentalHousingDwellunits, searchDbBolderRentalHousingRoomunits, searchDbBolderRentalHousingNeighbrhd, searchDbBolderRentalHousingComplexnm, searchDbBolderRentalHousingName, searchDbBolderRentalHousingPersontype, searchDbBolderRentalHousingCompany, searchDbBolderRentalHousingEngcompl, searchDbBolderRentalHousingLicenseexp, searchDbBolderRentalHousingLicensenum, searchDbBolderRentalHousingPpl1Coname, searchDbBolderRentalHousingPerson1, searchDbBolderRentalHousingPpl1Role, searchDbBolderRentalHousingPpl2Coname, searchDbBolderRentalHousingPerson2, searchDbBolderRentalHousingPpl2Role, searchDbBolderRentalHousingLocation);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeBolderRentalHousingApi#searchBolderRentalHousing");
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
| **searchDbBolderRentalHousingPropaddr1** | **String**| Property Address | [optional] |
| **searchDbBolderRentalHousingRentaltype** | **String**| Rental Type | [optional] |
| **searchDbBolderRentalHousingBldgtype** | **String**| Building Type | [optional] |
| **searchDbBolderRentalHousingDwellunits** | **Integer**| Dwelling Units | [optional] |
| **searchDbBolderRentalHousingRoomunits** | **Integer**| Room Units | [optional] |
| **searchDbBolderRentalHousingNeighbrhd** | **String**| Neighborhood | [optional] |
| **searchDbBolderRentalHousingComplexnm** | **String**| Complex Name | [optional] |
| **searchDbBolderRentalHousingName** | **String**| Name | [optional] |
| **searchDbBolderRentalHousingPersontype** | **String**| Person Type | [optional] |
| **searchDbBolderRentalHousingCompany** | **String**| Company | [optional] |
| **searchDbBolderRentalHousingEngcompl** | **String**| Engcompl | [optional] |
| **searchDbBolderRentalHousingLicenseexp** | **String**| Expiration Date | [optional] |
| **searchDbBolderRentalHousingLicensenum** | **String**| Licensenum | [optional] |
| **searchDbBolderRentalHousingPpl1Coname** | **String**| Ppl1 Coname | [optional] |
| **searchDbBolderRentalHousingPerson1** | **String**| Person 1 | [optional] |
| **searchDbBolderRentalHousingPpl1Role** | **String**| Ppl1 Role | [optional] |
| **searchDbBolderRentalHousingPpl2Coname** | **String**| Ppl2 Coname | [optional] |
| **searchDbBolderRentalHousingPerson2** | **String**| Person 2 | [optional] |
| **searchDbBolderRentalHousingPpl2Role** | **String**| Ppl2 Role | [optional] |
| **searchDbBolderRentalHousingLocation** | **String**| Location | [optional] |

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

