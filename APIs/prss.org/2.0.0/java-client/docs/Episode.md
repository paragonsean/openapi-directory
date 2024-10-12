

# Episode

An episode that defines a specific air date for an instance of a program.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beginAirDate** | **OffsetDateTime** | The date the air window opens for the episode. |  |
|**beginTransmissionDate** | **OffsetDateTime** | The date the live stream begins for the episode. Only set for live and LWSF episodes. |  [optional] |
|**createdDate** | **OffsetDateTime** | The date the segment was created. Generated at creation. |  [optional] |
|**customerId** | **Long** | The ID of the customer that owns this programs. |  [optional] |
|**endAirDate** | **OffsetDateTime** | The date the air window closes for the episode. |  |
|**endTransmissionDate** | **OffsetDateTime** | The date the live stream ends for the episode. Only set for live and LWSF episodes. |  [optional] |
|**id** | **Long** | The unique ID of the episode. Generated at creation. |  [optional] |
|**lastModifiedDate** | **OffsetDateTime** | The date the segment was last modified/updated. Automatically updated on any write operation. |  [optional] |
|**programId** | **Long** | The ID of the program that owns this episode. |  |
|**title** | **String** | The title of the program. |  |



