

# Project


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminUrl** | **String** | URL to the page where project administration can be done. Administrative access is still required when accessing the url. |  [optional] |
|**country** | **String** | The country code |  [optional] |
|**created** | **OffsetDateTime** | The timestamp when this project was created. |  [optional] |
|**createdBy** | **UUID** | The id of the user that created the project. If the creator is not known this value is *null* |  [optional] |
|**designId** | **Long** | The id of the design this project are using or null if no design is used |  [optional] |
|**externalId** | **String** | The external id (foreign key). Must not exceed 255 characters. |  [optional] |
|**id** | **Long** | Unique identifier representing a specific project. Id numbers are never reused. |  [optional] |
|**locale** | **String** | The primary locale for this project |  [optional] |
|**name** | **String** | The internal name of the project |  [optional] |
|**note** | **String** | The internal note field |  [optional] |
|**orgId** | **Long** | The id of the organization unit this project belongs to |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Project status. Can be either ACTIVATED, NEW or DISABLED |  [optional] |
|**timezone** | **String** | The main timezone for the project |  [optional] |
|**userDescription** | **String** | The description presented to participants. This value can be *null*. |  [optional] |
|**userTitle** | **String** | The title presented to participants |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVATED | &quot;ACTIVATED&quot; |
| NEW | &quot;NEW&quot; |
| DISABLED | &quot;DISABLED&quot; |



