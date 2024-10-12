

# LogProfileProperties

The log profile properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | **List&lt;String&gt;** | the categories of the logs. These categories are created as is convenient to the user. Some values are: &#39;Write&#39;, &#39;Delete&#39;, and/or &#39;Action.&#39; |  |
|**locations** | **List&lt;String&gt;** | List of regions for which Activity Log events should be stored or streamed. It is a comma separated list of valid ARM locations including the &#39;global&#39; location. |  |
|**retentionPolicy** | [**RetentionPolicy**](RetentionPolicy.md) |  |  |
|**serviceBusRuleId** | **String** | The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format: &#39;{service bus resource ID}/authorizationrules/{key name}&#39;. |  [optional] |
|**storageAccountId** | **String** | the resource id of the storage account to which you would like to send the Activity Log. |  [optional] |



