

# Action


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignoreIfNotPresent** | **Boolean** | This optional parameter is useful when the target element occasionally may not be present in the DOM. |  [optional] |
|**selector** | **String** | Some websites require clicking &#39;More&#39; button while scrolling a page. Put here &#39;More&#39; button valid CSS Selector. |  [optional] |
|**value** | **String** | Sequence of keys to send. Keys can include keystrokes such as ALT+A, ENTER, BACKSPACE, etc. |  [optional] |
|**skipLastIteration** | **Boolean** | It is only used for loop actions only. Skips the last iteration. |  [optional] |
|**waitDelay** | **String** | Wait time (in milliseconds). |  [optional] |
|**script** | **String** | The JavaScript snippet to run |  [optional] |
|**actions** | [**List&lt;Action&gt;**](Action.md) | list of actions combined in the loop are executed step-by-step |  [optional] |
|**times** | **Integer** | The number of times to scroll down a web page. |  [optional] |
|**scrollByPixels** | **BigDecimal** | Scrolls a web page by the number of pixels specified by &#39;scrollByPixels&#39; parameter. |  [optional] |
|**scrollingElementSelector** | **String** | Optionally specify here a valid CSS Selector of scrolling element. |  [optional] |



