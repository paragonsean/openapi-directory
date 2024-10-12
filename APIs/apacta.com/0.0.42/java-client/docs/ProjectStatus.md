

# ProjectStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** |  |  [optional] [readonly] |
|**createdById** | **UUID** |  |  [optional] |
|**deleted** | **String** | Only present if it&#39;s a deleted object |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**id** | **UUID** |  |  [optional] |
|**identifier** | [**IdentifierEnum**](#IdentifierEnum) | One of 3 values |  [optional] |
|**isCustom** | **Boolean** |  |  [optional] |
|**modified** | **String** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |



## Enum: IdentifierEnum

| Name | Value |
|---- | -----|
| READY_FOR_BILLING | &quot;ready_for_billing&quot; |
| OPEN | &quot;open&quot; |
| CLOSED | &quot;closed&quot; |



