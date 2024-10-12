

# Authentication


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | The email address where the one-time password (OTP) is sent. |  [optional] |
|**password** | **String** | The password used for 3D Secure password-based authentication. The value must be between 1 to 30 characters and must only contain the following supported characters.  * Characters between **a-z**, **A-Z**, and **0-9**  * Special characters: **äöüßÄÖÜ+-*_/ç%()&#x3D;?!~#&#39;\&quot;,;:$&amp;àùòâôûáúó** |  [optional] |
|**phone** | [**Phone**](Phone.md) | The phone number where the one-time password (OTP) is sent.  This object must have:  * A &#x60;type&#x60; set to **mobile**.  * A &#x60;number&#x60; with a valid country code.  * A &#x60;number&#x60; with more than 4 digits, excluding the country code.  &gt;Make sure to verify that the card user owns the phone number. |  [optional] |



