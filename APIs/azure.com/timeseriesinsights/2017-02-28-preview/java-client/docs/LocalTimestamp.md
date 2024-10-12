

# LocalTimestamp

An object that represents the local timestamp property. It contains the format of local timestamp that needs to be used and the corresponding timezone offset information. If a value isn't specified for localTimestamp, or if null, then the local timestamp will not be ingressed with the events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | [**FormatEnum**](#FormatEnum) | An enum that represents the format of the local timestamp property that needs to be set. |  [optional] |
|**timeZoneOffset** | [**LocalTimestampTimeZoneOffset**](LocalTimestampTimeZoneOffset.md) |  |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| EMBEDDED | &quot;Embedded&quot; |
| IANA | &quot;Iana&quot; |
| TIME_SPAN | &quot;TimeSpan&quot; |



