# CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1Version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **{String: Object}** | Output only. The asset which has been validated and is ready to be provisioned. See Version.original_asset for the schema. | [optional] 
**createTime** | **String** | Output only. The time when the version was created. | [optional] 
**description** | **String** | The user-supplied description of the version. Maximum of 256 characters. | [optional] 
**name** | **String** | Required. The resource name of the version, in the format &#x60;catalogs/{catalog_id}/products/{product_id}/versions/a-z*[a-z0-9]&#39;.  A unique identifier for the version under a product, which can&#39;t be changed after the version is created. The final segment of the name must between 1 and 63 characters in length. | [optional] 
**originalAsset** | **{String: Object}** | The user-supplied asset payload. The maximum size of the payload is 2MB. The JSON schema of the payload is defined as:  &#x60;&#x60;&#x60; type: object properties:   mainTemplate:     type: string     description: The file name of the main template and name prefix of     schema file. The content of the main template should be set in the     imports list. The schema file name is expected to be     &lt;mainTemplate&gt;.schema in the imports list. required: true   imports:     type: array     description: Import template and schema file contents. Required to have     both &lt;mainTemplate&gt; and &lt;mainTemplate&gt;.schema files. required: true     minItems: 2     items:       type: object       properties:         name:           type: string         content:           type: string &#x60;&#x60;&#x60; | [optional] 
**updateTime** | **String** | Output only. The time when the version was last updated. | [optional] 


