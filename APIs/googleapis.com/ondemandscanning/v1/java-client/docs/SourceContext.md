

# SourceContext

A SourceContext is a reference to a tree of files. A SourceContext together with a path point to a unique revision of a single file or directory.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudRepo** | [**CloudRepoSourceContext**](CloudRepoSourceContext.md) |  |  [optional] |
|**gerrit** | [**GerritSourceContext**](GerritSourceContext.md) |  |  [optional] |
|**git** | [**GitSourceContext**](GitSourceContext.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels with user defined metadata. |  [optional] |



