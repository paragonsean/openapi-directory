

# ReverseSshConnectivity

The details needed to configure a reverse SSH tunnel between the source and destination databases. These details will be used when calling the generateSshScript method (see https://cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/generateSshScript) to produce the script that will help set up the reverse SSH tunnel, and to set up the VPC peering between the Cloud SQL private network and the VPC.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vm** | **String** | The name of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel. |  [optional] |
|**vmIp** | **String** | Required. The IP of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel. |  [optional] |
|**vmPort** | **Integer** | Required. The forwarding port of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel. |  [optional] |
|**vpc** | **String** | The name of the VPC to peer with the Cloud SQL private network. |  [optional] |



