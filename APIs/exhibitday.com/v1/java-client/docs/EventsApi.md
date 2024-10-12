# EventsApi

All URIs are relative to *https://api.exhibitday.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**events0Get**](EventsApi.md#events0Get) | **GET** /v1/events/ |  |
| [**events1Post**](EventsApi.md#events1Post) | **POST** /v1/events/ |  |
| [**events2Patch**](EventsApi.md#events2Patch) | **PATCH** /v1/events/ |  |
| [**events3Delete**](EventsApi.md#events3Delete) | **DELETE** /v1/events/ |  |
| [**eventsInfo0Get**](EventsApi.md#eventsInfo0Get) | **GET** /v1/events/info |  |


<a id="events0Get"></a>
# **events0Get**
> String events0Get(apiKey, filterByEventNameContainsText, filterByStartDateGreaterThanOrEqualTo, filterByStartDateSmallerThanOrEqualTo, filterByEndDateGreaterThanOrEqualTo, filterByEndDateSmallerThanOrEqualTo, filterByEventParticipationTypeId, filterByEventFormatId, filterByEventStarRating, filterByEventTag, filterByCustomEventFieldCustomNNNNNN, filterByIntegrationMetadataField1, filterByIntegrationMetadataField2, filterByIntegrationMetadataField3, filterByIntegrationMetadataField4, filterByIntegrationMetadataField5, hydrateTasks, hydrateTaskSectionsList, hydrateCustomFields)



Retrieve Events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String filterByEventNameContainsText = "filterByEventNameContainsText_example"; // String | Only include events that have the given text in the event Name. For example: If you want to retrieve all the events that have the word “International” in the event Name field, pass in the value “International” for the filter_by_event_name_contains_text parameter. Note: this text search is not case-sensitive.
    LocalDate filterByStartDateGreaterThanOrEqualTo = LocalDate.now(); // LocalDate | Only include events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    LocalDate filterByStartDateSmallerThanOrEqualTo = LocalDate.now(); // LocalDate | Only include events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    LocalDate filterByEndDateGreaterThanOrEqualTo = LocalDate.now(); // LocalDate | Only include events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    LocalDate filterByEndDateSmallerThanOrEqualTo = LocalDate.now(); // LocalDate | Only include events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    BigDecimal filterByEventParticipationTypeId = new BigDecimal(78); // BigDecimal | Only include events that have their participation_type_id equal to the value passed in for this filter parameter. To get a list of available event Participation Type Ids in your workspace, refer to this endpoint: /v1/references/event_participation_types
    BigDecimal filterByEventFormatId = new BigDecimal(78); // BigDecimal | Only include events that have their format_id equal to the value passed in for this filter parameter. The following integer values are accepted (1 for In-Person, 2 for Virtual, 3 for Hybrid)
    BigDecimal filterByEventStarRating = new BigDecimal(78); // BigDecimal | Only include events that have their star rating equal to the value passed in for this filter parameter. The following integer values are accepted: 0, 1, 2, 3
    String filterByEventTag = "filterByEventTag_example"; // String | Only include events that have this tag. For example, you can use this filter to get all the events that have the tag “International”. Note: You can only pass in one tag to filter based on.
    String filterByCustomEventFieldCustomNNNNNN = "filterByCustomEventFieldCustomNNNNNN_example"; // String | This is a special filter that lets you filter down your events based on a value of a Custom Text field or a Custom Dropdown field under the Event Information tab, Event Booth tab, or the Special Event tab. To use this filter, you’ll need the field name for the custom text field or custom dropdown field. You can obtain a list of field names for custom event fields in your workspace from the following endpoint: /v1/references/event_custom_fields. For example, if you have configured a custom dropdown field called “Region” under the Event information tab, and its field name is “custom_123456” and you would like to filter your events to include only ones that have “Northeast” selected for that custom dropdown field, pass in “filter_by_custom_event_field__custom_123456” as the parameter name and “Northeast” as its parameter value. Note: You can only filter down based on one custom event field (and it has to be either a custom text field or a custom dropdown field).
    String filterByIntegrationMetadataField1 = "filterByIntegrationMetadataField1_example"; // String | Only include events that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
    String filterByIntegrationMetadataField2 = "filterByIntegrationMetadataField2_example"; // String | Only include events that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
    String filterByIntegrationMetadataField3 = "filterByIntegrationMetadataField3_example"; // String | Only include events that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
    String filterByIntegrationMetadataField4 = "filterByIntegrationMetadataField4_example"; // String | Only include events that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
    String filterByIntegrationMetadataField5 = "filterByIntegrationMetadataField5_example"; // String | Only include events that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
    String hydrateTasks = "false"; // String | Include the tasks collection for each event in the result set. Note: hydrating the task collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of tasks for each event in the result set.
    String hydrateTaskSectionsList = "false"; // String | Include the list of available task sections for each event in the result set. Note: hydrating the event task section collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of task sections for each event in the result set.
    String hydrateCustomFields = "false"; // String | Include the event custom fields (i.e. custom fields that have been added to your workspace) for each event in the result set. Note: hydrating the event custom field collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the custom field values for each event in the result set.
    try {
      String result = apiInstance.events0Get(apiKey, filterByEventNameContainsText, filterByStartDateGreaterThanOrEqualTo, filterByStartDateSmallerThanOrEqualTo, filterByEndDateGreaterThanOrEqualTo, filterByEndDateSmallerThanOrEqualTo, filterByEventParticipationTypeId, filterByEventFormatId, filterByEventStarRating, filterByEventTag, filterByCustomEventFieldCustomNNNNNN, filterByIntegrationMetadataField1, filterByIntegrationMetadataField2, filterByIntegrationMetadataField3, filterByIntegrationMetadataField4, filterByIntegrationMetadataField5, hydrateTasks, hydrateTaskSectionsList, hydrateCustomFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#events0Get");
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
| **apiKey** | **String**|  | |
| **filterByEventNameContainsText** | **String**| Only include events that have the given text in the event Name. For example: If you want to retrieve all the events that have the word “International” in the event Name field, pass in the value “International” for the filter_by_event_name_contains_text parameter. Note: this text search is not case-sensitive. | [optional] |
| **filterByStartDateGreaterThanOrEqualTo** | **LocalDate**| Only include events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |
| **filterByStartDateSmallerThanOrEqualTo** | **LocalDate**| Only include events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |
| **filterByEndDateGreaterThanOrEqualTo** | **LocalDate**| Only include events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |
| **filterByEndDateSmallerThanOrEqualTo** | **LocalDate**| Only include events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |
| **filterByEventParticipationTypeId** | **BigDecimal**| Only include events that have their participation_type_id equal to the value passed in for this filter parameter. To get a list of available event Participation Type Ids in your workspace, refer to this endpoint: /v1/references/event_participation_types | [optional] |
| **filterByEventFormatId** | **BigDecimal**| Only include events that have their format_id equal to the value passed in for this filter parameter. The following integer values are accepted (1 for In-Person, 2 for Virtual, 3 for Hybrid) | [optional] |
| **filterByEventStarRating** | **BigDecimal**| Only include events that have their star rating equal to the value passed in for this filter parameter. The following integer values are accepted: 0, 1, 2, 3 | [optional] |
| **filterByEventTag** | **String**| Only include events that have this tag. For example, you can use this filter to get all the events that have the tag “International”. Note: You can only pass in one tag to filter based on. | [optional] |
| **filterByCustomEventFieldCustomNNNNNN** | **String**| This is a special filter that lets you filter down your events based on a value of a Custom Text field or a Custom Dropdown field under the Event Information tab, Event Booth tab, or the Special Event tab. To use this filter, you’ll need the field name for the custom text field or custom dropdown field. You can obtain a list of field names for custom event fields in your workspace from the following endpoint: /v1/references/event_custom_fields. For example, if you have configured a custom dropdown field called “Region” under the Event information tab, and its field name is “custom_123456” and you would like to filter your events to include only ones that have “Northeast” selected for that custom dropdown field, pass in “filter_by_custom_event_field__custom_123456” as the parameter name and “Northeast” as its parameter value. Note: You can only filter down based on one custom event field (and it has to be either a custom text field or a custom dropdown field). | [optional] |
| **filterByIntegrationMetadataField1** | **String**| Only include events that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField2** | **String**| Only include events that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField3** | **String**| Only include events that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField4** | **String**| Only include events that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] |
| **filterByIntegrationMetadataField5** | **String**| Only include events that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] |
| **hydrateTasks** | **String**| Include the tasks collection for each event in the result set. Note: hydrating the task collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of tasks for each event in the result set. | [optional] [default to false] |
| **hydrateTaskSectionsList** | **String**| Include the list of available task sections for each event in the result set. Note: hydrating the event task section collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of task sections for each event in the result set. | [optional] [default to false] |
| **hydrateCustomFields** | **String**| Include the event custom fields (i.e. custom fields that have been added to your workspace) for each event in the result set. Note: hydrating the event custom field collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the custom field values for each event in the result set. | [optional] [default to false] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="events1Post"></a>
# **events1Post**
> String events1Post(apiKey, name, startDate, endDate, formatId, participationTypeId, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5)



Add an Event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String name = "name_example"; // String | The name of the event.
    LocalDate startDate = LocalDate.now(); // LocalDate | Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date.
    LocalDate endDate = LocalDate.now(); // LocalDate | Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date.
    BigDecimal formatId = new BigDecimal("1.0"); // BigDecimal | Integer representing the format_id for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid)
    BigDecimal participationTypeId = new BigDecimal("1.0"); // BigDecimal | Integer representing the event_participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id's: /v1/references/event_participation_types
    String integrationMetadataField1 = "integrationMetadataField1_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField2 = "integrationMetadataField2_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField3 = "integrationMetadataField3_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField4 = "integrationMetadataField4_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField5 = "integrationMetadataField5_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    try {
      String result = apiInstance.events1Post(apiKey, name, startDate, endDate, formatId, participationTypeId, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#events1Post");
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
| **apiKey** | **String**|  | |
| **name** | **String**| The name of the event. | |
| **startDate** | **LocalDate**| Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date. | |
| **endDate** | **LocalDate**| Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date. | |
| **formatId** | **BigDecimal**| Integer representing the format_id for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid) | [optional] [default to 1.0] |
| **participationTypeId** | **BigDecimal**| Integer representing the event_participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id&#39;s: /v1/references/event_participation_types | [optional] [default to 1.0] |
| **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="events2Patch"></a>
# **events2Patch**
> String events2Patch(apiKey, id, name, startDate, endDate, participationTypeId, formatId, starRating, websiteUrl, venueName, boothSize, boothNumber, eventNotes, boothNotes, budgetNotes, roiNotes, budgetBoothReservation, budgetBoothServices, budgetAttendeeRegistrations, budgetTravel, budgetGiveaways, budgetShipments, budgetMiscExpenses, budgetSponsorships, roiNumLeads, roiNumImpressionsBooth, roiNumImpressionsSponsorships, roiNumImpressionsMedia, roiNumMeetingsExistingCustomers, roiNumMeetingsNewCustomers, roiAmountActualSales, roiAmountPotentialSales, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5)



Update an Event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | The id of the event you would like to update.
    String name = "name_example"; // String | The name of the event.
    LocalDate startDate = LocalDate.now(); // LocalDate | Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date.
    LocalDate endDate = LocalDate.now(); // LocalDate | Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date.
    BigDecimal participationTypeId = new BigDecimal(78); // BigDecimal | Integer representing the participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id's: /v1/references/event_participation_types
    BigDecimal formatId = new BigDecimal(78); // BigDecimal | Integer representing the FormatId for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid)
    BigDecimal starRating = new BigDecimal(78); // BigDecimal | Star Rating for the event (0, 1, 2, or 3).
    String websiteUrl = "websiteUrl_example"; // String | URL of the event website. Must be a well-formed URL.
    String venueName = "venueName_example"; // String | The name of the venue for the event.
    BigDecimal boothSize = new BigDecimal(78); // BigDecimal | The size of your booth for the event.
    BigDecimal boothNumber = new BigDecimal(78); // BigDecimal | Your booth number for the event.
    BigDecimal eventNotes = new BigDecimal(78); // BigDecimal | Event Notes (under the Event Information tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
    BigDecimal boothNotes = new BigDecimal(78); // BigDecimal | Booth Notes (under the event Booth tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
    BigDecimal budgetNotes = new BigDecimal(78); // BigDecimal | Budget Notes (under the event Budget tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
    BigDecimal roiNotes = new BigDecimal(78); // BigDecimal | ROI Notes (under the event ROI tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
    BigDecimal budgetBoothReservation = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for reserving the booth for the event.
    BigDecimal budgetBoothServices = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for all the booth services for the event.
    BigDecimal budgetAttendeeRegistrations = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for event registration / attendee tickets.
    BigDecimal budgetTravel = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for travel and lodging for the event.
    BigDecimal budgetGiveaways = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for your giveaways (swag and raffle items) for the event.
    BigDecimal budgetShipments = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for all shipments for the event.
    BigDecimal budgetMiscExpenses = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for all miscellaneous expenses for the event.
    BigDecimal budgetSponsorships = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the budget for all sponsorships for the event.
    BigDecimal roiNumLeads = new BigDecimal(78); // BigDecimal | An integer (greater or equal to 0) that represents the number of leads generated from this event.
    BigDecimal roiNumImpressionsBooth = new BigDecimal(78); // BigDecimal | An integer (greater or equal to 0) that represents the number of booth walk-bys / impressions (i.e., estimated total number of people who saw your booth at this event).
    BigDecimal roiNumImpressionsSponsorships = new BigDecimal(78); // BigDecimal | An integer (greater or equal to 0) that represents the number of sponsorship impressions (i.e., estimated total number of people reached through all your sponsorships for this event).
    BigDecimal roiNumImpressionsMedia = new BigDecimal(78); // BigDecimal | An integer (greater or equal to 0) that represents the number of social/traditional media impressions (i.e., estimated total number of people reached via social media or traditional media coverage).
    BigDecimal roiNumMeetingsExistingCustomers = new BigDecimal(78); // BigDecimal | An integer (greater or equal to 0) that represents the number of meetings with existing customers (i.e., total number of meetings your team had with your existing customers at this event).
    BigDecimal roiNumMeetingsNewCustomers = new BigDecimal(78); // BigDecimal | An integer (greater or equal to 0) that represents the number of meetings with new/potential customers (i.e., total number of meetings your team had with new/potential customers at this event).
    BigDecimal roiAmountActualSales = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the actual sales amount (attributable to this event and already closed).
    BigDecimal roiAmountPotentialSales = new BigDecimal(78); // BigDecimal | A number (greater or equal to 0.00) that represents the additional opportunity / potential sales amount (attributable to this event, but, yet to be closed).
    String integrationMetadataField1 = "integrationMetadataField1_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField2 = "integrationMetadataField2_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField3 = "integrationMetadataField3_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField4 = "integrationMetadataField4_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    String integrationMetadataField5 = "integrationMetadataField5_example"; // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    try {
      String result = apiInstance.events2Patch(apiKey, id, name, startDate, endDate, participationTypeId, formatId, starRating, websiteUrl, venueName, boothSize, boothNumber, eventNotes, boothNotes, budgetNotes, roiNotes, budgetBoothReservation, budgetBoothServices, budgetAttendeeRegistrations, budgetTravel, budgetGiveaways, budgetShipments, budgetMiscExpenses, budgetSponsorships, roiNumLeads, roiNumImpressionsBooth, roiNumImpressionsSponsorships, roiNumImpressionsMedia, roiNumMeetingsExistingCustomers, roiNumMeetingsNewCustomers, roiAmountActualSales, roiAmountPotentialSales, integrationMetadataField1, integrationMetadataField2, integrationMetadataField3, integrationMetadataField4, integrationMetadataField5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#events2Patch");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| The id of the event you would like to update. | |
| **name** | **String**| The name of the event. | [optional] |
| **startDate** | **LocalDate**| Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date. | [optional] |
| **endDate** | **LocalDate**| Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date. | [optional] |
| **participationTypeId** | **BigDecimal**| Integer representing the participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id&#39;s: /v1/references/event_participation_types | [optional] |
| **formatId** | **BigDecimal**| Integer representing the FormatId for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid) | [optional] |
| **starRating** | **BigDecimal**| Star Rating for the event (0, 1, 2, or 3). | [optional] |
| **websiteUrl** | **String**| URL of the event website. Must be a well-formed URL. | [optional] |
| **venueName** | **String**| The name of the venue for the event. | [optional] |
| **boothSize** | **BigDecimal**| The size of your booth for the event. | [optional] |
| **boothNumber** | **BigDecimal**| Your booth number for the event. | [optional] |
| **eventNotes** | **BigDecimal**| Event Notes (under the Event Information tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] |
| **boothNotes** | **BigDecimal**| Booth Notes (under the event Booth tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] |
| **budgetNotes** | **BigDecimal**| Budget Notes (under the event Budget tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] |
| **roiNotes** | **BigDecimal**| ROI Notes (under the event ROI tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] |
| **budgetBoothReservation** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for reserving the booth for the event. | [optional] |
| **budgetBoothServices** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for all the booth services for the event. | [optional] |
| **budgetAttendeeRegistrations** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for event registration / attendee tickets. | [optional] |
| **budgetTravel** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for travel and lodging for the event. | [optional] |
| **budgetGiveaways** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for your giveaways (swag and raffle items) for the event. | [optional] |
| **budgetShipments** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for all shipments for the event. | [optional] |
| **budgetMiscExpenses** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for all miscellaneous expenses for the event. | [optional] |
| **budgetSponsorships** | **BigDecimal**| A number (greater or equal to 0.00) that represents the budget for all sponsorships for the event. | [optional] |
| **roiNumLeads** | **BigDecimal**| An integer (greater or equal to 0) that represents the number of leads generated from this event. | [optional] |
| **roiNumImpressionsBooth** | **BigDecimal**| An integer (greater or equal to 0) that represents the number of booth walk-bys / impressions (i.e., estimated total number of people who saw your booth at this event). | [optional] |
| **roiNumImpressionsSponsorships** | **BigDecimal**| An integer (greater or equal to 0) that represents the number of sponsorship impressions (i.e., estimated total number of people reached through all your sponsorships for this event). | [optional] |
| **roiNumImpressionsMedia** | **BigDecimal**| An integer (greater or equal to 0) that represents the number of social/traditional media impressions (i.e., estimated total number of people reached via social media or traditional media coverage). | [optional] |
| **roiNumMeetingsExistingCustomers** | **BigDecimal**| An integer (greater or equal to 0) that represents the number of meetings with existing customers (i.e., total number of meetings your team had with your existing customers at this event). | [optional] |
| **roiNumMeetingsNewCustomers** | **BigDecimal**| An integer (greater or equal to 0) that represents the number of meetings with new/potential customers (i.e., total number of meetings your team had with new/potential customers at this event). | [optional] |
| **roiAmountActualSales** | **BigDecimal**| A number (greater or equal to 0.00) that represents the actual sales amount (attributable to this event and already closed). | [optional] |
| **roiAmountPotentialSales** | **BigDecimal**| A number (greater or equal to 0.00) that represents the additional opportunity / potential sales amount (attributable to this event, but, yet to be closed). | [optional] |
| **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |
| **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="events3Delete"></a>
# **events3Delete**
> String events3Delete(apiKey, id)



Delete an Event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | The id of the event you would like to delete.
    try {
      String result = apiInstance.events3Delete(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#events3Delete");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| The id of the event you would like to delete. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="eventsInfo0Get"></a>
# **eventsInfo0Get**
> String eventsInfo0Get(apiKey, id)



Retrieve a Single Event by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal id = new BigDecimal(78); // BigDecimal | Id of the specific event that you would like to retrieve.
    try {
      String result = apiInstance.eventsInfo0Get(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsInfo0Get");
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
| **apiKey** | **String**|  | |
| **id** | **BigDecimal**| Id of the specific event that you would like to retrieve. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

