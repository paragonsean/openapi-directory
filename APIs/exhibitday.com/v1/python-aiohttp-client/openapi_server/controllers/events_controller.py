from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def events0_get(request: web.Request, api_key, filter_by_event_name_contains_text=None, filter_by_start_date_greater_than_or_equal_to=None, filter_by_start_date_smaller_than_or_equal_to=None, filter_by_end_date_greater_than_or_equal_to=None, filter_by_end_date_smaller_than_or_equal_to=None, filter_by_event_participation_type_id=None, filter_by_event_format_id=None, filter_by_event_star_rating=None, filter_by_event_tag=None, filter_by_custom_event_field__custom_nnnnnn=None, filter_by_integration_metadata_field_1=None, filter_by_integration_metadata_field_2=None, filter_by_integration_metadata_field_3=None, filter_by_integration_metadata_field_4=None, filter_by_integration_metadata_field_5=None, hydrate_tasks=None, hydrate_task_sections_list=None, hydrate_custom_fields=None) -> web.Response:
    """events0_get

    Retrieve Events

    :param api_key: 
    :type api_key: str
    :param filter_by_event_name_contains_text: Only include events that have the given text in the event Name. For example: If you want to retrieve all the events that have the word “International” in the event Name field, pass in the value “International” for the filter_by_event_name_contains_text parameter. Note: this text search is not case-sensitive.
    :type filter_by_event_name_contains_text: str
    :param filter_by_start_date_greater_than_or_equal_to: Only include events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_start_date_greater_than_or_equal_to: str
    :param filter_by_start_date_smaller_than_or_equal_to: Only include events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_start_date_smaller_than_or_equal_to: str
    :param filter_by_end_date_greater_than_or_equal_to: Only include events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_end_date_greater_than_or_equal_to: str
    :param filter_by_end_date_smaller_than_or_equal_to: Only include events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    :type filter_by_end_date_smaller_than_or_equal_to: str
    :param filter_by_event_participation_type_id: Only include events that have their participation_type_id equal to the value passed in for this filter parameter. To get a list of available event Participation Type Ids in your workspace, refer to this endpoint: /v1/references/event_participation_types
    :type filter_by_event_participation_type_id: 
    :param filter_by_event_format_id: Only include events that have their format_id equal to the value passed in for this filter parameter. The following integer values are accepted (1 for In-Person, 2 for Virtual, 3 for Hybrid)
    :type filter_by_event_format_id: 
    :param filter_by_event_star_rating: Only include events that have their star rating equal to the value passed in for this filter parameter. The following integer values are accepted: 0, 1, 2, 3
    :type filter_by_event_star_rating: 
    :param filter_by_event_tag: Only include events that have this tag. For example, you can use this filter to get all the events that have the tag “International”. Note: You can only pass in one tag to filter based on.
    :type filter_by_event_tag: str
    :param filter_by_custom_event_field__custom_nnnnnn: This is a special filter that lets you filter down your events based on a value of a Custom Text field or a Custom Dropdown field under the Event Information tab, Event Booth tab, or the Special Event tab. To use this filter, you’ll need the field name for the custom text field or custom dropdown field. You can obtain a list of field names for custom event fields in your workspace from the following endpoint: /v1/references/event_custom_fields. For example, if you have configured a custom dropdown field called “Region” under the Event information tab, and its field name is “custom_123456” and you would like to filter your events to include only ones that have “Northeast” selected for that custom dropdown field, pass in “filter_by_custom_event_field__custom_123456” as the parameter name and “Northeast” as its parameter value. Note: You can only filter down based on one custom event field (and it has to be either a custom text field or a custom dropdown field).
    :type filter_by_custom_event_field__custom_nnnnnn: str
    :param filter_by_integration_metadata_field_1: Only include events that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_1: str
    :param filter_by_integration_metadata_field_2: Only include events that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_2: str
    :param filter_by_integration_metadata_field_3: Only include events that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_3: str
    :param filter_by_integration_metadata_field_4: Only include events that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_4: str
    :param filter_by_integration_metadata_field_5: Only include events that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: An event&#39;s integration_metadata_field_5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular event (e.g., the \&quot;external id\&quot; of the event from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_5: str
    :param hydrate_tasks: Include the tasks collection for each event in the result set. Note: hydrating the task collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of tasks for each event in the result set.
    :type hydrate_tasks: str
    :param hydrate_task_sections_list: Include the list of available task sections for each event in the result set. Note: hydrating the event task section collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of task sections for each event in the result set.
    :type hydrate_task_sections_list: str
    :param hydrate_custom_fields: Include the event custom fields (i.e. custom fields that have been added to your workspace) for each event in the result set. Note: hydrating the event custom field collection for each event in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the custom field values for each event in the result set.
    :type hydrate_custom_fields: str

    """
    filter_by_start_date_greater_than_or_equal_to = util.deserialize_date(filter_by_start_date_greater_than_or_equal_to)
    filter_by_start_date_smaller_than_or_equal_to = util.deserialize_date(filter_by_start_date_smaller_than_or_equal_to)
    filter_by_end_date_greater_than_or_equal_to = util.deserialize_date(filter_by_end_date_greater_than_or_equal_to)
    filter_by_end_date_smaller_than_or_equal_to = util.deserialize_date(filter_by_end_date_smaller_than_or_equal_to)
    return web.Response(status=200)


