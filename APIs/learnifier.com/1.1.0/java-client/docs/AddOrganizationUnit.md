

# AddOrganizationUnit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caller** | **UUID** | The id of the user that initiated this operation |  [optional] |
|**clientNumber** | **String** | A client number. Sometimes used when communicating with external system. Must be unique if specified. |  [optional] |
|**country** | **String** | The country code that best matches the organization unit. If unspecified the platform default will be set. |  [optional] |
|**displayName** | **String** | The name shown for the organization unit |  |
|**externalId** | **String** | The external id (foreign key). Must not exceed 255 characters. |  [optional] |
|**parent** | **BigDecimal** | A Organization Unit id of the parent Organization Unit (optional). |  [optional] |



