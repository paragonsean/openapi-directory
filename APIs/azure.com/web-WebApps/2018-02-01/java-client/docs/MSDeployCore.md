

# MSDeployCore

MSDeploy ARM PUT core information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appOffline** | **Boolean** | Sets the AppOffline rule while the MSDeploy operation executes. Setting is &lt;code&gt;false&lt;/code&gt; by default. |  [optional] |
|**connectionString** | **String** | SQL Connection String |  [optional] |
|**dbType** | **String** | Database Type |  [optional] |
|**packageUri** | **String** | Package URI |  [optional] |
|**setParameters** | **Map&lt;String, String&gt;** | MSDeploy Parameters. Must not be set if SetParametersXmlFileUri is used. |  [optional] |
|**setParametersXmlFileUri** | **String** | URI of MSDeploy Parameters file. Must not be set if SetParameters is used. |  [optional] |
|**skipAppData** | **Boolean** | Controls whether the MSDeploy operation skips the App_Data directory. If set to &lt;code&gt;true&lt;/code&gt;, the existing App_Data directory on the destination will not be deleted, and any App_Data directory in the source will be ignored. Setting is &lt;code&gt;false&lt;/code&gt; by default. |  [optional] |



