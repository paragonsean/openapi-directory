

# TextModuleData

Data for Text module. All fields are optional. Header will be displayed if available, different types of bodies will be concatenated if they are defined.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | The body of the Text Module, which is defined as an uninterrupted string. Recommended maximum length is 500 characters to ensure full string is displayed on smaller screens. |  [optional] |
|**header** | **String** | The header of the Text Module. Recommended maximum length is 35 characters to ensure full string is displayed on smaller screens. |  [optional] |
|**id** | **String** | The ID associated with a text module. This field is here to enable ease of management of text modules. |  [optional] |
|**localizedBody** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**localizedHeader** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |



