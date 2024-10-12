

# ActionHookActionBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confirmation** | [**ActionConfirmationBody**](ActionConfirmationBody.md) |  |  [optional] |
|**httpMethod** | [**HttpMethodEnum**](#HttpMethodEnum) |  |  |
|**label** | **String** |  |  [optional] |
|**propertyNamesIncluded** | **List&lt;String&gt;** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**url** | **String** |  |  |



## Enum: HttpMethodEnum

| Name | Value |
|---- | -----|
| CONNECT | &quot;CONNECT&quot; |
| DELETE | &quot;DELETE&quot; |
| GET | &quot;GET&quot; |
| HEAD | &quot;HEAD&quot; |
| OPTIONS | &quot;OPTIONS&quot; |
| PATCH | &quot;PATCH&quot; |
| POST | &quot;POST&quot; |
| PUT | &quot;PUT&quot; |
| TRACE | &quot;TRACE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACTION_HOOK | &quot;ACTION_HOOK&quot; |



