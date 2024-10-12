

# XmlNs0Result

<p> If a request returns a list of items they're always wrapped into a Result. As there is a maximum amount of items to be returned at once a Result consists of the total amount of items (total), how many items per page you get (itemsPerPage), the current page (page) and the current list of items. </p>  <p> E.g. if there are 35 items, itemsPerPage is 10 and the current page is 2, then items 11 to 20 are in the list. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemsPerPage** | **BigDecimal** | the amount of items you get per page |  [optional] |
|**page** | **BigDecimal** | the current page. starts at 1 |  [optional] |
|**total** | **BigDecimal** | the total amount of items matching the query |  [optional] |



