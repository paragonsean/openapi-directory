

# BatchDeleteAlertsRequest

A request to perform batch delete on alerts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertId** | **List&lt;String&gt;** | Required. The list of alert IDs to delete. |  [optional] |
|**customerId** | **String** | Optional. The unique identifier of the Google Workspace account of the customer the alerts are associated with. The &#x60;customer_id&#x60; must have the initial \&quot;C\&quot; stripped (for example, &#x60;046psxkn&#x60;). Inferred from the caller identity if not provided. [Find your customer ID](https://support.google.com/cloudidentity/answer/10070793). |  [optional] |



