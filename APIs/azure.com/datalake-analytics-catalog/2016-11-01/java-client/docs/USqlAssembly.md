

# USqlAssembly

A Data Lake Analytics catalog U-SQL Assembly.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assemblyName** | **String** | the name of the assembly. |  [optional] |
|**clrName** | **String** | the name of the CLR. |  [optional] |
|**databaseName** | **String** | the name of the database. |  [optional] |
|**dependencies** | [**List&lt;USqlAssemblyDependencyInfo&gt;**](USqlAssemblyDependencyInfo.md) | the list of dependencies associated with the assembly |  [optional] |
|**files** | [**List&lt;USqlAssemblyFileInfo&gt;**](USqlAssemblyFileInfo.md) | the list of files associated with the assembly |  [optional] |
|**isUserDefined** | **Boolean** | the switch indicating if this assembly is user defined or not. |  [optional] |
|**isVisible** | **Boolean** | the switch indicating if this assembly is visible or not. |  [optional] |
|**computeAccountName** | **String** | the name of the Data Lake Analytics account. |  [optional] |
|**version** | **UUID** | the version of the catalog item. |  [optional] |



