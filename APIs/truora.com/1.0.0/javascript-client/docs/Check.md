# ChecksApi.Check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthCertificate** | **String** | Person birth certificate | [optional] 
**checkId** | **String** | Background check ID | 
**companySummary** | [**CompanySummary**](CompanySummary.md) |  | [optional] 
**country** | **String** | ID Document country | 
**creationDate** | **Date** | Background check creation date | 
**dateOfBirth** | **Date** | Person birthdate. Shown only if provided during check creation. YYYY-MM-DD format | [optional] 
**diplomaticId** | **String** | Person diplomatic id | [optional] 
**driverLicense** | **String** | Person driver&#39;s license | [optional] 
**firstName** | **String** | Person or entity first name. Shown only if provided during check creation | [optional] 
**foreignId** | **String** | Person foreign identification | [optional] 
**homonymProbability** | **Number** | [Experimental] Analyzes the probability that the results by name are attributed to a homonym. Number between 0 and 1 where 1 is the the greatest probability | [optional] 
**homonymScore** | **Number** | Background check score including results by name only. This might contain homonym information | [optional] 
**homonymScores** | [**[Score]**](Score.md) | Background check scores by name for each profile group. [Deprecated for API key V1] | [optional] 
**idScore** | **Number** | Background check score regarding results by ID number only. It is a number between 0 and 1 where 1 is the best score. This result is a weighted average of the id_scores listed under scores. | 
**issueDate** | **Date** | Issue date of the person ID | [optional] 
**lastName** | **String** | Person or entity last name. Shown only if provided during check creation | [optional] 
**licensePlate** | **String** | Vehicle license plate | [optional] 
**nationalId** | **String** | Person national identification | [optional] 
**nativeCountry** | **String** | Person origin country | [optional] 
**ownerDocumentId** | **String** | Vehicle owner identification | [optional] 
**ownerDocumentType** | **String** | Vehicle owner document type | [optional] 
**passport** | **String** | Person passport | [optional] 
**paymentDate** | **String** | Vehicle license payment date | [optional] 
**pep** | **String** | Colombian PEP idenfitication for Venezuelans | [optional] 
**phoneNumber** | **String** | Person phone number. Required by law in order to notify the person their background is being checked | [optional] 
**professionalCard** | **String** | Person professional card number | [optional] 
**ptp** | **String** | Temporary residence permit of the person | [optional] 
**region** | **String** | Region where the background is to be checked. By default, background checks in Brazil are performed in region where the person is from. Applies for some Brazil collectors only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.   | [optional] 
**reportId** | **String** | Report ID the background check is associated with | [optional] 
**score** | **Number** | Background check score. Number between 0 and 1 where 1 is the best score | 
**scores** | [**[Score]**](Score.md) | Background check score of each profile group and dataset | [optional] 
**status** | **String** | Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the check finished successfully, **error** means the check failed, **in_progress** means the check is currently being processed, **delayed** means the check is waiting for an additional requirement to be met, this can last up to 3 days. **Completed** and **error** are the two only final statuses | 
**statuses** | [**[Status]**](Status.md) | Database status list | 
**summary** | [**Summary**](Summary.md) |  | 
**taxId** | **String** | Person or company tax id | [optional] 
**type** | **String** | Background check type | 
**updateDate** | **Date** | Background check update date | [optional] 
**vehicleId** | **String** | Vehicle identification | [optional] 
**vehicleSummary** | [**VehicleSummary**](VehicleSummary.md) |  | [optional] 
**wrongInputs** | [**[WrongInput]**](WrongInput.md) | List of parameters entered during background check creation that do not match the information obtained | [optional] 



## Enum: CountryEnum


* `ALL` (value: `"ALL"`)

* `BR` (value: `"BR"`)

* `CL` (value: `"CL"`)

* `CO` (value: `"CO"`)

* `CR` (value: `"CR"`)

* `EC` (value: `"EC"`)

* `MX` (value: `"MX"`)

* `PE` (value: `"PE"`)

* `AR` (value: `"AR"`)





## Enum: NativeCountryEnum


* `ad` (value: `"ad"`)

* `ae` (value: `"ae"`)

* `af` (value: `"af"`)

* `ag` (value: `"ag"`)

* `ai` (value: `"ai"`)

* `al` (value: `"al"`)

* `am` (value: `"am"`)

* `an` (value: `"an"`)

* `ao` (value: `"ao"`)

* `aq` (value: `"aq"`)

* `ar` (value: `"ar"`)

* `as` (value: `"as"`)

* `at` (value: `"at"`)

* `au` (value: `"au"`)

* `aw` (value: `"aw"`)

* `ax` (value: `"ax"`)

* `az` (value: `"az"`)

* `ba` (value: `"ba"`)

* `bb` (value: `"bb"`)

* `bd` (value: `"bd"`)

* `be` (value: `"be"`)

* `bf` (value: `"bf"`)

* `bg` (value: `"bg"`)

* `bh` (value: `"bh"`)

* `bi` (value: `"bi"`)

* `bj` (value: `"bj"`)

