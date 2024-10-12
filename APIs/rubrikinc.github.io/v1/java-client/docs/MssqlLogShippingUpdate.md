

# MssqlLogShippingUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**shouldDisconnectStandbyUsers** | **Boolean** | Specifies whether to automatically disconnect users from a secondary database in standby mode when a restore operation is performed. If this value is set to false and users remain connected, any scheduled restore operations fail. If the \&quot;state\&quot; field is &#x60;RESTORING&#x60;, this value can be omitted and is ignored. |  [optional] |
|**state** | **MssqlLogShippingOkState** |  |  |



