

# SpotInsertion

A spot insertion for playing a series of spots when a cue is received during a program.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**broadcastServiceId** | **Long** | The ID of the broadcast service for the spot insertion. |  |
|**createdDate** | **OffsetDateTime** | The date and time the spot insertion was created. Generated at creation. |  [optional] [readonly] |
|**cue** | **String** | The cue that triggers the spot insertion. |  |
|**customerId** | **Long** | The ID of the customer who owns the spot insertion. Set to the logged-in customer at creation. |  [optional] [readonly] |
|**duration** | **Integer** | The duration of the spot insertion. |  |
|**endDate** | **LocalDate** | The date the spot insertion ends. The time will be set to midnight Eastern Time. |  |
|**id** | **Long** | The unique ID of the spot insertion. Generated at creation. |  [optional] [readonly] |
|**programId** | **Long** | The ID of the program for the spot insertion. |  |
|**spots** | **List&lt;Long&gt;** | The ordered list of spot IDs to play. |  |
|**startDate** | **LocalDate** | The date the spot insertion can start. The time will be set to midnight Eastern Time. |  |



