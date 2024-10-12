

# KYCScreeningResult

The results of a safe harbour KYC check of an individual 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressMatchCount** | **Integer** | The number of address matches |  |
|**checkResult** | [**CheckResultEnum**](#CheckResultEnum) | The disposition of the 2+2 Safe Harbour check  |  [optional] |
|**dobMatchCount** | **Integer** | The number of date of birth matches |  |
|**matchingSources** | **List&lt;String&gt;** | The is of matching data sources that produced a success match for the person being screened Example given is not indicative of the actual sources available.  |  [optional] |
|**nameMatchCount** | **Integer** | The number of name matches |  |



## Enum: CheckResultEnum

| Name | Value |
|---- | -----|
| NOT_SCREENED | &quot;NOT_SCREENED&quot; |
| PASS | &quot;PASS&quot; |
| REFER | &quot;REFER&quot; |
| FAIL | &quot;FAIL&quot; |



