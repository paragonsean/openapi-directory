

# RuleEmailAction

Specifies the action to send email when the rule condition is evaluated. The discriminator is always RuleEmailAction in this case.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customEmails** | **List&lt;String&gt;** | the list of administrator&#39;s custom email addresses to notify of the activation of the alert. |  [optional] |
|**sendToServiceOwners** | **Boolean** | Whether the administrators (service and co-administrators) of the service should be notified when the alert is activated. |  [optional] |



