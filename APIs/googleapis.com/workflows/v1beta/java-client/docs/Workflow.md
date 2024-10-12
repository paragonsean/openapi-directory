

# Workflow

Workflow program to be executed by Workflows.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp of when the workflow was created. |  [optional] [readonly] |
|**description** | **String** | Description of the workflow provided by the user. Must be at most 1000 unicode characters long. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels associated with this workflow. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores and dashes. Label keys must start with a letter. International characters are allowed. |  [optional] |
|**name** | **String** | The resource name of the workflow. Format: projects/{project}/locations/{location}/workflows/{workflow} |  [optional] |
|**revisionCreateTime** | **String** | Output only. The timestamp that the latest revision of the workflow was created. |  [optional] [readonly] |
|**revisionId** | **String** | Output only. The revision of the workflow. A new revision of a workflow is created as a result of updating the following properties of a workflow: - Service account - Workflow code to be executed The format is \&quot;000001-a4d\&quot;, where the first 6 characters define the zero-padded revision ordinal number. They are followed by a hyphen and 3 hexadecimal random characters. |  [optional] [readonly] |
|**serviceAccount** | **String** | The service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. Format: projects/{project}/serviceAccounts/{account} or {account} Using &#x60;-&#x60; as a wildcard for the &#x60;{project}&#x60; or not providing one at all will infer the project from the account. The &#x60;{account}&#x60; value can be the &#x60;email&#x60; address or the &#x60;unique_id&#x60; of the service account. If not provided, workflow will use the project&#39;s default service account. Modifying this field for an existing workflow results in a new workflow revision. |  [optional] |
|**sourceContents** | **String** | Workflow code to be executed. The size limit is 128KB. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the workflow deployment. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The last update timestamp of the workflow. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



