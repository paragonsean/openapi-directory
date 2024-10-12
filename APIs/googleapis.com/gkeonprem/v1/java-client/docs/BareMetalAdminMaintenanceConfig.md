

# BareMetalAdminMaintenanceConfig

BareMetalAdminMaintenanceConfig specifies configurations to put bare metal Admin cluster CRs nodes in and out of maintenance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maintenanceAddressCidrBlocks** | **List&lt;String&gt;** | Required. All IPv4 address from these ranges will be placed into maintenance mode. Nodes in maintenance mode will be cordoned and drained. When both of these are true, the \&quot;baremetal.cluster.gke.io/maintenance\&quot; annotation will be set on the node resource. |  [optional] |



