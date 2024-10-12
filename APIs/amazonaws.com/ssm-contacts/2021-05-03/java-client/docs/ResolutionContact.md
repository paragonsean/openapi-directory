

# ResolutionContact

<p>Information about the engagement resolution steps. The resolution starts from the first contact, which can be an escalation plan, then resolves to an on-call rotation, and finally to a personal contact.</p> <p>The <code>ResolutionContact</code> structure describes the information for each node or step in that process. It contains information about different contact types, such as the escalation, rotation, and personal contacts.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactArn** | [**String**](String.md) |  |  |
|**type** | [**ContactType**](ContactType.md) |  |  |
|**stageIndex** | [**Integer**](Integer.md) |  |  [optional] |



