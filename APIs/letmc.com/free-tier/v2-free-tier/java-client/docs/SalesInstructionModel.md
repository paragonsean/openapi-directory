

# SalesInstructionModel



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address1** | **String** | Address 1 of the property to be sold |  [optional] |
|**address2** | **String** | Address 2 of the property to be sold |  [optional] |
|**address3** | **String** | Address 3 of the property to be sold |  [optional] |
|**address4** | **String** | Address 4 of the property to be sold |  [optional] |
|**addressNumber** | **String** | Address number of the property to be sold |  [optional] |
|**area** | **String** | The area linked to the instruction |  [optional] |
|**bathrooms** | **Integer** | Number of bathrooms linked to the instruction |  [optional] |
|**bathroomsEnsuite** | **Integer** | How many of the bathrooms are ensuite? |  [optional] |
|**bedrooms** | **Integer** | Number of bedrooms linked to the instruction |  [optional] |
|**contractType** | [**ContractTypeEnum**](#ContractTypeEnum) | The contract type |  [optional] |
|**country** | [**CountryEnum**](#CountryEnum) | Address country of the property to be sold |  [optional] |
|**description** | **String** | The instruction description |  [optional] |
|**developmentOpp** | **Boolean** | Is the instruction a development opportunity? |  [optional] |
|**directions** | **String** | Directions linked to the instruction |  [optional] |
|**epCCurrentEER** | **Integer** | Current EER value |  [optional] |
|**epCCurrentEI** | **Integer** | Current EI value |  [optional] |
|**epCPotentialEER** | **Integer** | Potential EER value |  [optional] |
|**epCPotentialEI** | **Integer** | Potential EI value |  [optional] |
|**etag** | **String** | A unique identifier defining the object and change revision. |  [optional] |
|**hasElectricitySupply** | **Boolean** | Does the instruction have an electrical supply linked to it? |  [optional] |
|**hasGasSupply** | **Boolean** | Does the instruction have an gas supply linked to it? |  [optional] |
|**hasWaterMeter** | **Boolean** | Does the instruction have a water meter linked to it? |  [optional] |
|**investmentOpp** | **Boolean** | Is the instruction a investment opportunity? |  [optional] |
|**kitchens** | **Integer** | Number of kitchens linked to the property instruction |  [optional] |
|**OID** | **String** | The unique Object ID (OID). |  [optional] |
|**outsideSpaceBalcony** | **Boolean** | Does the instruction have an outside balcony linked to it? |  [optional] |
|**outsideSpaceCommunalGarden** | **Boolean** | Does the instruction have a communal garden linked to it? |  [optional] |
|**outsideSpaceConservatory** | **Boolean** | Does the instruction have a conservatory linked to it? |  [optional] |
|**outsideSpaceGarden** | **Boolean** | Does the instruction have a garden linked to it? |  [optional] |
|**outsideSpaceLargeGarden** | **Boolean** | Does the instruction have a large garden linked to it? |  [optional] |
|**outsideSpacePatio** | **Boolean** | Does the instruction have a patio linked to it? |  [optional] |
|**outsideSpaceRoofTerrace** | **Boolean** | Does the instruction have a roof terrace linked to it? |  [optional] |
|**outsideSpaceSouthFacingGarden** | **Boolean** | Does the instruction have a south facing garden? |  [optional] |
|**parkingAllocated** | **Boolean** | Is there any parking allocation linked to the instruction? |  [optional] |
|**parkingCarport** | **Boolean** | Does the instruction have a carport linked to it? |  [optional] |
|**parkingDoubleGarage** | **Boolean** | Does the instruction have a double garage linked to it? |  [optional] |
|**parkingGarage** | **Boolean** | Does the instruction have a garage linked to it? |  [optional] |
|**parkingOffRoad** | **Boolean** | Is there off road parking linked to the instruction? |  [optional] |
|**parkingOnRoad** | **Boolean** | Is there on road parking linked to the instruction? |  [optional] |
|**parkingPermit** | **Boolean** | Is a parking permit required? |  [optional] |
|**parkingSecureGated** | **Boolean** | Is there any secured gate parking linked to the instruction? |  [optional] |
|**parkingTripleGarage** | **Boolean** | Does the instruction have a triple garage linked to it? |  [optional] |
|**postcode** | **String** | Postcode of the property to be sold |  [optional] |
|**price** | **Double** | The price of the property to be sold |  [optional] |
|**propertyOwnableType** | [**PropertyOwnableTypeEnum**](#PropertyOwnableTypeEnum) | The property type |  [optional] |
|**receptionRooms** | **Integer** | Number of reception rooms linked to the instruction |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current instruction state |  [optional] |
|**tenure** | [**TenureEnum**](#TenureEnum) | Instruction tenure |  [optional] |
|**videoURL** | **String** | The URL of the video linked to the Sales Instruction |  [optional] |



## Enum: ContractTypeEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;Pending&quot; |
| SOLE_AGENCY | &quot;SoleAgency&quot; |
| SOLE_SELLING_RIGHTS | &quot;SoleSellingRights&quot; |
| JOINT_SOLE_AGENCY | &quot;JointSoleAgency&quot; |
| MULTI_AGENCY | &quot;MultiAgency&quot; |
| SUB_AGENT | &quot;SubAgent&quot; |



## Enum: CountryEnum

| Name | Value |
|---- | -----|
| AFGHANISTAN | &quot;Afghanistan&quot; |
| ALBANIA | &quot;Albania&quot; |
| ALGERIA | &quot;Algeria&quot; |
| ANDORRA | &quot;Andorra&quot; |
| ANGOLA | &quot;Angola&quot; |
| ANTIGUA_AND_BARBUDA | &quot;AntiguaAndBarbuda&quot; |
| ARGENTINA | &quot;Argentina&quot; |
| ARMENIA | &quot;Armenia&quot; |
| AUSTRALIA | &quot;Australia&quot; |
| AUSTRIA | &quot;Austria&quot; |
| AZERBAIJAN | &quot;Azerbaijan&quot; |
| BAHAMAS | &quot;Bahamas&quot; |
| BAHRAIN | &quot;Bahrain&quot; |
| BANGLADESH | &quot;Bangladesh&quot; |
| BARBADOS | &quot;Barbados&quot; |
| BELARUS | &quot;Belarus&quot; |
| BELGIUM | &quot;Belgium&quot; |
| BELIZE | &quot;Belize&quot; |
| BENIN | &quot;Benin&quot; |
| BHUTAN | &quot;Bhutan&quot; |
| BOLIVIA | &quot;Bolivia&quot; |
| BOSNIA_AND_HERZEGOVINA | &quot;BosniaAndHerzegovina&quot; |
| BOTSWANA | &quot;Botswana&quot; |
| BRAZIL | &quot;Brazil&quot; |
| BRUNEI | &quot;Brunei&quot; |
| BULGARIA | &quot;Bulgaria&quot; |
| BURKINA_FASO | &quot;BurkinaFaso&quot; |
| BURUNDI | &quot;Burundi&quot; |
| CAMBODIA | &quot;Cambodia&quot; |
| CAMEROON | &quot;Cameroon&quot; |
| CANADA | &quot;Canada&quot; |
| CAPE_VERDE | &quot;CapeVerde&quot; |
| CENTRAL_AFRICAN_REPUBLIC | &quot;CentralAfricanRepublic&quot; |
| CHAD | &quot;Chad&quot; |
| CHILE | &quot;Chile&quot; |
| CHINA | &quot;China&quot; |
| COLOMBIA | &quot;Colombia&quot; |
| COMOROS | &quot;Comoros&quot; |
| CONGO_BRAZZAVILLE | &quot;CongoBrazzaville&quot; |
| CONGO_DEMOCRATIC_REPUBLIC_OF_THE | &quot;CongoDemocraticRepublicOfThe&quot; |
| COSTA_RICA | &quot;CostaRica&quot; |
| COTE_D_IVOIRE | &quot;CoteDIvoire&quot; |
| CROATIA | &quot;Croatia&quot; |
| CUBA | &quot;Cuba&quot; |
| CYPRUS | &quot;Cyprus&quot; |
| CZECH_REPUBLIC | &quot;CzechRepublic&quot; |
| DENMARK | &quot;Denmark&quot; |
| DJIBOUTI | &quot;Djibouti&quot; |
| DOMINICA | &quot;Dominica&quot; |
| DOMINICAN_REPUBLIC | &quot;DominicanRepublic&quot; |
| EAST_TIMOR_TIMOR_TIMUR | &quot;EastTimorTimorTimur&quot; |
| ECUADOR | &quot;Ecuador&quot; |
| EGYPT | &quot;Egypt&quot; |
| EL_SALVADOR | &quot;ElSalvador&quot; |
| EQUATORIAL_GUINEA | &quot;EquatorialGuinea&quot; |
| ERITREA | &quot;Eritrea&quot; |
| ESTONIA | &quot;Estonia&quot; |
| ETHIOPIA | &quot;Ethiopia&quot; |
| FIJI | &quot;Fiji&quot; |
| FINLAND | &quot;Finland&quot; |
| FRANCE | &quot;France&quot; |
| GABON | &quot;Gabon&quot; |
| GAMBIA_THE | &quot;GambiaThe&quot; |
| GEORGIA | &quot;Georgia&quot; |
| GERMANY | &quot;Germany&quot; |
| GHANA | &quot;Ghana&quot; |
| GREECE | &quot;Greece&quot; |
| GRENADA | &quot;Grenada&quot; |
| GUATEMALA | &quot;Guatemala&quot; |
| GUINEA | &quot;Guinea&quot; |
| GUINEA_BISSAU | &quot;GuineaBissau&quot; |
| GUYANA | &quot;Guyana&quot; |
| HAITI | &quot;Haiti&quot; |
| HONDURAS | &quot;Honduras&quot; |
| HUNGARY | &quot;Hungary&quot; |
| ICELAND | &quot;Iceland&quot; |
| INDIA | &quot;India&quot; |
| INDONESIA | &quot;Indonesia&quot; |
| IRAN | &quot;Iran&quot; |
| IRAQ | &quot;Iraq&quot; |
| IRELAND | &quot;Ireland&quot; |
| ISRAEL | &quot;Israel&quot; |
| ITALY | &quot;Italy&quot; |
| JAMAICA | &quot;Jamaica&quot; |
| JAPAN | &quot;Japan&quot; |
| JORDAN | &quot;Jordan&quot; |
| KAZAKHSTAN | &quot;Kazakhstan&quot; |
| KENYA | &quot;Kenya&quot; |
| KIRIBATI | &quot;Kiribati&quot; |
| KOREA_NORTH | &quot;KoreaNorth&quot; |
| KOREA_SOUTH | &quot;KoreaSouth&quot; |
| KUWAIT | &quot;Kuwait&quot; |
| KYRGYZSTAN | &quot;Kyrgyzstan&quot; |
| LAOS | &quot;Laos&quot; |
| LATVIA | &quot;Latvia&quot; |
| LEBANON | &quot;Lebanon&quot; |
| LESOTHO | &quot;Lesotho&quot; |
| LIBERIA | &quot;Liberia&quot; |
| LIBYA | &quot;Libya&quot; |
| LIECHTENSTEIN | &quot;Liechtenstein&quot; |
| LITHUANIA | &quot;Lithuania&quot; |
| LUXEMBOURG | &quot;Luxembourg&quot; |
| MACEDONIA_FORMER_YUGOSLAV_REPUBLIC_OF | &quot;MacedoniaFormerYugoslavRepublicOf&quot; |
| MADAGASCAR | &quot;Madagascar&quot; |
| MALAWI | &quot;Malawi&quot; |
| MALAYSIA | &quot;Malaysia&quot; |
| MALDIVES | &quot;Maldives&quot; |
| MALI | &quot;Mali&quot; |
| MALTA | &quot;Malta&quot; |
| MARSHALL_ISLANDS | &quot;MarshallIslands&quot; |
| MAURITANIA | &quot;Mauritania&quot; |
| MAURITIUS | &quot;Mauritius&quot; |
| MEXICO | &quot;Mexico&quot; |
| MICRONESIA_FEDERATED_STATES_OF | &quot;MicronesiaFederatedStatesOf&quot; |
| MOLDOVA | &quot;Moldova&quot; |
| MONACO | &quot;Monaco&quot; |
| MONGOLIA | &quot;Mongolia&quot; |
| MOROCCO | &quot;Morocco&quot; |
| MOZAMBIQUE | &quot;Mozambique&quot; |
| MYANMAR | &quot;Myanmar&quot; |
| NAMIBIA | &quot;Namibia&quot; |
| NAURU | &quot;Nauru&quot; |
| NEPAL | &quot;Nepal&quot; |
| NETHERLANDS | &quot;Netherlands&quot; |
| NEW_ZEALAND | &quot;NewZealand&quot; |
| NICARAGUA | &quot;Nicaragua&quot; |
| NIGER | &quot;Niger&quot; |
| NIGERIA | &quot;Nigeria&quot; |
| NORWAY | &quot;Norway&quot; |
| OMAN | &quot;Oman&quot; |
| PAKISTAN | &quot;Pakistan&quot; |
| PALAU | &quot;Palau&quot; |
| PANAMA | &quot;Panama&quot; |
| PAPUA_NEW_GUINEA | &quot;PapuaNewGuinea&quot; |
| PARAGUAY | &quot;Paraguay&quot; |
| PERU | &quot;Peru&quot; |
| PHILIPPINES | &quot;Philippines&quot; |
| POLAND | &quot;Poland&quot; |
| PORTUGAL | &quot;Portugal&quot; |
| QATAR | &quot;Qatar&quot; |
| ROMANIA | &quot;Romania&quot; |
| RUSSIA | &quot;Russia&quot; |
| RWANDA | &quot;Rwanda&quot; |
| SAINT_KITTS_AND_NEVIS | &quot;SaintKittsAndNevis&quot; |
| SAINT_LUCIA | &quot;SaintLucia&quot; |
| SAINT_VINCENT_AND_THE_GRENADINES | &quot;SaintVincentAndTheGrenadines&quot; |
| SAMOA | &quot;Samoa&quot; |
| SAN_MARINO | &quot;SanMarino&quot; |
| SAO_TOME_AND_PRINCIPE | &quot;SaoTomeAndPrincipe&quot; |
| SAUDI_ARABIA | &quot;SaudiArabia&quot; |
| SENEGAL | &quot;Senegal&quot; |
| SERBIA_AND_MONTENEGRO | &quot;SerbiaAndMontenegro&quot; |
| SEYCHELLES | &quot;Seychelles&quot; |
| SIERRA_LEONE | &quot;SierraLeone&quot; |
| SINGAPORE | &quot;Singapore&quot; |
| SLOVAKIA | &quot;Slovakia&quot; |
| SLOVENIA | &quot;Slovenia&quot; |
| SOLOMON_ISLANDS | &quot;SolomonIslands&quot; |
| SOMALIA | &quot;Somalia&quot; |
| SOUTH_AFRICA | &quot;SouthAfrica&quot; |
| SPAIN | &quot;Spain&quot; |
| SRI_LANKA | &quot;SriLanka&quot; |
| SUDAN | &quot;Sudan&quot; |
| SURINAME | &quot;Suriname&quot; |
| SWAZILAND | &quot;Swaziland&quot; |
| SWEDEN | &quot;Sweden&quot; |
| SWITZERLAND | &quot;Switzerland&quot; |
| SYRIA | &quot;Syria&quot; |
| TAIWAN | &quot;Taiwan&quot; |
| TAJIKISTAN | &quot;Tajikistan&quot; |
| TANZANIA | &quot;Tanzania&quot; |
| THAILAND | &quot;Thailand&quot; |
| TOGO | &quot;Togo&quot; |
| TONGA | &quot;Tonga&quot; |
| TRINIDAD_AND_TOBAGO | &quot;TrinidadAndTobago&quot; |
| TUNISIA | &quot;Tunisia&quot; |
| TURKEY | &quot;Turkey&quot; |
| TURKMENISTAN | &quot;Turkmenistan&quot; |
| TUVALU | &quot;Tuvalu&quot; |
| UGANDA | &quot;Uganda&quot; |
| UKRAINE | &quot;Ukraine&quot; |
| UNITED_ARAB_EMIRATES | &quot;UnitedArabEmirates&quot; |
| UNITED_KINGDOM | &quot;UnitedKingdom&quot; |
| UNITED_STATES | &quot;UnitedStates&quot; |
| URUGUAY | &quot;Uruguay&quot; |
| UZBEKISTAN | &quot;Uzbekistan&quot; |
| VANUATU | &quot;Vanuatu&quot; |
| VATICAN_CITY | &quot;VaticanCity&quot; |
| VENEZUELA | &quot;Venezuela&quot; |
| VIETNAM | &quot;Vietnam&quot; |
| WESTERN_SAHARA | &quot;WesternSahara&quot; |
| YEMEN | &quot;Yemen&quot; |
| ZAMBIA | &quot;Zambia&quot; |
| ZIMBABWE | &quot;Zimbabwe&quot; |
| UNKNOWN_COUNTRY | &quot;UnknownCountry&quot; |
| HONG_KONG | &quot;HongKong&quot; |
| JERSEY | &quot;Jersey&quot; |
| CHANNEL_ISLANDS | &quot;ChannelIslands&quot; |
| BERMUDA | &quot;Bermuda&quot; |
| BRITISH_OVERSEAS_TERRITORY | &quot;BritishOverseasTerritory&quot; |



## Enum: PropertyOwnableTypeEnum

| Name | Value |
|---- | -----|
| HOUSE | &quot;House&quot; |
| FLAT_APARTMENT | &quot;FlatApartment&quot; |
| BUNGALOW | &quot;Bungalow&quot; |
| LAND | &quot;Land&quot; |
| HOUSE_FLAT_SHARE | &quot;HouseFlatShare&quot; |
| GARAGE_PARKING | &quot;GarageParking&quot; |
| COMMERCIAL_PROPERTY | &quot;CommercialProperty&quot; |
| BLOCK | &quot;Block&quot; |
| TERRACED_HOUSE | &quot;TerracedHouse&quot; |
| END_TERRACE_HOUSE | &quot;EndTerraceHouse&quot; |
| SEMI_DETACHED_HOUSE | &quot;SemiDetachedHouse&quot; |
| DETACHED_HOUSE | &quot;DetachedHouse&quot; |
| SEMI_DETACHED_BUNGALOW | &quot;SemiDetachedBungalow&quot; |
| TOWN_HOUSE | &quot;TownHouse&quot; |
| COTTAGE | &quot;Cottage&quot; |
| SERVICED_APARTMENT | &quot;ServicedApartment&quot; |
| STUDIO | &quot;Studio&quot; |
| APARTMENT | &quot;Apartment&quot; |
| BARN | &quot;Barn&quot; |
| FARM_HOUSE | &quot;FarmHouse&quot; |
| PENTHOUSE | &quot;Penthouse&quot; |
| BUILDING_PLOT | &quot;BuildingPlot&quot; |
| DETACHED_BUNGALOW | &quot;DetachedBungalow&quot; |
| LINK_DETACHED | &quot;LinkDetached&quot; |
| MID_TERRACED_BUNGALOW | &quot;MidTerracedBungalow&quot; |
| LAND_RESIDENTIAL | &quot;LandResidential&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| MARKET_APPRAISAL | &quot;MarketAppraisal&quot; |
| LOST_APPRAISAL | &quot;LostAppraisal&quot; |
| INSTRUCTED | &quot;Instructed&quot; |
| ADVERTISED | &quot;Advertised&quot; |
| UNDER_OFFER | &quot;UnderOffer&quot; |
| CONTRACTS_EXCHANGED | &quot;ContractsExchanged&quot; |
| COMPLETED | &quot;Completed&quot; |
| FALLEN_THROUGH | &quot;FallenThrough&quot; |
| WITHDRAWN | &quot;Withdrawn&quot; |



## Enum: TenureEnum

| Name | Value |
|---- | -----|
| FREEHOLD | &quot;Freehold&quot; |
| LEASEHOLD | &quot;Leasehold&quot; |
| COMMONHOLD | &quot;Commonhold&quot; |
| SHARE_OF_FREEHOLD | &quot;ShareOfFreehold&quot; |
| FLYING_FREEHOLD | &quot;FlyingFreehold&quot; |
| SHARE_TRANSFER | &quot;ShareTransfer&quot; |
| UNKNOWN | &quot;Unknown&quot; |



