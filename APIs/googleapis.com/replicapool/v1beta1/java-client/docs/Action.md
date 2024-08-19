

# Action

An action that gets executed during initialization of the replicas.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commands** | **List&lt;String&gt;** | A list of commands to run, one per line. If any command fails, the whole action is considered a failure and no further actions are run. This also marks the virtual machine or replica as a failure. |  [optional] |
|**envVariables** | [**List&lt;EnvVariable&gt;**](EnvVariable.md) | A list of environment variables to use for the commands in this action. |  [optional] |
|**timeoutMilliSeconds** | **Integer** | If an action&#39;s commands on a particular replica do not finish in the specified timeoutMilliSeconds, the replica is considered to be in a FAILING state. No efforts are made to stop any processes that were spawned or created as the result of running the action&#39;s commands. The default is the max allowed value, 1 hour (i.e. 3600000 milliseconds). |  [optional] |



