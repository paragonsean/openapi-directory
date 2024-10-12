# DatabaseMigrationApi.ReverseSshConnectivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | **String** | The name of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel. | [optional] 
**vmIp** | **String** | Required. The IP of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel. | [optional] 
**vmPort** | **Number** | Required. The forwarding port of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel. | [optional] 
**vpc** | **String** | The name of the VPC to peer with the Cloud SQL private network. | [optional] 


