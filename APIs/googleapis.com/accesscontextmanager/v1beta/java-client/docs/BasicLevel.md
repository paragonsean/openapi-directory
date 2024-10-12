

# BasicLevel

`BasicLevel` is an `AccessLevel` using a set of recommended features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**combiningFunction** | [**CombiningFunctionEnum**](#CombiningFunctionEnum) | How the &#x60;conditions&#x60; list should be combined to determine if a request is granted this &#x60;AccessLevel&#x60;. If AND is used, each &#x60;Condition&#x60; in &#x60;conditions&#x60; must be satisfied for the &#x60;AccessLevel&#x60; to be applied. If OR is used, at least one &#x60;Condition&#x60; in &#x60;conditions&#x60; must be satisfied for the &#x60;AccessLevel&#x60; to be applied. Default behavior is AND. |  [optional] |
|**conditions** | [**List&lt;Condition&gt;**](Condition.md) | Required. A list of requirements for the &#x60;AccessLevel&#x60; to be granted. |  [optional] |



## Enum: CombiningFunctionEnum

| Name | Value |
|---- | -----|
| AND | &quot;AND&quot; |
| OR | &quot;OR&quot; |



