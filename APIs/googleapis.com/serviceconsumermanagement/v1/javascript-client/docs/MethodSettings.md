# ServiceConsumerManagementApi.MethodSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoPopulatedFields** | **[String]** | List of top-level fields of the request message, that should be automatically populated by the client libraries based on their (google.api.field_info).format. Currently supported format: UUID4. Example of a YAML configuration: publishing: method_settings: - selector: google.example.v1.ExampleService.CreateExample auto_populated_fields: - request_id | [optional] 
**longRunning** | [**LongRunning**](LongRunning.md) |  | [optional] 
**selector** | **String** | The fully qualified name of the method, for which the options below apply. This is used to find the method to apply the options. | [optional] 


