

# RedactTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The transaction ID to redact |  |
|**product** | [**ProductEnum**](#ProductEnum) | Product name that the ID provided relates to |  |
|**type** | [**TypeEnum**](#TypeEnum) | Required if redacting SMS data |  |



## Enum: ProductEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| VOICE | &quot;voice&quot; |
| NUMBER_INSIGHT | &quot;number-insight&quot; |
| VERIFY | &quot;verify&quot; |
| VERIFY_SDK | &quot;verify-sdk&quot; |
| MESSAGES | &quot;messages&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



