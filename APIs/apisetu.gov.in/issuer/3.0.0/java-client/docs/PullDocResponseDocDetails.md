

# PullDocResponseDocDetails

Issuer can add meta content specific to document here.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataContent** | **String** | Enclose the Base64 byte encoded certificate metadata in XML format. The DataContent element should be sent only if the original request contains format attribute as “xml” or “both”. |  |
|**docContent** | **String** | Enclose the Base64 byte encoded contents of PDF file in this element. The DocContent element should be sent only if the format attribute in the original request is sent as “pdf” or “both” or is absent. |  |



