

# QueryFilter

<p>A structure that defines a key and values that you can use to filter the results. The only performance events that are returned are those that have values matching the ones that you specify in one of your <code>QueryFilter</code> structures.</p> <p>For example, you could specify <code>Browser</code> as the <code>Name</code> and specify <code>Chrome,Firefox</code> as the <code>Values</code> to return events generated only from those browsers.</p> <p>Specifying <code>Invert</code> as the <code>Name</code> works as a \"not equal to\" filter. For example, specify <code>Invert</code> as the <code>Name</code> and specify <code>Chrome</code> as the value to return all events except events from user sessions with the Chrome browser.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**values** | [**List**](List.md) |  |  [optional] |



