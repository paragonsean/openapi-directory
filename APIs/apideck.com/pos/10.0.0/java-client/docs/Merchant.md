

# Merchant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**language** | **String** | language code according to ISO 639-1. For the United States - EN |  [optional] |
|**mainLocationId** | **String** | The main location ID of the merchant |  [optional] |
|**name** | **String** | The name of the merchant |  [optional] |
|**ownerId** | **String** |  |  [optional] |
|**serviceCharges** | [**List&lt;ServiceCharge&gt;**](ServiceCharge.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of this merchant. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| OTHER | &quot;other&quot; |



