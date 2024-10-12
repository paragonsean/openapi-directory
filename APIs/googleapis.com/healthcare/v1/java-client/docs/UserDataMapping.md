

# UserDataMapping

Maps a resource to the associated user and Attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveTime** | **String** | Output only. Indicates the time when this mapping was archived. |  [optional] [readonly] |
|**archived** | **Boolean** | Output only. Indicates whether this mapping is archived. |  [optional] [readonly] |
|**dataId** | **String** | Required. A unique identifier for the mapped resource. |  [optional] |
|**name** | **String** | Resource name of the User data mapping, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}&#x60;. |  [optional] |
|**resourceAttributes** | [**List&lt;Attribute&gt;**](Attribute.md) | Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field \&quot;values\&quot; in each Attribute. |  [optional] |
|**userId** | **String** | Required. User&#39;s UUID provided by the client. |  [optional] |



