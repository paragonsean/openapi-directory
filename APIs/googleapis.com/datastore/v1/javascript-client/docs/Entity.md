# CloudDatastoreApi.Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**Key**](Key.md) |  | [optional] 
**properties** | [**{String: Value}**](Value.md) | The entity&#39;s properties. The map&#39;s keys are property names. A property name matching regex &#x60;__.*__&#x60; is reserved. A reserved property name is forbidden in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. | [optional] 


