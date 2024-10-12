# TypeCampaignDonorsApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchCampaignDonors**](TypeCampaignDonorsApi.md#searchCampaignDonors) | **GET** /repository/search/type/campaign_donors | Search API for &#39;Campaign Donors&#39; entry type |


<a id="searchCampaignDonors"></a>
# **searchCampaignDonors**
> searchCampaignDonors(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbCampaignDonorsCommittee, searchDbCampaignDonorsAmount, searchDbCampaignDonorsParty, searchDbCampaignDonorsDonor, searchDbCampaignDonorsGender, searchDbCampaignDonorsCity, searchDbCampaignDonorsState, searchDbCampaignDonorsZipCode, searchDbCampaignDonorsEmployer, searchDbCampaignDonorsOccupation, searchDbCampaignDonorsDate, searchDbCampaignDonorsLocation)

Search API for &#39;Campaign Donors&#39; entry type

API to search for entries of type Campaign Donors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeCampaignDonorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeCampaignDonorsApi apiInstance = new TypeCampaignDonorsApi(defaultClient);
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
    String searchDbCampaignDonorsCommittee = "searchDbCampaignDonorsCommittee_example"; // String | Committee
    Double searchDbCampaignDonorsAmount = 3.4D; // Double | Amount
    String searchDbCampaignDonorsParty = "searchDbCampaignDonorsParty_example"; // String | Party
    String searchDbCampaignDonorsDonor = "searchDbCampaignDonorsDonor_example"; // String | Donor
    String searchDbCampaignDonorsGender = "searchDbCampaignDonorsGender_example"; // String | Gender
    String searchDbCampaignDonorsCity = "searchDbCampaignDonorsCity_example"; // String | City
    String searchDbCampaignDonorsState = "searchDbCampaignDonorsState_example"; // String | State
    String searchDbCampaignDonorsZipCode = "searchDbCampaignDonorsZipCode_example"; // String | Zip Code
    String searchDbCampaignDonorsEmployer = "searchDbCampaignDonorsEmployer_example"; // String | Employer
    String searchDbCampaignDonorsOccupation = "searchDbCampaignDonorsOccupation_example"; // String | Occupation
    String searchDbCampaignDonorsDate = "searchDbCampaignDonorsDate_example"; // String | Date
    String searchDbCampaignDonorsLocation = "searchDbCampaignDonorsLocation_example"; // String | Location
    try {
      apiInstance.searchCampaignDonors(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbCampaignDonorsCommittee, searchDbCampaignDonorsAmount, searchDbCampaignDonorsParty, searchDbCampaignDonorsDonor, searchDbCampaignDonorsGender, searchDbCampaignDonorsCity, searchDbCampaignDonorsState, searchDbCampaignDonorsZipCode, searchDbCampaignDonorsEmployer, searchDbCampaignDonorsOccupation, searchDbCampaignDonorsDate, searchDbCampaignDonorsLocation);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeCampaignDonorsApi#searchCampaignDonors");
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
| **searchDbCampaignDonorsCommittee** | **String**| Committee | [optional] |
| **searchDbCampaignDonorsAmount** | **Double**| Amount | [optional] |
| **searchDbCampaignDonorsParty** | **String**| Party | [optional] |
| **searchDbCampaignDonorsDonor** | **String**| Donor | [optional] |
| **searchDbCampaignDonorsGender** | **String**| Gender | [optional] |
| **searchDbCampaignDonorsCity** | **String**| City | [optional] |
| **searchDbCampaignDonorsState** | **String**| State | [optional] |
| **searchDbCampaignDonorsZipCode** | **String**| Zip Code | [optional] |
| **searchDbCampaignDonorsEmployer** | **String**| Employer | [optional] |
| **searchDbCampaignDonorsOccupation** | **String**| Occupation | [optional] |
| **searchDbCampaignDonorsDate** | **String**| Date | [optional] |
| **searchDbCampaignDonorsLocation** | **String**| Location | [optional] |

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

