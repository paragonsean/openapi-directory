

# ServiceClass

The ServiceClass resource. Next id: 9

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time when the ServiceClass was created. |  [optional] [readonly] |
|**description** | **String** | A description of this resource. |  [optional] |
|**etag** | **String** | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels. |  [optional] |
|**name** | **String** | Immutable. The name of a ServiceClass resource. Format: projects/{project}/locations/{location}/serviceClasses/{service_class} See: https://google.aip.dev/122#fields-representing-resource-names |  [optional] |
|**serviceClass** | **String** | Output only. The generated service class name. Use this name to refer to the Service class in Service Connection Maps and Service Connection Policies. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when the ServiceClass was updated. |  [optional] [readonly] |



