# Arespass.Ec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alphabetSequence** | [**[EcAlphabetSequenceInner]**](EcAlphabetSequenceInner.md) | **The penalty applied to each character that has been found to be part of an alphabet sequence.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  | [optional] 
**apiVersion** | **String** | **This API version number.**  | [optional] 
**detectedKeyboard** | **String** | **The detected keyboard, QWERTY or Dvorak.**  | [optional] 
**efficiency** | **Number** | **The ratio entropy / idealEntropy.**  It is a float number in the range [0, 1].  | [optional] 
**entropy** | **Number** | **The entropy calculated for the input password.**  It is measured in bits.  | [optional] 
**entropyDistribution** | [**[EcEntropyDistributionInner]**](EcEntropyDistributionInner.md) | **The distribution of the calculated entropy among the password characters.**  | [optional] 
**idealEntropy** | **Number** | **The Shannon entropy.**  The Shannon entropy is the entropy calculated if no penalizations - words, number sequence, alphabet sequence, etc - were found in the password.  It is measured in bits.  | [optional] 
**keyboardSequence** | [**[EcKeyboardSequenceInner]**](EcKeyboardSequenceInner.md) | **The penalty applied to each character that has been found to be part of a keyboard sequence.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  | [optional] 
**l33tPassword** | **String** | The analyzed password after the l33t substitution. | [optional] 
**nonUniformEntropyDistributionPenalty** | **Number** | **The penalty applied to the whole password because of irregular entropy distribution.**  This penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  | [optional] 
**numberSequence** | [**[EcNumberSequenceInner]**](EcNumberSequenceInner.md) | **The penalty applied to each character that has been found to be part of a number sequence.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  | [optional] 
**password** | **String** | The analyzed password. | [optional] 
**passwordLength** | **Number** | The number of characters the password has. | [optional] 
**penalty** | **Number** | **The penalty applied to each character that has been found to be part of a word, number sequence, alphabet sequence, etc.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  Its value is equal to the value of the input parameter *penalty*.  | [optional] 
**repeatedChars** | [**[EcRepeatedCharsInner]**](EcRepeatedCharsInner.md) | **The penalty applied to each character that are repeated**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.            | [optional] 
**requestId** | **String** | **The identifier of the request that corresponds to this response.**  | [optional] 
**requestTimestamp** | **Number** | **The timestamp for this response.**  Milliseconds from the epoch of 1970-01-01T00:00:00Z.  | [optional] 
**summary** | **[String]** |  | [optional] 
**total** | [**[EcTotalInner]**](EcTotalInner.md) | **The total penalty applied to each character.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  | [optional] 
**words** | [**[EcWordsInner]**](EcWordsInner.md) | **The penalty applied to each character that has been found to be part of a word.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  | [optional] 


