# CallFireApiDocumentation.CallRecipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Map of user-defined string attributes associated with recipient | [optional] 
**contactId** | **Number** | An id of existing contact used as recipient | [optional] 
**dialplanXml** | **String** | An IVR xml document describing dialplan to setup an IVR broadcast. If dialplan is set there is no need to set live, machine and transfer sounds (or vice versa) | [optional] 
**fromNumber** | **String** | ~ | [optional] 
**liveMessage** | **String** | Text to be turned into a sound, this text will be played when the phone is answered | [optional] 
**liveMessageSoundId** | **Number** | An id of a sound file to play if phone is answered | [optional] 
**machineMessage** | **String** | Text to be used to turn into sound, this text will be played when answering machine is detected | [optional] 
**machineMessageSoundId** | **Number** | An id of a sound file to play if answering machine is detected | [optional] 
**phoneNumber** | **String** | Recipient&#39;s phone number in E.164 format (11-digit) or short code. Example: 12132000384 | [optional] 
**transferDigit** | **String** | A digit pressed to initiate the transfer | [optional] 
**transferMessage** | **String** | Text to be turned into sound, this text will be played when the transfer digit is played | [optional] 
**transferMessageSoundId** | **Number** | An id of a sound file to play if call is transferred | [optional] 
**transferNumber** | **String** | Phone number in E.164 format (11-digit) to transfer the call to. Example: 12132000384 | [optional] 
**voice** | **String** | The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) | [optional] 



## Enum: VoiceEnum


* `MALE1` (value: `"MALE1"`)

* `FEMALE1` (value: `"FEMALE1"`)

* `FEMALE2` (value: `"FEMALE2"`)

* `SPANISH1` (value: `"SPANISH1"`)

* `FRENCHCANADIAN1` (value: `"FRENCHCANADIAN1"`)




