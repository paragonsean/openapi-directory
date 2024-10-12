# AwsRoboMaker.CreateSimulationApplicationVersionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **String** | The application information for the simulation application. | 
**currentRevisionId** | **String** | The current revision id for the simulation application. If you provide a value and it matches the latest revision ID, a new version will be created. | [optional] 
**s3Etags** | **[String]** | The Amazon S3 eTag identifier for the zip file bundle that you use to create the simulation application. | [optional] 
**imageDigest** | **String** | The SHA256 digest used to identify the Docker image URI used to created the simulation application. | [optional] 


