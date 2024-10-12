# RubrikRestApi.RestoreFileJobConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainName** | **String** | Domain name (Use . for local admin). | [optional] 
**ignoreErrors** | **Boolean** | Optional Boolean field to determine whether to ignore errors during restore jobs that use the Rubrik Backup Service. When &#39;true&#39;, errors are ignored. Default value is &#39;false&#39;, errors are not ignored. | [optional] [default to false]
**password** | **String** | Password. | [optional] 
**path** | **String** | Absolute file path. | 
**restorePath** | **String** | Directory of folder to copy files into. | 
**shouldRestoreXAttrs** | **Boolean** | Boolean value that determines restore file settings for Linux systems and for Windows systems. For Linux, use &#39;true&#39; to include the extended attributes of restored files. For Window, use &#39;true&#39; to include alternate data streams for restored files. For both, use &#39;false&#39; to exclude this additional metadata. | [optional] 
**shouldSaveCredentials** | **Boolean** | A Boolean value that specifies whether to save the user-entered credentials. When &#39;true&#39;, the user-entered credentials are saved. | [optional] 
**shouldUseAgent** | **Boolean** | A Boolean that specifies whether to use the Rubrik Backup Service or VMware tools to restore file. When &#39;true&#39;, the RBS restores file. When &#39;false&#39;, the VMware tools restores file. | [optional] [default to true]
**username** | **String** | Username. | [optional] 


