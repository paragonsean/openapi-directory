# YouTubeDataApiV3.ContentRating

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acbRating** | **String** | The video&#39;s Australian Classification Board (ACB) or Australian Communications and Media Authority (ACMA) rating. ACMA ratings are used to classify children&#39;s television programming. | [optional] 
**agcomRating** | **String** | The video&#39;s rating from Italy&#39;s Autorità per le Garanzie nelle Comunicazioni (AGCOM). | [optional] 
**anatelRating** | **String** | The video&#39;s Anatel (Asociación Nacional de Televisión) rating for Chilean television. | [optional] 
**bbfcRating** | **String** | The video&#39;s British Board of Film Classification (BBFC) rating. | [optional] 
**bfvcRating** | **String** | The video&#39;s rating from Thailand&#39;s Board of Film and Video Censors. | [optional] 
**bmukkRating** | **String** | The video&#39;s rating from the Austrian Board of Media Classification (Bundesministerium für Unterricht, Kunst und Kultur). | [optional] 
**catvRating** | **String** | Rating system for Canadian TV - Canadian TV Classification System The video&#39;s rating from the Canadian Radio-Television and Telecommunications Commission (CRTC) for Canadian English-language broadcasts. For more information, see the Canadian Broadcast Standards Council website. | [optional] 
**catvfrRating** | **String** | The video&#39;s rating from the Canadian Radio-Television and Telecommunications Commission (CRTC) for Canadian French-language broadcasts. For more information, see the Canadian Broadcast Standards Council website. | [optional] 
**cbfcRating** | **String** | The video&#39;s Central Board of Film Certification (CBFC - India) rating. | [optional] 
**cccRating** | **String** | The video&#39;s Consejo de Calificación Cinematográfica (Chile) rating. | [optional] 
**cceRating** | **String** | The video&#39;s rating from Portugal&#39;s Comissão de Classificação de Espect´culos. | [optional] 
**chfilmRating** | **String** | The video&#39;s rating in Switzerland. | [optional] 
**chvrsRating** | **String** | The video&#39;s Canadian Home Video Rating System (CHVRS) rating. | [optional] 
**cicfRating** | **String** | The video&#39;s rating from the Commission de Contrôle des Films (Belgium). | [optional] 
**cnaRating** | **String** | The video&#39;s rating from Romania&#39;s CONSILIUL NATIONAL AL AUDIOVIZUALULUI (CNA). | [optional] 
**cncRating** | **String** | Rating system in France - Commission de classification cinematographique | [optional] 
**csaRating** | **String** | The video&#39;s rating from France&#39;s Conseil supérieur de l’audiovisuel, which rates broadcast content. | [optional] 
**cscfRating** | **String** | The video&#39;s rating from Luxembourg&#39;s Commission de surveillance de la classification des films (CSCF). | [optional] 
**czfilmRating** | **String** | The video&#39;s rating in the Czech Republic. | [optional] 
**djctqRating** | **String** | The video&#39;s Departamento de Justiça, Classificação, Qualificação e Títulos (DJCQT - Brazil) rating. | [optional] 
**djctqRatingReasons** | **[String]** | Reasons that explain why the video received its DJCQT (Brazil) rating. | [optional] 
**ecbmctRating** | **String** | Rating system in Turkey - Evaluation and Classification Board of the Ministry of Culture and Tourism | [optional] 
**eefilmRating** | **String** | The video&#39;s rating in Estonia. | [optional] 
**egfilmRating** | **String** | The video&#39;s rating in Egypt. | [optional] 
**eirinRating** | **String** | The video&#39;s Eirin (映倫) rating. Eirin is the Japanese rating system. | [optional] 
**fcbmRating** | **String** | The video&#39;s rating from Malaysia&#39;s Film Censorship Board. | [optional] 
**fcoRating** | **String** | The video&#39;s rating from Hong Kong&#39;s Office for Film, Newspaper and Article Administration. | [optional] 
**fmocRating** | **String** | This property has been deprecated. Use the contentDetails.contentRating.cncRating instead. | [optional] 
**fpbRating** | **String** | The video&#39;s rating from South Africa&#39;s Film and Publication Board. | [optional] 
**fpbRatingReasons** | **[String]** | Reasons that explain why the video received its FPB (South Africa) rating. | [optional] 
**fskRating** | **String** | The video&#39;s Freiwillige Selbstkontrolle der Filmwirtschaft (FSK - Germany) rating. | [optional] 
**grfilmRating** | **String** | The video&#39;s rating in Greece. | [optional] 
**icaaRating** | **String** | The video&#39;s Instituto de la Cinematografía y de las Artes Audiovisuales (ICAA - Spain) rating. | [optional] 
**ifcoRating** | **String** | The video&#39;s Irish Film Classification Office (IFCO - Ireland) rating. See the IFCO website for more information. | [optional] 
**ilfilmRating** | **String** | The video&#39;s rating in Israel. | [optional] 
**incaaRating** | **String** | The video&#39;s INCAA (Instituto Nacional de Cine y Artes Audiovisuales - Argentina) rating. | [optional] 
**kfcbRating** | **String** | The video&#39;s rating from the Kenya Film Classification Board. | [optional] 
**kijkwijzerRating** | **String** | The video&#39;s NICAM/Kijkwijzer rating from the Nederlands Instituut voor de Classificatie van Audiovisuele Media (Netherlands). | [optional] 
**kmrbRating** | **String** | The video&#39;s Korea Media Rating Board (영상물등급위원회) rating. The KMRB rates videos in South Korea. | [optional] 
**lsfRating** | **String** | The video&#39;s rating from Indonesia&#39;s Lembaga Sensor Film. | [optional] 
**mccaaRating** | **String** | The video&#39;s rating from Malta&#39;s Film Age-Classification Board. | [optional] 
**mccypRating** | **String** | The video&#39;s rating from the Danish Film Institute&#39;s (Det Danske Filminstitut) Media Council for Children and Young People. | [optional] 
**mcstRating** | **String** | The video&#39;s rating system for Vietnam - MCST | [optional] 
**mdaRating** | **String** | The video&#39;s rating from Singapore&#39;s Media Development Authority (MDA) and, specifically, it&#39;s Board of Film Censors (BFC). | [optional] 
**medietilsynetRating** | **String** | The video&#39;s rating from Medietilsynet, the Norwegian Media Authority. | [optional] 
**mekuRating** | **String** | The video&#39;s rating from Finland&#39;s Kansallinen Audiovisuaalinen Instituutti (National Audiovisual Institute). | [optional] 
**menaMpaaRating** | **String** | The rating system for MENA countries, a clone of MPAA. It is needed to prevent titles go live w/o additional QC check, since some of them can be inappropriate for the countries at all. See b/33408548 for more details. | [optional] 
**mibacRating** | **String** | The video&#39;s rating from the Ministero dei Beni e delle Attività Culturali e del Turismo (Italy). | [optional] 
**mocRating** | **String** | The video&#39;s Ministerio de Cultura (Colombia) rating. | [optional] 
**moctwRating** | **String** | The video&#39;s rating from Taiwan&#39;s Ministry of Culture (文化部). | [optional] 
**mpaaRating** | **String** | The video&#39;s Motion Picture Association of America (MPAA) rating. | [optional] 
**mpaatRating** | **String** | The rating system for trailer, DVD, and Ad in the US. See http://movielabs.com/md/ratings/v2.3/html/US_MPAAT_Ratings.html. | [optional] 
**mtrcbRating** | **String** | The video&#39;s rating from the Movie and Television Review and Classification Board (Philippines). | [optional] 
**nbcRating** | **String** | The video&#39;s rating from the Maldives National Bureau of Classification. | [optional] 
**nbcplRating** | **String** | The video&#39;s rating in Poland. | [optional] 
**nfrcRating** | **String** | The video&#39;s rating from the Bulgarian National Film Center. | [optional] 
**nfvcbRating** | **String** | The video&#39;s rating from Nigeria&#39;s National Film and Video Censors Board. | [optional] 
**nkclvRating** | **String** | The video&#39;s rating from the Nacionãlais Kino centrs (National Film Centre of Latvia). | [optional] 
**nmcRating** | **String** | The National Media Council ratings system for United Arab Emirates. | [optional] 
**oflcRating** | **String** | The video&#39;s Office of Film and Literature Classification (OFLC - New Zealand) rating. | [optional] 
**pefilmRating** | **String** | The video&#39;s rating in Peru. | [optional] 
**rcnofRating** | **String** | The video&#39;s rating from the Hungarian Nemzeti Filmiroda, the Rating Committee of the National Office of Film. | [optional] 
**resorteviolenciaRating** | **String** | The video&#39;s rating in Venezuela. | [optional] 
**rtcRating** | **String** | The video&#39;s General Directorate of Radio, Television and Cinematography (Mexico) rating. | [optional] 
**rteRating** | **String** | The video&#39;s rating from Ireland&#39;s Raidió Teilifís Éireann. | [optional] 
**russiaRating** | **String** | The video&#39;s National Film Registry of the Russian Federation (MKRF - Russia) rating. | [optional] 
**skfilmRating** | **String** | The video&#39;s rating in Slovakia. | [optional] 
**smaisRating** | **String** | The video&#39;s rating in Iceland. | [optional] 
**smsaRating** | **String** | The video&#39;s rating from Statens medieråd (Sweden&#39;s National Media Council). | [optional] 
**tvpgRating** | **String** | The video&#39;s TV Parental Guidelines (TVPG) rating. | [optional] 
**ytRating** | **String** | A rating that YouTube uses to identify age-restricted content. | [optional] 



