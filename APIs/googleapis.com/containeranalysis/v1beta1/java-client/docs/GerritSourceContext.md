

# GerritSourceContext

A SourceContext referring to a Gerrit project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aliasContext** | [**AliasContext**](AliasContext.md) |  |  [optional] |
|**gerritProject** | **String** | The full project name within the host. Projects may be nested, so \&quot;project/subproject\&quot; is a valid project name. The \&quot;repo name\&quot; is the hostURI/project. |  [optional] |
|**hostUri** | **String** | The URI of a running Gerrit instance. |  [optional] |
|**revisionId** | **String** | A revision (commit) ID. |  [optional] |



