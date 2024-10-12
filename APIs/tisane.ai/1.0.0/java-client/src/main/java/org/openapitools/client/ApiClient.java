/*
 * Tisane API Documentation
 * Tisane is a natural language processing library, providing:  *   standard NLP functionality *   special functions for detection of problematic or abusive content *   low-level NLP like morphological analysis and tokenization of no-space languages (Chinese, Japanese, Thai)       Tisane has monolithic architecture. All the functions are exposed using the same language models and the same analysis process invoked using the [POST /parse](#561264c5-6dbe-4bde-aba3-7defe837989f) method. Other methods in the API are either wrappers based on the process, helper methods, or allow inspection of the language models.  The current section of the documentation describes the two structures used in the parsing & transformation methods.  # Getting Started  This guide describes how to setup your Tisane account. The steps you need to complete are as follows:  *   Step 1 – Create an Account *   Step 2 – Save Your API Key *   Step 3 – Integrate the API       ## Step 1 – Create an Account  Navigate to [Sign up to Tisane API](https://tisane.ai/signup/). The free Community Plan allows up to 50,000 requests but comes with a limitation of 10 requests per minute.  ## Step 2 - Save Your API Key  You will need the API key to make requests. Open your [Developer Profile](https://tisane.ai/developer/) to find your API keys.  ## Step 3 - Integrate with the API  In summary, the POST /parse method has 3 attributes: *content*, *language*, and *settings*. All 3 attributes are mandatory.  For example:   `{\"language\": \"en\", \"content\": \"hello\", \"settings\": {}}`  Read on for more info on the [response](#response-reference) and the [settings](#settings-reference) specs. The method doc pages contain snippets of code for your favorite languages and platforms.  # Response Reference  The response of the [POST /parse](#561264c5-6dbe-4bde-aba3-7defe837989f) method contains several sections displayed or hidden according to the [settings](#settings-reference) provided.  The common attributes are:  *   `text` (string) - the original input *   `reduced_output` (boolean) - if the input is too big, and verbose information like the lexical chunk was requested, the verbose information will not be generated, and this flag will be set to `true` and returned as part of the response *   `sentiment` (floating-point number) - a number in range -1 to 1 indicating the document-level sentiment. Only shown when `document_sentiment` [setting](#settings-reference) is set to `true`. *   `signal2noise` (floating-point number) - a signal to noise ranking of the text, in relation to the array of concepts specified in the `relevant` [setting](#settings-reference). Only shown when the `relevant` setting exists.       ## Abusive or Problematic Content  The `abuse` section is an array of detected instances of content that may violate some terms of use. **NOTE**: the terms of use in online communities may vary, and so it is up to the administrators to determine whether the content is indeed abusive. For instance, it makes no sense to restrict sexual advances in a dating community, or censor profanities when it's accepted in the bulk of the community.  The section exists if instances of abuse are detected and the `abuse` [setting](#settings-reference) is either omitted or set to `true`.  Every instance contains the following attributes:  *   `offset` (unsigned integer) - zero-based offset where the instance starts *   `length` (unsigned integer) - length of the content *   `sentence_index` (unsigned integer) - zero-based index of the sentence containing the instance *   `text` (string) - fragment of text containing the instance (only included if the `snippets` [setting](#settings-reference) is set to `true`) *   `tags` (array of strings) - when exists, provides additional detail about the abuse. For instance, if the fragment is classified as an attempt to sell hard drugs, one of the tags will be *hard_drug*. *   `type` (string) - the type of the abuse *   `severity` (string) - how severe the abuse is. The levels of severity are `low`, `medium`, `high`, and `extreme` *   `explanation` (string) - when available, provides rationale for the annotation; set the `explain` setting to `true` to enable.       The currently supported types are:  *   `personal_attack` - an insult / attack on the addressee, e.g. an instance of cyberbullying. Please note that an attack on a post or a point, or just negative sentiment is not the same as an insult. The line may be blurred at times. See [our Knowledge Base for more information](http://tisane.ai/knowledgebase/how-do-i-detect-personal-attacks/). *   `bigotry` - hate speech aimed at one of the [protected classes](https://en.wikipedia.org/wiki/Protected_group). The hate speech detected is not just racial slurs, but, generally, hostile statements aimed at the group as a whole *   `profanity` - profane language, regardless of the intent *   `sexual_advances` - welcome or unwelcome attempts to gain some sort of sexual favor or gratification *   `criminal_activity` - attempts to sell or procure restricted items, criminal services, issuing death threats, and so on *   `external_contact` - attempts to establish contact or payment via external means of communication, e.g. phone, email, instant messaging (may violate the rules in certain communities, e.g. gig economy portals, e-commerce portals) *   `adult_only` - activities restricted for minors (e.g. consumption of alcohol) *   `mental_issues` - content indicative of suicidal thoughts or depression *   `allegation` - claimed knowledge or accusation of a misconduct (not necessarily crime) *   `provocation` - content likely to provoke an individual or a group *   `disturbing` - graphic descriptions that may disturb readers *   `no_meaningful_content` - unparseable gibberish without apparent meaning *   `data_leak` - private data like passwords, ID numbers, etc. *   `spam` - (RESERVED) spam content *   `generic` - undefined       ## Sentiment Analysis  The `sentiment_expressions` section is an array of detected fragments indicating the attitude towards aspects or entities.  The section exists if sentiment is detected and the `sentiment` [setting](#settings-reference) is either omitted or set to `true`.  Every instance contains the following attributes:  *   `offset` (unsigned integer) - zero-based offset where the instance starts *   `length` (unsigned integer) - length of the content *   `sentence_index` (unsigned integer) - zero-based index of the sentence containing the instance *   `text` (string) - fragment of text containing the instance (only included if the `snippets` setting is set to `true`) *   `polarity` (string) - whether the attitude is `positive`, `negative`, or `mixed`. Additionally, there is a `default` sentiment used for cases when the entire snippet has been pre-classified. For instance, if a review is split into two portions, *What did you like?* and *What did you not like?*, and the reviewer replies briefly, e.g. *The quiet. The service*, the utterance itself has no sentiment value. When the calling application is aware of the intended sentiment, the *default* sentiment simply provides the targets / aspects, which will be then added the sentiment externally. *   `targets` (array of strings) - when available, provides set of aspects and/or entities which are the targets of the sentiment. For instance, when the utterance is, *The breakfast was yummy but the staff is unfriendly*, the targets for the two sentiment expressions are `meal` and `staff`. Named entities may also be targets of the sentiment. *   `reasons` (array of strings) - when available, provides reasons for the sentiment. In the example utterance above (*The breakfast was yummy but the staff is unfriendly*), the `reasons` array for the `staff` is `[\"unfriendly\"]`, while the `reasons` array for `meal` is `[\"tasty\"]`. *   `explanation` (string) - when available, provides rationale for the sentiment; set the `explain` setting to `true` to enable.       Example:  ``` json \"sentiment_expressions\": [         {             \"sentence_index\": 0,              \"offset\": 0,              \"length\": 32,              \"polarity\": \"positive\",              \"reasons\": [\"close\"],              \"targets\": [\"location\"]          },          {             \"sentence_index\": 0,              \"offset\": 38,              \"length\": 29,              \"polarity\": \"negative\",              \"reasons\": [\"disrespectful\"],              \"targets\": [\"staff\"]          }      ]  ```  ## Entities  The `entities_summary` section is an array of named entity objects detected in the text.  The section exists if named entities are detected and the `entities` [setting](#settings-reference) is either omitted or set to `true`.  Every entity contains the following attributes:  *   `name` (string) - the most complete name of the entity in the text of all the mentions *   `ref_lemma` (string) - when available, the dictionary form of the entity in the reference language (English) regardless of the input language *   `type` (string) - a string or an array of strings specifying the type of the entity, such as `person`, `organization`, `numeric`, `amount_of_money`, `place`. Certain entities, like countries, may have several types (because a country is both a `place` and an `organization`). *   `subtype` (string) - a string indicating the subtype of the entity *   `mentions` (array of objects) - a set of instances where the entity was mentioned in the text       Every mention contains the following attributes:  *   `offset` (unsigned integer) - zero-based offset where the instance starts *   `length` (unsigned integer) - length of the content *   `sentence_index` (unsigned integer) - zero-based index of the sentence containing the instance *   `text` (string) - fragment of text containing the instance (only included if the `snippets` setting is set to `true`)       Example:  ``` json  \"entities_summary\": [         {             \"type\": \"person\",              \"name\": \"John Smith\",              \"ref_lemma\": \"John Smith\",              \"mentions\": [                 {                     \"sentence_index\": 0,                      \"offset\": 0,                      \"length\": 10 }              ]          }     ,          {             \"type\": [ \"organization\", \"place\" ]         ,              \"name\": \"UK\",              \"ref_lemma\": \"U.K.\",              \"mentions\": [                 {                     \"sentence_index\": 0,                      \"offset\": 40,                      \"length\": 2 }              ]          }      ]  ```  ### Entity Types and Subtypes  The currently supported entity types are:  *   `person`, with optional subtypes: `fictional_character`, `important_person`, `spiritual_being` *   `organization` (note that a country is both an organization and a place) *   `place` *   `time_range` *   `date` *   `time` *   `hashtag` *   `email` *   `amount_of_money` *   `phone` phone number, either domestic or international, in a variety of formats *   `role` (a social role, e.g. position in an organization) *   `software` *   `website` (URL), with an optional subtype: `tor` for Onion links; note that web services may also have the `software` type assigned *   `weight` *   `bank_account` only IBAN format is supported; subtypes: `iban` *   `credit_card`, with optional subtypes: `visa`, `mastercard`, `american_express`, `diners_club`, `discovery`, `jcb`, `unionpay` *   `coordinates` (GPS coordinates) *   `credential`, with optional subtypes: `md5`, `sha-1` *   `crypto`, with optional subtypes: `bitcoin`, `ethereum`, `monero`, `monero_payment_id`, `litecoin`, `dash` *   `event` *   `file` only Windows pathnames are supported; subtypes: `windows`, `facebook` (for images downloaded from Facebook) *   `flight_code` *   `identifier` *   `ip_address`, subtypes: `v4`, `v6` *   `mac_address` *   `numeric` (an unclassified numeric entity) *   `username`       ## Topics  The `topics` section is an array of topics (subjects, domains, themes in other terms) detected in the text.  The section exists if topics are detected and the `topics` [setting](#settings-reference) is either omitted or set to `true`.  By default, a topic is a string. If `topic_stats` [setting](#settings-reference) is set to `true`, then every entry in the array contains:  *   `topic` (string) - the topic itself *   `coverage` (floating-point number) - a number between 0 and 1, indicating the ratio between the number of sentences where the topic is detected to the total number of sentences       ## Long-Term Memory  The `memory` section contains optional context to pass to the `settings` in subsequent messages in the same conversation thread. See [Context and Long-Term Memory](#context-and-long-term-memory) for more details.  ## Low-Level: Sentences, Phrases, and Words  Tisane allows obtaining more in-depth data, specifically:  *   sentences and their corrected form, if a misspelling was detected *   lexical chunks and their grammatical and stylistic features *   parse trees and phrases       The `sentence_list` section is generated if the `words` or the `parses` [setting](#settings-reference) is set to `true`.  Every sentence structure in the list contains:  *   `offset` (unsigned integer) - zero-based offset where the sentence starts *   `length` (unsigned integer) - length of the sentence *   `text` (string) - the sentence itself *   `corrected_text` (string) - if a misspelling was detected and the spellchecking is active, contains the automatically corrected text *   `words` (array of structures) - if `words` [setting](#settings-reference) is set to `true`, generates extended information about every lexical chunk. (The term \"word\" is used for the sake of simplicity, however, it may not be linguistically correct to equate lexical chunks with words.) *   `parse_tree` (object) - if `parses` [setting](#settings-reference) is set to `true`, generates information about the parse tree and the phrases detected in the sentence. *   `nbest_parses` (array of parse objects) if `parses` [setting](#settings-reference) is set to `true` and `deterministic` [setting](#settings-reference) is set to `false`, generates information about the parse trees that were deemed close enough to the best one but not the best.       ### Words  Every lexical chunk (\"word\") structure in the `words` array contains:  *   `type` (string) - the type of the element: `punctuation` for punctuation marks, `numeral` for numerals, or `word` for everything else *   `text` (string) - the text *   `offset` (unsigned integer) - zero-based offset where the element starts *   `length` (unsigned integer) - length of the element *   `corrected_text` (string) - if a misspelling is detected, the corrected form *   `lettercase` (string) - the original letter case: `upper`, `capitalized`, or `mixed`. If lowercase or no case, the attribute is omitted. *   `stopword` (boolean) - determines whether the word is a [stopword](https://en.wikipedia.org/wiki/Stop_words) *   `grammar` (array of strings or structures) - generates the list of grammar features associated with the `word`. If the `feature_standard` setting is defined as `native`, then every feature is an object containing a numeral (`index`) and a string (`value`). Otherwise, every feature is a plain string       #### Advanced  For lexical words only:  *   `role` (string) - semantic role, like `agent` or `patient`. Note that in passive voice, the semantic roles are reverse to the syntactic roles. E.g. in a sentence like *The car was driven by David*, *car* is the patient, and *David* is the agent. *   `numeric_value` (floating-point number) - the numeric value, if the chunk has a value associated with it *   `family` (integer number) - the ID of the family associated with the disambiguated word-sense of the lexical chunk *   `definition` (string) - the definition of the family, if the `fetch_definitions` [setting](#settings-reference) is set to `true` *   `lexeme` (integer number) - the ID of the lexeme entry associated with the disambiguated word-sense of the lexical chunk *   `nondictionary_pattern` (integer number) - the ID of a non-dictionary pattern that matched, if the word was not in the language model but was classified by the nondictionary heuristics *   `style` (array of strings or structures) - generates the list of style features associated with the `word`. Only if the `feature_standard` setting is set to `native` or `description` *   `semantics` (array of strings or structures) - generates the list of semantic features associated with the `word`. Only if the `feature_standard` setting is set to `native` or `description` *   `segmentation` (structure) - generates info about the selected segmentation, if there are several possibilities to segment the current lexical chunk and the `deterministic` setting is set to `false`. A segmentation is simply an array of `word` structures. *   `other_segmentations` (array of structures) - generates info about the segmentations deemed incorrect during the disambiguation process. Every entry has the same structure as the `segmentation` structure. *   `nbest_senses` (array of structures) - when the `deterministic` setting is set to `false`, generates a set of hypotheses that were deemed incorrect by the disambiguation process. Every hypothesis contains the following attributes: `grammar`, `style`, and `semantics`, identical in structure to their counterparts above; and `senses`, an array of word-senses associated with every hypothesis. Every sense has a `family`, which is an ID of the associated family; and, if the `fetch_definitions` setting is set to `true`, `definition` and `ref_lemma` of that family.       For punctuation marks only:  *   `id` (integer number) - the ID of the punctuation mark *   `behavior` (string) - the behavior code of the punctuation mark. Values: `sentenceTerminator`, `genericComma`, `bracketStart`, `bracketEnd`, `scopeDelimiter`, `hyphen`, `quoteStart`, `quoteEnd`, `listComma` (for East-Asian enumeration commas like *、*)       ### Parse Trees and Phrases  Every parse tree, or more accurately, parse forest, is a collection of phrases, hierarchically linked to each other.  At the top level of the parse, there is an array of root phrases under the `phrases` element and the numeric `id` associated with it. Every phrase may have children phrases. Every phrase has the following attributes:  *   `type` (string) - a [Penn treebank phrase tag](http://nliblog.com/wiki/knowledge-base-2/nlp-1-natural-language-processing/penn-treebank/penn-treebank-phrase-level-tags/) denoting the type of the phrase, e.g. *S*, *VP*, *NP*, etc. *   `family` (integer number) - an ID of the phrase family *   `offset` (unsigned integer) - a zero-based offset where the phrase starts *   `length` (unsigned integer) - the span of the phrase *   `role` (string) - the semantic role of the phrase, if any, analogous to that of the words *   `text` (string) - the phrase text, where the phrase members are delimited by the vertical bar character. Children phrases are enclosed in brackets. E.g., *driven|by|David* or *(The|car)|was|(driven|by|David)*.       Example:  ``` json \"parse_tree\": { \"id\": 4, \"phrases\": [ {         \"type\": \"S\",         \"family\": 1451,         \"offset\": 0,         \"length\": 27,         \"text\": \"(The|car)|was|(driven|by|David)\",         \"children\": [                 {                         \"type\": \"NP\",                         \"family\": 1081,                         \"offset\": 0,                         \"length\": 7,                         \"text\": \"The|car\",                         \"role\": \"patient\"                 },                 {                         \"type\": \"VP\",                         \"family\": 1172,                         \"offset\": 12,                         \"length\": 15,                         \"text\": \"driven|by|David\",                         \"role\": \"verb\"                 }         ] }  ```  ### Context-Aware Spelling Correction  Tisane supports automatic, context-aware spelling correction. Whether it's a misspelling or a purported obfuscation, Tisane attempts to deduce the intended meaning, if the language model does not recognize the word.  When or if it's found, Tisane adds the `corrected_text` attribute to the word (if the words / lexical chunks are returned) and the sentence (if the sentence text is generated). Sentence-level `corrected_text` is displayed if `words` or `parses` are set to *true*.  Note that as Tisane works with large dictionaries, you may need to exclude more esoteric terms by using the `min_generic_frequency` setting.  Note that **the invocation of spell-checking does not depend on whether the sentences and the words sections are generated in the output**. The spellchecking can be disabled by setting `disable_spellcheck` to `true`. Another option is to enable the spellchecking for lowercase words only, thus excluding potential proper nouns in languages that support capitalization; to avoid spell-checking capitalized and uppercase words, set `lowercase_spellcheck_only` to `true`.  # Settings Reference  The purpose of the settings structure is to:  *   provide cues about the content being sent to improve the results *   customize the output and select sections to be shown *   define standards and formats in use *   define and calculate the signal to noise ranking       All settings are optional. To leave all settings to default, simply provide an empty object (`{}`).  ## Content Cues and Instructions  `format` (string) - the format of the content. Some policies will be applied depending on the format. Certain logic in the underlying language models may require the content to be of a certain format (e.g. logic applied on the reviews may seek for sentiment more aggressively). The default format is empty / undefined. The format values are:  *   `review` - a review of a product or a service or any other review. Normally, the underlying language models will seek for sentiment expressions more aggressively in reviews. *   `dialogue` - a comment or a post which is a part of a dialogue. An example of a logic more specific to a dialogue is name calling. A single word like \"idiot\" would not be a personal attack in any other format, but it is certainly a personal attack when part of a dialogue. *   `shortpost` - a microblogging post, e.g. a tweet. *   `longform` - a long post or an article. *   `proofread` - a post which was proofread. In the proofread posts, the spellchecking is switched off. *   `alias` - a nickname in an online community. *   `search` - a search query. Search queries may not always be grammatically correct. Certain topics and items, that we may otherwise let pass, are tagged with the `search` format.       `disable_spellcheck` (boolean) - determines whether the automatic spellchecking is to be disabled. Default: `false`.  `lowercase_spellcheck_only` (boolean) - determines whether the automatic spellchecking is only to be applied to words in lowercase. Default: `false`  `min_generic_frequency` (int) - allows excluding more esoteric terms; the valid values are 0 thru 10.  `subscope` (boolean) - enables sub-scope parsing, for scenarios like hashtag, URL parsing, and obfuscated content (e.g. *ihateyou*). Default: `false`.  `lang_detect_segmentation_regex` (string) - allows defining custom language detection fragment boundaries. For example, if multiple languages may be used in different sentences in the same text, you may want to define the regex as: `(([\\r\\n]|[.!?][ ]))` .  `domain_factors` (set of pairs made of strings and numbers) - provides a session-scope cues for the domains of discourse. This is a powerful tool that allows tailoring the result based on the use case. The format is, family ID of the domain as a key and the multiplication factor as a value (e.g. *\"12345\": 5.0*). For example, when processing text looking for criminal activity, we may want to set domains relevant to drugs, firearms, crime, higher: `\"domain_factors\": {\"31058\": 5.0, \"45220\": 5.0, \"14112\": 5.0, \"14509\": 3.0, \"28309\": 5.0, \"43220\": 5.0, \"34581\": 5.0}`. The same device can be used to eliminate noise coming from domains we know are irrelevant by setting the factor to a value lower than 1.  `when` (date string, format YYYY-MM-DD) - indicates when the utterance was uttered. (TO BE IMPLEMENTED) The purpose is to prune word senses that were not available at a particular point in time. For example, the words *troll*, *mail*, and *post* had nothing to do with the Internet 300 years ago because there was no Internet, and so in a text that was written hundreds of years ago, we should ignore the word senses that emerged only recently.  ## Output Customization  `abuse` (boolean) - output instances of abusive content (default: `true`)  `sentiment` (boolean) - output sentiment-bearing snippets (default: `true`)  `document_sentiment` (boolean) - output document-level sentiment (default: `false`)  `entities` (boolean) - output entities (default: `true`)  `topics` (boolean) - output topics (default: `true`), with two more relevant settings:  *   `topic_stats` (boolean) - include coverage statistics in the topic output (default: `false`). When set, the topic is an object containing the attributes `topic` (string) and `coverage` (floating-point number). The coverage indicates a share of sentences touching the topic among all the sentences. *   `optimize_topics` (boolean) - if `true`, the less specific topics are removed if they are parts of the more specific topics. For example, when the topic is `cryptocurrency`, the optimization removes `finance`.       `words` (boolean) - output the lexical chunks / words for every sentence (default: `false`). In languages without white spaces (Chinese, Japanese, Thai), the tokens are tokenized words. In languages with compounds (e.g. German, Dutch, Norwegian), the compounds are split.  `fetch_definitions` (boolean) - include definitions of the words in the output (default: `false`). Only relevant when the `words` setting is `true`  `parses` (boolean) - output parse forests of phrases  `deterministic` (boolean) - whether the n-best senses and n-best parses are to be output in addition to the detected sense. If `true`, only the detected sense will be output. Default: `true`  `snippets` (boolean) - include the text snippets in the abuse, sentiment, and entities sections (default: `false`)  `explain` (boolean) - if `true`, a reasoning for the abuse and sentiment snippets is provided when possible (see the `explanation` attribute)  ## Standards and Formats  `feature_standard` (string) - determines the standard used to output the features (grammar, style, semantics) in the response object. The standards we support are:  *   `ud`: [Universal Dependencies tags](https://universaldependencies.org/u/pos/) (default) *   `penn`: [Penn treebank tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) *   `native`: Tisane native feature codes *   `description`: Tisane native feature descriptions       Only the native Tisane standards (codes and descriptions) support style and semantic features.  `topic_standard` (string) - determines the standard used to output the topics in the response object. The standards we support are:  *   `iptc_code` - IPTC topic taxonomy code *   `iptc_description` - IPTC topic taxonomy description *   `iab_code` - IAB topic taxonomy code *   `iab_description` - IAB topic taxonomy description *   `native` - Tisane domain description, coming from the family description (default)       `sentiment_analysis_type` (string) - the type of the sentiment analysis strategy. The values are:  *   `products_and_services` - most common sentiment analysis of products and services *   `entity` - sentiment analysis with entities as targets *   `creative_content_review` - reviews of creative content (RESERVED) *   `political_essay` - political essays (RESERVED)       ## Context and Long-Term Memory  Human understanding of language is not a simple \"sliding window\" with scope limited to a sentence. Language is accompanied by gestures, visuals, and knowledge of the previous communication. Sometimes, code-words may be used to conceal the words' original meaning.  When detecting abuse, a name of an ethnicity or a religious group may be not offensive, but when superimposed over a picture of an ape or a pig, it is meant of offend. When translating from a language without gender distinctions in verbs (like English) to a language with distinctions (like Russian or Hebrew), there is no way to know from an utterance alone if the speaker is female. When a scammer is collecting details piecemeal over a series of utterances, knowledge of previous utterances is needed to take action.  Tisane's Memory module allows pre-initializing the analysis, as well as reassigning meanings, and more. The module is made of three simple components that are flexible enough for a variety of tasks:  ### Reassignments  Reassignments define the attributes to set based on other attributes. This allows to:  *   assign gender to 1st or 2nd person verbs, generating accurate translations *   overwrite original meaning of a group of words with all their inflected forms to analyze code-words and secret language *   add an additional feature or a hypernym to a family       and more, within a scope of a call.  The `assign` section is an array of structures defining:  *   `if` - conditions to match:     *   `regex` - a regular expression (RE2 syntax)     *   `family` - a family ID     *   `features` - a list of feature values. A feature is a structure with an `index` and a `value`. For example: `{\"index\":1, \"value\":\"NOUN\"}`.     *   `hypernym` - a family ID of a hypernym *   `then` - attributes to assign     *   `family` - a family ID     *   `features` - a list of feature values. A feature is a structure with an `index` and a `value`. For example: `{\"index\":1, \"value\":\"NOUN\"}`.     *   `hypernym` - a family ID of a hypernym  Examples:  *   the speaker is female: \\`\"assign\":\\[{\"if\":{\"features\":\\[{\"index\":9,\"value\":\"1\"}\\]},\"then\":{\"features\":\\[{\"index\":5,\"value\":\"F\"}\\]}}\\] *   assume that a mention of a container refers to an illegal item: \\`\"assign\":\\[{\"if\":{\"family\":26888},\"then\":{\"hypernym\":123078}}\\]       ### Flags  An array of flag structures that add some context. A flag is a structure with an `index` and a `value`. For example: `{\"index\":36, \"value\":\"WFH\"}`.  Aside from the flags returned in the `memory` section of the response, these flags can be set:  *   `{\"index\":36, \"value\":\"PEBD\"}` (agents_of_bad_things) - the context is about a bad player or an agent responsible for bad things *   `{\"index\":36, \"value\":\"BADANML\"}` (bad_animal) - the context is an animal that symbolizes bad qualities (e.g. pig, ape, snake, etc.) *   `{\"index\":36, \"value\":\"BULKMSG\"}` (bulk_message) - the message was sent in bulk *   `{\"index\":36, \"value\":\"DETHR\"}` (death_related) - the context is something related to death *   `{\"index\":36, \"value\":\"EARNMUCH\"}` (make_money) - the context is related to making money *   `{\"index\":36, \"value\":\"IDEP\"}` (my_departure) - the author of the text mentioned departing *   `{\"index\":36, \"value\":\"SECO\"}` (sexually_conservative) - any attempt to exchange photos or anything that may be either sexual or non-sexual is to be deemed sexual *   `{\"index\":36, \"value\":\"TRPA\"}` (trusted_party) - the author of the text claims to be a trusted party (e.g. a relative or a spouse) *   `{\"index\":36, \"value\":\"WSTE\"}` (waste) - the context is about waste, organic or inorganic *   `{\"index\":36, \"value\":\"WOPR\"}` (won_prize) - prize or money winning was mentioned or implied *   `{\"index\":36, \"value\":\"WFH\"}` (work_from_home) - work from home was mentioned *   `{\"index\":5, \"value\":\"ORG\"}` (organization) - an organization was mentioned *   `{\"index\":5, \"value\":\"ROLE\"}` (role) - a role or a position was mentioned       ### Antecedents  The section contains structures to be used in coreference resolution. The attributes are:  *   `family` - the family ID of the antecedent *   `features` - the list of features. Every feature is a structure with an `index` and a `value`. For example: `{\"index\":36, \"value\":\"WFH\"}`.       ## Signal to Noise Ranking  When we're studying a bunch of posts commenting on an issue or an article, we may want to prioritize the ones more relevant to the topic, and containing more reason and logic than emotion. This is what the signal to noise ranking is meant to achieve.  The signal to noise ranking is made of two parts:  1.  Determine the most relevant concepts. This part may be omitted, depending on the use case scenario (e.g. we want to track posts most relevant to a particular set of issues). 2.  Rank the actual post in relevance to these concepts.       To determine the most relevant concepts, we need to analyze the headline or the article itself. The headline is usually enough. We need two additional settings:  *   `keyword_features` (an object of strings with string values) - determines the features to look for in a word. When such a feature is found, the family ID is added to the set of potentially relevant family IDs. *   `stop_hypernyms` (an array of integers) - if a potentially relevant family ID has a hypernym listed in this setting, it will not be considered. For example, we extracted a set of nouns from the headline, but we may not be interested in abstractions or feelings. E.g. from a headline like *Fear and Loathing in Las Vegas* we want *Las Vegas* only. Optional.       If `keyword_features` is provided in the settings, the response will have a special attribute, `relevant`, containing a set of family IDs.  At the second stage, when ranking the actual posts or comments for relevance, this array is to be supplied among the settings. The ranking is boosted when the domain, the hypernyms, or the families related to those in the `relevant` array are mentioned, when negative and positive sentiment is linked to aspects, and penalized when the negativity is not linked to aspects, or abuse of any kind is found. The latter consideration may be disabled, e.g. when we are looking for specific criminal content. When the `abuse_not_noise` parameter is specified and set to `true`, the abuse is not penalized by the ranking calculations.  To sum it up, in order to calculate the signal to noise ranking:  1.  Analyze the headline with `keyword_features` and, optionally, `stop_hypernyms` in the settings. Obtain the `relevant` attribute. 2.  When analyzing the posts or the comments, specify the `relevant` attribute obtained in step 1.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import okhttp3.*;
import okhttp3.internal.http.HttpMethod;
import okhttp3.internal.tls.OkHostnameVerifier;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import okio.Buffer;
import okio.BufferedSink;
import okio.Okio;

import javax.net.ssl.*;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.Type;
import java.net.URI;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import java.security.KeyStore;
import java.security.SecureRandom;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.text.DateFormat;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.openapitools.client.auth.Authentication;
import org.openapitools.client.auth.HttpBasicAuth;
import org.openapitools.client.auth.HttpBearerAuth;
import org.openapitools.client.auth.ApiKeyAuth;

/**
 * <p>ApiClient class.</p>
 */
