

# CreateRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**CreateRuleRequestAction**](CreateRuleRequestAction.md) |  |  |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. |  [optional] |
|**match** | [**CreateRuleRequestMatch**](CreateRuleRequestMatch.md) |  |  |
|**name** | **String** | The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can&#39;t use a hyphen as the first or last character, or immediately after another hyphen. |  |
|**priority** | **Integer** | The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags for the rule. |  [optional] |



