# SendPersonToMerchant.Address31

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | City of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-25 | 
**country** | **String** | Country of the sender as an ISO alpha country code. Details- Alpha, Length: 3 | 
**countrySubdivision** | **String** | State or province of the sender. If the payment_transfer.sender.address.country is USA or CAN, the country subdivision is required. Details- Conditional, Alpha, 2-3 | [optional] 
**line1** | **String** | First line of the address of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-50 | [optional] 
**line2** | **String** | Second line of the address of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-50 | [optional] 
**postalCode** | **String** | Postal code of the sender. Format in 5 digits or 5 digits hyphen 4 digits.  Details numeric length: 5 or 5-4 | [optional] 


