# AgcoApi.UpdateSystemModelsPackageType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **String** | The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed. | [optional] 
**category** | **String** | The inventory category (from the InventoryPackage) used to determine what version of this package type is installed. | [optional] 
**description** | **String** | The description of the package type | 
**icon** | **String** | Optional.  The icon to use for the PackageType, in base 64 | [optional] 
**inventoryFrequency** | **Number** | The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours). | [optional] 
**inventoryPackage** | **String** | The inventory package used to determine what version of this package type is installed. | [optional] 
**localizedDescription** | **String** | Optional. The StringID used to localize the description of the PackageType | [optional] 
**localizedName** | **String** | Optional. The StringID used to localize the name of the PackageType | [optional] 
**maxDeltaPackages** | **Number** | The maximum number of \&quot;chained\&quot; delta packages to use when updating the client | [optional] 
**packageTypeID** | **String** | Read Only. The package type id. | [optional] 


