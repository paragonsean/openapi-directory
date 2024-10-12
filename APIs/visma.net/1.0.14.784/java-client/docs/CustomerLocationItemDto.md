

# CustomerLocationItemDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**AddressDto**](AddressDto.md) |  |  [optional] |
|**contact** | [**ContactDto**](ContactDto.md) |  |  [optional] |
|**corporateId** | **String** | The corporate id of the location |  [optional] |
|**countryId** | **String** | The country code of the location |  [optional] |
|**fobPointId** | **String** | Default FobPointId |  [optional] |
|**gln** | **String** | The global localization number of the location |  [optional] |
|**id** | **String** | Location id |  [optional] |
|**insurance** | **Boolean** | Default Insurance |  [optional] |
|**internalId** | **Integer** | An internal id of the customer location |  [optional] |
|**leadTime** | **Integer** | The number of days required for the shipped goods to reach the customer.  Used in the calculation of the scheduled shipment date |  [optional] |
|**name** | **String** | Location description |  [optional] |
|**preferredWarehouseId** | **String** | The preferred shipping warehouse of the customer set default for the order |  [optional] |
|**priceClassId** | **String** | Price class |  [optional] |
|**priority** | **Integer** | Default Priority |  [optional] |
|**resedentialDelivery** | **Boolean** | Default ResidentialDelivery.&lt;br /&gt;  This field will be removed with due date 1.12.2023. It is recommended to use &lt;see cref&#x3D;\&quot;P:Visma.net.ERP.SalesOrders.Api.Dto.CustomerLocationItemDto.ResidentialDelivery\&quot;&gt;ResidentialDelivery&lt;/see&gt; instead. |  [optional] |
|**residentialDelivery** | **Boolean** | Default ResidentialDelivery |  [optional] |
|**saturdayDelivery** | **Boolean** | Default SaturdayDelivery |  [optional] |
|**shipTermsId** | **String** | Default ShipTermsId |  [optional] |
|**shipViaId** | **String** | The ship via id that represents the carrier and its service to be used for shipping the ordered goods |  [optional] |
|**shipZoneId** | **String** | Default ShipZoneId |  [optional] |
|**shippingRule** | **String** | Shipping rule of the customer set default for the order  &lt;br&gt;Is one of the following options:&lt;br&gt;&lt;list type&#x3D;\&quot;bullet\&quot;&gt;&lt;item&gt;&lt;term&gt;CancelRemainder: &lt;/term&gt;&lt;description&gt;The ordered quantity should be delivered in one shipment&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;term&gt;BackOrderAllowed: &lt;/term&gt;&lt;description&gt;The ordered quantity can be delivered in multiple shipments.&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;term&gt;ShipComplete: &lt;/term&gt;&lt;description&gt;The ordered quantity should be delivered in one shipment.&lt;/description&gt;&lt;/item&gt;&lt;/list&gt; |  [optional] |
|**taxRegistrationId** | **String** | The tax registration id of the location |  [optional] |
|**taxZoneId** | **String** | The location tax/VAT zone id |  [optional] |
|**warehouseId** | **String** | The site id of the location |  [optional] |



