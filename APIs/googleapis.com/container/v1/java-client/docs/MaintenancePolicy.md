

# MaintenancePolicy

MaintenancePolicy defines the maintenance policy to be used for the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceVersion** | **String** | A hash identifying the version of this policy, so that updates to fields of the policy won&#39;t accidentally undo intermediate changes (and so that users of the API unaware of some fields won&#39;t accidentally remove other fields). Make a &#x60;get()&#x60; request to the cluster to get the current resource version and include it with requests to set the policy. |  [optional] |
|**window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  |  [optional] |



