# DataflowApi.SdkHarnessContainerImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **[String]** | The set of capabilities enumerated in the above Environment proto. See also [beam_runner_api.proto](https://github.com/apache/beam/blob/master/model/pipeline/src/main/proto/org/apache/beam/model/pipeline/v1/beam_runner_api.proto) | [optional] 
**containerImage** | **String** | A docker container image that resides in Google Container Registry. | [optional] 
**environmentId** | **String** | Environment ID for the Beam runner API proto Environment that corresponds to the current SDK Harness. | [optional] 
**useSingleCorePerContainer** | **Boolean** | If true, recommends the Dataflow service to use only one core per SDK container instance with this image. If false (or unset) recommends using more than one core per SDK container instance with this image for efficiency. Note that Dataflow service may choose to override this property if needed. | [optional] 


