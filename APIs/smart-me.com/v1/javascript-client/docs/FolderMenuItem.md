# SmartMe.FolderMenuItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoExportSettings** | [**AutoExportSettings**](AutoExportSettings.md) |  | [optional] 
**children** | [**[FolderMenuItem]**](FolderMenuItem.md) | Children folder menu items (sub folder menu items) | [optional] 
**description** | **String** | The Description of the folder | [optional] 
**folderType** | **String** | The folder type of the item | [optional] 
**icon** | **String** | The path to the Icon of this folder | [optional] 
**id** | **String** | The id of the folder menu item | [optional] 
**meterSerialNumber** | **String** | The serial number if the folder menu item is a meter.               Serial number is handled as a string, as javascript on client side cannot handle long integers properly. | [optional] 
**name** | **String** | The Name of the item | [optional] 
**userId** | **String** | The ID of the user of this folder (only for foldertype user) | [optional] 



## Enum: FolderTypeEnum


* `Folder` (value: `"Folder"`)

* `Location` (value: `"Location"`)

* `Factory` (value: `"Factory"`)

* `House` (value: `"House"`)

* `Office` (value: `"Office"`)

* `Machine` (value: `"Machine"`)

* `VirtualMeter` (value: `"VirtualMeter"`)

* `ElecticityFolder` (value: `"ElecticityFolder"`)

* `WaterFolder` (value: `"WaterFolder"`)

* `HeatFolder` (value: `"HeatFolder"`)

* `GasFolder` (value: `"GasFolder"`)

* `TemperatureFolder` (value: `"TemperatureFolder"`)

* `Sun` (value: `"Sun"`)

* `Light` (value: `"Light"`)

* `Ice` (value: `"Ice"`)

* `Sofa` (value: `"Sofa"`)

* `Food` (value: `"Food"`)

* `Coffee` (value: `"Coffee"`)

* `Car` (value: `"Car"`)

* `ChargingStation` (value: `"ChargingStation"`)

* `Meter` (value: `"Meter"`)

* `User` (value: `"User"`)

* `Trash` (value: `"Trash"`)

* `GridPhotovoltaicPowerSystem` (value: `"GridPhotovoltaicPowerSystem"`)




