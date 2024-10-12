# AmazonPolly.StartSpeechSynthesisTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **String** | Specifies the engine (&lt;code&gt;standard&lt;/code&gt; or &lt;code&gt;neural&lt;/code&gt;) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error. | [optional] 
**languageCode** | **String** | &lt;p&gt;Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). &lt;/p&gt; &lt;p&gt;If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\&quot;&gt;DescribeVoices&lt;/a&gt; operation for the &lt;code&gt;LanguageCode&lt;/code&gt; parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.&lt;/p&gt; | [optional] 
**lexiconNames** | **[String]** | List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.  | [optional] 
**outputFormat** | **String** | The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.  | 
**outputS3BucketName** | **String** | Amazon S3 bucket name to which the output file will be saved. | 
**outputS3KeyPrefix** | **String** | The Amazon S3 key prefix for the output speech file. | [optional] 
**sampleRate** | **String** | &lt;p&gt;The audio frequency specified in Hz.&lt;/p&gt; &lt;p&gt;The valid values for mp3 and ogg_vorbis are \&quot;8000\&quot;, \&quot;16000\&quot;, \&quot;22050\&quot;, and \&quot;24000\&quot;. The default value for standard voices is \&quot;22050\&quot;. The default value for neural voices is \&quot;24000\&quot;.&lt;/p&gt; &lt;p&gt;Valid values for pcm are \&quot;8000\&quot; and \&quot;16000\&quot; The default value is \&quot;16000\&quot;. &lt;/p&gt; | [optional] 
**snsTopicArn** | **String** | ARN for the SNS topic optionally used for providing status notification for a speech synthesis task. | [optional] 
**speechMarkTypes** | [**[SpeechMarkType]**](SpeechMarkType.md) | The type of speech marks returned for the input text. | [optional] 
**text** | **String** | The input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text.  | 
**textType** | **String** | Specifies whether the input text is plain text or SSML. The default value is plain text.  | [optional] 
**voiceId** | **String** | Voice ID to use for the synthesis.  | 



## Enum: EngineEnum


* `standard` (value: `"standard"`)

* `neural` (value: `"neural"`)





## Enum: LanguageCodeEnum


* `arb` (value: `"arb"`)

* `cmn-CN` (value: `"cmn-CN"`)

* `cy-GB` (value: `"cy-GB"`)

* `da-DK` (value: `"da-DK"`)

* `de-DE` (value: `"de-DE"`)

* `en-AU` (value: `"en-AU"`)

* `en-GB` (value: `"en-GB"`)

* `en-GB-WLS` (value: `"en-GB-WLS"`)

* `en-IN` (value: `"en-IN"`)

* `en-US` (value: `"en-US"`)

* `es-ES` (value: `"es-ES"`)

* `es-MX` (value: `"es-MX"`)

* `es-US` (value: `"es-US"`)

* `fr-CA` (value: `"fr-CA"`)

* `fr-FR` (value: `"fr-FR"`)

* `is-IS` (value: `"is-IS"`)

* `it-IT` (value: `"it-IT"`)

* `ja-JP` (value: `"ja-JP"`)

* `hi-IN` (value: `"hi-IN"`)

* `ko-KR` (value: `"ko-KR"`)

* `nb-NO` (value: `"nb-NO"`)

* `nl-NL` (value: `"nl-NL"`)

* `pl-PL` (value: `"pl-PL"`)

* `pt-BR` (value: `"pt-BR"`)

* `pt-PT` (value: `"pt-PT"`)

* `ro-RO` (value: `"ro-RO"`)

* `ru-RU` (value: `"ru-RU"`)

* `sv-SE` (value: `"sv-SE"`)

* `tr-TR` (value: `"tr-TR"`)

* `en-NZ` (value: `"en-NZ"`)

* `en-ZA` (value: `"en-ZA"`)

* `ca-ES` (value: `"ca-ES"`)

* `de-AT` (value: `"de-AT"`)

* `yue-CN` (value: `"yue-CN"`)

* `ar-AE` (value: `"ar-AE"`)

* `fi-FI` (value: `"fi-FI"`)

* `en-IE` (value: `"en-IE"`)

* `nl-BE` (value: `"nl-BE"`)

* `fr-BE` (value: `"fr-BE"`)





## Enum: OutputFormatEnum


* `json` (value: `"json"`)

* `mp3` (value: `"mp3"`)

* `ogg_vorbis` (value: `"ogg_vorbis"`)

* `pcm` (value: `"pcm"`)





## Enum: TextTypeEnum


* `ssml` (value: `"ssml"`)

* `text` (value: `"text"`)