## Enum: AcbRatingEnum


* `acbUnspecified` (value: `"acbUnspecified"`)

* `acbE` (value: `"acbE"`)

* `acbP` (value: `"acbP"`)

* `acbC` (value: `"acbC"`)

* `acbG` (value: `"acbG"`)

* `acbPg` (value: `"acbPg"`)

* `acbM` (value: `"acbM"`)

* `acbMa15plus` (value: `"acbMa15plus"`)

* `acbR18plus` (value: `"acbR18plus"`)

* `acbUnrated` (value: `"acbUnrated"`)





## Enum: AgcomRatingEnum


* `agcomUnspecified` (value: `"agcomUnspecified"`)

* `agcomT` (value: `"agcomT"`)

* `agcomVm14` (value: `"agcomVm14"`)

* `agcomVm18` (value: `"agcomVm18"`)

* `agcomUnrated` (value: `"agcomUnrated"`)





## Enum: AnatelRatingEnum


* `anatelUnspecified` (value: `"anatelUnspecified"`)

* `anatelF` (value: `"anatelF"`)

* `anatelI` (value: `"anatelI"`)

* `anatelI7` (value: `"anatelI7"`)

* `anatelI10` (value: `"anatelI10"`)

* `anatelI12` (value: `"anatelI12"`)

* `anatelR` (value: `"anatelR"`)

* `anatelA` (value: `"anatelA"`)

* `anatelUnrated` (value: `"anatelUnrated"`)





## Enum: BbfcRatingEnum


* `bbfcUnspecified` (value: `"bbfcUnspecified"`)

* `bbfcU` (value: `"bbfcU"`)

* `bbfcPg` (value: `"bbfcPg"`)

* `bbfc12a` (value: `"bbfc12a"`)

* `bbfc12` (value: `"bbfc12"`)

* `bbfc15` (value: `"bbfc15"`)

* `bbfc18` (value: `"bbfc18"`)

* `bbfcR18` (value: `"bbfcR18"`)

* `bbfcUnrated` (value: `"bbfcUnrated"`)





## Enum: BfvcRatingEnum


* `bfvcUnspecified` (value: `"bfvcUnspecified"`)

* `bfvcG` (value: `"bfvcG"`)

* `bfvcE` (value: `"bfvcE"`)

