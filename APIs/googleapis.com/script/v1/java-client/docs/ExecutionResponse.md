

# ExecutionResponse

An object that provides the return value of a function executed using the Apps Script API. If the script function returns successfully, the response body's response field contains this `ExecutionResponse` object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**result** | **Object** | The return value of the script function. The type matches the object type returned in Apps Script. Functions called using the Apps Script API cannot return Apps Script-specific objects (such as a &#x60;Document&#x60; or a &#x60;Calendar&#x60;); they can only return primitive types such as a &#x60;string&#x60;, &#x60;number&#x60;, &#x60;array&#x60;, &#x60;object&#x60;, or &#x60;boolean&#x60;. |  [optional] |



