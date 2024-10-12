# AwsBudgets.CreateBudgetActionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID of the user. It&#39;s a 12-digit number. | 
**budgetName** | **String** |  A string that represents the budget name. The \&quot;:\&quot; and \&quot;\\\&quot; characters, and the \&quot;/action/\&quot; substring, aren&#39;t allowed. | 
**notificationType** | [**NotificationType**](NotificationType.md) |  | 
**actionType** | [**ActionType**](ActionType.md) |  | 
**actionThreshold** | [**ActionThreshold**](ActionThreshold.md) |  | 
**definition** | [**Definition**](Definition.md) |  | 
**executionRoleArn** | **String** |  | 
**approvalModel** | [**ApprovalModel**](ApprovalModel.md) |  | 
**subscribers** | [**[Subscriber]**](Subscriber.md) |  A list of subscribers. | 


