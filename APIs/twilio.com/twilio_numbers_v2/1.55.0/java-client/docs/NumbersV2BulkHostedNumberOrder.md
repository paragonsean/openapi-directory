

# NumbersV2BulkHostedNumberOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bulkHostingSid** | **String** | A 34 character string that uniquely identifies this BulkHostedNumberOrder. |  [optional] |
|**dateCompleted** | **OffsetDateTime** | The date that this resource was completed, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**friendlyName** | **String** | A 128 character string that is a human-readable text that describes this resource. |  [optional] |
|**notificationEmail** | **String** | Email address used for send notifications about this Bulk hosted number request. |  [optional] |
|**requestStatus** | **BulkHostedNumberOrderEnumRequestStatus** |  |  [optional] |
|**results** | **List&lt;Object&gt;** | Contains a list of all the individual hosting orders and their information, for this Bulk request. Each result object is grouped by its order status. To see a complete list of order status, please check &#39;https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values&#39;. |  [optional] |
|**totalCount** | **Integer** | The total count of phone numbers in this Bulk hosting request. |  [optional] |
|**url** | **URI** | The URL of this BulkHostedNumberOrder resource. |  [optional] |



