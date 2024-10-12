# ServiceManagementApi.DotnetSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common** | [**CommonLanguageSettings**](CommonLanguageSettings.md) |  | [optional] 
**forcedNamespaceAliases** | **[String]** | Namespaces which must be aliased in snippets due to a known (but non-generator-predictable) naming collision | [optional] 
**handwrittenSignatures** | **[String]** | Method signatures (in the form \&quot;service.method(signature)\&quot;) which are provided separately, so shouldn&#39;t be generated. Snippets *calling* these methods are still generated, however. | [optional] 
**ignoredResources** | **[String]** | List of full resource types to ignore during generation. This is typically used for API-specific Location resources, which should be handled by the generator as if they were actually the common Location resources. Example entry: \&quot;documentai.googleapis.com/Location\&quot; | [optional] 
**renamedResources** | **{String: String}** | Map from full resource types to the effective short name for the resource. This is used when otherwise resource named from different services would cause naming collisions. Example entry: \&quot;datalabeling.googleapis.com/Dataset\&quot;: \&quot;DataLabelingDataset\&quot; | [optional] 
**renamedServices** | **{String: String}** | Map from original service names to renamed versions. This is used when the default generated types would cause a naming conflict. (Neither name is fully-qualified.) Example: Subscriber to SubscriberServiceApi. | [optional] 


