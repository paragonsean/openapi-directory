# YodleeCoreApis.TransactionCategorizationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryLevelId** | **Number** | The level of the category for which the rule is created.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, insurance, loan&lt;br&gt; | [optional] [readonly] 
**memId** | **Number** | Unique identifier of the user.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; | [optional] [readonly] 
**ruleClauses** | [**[RuleClause]**](RuleClause.md) | Details of rules. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; | [optional] [readonly] 
**rulePriority** | **Number** | The order in which the rules get executed on transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; | [optional] [readonly] 
**transactionCategorisationId** | **Number** | Category id that is assigned to the transaction when the transaction matches the rule clause. This is the id field of the transaction category resource.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; | [optional] [readonly] 
**userDefinedRuleId** | **Number** | Unique identifier generated for every rule the user creates.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; | [optional] [readonly] 


