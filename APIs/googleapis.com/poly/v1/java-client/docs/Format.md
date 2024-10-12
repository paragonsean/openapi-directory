

# Format

The same asset can be represented in different formats, for example, a [WaveFront .obj](//en.wikipedia.org/wiki/Wavefront_.obj_file) file with its corresponding .mtl file or a [Khronos glTF](//www.khronos.org/gltf) file with its corresponding .glb binary data. A format refers to a specific representation of an asset and contains all information needed to retrieve and describe this representation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formatComplexity** | [**FormatComplexity**](FormatComplexity.md) |  |  [optional] |
|**formatType** | **String** | A short string that identifies the format type of this representation. Possible values are: &#x60;FBX&#x60;, &#x60;GLTF&#x60;, &#x60;GLTF2&#x60;, &#x60;OBJ&#x60;, and &#x60;TILT&#x60;. |  [optional] |
|**resources** | [**List&lt;ModelFile&gt;**](ModelFile.md) | A list of dependencies of the root element. May include, but is not limited to, materials, textures, and shader programs. |  [optional] |
|**root** | [**ModelFile**](ModelFile.md) |  |  [optional] |



