

# Tiered


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brackets** | [**List&lt;StairstepAllOfBrackets&gt;**](StairstepAllOfBrackets.md) | The price brackets, along with the price formula, is used to calculate the amount to charge for the product on this plan on the invoice.  The \&quot;tiered\&quot; example:  Price per apple | Max quantity | Description ----------------|--------------|------------ $5              | 1            | 1 $4              | 5            | 2 to 5 $3              | null         | 6 or more  If someone bought 1 apple, it would be $5.  If someone bought 2 apples, it would be $9. $5 per apple for the first apple, then $4 per apple for the 2nd to 5th apple.  |  |



