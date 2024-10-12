# DataflowKitWebScraper.Serprequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**[Field]**](Field.md) | Specify CSS selectors (patterns) used to gather data from Search Engine Result Pages.  Ready-to-use payloads for collecting search results from the most popular Search Engines are available. These payloads are customizable, though.  | [optional] 
**format** | **String** | Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format. | 
**name** | **String** | Collection name. | 
**pageNum** | **Number** | Specify number of pages to crawl. | [optional] [default to 1]
**proxy** | **String** | Always specify proxy for sending SERP requests. Add choosen [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to &#x60;country-&#x60; value to send requests through a proxy in the specified country. Use &#x60;country-any&#x60; to use random geo-targets. | 
**type** | **String** | For SERP requests you should _always_ use &#x60;chrome&#x60; type to fetch content with a Headless chrome browser | 
**url** | **String** | url holds the link to a Search Engine to use, and other optional parameters like languages or country. | 



## Enum: FormatEnum


* `csv` (value: `"csv"`)

* `json` (value: `"json"`)

* `jsonl` (value: `"jsonl"`)

* `excel` (value: `"excel"`)

* `xml` (value: `"xml"`)




