

# Address33

Address of the recipient/merchant.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**city** | **String** | City of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-25 |  |
|**country** | **String** | The recipient&#39;s/merchant&#39;s home country as an ISO 3166-1 alpha-3 country code, in uppercase. Details- Alpha, Length: 3 |  |
|**countrySubdivision** | **String** | State or province of the recipient/merchant. If the merchant_transfer.recipient.address.country is USA or CAN, the country subdivision code is required.   Type: Alpha [A-Z], Length 2-3 |  [optional] |
|**line1** | **String** | First line of the address of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-50 |  [optional] |
|**line2** | **String** | Second line of the address of the recipient/merchant.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-50 |  [optional] |
|**postalCode** | **String** | Postal code of the recipient/merchant. Format in 5 digits or 5 digits hyphen 4 digits.  Details numeric length: 5 or 5-4 |  [optional] |



