

# FreeListingsProgramStatus

Response message for GetFreeListingsProgramStatus.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**globalState** | [**GlobalStateEnum**](#GlobalStateEnum) | State of the program. &#x60;ENABLED&#x60; if there are offers for at least one region. |  [optional] |
|**regionStatuses** | [**List&lt;FreeListingsProgramStatusRegionStatus&gt;**](FreeListingsProgramStatusRegionStatus.md) | Status of the program in each region. Regions with the same status and review eligibility are grouped together in &#x60;regionCodes&#x60;. |  [optional] |



## Enum: GlobalStateEnum

| Name | Value |
|---- | -----|
| PROGRAM_STATE_UNSPECIFIED | &quot;PROGRAM_STATE_UNSPECIFIED&quot; |
| NOT_ENABLED | &quot;NOT_ENABLED&quot; |
| NO_OFFERS_UPLOADED | &quot;NO_OFFERS_UPLOADED&quot; |
| ENABLED | &quot;ENABLED&quot; |



