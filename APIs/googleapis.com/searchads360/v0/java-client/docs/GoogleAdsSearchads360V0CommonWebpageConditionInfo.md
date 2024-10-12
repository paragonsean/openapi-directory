

# GoogleAdsSearchads360V0CommonWebpageConditionInfo

Logical expression for targeting webpages of an advertiser's website.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**argument** | **String** | Argument of webpage targeting condition. |  [optional] |
|**operand** | [**OperandEnum**](#OperandEnum) | Operand of webpage targeting condition. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Operator of webpage targeting condition. |  [optional] |



## Enum: OperandEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| URL | &quot;URL&quot; |
| CATEGORY | &quot;CATEGORY&quot; |
| PAGE_TITLE | &quot;PAGE_TITLE&quot; |
| PAGE_CONTENT | &quot;PAGE_CONTENT&quot; |
| CUSTOM_LABEL | &quot;CUSTOM_LABEL&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| EQUALS | &quot;EQUALS&quot; |
| CONTAINS | &quot;CONTAINS&quot; |