* `bm` (value: `"bm"`)

* `bn` (value: `"bn"`)

* `bo` (value: `"bo"`)

* `br` (value: `"br"`)

* `bs` (value: `"bs"`)

* `bt` (value: `"bt"`)

* `bv` (value: `"bv"`)

* `bw` (value: `"bw"`)

* `by` (value: `"by"`)

* `bz` (value: `"bz"`)

* `ca` (value: `"ca"`)

* `cc` (value: `"cc"`)

* `cd` (value: `"cd"`)

* `cf` (value: `"cf"`)

* `cg` (value: `"cg"`)

* `ch` (value: `"ch"`)

* `ci` (value: `"ci"`)

* `ck` (value: `"ck"`)

* `cl` (value: `"cl"`)

* `cm` (value: `"cm"`)

* `cn` (value: `"cn"`)

* `co` (value: `"co"`)

* `cr` (value: `"cr"`)

* `cu` (value: `"cu"`)

* `cv` (value: `"cv"`)

* `cx` (value: `"cx"`)

* `cy` (value: `"cy"`)

* `cz` (value: `"cz"`)

* `de` (value: `"de"`)

* `dj` (value: `"dj"`)

* `dk` (value: `"dk"`)

* `dm` (value: `"dm"`)

* `do` (value: `"do"`)

* `dz` (value: `"dz"`)

* `ea` (value: `"ea"`)

* `ec` (value: `"ec"`)

* `ee` (value: `"ee"`)

* `eg` (value: `"eg"`)

* `eh` (value: `"eh"`)

* `er` (value: `"er"`)

* `es` (value: `"es"`)

* `et` (value: `"et"`)

* `fi` (value: `"fi"`)

* `fj` (value: `"fj"`)

* `fk` (value: `"fk"`)

* `fm` (value: `"fm"`)

* `fo` (value: `"fo"`)

* `fr` (value: `"fr"`)

* `ga` (value: `"ga"`)

* `gb` (value: `"gb"`)

* `gd` (value: `"gd"`)

* `ge` (value: `"ge"`)

* `gf` (value: `"gf"`)

* `gg` (value: `"gg"`)

* `gh` (value: `"gh"`)

* `gi` (value: `"gi"`)

* `gl` (value: `"gl"`)

* `gm` (value: `"gm"`)

* `gn` (value: `"gn"`)

* `gp` (value: `"gp"`)

* `gq` (value: `"gq"`)

* `gr` (value: `"gr"`)

* `gs` (value: `"gs"`)

* `gt` (value: `"gt"`)

* `gu` (value: `"gu"`)

* `gw` (value: `"gw"`)

* `gy` (value: `"gy"`)

* `hk` (value: `"hk"`)

* `hm` (value: `"hm"`)

* `hn` (value: `"hn"`)

* `hr` (value: `"hr"`)

* `ht` (value: `"ht"`)

* `hu` (value: `"hu"`)

* `id` (value: `"id"`)

* `ie` (value: `"ie"`)

* `il` (value: `"il"`)

* `im` (value: `"im"`)

* `in` (value: `"in"`)

* `io` (value: `"io"`)

* `iq` (value: `"iq"`)

* `ir` (value: `"ir"`)

* `is` (value: `"is"`)

* `it` (value: `"it"`)

* `je` (value: `"je"`)

* `jm` (value: `"jm"`)

* `jo` (value: `"jo"`)

* `jp` (value: `"jp"`)

* `ke` (value: `"ke"`)

* `kg` (value: `"kg"`)

* `kh` (value: `"kh"`)

* `ki` (value: `"ki"`)

* `km` (value: `"km"`)

* `kn` (value: `"kn"`)

* `kp` (value: `"kp"`)

* `kr` (value: `"kr"`)

* `kw` (value: `"kw"`)

* `ky` (value: `"ky"`)

* `kz` (value: `"kz"`)

* `la` (value: `"la"`)

* `lb` (value: `"lb"`)

* `lc` (value: `"lc"`)

* `li` (value: `"li"`)

* `lk` (value: `"lk"`)

* `lr` (value: `"lr"`)

* `ls` (value: `"ls"`)

* `lt` (value: `"lt"`)

* `lu` (value: `"lu"`)

* `lv` (value: `"lv"`)

* `ly` (value: `"ly"`)

* `ma` (value: `"ma"`)

* `mc` (value: `"mc"`)

* `md` (value: `"md"`)

* `me` (value: `"me"`)

* `mg` (value: `"mg"`)

* `mh` (value: `"mh"`)

* `mk` (value: `"mk"`)

* `ml` (value: `"ml"`)

* `mm` (value: `"mm"`)

* `mn` (value: `"mn"`)

* `mo` (value: `"mo"`)

* `mp` (value: `"mp"`)

* `mq` (value: `"mq"`)

* `mr` (value: `"mr"`)

* `ms` (value: `"ms"`)

* `mt` (value: `"mt"`)

* `mu` (value: `"mu"`)

* `mv` (value: `"mv"`)

* `mw` (value: `"mw"`)

* `mx` (value: `"mx"`)

