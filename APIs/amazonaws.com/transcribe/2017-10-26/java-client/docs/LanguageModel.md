

# LanguageModel

<p>Provides information about a custom language model, including:</p> <ul> <li> <p>The base model name</p> </li> <li> <p>When the model was created</p> </li> <li> <p>The location of the files used to train the model</p> </li> <li> <p>When the model was last modified</p> </li> <li> <p>The name you chose for the model</p> </li> <li> <p>The model's language</p> </li> <li> <p>The model's processing state</p> </li> <li> <p>Any available upgrades for the base model</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modelName** | [**String**](String.md) |  |  [optional] |
|**createTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**languageCode** | [**CLMLanguageCode**](CLMLanguageCode.md) |  |  [optional] |
|**baseModelName** | [**BaseModelName**](BaseModelName.md) |  |  [optional] |
|**modelStatus** | [**ModelStatus**](ModelStatus.md) |  |  [optional] |
|**upgradeAvailability** | [**Boolean**](Boolean.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**inputDataConfig** | [**LanguageModelInputDataConfig**](LanguageModelInputDataConfig.md) |  |  [optional] |



