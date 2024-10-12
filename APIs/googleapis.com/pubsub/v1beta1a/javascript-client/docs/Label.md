# CloudPubSubApi.Label

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | The key of a label is a syntactically valid URL (as per RFC 1738) with the \&quot;scheme\&quot; and initial slashes omitted and with the additional restrictions noted below. Each key should be globally unique. The \&quot;host\&quot; portion is called the \&quot;namespace\&quot; and is not necessarily resolvable to a network endpoint. Instead, the namespace indicates what system or entity defines the semantics of the label. Namespaces do not restrict the set of objects to which a label may be associated. Keys are defined by the following grammar: key &#x3D; hostname \&quot;/\&quot; kpath kpath &#x3D; ksegment *[ \&quot;/\&quot; ksegment ] ksegment &#x3D; alphadigit | *[ alphadigit | \&quot;-\&quot; | \&quot;_\&quot; | \&quot;.\&quot; ] where \&quot;hostname\&quot; and \&quot;alphadigit\&quot; are defined as in RFC 1738. Example key: spanner.google.com/universe | [optional] 
**numValue** | **String** | An integer value. | [optional] 
**strValue** | **String** | A string value. | [optional] 


