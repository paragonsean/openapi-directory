# CallFireApiDocumentation.CallBroadcastSounds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dncDigit** | **String** | Digit pressed to place contact in DNC list | [optional] 
**dncSoundId** | **Number** | An id of sound file to play when recipient decided to opt out and pressed DNC digit | [optional] 
**dncSoundText** | **String** | Text to be turned into sound, plays to notify that Do Not Call digit has been pressed and inform your contact of their placement on the Do Not Call list | [optional] 
**dncSoundTextVoice** | **String** | The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) | [optional] 
**liveSoundId** | **Number** | An id of sound file to play if phone is answered | [optional] 
**liveSoundText** | **String** | Text to be used to turned into a sound. This text will be played when the phone is answered | [optional] 
**liveSoundTextVoice** | **String** | The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a live sound | [optional] 
**machineSoundId** | **Number** | An id of a sound file to play if answering machine is detected | [optional] 
**machineSoundText** | **String** | Text to be turned into a sound. This text will be played when answering machine is detected | [optional] 
**machineSoundTextVoice** | **String** | The voice to be used (MALE1, FEMALE1 , FEMALE2, SPANISH1, FRENCHCANADIAN1) for a machine sound | [optional] 
**transferDigit** | **String** | Digit pressed to initiate a transfer | [optional] 
**transferNumber** | **String** | Phone number in E.164 format (11-digit) to transfer call to.  Example: 12132000384, 67076 | [optional] 
**transferSoundId** | **Number** | An id of a file to play if call is transferred | [optional] 
**transferSoundText** | **String** | Text to be turned into a sound. This text will be played when the transfer digit is played | [optional] 
**transferSoundTextVoice** | **String** | The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a sound transfer | [optional] 



## Enum: DncSoundTextVoiceEnum


* `MALE1` (value: `"MALE1"`)

* `FEMALE1` (value: `"FEMALE1"`)

* `FEMALE2` (value: `"FEMALE2"`)

* `SPANISH1` (value: `"SPANISH1"`)

* `FRENCHCANADIAN1` (value: `"FRENCHCANADIAN1"`)





## Enum: LiveSoundTextVoiceEnum


* `MALE1` (value: `"MALE1"`)

* `FEMALE1` (value: `"FEMALE1"`)

* `FEMALE2` (value: `"FEMALE2"`)

* `SPANISH1` (value: `"SPANISH1"`)

* `FRENCHCANADIAN1` (value: `"FRENCHCANADIAN1"`)





## Enum: MachineSoundTextVoiceEnum


* `MALE1` (value: `"MALE1"`)

* `FEMALE1` (value: `"FEMALE1"`)

* `FEMALE2` (value: `"FEMALE2"`)

* `SPANISH1` (value: `"SPANISH1"`)

* `FRENCHCANADIAN1` (value: `"FRENCHCANADIAN1"`)





## Enum: TransferSoundTextVoiceEnum


* `MALE1` (value: `"MALE1"`)

* `FEMALE1` (value: `"FEMALE1"`)

* `FEMALE2` (value: `"FEMALE2"`)

* `SPANISH1` (value: `"SPANISH1"`)

* `FRENCHCANADIAN1` (value: `"FRENCHCANADIAN1"`)




