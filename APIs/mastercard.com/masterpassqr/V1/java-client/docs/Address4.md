

# Address4

Address of the sender. Optional

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**city** | **String** | City of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-25. |  |
|**country** | **String** | Country of the sender as an ISO alpha country code.   Type: Alpha [A-Z], Length: 3. |  |
|**countrySubdivision** | **String** | State or province of the sender. If the merchant_transfer.sender.address.country is USA or CAN, the country subdivision is required.   Type: Alpha [A-Z], Length 2-3 |  [optional] |
|**line1** | **String** | First line of the address of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-50 |  [optional] |
|**line2** | **String** | Second line of the address of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-50 |  [optional] |
|**postalCode** | **String** | Postal code of the sender.   Type: Alphanumeric Special [a-zA-Z0-9- ], Length: 1-10 |  [optional] |



