

# Operation

An Operation of a Service or API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindings** | [**Map&lt;String, Binding&gt;**](Binding.md) | Map of protocol binding details for this operation |  [optional] |
|**defaultDelay** | **BigDecimal** | Default response time delay for mocks |  [optional] |
|**dispatcher** | **String** | Dispatcher strategy used for mocks |  [optional] |
|**dispatcherRules** | **String** | DispatcherRules used for mocks |  [optional] |
|**inputName** | **String** | Name of input parameters in case of Xml based Service |  [optional] |
|**method** | **String** | Represents transport method |  |
|**name** | **String** | Unique name of this Operation within Service scope |  |
|**outputName** | **String** | Name of output parameters in case of Xml based Service |  [optional] |
|**parameterContraints** | [**List&lt;ParameterConstraint&gt;**](ParameterConstraint.md) | Contraints that may apply to mock invocatino on this operation |  [optional] |
|**resourcePaths** | **List&lt;String&gt;** | Paths the mocks endpoints are mapped on |  [optional] |



