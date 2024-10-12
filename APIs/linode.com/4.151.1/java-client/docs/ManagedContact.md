

# ManagedContact

Information about someone Linode's special forces may contact in case an issue is detected with a manager service. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | The address to email this Contact to alert them of issues.  |  [optional] |
|**group** | **String** | A grouping for this Contact. This is for display purposes only.  |  [optional] |
|**id** | **Integer** | This Contact&#39;s unique ID.  |  [optional] [readonly] |
|**name** | **String** | The name of this Contact.  |  [optional] |
|**phone** | [**ManagedContactPhone**](ManagedContactPhone.md) |  |  [optional] |
|**updated** | **OffsetDateTime** | When this Contact was last updated.  |  [optional] [readonly] |



