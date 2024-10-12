

# GoogleCloudRetailV2betaConditionQueryTerm

Query terms that we want to match on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fullMatch** | **Boolean** | Whether this is supposed to be a full or partial match. |  [optional] |
|**value** | **String** | The value of the term to match on. Value cannot be empty. Value can have at most 3 terms if specified as a partial match. Each space separated string is considered as one term. For example, \&quot;a b c\&quot; is 3 terms and allowed, but \&quot; a b c d\&quot; is 4 terms and not allowed for a partial match. |  [optional] |



