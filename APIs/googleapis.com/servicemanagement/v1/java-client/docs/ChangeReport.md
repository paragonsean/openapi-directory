

# ChangeReport

Change report associated with a particular service configuration. It contains a list of ConfigChanges based on the comparison between two service configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configChanges** | [**List&lt;ConfigChange&gt;**](ConfigChange.md) | List of changes between two service configurations. The changes will be alphabetically sorted based on the identifier of each change. A ConfigChange identifier is a dot separated path to the configuration. Example: visibility.rules[selector&#x3D;&#39;LibraryService.CreateBook&#39;].restriction |  [optional] |



