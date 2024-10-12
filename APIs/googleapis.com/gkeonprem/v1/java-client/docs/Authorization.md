

# Authorization

Authorization defines the On-Prem cluster authorization configuration to bootstrap onto the admin cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminUsers** | [**List&lt;ClusterUser&gt;**](ClusterUser.md) | For VMware and bare metal user clusters, users will be granted the cluster-admin role on the cluster, which provides full administrative access to the cluster. For bare metal admin clusters, users will be granted the cluster-view role, which limits users to read-only access. |  [optional] |



