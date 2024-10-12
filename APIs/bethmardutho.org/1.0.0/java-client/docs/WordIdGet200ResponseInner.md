

# WordIdGet200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eastern** | **String** | Eastern vocalized form of this Syriac word. |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | The gender of a Syriac adjective, noun, numeral, pronoun, suffix, or verb. |  [optional] |
|**glosses** | **Map&lt;String, List&lt;String&gt;&gt;** | A hashmap with language name as a key and and array of text strings in that language |  [optional] |
|**hasSeyame** | **Boolean** | Indicator to the presence of a Seyame in this word. |  [optional] |
|**isEnclitic** | **Boolean** | Indicator if this Syriac word is an enclitic. |  [optional] |
|**isLexicalForm** | **Boolean** | Indicator if this Syriac word is the lexeme form. |  [optional] |
|**isTheoretical** | **Boolean** | Indicator if this Syriac word is theoretical or it is attested. |  [optional] |
|**kaylo** | [**KayloEnum**](#KayloEnum) | The Kaylo or conjugation of a Syriac verb. |  [optional] |
|**lexeme** | **Object** |  |  |
|**number** | [**NumberEnum**](#NumberEnum) | The number of a Syriac adjective, noun, suffix, or verb. |  [optional] |
|**person** | [**PersonEnum**](#PersonEnum) | The person of a Syriac verb. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of a Syriac substantive or adjective. |  [optional] |
|**suffixGender** | **Object** |  |  [optional] |
|**suffixNumber** | **Object** |  |  [optional] |
|**suffixPerson** | **Object** |  |  [optional] |
|**suffixType** | [**SuffixTypeEnum**](#SuffixTypeEnum) | The type of suffix attached to the Syriac word. |  [optional] |
|**syriac** | **String** | Consonantal form of this Syriac word. |  |
|**tense** | [**TenseEnum**](#TenseEnum) | The tense of a Syriac verb. |  [optional] |
|**western** | **String** | Western vocalized form of this Syriac word. |  [optional] |
|**word** | [**WordIdGet200ResponseInnerWord**](WordIdGet200ResponseInnerWord.md) |  |  |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| COMMON | &quot;common&quot; |
| FEMININE | &quot;feminine&quot; |
| MASCULINE | &quot;masculine&quot; |



## Enum: KayloEnum

| Name | Value |
|---- | -----|
| ETTAPH_AL_PASS_OF_TAPH_EL_ | &quot;ettaphʿal (pass. of Taphʿel)&quot; |
| IVA | &quot;IVa&quot; |
| IVP | &quot;IVp&quot; |
| P_AL | &quot;pʿal&quot; |
| PA_EL | &quot;paʿʿel&quot; |
| SHAPH_EL | &quot;shaphʿel&quot; |
| PALPEL | &quot;palpel&quot; |
| ETHPA_AL | &quot;ethpaʿʿal&quot; |
| APH_EL | &quot;aphʿel&quot; |
| ETTAPH_AL | &quot;ettaphʿal&quot; |
| SAPH_EL | &quot;saphʿel&quot; |
| ETHP_EL | &quot;ethpʿel&quot; |
| P | &quot;p&quot; |
| ETHP | &quot;ethp&quot; |
| ETHPALPAL | &quot;ethpalpal&quot; |
| PAY_EL | &quot;payʿel&quot; |
| ETHPAY_AL | &quot;ethpayʿal&quot; |
| ETHPAR_AL | &quot;ethparʿal&quot; |
| ESHTAPH_AL | &quot;eshtaphʿal&quot; |
| ETHPAW_AL | &quot;ethpawʿal&quot; |
| PAW_EL | &quot;pawʿel&quot; |
| PALPAL | &quot;palpal&quot; |
| PAM_EL | &quot;pamʿel&quot; |
| TAPH_EL | &quot;taphʿel&quot; |
| PAR_EL | &quot;parʿel&quot; |
| ESTAPH_AL | &quot;estaphʿal&quot; |
| ETHPA_LI | &quot;ethpaʿli&quot; |
| PA_LI | &quot;paʿli&quot; |



## Enum: NumberEnum

| Name | Value |
|---- | -----|
| PLURAL | &quot;plural&quot; |
| SINGULAR | &quot;singular&quot; |



## Enum: PersonEnum

| Name | Value |
|---- | -----|
| FIRST | &quot;first&quot; |
| SECOND | &quot;second&quot; |
| THIRD | &quot;third&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ABSOLUTE | &quot;absolute&quot; |
| EMPHATIC | &quot;emphatic&quot; |
| CONSTRUCT | &quot;construct&quot; |



## Enum: SuffixTypeEnum

| Name | Value |
|---- | -----|
| CONTRACTION | &quot;contraction&quot; |
| SUFFIX | &quot;suffix&quot; |



## Enum: TenseEnum

| Name | Value |
|---- | -----|
| ACTIVE_PARTICIPLE | &quot;active participle&quot; |
| IMPERATIVE | &quot;imperative&quot; |
| IMPERFECT | &quot;imperfect&quot; |
| INFINITIVE | &quot;infinitive&quot; |
| PARTICIPLE | &quot;participle&quot; |
| PASSIVE_PARTICIPLE | &quot;passive participle&quot; |
| PERFECT | &quot;perfect&quot; |



