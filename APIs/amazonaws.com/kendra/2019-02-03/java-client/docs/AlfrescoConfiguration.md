

# AlfrescoConfiguration

<p>Provides the configuration information to connect to Alfresco as your data source.</p> <note> <p>Support for <code>AlfrescoConfiguration</code> ended May 2023. We recommend migrating to or using the Alfresco data source template schema / <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html\">TemplateConfiguration</a> API.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**siteUrl** | [**String**](String.md) |  |  |
|**siteId** | [**String**](String.md) |  |  |
|**secretArn** | [**String**](String.md) |  |  |
|**sslCertificateS3Path** | [**AlfrescoConfigurationSslCertificateS3Path**](AlfrescoConfigurationSslCertificateS3Path.md) |  |  |
|**crawlSystemFolders** | [**Boolean**](Boolean.md) |  |  [optional] |
|**crawlComments** | [**Boolean**](Boolean.md) |  |  [optional] |
|**entityFilter** | [**List**](List.md) |  |  [optional] |
|**documentLibraryFieldMappings** | [**List**](List.md) |  |  [optional] |
|**blogFieldMappings** | [**List**](List.md) |  |  [optional] |
|**wikiFieldMappings** | [**List**](List.md) |  |  [optional] |
|**inclusionPatterns** | [**List**](List.md) |  |  [optional] |
|**exclusionPatterns** | [**List**](List.md) |  |  [optional] |
|**vpcConfiguration** | [**AlfrescoConfigurationVpcConfiguration**](AlfrescoConfigurationVpcConfiguration.md) |  |  [optional] |



