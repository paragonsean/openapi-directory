

# Environment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auth** | **String** |  |  [optional] |
|**clientCertificate** | **String** |  |  [optional] |
|**emails** | **Object** |  |  [optional] |
|**exportedAt** | **Integer** |  |  [optional] |
|**headers** | **Object** |  |  [optional] |
|**id** | **String** | The unique identifier for this environment. |  [optional] |
|**initialScriptHash** | **String** |  |  [optional] |
|**initialVariables** | **Object** |  |  [optional] |
|**integrations** | [**List&lt;Integration&gt;**](Integration.md) | The list of integrations for this environment. |  [optional] |
|**name** | **String** | Name of this environment. |  |
|**parentEnvironmentId** | **String** |  |  [optional] |
|**preserveCookies** | **Boolean** |  |  [optional] |
|**regions** | **List&lt;String&gt;** | An array of the region codes that this environment is using. |  [optional] |
|**remoteAgents** | [**List&lt;Agent&gt;**](Agent.md) |  |  [optional] |
|**retryOnFailure** | **Boolean** |  |  [optional] |
|**script** | **String** |  |  [optional] |
|**scriptLibrary** | **List&lt;String&gt;** | The list of ids for scripts, part of the script libraries, being used for this environment. |  [optional] |
|**stopOnFailure** | **Boolean** | Stop executing the test after the first failed step. |  [optional] |
|**testId** | **String** | The unique identifier for this test. |  [optional] |
|**verifySsl** | **Boolean** | Validate all SSL certificates on any HTTPS connections. |  [optional] |
|**version** | **String** |  |  [optional] |
|**webhooks** | **String** |  |  [optional] |



