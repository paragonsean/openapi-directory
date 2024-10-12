

# Assignment

An assignment represents the group or groups of VM instances that the policy applies to. If an assignment is empty, it applies to all VM instances. Otherwise, the targeted VM instances must meet all the criteria specified. So if both labels and zones are specified, the policy applies to VM instances with those labels and in those zones.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupLabels** | [**List&lt;AssignmentGroupLabel&gt;**](AssignmentGroupLabel.md) | Targets instances matching at least one of these label sets. This allows an assignment to target disparate groups, for example \&quot;env&#x3D;prod or env&#x3D;staging\&quot;. |  [optional] |
|**instanceNamePrefixes** | **List&lt;String&gt;** | Targets VM instances whose name starts with one of these prefixes. Like labels, this is another way to group VM instances when targeting configs, for example prefix&#x3D;\&quot;prod-\&quot;. Only supported for project-level policies. |  [optional] |
|**instances** | **List&lt;String&gt;** | Targets any of the instances specified. Instances are specified by their URI in the form &#x60;zones/[ZONE]/instances/[INSTANCE_NAME]&#x60;. Instance targeting is uncommon and is supported to facilitate the management of changes by the instance or to target specific VM instances for development and testing. Only supported for project-level policies and must reference instances within this project. |  [optional] |
|**osTypes** | [**List&lt;AssignmentOsType&gt;**](AssignmentOsType.md) | Targets VM instances matching at least one of the following OS types. VM instances must match all supplied criteria for a given OsType to be included. |  [optional] |
|**zones** | **List&lt;String&gt;** | Targets instances in any of these zones. Leave empty to target instances in any zone. Zonal targeting is uncommon and is supported to facilitate the management of changes by zone. |  [optional] |



