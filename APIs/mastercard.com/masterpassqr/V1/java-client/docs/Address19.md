

# Address19

Address of the recipient/merchant.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**city** | **String** | City of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Maximum Length: 25 |  [optional] |
|**country** | **String** | Country of the recipient as an ISO alpha country code.   Type: Alpha [A-Z], Maximum Length: 3 |  [optional] |
|**countrySubdivision** | **String** | State or province of the recipient/merchant. If the merchant_transfer.recipient.address.country is USA or CAN, the country subdivision code is required.   Type: Alpha [A-Z], Maximum Length: 3 |  [optional] |
|**line1** | **String** | First line of the address of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Maximum Length: 50 |  [optional] |
|**line2** | **String** | Second line of the address of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Maximum Length: 50 |  [optional] |
|**postalCode** | **String** | Postal code of the recipient.   Type: Alphanumeric Special [a-zA-Z0-9- ], Maximum Length: 10 |  [optional] |



