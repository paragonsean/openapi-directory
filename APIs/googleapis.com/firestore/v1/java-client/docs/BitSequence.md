

# BitSequence

A sequence of bits, encoded in a byte array. Each byte in the `bitmap` byte array stores 8 bits of the sequence. The only exception is the last byte, which may store 8 _or fewer_ bits. The `padding` defines the number of bits of the last byte to be ignored as \"padding\". The values of these \"padding\" bits are unspecified and must be ignored. To retrieve the first bit, bit 0, calculate: `(bitmap[0] & 0x01) != 0`. To retrieve the second bit, bit 1, calculate: `(bitmap[0] & 0x02) != 0`. To retrieve the third bit, bit 2, calculate: `(bitmap[0] & 0x04) != 0`. To retrieve the fourth bit, bit 3, calculate: `(bitmap[0] & 0x08) != 0`. To retrieve bit n, calculate: `(bitmap[n / 8] & (0x01 << (n % 8))) != 0`. The \"size\" of a `BitSequence` (the number of bits it contains) is calculated by this formula: `(bitmap.length * 8) - padding`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bitmap** | **byte[]** | The bytes that encode the bit sequence. May have a length of zero. |  [optional] |
|**padding** | **Integer** | The number of bits of the last byte in &#x60;bitmap&#x60; to ignore as \&quot;padding\&quot;. If the length of &#x60;bitmap&#x60; is zero, then this value must be &#x60;0&#x60;. Otherwise, this value must be between 0 and 7, inclusive. |  [optional] |