* `bfvc13` (value: `"bfvc13"`)

* `bfvc15` (value: `"bfvc15"`)

* `bfvc18` (value: `"bfvc18"`)

* `bfvc20` (value: `"bfvc20"`)

* `bfvcB` (value: `"bfvcB"`)

* `bfvcUnrated` (value: `"bfvcUnrated"`)





## Enum: BmukkRatingEnum


* `bmukkUnspecified` (value: `"bmukkUnspecified"`)

* `bmukkAa` (value: `"bmukkAa"`)

* `bmukk6` (value: `"bmukk6"`)

* `bmukk8` (value: `"bmukk8"`)

* `bmukk10` (value: `"bmukk10"`)

* `bmukk12` (value: `"bmukk12"`)

* `bmukk14` (value: `"bmukk14"`)

* `bmukk16` (value: `"bmukk16"`)

* `bmukkUnrated` (value: `"bmukkUnrated"`)





## Enum: CatvRatingEnum


* `catvUnspecified` (value: `"catvUnspecified"`)

* `catvC` (value: `"catvC"`)

* `catvC8` (value: `"catvC8"`)

* `catvG` (value: `"catvG"`)

* `catvPg` (value: `"catvPg"`)

* `catv14plus` (value: `"catv14plus"`)

* `catv18plus` (value: `"catv18plus"`)

* `catvUnrated` (value: `"catvUnrated"`)

* `catvE` (value: `"catvE"`)





## Enum: CatvfrRatingEnum


* `catvfrUnspecified` (value: `"catvfrUnspecified"`)

* `catvfrG` (value: `"catvfrG"`)

* `catvfr8plus` (value: `"catvfr8plus"`)

* `catvfr13plus` (value: `"catvfr13plus"`)

* `catvfr16plus` (value: `"catvfr16plus"`)

* `catvfr18plus` (value: `"catvfr18plus"`)

* `catvfrUnrated` (value: `"catvfrUnrated"`)

* `catvfrE` (value: `"catvfrE"`)





## Enum: CbfcRatingEnum


* `cbfcUnspecified` (value: `"cbfcUnspecified"`)

* `cbfcU` (value: `"cbfcU"`)

* `cbfcUA` (value: `"cbfcUA"`)

* `cbfcUA7plus` (value: `"cbfcUA7plus"`)

* `cbfcUA13plus` (value: `"cbfcUA13plus"`)

* `cbfcUA16plus` (value: `"cbfcUA16plus"`)

* `cbfcA` (value: `"cbfcA"`)

* `cbfcS` (value: `"cbfcS"`)

* `cbfcUnrated` (value: `"cbfcUnrated"`)





## Enum: CccRatingEnum


* `cccUnspecified` (value: `"cccUnspecified"`)

* `cccTe` (value: `"cccTe"`)

* `ccc6` (value: `"ccc6"`)

* `ccc14` (value: `"ccc14"`)

* `ccc18` (value: `"ccc18"`)

* `ccc18v` (value: `"ccc18v"`)

* `ccc18s` (value: `"ccc18s"`)

* `cccUnrated` (value: `"cccUnrated"`)





## Enum: CceRatingEnum


* `cceUnspecified` (value: `"cceUnspecified"`)

* `cceM4` (value: `"cceM4"`)

* `cceM6` (value: `"cceM6"`)

* `cceM12` (value: `"cceM12"`)

* `cceM16` (value: `"cceM16"`)

* `cceM18` (value: `"cceM18"`)

* `cceUnrated` (value: `"cceUnrated"`)

* `cceM14` (value: `"cceM14"`)





## Enum: ChfilmRatingEnum


* `chfilmUnspecified` (value: `"chfilmUnspecified"`)

* `chfilm0` (value: `"chfilm0"`)

* `chfilm6` (value: `"chfilm6"`)

* `chfilm12` (value: `"chfilm12"`)

* `chfilm16` (value: `"chfilm16"`)

* `chfilm18` (value: `"chfilm18"`)

* `chfilmUnrated` (value: `"chfilmUnrated"`)





## Enum: ChvrsRatingEnum


* `chvrsUnspecified` (value: `"chvrsUnspecified"`)

* `chvrsG` (value: `"chvrsG"`)

* `chvrsPg` (value: `"chvrsPg"`)

* `chvrs14a` (value: `"chvrs14a"`)

* `chvrs18a` (value: `"chvrs18a"`)

* `chvrsR` (value: `"chvrsR"`)

* `chvrsE` (value: `"chvrsE"`)

* `chvrsUnrated` (value: `"chvrsUnrated"`)





## Enum: CicfRatingEnum


* `cicfUnspecified` (value: `"cicfUnspecified"`)

* `cicfE` (value: `"cicfE"`)

* `cicfKtEa` (value: `"cicfKtEa"`)

* `cicfKntEna` (value: `"cicfKntEna"`)

* `cicfUnrated` (value: `"cicfUnrated"`)





## Enum: CnaRatingEnum


* `cnaUnspecified` (value: `"cnaUnspecified"`)

* `cnaAp` (value: `"cnaAp"`)

* `cna12` (value: `"cna12"`)

* `cna15` (value: `"cna15"`)

* `cna18` (value: `"cna18"`)

* `cna18plus` (value: `"cna18plus"`)

* `cnaUnrated` (value: `"cnaUnrated"`)





## Enum: CncRatingEnum


* `cncUnspecified` (value: `"cncUnspecified"`)

* `cncT` (value: `"cncT"`)

* `cnc10` (value: `"cnc10"`)

* `cnc12` (value: `"cnc12"`)

* `cnc16` (value: `"cnc16"`)

* `cnc18` (value: `"cnc18"`)

* `cncE` (value: `"cncE"`)

* `cncInterdiction` (value: `"cncInterdiction"`)

* `cncUnrated` (value: `"cncUnrated"`)





## Enum: CsaRatingEnum


* `csaUnspecified` (value: `"csaUnspecified"`)

