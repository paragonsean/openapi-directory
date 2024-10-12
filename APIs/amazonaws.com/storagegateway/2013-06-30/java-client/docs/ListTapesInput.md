

# ListTapesInput

<p>A JSON object that contains one or more of the following fields:</p> <ul> <li> <p> <a>ListTapesInput$Limit</a> </p> </li> <li> <p> <a>ListTapesInput$Marker</a> </p> </li> <li> <p> <a>ListTapesInput$TapeARNs</a> </p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tapeARNs** | **List&lt;String&gt;** | The Amazon Resource Name (ARN) of each of the tapes you want to list. If you don&#39;t specify a tape ARN, the response lists all tapes in both your VTL and VTS. |  [optional] |
|**marker** | [**String**](String.md) |  |  [optional] |
|**limit** | [**Integer**](Integer.md) |  |  [optional] |



