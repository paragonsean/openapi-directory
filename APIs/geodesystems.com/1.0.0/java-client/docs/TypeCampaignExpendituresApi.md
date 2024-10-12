# TypeCampaignExpendituresApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchCampaignExpenditures**](TypeCampaignExpendituresApi.md#searchCampaignExpenditures) | **GET** /repository/search/type/campaign_expenditures | Search API for &#39;Campaign Expenditures&#39; entry type |


<a id="searchCampaignExpenditures"></a>
# **searchCampaignExpenditures**
> searchCampaignExpenditures(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbCampaignExpendituresCommittee, searchDbCampaignExpendituresAmount, searchDbCampaignExpendituresParty, searchDbCampaignExpendituresRecipient, searchDbCampaignExpendituresCity, searchDbCampaignExpendituresState, searchDbCampaignExpendituresZipCode, searchDbCampaignExpendituresTransactionDate, searchDbCampaignExpendituresPurpose, searchDbCampaignExpendituresMemoText, searchDbCampaignExpendituresLocation)

Search API for &#39;Campaign Expenditures&#39; entry type

API to search for entries of type Campaign Expenditures

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeCampaignExpendituresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeCampaignExpendituresApi apiInstance = new TypeCampaignExpendituresApi(defaultClient);
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
    String searchDbCampaignExpendituresCommittee = "searchDbCampaignExpendituresCommittee_example"; // String | Committee
    Double searchDbCampaignExpendituresAmount = 3.4D; // Double | Amount
    String searchDbCampaignExpendituresParty = "searchDbCampaignExpendituresParty_example"; // String | Party
    String searchDbCampaignExpendituresRecipient = "searchDbCampaignExpendituresRecipient_example"; // String | Recipient
    String searchDbCampaignExpendituresCity = "searchDbCampaignExpendituresCity_example"; // String | City
    String searchDbCampaignExpendituresState = "searchDbCampaignExpendituresState_example"; // String | State
    String searchDbCampaignExpendituresZipCode = "searchDbCampaignExpendituresZipCode_example"; // String | Zip Code
    String searchDbCampaignExpendituresTransactionDate = "searchDbCampaignExpendituresTransactionDate_example"; // String | Transaction Date
    String searchDbCampaignExpendituresPurpose = "searchDbCampaignExpendituresPurpose_example"; // String | Purpose
    String searchDbCampaignExpendituresMemoText = "searchDbCampaignExpendituresMemoText_example"; // String | Memo Text
    String searchDbCampaignExpendituresLocation = "searchDbCampaignExpendituresLocation_example"; // String | Location
    try {
      apiInstance.searchCampaignExpenditures(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbCampaignExpendituresCommittee, searchDbCampaignExpendituresAmount, searchDbCampaignExpendituresParty, searchDbCampaignExpendituresRecipient, searchDbCampaignExpendituresCity, searchDbCampaignExpendituresState, searchDbCampaignExpendituresZipCode, searchDbCampaignExpendituresTransactionDate, searchDbCampaignExpendituresPurpose, searchDbCampaignExpendituresMemoText, searchDbCampaignExpendituresLocation);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeCampaignExpendituresApi#searchCampaignExpenditures");
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
| **searchDbCampaignExpendituresCommittee** | **String**| Committee | [optional] |
| **searchDbCampaignExpendituresAmount** | **Double**| Amount | [optional] |
| **searchDbCampaignExpendituresParty** | **String**| Party | [optional] |
| **searchDbCampaignExpendituresRecipient** | **String**| Recipient | [optional] |
| **searchDbCampaignExpendituresCity** | **String**| City | [optional] |
| **searchDbCampaignExpendituresState** | **String**| State | [optional] |
| **searchDbCampaignExpendituresZipCode** | **String**| Zip Code | [optional] |
| **searchDbCampaignExpendituresTransactionDate** | **String**| Transaction Date | [optional] |
| **searchDbCampaignExpendituresPurpose** | **String**| Purpose | [optional] |
| **searchDbCampaignExpendituresMemoText** | **String**| Memo Text | [optional] |
| **searchDbCampaignExpendituresLocation** | **String**| Location | [optional] |

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

