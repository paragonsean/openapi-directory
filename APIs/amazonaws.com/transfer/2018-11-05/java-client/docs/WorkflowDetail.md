

# WorkflowDetail

<p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workflowId** | [**String**](String.md) |  |  |
|**executionRole** | [**String**](String.md) |  |  |



