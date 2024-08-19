

# Ownership



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | The id of the app that is owned |  |
|**customData** | **Object** | A custom JSON object that you can create and attach to this record |  [optional] |
|**date** | **Long** | The date (in millis) of when this app was owned |  |
|**developerId** | **String** | The id of the developer for this app |  |
|**expires** | **Long** | The date (in millis) of when this app ownership expires |  [optional] |
|**model** | [**Model**](Model.md) |  |  |
|**ownershipId** | **String** | The id of this ownership |  |
|**ownershipStatus** | [**OwnershipStatusEnum**](#OwnershipStatusEnum) | The current ownership status for this app |  |
|**ownershipType** | [**OwnershipTypeEnum**](#OwnershipTypeEnum) | The current ownership type for this app |  |
|**uninstallDate** | **Long** | The date (in millis) of when this app was uninstalled |  [optional] |
|**userId** | **String** | The id of the user that owns this app |  |



## Enum: OwnershipStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACTIVE | &quot;active&quot; |
| UNINSTALLED | &quot;uninstalled&quot; |
| CANCELLED | &quot;cancelled&quot; |



## Enum: OwnershipTypeEnum

| Name | Value |
|---- | -----|
| FULL | &quot;full&quot; |
| SUBSCRIPTION | &quot;subscription&quot; |
| TRIAL | &quot;trial&quot; |



