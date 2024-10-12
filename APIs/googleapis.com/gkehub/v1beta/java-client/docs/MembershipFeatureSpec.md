

# MembershipFeatureSpec

MembershipFeatureSpec contains configuration information for a single Membership. NOTE: Please use snake case in your feature name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**anthosobservability** | [**AnthosObservabilityMembershipSpec**](AnthosObservabilityMembershipSpec.md) |  |  [optional] |
|**cloudbuild** | [**MembershipSpec**](MembershipSpec.md) |  |  [optional] |
|**configmanagement** | [**ConfigManagementMembershipSpec**](ConfigManagementMembershipSpec.md) |  |  [optional] |
|**fleetobservability** | **Object** | **FleetObservability**: The membership-specific input for FleetObservability feature. |  [optional] |
|**identityservice** | [**IdentityServiceMembershipSpec**](IdentityServiceMembershipSpec.md) |  |  [optional] |
|**mesh** | [**ServiceMeshMembershipSpec**](ServiceMeshMembershipSpec.md) |  |  [optional] |
|**origin** | [**Origin**](Origin.md) |  |  [optional] |
|**policycontroller** | [**PolicyControllerMembershipSpec**](PolicyControllerMembershipSpec.md) |  |  [optional] |



