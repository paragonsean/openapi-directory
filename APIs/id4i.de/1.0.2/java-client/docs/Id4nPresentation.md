

# Id4nPresentation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTimestamp** | **Long** | The UTC unix timestamp of when this ID has been created |  [optional] [readonly] |
|**holderOrganizationId** | **String** | Organization namespace of the holder of the ID |  [optional] [readonly] |
|**id4n** | **String** | The ID |  [optional] [readonly] |
|**label** | **String** |  |  [optional] [readonly] |
|**ownerOrganizationId** | **String** | Organization namespace of the ID owner |  [optional] [readonly] |
|**properties** | **Map&lt;String, String&gt;** | The properties of the organization |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of ID |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GUID | &quot;GUID&quot; |
| ROUTING_COLLECTION | &quot;ROUTING_COLLECTION&quot; |
| LOGISTIC_COLLECTION | &quot;LOGISTIC_COLLECTION&quot; |
| LABELLED_COLLECTION | &quot;LABELLED_COLLECTION&quot; |



