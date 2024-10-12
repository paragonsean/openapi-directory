

# SynthesizeSpeechRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**engine** | [**EngineEnum**](#EngineEnum) | &lt;p&gt;Specifies the engine (&lt;code&gt;standard&lt;/code&gt; or &lt;code&gt;neural&lt;/code&gt;) for Amazon Polly to use when processing input text for speech synthesis. For information on Amazon Polly voices and which voices are available in standard-only, NTTS-only, and both standard and NTTS formats, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/voicelist.html\&quot;&gt;Available Voices&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;NTTS-only voices&lt;/b&gt; &lt;/p&gt; &lt;p&gt;When using NTTS-only voices such as Kevin (en-US), this parameter is required and must be set to &lt;code&gt;neural&lt;/code&gt;. If the engine is not specified, or is set to &lt;code&gt;standard&lt;/code&gt;, this will result in an error. &lt;/p&gt; &lt;p&gt;Type: String&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;standard&lt;/code&gt; | &lt;code&gt;neural&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Required: Yes&lt;/p&gt; &lt;p&gt; &lt;b&gt;Standard voices&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For standard voices, this is not required; the engine parameter defaults to &lt;code&gt;standard&lt;/code&gt;. If the engine is not specified, or is set to &lt;code&gt;standard&lt;/code&gt; and an NTTS-only voice is selected, this will result in an error. &lt;/p&gt; |  [optional] |
|**languageCode** | [**LanguageCodeEnum**](#LanguageCodeEnum) | &lt;p&gt;Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). &lt;/p&gt; &lt;p&gt;If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\&quot;&gt;DescribeVoices&lt;/a&gt; operation for the &lt;code&gt;LanguageCode&lt;/code&gt; parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.&lt;/p&gt; |  [optional] |
|**lexiconNames** | **List&lt;String&gt;** | List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html\&quot;&gt;PutLexicon&lt;/a&gt;. |  [optional] |
|**outputFormat** | [**OutputFormatEnum**](#OutputFormatEnum) | &lt;p&gt; The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. &lt;/p&gt; &lt;p&gt;When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format. &lt;/p&gt; |  |
|**sampleRate** | **String** | &lt;p&gt;The audio frequency specified in Hz.&lt;/p&gt; &lt;p&gt;The valid values for mp3 and ogg_vorbis are \&quot;8000\&quot;, \&quot;16000\&quot;, \&quot;22050\&quot;, and \&quot;24000\&quot;. The default value for standard voices is \&quot;22050\&quot;. The default value for neural voices is \&quot;24000\&quot;.&lt;/p&gt; &lt;p&gt;Valid values for pcm are \&quot;8000\&quot; and \&quot;16000\&quot; The default value is \&quot;16000\&quot;. &lt;/p&gt; |  [optional] |
|**speechMarkTypes** | **List&lt;SpeechMarkType&gt;** | The type of speech marks returned for the input text. |  [optional] |
|**text** | **String** |  Input text to synthesize. If you specify &lt;code&gt;ssml&lt;/code&gt; as the &lt;code&gt;TextType&lt;/code&gt;, follow the SSML format for the input text.  |  |
|**textType** | [**TextTypeEnum**](#TextTypeEnum) |  Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/ssml.html\&quot;&gt;Using SSML&lt;/a&gt;. |  [optional] |
|**voiceId** | [**VoiceIdEnum**](#VoiceIdEnum) |  Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\&quot;&gt;DescribeVoices&lt;/a&gt; operation.  |  |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;standard&quot; |
| NEURAL | &quot;neural&quot; |



## Enum: LanguageCodeEnum

| Name | Value |
|---- | -----|
| ARB | &quot;arb&quot; |
| CMN_CN | &quot;cmn-CN&quot; |
| CY_GB | &quot;cy-GB&quot; |
| DA_DK | &quot;da-DK&quot; |
| DE_DE | &quot;de-DE&quot; |
| EN_AU | &quot;en-AU&quot; |
| EN_GB | &quot;en-GB&quot; |
| EN_GB_WLS | &quot;en-GB-WLS&quot; |
| EN_IN | &quot;en-IN&quot; |
| EN_US | &quot;en-US&quot; |
| ES_ES | &quot;es-ES&quot; |
| ES_MX | &quot;es-MX&quot; |
| ES_US | &quot;es-US&quot; |
| FR_CA | &quot;fr-CA&quot; |
| FR_FR | &quot;fr-FR&quot; |
| IS_IS | &quot;is-IS&quot; |
| IT_IT | &quot;it-IT&quot; |
| JA_JP | &quot;ja-JP&quot; |
| HI_IN | &quot;hi-IN&quot; |
| KO_KR | &quot;ko-KR&quot; |
| NB_NO | &quot;nb-NO&quot; |
| NL_NL | &quot;nl-NL&quot; |
| PL_PL | &quot;pl-PL&quot; |
| PT_BR | &quot;pt-BR&quot; |
| PT_PT | &quot;pt-PT&quot; |
| RO_RO | &quot;ro-RO&quot; |
| RU_RU | &quot;ru-RU&quot; |
| SV_SE | &quot;sv-SE&quot; |
| TR_TR | &quot;tr-TR&quot; |
| EN_NZ | &quot;en-NZ&quot; |
| EN_ZA | &quot;en-ZA&quot; |
| CA_ES | &quot;ca-ES&quot; |
| DE_AT | &quot;de-AT&quot; |
| YUE_CN | &quot;yue-CN&quot; |
| AR_AE | &quot;ar-AE&quot; |
| FI_FI | &quot;fi-FI&quot; |
| EN_IE | &quot;en-IE&quot; |
| NL_BE | &quot;nl-BE&quot; |
| FR_BE | &quot;fr-BE&quot; |



## Enum: OutputFormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;json&quot; |
| MP3 | &quot;mp3&quot; |
| OGG_VORBIS | &quot;ogg_vorbis&quot; |
| PCM | &quot;pcm&quot; |



## Enum: TextTypeEnum

| Name | Value |
|---- | -----|
| SSML | &quot;ssml&quot; |
| TEXT | &quot;text&quot; |



## Enum: VoiceIdEnum

| Name | Value |
|---- | -----|
| ADITI | &quot;Aditi&quot; |
| AMY | &quot;Amy&quot; |
| ASTRID | &quot;Astrid&quot; |
| BIANCA | &quot;Bianca&quot; |
| BRIAN | &quot;Brian&quot; |
| CAMILA | &quot;Camila&quot; |
| CARLA | &quot;Carla&quot; |
| CARMEN | &quot;Carmen&quot; |
| CELINE | &quot;Celine&quot; |
| CHANTAL | &quot;Chantal&quot; |
| CONCHITA | &quot;Conchita&quot; |
| CRISTIANO | &quot;Cristiano&quot; |
| DORA | &quot;Dora&quot; |
| EMMA | &quot;Emma&quot; |
| ENRIQUE | &quot;Enrique&quot; |
| EWA | &quot;Ewa&quot; |
| FILIZ | &quot;Filiz&quot; |
| GABRIELLE | &quot;Gabrielle&quot; |
| GERAINT | &quot;Geraint&quot; |
| GIORGIO | &quot;Giorgio&quot; |
| GWYNETH | &quot;Gwyneth&quot; |
| HANS | &quot;Hans&quot; |
| INES | &quot;Ines&quot; |
| IVY | &quot;Ivy&quot; |
| JACEK | &quot;Jacek&quot; |
| JAN | &quot;Jan&quot; |
| JOANNA | &quot;Joanna&quot; |
| JOEY | &quot;Joey&quot; |
| JUSTIN | &quot;Justin&quot; |
| KARL | &quot;Karl&quot; |
| KENDRA | &quot;Kendra&quot; |
| KEVIN | &quot;Kevin&quot; |
| KIMBERLY | &quot;Kimberly&quot; |
| LEA | &quot;Lea&quot; |
| LIV | &quot;Liv&quot; |
| LOTTE | &quot;Lotte&quot; |
| LUCIA | &quot;Lucia&quot; |
| LUPE | &quot;Lupe&quot; |
| MADS | &quot;Mads&quot; |
| MAJA | &quot;Maja&quot; |
| MARLENE | &quot;Marlene&quot; |
| MATHIEU | &quot;Mathieu&quot; |
| MATTHEW | &quot;Matthew&quot; |
| MAXIM | &quot;Maxim&quot; |
| MIA | &quot;Mia&quot; |
| MIGUEL | &quot;Miguel&quot; |
| MIZUKI | &quot;Mizuki&quot; |
| NAJA | &quot;Naja&quot; |
| NICOLE | &quot;Nicole&quot; |
| OLIVIA | &quot;Olivia&quot; |
| PENELOPE | &quot;Penelope&quot; |
| RAVEENA | &quot;Raveena&quot; |
| RICARDO | &quot;Ricardo&quot; |
| RUBEN | &quot;Ruben&quot; |
| RUSSELL | &quot;Russell&quot; |
| SALLI | &quot;Salli&quot; |
| SEOYEON | &quot;Seoyeon&quot; |
| TAKUMI | &quot;Takumi&quot; |
| TATYANA | &quot;Tatyana&quot; |
| VICKI | &quot;Vicki&quot; |
| VITORIA | &quot;Vitoria&quot; |
| ZEINA | &quot;Zeina&quot; |
| ZHIYU | &quot;Zhiyu&quot; |
| ARIA | &quot;Aria&quot; |
| AYANDA | &quot;Ayanda&quot; |
| ARLET | &quot;Arlet&quot; |
| HANNAH | &quot;Hannah&quot; |
| ARTHUR | &quot;Arthur&quot; |
| DANIEL | &quot;Daniel&quot; |
| LIAM | &quot;Liam&quot; |
| PEDRO | &quot;Pedro&quot; |
| KAJAL | &quot;Kajal&quot; |
| HIUJIN | &quot;Hiujin&quot; |
| LAURA | &quot;Laura&quot; |
| ELIN | &quot;Elin&quot; |
| IDA | &quot;Ida&quot; |
| SUVI | &quot;Suvi&quot; |
| OLA | &quot;Ola&quot; |
| HALA | &quot;Hala&quot; |
| ANDRES | &quot;Andres&quot; |
| SERGIO | &quot;Sergio&quot; |
| REMI | &quot;Remi&quot; |
| ADRIANO | &quot;Adriano&quot; |
| THIAGO | &quot;Thiago&quot; |
| RUTH | &quot;Ruth&quot; |
| STEPHEN | &quot;Stephen&quot; |
| KAZUHA | &quot;Kazuha&quot; |
| TOMOKO | &quot;Tomoko&quot; |
| NIAMH | &quot;Niamh&quot; |
| SOFIE | &quot;Sofie&quot; |
| LISA | &quot;Lisa&quot; |
| ISABELLE | &quot;Isabelle&quot; |



