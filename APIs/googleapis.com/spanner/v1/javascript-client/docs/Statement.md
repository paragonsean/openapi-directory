# CloudSpannerApi.Statement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paramTypes** | [**{String: Type}**](Type.md) | It is not always possible for Cloud Spanner to infer the right SQL type from a JSON value. For example, values of type &#x60;BYTES&#x60; and values of type &#x60;STRING&#x60; both appear in params as JSON strings. In these cases, &#x60;param_types&#x60; can be used to specify the exact SQL type for some or all of the SQL statement parameters. See the definition of Type for more information about SQL types. | [optional] 
**params** | **{String: Object}** | Parameter names and values that bind to placeholders in the DML string. A parameter placeholder consists of the &#x60;@&#x60; character followed by the parameter name (for example, &#x60;@firstName&#x60;). Parameter names can contain letters, numbers, and underscores. Parameters can appear anywhere that a literal value is expected. The same parameter name can be used more than once, for example: &#x60;\&quot;WHERE id &gt; @msg_id AND id &lt; @msg_id + 100\&quot;&#x60; It is an error to execute a SQL statement with unbound parameters. | [optional] 
**sql** | **String** | Required. The DML string. | [optional] 


