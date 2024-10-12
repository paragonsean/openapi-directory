

# RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer

Data used to create a new Billbee user account

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptTerms** | **Boolean** | Set to true, if the user has accepted the Billbee terms &amp;amp; conditions |  [optional] |
|**address** | [**RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainerUserAddress**](RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainerUserAddress.md) |  |  [optional] |
|**affiliateCouponCode** | **String** | Specifies an billbee affiliate code to attach to the user |  [optional] |
|**defaultCurrrency** | **String** | Optionally specify the default currency of the user |  [optional] |
|**defaultVatIndex** | **Integer** | Optionally specify the default vat index of the user |  [optional] |
|**defaultVatMode** | [**DefaultVatModeEnum**](#DefaultVatModeEnum) | Optionally specify the default vat mode of the user |  [optional] |
|**email** | **String** | The Email address of the user to create |  |
|**password** | **String** |  |  [optional] |
|**vat1Rate** | **Double** | Optionally specify the vat1 (normal) rate of the user |  [optional] |
|**vat2Rate** | **Double** | Optionally specify the vat2 (reduced) rate of the user |  [optional] |



## Enum: DefaultVatModeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |



