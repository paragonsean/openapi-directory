

# ClientScriptForConnect

Client script details for file / folder restore.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**osType** | **String** | OS type - Windows, Linux etc. for which this file / folder restore client script works. |  [optional] |
|**scriptContent** | **String** | File content of the client script for file / folder restore. |  [optional] |
|**scriptExtension** | **String** | File extension of the client script for file / folder restore - .ps1 , .sh , etc. |  [optional] |
|**scriptNameSuffix** | **String** | Mandatory suffix that should be added to the name of script that is given for download to user.  If its null or empty then , ignore it. |  [optional] |
|**url** | **String** | URL of Executable from where to source the content. If this is not null then ScriptContent should not be used |  [optional] |



