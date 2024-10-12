# TypeBoulderCountyVoterDetailsApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchBoulderCountyVoterDetails**](TypeBoulderCountyVoterDetailsApi.md#searchBoulderCountyVoterDetails) | **GET** /repository/search/type/boulder_county_voter_details | Search API for &#39;Boulder County Voter Details&#39; entry type |


<a id="searchBoulderCountyVoterDetails"></a>
# **searchBoulderCountyVoterDetails**
> searchBoulderCountyVoterDetails(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBoulderCountyVoterDetailsFirstName, searchDbBoulderCountyVoterDetailsLastName, searchDbBoulderCountyVoterDetailsRegistrationDate, searchDbBoulderCountyVoterDetailsLastUpdatedDate, searchDbBoulderCountyVoterDetailsResidentialAddress, searchDbBoulderCountyVoterDetailsResidentialCity, searchDbBoulderCountyVoterDetailsMailingZipCode, searchDbBoulderCountyVoterDetailsVoterStatus, searchDbBoulderCountyVoterDetailsParty, searchDbBoulderCountyVoterDetailsGender, searchDbBoulderCountyVoterDetailsBirthYear, searchDbBoulderCountyVoterDetailsPrecinctCode, searchDbBoulderCountyVoterDetailsCongressional, searchDbBoulderCountyVoterDetailsStateSenate, searchDbBoulderCountyVoterDetailsStateHouse, searchDbBoulderCountyVoterDetailsMunicipality, searchDbBoulderCountyVoterDetailsCityWardDistrict, searchDbBoulderCountyVoterDetailsSchoolDistrict, searchDbBoulderCountyVoterDetailsLocation)

Search API for &#39;Boulder County Voter Details&#39; entry type

