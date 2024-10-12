# SedraIvApi.WordIdGet200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eastern** | **String** | Eastern vocalized form of this Syriac word. | [optional] 
**gender** | **String** | The gender of a Syriac adjective, noun, numeral, pronoun, suffix, or verb. | [optional] 
**glosses** | **{String: [String]}** | A hashmap with language name as a key and and array of text strings in that language | [optional] 
**hasSeyame** | **Boolean** | Indicator to the presence of a Seyame in this word. | [optional] 
**isEnclitic** | **Boolean** | Indicator if this Syriac word is an enclitic. | [optional] 
**isLexicalForm** | **Boolean** | Indicator if this Syriac word is the lexeme form. | [optional] 
**isTheoretical** | **Boolean** | Indicator if this Syriac word is theoretical or it is attested. | [optional] 
**kaylo** | **String** | The Kaylo or conjugation of a Syriac verb. | [optional] 
**lexeme** | **Object** |  | 
**number** | **String** | The number of a Syriac adjective, noun, suffix, or verb. | [optional] 
**person** | **String** | The person of a Syriac verb. | [optional] 
**state** | **String** | The state of a Syriac substantive or adjective. | [optional] 
**suffixGender** | **Object** |  | [optional] 
**suffixNumber** | **Object** |  | [optional] 
**suffixPerson** | **Object** |  | [optional] 
**suffixType** | **String** | The type of suffix attached to the Syriac word. | [optional] 
**syriac** | **String** | Consonantal form of this Syriac word. | 
**tense** | **String** | The tense of a Syriac verb. | [optional] 
**western** | **String** | Western vocalized form of this Syriac word. | [optional] 
**word** | [**WordIdGet200ResponseInnerWord**](WordIdGet200ResponseInnerWord.md) |  | 



## Enum: GenderEnum


* `common` (value: `"common"`)

* `feminine` (value: `"feminine"`)

* `masculine` (value: `"masculine"`)





## Enum: KayloEnum


* `ettaphʿal (pass. of Taphʿel)` (value: `"ettaphʿal (pass. of Taphʿel)"`)

* `IVa` (value: `"IVa"`)

* `IVp` (value: `"IVp"`)

* `pʿal` (value: `"pʿal"`)

* `paʿʿel` (value: `"paʿʿel"`)

* `shaphʿel` (value: `"shaphʿel"`)

* `palpel` (value: `"palpel"`)

* `ethpaʿʿal` (value: `"ethpaʿʿal"`)

* `aphʿel` (value: `"aphʿel"`)

* `ettaphʿal` (value: `"ettaphʿal"`)

* `saphʿel` (value: `"saphʿel"`)

* `ethpʿel` (value: `"ethpʿel"`)

* `p` (value: `"p"`)

* `ethp` (value: `"ethp"`)

* `ethpalpal` (value: `"ethpalpal"`)

* `payʿel` (value: `"payʿel"`)

* `ethpayʿal` (value: `"ethpayʿal"`)

* `ethparʿal` (value: `"ethparʿal"`)

* `eshtaphʿal` (value: `"eshtaphʿal"`)

* `ethpawʿal` (value: `"ethpawʿal"`)

* `pawʿel` (value: `"pawʿel"`)

* `palpal` (value: `"palpal"`)

* `pamʿel` (value: `"pamʿel"`)

* `taphʿel` (value: `"taphʿel"`)

* `parʿel` (value: `"parʿel"`)

* `estaphʿal` (value: `"estaphʿal"`)

* `ethpaʿli` (value: `"ethpaʿli"`)

* `paʿli` (value: `"paʿli"`)





## Enum: NumberEnum


* `plural` (value: `"plural"`)

* `singular` (value: `"singular"`)





## Enum: PersonEnum


* `first` (value: `"first"`)

* `second` (value: `"second"`)

* `third` (value: `"third"`)





## Enum: StateEnum


* `absolute` (value: `"absolute"`)

* `emphatic` (value: `"emphatic"`)

* `construct` (value: `"construct"`)





## Enum: SuffixTypeEnum


* `contraction` (value: `"contraction"`)

* `suffix` (value: `"suffix"`)





## Enum: TenseEnum


* `active participle` (value: `"active participle"`)

* `imperative` (value: `"imperative"`)

* `imperfect` (value: `"imperfect"`)

* `infinitive` (value: `"infinitive"`)

* `participle` (value: `"participle"`)

* `passive participle` (value: `"passive participle"`)

* `perfect` (value: `"perfect"`)




