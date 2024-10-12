

# GuestOsDetails

Information from Guest-level collections.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**GuestConfigDetails**](GuestConfigDetails.md) |  |  [optional] |
|**family** | [**FamilyEnum**](#FamilyEnum) | What family the OS belong to, if known. |  [optional] |
|**osName** | **String** | The name of the operating system. |  [optional] |
|**runtime** | [**GuestRuntimeDetails**](GuestRuntimeDetails.md) |  |  [optional] |
|**version** | **String** | The version of the operating system. |  [optional] |



## Enum: FamilyEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;OS_FAMILY_UNKNOWN&quot; |
| WINDOWS | &quot;OS_FAMILY_WINDOWS&quot; |
| LINUX | &quot;OS_FAMILY_LINUX&quot; |
| UNIX | &quot;OS_FAMILY_UNIX&quot; |