API to search for entries of type Boulder County Voter Details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeBoulderCountyVoterDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeBoulderCountyVoterDetailsApi apiInstance = new TypeBoulderCountyVoterDetailsApi(defaultClient);
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
    String searchDbBoulderCountyVoterDetailsFirstName = "searchDbBoulderCountyVoterDetailsFirstName_example"; // String | First Name
    String searchDbBoulderCountyVoterDetailsLastName = "searchDbBoulderCountyVoterDetailsLastName_example"; // String | Last Name
    String searchDbBoulderCountyVoterDetailsRegistrationDate = "searchDbBoulderCountyVoterDetailsRegistrationDate_example"; // String | Registration Date
    String searchDbBoulderCountyVoterDetailsLastUpdatedDate = "searchDbBoulderCountyVoterDetailsLastUpdatedDate_example"; // String | Last Updated Date
    String searchDbBoulderCountyVoterDetailsResidentialAddress = "searchDbBoulderCountyVoterDetailsResidentialAddress_example"; // String | Residential Address
    String searchDbBoulderCountyVoterDetailsResidentialCity = "searchDbBoulderCountyVoterDetailsResidentialCity_example"; // String | Residential City
    String searchDbBoulderCountyVoterDetailsMailingZipCode = "searchDbBoulderCountyVoterDetailsMailingZipCode_example"; // String | Mailing Zip Code
    String searchDbBoulderCountyVoterDetailsVoterStatus = "searchDbBoulderCountyVoterDetailsVoterStatus_example"; // String | Voter Status
    String searchDbBoulderCountyVoterDetailsParty = "searchDbBoulderCountyVoterDetailsParty_example"; // String | Party
    String searchDbBoulderCountyVoterDetailsGender = "searchDbBoulderCountyVoterDetailsGender_example"; // String | Gender
    Integer searchDbBoulderCountyVoterDetailsBirthYear = 56; // Integer | Birth Year
    String searchDbBoulderCountyVoterDetailsPrecinctCode = "searchDbBoulderCountyVoterDetailsPrecinctCode_example"; // String | Precinct Code
    String searchDbBoulderCountyVoterDetailsCongressional = "searchDbBoulderCountyVoterDetailsCongressional_example"; // String | Congressional
    String searchDbBoulderCountyVoterDetailsStateSenate = "searchDbBoulderCountyVoterDetailsStateSenate_example"; // String | State Senate
    String searchDbBoulderCountyVoterDetailsStateHouse = "searchDbBoulderCountyVoterDetailsStateHouse_example"; // String | State House
    String searchDbBoulderCountyVoterDetailsMunicipality = "searchDbBoulderCountyVoterDetailsMunicipality_example"; // String | Municipality
    String searchDbBoulderCountyVoterDetailsCityWardDistrict = "searchDbBoulderCountyVoterDetailsCityWardDistrict_example"; // String | City Ward/district
    String searchDbBoulderCountyVoterDetailsSchoolDistrict = "searchDbBoulderCountyVoterDetailsSchoolDistrict_example"; // String | School District
    String searchDbBoulderCountyVoterDetailsLocation = "searchDbBoulderCountyVoterDetailsLocation_example"; // String | Location
    try {
      apiInstance.searchBoulderCountyVoterDetails(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBoulderCountyVoterDetailsFirstName, searchDbBoulderCountyVoterDetailsLastName, searchDbBoulderCountyVoterDetailsRegistrationDate, searchDbBoulderCountyVoterDetailsLastUpdatedDate, searchDbBoulderCountyVoterDetailsResidentialAddress, searchDbBoulderCountyVoterDetailsResidentialCity, searchDbBoulderCountyVoterDetailsMailingZipCode, searchDbBoulderCountyVoterDetailsVoterStatus, searchDbBoulderCountyVoterDetailsParty, searchDbBoulderCountyVoterDetailsGender, searchDbBoulderCountyVoterDetailsBirthYear, searchDbBoulderCountyVoterDetailsPrecinctCode, searchDbBoulderCountyVoterDetailsCongressional, searchDbBoulderCountyVoterDetailsStateSenate, searchDbBoulderCountyVoterDetailsStateHouse, searchDbBoulderCountyVoterDetailsMunicipality, searchDbBoulderCountyVoterDetailsCityWardDistrict, searchDbBoulderCountyVoterDetailsSchoolDistrict, searchDbBoulderCountyVoterDetailsLocation);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeBoulderCountyVoterDetailsApi#searchBoulderCountyVoterDetails");
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
| **searchDbBoulderCountyVoterDetailsFirstName** | **String**| First Name | [optional] |
| **searchDbBoulderCountyVoterDetailsLastName** | **String**| Last Name | [optional] |
| **searchDbBoulderCountyVoterDetailsRegistrationDate** | **String**| Registration Date | [optional] |
| **searchDbBoulderCountyVoterDetailsLastUpdatedDate** | **String**| Last Updated Date | [optional] |
| **searchDbBoulderCountyVoterDetailsResidentialAddress** | **String**| Residential Address | [optional] |
| **searchDbBoulderCountyVoterDetailsResidentialCity** | **String**| Residential City | [optional] |
| **searchDbBoulderCountyVoterDetailsMailingZipCode** | **String**| Mailing Zip Code | [optional] |
| **searchDbBoulderCountyVoterDetailsVoterStatus** | **String**| Voter Status | [optional] |
| **searchDbBoulderCountyVoterDetailsParty** | **String**| Party | [optional] |
| **searchDbBoulderCountyVoterDetailsGender** | **String**| Gender | [optional] |
| **searchDbBoulderCountyVoterDetailsBirthYear** | **Integer**| Birth Year | [optional] |
| **searchDbBoulderCountyVoterDetailsPrecinctCode** | **String**| Precinct Code | [optional] |
| **searchDbBoulderCountyVoterDetailsCongressional** | **String**| Congressional | [optional] |
| **searchDbBoulderCountyVoterDetailsStateSenate** | **String**| State Senate | [optional] |
| **searchDbBoulderCountyVoterDetailsStateHouse** | **String**| State House | [optional] |
| **searchDbBoulderCountyVoterDetailsMunicipality** | **String**| Municipality | [optional] |
| **searchDbBoulderCountyVoterDetailsCityWardDistrict** | **String**| City Ward/district | [optional] |
| **searchDbBoulderCountyVoterDetailsSchoolDistrict** | **String**| School District | [optional] |
| **searchDbBoulderCountyVoterDetailsLocation** | **String**| Location | [optional] |

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

