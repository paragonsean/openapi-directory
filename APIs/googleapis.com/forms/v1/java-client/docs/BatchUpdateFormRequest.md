

# BatchUpdateFormRequest

A batch of updates to perform on a form. All the specified updates are made or none of them are.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeFormInResponse** | **Boolean** | Whether to return an updated version of the model in the response. |  [optional] |
|**requests** | [**List&lt;Request&gt;**](Request.md) | Required. The update requests of this batch. |  [optional] |
|**writeControl** | [**WriteControl**](WriteControl.md) |  |  [optional] |



