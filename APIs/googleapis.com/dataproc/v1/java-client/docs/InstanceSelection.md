

# InstanceSelection

Defines machines types and a rank to which the machines types belong.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**machineTypes** | **List&lt;String&gt;** | Optional. Full machine-type names, e.g. \&quot;n1-standard-16\&quot;. |  [optional] |
|**rank** | **Integer** | Optional. Preference of this instance selection. Lower number means higher preference. Dataproc will first try to create a VM based on the machine-type with priority rank and fallback to next rank based on availability. Machine types and instance selections with the same priority have the same preference. |  [optional] |



