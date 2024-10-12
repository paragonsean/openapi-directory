

# CardFetchBodyPatch

Variant of CardFetchBody with fields as optional for patches

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectTypes** | [**List&lt;CardObjectTypeBody&gt;**](CardObjectTypeBody.md) | An array of CRM object types where this card should be displayed. HubSpot will call your target URL whenever a user visits a record page of the types defined here. |  |
|**targetUrl** | **String** | URL to a service endpoint that will respond with details for this card. HubSpot will call this endpoint each time a user visits a CRM record page where this card should be displayed. |  [optional] |



