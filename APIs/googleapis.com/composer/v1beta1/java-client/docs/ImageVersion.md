

# ImageVersion

Image Version information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDisabled** | **Boolean** | Whether it is impossible to create an environment with the image version. |  [optional] |
|**imageVersionId** | **String** | The string identifier of the ImageVersion, in the form: \&quot;composer-x.y.z-airflow-a.b.c\&quot; |  [optional] |
|**isDefault** | **Boolean** | Whether this is the default ImageVersion used by Composer during environment creation if no input ImageVersion is specified. |  [optional] |
|**releaseDate** | [**Date**](Date.md) |  |  [optional] |
|**supportedPythonVersions** | **List&lt;String&gt;** | supported python versions |  [optional] |
|**upgradeDisabled** | **Boolean** | Whether it is impossible to upgrade an environment running with the image version. |  [optional] |



