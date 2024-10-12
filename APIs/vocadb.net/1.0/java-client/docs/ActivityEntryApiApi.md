# ActivityEntryApiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiActivityEntriesGet**](ActivityEntryApiApi.md#apiActivityEntriesGet) | **GET** /api/activityEntries |  |


<a id="apiActivityEntriesGet"></a>
# **apiActivityEntriesGet**
> ActivityEntryForApiContractPartialFindResult apiActivityEntriesGet(before, since, userId, editEvent, entryType, maxResults, getTotalCount, fields, entryFields, lang, sortRule)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityEntryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ActivityEntryApiApi apiInstance = new ActivityEntryApiApi(defaultClient);
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | 
    Integer userId = 56; // Integer | 
    EntryEditEvent editEvent = EntryEditEvent.fromValue("Created"); // EntryEditEvent | 
    EntryType entryType = EntryType.fromValue("Undefined"); // EntryType | 
    Integer maxResults = 50; // Integer | 
    Boolean getTotalCount = false; // Boolean | 
    ActivityEntryOptionalFields fields = ActivityEntryOptionalFields.fromValue("None"); // ActivityEntryOptionalFields | 
    EntryOptionalFields entryFields = EntryOptionalFields.fromValue("None"); // EntryOptionalFields | 
    ContentLanguagePreference lang = ContentLanguagePreference.fromValue("Default"); // ContentLanguagePreference | 
    ActivityEntrySortRule sortRule = ActivityEntrySortRule.fromValue("CreateDateDescending"); // ActivityEntrySortRule | 
    try {
      ActivityEntryForApiContractPartialFindResult result = apiInstance.apiActivityEntriesGet(before, since, userId, editEvent, entryType, maxResults, getTotalCount, fields, entryFields, lang, sortRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityEntryApiApi#apiActivityEntriesGet");
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
| **before** | **OffsetDateTime**|  | [optional] |
| **since** | **OffsetDateTime**|  | [optional] |
| **userId** | **Integer**|  | [optional] |
| **editEvent** | [**EntryEditEvent**](.md)|  | [optional] [enum: Created, Updated, Deleted, Restored] |
| **entryType** | [**EntryType**](.md)|  | [optional] [enum: Undefined, Album, Artist, DiscussionTopic, PV, ReleaseEvent, ReleaseEventSeries, Song, SongList, Tag, User, Venue] |
| **maxResults** | **Integer**|  | [optional] [default to 50] |
| **getTotalCount** | **Boolean**|  | [optional] [default to false] |
| **fields** | [**ActivityEntryOptionalFields**](.md)|  | [optional] [enum: None, ArchivedVersion, Entry] |
| **entryFields** | [**EntryOptionalFields**](.md)|  | [optional] [enum: None, AdditionalNames, Description, MainPicture, Names, PVs, Tags, WebLinks] |
| **lang** | [**ContentLanguagePreference**](.md)|  | [optional] [enum: Default, Japanese, Romaji, English] |
| **sortRule** | [**ActivityEntrySortRule**](.md)|  | [optional] [enum: CreateDateDescending, CreateDate] |

### Return type

[**ActivityEntryForApiContractPartialFindResult**](ActivityEntryForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

