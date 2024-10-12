

# SupernovaInstanceView


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Identifier of running app/add-on |  [optional] |
|**appPort** | **BigDecimal** | Port of the HV that&#39;s redirected to 8080 on VM |  |
|**commitId** | **String** |  |  [optional] |
|**createdAt** | **BigDecimal** | Integer unix timestamp |  [optional] |
|**deployId** | **String** |  |  [optional] |
|**deployNumber** | **BigDecimal** |  |  [optional] |
|**displayName** | **String** | Generated PokéName. This name is generated from the uuid. |  [optional] |
|**flavor** | [**SupernovaInstanceViewFlavor**](SupernovaInstanceViewFlavor.md) |  |  |
|**hv** | **String** | String name of hv. |  |
|**image** | **String** | Base system image. E.g. java-20181030, node-20180912… |  |
|**instanceNumber** | **BigDecimal** |  |  [optional] |
|**internalIP** | **String** |  |  [optional] |
|**ip** | **String** | Public IP of the HV |  |
|**ownerId** | **String** | Identifier of the owner of the app/add-on running |  [optional] |
|**source** | **String** | Who/what started this instance? E.g. \&quot;app\&quot;, \&quot;cli\&quot; |  |
|**sshPort** | **BigDecimal** | Port of the HV that&#39;s redirected to 22 on VM |  [optional] |
|**state** | **String** |  |  [optional] |
|**uuid** | **String** |  |  |
|**zabbixPort** | **BigDecimal** | Port of the HV that&#39;s redirected to 10050 on VM |  |
|**zone** | **String** |  |  [optional] |



