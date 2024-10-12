

# GenerateTcpProxyScriptRequest

Request message for 'GenerateTcpProxyScript' request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vmMachineType** | **String** | Required. The type of the Compute instance that will host the proxy. |  [optional] |
|**vmName** | **String** | Required. The name of the Compute instance that will host the proxy. |  [optional] |
|**vmSubnet** | **String** | Required. The name of the subnet the Compute instance will use for private connectivity. Must be supplied in the form of projects/{project}/regions/{region}/subnetworks/{subnetwork}. Note: the region for the subnet must match the Compute instance region. |  [optional] |
|**vmZone** | **String** | Optional. The Google Cloud Platform zone to create the VM in. The fully qualified name of the zone must be specified, including the region name, for example \&quot;us-central1-b\&quot;. If not specified, uses the \&quot;-b\&quot; zone of the destination Connection Profile&#39;s region. |  [optional] |



