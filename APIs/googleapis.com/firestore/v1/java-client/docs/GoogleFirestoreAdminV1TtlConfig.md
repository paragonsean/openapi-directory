

# GoogleFirestoreAdminV1TtlConfig

The TTL (time-to-live) configuration for documents that have this `Field` set. Storing a timestamp value into a TTL-enabled field will be treated as the document's absolute expiration time. Timestamp values in the past indicate that the document is eligible for immediate expiration. Using any other data type or leaving the field absent will disable expiration for the individual document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the TTL configuration. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| NEEDS_REPAIR | &quot;NEEDS_REPAIR&quot; |



