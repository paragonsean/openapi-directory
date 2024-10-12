

# UpdateSystemModelsUpdateGroup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the update group |  |
|**ID** | **String** |  |  [optional] |
|**inventoryFrequency** | **Integer** | The time in minutes between inventory checks. Default value is 1440 minutes (one day). |  [optional] |
|**inventoryPackage** | **String** | The Package ID of the package used for inventory |  [optional] |
|**localizedDescription** | **String** | Optional. The StringID used to localize the description of the update group |  [optional] |
|**localizedName** | **String** | Optional. The StringID used to localize the name of the update group |  [optional] |
|**priority** | **Integer** | The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority. |  |
|**reportField** | **String** | A field to return in the status report for this update group.              Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute}) |  [optional] |
|**updateType** | **String** | The update type name |  |
|**validatingField** | **String** | A field used for validation in the status report for this update group.              Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute}) |  [optional] |
|**valueToValidate** | **String** | The value to validate the ValidationField against. |  [optional] |
|**version** | **byte[]** | The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType |  [optional] |



