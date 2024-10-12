

# ActivityLogAlertLeafCondition

An Activity Log alert condition that is met by comparing an activity log field and value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**equals** | **String** | The field value will be compared to this value (case-insensitive) to determine if the condition is met. |  |
|**field** | **String** | The name of the field that this condition will examine. The possible values for this field are (case-insensitive): &#39;resourceId&#39;, &#39;category&#39;, &#39;caller&#39;, &#39;level&#39;, &#39;operationName&#39;, &#39;resourceGroup&#39;, &#39;resourceProvider&#39;, &#39;status&#39;, &#39;subStatus&#39;, &#39;resourceType&#39;, or anything beginning with &#39;properties.&#39;. |  |



