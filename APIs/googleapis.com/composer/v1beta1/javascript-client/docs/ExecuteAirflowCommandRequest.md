# CloudComposerApi.ExecuteAirflowCommandRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **String** | Airflow command. | [optional] 
**parameters** | **[String]** | Parameters for the Airflow command/subcommand as an array of arguments. It may contain positional arguments like &#x60;[\&quot;my-dag-id\&quot;]&#x60;, key-value parameters like &#x60;[\&quot;--foo&#x3D;bar\&quot;]&#x60; or &#x60;[\&quot;--foo\&quot;,\&quot;bar\&quot;]&#x60;, or other flags like &#x60;[\&quot;-f\&quot;]&#x60;. | [optional] 
**subcommand** | **String** | Airflow subcommand. | [optional] 


