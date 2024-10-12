

# KnownRelCodeType

alternate: The value \"alternate\" signifies that the IRI in the value of the href attribute identifies an alternate version of the resource described by the containing element.related: The value \"related\" signifies that the IRI in the value of the href attribute identifies a resource related to the resource described by the containing element. For example, the feed for a site that discusses the performance of the search engine at \"http://search.example.com\" might contain, as a child of atom:feed. An identical link might appear as a child of any atom:entry whose content contains a discussion of that same search engine.self: The value \"self\" signifies that the IRI in the value of the href attribute identifies a resource equivalent to the containing element.enclosure: The value \"enclosure\" signifies that the IRI in the value of the href attribute identifies a related resource that is potentially large in size and might require special handling. For atom:link elements with rel=\"enclosure\", the length attribute SHOULD be provided.via: The value \"via\" signifies that the IRI in the value of the href attribute identifies a resource that is the source of the information provided in the containing element.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|



