

# UpdateBudgetActionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The account ID of the user. It&#39;s a 12-digit number. |  |
|**budgetName** | **String** |  A string that represents the budget name. The \&quot;:\&quot; and \&quot;\\\&quot; characters, and the \&quot;/action/\&quot; substring, aren&#39;t allowed. |  |
|**actionId** | [**String**](String.md) |  |  |
|**notificationType** | **NotificationType** |  |  [optional] |
|**actionThreshold** | [**ActionThreshold**](ActionThreshold.md) |  |  [optional] |
|**definition** | [**Definition**](Definition.md) |  |  [optional] |
|**executionRoleArn** | [**String**](String.md) |  |  [optional] |
|**approvalModel** | [**ApprovalModel**](ApprovalModel.md) |  |  [optional] |
|**subscribers** | [**List&lt;Subscriber&gt;**](Subscriber.md) |  A list of subscribers. |  [optional] |



