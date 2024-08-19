

# VirtualMachineScaleSetListOSUpgradeHistory

List of Virtual Machine Scale Set OS Upgrade History operation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | The uri to fetch the next page of OS Upgrade History. Call ListNext() with this to fetch the next page of history of upgrades. |  [optional] |
|**value** | [**List&lt;UpgradeOperationHistoricalStatusInfo&gt;**](UpgradeOperationHistoricalStatusInfo.md) | The list of OS upgrades performed on the virtual machine scale set. |  |



