

# Membership

Membership contains information about a member cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authority** | [**Authority**](Authority.md) |  |  [optional] |
|**createTime** | **String** | Output only. When the Membership was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. When the Membership was deleted. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of this membership, limited to 63 characters. Must match the regex: &#x60;a-zA-Z0-9*&#x60; |  [optional] |
|**endpoint** | [**MembershipEndpoint**](MembershipEndpoint.md) |  |  [optional] |
|**externalId** | **String** | Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. For GKE clusters, external_id is managed by the Hub API and updates will be ignored. The ID must match the regex: &#x60;a-zA-Z0-9*&#x60; If this Membership represents a Kubernetes cluster, this value should be set to the UID of the &#x60;kube-system&#x60; namespace object. |  [optional] |
|**infrastructureType** | [**InfrastructureTypeEnum**](#InfrastructureTypeEnum) | Optional. The infrastructure type this Membership is running on. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. GCP labels for this membership. |  [optional] |
|**lastConnectionTime** | **String** | Output only. For clusters using Connect, the timestamp of the most recent connection established with Google Cloud. This time is updated every several minutes, not continuously. For clusters that do not use GKE Connect, or that have never connected successfully, this field will be unset. |  [optional] [readonly] |
|**monitoringConfig** | [**MonitoringConfig**](MonitoringConfig.md) |  |  [optional] |
|**name** | **String** | Output only. The full, unique name of this Membership resource in the format &#x60;projects/_*_/locations/_*_/memberships/{membership_id}&#x60;, set during creation. &#x60;membership_id&#x60; must be a valid RFC 1123 compliant DNS label: 1. At most 63 characters in length 2. It must consist of lower case alphanumeric characters or &#x60;-&#x60; 3. It must start and end with an alphanumeric character Which can be expressed as the regex: &#x60;[a-z0-9]([-a-z0-9]*[a-z0-9])?&#x60;, with a maximum length of 63 characters. |  [optional] [readonly] |
|**state** | [**MembershipState**](MembershipState.md) |  |  [optional] |
|**uniqueId** | **String** | Output only. Google-generated UUID for this resource. This is unique across all Membership resources. If a Membership resource is deleted and another resource with the same name is created, it gets a different unique_id. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. When the Membership was last updated. |  [optional] [readonly] |



## Enum: InfrastructureTypeEnum

| Name | Value |
|---- | -----|
| INFRASTRUCTURE_TYPE_UNSPECIFIED | &quot;INFRASTRUCTURE_TYPE_UNSPECIFIED&quot; |
| ON_PREM | &quot;ON_PREM&quot; |
| MULTI_CLOUD | &quot;MULTI_CLOUD&quot; |



