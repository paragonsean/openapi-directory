

# FolderSettings

Container for the folder settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The Description of the folder or meter |  [optional] |
|**enable** | **Boolean** | Flag if the meter is enabled (folder not supported yet) |  [optional] |
|**folderType** | [**FolderTypeEnum**](#FolderTypeEnum) | The Type of the folder |  [optional] |
|**name** | **String** | The Name of the folder or meter |  [optional] |
|**parentFolderId** | **String** | The parent folder ID of this item |  [optional] |
|**serialNumber** | **Long** | The serial number (meter only) |  [optional] |
|**useableForVirtualBillingMeters** | **Boolean** | Flag if the meter is usable for virtual billing meters (e.g. washroom) |  [optional] |
|**valueCorrection** | **Double** | The value correction on this meter |  [optional] |
|**valueCorrectionParentFolder** | **Double** | The value correction on all parent folders. but not on the meter itself |  [optional] |
|**visualizationName** | **String** | The name of the visualization of the folder |  [optional] |



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