async def events1_post(request: web.Request, api_key, name, start_date, end_date, format_id=None, participation_type_id=None, integration_metadata_field_1=None, integration_metadata_field_2=None, integration_metadata_field_3=None, integration_metadata_field_4=None, integration_metadata_field_5=None) -> web.Response:
    """events1_post

    Add an Event

    :param api_key: 
    :type api_key: str
    :param name: The name of the event.
    :type name: str
    :param start_date: Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date.
    :type start_date: str
    :param end_date: Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date.
    :type end_date: str
    :param format_id: Integer representing the format_id for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid)
    :type format_id: 
    :param participation_type_id: Integer representing the event_participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id&#39;s: /v1/references/event_participation_types
    :type participation_type_id: 
    :param integration_metadata_field_1: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_1: str
    :param integration_metadata_field_2: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_2: str
    :param integration_metadata_field_3: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_3: str
    :param integration_metadata_field_4: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_4: str
    :param integration_metadata_field_5: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_5: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def events2_patch(request: web.Request, api_key, id, name=None, start_date=None, end_date=None, participation_type_id=None, format_id=None, star_rating=None, website_url=None, venue_name=None, booth_size=None, booth_number=None, event_notes=None, booth_notes=None, budget_notes=None, roi_notes=None, budget_booth_reservation=None, budget_booth_services=None, budget_attendee_registrations=None, budget_travel=None, budget_giveaways=None, budget_shipments=None, budget_misc_expenses=None, budget_sponsorships=None, roi_num_leads=None, roi_num_impressions_booth=None, roi_num_impressions_sponsorships=None, roi_num_impressions_media=None, roi_num_meetings_existing_customers=None, roi_num_meetings_new_customers=None, roi_amount_actual_sales=None, roi_amount_potential_sales=None, integration_metadata_field_1=None, integration_metadata_field_2=None, integration_metadata_field_3=None, integration_metadata_field_4=None, integration_metadata_field_5=None) -> web.Response:
    """events2_patch

    Update an Event

    :param api_key: 
    :type api_key: str
    :param id: The id of the event you would like to update.
    :type id: 
    :param name: The name of the event.
    :type name: str
    :param start_date: Event Start Date (format: YYYY-MM-DD). Must be smaller or equal to Event End Date.
    :type start_date: str
    :param end_date: Event End Date (format: YYYY-MM-DD). Must be greater or equal to Event Start Date.
    :type end_date: str
    :param participation_type_id: Integer representing the participation_type_id for the event (1: Committed, 2: Considering, 3: Not Going). Note: you can use the following endpoint to retrieve a list of available participation_type_id&#39;s: /v1/references/event_participation_types
    :type participation_type_id: 
    :param format_id: Integer representing the FormatId for the event (1 for In-Person, 2 for Virtual, 3 for Hybrid)
    :type format_id: 
    :param star_rating: Star Rating for the event (0, 1, 2, or 3).
    :type star_rating: 
    :param website_url: URL of the event website. Must be a well-formed URL.
    :type website_url: str
    :param venue_name: The name of the venue for the event.
    :type venue_name: str
    :param booth_size: The size of your booth for the event.
    :type booth_size: 
    :param booth_number: Your booth number for the event.
    :type booth_number: 
    :param event_notes: Event Notes (under the Event Information tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag.
    :type event_notes: 
    :param booth_notes: Booth Notes (under the event Booth tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag.
    :type booth_notes: 
    :param budget_notes: Budget Notes (under the event Budget tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag.
    :type budget_notes: 
    :param roi_notes: ROI Notes (under the event ROI tab). Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag.
    :type roi_notes: 
    :param budget_booth_reservation: A number (greater or equal to 0.00) that represents the budget for reserving the booth for the event.
    :type budget_booth_reservation: 
    :param budget_booth_services: A number (greater or equal to 0.00) that represents the budget for all the booth services for the event.
    :type budget_booth_services: 
    :param budget_attendee_registrations: A number (greater or equal to 0.00) that represents the budget for event registration / attendee tickets.
    :type budget_attendee_registrations: 
    :param budget_travel: A number (greater or equal to 0.00) that represents the budget for travel and lodging for the event.
    :type budget_travel: 
    :param budget_giveaways: A number (greater or equal to 0.00) that represents the budget for your giveaways (swag and raffle items) for the event.
    :type budget_giveaways: 
    :param budget_shipments: A number (greater or equal to 0.00) that represents the budget for all shipments for the event.
    :type budget_shipments: 
    :param budget_misc_expenses: A number (greater or equal to 0.00) that represents the budget for all miscellaneous expenses for the event.
    :type budget_misc_expenses: 
    :param budget_sponsorships: A number (greater or equal to 0.00) that represents the budget for all sponsorships for the event.
    :type budget_sponsorships: 
    :param roi_num_leads: An integer (greater or equal to 0) that represents the number of leads generated from this event.
    :type roi_num_leads: 
    :param roi_num_impressions_booth: An integer (greater or equal to 0) that represents the number of booth walk-bys / impressions (i.e., estimated total number of people who saw your booth at this event).
    :type roi_num_impressions_booth: 
    :param roi_num_impressions_sponsorships: An integer (greater or equal to 0) that represents the number of sponsorship impressions (i.e., estimated total number of people reached through all your sponsorships for this event).
    :type roi_num_impressions_sponsorships: 
    :param roi_num_impressions_media: An integer (greater or equal to 0) that represents the number of social/traditional media impressions (i.e., estimated total number of people reached via social media or traditional media coverage).
    :type roi_num_impressions_media: 
    :param roi_num_meetings_existing_customers: An integer (greater or equal to 0) that represents the number of meetings with existing customers (i.e., total number of meetings your team had with your existing customers at this event).
    :type roi_num_meetings_existing_customers: 
    :param roi_num_meetings_new_customers: An integer (greater or equal to 0) that represents the number of meetings with new/potential customers (i.e., total number of meetings your team had with new/potential customers at this event).
    :type roi_num_meetings_new_customers: 
    :param roi_amount_actual_sales: A number (greater or equal to 0.00) that represents the actual sales amount (attributable to this event and already closed).
    :type roi_amount_actual_sales: 
    :param roi_amount_potential_sales: A number (greater or equal to 0.00) that represents the additional opportunity / potential sales amount (attributable to this event, but, yet to be closed).
    :type roi_amount_potential_sales: 
    :param integration_metadata_field_1: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_1: str
    :param integration_metadata_field_2: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_2: str
    :param integration_metadata_field_3: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_3: str
    :param integration_metadata_field_4: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_4: str
    :param integration_metadata_field_5: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular event. For example, you can use it to store the \&quot;external id\&quot; of the event (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of events (using the /v1/events endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_5: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def events3_delete(request: web.Request, api_key, id) -> web.Response:
    """events3_delete

    Delete an Event

    :param api_key: 
    :type api_key: str
    :param id: The id of the event you would like to delete.
    :type id: 

    """
    return web.Response(status=200)


async def events_info0_get(request: web.Request, api_key, id) -> web.Response:
    """events_info0_get

    Retrieve a Single Event by id

    :param api_key: 
    :type api_key: str
    :param id: Id of the specific event that you would like to retrieve.
    :type id: 

    """
    return web.Response(status=200)
