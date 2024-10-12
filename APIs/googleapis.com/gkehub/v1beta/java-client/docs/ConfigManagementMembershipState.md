

# ConfigManagementMembershipState

**Anthos Config Management**: State for a single cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**binauthzState** | [**ConfigManagementBinauthzState**](ConfigManagementBinauthzState.md) |  |  [optional] |
|**clusterName** | **String** | This field is set to the &#x60;cluster_name&#x60; field of the Membership Spec if it is not empty. Otherwise, it is set to the cluster&#39;s fleet membership name. |  [optional] |
|**configSyncState** | [**ConfigManagementConfigSyncState**](ConfigManagementConfigSyncState.md) |  |  [optional] |
|**hierarchyControllerState** | [**ConfigManagementHierarchyControllerState**](ConfigManagementHierarchyControllerState.md) |  |  [optional] |
|**membershipSpec** | [**ConfigManagementMembershipSpec**](ConfigManagementMembershipSpec.md) |  |  [optional] |
|**operatorState** | [**ConfigManagementOperatorState**](ConfigManagementOperatorState.md) |  |  [optional] |
|**policyControllerState** | [**ConfigManagementPolicyControllerState**](ConfigManagementPolicyControllerState.md) |  |  [optional] |



