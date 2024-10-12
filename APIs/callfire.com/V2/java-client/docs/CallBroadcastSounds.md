

# CallBroadcastSounds

A set of sounds assigned to a voice broadcast to play according to an answering machine configuration. You can add the existing sounds from the account's sound library or to provide a text which will be converted into a speech. There are four sound options available for a Voice Broadcast campaign

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dncDigit** | **String** | Digit pressed to place contact in DNC list |  [optional] |
|**dncSoundId** | **Long** | An id of sound file to play when recipient decided to opt out and pressed DNC digit |  [optional] |
|**dncSoundText** | **String** | Text to be turned into sound, plays to notify that Do Not Call digit has been pressed and inform your contact of their placement on the Do Not Call list |  [optional] |
|**dncSoundTextVoice** | [**DncSoundTextVoiceEnum**](#DncSoundTextVoiceEnum) | The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) |  [optional] |
|**liveSoundId** | **Long** | An id of sound file to play if phone is answered |  [optional] |
|**liveSoundText** | **String** | Text to be used to turned into a sound. This text will be played when the phone is answered |  [optional] |
|**liveSoundTextVoice** | [**LiveSoundTextVoiceEnum**](#LiveSoundTextVoiceEnum) | The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a live sound |  [optional] |
|**machineSoundId** | **Long** | An id of a sound file to play if answering machine is detected |  [optional] |
|**machineSoundText** | **String** | Text to be turned into a sound. This text will be played when answering machine is detected |  [optional] |
|**machineSoundTextVoice** | [**MachineSoundTextVoiceEnum**](#MachineSoundTextVoiceEnum) | The voice to be used (MALE1, FEMALE1 , FEMALE2, SPANISH1, FRENCHCANADIAN1) for a machine sound |  [optional] |
|**transferDigit** | **String** | Digit pressed to initiate a transfer |  [optional] |
|**transferNumber** | **String** | Phone number in E.164 format (11-digit) to transfer call to.  Example: 12132000384, 67076 |  [optional] |
|**transferSoundId** | **Long** | An id of a file to play if call is transferred |  [optional] |
|**transferSoundText** | **String** | Text to be turned into a sound. This text will be played when the transfer digit is played |  [optional] |
|**transferSoundTextVoice** | [**TransferSoundTextVoiceEnum**](#TransferSoundTextVoiceEnum) | The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a sound transfer |  [optional] |



## Enum: DncSoundTextVoiceEnum

| Name | Value |
|---- | -----|
| MALE1 | &quot;MALE1&quot; |
| FEMALE1 | &quot;FEMALE1&quot; |
| FEMALE2 | &quot;FEMALE2&quot; |
| SPANISH1 | &quot;SPANISH1&quot; |
| FRENCHCANADIAN1 | &quot;FRENCHCANADIAN1&quot; |



## Enum: LiveSoundTextVoiceEnum

| Name | Value |
|---- | -----|
| MALE1 | &quot;MALE1&quot; |
| FEMALE1 | &quot;FEMALE1&quot; |
| FEMALE2 | &quot;FEMALE2&quot; |
| SPANISH1 | &quot;SPANISH1&quot; |
| FRENCHCANADIAN1 | &quot;FRENCHCANADIAN1&quot; |



## Enum: MachineSoundTextVoiceEnum

| Name | Value |
|---- | -----|
| MALE1 | &quot;MALE1&quot; |
| FEMALE1 | &quot;FEMALE1&quot; |
| FEMALE2 | &quot;FEMALE2&quot; |
| SPANISH1 | &quot;SPANISH1&quot; |
| FRENCHCANADIAN1 | &quot;FRENCHCANADIAN1&quot; |



## Enum: TransferSoundTextVoiceEnum

| Name | Value |
|---- | -----|
| MALE1 | &quot;MALE1&quot; |
| FEMALE1 | &quot;FEMALE1&quot; |
| FEMALE2 | &quot;FEMALE2&quot; |
| SPANISH1 | &quot;SPANISH1&quot; |
| FRENCHCANADIAN1 | &quot;FRENCHCANADIAN1&quot; |



