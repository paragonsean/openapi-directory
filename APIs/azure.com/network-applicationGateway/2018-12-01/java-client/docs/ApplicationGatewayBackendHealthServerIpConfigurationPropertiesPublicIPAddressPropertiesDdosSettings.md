

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDdosSettings

Contains the DDoS protection settings of the public IP.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ddosCustomPolicy** | **Model0** |  |  [optional] |
|**protectionCoverage** | [**ProtectionCoverageEnum**](#ProtectionCoverageEnum) | The DDoS protection policy customizability of the public IP. Only standard coverage will have the ability to be customized. |  [optional] |



## Enum: ProtectionCoverageEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |



