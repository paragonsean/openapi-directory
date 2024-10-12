

# ExplainDataAccessResponse

List of consent scopes that are applicable to the explained access on a given resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consentScopes** | [**List&lt;ExplainDataAccessConsentScope&gt;**](ExplainDataAccessConsentScope.md) | List of applicable consent scopes. Sorted in order of actor such that scopes belonging to the same actor will be adjacent to each other in the list. |  [optional] |
|**warning** | **String** | Warnings associated with this response. It inform user with exceeded scope limit errors. |  [optional] |



