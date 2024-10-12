

# AnswerPreCheckoutQueryPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | Required if *ok* is *False*. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. \&quot;Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!\&quot;). Telegram will display this message to the user. |  [optional] |
|**ok** | **Boolean** | Specify *True* if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use *False* if there are any problems. |  |
|**preCheckoutQueryId** | **String** | Unique identifier for the query to be answered |  |