* `csaT` (value: `"csaT"`)

* `csa10` (value: `"csa10"`)

* `csa12` (value: `"csa12"`)

* `csa16` (value: `"csa16"`)

* `csa18` (value: `"csa18"`)

* `csaInterdiction` (value: `"csaInterdiction"`)

* `csaUnrated` (value: `"csaUnrated"`)





## Enum: CscfRatingEnum


* `cscfUnspecified` (value: `"cscfUnspecified"`)

* `cscfAl` (value: `"cscfAl"`)

* `cscfA` (value: `"cscfA"`)

* `cscf6` (value: `"cscf6"`)

* `cscf9` (value: `"cscf9"`)

* `cscf12` (value: `"cscf12"`)

* `cscf16` (value: `"cscf16"`)

* `cscf18` (value: `"cscf18"`)

* `cscfUnrated` (value: `"cscfUnrated"`)





## Enum: CzfilmRatingEnum


* `czfilmUnspecified` (value: `"czfilmUnspecified"`)

* `czfilmU` (value: `"czfilmU"`)

* `czfilm12` (value: `"czfilm12"`)

* `czfilm14` (value: `"czfilm14"`)

* `czfilm18` (value: `"czfilm18"`)

* `czfilmUnrated` (value: `"czfilmUnrated"`)





## Enum: DjctqRatingEnum


* `djctqUnspecified` (value: `"djctqUnspecified"`)

* `djctqL` (value: `"djctqL"`)

* `djctq10` (value: `"djctq10"`)

* `djctq12` (value: `"djctq12"`)

* `djctq14` (value: `"djctq14"`)

* `djctq16` (value: `"djctq16"`)

* `djctq18` (value: `"djctq18"`)

* `djctqEr` (value: `"djctqEr"`)

* `djctqL10` (value: `"djctqL10"`)

* `djctqL12` (value: `"djctqL12"`)

* `djctqL14` (value: `"djctqL14"`)

* `djctqL16` (value: `"djctqL16"`)

* `djctqL18` (value: `"djctqL18"`)

* `djctq1012` (value: `"djctq1012"`)

* `djctq1014` (value: `"djctq1014"`)

* `djctq1016` (value: `"djctq1016"`)

* `djctq1018` (value: `"djctq1018"`)

* `djctq1214` (value: `"djctq1214"`)

* `djctq1216` (value: `"djctq1216"`)

* `djctq1218` (value: `"djctq1218"`)

* `djctq1416` (value: `"djctq1416"`)

* `djctq1418` (value: `"djctq1418"`)

* `djctq1618` (value: `"djctq1618"`)

* `djctqUnrated` (value: `"djctqUnrated"`)





## Enum: [DjctqRatingReasonsEnum]


* `djctqRatingReasonUnspecified` (value: `"djctqRatingReasonUnspecified"`)

* `djctqViolence` (value: `"djctqViolence"`)

* `djctqExtremeViolence` (value: `"djctqExtremeViolence"`)

* `djctqSexualContent` (value: `"djctqSexualContent"`)

* `djctqNudity` (value: `"djctqNudity"`)

* `djctqSex` (value: `"djctqSex"`)

* `djctqExplicitSex` (value: `"djctqExplicitSex"`)

* `djctqDrugs` (value: `"djctqDrugs"`)

* `djctqLegalDrugs` (value: `"djctqLegalDrugs"`)

* `djctqIllegalDrugs` (value: `"djctqIllegalDrugs"`)

* `djctqInappropriateLanguage` (value: `"djctqInappropriateLanguage"`)

* `djctqCriminalActs` (value: `"djctqCriminalActs"`)

* `djctqImpactingContent` (value: `"djctqImpactingContent"`)





## Enum: EcbmctRatingEnum


* `ecbmctUnspecified` (value: `"ecbmctUnspecified"`)

* `ecbmctG` (value: `"ecbmctG"`)

* `ecbmct7a` (value: `"ecbmct7a"`)

* `ecbmct7plus` (value: `"ecbmct7plus"`)

* `ecbmct13a` (value: `"ecbmct13a"`)

* `ecbmct13plus` (value: `"ecbmct13plus"`)

* `ecbmct15a` (value: `"ecbmct15a"`)

* `ecbmct15plus` (value: `"ecbmct15plus"`)

* `ecbmct18plus` (value: `"ecbmct18plus"`)

* `ecbmctUnrated` (value: `"ecbmctUnrated"`)





## Enum: EefilmRatingEnum


* `eefilmUnspecified` (value: `"eefilmUnspecified"`)

* `eefilmPere` (value: `"eefilmPere"`)

* `eefilmL` (value: `"eefilmL"`)

* `eefilmMs6` (value: `"eefilmMs6"`)

* `eefilmK6` (value: `"eefilmK6"`)

* `eefilmMs12` (value: `"eefilmMs12"`)

* `eefilmK12` (value: `"eefilmK12"`)

* `eefilmK14` (value: `"eefilmK14"`)

* `eefilmK16` (value: `"eefilmK16"`)

* `eefilmUnrated` (value: `"eefilmUnrated"`)





## Enum: EgfilmRatingEnum


* `egfilmUnspecified` (value: `"egfilmUnspecified"`)

* `egfilmGn` (value: `"egfilmGn"`)

* `egfilm18` (value: `"egfilm18"`)

* `egfilmBn` (value: `"egfilmBn"`)

* `egfilmUnrated` (value: `"egfilmUnrated"`)





## Enum: EirinRatingEnum


* `eirinUnspecified` (value: `"eirinUnspecified"`)

* `eirinG` (value: `"eirinG"`)

* `eirinPg12` (value: `"eirinPg12"`)

* `eirinR15plus` (value: `"eirinR15plus"`)

* `eirinR18plus` (value: `"eirinR18plus"`)

* `eirinUnrated` (value: `"eirinUnrated"`)





## Enum: FcbmRatingEnum


* `fcbmUnspecified` (value: `"fcbmUnspecified"`)

