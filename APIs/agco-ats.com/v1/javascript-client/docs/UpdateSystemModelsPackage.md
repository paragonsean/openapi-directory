# AgcoApi.UpdateSystemModelsPackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autorun** | **Boolean** | Value is true if package should run automatically. Default value is false. | [optional] 
**CRC** | **String** | The CRC used to validate the download. | 
**description** | **String** | The package description | 
**localizedName** | **String** | Optional. The StringID used to localize the name of the Package | [optional] 
**notes** | **String** | Notes about the package | [optional] 
**packageID** | **String** | Read Only. The package ID | [optional] 
**packageTypeID** | **String** | The id of the package type this package belongs to. | 
**previousVersion** | **Number** | For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0. | [optional] 
**releaseDate** | **Date** | The date the package was released | 
**released** | **Boolean** | True if the package is released.  Default value is False. | [optional] 
**removeOnSuccess** | **Boolean** | True to remove the package after successful execution.  Default value is False. | [optional] 
**size** | **Number** | The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.              If the size provided does not match the size in the response from the URL an error will be returned. | [optional] 
**switches** | **String** | The command line arguments for the package.  Default value is an empty string. | [optional] 
**url** | **String** | The Url to download the package from. | 
**version** | **Number** | The version. | 


