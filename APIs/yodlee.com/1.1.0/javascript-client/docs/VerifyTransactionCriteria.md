# YodleeCoreApis.VerifyTransactionCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** |  | 
**baseType** | **String** | Indicates if the transaction appears as a debit or a credit transaction in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**date** | **String** |  | 
**dateVariance** | **String** |  | [optional] 
**keyword** | **String** |  | [optional] 
**matched** | **String** | Indicates if the criteria is matched or not. &lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**verifiedTransaction** | [**[Transaction]**](Transaction.md) |  | [optional] [readonly] 



## Enum: BaseTypeEnum


* `CREDIT` (value: `"CREDIT"`)

* `DEBIT` (value: `"DEBIT"`)





## Enum: MatchedEnum


* `COMPLETE` (value: `"COMPLETE"`)

* `NONE` (value: `"NONE"`)