* `fcbmU` (value: `"fcbmU"`)

* `fcbmPg13` (value: `"fcbmPg13"`)

* `fcbmP13` (value: `"fcbmP13"`)

* `fcbm18` (value: `"fcbm18"`)

* `fcbm18sx` (value: `"fcbm18sx"`)

* `fcbm18pa` (value: `"fcbm18pa"`)

* `fcbm18sg` (value: `"fcbm18sg"`)

* `fcbm18pl` (value: `"fcbm18pl"`)

* `fcbmUnrated` (value: `"fcbmUnrated"`)





## Enum: FcoRatingEnum


* `fcoUnspecified` (value: `"fcoUnspecified"`)

* `fcoI` (value: `"fcoI"`)

* `fcoIia` (value: `"fcoIia"`)

* `fcoIib` (value: `"fcoIib"`)

* `fcoIi` (value: `"fcoIi"`)

* `fcoIii` (value: `"fcoIii"`)

* `fcoUnrated` (value: `"fcoUnrated"`)





## Enum: FmocRatingEnum


* `fmocUnspecified` (value: `"fmocUnspecified"`)

* `fmocU` (value: `"fmocU"`)

* `fmoc10` (value: `"fmoc10"`)

* `fmoc12` (value: `"fmoc12"`)

* `fmoc16` (value: `"fmoc16"`)

* `fmoc18` (value: `"fmoc18"`)

* `fmocE` (value: `"fmocE"`)

* `fmocUnrated` (value: `"fmocUnrated"`)





## Enum: FpbRatingEnum


* `fpbUnspecified` (value: `"fpbUnspecified"`)

* `fpbA` (value: `"fpbA"`)

* `fpbPg` (value: `"fpbPg"`)

* `fpb79Pg` (value: `"fpb79Pg"`)

* `fpb1012Pg` (value: `"fpb1012Pg"`)

* `fpb13` (value: `"fpb13"`)

* `fpb16` (value: `"fpb16"`)

* `fpb18` (value: `"fpb18"`)

* `fpbX18` (value: `"fpbX18"`)

* `fpbXx` (value: `"fpbXx"`)

* `fpbUnrated` (value: `"fpbUnrated"`)

* `fpb10` (value: `"fpb10"`)





## Enum: [FpbRatingReasonsEnum]


* `fpbRatingReasonUnspecified` (value: `"fpbRatingReasonUnspecified"`)

* `fpbBlasphemy` (value: `"fpbBlasphemy"`)

* `fpbLanguage` (value: `"fpbLanguage"`)

* `fpbNudity` (value: `"fpbNudity"`)

* `fpbPrejudice` (value: `"fpbPrejudice"`)

* `fpbSex` (value: `"fpbSex"`)

* `fpbViolence` (value: `"fpbViolence"`)

* `fpbDrugs` (value: `"fpbDrugs"`)

* `fpbSexualViolence` (value: `"fpbSexualViolence"`)

* `fpbHorror` (value: `"fpbHorror"`)

* `fpbCriminalTechniques` (value: `"fpbCriminalTechniques"`)

* `fpbImitativeActsTechniques` (value: `"fpbImitativeActsTechniques"`)





## Enum: FskRatingEnum


* `fskUnspecified` (value: `"fskUnspecified"`)

* `fsk0` (value: `"fsk0"`)

* `fsk6` (value: `"fsk6"`)

* `fsk12` (value: `"fsk12"`)

* `fsk16` (value: `"fsk16"`)

* `fsk18` (value: `"fsk18"`)

* `fskUnrated` (value: `"fskUnrated"`)





## Enum: GrfilmRatingEnum


* `grfilmUnspecified` (value: `"grfilmUnspecified"`)

* `grfilmK` (value: `"grfilmK"`)

* `grfilmE` (value: `"grfilmE"`)

* `grfilmK12` (value: `"grfilmK12"`)

* `grfilmK13` (value: `"grfilmK13"`)

* `grfilmK15` (value: `"grfilmK15"`)

* `grfilmK17` (value: `"grfilmK17"`)

* `grfilmK18` (value: `"grfilmK18"`)

* `grfilmUnrated` (value: `"grfilmUnrated"`)





## Enum: IcaaRatingEnum


* `icaaUnspecified` (value: `"icaaUnspecified"`)

* `icaaApta` (value: `"icaaApta"`)

* `icaa7` (value: `"icaa7"`)

* `icaa12` (value: `"icaa12"`)

* `icaa13` (value: `"icaa13"`)

* `icaa16` (value: `"icaa16"`)

* `icaa18` (value: `"icaa18"`)

* `icaaX` (value: `"icaaX"`)

* `icaaUnrated` (value: `"icaaUnrated"`)





## Enum: IfcoRatingEnum


* `ifcoUnspecified` (value: `"ifcoUnspecified"`)

* `ifcoG` (value: `"ifcoG"`)

* `ifcoPg` (value: `"ifcoPg"`)

* `ifco12` (value: `"ifco12"`)

* `ifco12a` (value: `"ifco12a"`)

* `ifco15` (value: `"ifco15"`)

* `ifco15a` (value: `"ifco15a"`)

* `ifco16` (value: `"ifco16"`)

* `ifco18` (value: `"ifco18"`)

* `ifcoUnrated` (value: `"ifcoUnrated"`)





## Enum: IlfilmRatingEnum


* `ilfilmUnspecified` (value: `"ilfilmUnspecified"`)

* `ilfilmAa` (value: `"ilfilmAa"`)

* `ilfilm12` (value: `"ilfilm12"`)

* `ilfilm14` (value: `"ilfilm14"`)

* `ilfilm16` (value: `"ilfilm16"`)

* `ilfilm18` (value: `"ilfilm18"`)

* `ilfilmUnrated` (value: `"ilfilmUnrated"`)





## Enum: IncaaRatingEnum


* `incaaUnspecified` (value: `"incaaUnspecified"`)

* `incaaAtp` (value: `"incaaAtp"`)

