

# RegionsVersion

The version of the available regions being used for the specified resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**version** | **String** | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. |  [optional] |



