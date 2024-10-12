

# VerifyTransactionCriteria


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** |  |  |
|**baseType** | [**BaseTypeEnum**](#BaseTypeEnum) | Indicates if the transaction appears as a debit or a credit transaction in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] |
|**date** | **String** |  |  |
|**dateVariance** | **String** |  |  [optional] |
|**keyword** | **String** |  |  [optional] |
|**matched** | [**MatchedEnum**](#MatchedEnum) | Indicates if the criteria is matched or not. &lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**verifiedTransaction** | [**List&lt;Transaction&gt;**](Transaction.md) |  |  [optional] [readonly] |



## Enum: BaseTypeEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;CREDIT&quot; |
| DEBIT | &quot;DEBIT&quot; |



## Enum: MatchedEnum

| Name | Value |
|---- | -----|
| COMPLETE | &quot;COMPLETE&quot; |
| NONE | &quot;NONE&quot; |



