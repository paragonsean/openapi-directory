

# FolderMenuItem

A folder menu item

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoExportSettings** | [**AutoExportSettings**](AutoExportSettings.md) |  |  [optional] |
|**children** | [**List&lt;FolderMenuItem&gt;**](FolderMenuItem.md) | Children folder menu items (sub folder menu items) |  [optional] |
|**description** | **String** | The Description of the folder |  [optional] |
|**folderType** | [**FolderTypeEnum**](#FolderTypeEnum) | The folder type of the item |  [optional] |
|**icon** | **String** | The path to the Icon of this folder |  [optional] |
|**id** | **String** | The id of the folder menu item |  [optional] |
|**meterSerialNumber** | **String** | The serial number if the folder menu item is a meter.               Serial number is handled as a string, as javascript on client side cannot handle long integers properly. |  [optional] |
|**name** | **String** | The Name of the item |  [optional] |
|**userId** | **String** | The ID of the user of this folder (only for foldertype user) |  [optional] |



## Enum: FolderTypeEnum

| Name | Value |
|---- | -----|
| FOLDER | &quot;Folder&quot; |
| LOCATION | &quot;Location&quot; |
| FACTORY | &quot;Factory&quot; |
| HOUSE | &quot;House&quot; |
| OFFICE | &quot;Office&quot; |
| MACHINE | &quot;Machine&quot; |
| VIRTUAL_METER | &quot;VirtualMeter&quot; |
| ELECTICITY_FOLDER | &quot;ElecticityFolder&quot; |
| WATER_FOLDER | &quot;WaterFolder&quot; |
| HEAT_FOLDER | &quot;HeatFolder&quot; |
| GAS_FOLDER | &quot;GasFolder&quot; |
| TEMPERATURE_FOLDER | &quot;TemperatureFolder&quot; |
| SUN | &quot;Sun&quot; |
| LIGHT | &quot;Light&quot; |
| ICE | &quot;Ice&quot; |
| SOFA | &quot;Sofa&quot; |
| FOOD | &quot;Food&quot; |
| COFFEE | &quot;Coffee&quot; |
| CAR | &quot;Car&quot; |
| CHARGING_STATION | &quot;ChargingStation&quot; |
| METER | &quot;Meter&quot; |
| USER | &quot;User&quot; |
| TRASH | &quot;Trash&quot; |
| GRID_PHOTOVOLTAIC_POWER_SYSTEM | &quot;GridPhotovoltaicPowerSystem&quot; |



