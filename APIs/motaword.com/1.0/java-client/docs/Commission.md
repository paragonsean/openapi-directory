

# Commission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Monetary**](Monetary.md) |  |  [optional] |
|**date** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**project** | [**Project**](Project.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| UNCLAIMED | &quot;unclaimed&quot; |
| FAILED | &quot;failed&quot; |
| SENT | &quot;sent&quot; |
| WAITING | &quot;waiting&quot; |
| WAITING_INVOICE | &quot;waiting_invoice&quot; |



