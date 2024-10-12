# CloudFirestoreApi.GoogleFirestoreAdminV1Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexConfig** | [**GoogleFirestoreAdminV1IndexConfig**](GoogleFirestoreAdminV1IndexConfig.md) |  | [optional] 
**name** | **String** | Required. A field name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}&#x60; A field path may be a simple field name, e.g. &#x60;address&#x60; or a path to fields within map_value , e.g. &#x60;address.city&#x60;, or a special field path. The only valid special field is &#x60;*&#x60;, which represents any field. Field paths may be quoted using &#x60; (backtick). The only character that needs to be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include: &#x60;*&#x60;, &#x60;.&#x60;, &#x60;&#x60;&#x60; (backtick), &#x60;[&#x60;, &#x60;]&#x60;, as well as any ascii symbolic characters. Examples: (Note: Comments here are written in markdown syntax, so there is an additional layer of backticks to represent a code block) &#x60;\\&#x60;address.city\\&#x60;&#x60; represents a field named &#x60;address.city&#x60;, not the map key &#x60;city&#x60; in the field &#x60;address&#x60;. &#x60;\\&#x60;*\\&#x60;&#x60; represents a field named &#x60;*&#x60;, not any field. A special &#x60;Field&#x60; contains the default indexing settings for all fields. This field&#39;s resource name is: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/_*&#x60; Indexes defined on this &#x60;Field&#x60; will be applied to all fields which do not have their own &#x60;Field&#x60; index configuration. | [optional] 
**ttlConfig** | [**GoogleFirestoreAdminV1TtlConfig**](GoogleFirestoreAdminV1TtlConfig.md) |  | [optional] 


