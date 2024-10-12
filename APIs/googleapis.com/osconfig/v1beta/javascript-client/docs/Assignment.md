# OsConfigApi.Assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupLabels** | [**[AssignmentGroupLabel]**](AssignmentGroupLabel.md) | Targets instances matching at least one of these label sets. This allows an assignment to target disparate groups, for example \&quot;env&#x3D;prod or env&#x3D;staging\&quot;. | [optional] 
**instanceNamePrefixes** | **[String]** | Targets VM instances whose name starts with one of these prefixes. Like labels, this is another way to group VM instances when targeting configs, for example prefix&#x3D;\&quot;prod-\&quot;. Only supported for project-level policies. | [optional] 
**instances** | **[String]** | Targets any of the instances specified. Instances are specified by their URI in the form &#x60;zones/[ZONE]/instances/[INSTANCE_NAME]&#x60;. Instance targeting is uncommon and is supported to facilitate the management of changes by the instance or to target specific VM instances for development and testing. Only supported for project-level policies and must reference instances within this project. | [optional] 
**osTypes** | [**[AssignmentOsType]**](AssignmentOsType.md) | Targets VM instances matching at least one of the following OS types. VM instances must match all supplied criteria for a given OsType to be included. | [optional] 
**zones** | **[String]** | Targets instances in any of these zones. Leave empty to target instances in any zone. Zonal targeting is uncommon and is supported to facilitate the management of changes by zone. | [optional] 


