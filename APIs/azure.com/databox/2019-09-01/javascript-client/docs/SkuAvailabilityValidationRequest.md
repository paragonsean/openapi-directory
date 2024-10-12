# DataBoxManagementClient.SkuAvailabilityValidationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements | 
**deviceType** | **String** | Device type to be used for the job. | 
**location** | **String** | Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version&#x3D;2018-01-01 | 
**transferType** | **String** | Type of the transfer. | 



## Enum: DeviceTypeEnum


* `DataBox` (value: `"DataBox"`)

* `DataBoxDisk` (value: `"DataBoxDisk"`)

* `DataBoxHeavy` (value: `"DataBoxHeavy"`)





## Enum: TransferTypeEnum


* `ImportToAzure` (value: `"ImportToAzure"`)




