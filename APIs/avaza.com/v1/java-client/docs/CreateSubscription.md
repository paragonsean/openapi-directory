

# CreateSubscription

New Subscription to be Created

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**event** | **String** | The event code to be notified about. Possible values: company_created, contact_created, invoice_created, invoice_sent, project_created, task_created |  |
|**secret** | **String** | Optional Secret string (255 char max). If provided, the secret will be BASE 64 encoded and used as a basic authentication http header with webhook notifications. i.e. Authorization Basic [BASE64 of Secret]\&quot; |  [optional] |
|**targetUrl** | **String** | The URL that should be notified of the event. |  |



