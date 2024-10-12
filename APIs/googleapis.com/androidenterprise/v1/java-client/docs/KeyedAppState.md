

# KeyedAppState

Represents a keyed app state containing a key, timestamp, severity level, optional description, and optional data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **String** | Additional field intended for machine-readable data. For example, a number or JSON object. To prevent XSS, we recommend removing any HTML from the data before displaying it. |  [optional] |
|**key** | **String** | Key indicating what the app is providing a state for. The content of the key is set by the app&#39;s developer. To prevent XSS, we recommend removing any HTML from the key before displaying it. This field will always be present. |  [optional] |
|**message** | **String** | Free-form, human-readable message describing the app state. For example, an error message. To prevent XSS, we recommend removing any HTML from the message before displaying it. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of the app state. This field will always be present. |  [optional] |
|**stateTimestampMillis** | **String** | Timestamp of when the app set the state in milliseconds since epoch. This field will always be present. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNKNOWN | &quot;severityUnknown&quot; |
| SEVERITY_INFO | &quot;severityInfo&quot; |
| SEVERITY_ERROR | &quot;severityError&quot; |



