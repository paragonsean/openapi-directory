

# ImageSelector

A set of selection criteria to match an image by a tagged pullstring based on its components, with regex support in each field

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**registry** | **String** | The registry section of a pull string. e.g. with \&quot;docker.io/anchore/anchore-engine:latest\&quot;, this is \&quot;docker.io\&quot; |  [optional] |
|**repository** | **String** | The repository section of a pull string. e.g. with \&quot;docker.io/anchore/anchore-engine:latest\&quot;, this is \&quot;anchore/anchore-engine\&quot; |  [optional] |
|**tag** | **String** | The tag-only section of a pull string. e.g. with \&quot;docker.io/anchore/anchore-engine:latest\&quot;, this is \&quot;latest\&quot; |  [optional] |



