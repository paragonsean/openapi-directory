

# DataRepositoryConfiguration

<p>The data repository configuration object for Lustre file systems returned in the response of the <code>CreateFileSystem</code> operation.</p> <p>This data type is not supported on file systems with a data repository association. For file systems with a data repository association, see .</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lifecycle** | [**DataRepositoryLifecycle**](DataRepositoryLifecycle.md) |  |  [optional] |
|**importPath** | [**String**](String.md) |  |  [optional] |
|**exportPath** | [**String**](String.md) |  |  [optional] |
|**importedFileChunkSize** | [**Integer**](Integer.md) |  |  [optional] |
|**autoImportPolicy** | [**AutoImportPolicyType**](AutoImportPolicyType.md) |  |  [optional] |
|**failureDetails** | [**DataRepositoryFailureDetails**](DataRepositoryFailureDetails.md) |  |  [optional] |