* `incaaSam13` (value: `"incaaSam13"`)

* `incaaSam16` (value: `"incaaSam16"`)

* `incaaSam18` (value: `"incaaSam18"`)

* `incaaC` (value: `"incaaC"`)

* `incaaUnrated` (value: `"incaaUnrated"`)





## Enum: KfcbRatingEnum


* `kfcbUnspecified` (value: `"kfcbUnspecified"`)

* `kfcbG` (value: `"kfcbG"`)

* `kfcbPg` (value: `"kfcbPg"`)

* `kfcb16plus` (value: `"kfcb16plus"`)

* `kfcbR` (value: `"kfcbR"`)

* `kfcbUnrated` (value: `"kfcbUnrated"`)





## Enum: KijkwijzerRatingEnum


* `kijkwijzerUnspecified` (value: `"kijkwijzerUnspecified"`)

* `kijkwijzerAl` (value: `"kijkwijzerAl"`)

* `kijkwijzer6` (value: `"kijkwijzer6"`)

* `kijkwijzer9` (value: `"kijkwijzer9"`)

* `kijkwijzer12` (value: `"kijkwijzer12"`)

* `kijkwijzer16` (value: `"kijkwijzer16"`)

* `kijkwijzer18` (value: `"kijkwijzer18"`)

* `kijkwijzerUnrated` (value: `"kijkwijzerUnrated"`)





## Enum: KmrbRatingEnum


* `kmrbUnspecified` (value: `"kmrbUnspecified"`)

* `kmrbAll` (value: `"kmrbAll"`)

* `kmrb12plus` (value: `"kmrb12plus"`)

* `kmrb15plus` (value: `"kmrb15plus"`)

* `kmrbTeenr` (value: `"kmrbTeenr"`)

* `kmrbR` (value: `"kmrbR"`)

* `kmrbUnrated` (value: `"kmrbUnrated"`)





## Enum: LsfRatingEnum


* `lsfUnspecified` (value: `"lsfUnspecified"`)

* `lsfSu` (value: `"lsfSu"`)

* `lsfA` (value: `"lsfA"`)

* `lsfBo` (value: `"lsfBo"`)

* `lsf13` (value: `"lsf13"`)

* `lsfR` (value: `"lsfR"`)

* `lsf17` (value: `"lsf17"`)

* `lsfD` (value: `"lsfD"`)

* `lsf21` (value: `"lsf21"`)

* `lsfUnrated` (value: `"lsfUnrated"`)





## Enum: MccaaRatingEnum


* `mccaaUnspecified` (value: `"mccaaUnspecified"`)

* `mccaaU` (value: `"mccaaU"`)

* `mccaaPg` (value: `"mccaaPg"`)

* `mccaa12a` (value: `"mccaa12a"`)

* `mccaa12` (value: `"mccaa12"`)

* `mccaa14` (value: `"mccaa14"`)

* `mccaa15` (value: `"mccaa15"`)

* `mccaa16` (value: `"mccaa16"`)

* `mccaa18` (value: `"mccaa18"`)

* `mccaaUnrated` (value: `"mccaaUnrated"`)





## Enum: MccypRatingEnum


* `mccypUnspecified` (value: `"mccypUnspecified"`)

* `mccypA` (value: `"mccypA"`)

* `mccyp7` (value: `"mccyp7"`)

* `mccyp11` (value: `"mccyp11"`)

* `mccyp15` (value: `"mccyp15"`)

* `mccypUnrated` (value: `"mccypUnrated"`)





## Enum: McstRatingEnum


* `mcstUnspecified` (value: `"mcstUnspecified"`)

* `mcstP` (value: `"mcstP"`)

* `mcst0` (value: `"mcst0"`)

* `mcstC13` (value: `"mcstC13"`)

* `mcstC16` (value: `"mcstC16"`)

* `mcst16plus` (value: `"mcst16plus"`)

* `mcstC18` (value: `"mcstC18"`)

* `mcstGPg` (value: `"mcstGPg"`)

* `mcstUnrated` (value: `"mcstUnrated"`)





## Enum: MdaRatingEnum


* `mdaUnspecified` (value: `"mdaUnspecified"`)

* `mdaG` (value: `"mdaG"`)

* `mdaPg` (value: `"mdaPg"`)

* `mdaPg13` (value: `"mdaPg13"`)

* `mdaNc16` (value: `"mdaNc16"`)

* `mdaM18` (value: `"mdaM18"`)

* `mdaR21` (value: `"mdaR21"`)

* `mdaUnrated` (value: `"mdaUnrated"`)





## Enum: MedietilsynetRatingEnum


* `medietilsynetUnspecified` (value: `"medietilsynetUnspecified"`)

* `medietilsynetA` (value: `"medietilsynetA"`)

* `medietilsynet6` (value: `"medietilsynet6"`)

* `medietilsynet7` (value: `"medietilsynet7"`)

* `medietilsynet9` (value: `"medietilsynet9"`)

* `medietilsynet11` (value: `"medietilsynet11"`)

* `medietilsynet12` (value: `"medietilsynet12"`)

* `medietilsynet15` (value: `"medietilsynet15"`)

* `medietilsynet18` (value: `"medietilsynet18"`)

* `medietilsynetUnrated` (value: `"medietilsynetUnrated"`)





## Enum: MekuRatingEnum


* `mekuUnspecified` (value: `"mekuUnspecified"`)

* `mekuS` (value: `"mekuS"`)

* `meku7` (value: `"meku7"`)

* `meku12` (value: `"meku12"`)

* `meku16` (value: `"meku16"`)

* `meku18` (value: `"meku18"`)

* `mekuUnrated` (value: `"mekuUnrated"`)





## Enum: MenaMpaaRatingEnum


* `menaMpaaUnspecified` (value: `"menaMpaaUnspecified"`)

* `menaMpaaG` (value: `"menaMpaaG"`)

* `menaMpaaPg` (value: `"menaMpaaPg"`)

* `menaMpaaPg13` (value: `"menaMpaaPg13"`)