public class ApiClient {

    private String basePath = "https://api.tisane.ai";
    protected List<ServerConfiguration> servers = new ArrayList<ServerConfiguration>(Arrays.asList(
    new ServerConfiguration(
      "https://api.tisane.ai",
      "No description provided",
      new HashMap<String, ServerVariable>()
    )
  ));
    protected Integer serverIndex = 0;
    protected Map<String, String> serverVariables = null;
    private boolean debugging = false;
    private Map<String, String> defaultHeaderMap = new HashMap<String, String>();
    private Map<String, String> defaultCookieMap = new HashMap<String, String>();
    private String tempFolderPath = null;

    private Map<String, Authentication> authentications;

    private DateFormat dateFormat;
    private DateFormat datetimeFormat;
    private boolean lenientDatetimeFormat;
    private int dateLength;

    private InputStream sslCaCert;
    private boolean verifyingSsl;
    private KeyManager[] keyManagers;

    private OkHttpClient httpClient;
    private JSON json;

    private HttpLoggingInterceptor loggingInterceptor;

    /**
     * Basic constructor for ApiClient
     */
    public ApiClient() {
        init();
        initHttpClient();

        // Setup authentications (key: authentication name, value: authentication).
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    /**
     * Basic constructor with custom OkHttpClient
     *
     * @param client a {@link okhttp3.OkHttpClient} object
     */
    public ApiClient(OkHttpClient client) {
        init();

        httpClient = client;

        // Setup authentications (key: authentication name, value: authentication).
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    private void initHttpClient() {
        initHttpClient(Collections.<Interceptor>emptyList());
    }

    private void initHttpClient(List<Interceptor> interceptors) {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        builder.addNetworkInterceptor(getProgressInterceptor());
        for (Interceptor interceptor: interceptors) {
            builder.addInterceptor(interceptor);
        }

        httpClient = builder.build();
    }

    private void init() {
        verifyingSsl = true;

        json = new JSON();

        // Set default User-Agent.
        setUserAgent("OpenAPI-Generator/1.0.0/java");

        authentications = new HashMap<String, Authentication>();
    }

    /**
     * Get base path
     *
     * @return Base path
     */
    public String getBasePath() {
        return basePath;
    }

    /**
     * Set base path
     *
     * @param basePath Base path of the URL (e.g https://api.tisane.ai
     * @return An instance of OkHttpClient
     */
    public ApiClient setBasePath(String basePath) {
        this.basePath = basePath;
        this.serverIndex = null;
        return this;
    }

    public List<ServerConfiguration> getServers() {
        return servers;
    }

    public ApiClient setServers(List<ServerConfiguration> servers) {
        this.servers = servers;
        return this;
    }

    public Integer getServerIndex() {
        return serverIndex;
    }

    public ApiClient setServerIndex(Integer serverIndex) {
        this.serverIndex = serverIndex;
        return this;
    }

    public Map<String, String> getServerVariables() {
        return serverVariables;
    }

    public ApiClient setServerVariables(Map<String, String> serverVariables) {
        this.serverVariables = serverVariables;
        return this;
    }

    /**
     * Get HTTP client
     *
     * @return An instance of OkHttpClient
     */
    public OkHttpClient getHttpClient() {
        return httpClient;
    }

    /**
     * Set HTTP client, which must never be null.
     *
     * @param newHttpClient An instance of OkHttpClient
     * @return Api Client
     * @throws java.lang.NullPointerException when newHttpClient is null
     */
    public ApiClient setHttpClient(OkHttpClient newHttpClient) {
        this.httpClient = Objects.requireNonNull(newHttpClient, "HttpClient must not be null!");
        return this;
    }

    /**
     * Get JSON
     *
     * @return JSON object
     */
    public JSON getJSON() {
        return json;
    }

    /**
     * Set JSON
     *
     * @param json JSON object
     * @return Api client
     */
    public ApiClient setJSON(JSON json) {
        this.json = json;
        return this;
    }

    /**
     * True if isVerifyingSsl flag is on
     *
     * @return True if isVerifySsl flag is on
     */
    public boolean isVerifyingSsl() {
        return verifyingSsl;
    }

    /**
     * Configure whether to verify certificate and hostname when making https requests.
     * Default to true.
     * NOTE: Do NOT set to false in production code, otherwise you would face multiple types of cryptographic attacks.
     *
     * @param verifyingSsl True to verify TLS/SSL connection
     * @return ApiClient
     */
    public ApiClient setVerifyingSsl(boolean verifyingSsl) {
        this.verifyingSsl = verifyingSsl;
        applySslSettings();
        return this;
    }

    /**
     * Get SSL CA cert.
     *
     * @return Input stream to the SSL CA cert
     */
    public InputStream getSslCaCert() {
        return sslCaCert;
    }

    /**
     * Configure the CA certificate to be trusted when making https requests.
     * Use null to reset to default.
     *
     * @param sslCaCert input stream for SSL CA cert
     * @return ApiClient
     */
    public ApiClient setSslCaCert(InputStream sslCaCert) {
        this.sslCaCert = sslCaCert;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>keyManagers</code>.</p>
     *
     * @return an array of {@link javax.net.ssl.KeyManager} objects
     */
    public KeyManager[] getKeyManagers() {
        return keyManagers;
    }

    /**
     * Configure client keys to use for authorization in an SSL session.
     * Use null to reset to default.
     *
     * @param managers The KeyManagers to use
     * @return ApiClient
     */
    public ApiClient setKeyManagers(KeyManager[] managers) {
        this.keyManagers = managers;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>dateFormat</code>.</p>
     *
     * @return a {@link java.text.DateFormat} object
     */
    public DateFormat getDateFormat() {
        return dateFormat;
    }

    /**
     * <p>Setter for the field <code>dateFormat</code>.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setDateFormat(DateFormat dateFormat) {
        JSON.setDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set SqlDateFormat.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setSqlDateFormat(DateFormat dateFormat) {
        JSON.setSqlDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set OffsetDateTimeFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        JSON.setOffsetDateTimeFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LocalDateFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLocalDateFormat(DateTimeFormatter dateFormat) {
        JSON.setLocalDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LenientOnJson.</p>
     *
     * @param lenientOnJson a boolean
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLenientOnJson(boolean lenientOnJson) {
        JSON.setLenientOnJson(lenientOnJson);
        return this;
    }

    /**
     * Get authentications (key: authentication name, value: authentication).
     *
     * @return Map of authentication objects
     */
    public Map<String, Authentication> getAuthentications() {
        return authentications;
    }

    /**
     * Get authentication for the given name.
     *
     * @param authName The authentication name
     * @return The authentication, null if not found
     */
    public Authentication getAuthentication(String authName) {
        return authentications.get(authName);
    }


    /**
     * Helper method to set username for the first HTTP basic authentication.
     *
     * @param username Username
     */
    public void setUsername(String username) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setUsername(username);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set password for the first HTTP basic authentication.
     *
     * @param password Password
     */
    public void setPassword(String password) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setPassword(password);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set API key value for the first API key authentication.
     *
     * @param apiKey API key
     */
    public void setApiKey(String apiKey) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKey(apiKey);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set API key prefix for the first API key authentication.
     *
     * @param apiKeyPrefix API key prefix
     */
    public void setApiKeyPrefix(String apiKeyPrefix) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKeyPrefix(apiKeyPrefix);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set access token for the first OAuth2 authentication.
     *
     * @param accessToken Access token
     */
    public void setAccessToken(String accessToken) {
        throw new RuntimeException("No OAuth2 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param sessionToken Session Token
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String sessionToken, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Set the User-Agent header's value (by adding to the default header map).
     *
     * @param userAgent HTTP request's user agent
     * @return ApiClient
     */
    public ApiClient setUserAgent(String userAgent) {
        addDefaultHeader("User-Agent", userAgent);
        return this;
    }

    /**
     * Add a default header.
     *
     * @param key The header's key
     * @param value The header's value
     * @return ApiClient
     */
    public ApiClient addDefaultHeader(String key, String value) {
        defaultHeaderMap.put(key, value);
        return this;
    }

    /**
     * Add a default cookie.
     *
     * @param key The cookie's key
     * @param value The cookie's value
     * @return ApiClient
     */
    public ApiClient addDefaultCookie(String key, String value) {
        defaultCookieMap.put(key, value);
        return this;
    }

    /**
     * Check that whether debugging is enabled for this API client.
     *
     * @return True if debugging is enabled, false otherwise.
     */
    public boolean isDebugging() {
        return debugging;
    }

    /**
     * Enable/disable debugging for this API client.
     *
     * @param debugging To enable (true) or disable (false) debugging
     * @return ApiClient
     */
    public ApiClient setDebugging(boolean debugging) {
        if (debugging != this.debugging) {
            if (debugging) {
                loggingInterceptor = new HttpLoggingInterceptor();
                loggingInterceptor.setLevel(Level.BODY);
                httpClient = httpClient.newBuilder().addInterceptor(loggingInterceptor).build();
            } else {
                final OkHttpClient.Builder builder = httpClient.newBuilder();
                builder.interceptors().remove(loggingInterceptor);
                httpClient = builder.build();
                loggingInterceptor = null;
            }
        }
        this.debugging = debugging;
        return this;
    }

    /**
     * The path of temporary folder used to store downloaded files from endpoints
     * with file response. The default value is <code>null</code>, i.e. using
     * the system's default temporary folder.
     *
     * @see <a href="https://docs.oracle.com/javase/7/docs/api/java/nio/file/Files.html#createTempFile(java.lang.String,%20java.lang.String,%20java.nio.file.attribute.FileAttribute...)">createTempFile</a>
     * @return Temporary folder path
     */
    public String getTempFolderPath() {
        return tempFolderPath;
    }

    /**
     * Set the temporary folder path (for downloading files)
     *
     * @param tempFolderPath Temporary folder path
     * @return ApiClient
     */
    public ApiClient setTempFolderPath(String tempFolderPath) {
        this.tempFolderPath = tempFolderPath;
        return this;
    }

    /**
     * Get connection timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getConnectTimeout() {
        return httpClient.connectTimeoutMillis();
    }

    /**
     * Sets the connect timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param connectionTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setConnectTimeout(int connectionTimeout) {
        httpClient = httpClient.newBuilder().connectTimeout(connectionTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get read timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getReadTimeout() {
        return httpClient.readTimeoutMillis();
    }

    /**
     * Sets the read timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param readTimeout read timeout in milliseconds
     * @return Api client
     */
    public ApiClient setReadTimeout(int readTimeout) {
        httpClient = httpClient.newBuilder().readTimeout(readTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get write timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getWriteTimeout() {
        return httpClient.writeTimeoutMillis();
    }

    /**
     * Sets the write timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param writeTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setWriteTimeout(int writeTimeout) {
        httpClient = httpClient.newBuilder().writeTimeout(writeTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }


    /**
     * Format the given parameter object into string.
     *
     * @param param Parameter
     * @return String representation of the parameter
     */
    public String parameterToString(Object param) {
        if (param == null) {
            return "";
        } else if (param instanceof Date || param instanceof OffsetDateTime || param instanceof LocalDate) {
            //Serialize to json string and remove the " enclosing characters
            String jsonStr = JSON.serialize(param);
            return jsonStr.substring(1, jsonStr.length() - 1);
        } else if (param instanceof Collection) {
            StringBuilder b = new StringBuilder();
            for (Object o : (Collection) param) {
                if (b.length() > 0) {
                    b.append(",");
                }
                b.append(o);
            }
            return b.toString();
        } else {
            return String.valueOf(param);
        }
    }

    /**
     * Formats the specified query parameter to a list containing a single {@code Pair} object.
     *
     * Note that {@code value} must not be a collection.
     *
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list containing a single {@code Pair} object.
     */
    public List<Pair> parameterToPair(String name, Object value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value instanceof Collection) {
            return params;
        }

        params.add(new Pair(name, parameterToString(value)));
        return params;
    }

    /**
     * Formats the specified collection query parameters to a list of {@code Pair} objects.
     *
     * Note that the values of each of the returned Pair objects are percent-encoded.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list of {@code Pair} objects.
     */
    public List<Pair> parameterToPairs(String collectionFormat, String name, Collection value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value.isEmpty()) {
            return params;
        }

        // create the params based on the collection format
        if ("multi".equals(collectionFormat)) {
            for (Object item : value) {
                params.add(new Pair(name, escapeString(parameterToString(item))));
            }
            return params;
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        // escape all delimiters except commas, which are URI reserved
        // characters
        if ("ssv".equals(collectionFormat)) {
            delimiter = escapeString(" ");
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = escapeString("\t");
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = escapeString("|");
        }

        StringBuilder sb = new StringBuilder();
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(escapeString(parameterToString(item)));
        }

        params.add(new Pair(name, sb.substring(delimiter.length())));

        return params;
    }

    /**
    * Formats the specified free-form query parameters to a list of {@code Pair} objects.
    *
    * @param value The free-form query parameters.
    * @return A list of {@code Pair} objects.
    */
    public List<Pair> freeFormParameterToPairs(Object value) {
        List<Pair> params = new ArrayList<>();

        // preconditions
        if (value == null || !(value instanceof Map )) {
            return params;
        }

        final Map<String, Object> valuesMap = (Map<String, Object>) value;

        for (Map.Entry<String, Object> entry : valuesMap.entrySet()) {
            params.add(new Pair(entry.getKey(), parameterToString(entry.getValue())));
        }

        return params;
    }


    /**
     * Formats the specified collection path parameter to a string value.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param value The value of the parameter.
     * @return String representation of the parameter
     */
    public String collectionPathParameterToString(String collectionFormat, Collection value) {
        // create the value based on the collection format
        if ("multi".equals(collectionFormat)) {
            // not valid for path params
            return parameterToString(value);
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        if ("ssv".equals(collectionFormat)) {
            delimiter = " ";
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = "\t";
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = "|";
        }

        StringBuilder sb = new StringBuilder() ;
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(parameterToString(item));
        }

        return sb.substring(delimiter.length());
    }

    /**
     * Sanitize filename by removing path.
     * e.g. ../../sun.gif becomes sun.gif
     *
     * @param filename The filename to be sanitized
     * @return The sanitized filename
     */
    public String sanitizeFilename(String filename) {
        return filename.replaceAll(".*[/\\\\]", "");
    }

    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     *   application/json
     *   application/json; charset=UTF8
     *   APPLICATION/JSON
     *   application/vnd.company+json
     * "* / *" is also default to JSON
     * @param mime MIME (Multipurpose Internet Mail Extensions)
     * @return True if the given MIME is JSON, false otherwise.
     */
    public boolean isJsonMime(String mime) {
        String jsonMime = "(?i)^(application/json|[^;/ \t]+/[^;/ \t]+[+]json)[ \t]*(;.*)?$";
        return mime != null && (mime.matches(jsonMime) || mime.equals("*/*"));
    }

    /**
     * Select the Accept header's value from the given accepts array:
     *   if JSON exists in the given array, use it;
     *   otherwise use all of them (joining into a string)
     *
     * @param accepts The accepts array to select from
     * @return The Accept header to use. If the given array is empty,
     *   null will be returned (not to set the Accept header explicitly).
     */
    public String selectHeaderAccept(String[] accepts) {
        if (accepts.length == 0) {
            return null;
        }
        for (String accept : accepts) {
            if (isJsonMime(accept)) {
                return accept;
            }
        }
        return StringUtil.join(accepts, ",");
    }

    /**
     * Select the Content-Type header's value from the given array:
     *   if JSON exists in the given array, use it;
     *   otherwise use the first one of the array.
     *
     * @param contentTypes The Content-Type array to select from
     * @return The Content-Type header to use. If the given array is empty,
     *   returns null. If it matches "any", JSON will be used.
     */
    public String selectHeaderContentType(String[] contentTypes) {
        if (contentTypes.length == 0) {
            return null;
        }

        if (contentTypes[0].equals("*/*")) {
            return "application/json";
        }

        for (String contentType : contentTypes) {
            if (isJsonMime(contentType)) {
                return contentType;
            }
        }

        return contentTypes[0];
    }

    /**
     * Escape the given string to be used as URL query value.
     *
     * @param str String to be escaped
     * @return Escaped string
     */
    public String escapeString(String str) {
        try {
            return URLEncoder.encode(str, "utf8").replaceAll("\\+", "%20");
        } catch (UnsupportedEncodingException e) {
            return str;
        }
    }

    /**
     * Deserialize response body to Java object, according to the return type and
     * the Content-Type response header.
     *
     * @param <T> Type
     * @param response HTTP response
     * @param returnType The type of the Java object
     * @return The deserialized Java object
     * @throws org.openapitools.client.ApiException If fail to deserialize response body, i.e. cannot read response body
     *   or the Content-Type of the response is not supported.
     */
    @SuppressWarnings("unchecked")
    public <T> T deserialize(Response response, Type returnType) throws ApiException {
        if (response == null || returnType == null) {
            return null;
        }

        if ("byte[]".equals(returnType.toString())) {
            // Handle binary response (byte array).
            try {
                return (T) response.body().bytes();
            } catch (IOException e) {
                throw new ApiException(e);
            }
        } else if (returnType.equals(File.class)) {
            // Handle file downloading.
            return (T) downloadFileFromResponse(response);
        }

        String respBody;
        try {
            if (response.body() != null)
                respBody = response.body().string();
            else
                respBody = null;
        } catch (IOException e) {
            throw new ApiException(e);
        }

        if (respBody == null || "".equals(respBody)) {
            return null;
        }

        String contentType = response.headers().get("Content-Type");
        if (contentType == null) {
            // ensuring a default content type
            contentType = "application/json";
        }
        if (isJsonMime(contentType)) {
            return JSON.deserialize(respBody, returnType);
        } else if (returnType.equals(String.class)) {
            // Expecting string, return the raw response body.
            return (T) respBody;
        } else {
            throw new ApiException(
                    "Content type \"" + contentType + "\" is not supported for type: " + returnType,
                    response.code(),
                    response.headers().toMultimap(),
                    respBody);
        }
    }

    /**
     * Serialize the given Java object into request body according to the object's
     * class and the request Content-Type.
     *
     * @param obj The Java object
     * @param contentType The request Content-Type
     * @return The serialized request body
     * @throws org.openapitools.client.ApiException If fail to serialize the given object
     */
    public RequestBody serialize(Object obj, String contentType) throws ApiException {
        if (obj instanceof byte[]) {
            // Binary (byte array) body parameter support.
            return RequestBody.create((byte[]) obj, MediaType.parse(contentType));
        } else if (obj instanceof File) {
            // File body parameter support.
            return RequestBody.create((File) obj, MediaType.parse(contentType));
        } else if ("text/plain".equals(contentType) && obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else if (isJsonMime(contentType)) {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            return RequestBody.create(content, MediaType.parse(contentType));
        } else if (obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else {
            throw new ApiException("Content type \"" + contentType + "\" is not supported");
        }
    }

    /**
     * Download file from the given response.
     *
     * @param response An instance of the Response object
     * @throws org.openapitools.client.ApiException If fail to read file content from response and write to disk
     * @return Downloaded file
     */
    public File downloadFileFromResponse(Response response) throws ApiException {
        try {
            File file = prepareDownloadFile(response);
            BufferedSink sink = Okio.buffer(Okio.sink(file));
            sink.writeAll(response.body().source());
            sink.close();
            return file;
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * Prepare file for download
     *
     * @param response An instance of the Response object
     * @return Prepared file for the download
     * @throws java.io.IOException If fail to prepare file for download
     */
    public File prepareDownloadFile(Response response) throws IOException {
        String filename = null;
        String contentDisposition = response.header("Content-Disposition");
        if (contentDisposition != null && !"".equals(contentDisposition)) {
            // Get filename from the Content-Disposition header.
            Pattern pattern = Pattern.compile("filename=['\"]?([^'\"\\s]+)['\"]?");
            Matcher matcher = pattern.matcher(contentDisposition);
            if (matcher.find()) {
                filename = sanitizeFilename(matcher.group(1));
            }
        }

        String prefix = null;
        String suffix = null;
        if (filename == null) {
            prefix = "download-";
            suffix = "";
        } else {
            int pos = filename.lastIndexOf(".");
            if (pos == -1) {
                prefix = filename + "-";
            } else {
                prefix = filename.substring(0, pos) + "-";
                suffix = filename.substring(pos);
            }
            // Files.createTempFile requires the prefix to be at least three characters long
            if (prefix.length() < 3)
                prefix = "download-";
        }

        if (tempFolderPath == null)
            return Files.createTempFile(prefix, suffix).toFile();
        else
            return Files.createTempFile(Paths.get(tempFolderPath), prefix, suffix).toFile();
    }

    /**
     * {@link #execute(Call, Type)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @return ApiResponse&lt;T&gt;
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call) throws ApiException {
        return execute(call, null);
    }

    /**
     * Execute HTTP call and deserialize the HTTP response body into the given return type.
     *
     * @param returnType The return type used to deserialize HTTP response body
     * @param <T> The return type corresponding to (same with) returnType
     * @param call Call
     * @return ApiResponse object containing response status, headers and
     *   data, which is a Java object deserialized from response body and would be null
     *   when returnType is null.
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call, Type returnType) throws ApiException {
        try {
            Response response = call.execute();
            T data = handleResponse(response, returnType);
            return new ApiResponse<T>(response.code(), response.headers().toMultimap(), data);
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * {@link #executeAsync(Call, Type, ApiCallback)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @param callback ApiCallback&lt;T&gt;
     */
    public <T> void executeAsync(Call call, ApiCallback<T> callback) {
        executeAsync(call, null, callback);
    }

    /**
     * Execute HTTP call asynchronously.
     *
     * @param <T> Type
     * @param call The callback to be executed when the API call finishes
     * @param returnType Return type
     * @param callback ApiCallback
     * @see #execute(Call, Type)
     */
    @SuppressWarnings("unchecked")
    public <T> void executeAsync(Call call, final Type returnType, final ApiCallback<T> callback) {
        call.enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                callback.onFailure(new ApiException(e), 0, null);
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                T result;
                try {
                    result = (T) handleResponse(response, returnType);
                } catch (ApiException e) {
                    callback.onFailure(e, response.code(), response.headers().toMultimap());
                    return;
                } catch (Exception e) {
                    callback.onFailure(new ApiException(e), response.code(), response.headers().toMultimap());
                    return;
                }
                callback.onSuccess(result, response.code(), response.headers().toMultimap());
            }
        });
    }

    /**
     * Handle the given response, return the deserialized object when the response is successful.
     *
     * @param <T> Type
     * @param response Response
     * @param returnType Return type
     * @return Type
     * @throws org.openapitools.client.ApiException If the response has an unsuccessful status code or
     *                      fail to deserialize the response body
     */
    public <T> T handleResponse(Response response, Type returnType) throws ApiException {
        if (response.isSuccessful()) {
            if (returnType == null || response.code() == 204) {
                // returning null if the returnType is not defined,
                // or the status code is 204 (No Content)
                if (response.body() != null) {
                    try {
                        response.body().close();
                    } catch (Exception e) {
                        throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                    }
                }
                return null;
            } else {
                return deserialize(response, returnType);
            }
        } else {
            String respBody = null;
            if (response.body() != null) {
                try {
                    respBody = response.body().string();
                } catch (IOException e) {
                    throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                }
            }
            throw new ApiException(response.message(), response.code(), response.headers().toMultimap(), respBody);
        }
    }

    /**
     * Build HTTP call with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP call
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Call buildCall(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        Request request = buildRequest(baseUrl, path, method, queryParams, collectionQueryParams, body, headerParams, cookieParams, formParams, authNames, callback);

        return httpClient.newCall(request);
    }

    /**
     * Build an HTTP request with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP request
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Request buildRequest(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        final String url = buildUrl(baseUrl, path, queryParams, collectionQueryParams);

        // prepare HTTP request body
        RequestBody reqBody;
        String contentType = headerParams.get("Content-Type");
        String contentTypePure = contentType;
        if (contentTypePure != null && contentTypePure.contains(";")) {
            contentTypePure = contentType.substring(0, contentType.indexOf(";"));
        }
        if (!HttpMethod.permitsRequestBody(method)) {
            reqBody = null;
        } else if ("application/x-www-form-urlencoded".equals(contentTypePure)) {
            reqBody = buildRequestBodyFormEncoding(formParams);
        } else if ("multipart/form-data".equals(contentTypePure)) {
            reqBody = buildRequestBodyMultipart(formParams);
        } else if (body == null) {
            if ("DELETE".equals(method)) {
                // allow calling DELETE without sending a request body
                reqBody = null;
            } else {
                // use an empty request body (for POST, PUT and PATCH)
                reqBody = RequestBody.create("", contentType == null ? null : MediaType.parse(contentType));
            }
        } else {
            reqBody = serialize(body, contentType);
        }

        List<Pair> updatedQueryParams = new ArrayList<>(queryParams);

        // update parameters with authentication settings
        updateParamsForAuth(authNames, updatedQueryParams, headerParams, cookieParams, requestBodyToString(reqBody), method, URI.create(url));

        final Request.Builder reqBuilder = new Request.Builder().url(buildUrl(baseUrl, path, updatedQueryParams, collectionQueryParams));
        processHeaderParams(headerParams, reqBuilder);
        processCookieParams(cookieParams, reqBuilder);

        // Associate callback with request (if not null) so interceptor can
        // access it when creating ProgressResponseBody
        reqBuilder.tag(callback);

        Request request = null;

        if (callback != null && reqBody != null) {
            ProgressRequestBody progressRequestBody = new ProgressRequestBody(reqBody, callback);
            request = reqBuilder.method(method, progressRequestBody).build();
        } else {
            request = reqBuilder.method(method, reqBody).build();
        }

        return request;
    }

    /**
     * Build full URL by concatenating base path, the given sub path and query parameters.
     *
     * @param baseUrl The base URL
     * @param path The sub path
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @return The full URL
     */
    public String buildUrl(String baseUrl, String path, List<Pair> queryParams, List<Pair> collectionQueryParams) {
        final StringBuilder url = new StringBuilder();
        if (baseUrl != null) {
            url.append(baseUrl).append(path);
        } else {
            String baseURL;
            if (serverIndex != null) {
                if (serverIndex < 0 || serverIndex >= servers.size()) {
                    throw new ArrayIndexOutOfBoundsException(String.format(
                    "Invalid index %d when selecting the host settings. Must be less than %d", serverIndex, servers.size()
                    ));
                }
                baseURL = servers.get(serverIndex).URL(serverVariables);
            } else {
                baseURL = basePath;
            }
            url.append(baseURL).append(path);
        }

        if (queryParams != null && !queryParams.isEmpty()) {
            // support (constant) query string in `path`, e.g. "/posts?draft=1"
            String prefix = path.contains("?") ? "&" : "?";
            for (Pair param : queryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    url.append(escapeString(param.getName())).append("=").append(escapeString(value));
                }
            }
        }

        if (collectionQueryParams != null && !collectionQueryParams.isEmpty()) {
            String prefix = url.toString().contains("?") ? "&" : "?";
            for (Pair param : collectionQueryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    // collection query parameter value already escaped as part of parameterToPairs
                    url.append(escapeString(param.getName())).append("=").append(value);
                }
            }
        }

        return url.toString();
    }

    /**
     * Set header parameters to the request builder, including default headers.
     *
     * @param headerParams Header parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processHeaderParams(Map<String, String> headerParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : headerParams.entrySet()) {
            reqBuilder.header(param.getKey(), parameterToString(param.getValue()));
        }
        for (Entry<String, String> header : defaultHeaderMap.entrySet()) {
            if (!headerParams.containsKey(header.getKey())) {
                reqBuilder.header(header.getKey(), parameterToString(header.getValue()));
            }
        }
    }

    /**
     * Set cookie parameters to the request builder, including default cookies.
     *
     * @param cookieParams Cookie parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processCookieParams(Map<String, String> cookieParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : cookieParams.entrySet()) {
            reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
        }
        for (Entry<String, String> param : defaultCookieMap.entrySet()) {
            if (!cookieParams.containsKey(param.getKey())) {
                reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
            }
        }
    }

    /**
     * Update query and header parameters based on authentication settings.
     *
     * @param authNames The authentications to apply
     * @param queryParams List of query parameters
     * @param headerParams Map of header parameters
     * @param cookieParams Map of cookie parameters
     * @param payload HTTP request body
     * @param method HTTP method
     * @param uri URI
     * @throws org.openapitools.client.ApiException If fails to update the parameters
     */
    public void updateParamsForAuth(String[] authNames, List<Pair> queryParams, Map<String, String> headerParams,
                                    Map<String, String> cookieParams, String payload, String method, URI uri) throws ApiException {
        for (String authName : authNames) {
            Authentication auth = authentications.get(authName);
            if (auth == null) {
                throw new RuntimeException("Authentication undefined: " + authName);
            }
            auth.applyToParams(queryParams, headerParams, cookieParams, payload, method, uri);
        }
    }

    /**
     * Build a form-encoding request body with the given form parameters.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyFormEncoding(Map<String, Object> formParams) {
        okhttp3.FormBody.Builder formBuilder = new okhttp3.FormBody.Builder();
        for (Entry<String, Object> param : formParams.entrySet()) {
            formBuilder.add(param.getKey(), parameterToString(param.getValue()));
        }
        return formBuilder.build();
    }

    /**
     * Build a multipart (file uploading) request body with the given form parameters,
     * which could contain text fields and file fields.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyMultipart(Map<String, Object> formParams) {
        MultipartBody.Builder mpBuilder = new MultipartBody.Builder().setType(MultipartBody.FORM);
        for (Entry<String, Object> param : formParams.entrySet()) {
            if (param.getValue() instanceof File) {
                File file = (File) param.getValue();
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), file);
            } else if (param.getValue() instanceof List) {
                List list = (List) param.getValue();
                for (Object item: list) {
                    if (item instanceof File) {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), (File) item);
                    } else {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
                    }
                }
            } else {
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
            }
        }
        return mpBuilder.build();
    }

    /**
     * Guess Content-Type header from the given file (defaults to "application/octet-stream").
     *
     * @param file The given file
     * @return The guessed Content-Type
     */
    public String guessContentTypeFromFile(File file) {
        String contentType = URLConnection.guessContentTypeFromName(file.getName());
        if (contentType == null) {
            return "application/octet-stream";
        } else {
            return contentType;
        }
    }

    /**
     * Add a Content-Disposition Header for the given key and file to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder 
     * @param key The key of the Header element
     * @param file The file to add to the Header
     */ 
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, File file) {
        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"; filename=\"" + file.getName() + "\"");
        MediaType mediaType = MediaType.parse(guessContentTypeFromFile(file));
        mpBuilder.addPart(partHeaders, RequestBody.create(file, mediaType));
    }

    /**
     * Add a Content-Disposition Header for the given key and complex object to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder
     * @param key The key of the Header element
     * @param obj The complex object to add to the Header
     */
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, Object obj) {
        RequestBody requestBody;
        if (obj instanceof String) {
            requestBody = RequestBody.create((String) obj, MediaType.parse("text/plain"));
        } else {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            requestBody = RequestBody.create(content, MediaType.parse("application/json"));
        }

        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"");
        mpBuilder.addPart(partHeaders, requestBody);
    }

    /**
     * Get network interceptor to add it to the httpClient to track download progress for
     * async requests.
     */
    private Interceptor getProgressInterceptor() {
        return new Interceptor() {
            @Override
            public Response intercept(Interceptor.Chain chain) throws IOException {
                final Request request = chain.request();
                final Response originalResponse = chain.proceed(request);
                if (request.tag() instanceof ApiCallback) {
                    final ApiCallback callback = (ApiCallback) request.tag();
                    return originalResponse.newBuilder()
                        .body(new ProgressResponseBody(originalResponse.body(), callback))
                        .build();
                }
                return originalResponse;
            }
        };
    }

    /**
     * Apply SSL related settings to httpClient according to the current values of
     * verifyingSsl and sslCaCert.
     */
    private void applySslSettings() {
        try {
            TrustManager[] trustManagers;
            HostnameVerifier hostnameVerifier;
            if (!verifyingSsl) {
                trustManagers = new TrustManager[]{
                        new X509TrustManager() {
                            @Override
                            public void checkClientTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public void checkServerTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public java.security.cert.X509Certificate[] getAcceptedIssuers() {
                                return new java.security.cert.X509Certificate[]{};
                            }
                        }
                };
                hostnameVerifier = new HostnameVerifier() {
                    @Override
                    public boolean verify(String hostname, SSLSession session) {
                        return true;
                    }
                };
            } else {
                TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());

                if (sslCaCert == null) {
                    trustManagerFactory.init((KeyStore) null);
                } else {
                    char[] password = null; // Any password will work.
                    CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
                    Collection<? extends Certificate> certificates = certificateFactory.generateCertificates(sslCaCert);
                    if (certificates.isEmpty()) {
                        throw new IllegalArgumentException("expected non-empty set of trusted certificates");
                    }
                    KeyStore caKeyStore = newEmptyKeyStore(password);
                    int index = 0;
                    for (Certificate certificate : certificates) {
                        String certificateAlias = "ca" + (index++);
                        caKeyStore.setCertificateEntry(certificateAlias, certificate);
                    }
                    trustManagerFactory.init(caKeyStore);
                }
                trustManagers = trustManagerFactory.getTrustManagers();
                hostnameVerifier = OkHostnameVerifier.INSTANCE;
            }

            SSLContext sslContext = SSLContext.getInstance("TLS");
            sslContext.init(keyManagers, trustManagers, new SecureRandom());
            httpClient = httpClient.newBuilder()
                            .sslSocketFactory(sslContext.getSocketFactory(), (X509TrustManager) trustManagers[0])
                            .hostnameVerifier(hostnameVerifier)
                            .build();
        } catch (GeneralSecurityException e) {
            throw new RuntimeException(e);
        }
    }

    private KeyStore newEmptyKeyStore(char[] password) throws GeneralSecurityException {
        try {
            KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
            keyStore.load(null, password);
            return keyStore;
        } catch (IOException e) {
            throw new AssertionError(e);
        }
    }

    /**
     * Convert the HTTP request body to a string.
     *
     * @param requestBody The HTTP request object
     * @return The string representation of the HTTP request body
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object into a string
     */
    private String requestBodyToString(RequestBody requestBody) throws ApiException {
        if (requestBody != null) {
            try {
                final Buffer buffer = new Buffer();
                requestBody.writeTo(buffer);
                return buffer.readUtf8();
            } catch (final IOException e) {
                throw new ApiException(e);
            }
        }

        // empty http request body
        return "";
    }
}
