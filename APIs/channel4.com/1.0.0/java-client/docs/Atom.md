

# Atom

This version of the Atom schema is based on version 1.0 of the format specifications, found here http://www.atomenabled.org/developers/syndication/atom-format-spec.php. The original namespace was http://www.w3.org/2005/Atom but we changed it to http://www.opengis.net/atom/2005 to avoid conflicting definitions of the same namespace in the future. NOT DONE YET. There is no XSD official schema for atom but this one seems to be the most known: http://www.kbcafe.com/rss/atom.xsd.xml (The Atom Publishing Protocol was issued as a Proposed Standard in IETF RFC 5023 in October 2007 http://tools.ietf.org/html/rfc5023) An Atom document may have two root elements, feed and entry, as defined in section 2.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feed** | **Map&lt;String, Object&gt;** | The Atom feed construct is defined in section 4.1.1 of the format spec. |  |



