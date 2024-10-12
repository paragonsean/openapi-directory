

# GenerateSshScriptRequest

Request message for 'GenerateSshScript' request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vm** | **String** | Required. Bastion VM Instance name to use or to create. |  [optional] |
|**vmCreationConfig** | [**VmCreationConfig**](VmCreationConfig.md) |  |  [optional] |
|**vmPort** | **Integer** | The port that will be open on the bastion host. |  [optional] |
|**vmSelectionConfig** | [**VmSelectionConfig**](VmSelectionConfig.md) |  |  [optional] |



