

# DataSource

Definition of a unique source of sensor data. Data sources can expose raw data coming from hardware sensors on local or companion devices. They can also expose derived data, created by transforming or merging other data sources. Multiple data sources can exist for the same data type. Every data point inserted into or read from this service has an associated data source. The data source contains enough information to uniquely identify its data, including the hardware device and the application that collected and/or transformed the data. It also holds useful metadata, such as the hardware and application versions, and the device type. Each data source produces a unique stream of data, with a unique identifier. Not all changes to data source affect the stream identifier, so that data collected by updated versions of the same application/device can still be considered to belong to the same data stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**application** | [**Application**](Application.md) |  |  [optional] |
|**dataQualityStandard** | [**List&lt;DataQualityStandardEnum&gt;**](#List&lt;DataQualityStandardEnum&gt;) | DO NOT POPULATE THIS FIELD. It is never populated in responses from the platform, and is ignored in queries. It will be removed in a future version entirely. |  [optional] |
|**dataStreamId** | **String** | A unique identifier for the data stream produced by this data source. The identifier includes: - The physical device&#39;s manufacturer, model, and serial number (UID). - The application&#39;s package name or name. Package name is used when the data source was created by an Android application. The developer project number is used when the data source was created by a REST client. - The data source&#39;s type. - The data source&#39;s stream name. Note that not all attributes of the data source are used as part of the stream identifier. In particular, the version of the hardware/the application isn&#39;t used. This allows us to preserve the same stream through version updates. This also means that two DataSource objects may represent the same data stream even if they&#39;re not equal. The exact format of the data stream ID created by an Android application is: type:dataType.name:application.packageName:device.manufacturer:device.model:device.uid:dataStreamName The exact format of the data stream ID created by a REST client is: type:dataType.name:developer project number:device.manufacturer:device.model:device.uid:dataStreamName When any of the optional fields that make up the data stream ID are absent, they will be omitted from the data stream ID. The minimum viable data stream ID would be: type:dataType.name:developer project number Finally, the developer project number and device UID are obfuscated when read by any REST or Android client that did not create the data source. Only the data source creator will see the developer project number in clear and normal form. This means a client will see a different set of data_stream_ids than another client with different credentials. |  [optional] |
|**dataStreamName** | **String** | The stream name uniquely identifies this particular data source among other data sources of the same type from the same underlying producer. Setting the stream name is optional, but should be done whenever an application exposes two streams for the same data type, or when a device has two equivalent sensors. |  [optional] |
|**dataType** | [**DataType**](DataType.md) |  |  [optional] |
|**device** | [**Device**](Device.md) |  |  [optional] |
|**name** | **String** | An end-user visible name for this data source. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | A constant describing the type of this data source. Indicates whether this data source produces raw or derived data. |  [optional] |



## Enum: List&lt;DataQualityStandardEnum&gt;

| Name | Value |
|---- | -----|
| DATA_QUALITY_UNKNOWN | &quot;dataQualityUnknown&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_ESH2002 | &quot;dataQualityBloodPressureEsh2002&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_ESH2010 | &quot;dataQualityBloodPressureEsh2010&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_AAMI | &quot;dataQualityBloodPressureAami&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_AA | &quot;dataQualityBloodPressureBhsAA&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_AB | &quot;dataQualityBloodPressureBhsAB&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_BA | &quot;dataQualityBloodPressureBhsBA&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_BB | &quot;dataQualityBloodPressureBhsBB&quot; |
| DATA_QUALITY_BLOOD_GLUCOSE_ISO151972003 | &quot;dataQualityBloodGlucoseIso151972003&quot; |
| DATA_QUALITY_BLOOD_GLUCOSE_ISO151972013 | &quot;dataQualityBloodGlucoseIso151972013&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RAW | &quot;raw&quot; |
| DERIVED | &quot;derived&quot; |



