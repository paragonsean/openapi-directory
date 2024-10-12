

# SasPortalDeviceAirInterface

Information about the device's air interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**radioTechnology** | [**RadioTechnologyEnum**](#RadioTechnologyEnum) | Conditional. This field specifies the radio access technology that is used for the CBSD. |  [optional] |
|**supportedSpec** | **String** | Optional. This field is related to the &#x60;radioTechnology&#x60; and provides the air interface specification that the CBSD is compliant with at the time of registration. |  [optional] |



## Enum: RadioTechnologyEnum

| Name | Value |
|---- | -----|
| RADIO_TECHNOLOGY_UNSPECIFIED | &quot;RADIO_TECHNOLOGY_UNSPECIFIED&quot; |
| E_UTRA | &quot;E_UTRA&quot; |
| CAMBIUM_NETWORKS | &quot;CAMBIUM_NETWORKS&quot; |
| FOUR_G_BBW_SAA_1 | &quot;FOUR_G_BBW_SAA_1&quot; |
| NR | &quot;NR&quot; |
| DOODLE_CBRS | &quot;DOODLE_CBRS&quot; |
| CW | &quot;CW&quot; |
| REDLINE | &quot;REDLINE&quot; |
| TARANA_WIRELESS | &quot;TARANA_WIRELESS&quot; |



