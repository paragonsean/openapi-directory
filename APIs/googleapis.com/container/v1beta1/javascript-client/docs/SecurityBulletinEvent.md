# KubernetesEngineApi.SecurityBulletinEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affectedSupportedMinors** | **[String]** | The GKE minor versions affected by this vulnerability. | [optional] 
**briefDescription** | **String** | A brief description of the bulletin. See the bulletin pointed to by the bulletin_uri field for an expanded description. | [optional] 
**bulletinId** | **String** | The ID of the bulletin corresponding to the vulnerability. | [optional] 
**bulletinUri** | **String** | The URI link to the bulletin on the website for more information. | [optional] 
**cveIds** | **[String]** | The CVEs associated with this bulletin. | [optional] 
**manualStepsRequired** | **Boolean** | If this field is specified, it means there are manual steps that the user must take to make their clusters safe. | [optional] 
**patchedVersions** | **[String]** | The GKE versions where this vulnerability is patched. | [optional] 
**resourceTypeAffected** | **String** | The resource type (node/control plane) that has the vulnerability. Multiple notifications (1 notification per resource type) will be sent for a vulnerability that affects &gt; 1 resource type. | [optional] 
**severity** | **String** | The severity of this bulletin as it relates to GKE. | [optional] 
**suggestedUpgradeTarget** | **String** | This represents a version selected from the patched_versions field that the cluster receiving this notification should most likely want to upgrade to based on its current version. Note that if this notification is being received by a given cluster, it means that this version is currently available as an upgrade target in that cluster&#39;s location. | [optional] 


