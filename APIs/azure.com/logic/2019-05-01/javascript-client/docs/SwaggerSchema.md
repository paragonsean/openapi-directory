# LogicManagementClient.SwaggerSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalProperties** | **Object** |  | [optional] 
**allOf** | [**[SwaggerSchema]**](SwaggerSchema.md) | The schemas which must pass validation when this schema is used. | [optional] 
**discriminator** | **String** | The discriminator. | [optional] 
**dynamicListNew** | [**SwaggerCustomDynamicList**](SwaggerCustomDynamicList.md) |  | [optional] 
**dynamicSchemaNew** | [**SwaggerCustomDynamicProperties**](SwaggerCustomDynamicProperties.md) |  | [optional] 
**dynamicSchemaOld** | [**SwaggerCustomDynamicSchema**](SwaggerCustomDynamicSchema.md) |  | [optional] 
**dynamicTree** | [**SwaggerCustomDynamicTree**](SwaggerCustomDynamicTree.md) |  | [optional] 
**example** | **Object** |  | [optional] 
**externalDocs** | [**SwaggerExternalDocumentation**](SwaggerExternalDocumentation.md) |  | [optional] 
**items** | [**SwaggerSchema**](SwaggerSchema.md) |  | [optional] 
**maxProperties** | **Number** | The maximum number of allowed properties. | [optional] 
**minProperties** | **Number** | The minimum number of allowed properties. | [optional] 
**notificationUrlExtension** | **Boolean** | Indicates the notification url extension. If this is set, the property&#39;s value should be a callback url for a webhook. | [optional] 
**properties** | [**{String: SwaggerSchema}**](SwaggerSchema.md) | The object properties | [optional] 
**readOnly** | **Boolean** | Indicates whether this property must be present in the a request. | [optional] 
**ref** | **String** | The reference. | [optional] 
**required** | **[String]** | The object required properties. | [optional] 
**title** | **String** | The title. | [optional] 
**type** | [**SwaggerSchemaType**](SwaggerSchemaType.md) |  | [optional] 
**xml** | [**SwaggerXml**](SwaggerXml.md) |  | [optional] 


