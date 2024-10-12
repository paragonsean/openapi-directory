# TestTheExhibitDayApiWithSwagger.EventsApi

All URIs are relative to *https://api.exhibitday.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events0Get**](EventsApi.md#events0Get) | **GET** /v1/events/ | 
[**events1Post**](EventsApi.md#events1Post) | **POST** /v1/events/ | 
[**events2Patch**](EventsApi.md#events2Patch) | **PATCH** /v1/events/ | 
[**events3Delete**](EventsApi.md#events3Delete) | **DELETE** /v1/events/ | 
[**eventsInfo0Get**](EventsApi.md#eventsInfo0Get) | **GET** /v1/events/info | 



## events0Get

> String events0Get(apiKey, opts)



Retrieve Events

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.EventsApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'filterByEventNameContainsText': "filterByEventNameContainsText_example", // String | Only include events that have the given text in the event Name. For example: If you want to retrieve all the events that have the word “International” in the event Name field, pass in the value “International” for the filter_by_event_name_contains_text parameter. Note: this text search is not case-sensitive.
  'filterByStartDateGreaterThanOrEqualTo': new Date("2013-10-20"), // Date | Only include events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
  'filterByStartDateSmallerThanOrEqualTo': new Date("2013-10-20"), // Date | Only include events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
  'filterByEndDateGreaterThanOrEqualTo': new Date("2013-10-20"), // Date | Only include events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
  'filterByEndDateSmallerThanOrEqualTo': new Date("2013-10-20"), // Date | Only include events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
  'filterByEventParticipationTypeId': 3.4, // Number | Only include events that have their participation_type_id equal to the value passed in for this filter parameter. To get a list of available event Participation Type Ids in your workspace, refer to this endpoint: /v1/references/event_participation_types
  'filterByEventFormatId': 3.4, // Number | Only include events that have their format_id equal to the value passed in for this filter parameter. The following integer values are accepted (1 for In-Person, 2 for Virtual, 3 for Hybrid)
  'filterByEventStarRating': 3.4, // Number | Only include events that have their star rating equal to the value passed in for this filter parameter. The following integer values are accepted: 0, 1, 2, 3
  'filterByEventTag': "filterByEventTag_example", // String | Only include events that have this tag. For example, you can use this filter to get all the events that have the tag “International”. Note: You can only pass in one tag to filter based on.
  'filterByCustomEventFieldCustomNNNNNN': "filterByCustomEventFieldCustomNNNNNN_example", // String | This is a special filter that lets you filter down your events based on a value of a Custom Text field or a Custom Dropdown field under the Event Information tab, Event Booth tab, or the Special Event tab. To use this filter, you’ll need the field name for the custom text field or custom dropdown field. You can obtain a list of field names for custom event fields in your workspace from the following endpoint: /v1/references/event_custom_fields. For example, if you have configured a custom dropdown field called “Region” under the Event information tab, and its field name is “custom_123456” and you would like to filter your events to include only ones that have “Northeast” selected for that custom dropdown field, pass in “filter_by_custom_event_field__custom_123456” as the parameter name and “Northeast” as its parameter value. Note: You can only filter down based on one custom event field (and it has to be either a custom text field or a custom dropdown field).
  'filterByIntegrationMetadataField1': "filterByIntegrationMetadataField1_example", // String | Only include events that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
  'filterByIntegrationMetadataField2': "filterByIntegrationMetadataField2_example", // String | Only include events that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
  'filterByIntegrationMetadataField3': "filterByIntegrationMetadataField3_example", // String | Only include events that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
  'filterByIntegrationMetadataField4': "filterByIntegrationMetadataField4_example", // String | Only include events that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
  'filterByIntegrationMetadataField5': "filterByIntegrationMetadataField5_example", // String | Only include events that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: An event's integration_metadata_field_5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \"external id\" of the event from another system you're integrating with).
  'hydrateTasks': "'false'", // String | Include the tasks collection for each event in the result set. Note: hydrating the task collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of tasks for each event in the result set.
  'hydrateTaskSectionsList': "'false'", // String | Include the list of available task sections for each event in the result set. Note: hydrating the event task section collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of task sections for each event in the result set.
  'hydrateCustomFields': "'false'" // String | Include the event custom fields (i.e. custom fields that have been added to your workspace) for each event in the result set. Note: hydrating the event custom field collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the custom field values for each event in the result set.
};
apiInstance.events0Get(apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **filterByEventNameContainsText** | **String**| Only include events that have the given text in the event Name. For example: If you want to retrieve all the events that have the word “International” in the event Name field, pass in the value “International” for the filter_by_event_name_contains_text parameter. Note: this text search is not case-sensitive. | [optional] 
 **filterByStartDateGreaterThanOrEqualTo** | **Date**| Only include events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 
 **filterByStartDateSmallerThanOrEqualTo** | **Date**| Only include events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 
 **filterByEndDateGreaterThanOrEqualTo** | **Date**| Only include events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 
 **filterByEndDateSmallerThanOrEqualTo** | **Date**| Only include events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 
 **filterByEventParticipationTypeId** | **Number**| Only include events that have their participation_type_id equal to the value passed in for this filter parameter. To get a list of available event Participation Type Ids in your workspace, refer to this endpoint: /v1/references/event_participation_types | [optional] 
 **filterByEventFormatId** | **Number**| Only include events that have their format_id equal to the value passed in for this filter parameter. The following integer values are accepted (1 for In-Person, 2 for Virtual, 3 for Hybrid) | [optional] 
 **filterByEventStarRating** | **Number**| Only include events that have their star rating equal to the value passed in for this filter parameter. The following integer values are accepted: 0, 1, 2, 3 | [optional] 
 **filterByEventTag** | **String**| Only include events that have this tag. For example, you can use this filter to get all the events that have the tag “International”. Note: You can only pass in one tag to filter based on. | [optional] 
 **filterByCustomEventFieldCustomNNNNNN** | **String**| This is a special filter that lets you filter down your events based on a value of a Custom Text field or a Custom Dropdown field under the Event Information tab, Event Booth tab, or the Special Event tab. To use this filter, you’ll need the field name for the custom text field or custom dropdown field. You can obtain a list of field names for custom event fields in your workspace from the following endpoint: /v1/references/event_custom_fields. For example, if you have configured a custom dropdown field called “Region” under the Event information tab, and its field name is “custom_123456” and you would like to filter your events to include only ones that have “Northeast” selected for that custom dropdown field, pass in “filter_by_custom_event_field__custom_123456” as the parameter name and “Northeast” as its parameter value. Note: You can only filter down based on one custom event field (and it has to be either a custom text field or a custom dropdown field). | [optional] 
 **filterByIntegrationMetadataField1** | **String**| Only include events that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField2** | **String**| Only include events that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField3** | **String**| Only include events that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField4** | **String**| Only include events that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] 
 **filterByIntegrationMetadataField5** | **String**| Only include events that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with). | [optional] 
 **hydrateTasks** | **String**| Include the tasks collection for each event in the result set. Note: hydrating the task collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of tasks for each event in the result set. | [optional] [default to &#39;false&#39;]
 **hydrateTaskSectionsList** | **String**| Include the list of available task sections for each event in the result set. Note: hydrating the event task section collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of task sections for each event in the result set. | [optional] [default to &#39;false&#39;]
 **hydrateCustomFields** | **String**| Include the event custom fields (i.e. custom fields that have been added to your workspace) for each event in the result set. Note: hydrating the event custom field collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the custom field values for each event in the result set. | [optional] [default to &#39;false&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## events1Post

> String events1Post(apiKey, name, startDate, endDate, opts)



Add an Event

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.EventsApi();
let apiKey = "apiKey_example"; // String | 
let name = "name_example"; // String | The name of the event.
let startDate = new Date("2013-10-20"); // Date | Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date.
let endDate = new Date("2013-10-20"); // Date | Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date.
let opts = {
  'formatId': 1.0, // Number | Integer representing the format_id for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid)
  'participationTypeId': 1.0, // Number | Integer representing the event_participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id's: /v1/references/event_participation_types
  'integrationMetadataField1': "integrationMetadataField1_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField2': "integrationMetadataField2_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField3': "integrationMetadataField3_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField4': "integrationMetadataField4_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField5': "integrationMetadataField5_example" // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
};
apiInstance.events1Post(apiKey, name, startDate, endDate, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **name** | **String**| The name of the event. | 
 **startDate** | **Date**| Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date. | 
 **endDate** | **Date**| Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date. | 
 **formatId** | **Number**| Integer representing the format_id for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid) | [optional] [default to 1.0]
 **participationTypeId** | **Number**| Integer representing the event_participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id&#39;s: /v1/references/event_participation_types | [optional] [default to 1.0]
 **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## events2Patch

> String events2Patch(apiKey, id, opts)



Update an Event

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.EventsApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | The id of the event you would like to update.
let opts = {
  'name': "name_example", // String | The name of the event.
  'startDate': new Date("2013-10-20"), // Date | Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date.
  'endDate': new Date("2013-10-20"), // Date | Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date.
  'participationTypeId': 3.4, // Number | Integer representing the participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id's: /v1/references/event_participation_types
  'formatId': 3.4, // Number | Integer representing the FormatId for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid)
  'starRating': 3.4, // Number | Star Rating for the event (0, 1, 2, or 3).
  'websiteUrl': "websiteUrl_example", // String | URL of the event website. Must be a well-formed URL.
  'venueName': "venueName_example", // String | The name of the venue for the event.
  'boothSize': 3.4, // Number | The size of your booth for the event.
  'boothNumber': 3.4, // Number | Your booth number for the event.
  'eventNotes': 3.4, // Number | Event Notes (under the Event Information tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
  'boothNotes': 3.4, // Number | Booth Notes (under the event Booth tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
  'budgetNotes': 3.4, // Number | Budget Notes (under the event Budget tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
  'roiNotes': 3.4, // Number | ROI Notes (under the event ROI tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a <br/> tag.
  'budgetBoothReservation': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for reserving the booth for the event.
  'budgetBoothServices': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for all the booth services for the event.
  'budgetAttendeeRegistrations': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for event registration / attendee tickets.
  'budgetTravel': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for travel and lodging for the event.
  'budgetGiveaways': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for your giveaways (swag and raffle items) for the event.
  'budgetShipments': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for all shipments for the event.
  'budgetMiscExpenses': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for all miscellaneous expenses for the event.
  'budgetSponsorships': 3.4, // Number | A number (greater or equal to 0.00) that represents the budget for all sponsorships for the event.
  'roiNumLeads': 3.4, // Number | An integer (greater or equal to 0) that represents the number of leads generated from this event.
  'roiNumImpressionsBooth': 3.4, // Number | An integer (greater or equal to 0) that represents the number of booth walk-bys / impressions (i.e., estimated total number of people who saw your booth at this event).
  'roiNumImpressionsSponsorships': 3.4, // Number | An integer (greater or equal to 0) that represents the number of sponsorship impressions (i.e., estimated total number of people reached through all your sponsorships for this event).
  'roiNumImpressionsMedia': 3.4, // Number | An integer (greater or equal to 0) that represents the number of social/traditional media impressions (i.e., estimated total number of people reached via social media or traditional media coverage).
  'roiNumMeetingsExistingCustomers': 3.4, // Number | An integer (greater or equal to 0) that represents the number of meetings with existing customers (i.e., total number of meetings your team had with your existing customers at this event).
  'roiNumMeetingsNewCustomers': 3.4, // Number | An integer (greater or equal to 0) that represents the number of meetings with new/potential customers (i.e., total number of meetings your team had with new/potential customers at this event).
  'roiAmountActualSales': 3.4, // Number | A number (greater or equal to 0.00) that represents the actual sales amount (attributable to this event and already closed).
  'roiAmountPotentialSales': 3.4, // Number | A number (greater or equal to 0.00) that represents the additional opportunity / potential sales amount (attributable to this event, but, yet to be closed).
  'integrationMetadataField1': "integrationMetadataField1_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField2': "integrationMetadataField2_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField3': "integrationMetadataField3_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField4': "integrationMetadataField4_example", // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
  'integrationMetadataField5': "integrationMetadataField5_example" // String | This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you'd like about a particular event. For example, you can use it to store the \"external id\" of the event (from another system you're integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
};
apiInstance.events2Patch(apiKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| The id of the event you would like to update. | 
 **name** | **String**| The name of the event. | [optional] 
 **startDate** | **Date**| Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date. | [optional] 
 **endDate** | **Date**| Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date. | [optional] 
 **participationTypeId** | **Number**| Integer representing the participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id&#39;s: /v1/references/event_participation_types | [optional] 
 **formatId** | **Number**| Integer representing the FormatId for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid) | [optional] 
 **starRating** | **Number**| Star Rating for the event (0, 1, 2, or 3). | [optional] 
 **websiteUrl** | **String**| URL of the event website. Must be a well-formed URL. | [optional] 
 **venueName** | **String**| The name of the venue for the event. | [optional] 
 **boothSize** | **Number**| The size of your booth for the event. | [optional] 
 **boothNumber** | **Number**| Your booth number for the event. | [optional] 
 **eventNotes** | **Number**| Event Notes (under the Event Information tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] 
 **boothNotes** | **Number**| Booth Notes (under the event Booth tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] 
 **budgetNotes** | **Number**| Budget Notes (under the event Budget tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] 
 **roiNotes** | **Number**| ROI Notes (under the event ROI tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag. | [optional] 
 **budgetBoothReservation** | **Number**| A number (greater or equal to 0.00) that represents the budget for reserving the booth for the event. | [optional] 
 **budgetBoothServices** | **Number**| A number (greater or equal to 0.00) that represents the budget for all the booth services for the event. | [optional] 
 **budgetAttendeeRegistrations** | **Number**| A number (greater or equal to 0.00) that represents the budget for event registration / attendee tickets. | [optional] 
 **budgetTravel** | **Number**| A number (greater or equal to 0.00) that represents the budget for travel and lodging for the event. | [optional] 
 **budgetGiveaways** | **Number**| A number (greater or equal to 0.00) that represents the budget for your giveaways (swag and raffle items) for the event. | [optional] 
 **budgetShipments** | **Number**| A number (greater or equal to 0.00) that represents the budget for all shipments for the event. | [optional] 
 **budgetMiscExpenses** | **Number**| A number (greater or equal to 0.00) that represents the budget for all miscellaneous expenses for the event. | [optional] 
 **budgetSponsorships** | **Number**| A number (greater or equal to 0.00) that represents the budget for all sponsorships for the event. | [optional] 
 **roiNumLeads** | **Number**| An integer (greater or equal to 0) that represents the number of leads generated from this event. | [optional] 
 **roiNumImpressionsBooth** | **Number**| An integer (greater or equal to 0) that represents the number of booth walk-bys / impressions (i.e., estimated total number of people who saw your booth at this event). | [optional] 
 **roiNumImpressionsSponsorships** | **Number**| An integer (greater or equal to 0) that represents the number of sponsorship impressions (i.e., estimated total number of people reached through all your sponsorships for this event). | [optional] 
 **roiNumImpressionsMedia** | **Number**| An integer (greater or equal to 0) that represents the number of social/traditional media impressions (i.e., estimated total number of people reached via social media or traditional media coverage). | [optional] 
 **roiNumMeetingsExistingCustomers** | **Number**| An integer (greater or equal to 0) that represents the number of meetings with existing customers (i.e., total number of meetings your team had with your existing customers at this event). | [optional] 
 **roiNumMeetingsNewCustomers** | **Number**| An integer (greater or equal to 0) that represents the number of meetings with new/potential customers (i.e., total number of meetings your team had with new/potential customers at this event). | [optional] 
 **roiAmountActualSales** | **Number**| A number (greater or equal to 0.00) that represents the actual sales amount (attributable to this event and already closed). | [optional] 
 **roiAmountPotentialSales** | **Number**| A number (greater or equal to 0.00) that represents the additional opportunity / potential sales amount (attributable to this event, but, yet to be closed). | [optional] 
 **integrationMetadataField1** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField2** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField3** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField4** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 
 **integrationMetadataField5** | **String**| This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field. | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## events3Delete

> String events3Delete(apiKey, id)



Delete an Event

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.EventsApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | The id of the event you would like to delete.
apiInstance.events3Delete(apiKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| The id of the event you would like to delete. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsInfo0Get

> String eventsInfo0Get(apiKey, id)



Retrieve a Single Event by id

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.EventsApi();
let apiKey = "apiKey_example"; // String | 
let id = 3.4; // Number | Id of the specific event that you would like to retrieve.
apiInstance.eventsInfo0Get(apiKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  | 
 **id** | **Number**| Id of the specific event that you would like to retrieve. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

