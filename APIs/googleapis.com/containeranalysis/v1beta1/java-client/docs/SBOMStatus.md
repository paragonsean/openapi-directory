

# SBOMStatus

The status of an SBOM generation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** | If there was an error generating an SBOM, this will indicate what that error was. |  [optional] |
|**sbomState** | [**SbomStateEnum**](#SbomStateEnum) | The progress of the SBOM generation. |  [optional] |



## Enum: SbomStateEnum

| Name | Value |
|---- | -----|
| SBOM_STATE_UNSPECIFIED | &quot;SBOM_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



