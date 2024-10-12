

# AutomationSource

The source event types which evaluate the security automation set of rules. For example - security alerts and security assessments. To learn more about the supported security events data models schemas - please visit https://aka.ms/ASCAutomationSchemas.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventSource** | [**EventSourceEnum**](#EventSourceEnum) | A valid event source type. |  [optional] |
|**ruleSets** | [**List&lt;AutomationRuleSet&gt;**](AutomationRuleSet.md) | A set of rules which evaluate upon event interception. A logical disjunction is applied between defined rule sets (logical &#39;or&#39;). |  [optional] |



## Enum: EventSourceEnum

| Name | Value |
|---- | -----|
| ASSESSMENTS | &quot;Assessments&quot; |
| ALERTS | &quot;Alerts&quot; |



