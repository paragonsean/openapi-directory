

# IncidentList

A widget that displays a list of incidents

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**monitoredResources** | [**List&lt;MonitoredResource&gt;**](MonitoredResource.md) | Optional. The monitored resource for which incidents are listed. The resource doesn&#39;t need to be fully specified. That is, you can specify the resource type but not the values of the resource labels. The resource type and labels are used for filtering. |  [optional] |
|**policyNames** | **List&lt;String&gt;** | Optional. A list of alert policy names to filter the incident list by. Don&#39;t include the project ID prefix in the policy name. For example, use alertPolicies/utilization. |  [optional] |



