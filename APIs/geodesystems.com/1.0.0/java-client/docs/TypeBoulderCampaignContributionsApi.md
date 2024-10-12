# TypeBoulderCampaignContributionsApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchBoulderCampaignContributions**](TypeBoulderCampaignContributionsApi.md#searchBoulderCampaignContributions) | **GET** /repository/search/type/boulder_campaign_contributions | Search API for &#39;Boulder Campaign Contributions&#39; entry type |


<a id="searchBoulderCampaignContributions"></a>
# **searchBoulderCampaignContributions**
> searchBoulderCampaignContributions(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBoulderCampaignContributionsCommittee, searchDbBoulderCampaignContributionsType, searchDbBoulderCampaignContributionsCommitteeNum, searchDbBoulderCampaignContributionsCandidate, searchDbBoulderCampaignContributionsFilingDate, searchDbBoulderCampaignContributionsAmendedDate, searchDbBoulderCampaignContributionsOfficialFiling, searchDbBoulderCampaignContributionsTransactionDate, searchDbBoulderCampaignContributionsLastName, searchDbBoulderCampaignContributionsFirstName, searchDbBoulderCampaignContributionsStreet, searchDbBoulderCampaignContributionsCity, searchDbBoulderCampaignContributionsState, searchDbBoulderCampaignContributionsZip, searchDbBoulderCampaignContributionsContribution, searchDbBoulderCampaignContributionsContributionType, searchDbBoulderCampaignContributionsAnonymous, searchDbBoulderCampaignContributionsFromCandidate, searchDbBoulderCampaignContributionsMatch)

Search API for &#39;Boulder Campaign Contributions&#39; entry type

API to search for entries of type Boulder Campaign Contributions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeBoulderCampaignContributionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeBoulderCampaignContributionsApi apiInstance = new TypeBoulderCampaignContributionsApi(defaultClient);
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
    String searchDbBoulderCampaignContributionsCommittee = "searchDbBoulderCampaignContributionsCommittee_example"; // String | Committee
    String searchDbBoulderCampaignContributionsType = "searchDbBoulderCampaignContributionsType_example"; // String | Type
    String searchDbBoulderCampaignContributionsCommitteeNum = "searchDbBoulderCampaignContributionsCommitteeNum_example"; // String | Committee Num
    String searchDbBoulderCampaignContributionsCandidate = "searchDbBoulderCampaignContributionsCandidate_example"; // String | Candidate
    String searchDbBoulderCampaignContributionsFilingDate = "searchDbBoulderCampaignContributionsFilingDate_example"; // String | Filing Date
    String searchDbBoulderCampaignContributionsAmendedDate = "searchDbBoulderCampaignContributionsAmendedDate_example"; // String | Amended Date
    String searchDbBoulderCampaignContributionsOfficialFiling = "searchDbBoulderCampaignContributionsOfficialFiling_example"; // String | Official Filing
    String searchDbBoulderCampaignContributionsTransactionDate = "searchDbBoulderCampaignContributionsTransactionDate_example"; // String | Transaction Date
    String searchDbBoulderCampaignContributionsLastName = "searchDbBoulderCampaignContributionsLastName_example"; // String | Last Name
    String searchDbBoulderCampaignContributionsFirstName = "searchDbBoulderCampaignContributionsFirstName_example"; // String | First Name
    String searchDbBoulderCampaignContributionsStreet = "searchDbBoulderCampaignContributionsStreet_example"; // String | Street
    String searchDbBoulderCampaignContributionsCity = "searchDbBoulderCampaignContributionsCity_example"; // String | City
    String searchDbBoulderCampaignContributionsState = "searchDbBoulderCampaignContributionsState_example"; // String | State
    String searchDbBoulderCampaignContributionsZip = "searchDbBoulderCampaignContributionsZip_example"; // String | Zip
    Double searchDbBoulderCampaignContributionsContribution = 3.4D; // Double | Contribution
    String searchDbBoulderCampaignContributionsContributionType = "searchDbBoulderCampaignContributionsContributionType_example"; // String | Contribution Type
    String searchDbBoulderCampaignContributionsAnonymous = "searchDbBoulderCampaignContributionsAnonymous_example"; // String | Anonymous
    String searchDbBoulderCampaignContributionsFromCandidate = "searchDbBoulderCampaignContributionsFromCandidate_example"; // String | From Candidate
    Double searchDbBoulderCampaignContributionsMatch = 3.4D; // Double | Match
    try {
      apiInstance.searchBoulderCampaignContributions(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbBoulderCampaignContributionsCommittee, searchDbBoulderCampaignContributionsType, searchDbBoulderCampaignContributionsCommitteeNum, searchDbBoulderCampaignContributionsCandidate, searchDbBoulderCampaignContributionsFilingDate, searchDbBoulderCampaignContributionsAmendedDate, searchDbBoulderCampaignContributionsOfficialFiling, searchDbBoulderCampaignContributionsTransactionDate, searchDbBoulderCampaignContributionsLastName, searchDbBoulderCampaignContributionsFirstName, searchDbBoulderCampaignContributionsStreet, searchDbBoulderCampaignContributionsCity, searchDbBoulderCampaignContributionsState, searchDbBoulderCampaignContributionsZip, searchDbBoulderCampaignContributionsContribution, searchDbBoulderCampaignContributionsContributionType, searchDbBoulderCampaignContributionsAnonymous, searchDbBoulderCampaignContributionsFromCandidate, searchDbBoulderCampaignContributionsMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeBoulderCampaignContributionsApi#searchBoulderCampaignContributions");
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
| **searchDbBoulderCampaignContributionsCommittee** | **String**| Committee | [optional] |
| **searchDbBoulderCampaignContributionsType** | **String**| Type | [optional] |
| **searchDbBoulderCampaignContributionsCommitteeNum** | **String**| Committee Num | [optional] |
| **searchDbBoulderCampaignContributionsCandidate** | **String**| Candidate | [optional] |
| **searchDbBoulderCampaignContributionsFilingDate** | **String**| Filing Date | [optional] |
| **searchDbBoulderCampaignContributionsAmendedDate** | **String**| Amended Date | [optional] |
| **searchDbBoulderCampaignContributionsOfficialFiling** | **String**| Official Filing | [optional] |
| **searchDbBoulderCampaignContributionsTransactionDate** | **String**| Transaction Date | [optional] |
| **searchDbBoulderCampaignContributionsLastName** | **String**| Last Name | [optional] |
| **searchDbBoulderCampaignContributionsFirstName** | **String**| First Name | [optional] |
| **searchDbBoulderCampaignContributionsStreet** | **String**| Street | [optional] |
| **searchDbBoulderCampaignContributionsCity** | **String**| City | [optional] |
| **searchDbBoulderCampaignContributionsState** | **String**| State | [optional] |
| **searchDbBoulderCampaignContributionsZip** | **String**| Zip | [optional] |
| **searchDbBoulderCampaignContributionsContribution** | **Double**| Contribution | [optional] |
| **searchDbBoulderCampaignContributionsContributionType** | **String**| Contribution Type | [optional] |
| **searchDbBoulderCampaignContributionsAnonymous** | **String**| Anonymous | [optional] |
| **searchDbBoulderCampaignContributionsFromCandidate** | **String**| From Candidate | [optional] |
| **searchDbBoulderCampaignContributionsMatch** | **Double**| Match | [optional] |

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

