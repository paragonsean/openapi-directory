

# CreateVappNetworkParams


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isDeployed** | **Boolean** | Boolean value that indicates whether the specified vApp network object has been deployed. Value is &#39;true&#39; when the vApp network object has been deployed and &#39;false&#39; when it has not been deployed. |  |
|**name** | **String** | Name of the specified vApp network object. |  |
|**parentNetworkId** | **String** | vCloud Director ID of the associated organization VDC network object. For an Isolated network, the value is empty. |  [optional] |
|**newName** | **String** | Name to assign to the vApp network that is referenced by the specified new vApp network object. If a name is specified, the Rubrik REST API server uses the name to rename the vApp network within the vCloud. If the value is empty, the vApp network is not renamed. |  [optional] |



