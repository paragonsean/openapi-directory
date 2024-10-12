

# ResponseStatusCode

A status to accept. Either a status code class like \"2xx\", or an integer status code like \"200\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**statusClass** | [**StatusClassEnum**](#StatusClassEnum) | A class of status codes to accept. |  [optional] |
|**statusValue** | **Integer** | A status code to accept. |  [optional] |



## Enum: StatusClassEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATUS_CLASS_UNSPECIFIED&quot; |
| _1_XX | &quot;STATUS_CLASS_1XX&quot; |
| _2_XX | &quot;STATUS_CLASS_2XX&quot; |
| _3_XX | &quot;STATUS_CLASS_3XX&quot; |
| _4_XX | &quot;STATUS_CLASS_4XX&quot; |
| _5_XX | &quot;STATUS_CLASS_5XX&quot; |
| ANY | &quot;STATUS_CLASS_ANY&quot; |