* `menaMpaaR` (value: `"menaMpaaR"`)

* `menaMpaaUnrated` (value: `"menaMpaaUnrated"`)





## Enum: MibacRatingEnum


* `mibacUnspecified` (value: `"mibacUnspecified"`)

* `mibacT` (value: `"mibacT"`)

* `mibacVap` (value: `"mibacVap"`)

* `mibacVm6` (value: `"mibacVm6"`)

* `mibacVm12` (value: `"mibacVm12"`)

* `mibacVm14` (value: `"mibacVm14"`)

* `mibacVm16` (value: `"mibacVm16"`)

* `mibacVm18` (value: `"mibacVm18"`)

* `mibacUnrated` (value: `"mibacUnrated"`)





## Enum: MocRatingEnum


* `mocUnspecified` (value: `"mocUnspecified"`)

* `mocE` (value: `"mocE"`)

* `mocT` (value: `"mocT"`)

* `moc7` (value: `"moc7"`)

* `moc12` (value: `"moc12"`)

* `moc15` (value: `"moc15"`)

* `moc18` (value: `"moc18"`)

* `mocX` (value: `"mocX"`)

* `mocBanned` (value: `"mocBanned"`)

* `mocUnrated` (value: `"mocUnrated"`)





## Enum: MoctwRatingEnum


* `moctwUnspecified` (value: `"moctwUnspecified"`)

* `moctwG` (value: `"moctwG"`)

* `moctwP` (value: `"moctwP"`)

* `moctwPg` (value: `"moctwPg"`)

* `moctwR` (value: `"moctwR"`)

* `moctwUnrated` (value: `"moctwUnrated"`)

* `moctwR12` (value: `"moctwR12"`)

* `moctwR15` (value: `"moctwR15"`)





## Enum: MpaaRatingEnum


* `mpaaUnspecified` (value: `"mpaaUnspecified"`)

* `mpaaG` (value: `"mpaaG"`)

* `mpaaPg` (value: `"mpaaPg"`)

* `mpaaPg13` (value: `"mpaaPg13"`)

* `mpaaR` (value: `"mpaaR"`)

* `mpaaNc17` (value: `"mpaaNc17"`)

* `mpaaX` (value: `"mpaaX"`)

* `mpaaUnrated` (value: `"mpaaUnrated"`)





## Enum: MpaatRatingEnum


* `mpaatUnspecified` (value: `"mpaatUnspecified"`)

* `mpaatGb` (value: `"mpaatGb"`)

* `mpaatRb` (value: `"mpaatRb"`)





## Enum: MtrcbRatingEnum


* `mtrcbUnspecified` (value: `"mtrcbUnspecified"`)

* `mtrcbG` (value: `"mtrcbG"`)

* `mtrcbPg` (value: `"mtrcbPg"`)

* `mtrcbR13` (value: `"mtrcbR13"`)

* `mtrcbR16` (value: `"mtrcbR16"`)

* `mtrcbR18` (value: `"mtrcbR18"`)

* `mtrcbX` (value: `"mtrcbX"`)

* `mtrcbUnrated` (value: `"mtrcbUnrated"`)





## Enum: NbcRatingEnum


* `nbcUnspecified` (value: `"nbcUnspecified"`)

* `nbcG` (value: `"nbcG"`)

* `nbcPg` (value: `"nbcPg"`)

* `nbc12plus` (value: `"nbc12plus"`)

* `nbc15plus` (value: `"nbc15plus"`)

* `nbc18plus` (value: `"nbc18plus"`)

* `nbc18plusr` (value: `"nbc18plusr"`)

* `nbcPu` (value: `"nbcPu"`)

* `nbcUnrated` (value: `"nbcUnrated"`)





## Enum: NbcplRatingEnum


* `nbcplUnspecified` (value: `"nbcplUnspecified"`)

* `nbcplI` (value: `"nbcplI"`)

* `nbcplIi` (value: `"nbcplIi"`)

* `nbcplIii` (value: `"nbcplIii"`)

* `nbcplIv` (value: `"nbcplIv"`)

* `nbcpl18plus` (value: `"nbcpl18plus"`)

* `nbcplUnrated` (value: `"nbcplUnrated"`)





## Enum: NfrcRatingEnum


* `nfrcUnspecified` (value: `"nfrcUnspecified"`)

* `nfrcA` (value: `"nfrcA"`)

* `nfrcB` (value: `"nfrcB"`)

* `nfrcC` (value: `"nfrcC"`)

* `nfrcD` (value: `"nfrcD"`)

* `nfrcX` (value: `"nfrcX"`)

* `nfrcUnrated` (value: `"nfrcUnrated"`)





## Enum: NfvcbRatingEnum


* `nfvcbUnspecified` (value: `"nfvcbUnspecified"`)

* `nfvcbG` (value: `"nfvcbG"`)

* `nfvcbPg` (value: `"nfvcbPg"`)

* `nfvcb12` (value: `"nfvcb12"`)

* `nfvcb12a` (value: `"nfvcb12a"`)

* `nfvcb15` (value: `"nfvcb15"`)

* `nfvcb18` (value: `"nfvcb18"`)

* `nfvcbRe` (value: `"nfvcbRe"`)

* `nfvcbUnrated` (value: `"nfvcbUnrated"`)





## Enum: NkclvRatingEnum


* `nkclvUnspecified` (value: `"nkclvUnspecified"`)

* `nkclvU` (value: `"nkclvU"`)

* `nkclv7plus` (value: `"nkclv7plus"`)

* `nkclv12plus` (value: `"nkclv12plus"`)

* `nkclv16plus` (value: `"nkclv16plus"`)

* `nkclv18plus` (value: `"nkclv18plus"`)

* `nkclvUnrated` (value: `"nkclvUnrated"`)





## Enum: NmcRatingEnum


* `nmcUnspecified` (value: `"nmcUnspecified"`)

* `nmcG` (value: `"nmcG"`)

