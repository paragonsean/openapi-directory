# FitnessApi.DataSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | [optional] 
**dataQualityStandard** | **[String]** | DO NOT POPULATE THIS FIELD. It is never populated in responses from the platform, and is ignored in queries. It will be removed in a future version entirely. | [optional] 
**dataStreamId** | **String** | A unique identifier for the data stream produced by this data source. The identifier includes: - The physical device&#39;s manufacturer, model, and serial number (UID). - The application&#39;s package name or name. Package name is used when the data source was created by an Android application. The developer project number is used when the data source was created by a REST client. - The data source&#39;s type. - The data source&#39;s stream name. Note that not all attributes of the data source are used as part of the stream identifier. In particular, the version of the hardware/the application isn&#39;t used. This allows us to preserve the same stream through version updates. This also means that two DataSource objects may represent the same data stream even if they&#39;re not equal. The exact format of the data stream ID created by an Android application is: type:dataType.name:application.packageName:device.manufacturer:device.model:device.uid:dataStreamName The exact format of the data stream ID created by a REST client is: type:dataType.name:developer project number:device.manufacturer:device.model:device.uid:dataStreamName When any of the optional fields that make up the data stream ID are absent, they will be omitted from the data stream ID. The minimum viable data stream ID would be: type:dataType.name:developer project number Finally, the developer project number and device UID are obfuscated when read by any REST or Android client that did not create the data source. Only the data source creator will see the developer project number in clear and normal form. This means a client will see a different set of data_stream_ids than another client with different credentials. | [optional] 
**dataStreamName** | **String** | The stream name uniquely identifies this particular data source among other data sources of the same type from the same underlying producer. Setting the stream name is optional, but should be done whenever an application exposes two streams for the same data type, or when a device has two equivalent sensors. | [optional] 
**dataType** | [**DataType**](DataType.md) |  | [optional] 
**device** | [**Device**](Device.md) |  | [optional] 
**name** | **String** | An end-user visible name for this data source. | [optional] 
**type** | **String** | A constant describing the type of this data source. Indicates whether this data source produces raw or derived data. | [optional] 



## Enum: [DataQualityStandardEnum]


* `dataQualityUnknown` (value: `"dataQualityUnknown"`)

* `dataQualityBloodPressureEsh2002` (value: `"dataQualityBloodPressureEsh2002"`)

* `dataQualityBloodPressureEsh2010` (value: `"dataQualityBloodPressureEsh2010"`)

* `dataQualityBloodPressureAami` (value: `"dataQualityBloodPressureAami"`)

* `dataQualityBloodPressureBhsAA` (value: `"dataQualityBloodPressureBhsAA"`)

* `dataQualityBloodPressureBhsAB` (value: `"dataQualityBloodPressureBhsAB"`)

* `dataQualityBloodPressureBhsBA` (value: `"dataQualityBloodPressureBhsBA"`)

* `dataQualityBloodPressureBhsBB` (value: `"dataQualityBloodPressureBhsBB"`)

* `dataQualityBloodGlucoseIso151972003` (value: `"dataQualityBloodGlucoseIso151972003"`)

* `dataQualityBloodGlucoseIso151972013` (value: `"dataQualityBloodGlucoseIso151972013"`)





## Enum: TypeEnum


* `raw` (value: `"raw"`)

* `derived` (value: `"derived"`)