## Enum: VoiceIdEnum


* `Aditi` (value: `"Aditi"`)

* `Amy` (value: `"Amy"`)

* `Astrid` (value: `"Astrid"`)

* `Bianca` (value: `"Bianca"`)

* `Brian` (value: `"Brian"`)

* `Camila` (value: `"Camila"`)

* `Carla` (value: `"Carla"`)

* `Carmen` (value: `"Carmen"`)

* `Celine` (value: `"Celine"`)

* `Chantal` (value: `"Chantal"`)

* `Conchita` (value: `"Conchita"`)

* `Cristiano` (value: `"Cristiano"`)

* `Dora` (value: `"Dora"`)

* `Emma` (value: `"Emma"`)

* `Enrique` (value: `"Enrique"`)

* `Ewa` (value: `"Ewa"`)

* `Filiz` (value: `"Filiz"`)

* `Gabrielle` (value: `"Gabrielle"`)

* `Geraint` (value: `"Geraint"`)

* `Giorgio` (value: `"Giorgio"`)

* `Gwyneth` (value: `"Gwyneth"`)

* `Hans` (value: `"Hans"`)

* `Ines` (value: `"Ines"`)

* `Ivy` (value: `"Ivy"`)

* `Jacek` (value: `"Jacek"`)

* `Jan` (value: `"Jan"`)

* `Joanna` (value: `"Joanna"`)

* `Joey` (value: `"Joey"`)

* `Justin` (value: `"Justin"`)

* `Karl` (value: `"Karl"`)

* `Kendra` (value: `"Kendra"`)

* `Kevin` (value: `"Kevin"`)

* `Kimberly` (value: `"Kimberly"`)

* `Lea` (value: `"Lea"`)

* `Liv` (value: `"Liv"`)

* `Lotte` (value: `"Lotte"`)

* `Lucia` (value: `"Lucia"`)

* `Lupe` (value: `"Lupe"`)

* `Mads` (value: `"Mads"`)

* `Maja` (value: `"Maja"`)

* `Marlene` (value: `"Marlene"`)

* `Mathieu` (value: `"Mathieu"`)

* `Matthew` (value: `"Matthew"`)

* `Maxim` (value: `"Maxim"`)

* `Mia` (value: `"Mia"`)

* `Miguel` (value: `"Miguel"`)

* `Mizuki` (value: `"Mizuki"`)

* `Naja` (value: `"Naja"`)

* `Nicole` (value: `"Nicole"`)

* `Olivia` (value: `"Olivia"`)

* `Penelope` (value: `"Penelope"`)

* `Raveena` (value: `"Raveena"`)

* `Ricardo` (value: `"Ricardo"`)

* `Ruben` (value: `"Ruben"`)

* `Russell` (value: `"Russell"`)

* `Salli` (value: `"Salli"`)

* `Seoyeon` (value: `"Seoyeon"`)

* `Takumi` (value: `"Takumi"`)

* `Tatyana` (value: `"Tatyana"`)

* `Vicki` (value: `"Vicki"`)

* `Vitoria` (value: `"Vitoria"`)

* `Zeina` (value: `"Zeina"`)

* `Zhiyu` (value: `"Zhiyu"`)

* `Aria` (value: `"Aria"`)

* `Ayanda` (value: `"Ayanda"`)

* `Arlet` (value: `"Arlet"`)

* `Hannah` (value: `"Hannah"`)

* `Arthur` (value: `"Arthur"`)

* `Daniel` (value: `"Daniel"`)

* `Liam` (value: `"Liam"`)

* `Pedro` (value: `"Pedro"`)

* `Kajal` (value: `"Kajal"`)

* `Hiujin` (value: `"Hiujin"`)

* `Laura` (value: `"Laura"`)

* `Elin` (value: `"Elin"`)

* `Ida` (value: `"Ida"`)

* `Suvi` (value: `"Suvi"`)

* `Ola` (value: `"Ola"`)

* `Hala` (value: `"Hala"`)

* `Andres` (value: `"Andres"`)

* `Sergio` (value: `"Sergio"`)

* `Remi` (value: `"Remi"`)

* `Adriano` (value: `"Adriano"`)

* `Thiago` (value: `"Thiago"`)

* `Ruth` (value: `"Ruth"`)

* `Stephen` (value: `"Stephen"`)

* `Kazuha` (value: `"Kazuha"`)

* `Tomoko` (value: `"Tomoko"`)

* `Niamh` (value: `"Niamh"`)

* `Sofie` (value: `"Sofie"`)

* `Lisa` (value: `"Lisa"`)

* `Isabelle` (value: `"Isabelle"`)




