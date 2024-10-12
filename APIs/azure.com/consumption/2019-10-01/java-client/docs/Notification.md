

# Notification

The notification associated with a budget.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactEmails** | **List&lt;String&gt;** | Email addresses to send the budget notification to when the threshold is exceeded. |  |
|**contactGroups** | **List&lt;String&gt;** | Action groups to send the budget notification to when the threshold is exceeded. |  [optional] |
|**contactRoles** | **List&lt;String&gt;** | Contact roles to send the budget notification to when the threshold is exceeded. |  [optional] |
|**enabled** | **Boolean** | The notification is enabled or not. |  |
|**operator** | [**OperatorEnum**](#OperatorEnum) | The comparison operator. |  |
|**threshold** | **BigDecimal** | Threshold value associated with a notification. Notification is sent when the cost exceeded the threshold. It is always percent and has to be between 0 and 1000. |  |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUAL_TO | &quot;EqualTo&quot; |
| GREATER_THAN | &quot;GreaterThan&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;GreaterThanOrEqualTo&quot; |



