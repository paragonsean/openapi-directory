

# Recipe

Steps taken to build the artifact. For a TaskRun, typically each container corresponds to one step in the recipe.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | **List&lt;Map&lt;String, Object&gt;&gt;** | Collection of all external inputs that influenced the build on top of recipe.definedInMaterial and recipe.entryPoint. For example, if the recipe type were \&quot;make\&quot;, then this might be the flags passed to make aside from the target, which is captured in recipe.entryPoint. Since the arguments field can greatly vary in structure, depending on the builder and recipe type, this is of form \&quot;Any\&quot;. |  [optional] |
|**definedInMaterial** | **String** | Index in materials containing the recipe steps that are not implied by recipe.type. For example, if the recipe type were \&quot;make\&quot;, then this would point to the source containing the Makefile, not the make program itself. Set to -1 if the recipe doesn&#39;t come from a material, as zero is default unset value for int64. |  [optional] |
|**entryPoint** | **String** | String identifying the entry point into the build. This is often a path to a configuration file and/or a target label within that file. The syntax and meaning are defined by recipe.type. For example, if the recipe type were \&quot;make\&quot;, then this would reference the directory in which to run make as well as which target to use. |  [optional] |
|**environment** | **List&lt;Map&lt;String, Object&gt;&gt;** | Any other builder-controlled inputs necessary for correctly evaluating the recipe. Usually only needed for reproducing the build but not evaluated as part of policy. Since the environment field can greatly vary in structure, depending on the builder and recipe type, this is of form \&quot;Any\&quot;. |  [optional] |
|**type** | **String** | URI indicating what type of recipe was performed. It determines the meaning of recipe.entryPoint, recipe.arguments, recipe.environment, and materials. |  [optional] |



