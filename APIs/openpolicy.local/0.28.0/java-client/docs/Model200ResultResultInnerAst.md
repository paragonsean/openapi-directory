

# Model200ResultResultInnerAst

The types for declarations and runtime objects passed to your implementation. This consists of an abstract syntax tree (AST) of policy modules, package and import declarations, rules, expressions, and terms.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_package** | [**Model200ResultResultInnerAstPackage**](Model200ResultResultInnerAstPackage.md) |  |  [optional] |
|**rules** | [**Set&lt;Model200ResultResultInnerAstRulesInner&gt;**](Model200ResultResultInnerAstRulesInner.md) | When OPA evaluates a rule, it generates the content of a [virtual documents](https://www.openpolicyagent.org/docs/latest/philosophy/#the-opa-document-model) |  [optional] |