* `my` (value: `"my"`)

* `mz` (value: `"mz"`)

* `na` (value: `"na"`)

* `nc` (value: `"nc"`)

* `ne` (value: `"ne"`)

* `nf` (value: `"nf"`)

* `ng` (value: `"ng"`)

* `ni` (value: `"ni"`)

* `nl` (value: `"nl"`)

* `false` (value: `"false"`)

* `np` (value: `"np"`)

* `nr` (value: `"nr"`)

* `nu` (value: `"nu"`)

* `nz` (value: `"nz"`)

* `om` (value: `"om"`)

* `pa` (value: `"pa"`)

* `pe` (value: `"pe"`)

* `pf` (value: `"pf"`)

* `pg` (value: `"pg"`)

* `ph` (value: `"ph"`)

* `pk` (value: `"pk"`)

* `pl` (value: `"pl"`)

* `pm` (value: `"pm"`)

* `pn` (value: `"pn"`)

* `pr` (value: `"pr"`)

* `ps` (value: `"ps"`)

* `pt` (value: `"pt"`)

* `pw` (value: `"pw"`)

* `py` (value: `"py"`)

* `qa` (value: `"qa"`)

* `re` (value: `"re"`)

* `ro` (value: `"ro"`)

* `rs` (value: `"rs"`)

* `ru` (value: `"ru"`)

* `rw` (value: `"rw"`)

* `sa` (value: `"sa"`)

* `sb` (value: `"sb"`)

* `sc` (value: `"sc"`)

* `sd` (value: `"sd"`)

* `se` (value: `"se"`)

* `sg` (value: `"sg"`)

* `sh` (value: `"sh"`)

* `si` (value: `"si"`)

* `sj` (value: `"sj"`)

* `sk` (value: `"sk"`)

* `sl` (value: `"sl"`)

* `sm` (value: `"sm"`)

* `sn` (value: `"sn"`)

* `so` (value: `"so"`)

* `sr` (value: `"sr"`)

* `st` (value: `"st"`)

* `sv` (value: `"sv"`)

* `sy` (value: `"sy"`)

* `sz` (value: `"sz"`)

* `tc` (value: `"tc"`)

* `td` (value: `"td"`)

* `tf` (value: `"tf"`)

* `tg` (value: `"tg"`)

* `th` (value: `"th"`)

* `tj` (value: `"tj"`)

* `tk` (value: `"tk"`)

* `tl` (value: `"tl"`)

* `tm` (value: `"tm"`)

* `tn` (value: `"tn"`)

* `to` (value: `"to"`)

* `tr` (value: `"tr"`)

* `tt` (value: `"tt"`)

* `tv` (value: `"tv"`)

* `tw` (value: `"tw"`)

* `tz` (value: `"tz"`)

* `ua` (value: `"ua"`)

* `ug` (value: `"ug"`)

* `um` (value: `"um"`)

* `us` (value: `"us"`)

* `uy` (value: `"uy"`)

* `uz` (value: `"uz"`)

* `va` (value: `"va"`)

* `vc` (value: `"vc"`)

* `ve` (value: `"ve"`)

* `vg` (value: `"vg"`)

* `vi` (value: `"vi"`)

* `vn` (value: `"vn"`)

* `vu` (value: `"vu"`)

* `wf` (value: `"wf"`)

* `ws` (value: `"ws"`)

* `ye` (value: `"ye"`)

* `yt` (value: `"yt"`)

* `za` (value: `"za"`)

* `zm` (value: `"zm"`)

* `zw` (value: `"zw"`)





## Enum: RegionEnum


* `DF` (value: `"DF"`)

* `AC` (value: `"AC"`)

* `AL` (value: `"AL"`)

* `AP` (value: `"AP"`)

* `AM` (value: `"AM"`)

* `BA` (value: `"BA"`)

* `CE` (value: `"CE"`)

* `ES` (value: `"ES"`)

* `GO` (value: `"GO"`)

* `MA` (value: `"MA"`)

* `MT` (value: `"MT"`)

* `MS` (value: `"MS"`)

* `MG` (value: `"MG"`)

* `PA` (value: `"PA"`)

* `PB` (value: `"PB"`)

* `PR` (value: `"PR"`)

* `PE` (value: `"PE"`)

* `PI` (value: `"PI"`)

* `RJ` (value: `"RJ"`)

* `RN` (value: `"RN"`)

* `RS` (value: `"RS"`)

* `RO` (value: `"RO"`)

* `RR` (value: `"RR"`)

* `SC` (value: `"SC"`)

* `SP` (value: `"SP"`)

* `SE` (value: `"SE"`)

* `TO` (value: `"TO"`)





## Enum: StatusEnum


* `not_started` (value: `"not_started"`)

* `in_progress` (value: `"in_progress"`)

* `completed` (value: `"completed"`)

* `error` (value: `"error"`)

* `delayed` (value: `"delayed"`)





## Enum: TypeEnum


* `company` (value: `"company"`)

* `person` (value: `"person"`)

* `vehicle` (value: `"vehicle"`)




