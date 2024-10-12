

# PatchInstanceFilter

A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**all** | **Boolean** | Target all VM instances in the project. If true, no other criteria is permitted. |  [optional] |
|**groupLabels** | [**List&lt;PatchInstanceFilterGroupLabel&gt;**](PatchInstanceFilterGroupLabel.md) | Targets VM instances matching ANY of these GroupLabels. This allows targeting of disparate groups of VM instances. |  [optional] |
|**instanceNamePrefixes** | **List&lt;String&gt;** | Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix&#x3D;\&quot;prod-\&quot;. |  [optional] |
|**instances** | **List&lt;String&gt;** | Targets any of the VM instances specified. Instances are specified by their URI in the form &#x60;zones/[ZONE]/instances/[INSTANCE_NAME]&#x60;, &#x60;projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]&#x60;, or &#x60;https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]&#x60; |  [optional] |
|**zones** | **List&lt;String&gt;** | Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone. |  [optional] |



