

# AGCOPowerServicesModelsECU

An AGCO Power ECU

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationCode** | **byte[]** | The code used to activate the ECU. May not be modified. Returned only on activation. |  [optional] |
|**damagedDescription** | **String** | A description why the ECU cannot be deactivated. |  [optional] |
|**engineSerialNumber** | **String** | The serial number of the ECU’s engine |  |
|**replacesECUSerialNumber** | **String** | The serial number of the ECU that this ECU replaces. Required if activating an ECU.. |  [optional] |
|**serialNumber** | **String** | The serial number of the ECU |  |
|**state** | [**StateEnum**](#StateEnum) | The state of the ECU |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| INACTIVE | &quot;Inactive&quot; |
| DAMAGED | &quot;Damaged&quot; |



