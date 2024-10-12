# ApicurioRegistryApi.ArtifactRulesApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createArtifactRule**](ArtifactRulesApi.md#createArtifactRule) | **POST** /artifacts/{artifactId}/rules | Create artifact rule
[**deleteArtifactRule**](ArtifactRulesApi.md#deleteArtifactRule) | **DELETE** /artifacts/{artifactId}/rules/{rule} | Delete artifact rule
[**deleteArtifactRules**](ArtifactRulesApi.md#deleteArtifactRules) | **DELETE** /artifacts/{artifactId}/rules | Delete artifact rules
[**getArtifactRuleConfig**](ArtifactRulesApi.md#getArtifactRuleConfig) | **GET** /artifacts/{artifactId}/rules/{rule} | Get artifact rule configuration
[**listArtifactRules**](ArtifactRulesApi.md#listArtifactRules) | **GET** /artifacts/{artifactId}/rules | List artifact rules
[**testUpdateArtifact**](ArtifactRulesApi.md#testUpdateArtifact) | **PUT** /artifacts/{artifactId}/test | Test update artifact
[**updateArtifactRuleConfig**](ArtifactRulesApi.md#updateArtifactRuleConfig) | **PUT** /artifacts/{artifactId}/rules/{rule} | Update artifact rule configuration



## createArtifactRule

> createArtifactRule(artifactId, rule)

Create artifact rule

Adds a rule to the list of rules that get applied to the artifact when adding new versions.  All configured rules must pass to successfully add a new artifact version.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * Rule (named in the request body) is unknown (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactRulesApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let rule = new ApicurioRegistryApi.Rule(); // Rule | 
apiInstance.createArtifactRule(artifactId, rule, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 
 **rule** | [**Rule**](Rule.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteArtifactRule

> deleteArtifactRule(rule, artifactId)

Delete artifact rule

Deletes a rule from the artifact.  This results in the rule no longer applying for this artifact.  If this is the only rule configured for the artifact, this is the  same as deleting **all** rules, and the globally configured rules now apply to this artifact.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No rule with this name/type is configured for this artifact (HTTP error &#x60;404&#x60;) * Invalid rule type (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactRulesApi();
let rule = "rule_example"; // String | The unique name/type of a rule.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.deleteArtifactRule(rule, artifactId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **String**| The unique name/type of a rule. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteArtifactRules

> deleteArtifactRules(artifactId)

Delete artifact rules

Deletes all of the rules configured for the artifact.  After this is done, the global rules apply to the artifact again.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactRulesApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.deleteArtifactRules(artifactId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArtifactRuleConfig

> Rule getArtifactRuleConfig(rule, artifactId)

Get artifact rule configuration

Returns information about a single rule configured for an artifact.  This is useful when you want to know what the current configuration settings are for a specific rule.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No rule with this name/type is configured for this artifact (HTTP error &#x60;404&#x60;) * Invalid rule type (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactRulesApi();
let rule = "rule_example"; // String | The unique name/type of a rule.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.getArtifactRuleConfig(rule, artifactId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **String**| The unique name/type of a rule. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listArtifactRules

> [RuleType] listArtifactRules(artifactId)

List artifact rules

Returns a list of all rules configured for the artifact.  The set of rules determines how the content of an artifact can evolve over time.  If no rules are configured for an artifact, the set of globally configured rules are used.  If no global rules  are defined, there are no restrictions on content evolution.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactRulesApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
apiInstance.listArtifactRules(artifactId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 

### Return type

[**[RuleType]**](RuleType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## testUpdateArtifact

> testUpdateArtifact(artifactId, opts)

Test update artifact

Tests whether an update to the artifact&#39;s content *would* succeed for the provided content. Ultimately, this applies any rules configured for the artifact against the given content to determine whether the rules would pass or fail, but without actually updating the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in  JSON format for *most* of the supported types, but may be in another format for a few  (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following  supported list:   * Avro (&#x60;AVRO&#x60;)   * Protobuf (&#x60;PROTOBUF&#x60;)   * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;)   * JSON Schema (&#x60;JSON&#x60;)   * Kafka Connect (&#x60;KCONNECT&#x60;)  * OpenAPI (&#x60;OPENAPI&#x60;)   * AsyncAPI (&#x60;ASYNCAPI&#x60;)  * GraphQL (&#x60;GRAPHQL&#x60;)  * Web Services Description Language (&#x60;WSDL&#x60;)  * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can explicitly specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or by including a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * The provided artifact type is not recognized (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)  When successful, this operation simply returns a *No Content* response.

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactRulesApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let opts = {
  'xRegistryArtifactType': "xRegistryArtifactType_example" // String | This header parameter can be used to indicate the type of the artifact being added.  Possible values include:  * Avro (`AVRO`)   * Protobuf (`PROTOBUF`)   * Protobuf File Descriptor (`PROTOBUF_FD`)   * JSON Schema (`JSON`)   * Kafka Connect (`KCONNECT`)   * OpenAPI (`OPENAPI`)   * AsyncAPI (`ASYNCAPI`)  * GraphQL (`GRAPHQL`)   * Web Services Description Language (`WSDL`)   * XML Schema (`XSD`)
};
apiInstance.testUpdateArtifact(artifactId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 
 **xRegistryArtifactType** | **String**| This header parameter can be used to indicate the type of the artifact being added.  Possible values include:  * Avro (&#x60;AVRO&#x60;)   * Protobuf (&#x60;PROTOBUF&#x60;)   * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;)   * JSON Schema (&#x60;JSON&#x60;)   * Kafka Connect (&#x60;KCONNECT&#x60;)   * OpenAPI (&#x60;OPENAPI&#x60;)   * AsyncAPI (&#x60;ASYNCAPI&#x60;)  * GraphQL (&#x60;GRAPHQL&#x60;)   * Web Services Description Language (&#x60;WSDL&#x60;)   * XML Schema (&#x60;XSD&#x60;) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateArtifactRuleConfig

> Rule updateArtifactRuleConfig(rule, artifactId, rule2)

Update artifact rule configuration

Updates the configuration of a single rule for the artifact.  The configuration data is specific to each rule type, so the configuration of the &#x60;COMPATIBILITY&#x60; rule  is in a different format from the configuration of the &#x60;VALIDITY&#x60; rule.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No rule with this name/type is configured for this artifact (HTTP error &#x60;404&#x60;) * Invalid rule type (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.ArtifactRulesApi();
let rule = "rule_example"; // String | The unique name/type of a rule.
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let rule2 = new ApicurioRegistryApi.Rule(); // Rule | 
apiInstance.updateArtifactRuleConfig(rule, artifactId, rule2, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **String**| The unique name/type of a rule. | 
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 
 **rule2** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