* `nmcPg` (value: `"nmcPg"`)

* `nmcPg13` (value: `"nmcPg13"`)

* `nmcPg15` (value: `"nmcPg15"`)

* `nmc15plus` (value: `"nmc15plus"`)

* `nmc18plus` (value: `"nmc18plus"`)

* `nmc18tc` (value: `"nmc18tc"`)

* `nmcUnrated` (value: `"nmcUnrated"`)





## Enum: OflcRatingEnum


* `oflcUnspecified` (value: `"oflcUnspecified"`)

* `oflcG` (value: `"oflcG"`)

* `oflcPg` (value: `"oflcPg"`)

* `oflcM` (value: `"oflcM"`)

* `oflcR13` (value: `"oflcR13"`)

* `oflcR15` (value: `"oflcR15"`)

* `oflcR16` (value: `"oflcR16"`)

* `oflcR18` (value: `"oflcR18"`)

* `oflcUnrated` (value: `"oflcUnrated"`)

* `oflcRp13` (value: `"oflcRp13"`)

* `oflcRp16` (value: `"oflcRp16"`)

* `oflcRp18` (value: `"oflcRp18"`)





## Enum: PefilmRatingEnum


* `pefilmUnspecified` (value: `"pefilmUnspecified"`)

* `pefilmPt` (value: `"pefilmPt"`)

* `pefilmPg` (value: `"pefilmPg"`)

* `pefilm14` (value: `"pefilm14"`)

* `pefilm18` (value: `"pefilm18"`)

* `pefilmUnrated` (value: `"pefilmUnrated"`)





## Enum: RcnofRatingEnum


* `rcnofUnspecified` (value: `"rcnofUnspecified"`)

* `rcnofI` (value: `"rcnofI"`)

* `rcnofIi` (value: `"rcnofIi"`)

* `rcnofIii` (value: `"rcnofIii"`)

* `rcnofIv` (value: `"rcnofIv"`)

* `rcnofV` (value: `"rcnofV"`)

* `rcnofVi` (value: `"rcnofVi"`)

* `rcnofUnrated` (value: `"rcnofUnrated"`)





## Enum: ResorteviolenciaRatingEnum


* `resorteviolenciaUnspecified` (value: `"resorteviolenciaUnspecified"`)

* `resorteviolenciaA` (value: `"resorteviolenciaA"`)

* `resorteviolenciaB` (value: `"resorteviolenciaB"`)

* `resorteviolenciaC` (value: `"resorteviolenciaC"`)

* `resorteviolenciaD` (value: `"resorteviolenciaD"`)

* `resorteviolenciaE` (value: `"resorteviolenciaE"`)

* `resorteviolenciaUnrated` (value: `"resorteviolenciaUnrated"`)





## Enum: RtcRatingEnum


* `rtcUnspecified` (value: `"rtcUnspecified"`)

* `rtcAa` (value: `"rtcAa"`)

* `rtcA` (value: `"rtcA"`)

* `rtcB` (value: `"rtcB"`)

* `rtcB15` (value: `"rtcB15"`)

* `rtcC` (value: `"rtcC"`)

* `rtcD` (value: `"rtcD"`)

* `rtcUnrated` (value: `"rtcUnrated"`)





## Enum: RteRatingEnum


* `rteUnspecified` (value: `"rteUnspecified"`)

* `rteGa` (value: `"rteGa"`)

* `rteCh` (value: `"rteCh"`)

* `rtePs` (value: `"rtePs"`)

* `rteMa` (value: `"rteMa"`)

* `rteUnrated` (value: `"rteUnrated"`)





## Enum: RussiaRatingEnum


* `russiaUnspecified` (value: `"russiaUnspecified"`)

* `russia0` (value: `"russia0"`)

* `russia6` (value: `"russia6"`)

* `russia12` (value: `"russia12"`)

* `russia16` (value: `"russia16"`)

* `russia18` (value: `"russia18"`)

* `russiaUnrated` (value: `"russiaUnrated"`)





## Enum: SkfilmRatingEnum


* `skfilmUnspecified` (value: `"skfilmUnspecified"`)

* `skfilmG` (value: `"skfilmG"`)

* `skfilmP2` (value: `"skfilmP2"`)

* `skfilmP5` (value: `"skfilmP5"`)

* `skfilmP8` (value: `"skfilmP8"`)

* `skfilmUnrated` (value: `"skfilmUnrated"`)





## Enum: SmaisRatingEnum


* `smaisUnspecified` (value: `"smaisUnspecified"`)

* `smaisL` (value: `"smaisL"`)

* `smais7` (value: `"smais7"`)

* `smais12` (value: `"smais12"`)

* `smais14` (value: `"smais14"`)

* `smais16` (value: `"smais16"`)

* `smais18` (value: `"smais18"`)

* `smaisUnrated` (value: `"smaisUnrated"`)





## Enum: SmsaRatingEnum


* `smsaUnspecified` (value: `"smsaUnspecified"`)

* `smsaA` (value: `"smsaA"`)

* `smsa7` (value: `"smsa7"`)

* `smsa11` (value: `"smsa11"`)

* `smsa15` (value: `"smsa15"`)

* `smsaUnrated` (value: `"smsaUnrated"`)





## Enum: TvpgRatingEnum


* `tvpgUnspecified` (value: `"tvpgUnspecified"`)

* `tvpgY` (value: `"tvpgY"`)

* `tvpgY7` (value: `"tvpgY7"`)

* `tvpgY7Fv` (value: `"tvpgY7Fv"`)

* `tvpgG` (value: `"tvpgG"`)

* `tvpgPg` (value: `"tvpgPg"`)

* `pg14` (value: `"pg14"`)

* `tvpgMa` (value: `"tvpgMa"`)

* `tvpgUnrated` (value: `"tvpgUnrated"`)





## Enum: YtRatingEnum


* `ytUnspecified` (value: `"ytUnspecified"`)

* `ytAgeRestricted` (value: `"ytAgeRestricted"`)




