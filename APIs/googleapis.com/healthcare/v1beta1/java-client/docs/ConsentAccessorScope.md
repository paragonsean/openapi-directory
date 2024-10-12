

# ConsentAccessorScope

The accessor scope that describes who can access, for what purpose, in which environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actor** | **String** | An individual, group, or access role that identifies the accessor or a characteristic of the accessor. This can be a resource ID (such as &#x60;{resourceType}/{id}&#x60;) or an external URI. This value must be present. |  [optional] |
|**environment** | **String** | An abstract identifier that describes the environment or conditions under which the accessor is acting. Can be “*” if it applies to all environments. |  [optional] |
|**purpose** | **String** | The intent of data use. Can be “*” if it applies to all purposes. |  [optional] |



