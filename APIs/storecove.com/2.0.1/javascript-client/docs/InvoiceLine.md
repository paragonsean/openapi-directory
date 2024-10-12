# StorecoveApi.InvoiceLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountingCost** | **String** | The buyer&#39;s accounting cost centre for this invoice line, expressed as text. | [optional] 
**additionalItemProperties** | [**[AdditionalItemProperty]**](AdditionalItemProperty.md) | An array of additional item properties. | [optional] 
**allowanceCharge** | **Number** | The discount or surcharge on this item. Should be negative for discounts | [optional] 
**allowanceCharges** | [**[LineAllowanceCharge]**](LineAllowanceCharge.md) | An array of allowance charges. NOTE: this is currently supported only when sending from/to Italy. | [optional] 
**amountExcludingTax** | **Number** | The amount excluding tax. EXPERIMENTAL. Use amountExcludingVat. | [optional] 
**amountExcludingVat** | **Number** | The amount excluding VAT. Should equal quantity x itemPrice + allowanceCharge. | [optional] 
**amountIncludingTax** | **Number** | The amount including tax. Can only be used for \&quot;priceMode\&quot;: \&quot;price_mode_gross\&quot;. Use either this property or amountExcludingTax (amountExcludingVat). | [optional] 
**buyersItemIdentification** | **String** | DEPRECATED. Use the references array with &#39;line_buyers_item_identification&#39; documentType. The ID the buyer assigned to this item. | [optional] 
**description** | **String** | The description for this invoice line. | [optional] 
**invoicePeriod** | **String** | The period (or specific date) to which the invoice line applies. Format: yyyy-mm-dd - yyyy-mm-dd. | [optional] 
**itemPrice** | **Number** | The price per item (may be fractional) | [optional] [default to 1]
**lineId** | **String** | The id for this invoice line. | [optional] 
**name** | **String** | A short name for this invoice line. If not provided, it will be taken from description and description will be set to an emtpy string. | [optional] 
**note** | **String** | A note to add to the document line | [optional] 
**orderLineReferenceLineId** | **String** | A reference to the LineID of the order. The order itself is specified as the orderReference at the invoice level. It is not possible to specify an orderReference at the invoice line level. An invoice MUST at this time be for a single order only. | [optional] 
**quantity** | **Number** | The number of items (may be fractional). | [optional] [default to 1]
**quantityUnitCode** | **String** | The unit of measure that applies to the invoiced quantity. Codes for unit of packaging from UNECE Recommendation No. 21 can be used in accordance with the descriptions in the \&quot;Intro\&quot; section of UN/ECE Recommendation 20, Revision 11 (2015): The 2 character alphanumeric code values in UNECE Recommendation 21 shall be used. To avoid duplication with existing code values in UNECE Recommendation No. 20, each code value from UNECE Recommendation 21 shall be prefixed with an “X”, resulting in a 3 alphanumeric code when used as a unit of measure. Note that the following additionally allowed codes are deprecated and will be converted to C62: 04, 05, 08, 16, 17, 18, 19, 26, 29, 30, 31, 32, 36, 43, 44, 45, 46, 47, 48, 53, 54, 62, 63, 64, 66, 69, 71, 72, 73, 76, 78, 84, 90, 92, 93, 94, 95, 96, 97, 98, 1A, 1B, 1C, 1D, 1E, 1F, 1G, 1H, 1J, 1K, 1L, 1M, 1X, 2V, 2W, 3E, 3G, 3H, 3I, 4A, 4B, 4E, 5C, 5F, 5G, 5H, 5I, 5K, 5P, 5Q, A1, A25, A50, A51, A52, A57, A58, A60, A61, A62, A63, A64, A65, A66, A67, A77, A78, A79, A80, A81, A82, A83, AJ, AM, AP, AR, ARE, ATT, AV, AW, B0, B2, B36, B37, B38, B39, B40, B5, B51, B6, B65, B9, BD, BE, BG, BH, BJ, BK, BL, BO, BR, BT, BW, BX, BZ, C1, C2, C4, C5, C6, C77, C98, CA, CH, CJ, CK, CL, CO, CQ, CR, CS, CT, CU, CV, CY, CZ, D14, D28, D35, D37, D38, D39, D40, D64, D66, D67, D7, D70, D71, D72, D75, D76, D79, D8, D9, D90, D92, D96, D97, D98, D99, DC, DE, DI, DQ, DR, DRM, DS, DU, DX, DY, E2, E3, E5, EC, EP, EV, F1, F9, FB, FD, FE, FG, FM, G7, GC, GD, GH, GK, GN, GRT, GT, GW, GY, GZ, H1, H2, HAR, HD, HE, HF, HI, HJ, HK, HL, HN, HO, HP, HS, HT, HY, IC, IF, II, IL, IM, IP, IT, JB, JG, JO, JR, K5, KD, KF, KG, KS, KTM, LC, LE, LI, LJ, LX, M0, MA, MF, MK, MQ, MT, MV, N2, NB, NBB, NC, ND, NE, NG, NH, NI, NJ, NN, NPL, NPR, NQ, NR, NRL, NTT, NV, NY, OP, OZ, P0, P3, P4, P6, P7, P8, P9, PA, PB, PE, PF, PG, PK, PL, PM, PN, PT, PU, PV, PW, PY, PZ, QD, QH, QK, QT, R4, RA, RD, RG, RK, RL, RN, RO, RS, RU, S5, S6, S7, S8, SA, SD, SE, SHT, SK, SL, SN, SO, SP, SS, SST, ST, SV, T1, T4, T5, T6, T7, T8, TA, TC, TD, TE, TF, TJ, TK, TL, TN, TQ, TR, TS, TSD, TSH, TT, TU, TV, TW, TY, UA, UD, UE, UF, UH, UM, VI, VQ, VS, W4, WH, WI, WR, WW, YL, YT, Z1, Z2, Z3, Z4, Z5, Z6, Z8 | [optional] [default to &#39;C62&#39;]
**references** | [**[Reference]**](Reference.md) | An array of references to other documents or codes. Note that many syntaxes do not support multiple references of the same type in which case they will be concatenated with &#39;,&#39;. Also, not all syntaxes support all documentTypes. | [optional] 
**sellersItemIdentification** | **String** | DEPRECATED. Use the references array with &#39;line_sellers_item_identification&#39; documentType. The ID the seller assigned to this item. | [optional] 
**standardItemIdentification** | **String** | Standardized ID for the item. | [optional] 
**standardItemIdentificationSchemeAgencyId** | **String** | DEPRECATED. Use the references array with &#39;line_standard_item_identification&#39; documentType. The scheme agency for the standardized ID for the item. | [optional] [default to &#39;9&#39;]
**standardItemIdentificationSchemeId** | **String** | DEPRECATED. Use the references array with &#39;line_standard_item_identification&#39; documentType. The scheme for the standardized ID for the item. | [optional] [default to &#39;GTIN&#39;]
**tax** | [**Tax**](Tax.md) |  | [optional] 
**taxesDutiesFees** | [**[Tax]**](Tax.md) | An array of taxes, duties and fees for this invoice line. Multiple taxesDutiesFees items is allowed only for IN (India) and US (USA) taxes. All other countries can only have a single Tax item in this array. | [optional] 



## Enum: QuantityUnitCodeEnum


* `10` (value: `"10"`)

* `11` (value: `"11"`)

* `13` (value: `"13"`)

* `14` (value: `"14"`)

* `15` (value: `"15"`)

* `20` (value: `"20"`)

* `21` (value: `"21"`)

* `22` (value: `"22"`)

* `23` (value: `"23"`)

* `24` (value: `"24"`)

* `25` (value: `"25"`)

* `27` (value: `"27"`)

* `28` (value: `"28"`)

* `33` (value: `"33"`)

* `34` (value: `"34"`)

* `35` (value: `"35"`)

* `37` (value: `"37"`)

* `38` (value: `"38"`)

* `40` (value: `"40"`)

* `41` (value: `"41"`)

* `56` (value: `"56"`)

* `57` (value: `"57"`)

* `58` (value: `"58"`)

* `59` (value: `"59"`)

* `60` (value: `"60"`)

* `61` (value: `"61"`)

* `74` (value: `"74"`)

* `77` (value: `"77"`)

* `80` (value: `"80"`)

* `81` (value: `"81"`)

* `85` (value: `"85"`)

* `87` (value: `"87"`)

* `89` (value: `"89"`)

* `91` (value: `"91"`)

* `1I` (value: `"1I"`)

* `2A` (value: `"2A"`)

* `2B` (value: `"2B"`)

* `2C` (value: `"2C"`)

* `2G` (value: `"2G"`)

* `2H` (value: `"2H"`)

* `2I` (value: `"2I"`)

* `2J` (value: `"2J"`)

* `2K` (value: `"2K"`)

* `2L` (value: `"2L"`)

* `2M` (value: `"2M"`)

* `2N` (value: `"2N"`)

* `2P` (value: `"2P"`)

* `2Q` (value: `"2Q"`)

* `2R` (value: `"2R"`)

* `2U` (value: `"2U"`)

* `2X` (value: `"2X"`)

* `2Y` (value: `"2Y"`)

* `2Z` (value: `"2Z"`)

* `3B` (value: `"3B"`)

* `3C` (value: `"3C"`)

* `4C` (value: `"4C"`)

* `4G` (value: `"4G"`)

* `4H` (value: `"4H"`)

* `4K` (value: `"4K"`)

* `4L` (value: `"4L"`)

* `4M` (value: `"4M"`)

* `4N` (value: `"4N"`)

* `4O` (value: `"4O"`)

* `4P` (value: `"4P"`)

* `4Q` (value: `"4Q"`)

* `4R` (value: `"4R"`)

* `4T` (value: `"4T"`)

* `4U` (value: `"4U"`)

* `4W` (value: `"4W"`)

* `4X` (value: `"4X"`)

* `5A` (value: `"5A"`)

* `5B` (value: `"5B"`)

* `5E` (value: `"5E"`)

* `5J` (value: `"5J"`)

* `A10` (value: `"A10"`)

* `A11` (value: `"A11"`)

* `A12` (value: `"A12"`)

* `A13` (value: `"A13"`)

* `A14` (value: `"A14"`)

* `A15` (value: `"A15"`)

* `A16` (value: `"A16"`)

* `A17` (value: `"A17"`)

* `A18` (value: `"A18"`)

* `A19` (value: `"A19"`)

* `A2` (value: `"A2"`)

* `A20` (value: `"A20"`)

* `A21` (value: `"A21"`)

* `A22` (value: `"A22"`)

* `A23` (value: `"A23"`)

* `A24` (value: `"A24"`)

* `A26` (value: `"A26"`)

* `A27` (value: `"A27"`)

* `A28` (value: `"A28"`)

* `A29` (value: `"A29"`)

* `A3` (value: `"A3"`)

* `A30` (value: `"A30"`)

* `A31` (value: `"A31"`)

* `A32` (value: `"A32"`)

* `A33` (value: `"A33"`)

* `A34` (value: `"A34"`)

* `A35` (value: `"A35"`)

* `A36` (value: `"A36"`)

* `A37` (value: `"A37"`)

* `A38` (value: `"A38"`)

* `A39` (value: `"A39"`)

* `A4` (value: `"A4"`)

* `A40` (value: `"A40"`)

* `A41` (value: `"A41"`)

* `A42` (value: `"A42"`)

* `A43` (value: `"A43"`)

* `A44` (value: `"A44"`)

* `A45` (value: `"A45"`)

* `A47` (value: `"A47"`)

* `A48` (value: `"A48"`)

* `A49` (value: `"A49"`)

* `A5` (value: `"A5"`)

* `A53` (value: `"A53"`)

* `A54` (value: `"A54"`)

* `A55` (value: `"A55"`)

* `A56` (value: `"A56"`)

* `A59` (value: `"A59"`)

* `A6` (value: `"A6"`)

* `A68` (value: `"A68"`)

* `A69` (value: `"A69"`)

* `A7` (value: `"A7"`)

* `A70` (value: `"A70"`)

* `A71` (value: `"A71"`)

* `A73` (value: `"A73"`)

* `A74` (value: `"A74"`)

* `A75` (value: `"A75"`)

* `A76` (value: `"A76"`)

* `A8` (value: `"A8"`)

* `A84` (value: `"A84"`)

* `A85` (value: `"A85"`)

* `A86` (value: `"A86"`)

* `A87` (value: `"A87"`)

* `A88` (value: `"A88"`)

* `A89` (value: `"A89"`)

* `A9` (value: `"A9"`)

* `A90` (value: `"A90"`)

* `A91` (value: `"A91"`)

* `A93` (value: `"A93"`)

* `A94` (value: `"A94"`)

* `A95` (value: `"A95"`)

* `A96` (value: `"A96"`)

* `A97` (value: `"A97"`)

* `A98` (value: `"A98"`)

* `A99` (value: `"A99"`)

* `AA` (value: `"AA"`)

* `AB` (value: `"AB"`)

* `ACR` (value: `"ACR"`)

* `ACT` (value: `"ACT"`)

* `AD` (value: `"AD"`)

* `AE` (value: `"AE"`)

* `AH` (value: `"AH"`)

* `AI` (value: `"AI"`)

* `AK` (value: `"AK"`)

* `AL` (value: `"AL"`)

* `AMH` (value: `"AMH"`)

* `AMP` (value: `"AMP"`)

* `ANN` (value: `"ANN"`)

* `APZ` (value: `"APZ"`)

* `AQ` (value: `"AQ"`)

* `AS` (value: `"AS"`)

* `ASM` (value: `"ASM"`)

* `ASU` (value: `"ASU"`)

* `ATM` (value: `"ATM"`)

* `AWG` (value: `"AWG"`)

* `AY` (value: `"AY"`)

* `AZ` (value: `"AZ"`)

* `B1` (value: `"B1"`)

* `B10` (value: `"B10"`)

* `B11` (value: `"B11"`)

* `B12` (value: `"B12"`)

* `B13` (value: `"B13"`)

* `B14` (value: `"B14"`)

* `B15` (value: `"B15"`)

* `B16` (value: `"B16"`)

* `B17` (value: `"B17"`)

* `B18` (value: `"B18"`)

* `B19` (value: `"B19"`)

* `B20` (value: `"B20"`)

* `B21` (value: `"B21"`)

* `B22` (value: `"B22"`)

* `B23` (value: `"B23"`)

* `B24` (value: `"B24"`)

* `B25` (value: `"B25"`)

* `B26` (value: `"B26"`)

* `B27` (value: `"B27"`)

* `B28` (value: `"B28"`)

* `B29` (value: `"B29"`)

* `B3` (value: `"B3"`)

* `B30` (value: `"B30"`)

* `B31` (value: `"B31"`)

* `B32` (value: `"B32"`)

* `B33` (value: `"B33"`)

* `B34` (value: `"B34"`)

* `B35` (value: `"B35"`)

* `B4` (value: `"B4"`)

* `B41` (value: `"B41"`)

* `B42` (value: `"B42"`)

* `B43` (value: `"B43"`)

* `B44` (value: `"B44"`)

* `B45` (value: `"B45"`)

* `B46` (value: `"B46"`)

* `B47` (value: `"B47"`)

* `B48` (value: `"B48"`)

* `B49` (value: `"B49"`)

* `B50` (value: `"B50"`)

* `B52` (value: `"B52"`)

* `B53` (value: `"B53"`)

* `B54` (value: `"B54"`)

* `B55` (value: `"B55"`)

* `B56` (value: `"B56"`)

* `B57` (value: `"B57"`)

* `B58` (value: `"B58"`)

* `B59` (value: `"B59"`)

* `B60` (value: `"B60"`)

* `B61` (value: `"B61"`)

* `B62` (value: `"B62"`)

* `B63` (value: `"B63"`)

* `B64` (value: `"B64"`)

* `B66` (value: `"B66"`)

* `B67` (value: `"B67"`)

* `B68` (value: `"B68"`)

* `B69` (value: `"B69"`)

* `B7` (value: `"B7"`)

* `B70` (value: `"B70"`)

* `B71` (value: `"B71"`)

* `B72` (value: `"B72"`)

* `B73` (value: `"B73"`)

* `B74` (value: `"B74"`)

* `B75` (value: `"B75"`)

* `B76` (value: `"B76"`)

* `B77` (value: `"B77"`)

* `B78` (value: `"B78"`)

* `B79` (value: `"B79"`)

* `B8` (value: `"B8"`)

* `B80` (value: `"B80"`)

* `B81` (value: `"B81"`)

* `B82` (value: `"B82"`)

* `B83` (value: `"B83"`)

* `B84` (value: `"B84"`)

* `B85` (value: `"B85"`)

* `B86` (value: `"B86"`)

* `B87` (value: `"B87"`)

* `B88` (value: `"B88"`)

* `B89` (value: `"B89"`)

* `B90` (value: `"B90"`)

* `B91` (value: `"B91"`)

* `B92` (value: `"B92"`)

* `B93` (value: `"B93"`)

* `B94` (value: `"B94"`)

* `B95` (value: `"B95"`)

* `B96` (value: `"B96"`)

* `B97` (value: `"B97"`)

* `B98` (value: `"B98"`)

* `B99` (value: `"B99"`)

* `BAR` (value: `"BAR"`)

* `BB` (value: `"BB"`)

* `BFT` (value: `"BFT"`)

* `BHP` (value: `"BHP"`)

* `BIL` (value: `"BIL"`)

* `BLD` (value: `"BLD"`)

* `BLL` (value: `"BLL"`)

* `BP` (value: `"BP"`)

* `BPM` (value: `"BPM"`)

* `BQL` (value: `"BQL"`)

* `BTU` (value: `"BTU"`)

* `BUA` (value: `"BUA"`)

* `BUI` (value: `"BUI"`)

* `C0` (value: `"C0"`)

* `C10` (value: `"C10"`)

* `C11` (value: `"C11"`)

* `C12` (value: `"C12"`)

* `C13` (value: `"C13"`)

* `C14` (value: `"C14"`)

* `C15` (value: `"C15"`)

* `C16` (value: `"C16"`)

* `C17` (value: `"C17"`)

* `C18` (value: `"C18"`)

* `C19` (value: `"C19"`)

* `C20` (value: `"C20"`)

* `C21` (value: `"C21"`)

* `C22` (value: `"C22"`)

* `C23` (value: `"C23"`)

* `C24` (value: `"C24"`)

* `C25` (value: `"C25"`)

* `C26` (value: `"C26"`)

* `C27` (value: `"C27"`)

* `C28` (value: `"C28"`)

* `C29` (value: `"C29"`)

* `C3` (value: `"C3"`)

* `C30` (value: `"C30"`)

* `C31` (value: `"C31"`)

* `C32` (value: `"C32"`)

* `C33` (value: `"C33"`)

* `C34` (value: `"C34"`)

* `C35` (value: `"C35"`)

* `C36` (value: `"C36"`)

* `C37` (value: `"C37"`)

* `C38` (value: `"C38"`)

* `C39` (value: `"C39"`)

* `C40` (value: `"C40"`)

* `C41` (value: `"C41"`)

* `C42` (value: `"C42"`)

* `C43` (value: `"C43"`)

* `C44` (value: `"C44"`)

* `C45` (value: `"C45"`)

* `C46` (value: `"C46"`)

* `C47` (value: `"C47"`)

* `C48` (value: `"C48"`)

* `C49` (value: `"C49"`)

* `C50` (value: `"C50"`)

* `C51` (value: `"C51"`)

* `C52` (value: `"C52"`)

* `C53` (value: `"C53"`)

* `C54` (value: `"C54"`)

* `C55` (value: `"C55"`)

* `C56` (value: `"C56"`)

* `C57` (value: `"C57"`)

* `C58` (value: `"C58"`)

* `C59` (value: `"C59"`)

* `C60` (value: `"C60"`)

* `C61` (value: `"C61"`)

* `C62` (value: `"C62"`)

* `C63` (value: `"C63"`)

* `C64` (value: `"C64"`)

* `C65` (value: `"C65"`)

* `C66` (value: `"C66"`)

* `C67` (value: `"C67"`)

* `C68` (value: `"C68"`)

* `C69` (value: `"C69"`)

* `C7` (value: `"C7"`)

* `C70` (value: `"C70"`)

* `C71` (value: `"C71"`)

* `C72` (value: `"C72"`)

* `C73` (value: `"C73"`)

* `C74` (value: `"C74"`)

* `C75` (value: `"C75"`)

* `C76` (value: `"C76"`)

* `C78` (value: `"C78"`)

* `C79` (value: `"C79"`)

* `C8` (value: `"C8"`)

* `C80` (value: `"C80"`)

* `C81` (value: `"C81"`)

* `C82` (value: `"C82"`)

* `C83` (value: `"C83"`)

* `C84` (value: `"C84"`)

* `C85` (value: `"C85"`)

* `C86` (value: `"C86"`)

* `C87` (value: `"C87"`)

* `C88` (value: `"C88"`)

* `C89` (value: `"C89"`)

* `C9` (value: `"C9"`)

* `C90` (value: `"C90"`)

* `C91` (value: `"C91"`)

* `C92` (value: `"C92"`)

* `C93` (value: `"C93"`)

* `C94` (value: `"C94"`)

* `C95` (value: `"C95"`)

* `C96` (value: `"C96"`)

* `C97` (value: `"C97"`)

* `C99` (value: `"C99"`)

* `CCT` (value: `"CCT"`)

* `CDL` (value: `"CDL"`)

* `CEL` (value: `"CEL"`)

* `CEN` (value: `"CEN"`)

* `CG` (value: `"CG"`)

* `CGM` (value: `"CGM"`)

* `CKG` (value: `"CKG"`)

* `CLF` (value: `"CLF"`)

* `CLT` (value: `"CLT"`)

* `CMK` (value: `"CMK"`)

* `CMQ` (value: `"CMQ"`)

* `CMT` (value: `"CMT"`)

* `CNP` (value: `"CNP"`)

* `CNT` (value: `"CNT"`)

* `COU` (value: `"COU"`)

* `CTG` (value: `"CTG"`)

* `CTM` (value: `"CTM"`)

* `CTN` (value: `"CTN"`)

* `CUR` (value: `"CUR"`)

* `CWA` (value: `"CWA"`)

* `CWI` (value: `"CWI"`)

* `D03` (value: `"D03"`)

* `D04` (value: `"D04"`)

* `D1` (value: `"D1"`)

* `D10` (value: `"D10"`)

* `D11` (value: `"D11"`)

* `D12` (value: `"D12"`)

* `D13` (value: `"D13"`)

* `D15` (value: `"D15"`)

* `D16` (value: `"D16"`)

* `D17` (value: `"D17"`)

* `D18` (value: `"D18"`)

* `D19` (value: `"D19"`)

* `D2` (value: `"D2"`)

* `D20` (value: `"D20"`)

* `D21` (value: `"D21"`)

* `D22` (value: `"D22"`)

* `D23` (value: `"D23"`)

* `D24` (value: `"D24"`)

* `D25` (value: `"D25"`)

* `D26` (value: `"D26"`)

* `D27` (value: `"D27"`)

* `D29` (value: `"D29"`)

* `D30` (value: `"D30"`)

* `D31` (value: `"D31"`)

* `D32` (value: `"D32"`)

* `D33` (value: `"D33"`)

* `D34` (value: `"D34"`)

* `D36` (value: `"D36"`)

* `D41` (value: `"D41"`)

* `D42` (value: `"D42"`)

* `D43` (value: `"D43"`)

* `D44` (value: `"D44"`)

* `D45` (value: `"D45"`)

* `D46` (value: `"D46"`)

* `D47` (value: `"D47"`)

* `D48` (value: `"D48"`)

* `D49` (value: `"D49"`)

* `D5` (value: `"D5"`)

* `D50` (value: `"D50"`)

* `D51` (value: `"D51"`)

* `D52` (value: `"D52"`)

* `D53` (value: `"D53"`)

* `D54` (value: `"D54"`)

* `D55` (value: `"D55"`)

* `D56` (value: `"D56"`)

* `D57` (value: `"D57"`)

* `D58` (value: `"D58"`)

* `D59` (value: `"D59"`)

* `D6` (value: `"D6"`)

* `D60` (value: `"D60"`)

* `D61` (value: `"D61"`)

* `D62` (value: `"D62"`)

* `D63` (value: `"D63"`)

* `D65` (value: `"D65"`)

* `D68` (value: `"D68"`)

* `D69` (value: `"D69"`)

* `D73` (value: `"D73"`)

* `D74` (value: `"D74"`)

* `D77` (value: `"D77"`)

* `D78` (value: `"D78"`)

* `D80` (value: `"D80"`)

* `D81` (value: `"D81"`)

* `D82` (value: `"D82"`)

* `D83` (value: `"D83"`)

* `D85` (value: `"D85"`)

* `D86` (value: `"D86"`)

* `D87` (value: `"D87"`)

* `D88` (value: `"D88"`)

* `D89` (value: `"D89"`)

* `D91` (value: `"D91"`)

* `D93` (value: `"D93"`)

* `D94` (value: `"D94"`)

* `D95` (value: `"D95"`)

* `DAA` (value: `"DAA"`)

* `DAD` (value: `"DAD"`)

* `DAY` (value: `"DAY"`)

* `DB` (value: `"DB"`)

* `DD` (value: `"DD"`)

* `DEC` (value: `"DEC"`)

* `DG` (value: `"DG"`)

* `DJ` (value: `"DJ"`)

* `DLT` (value: `"DLT"`)

* `DMA` (value: `"DMA"`)

* `DMK` (value: `"DMK"`)

* `DMO` (value: `"DMO"`)

* `DMQ` (value: `"DMQ"`)

* `DMT` (value: `"DMT"`)

* `DN` (value: `"DN"`)

* `DPC` (value: `"DPC"`)

* `DPR` (value: `"DPR"`)

* `DPT` (value: `"DPT"`)

* `DRA` (value: `"DRA"`)

* `DRI` (value: `"DRI"`)

* `DRL` (value: `"DRL"`)

* `DT` (value: `"DT"`)

* `DTN` (value: `"DTN"`)

* `DWT` (value: `"DWT"`)

* `DZN` (value: `"DZN"`)

* `DZP` (value: `"DZP"`)

* `E01` (value: `"E01"`)

* `E07` (value: `"E07"`)

* `E08` (value: `"E08"`)

* `E09` (value: `"E09"`)

* `E10` (value: `"E10"`)

* `E12` (value: `"E12"`)

* `E14` (value: `"E14"`)

* `E15` (value: `"E15"`)

* `E16` (value: `"E16"`)

* `E17` (value: `"E17"`)

* `E18` (value: `"E18"`)

* `E19` (value: `"E19"`)

* `E20` (value: `"E20"`)

* `E21` (value: `"E21"`)

* `E22` (value: `"E22"`)

* `E23` (value: `"E23"`)

* `E25` (value: `"E25"`)

* `E27` (value: `"E27"`)

* `E28` (value: `"E28"`)

* `E30` (value: `"E30"`)

* `E31` (value: `"E31"`)

* `E32` (value: `"E32"`)

* `E33` (value: `"E33"`)

* `E34` (value: `"E34"`)

* `E35` (value: `"E35"`)

* `E36` (value: `"E36"`)

* `E37` (value: `"E37"`)

* `E38` (value: `"E38"`)

* `E39` (value: `"E39"`)

* `E4` (value: `"E4"`)

* `E40` (value: `"E40"`)

* `E41` (value: `"E41"`)

* `E42` (value: `"E42"`)

* `E43` (value: `"E43"`)

* `E44` (value: `"E44"`)

* `E45` (value: `"E45"`)

* `E46` (value: `"E46"`)

* `E47` (value: `"E47"`)

* `E48` (value: `"E48"`)

* `E49` (value: `"E49"`)

* `E50` (value: `"E50"`)

* `E51` (value: `"E51"`)

* `E52` (value: `"E52"`)

* `E53` (value: `"E53"`)

* `E54` (value: `"E54"`)

* `E55` (value: `"E55"`)

* `E56` (value: `"E56"`)

* `E57` (value: `"E57"`)

* `E58` (value: `"E58"`)

* `E59` (value: `"E59"`)

* `E60` (value: `"E60"`)

* `E61` (value: `"E61"`)

* `E62` (value: `"E62"`)

* `E63` (value: `"E63"`)

* `E64` (value: `"E64"`)

* `E65` (value: `"E65"`)

* `E66` (value: `"E66"`)

* `E67` (value: `"E67"`)

* `E68` (value: `"E68"`)

* `E69` (value: `"E69"`)

* `E70` (value: `"E70"`)

* `E71` (value: `"E71"`)

* `E72` (value: `"E72"`)

* `E73` (value: `"E73"`)

* `E74` (value: `"E74"`)

* `E75` (value: `"E75"`)

* `E76` (value: `"E76"`)

* `E77` (value: `"E77"`)

* `E78` (value: `"E78"`)

* `E79` (value: `"E79"`)

* `E80` (value: `"E80"`)

* `E81` (value: `"E81"`)

* `E82` (value: `"E82"`)

* `E83` (value: `"E83"`)

* `E84` (value: `"E84"`)

* `E85` (value: `"E85"`)

* `E86` (value: `"E86"`)

* `E87` (value: `"E87"`)

* `E88` (value: `"E88"`)

* `E89` (value: `"E89"`)

* `E90` (value: `"E90"`)

* `E91` (value: `"E91"`)

* `E92` (value: `"E92"`)

* `E93` (value: `"E93"`)

* `E94` (value: `"E94"`)

* `E95` (value: `"E95"`)

* `E96` (value: `"E96"`)

* `E97` (value: `"E97"`)

* `E98` (value: `"E98"`)

* `E99` (value: `"E99"`)

* `EA` (value: `"EA"`)

* `EB` (value: `"EB"`)

* `EQ` (value: `"EQ"`)

* `F01` (value: `"F01"`)

* `F02` (value: `"F02"`)

* `F03` (value: `"F03"`)

* `F04` (value: `"F04"`)

* `F05` (value: `"F05"`)

* `F06` (value: `"F06"`)

* `F07` (value: `"F07"`)

* `F08` (value: `"F08"`)

* `F10` (value: `"F10"`)

* `F11` (value: `"F11"`)

* `F12` (value: `"F12"`)

* `F13` (value: `"F13"`)

* `F14` (value: `"F14"`)

* `F15` (value: `"F15"`)

* `F16` (value: `"F16"`)

* `F17` (value: `"F17"`)

* `F18` (value: `"F18"`)

* `F19` (value: `"F19"`)

* `F20` (value: `"F20"`)

* `F21` (value: `"F21"`)

* `F22` (value: `"F22"`)

* `F23` (value: `"F23"`)

* `F24` (value: `"F24"`)

* `F25` (value: `"F25"`)

* `F26` (value: `"F26"`)

* `F27` (value: `"F27"`)

* `F28` (value: `"F28"`)

* `F29` (value: `"F29"`)

* `F30` (value: `"F30"`)

* `F31` (value: `"F31"`)

* `F32` (value: `"F32"`)

* `F33` (value: `"F33"`)

* `F34` (value: `"F34"`)

* `F35` (value: `"F35"`)

* `F36` (value: `"F36"`)

* `F37` (value: `"F37"`)

* `F38` (value: `"F38"`)

* `F39` (value: `"F39"`)

* `F40` (value: `"F40"`)

* `F41` (value: `"F41"`)

* `F42` (value: `"F42"`)

* `F43` (value: `"F43"`)

* `F44` (value: `"F44"`)

* `F45` (value: `"F45"`)

* `F46` (value: `"F46"`)

* `F47` (value: `"F47"`)

* `F48` (value: `"F48"`)

* `F49` (value: `"F49"`)

* `F50` (value: `"F50"`)

* `F51` (value: `"F51"`)

* `F52` (value: `"F52"`)

* `F53` (value: `"F53"`)

* `F54` (value: `"F54"`)

* `F55` (value: `"F55"`)

* `F56` (value: `"F56"`)

* `F57` (value: `"F57"`)

* `F58` (value: `"F58"`)

* `F59` (value: `"F59"`)

* `F60` (value: `"F60"`)

* `F61` (value: `"F61"`)

* `F62` (value: `"F62"`)

* `F63` (value: `"F63"`)

* `F64` (value: `"F64"`)

* `F65` (value: `"F65"`)

* `F66` (value: `"F66"`)

* `F67` (value: `"F67"`)

* `F68` (value: `"F68"`)

* `F69` (value: `"F69"`)

* `F70` (value: `"F70"`)

* `F71` (value: `"F71"`)

* `F72` (value: `"F72"`)

* `F73` (value: `"F73"`)

* `F74` (value: `"F74"`)

* `F75` (value: `"F75"`)

* `F76` (value: `"F76"`)

* `F77` (value: `"F77"`)

* `F78` (value: `"F78"`)

* `F79` (value: `"F79"`)

* `F80` (value: `"F80"`)

* `F81` (value: `"F81"`)

* `F82` (value: `"F82"`)

* `F83` (value: `"F83"`)

* `F84` (value: `"F84"`)

* `F85` (value: `"F85"`)

* `F86` (value: `"F86"`)

* `F87` (value: `"F87"`)

* `F88` (value: `"F88"`)

* `F89` (value: `"F89"`)

* `F90` (value: `"F90"`)

* `F91` (value: `"F91"`)

* `F92` (value: `"F92"`)

* `F93` (value: `"F93"`)

* `F94` (value: `"F94"`)

* `F95` (value: `"F95"`)

* `F96` (value: `"F96"`)

* `F97` (value: `"F97"`)

* `F98` (value: `"F98"`)

* `F99` (value: `"F99"`)

* `FAH` (value: `"FAH"`)

* `FAR` (value: `"FAR"`)

* `FBM` (value: `"FBM"`)

* `FC` (value: `"FC"`)

* `FF` (value: `"FF"`)

* `FH` (value: `"FH"`)

* `FIT` (value: `"FIT"`)

* `FL` (value: `"FL"`)

* `FOT` (value: `"FOT"`)

* `FP` (value: `"FP"`)

* `FR` (value: `"FR"`)

* `FS` (value: `"FS"`)

* `FTK` (value: `"FTK"`)

* `FTQ` (value: `"FTQ"`)

* `G01` (value: `"G01"`)

* `G04` (value: `"G04"`)

* `G05` (value: `"G05"`)

* `G06` (value: `"G06"`)

* `G08` (value: `"G08"`)

* `G09` (value: `"G09"`)

* `G10` (value: `"G10"`)

* `G11` (value: `"G11"`)

* `G12` (value: `"G12"`)

* `G13` (value: `"G13"`)

* `G14` (value: `"G14"`)

* `G15` (value: `"G15"`)

* `G16` (value: `"G16"`)

* `G17` (value: `"G17"`)

* `G18` (value: `"G18"`)

* `G19` (value: `"G19"`)

* `G2` (value: `"G2"`)

* `G20` (value: `"G20"`)

* `G21` (value: `"G21"`)

* `G23` (value: `"G23"`)

* `G24` (value: `"G24"`)

* `G25` (value: `"G25"`)

* `G26` (value: `"G26"`)

* `G27` (value: `"G27"`)

* `G28` (value: `"G28"`)

* `G29` (value: `"G29"`)

* `G3` (value: `"G3"`)

* `G30` (value: `"G30"`)

* `G31` (value: `"G31"`)

* `G32` (value: `"G32"`)

* `G33` (value: `"G33"`)

* `G34` (value: `"G34"`)

* `G35` (value: `"G35"`)

* `G36` (value: `"G36"`)

* `G37` (value: `"G37"`)

* `G38` (value: `"G38"`)

* `G39` (value: `"G39"`)

* `G40` (value: `"G40"`)

* `G41` (value: `"G41"`)

* `G42` (value: `"G42"`)

* `G43` (value: `"G43"`)

* `G44` (value: `"G44"`)

* `G45` (value: `"G45"`)

* `G46` (value: `"G46"`)

* `G47` (value: `"G47"`)

* `G48` (value: `"G48"`)

* `G49` (value: `"G49"`)

* `G50` (value: `"G50"`)

* `G51` (value: `"G51"`)

* `G52` (value: `"G52"`)

* `G53` (value: `"G53"`)

* `G54` (value: `"G54"`)

* `G55` (value: `"G55"`)

* `G56` (value: `"G56"`)

* `G57` (value: `"G57"`)

* `G58` (value: `"G58"`)

* `G59` (value: `"G59"`)

* `G60` (value: `"G60"`)

* `G61` (value: `"G61"`)

* `G62` (value: `"G62"`)

* `G63` (value: `"G63"`)

* `G64` (value: `"G64"`)

* `G65` (value: `"G65"`)

* `G66` (value: `"G66"`)

* `G67` (value: `"G67"`)

* `G68` (value: `"G68"`)

* `G69` (value: `"G69"`)

* `G70` (value: `"G70"`)

* `G71` (value: `"G71"`)

* `G72` (value: `"G72"`)

* `G73` (value: `"G73"`)

* `G74` (value: `"G74"`)

* `G75` (value: `"G75"`)

* `G76` (value: `"G76"`)

* `G77` (value: `"G77"`)

* `G78` (value: `"G78"`)

* `G79` (value: `"G79"`)

* `G80` (value: `"G80"`)

* `G81` (value: `"G81"`)

* `G82` (value: `"G82"`)

* `G83` (value: `"G83"`)

* `G84` (value: `"G84"`)

* `G85` (value: `"G85"`)

* `G86` (value: `"G86"`)

* `G87` (value: `"G87"`)

* `G88` (value: `"G88"`)

* `G89` (value: `"G89"`)

* `G90` (value: `"G90"`)

* `G91` (value: `"G91"`)

* `G92` (value: `"G92"`)

* `G93` (value: `"G93"`)

* `G94` (value: `"G94"`)

* `G95` (value: `"G95"`)

* `G96` (value: `"G96"`)

* `G97` (value: `"G97"`)

* `G98` (value: `"G98"`)

* `G99` (value: `"G99"`)

* `GB` (value: `"GB"`)

* `GBQ` (value: `"GBQ"`)

* `GDW` (value: `"GDW"`)

* `GE` (value: `"GE"`)

* `GF` (value: `"GF"`)

* `GFI` (value: `"GFI"`)

* `GGR` (value: `"GGR"`)

* `GIA` (value: `"GIA"`)

* `GIC` (value: `"GIC"`)

* `GII` (value: `"GII"`)

* `GIP` (value: `"GIP"`)

* `GJ` (value: `"GJ"`)

* `GL` (value: `"GL"`)

* `GLD` (value: `"GLD"`)

* `GLI` (value: `"GLI"`)

* `GLL` (value: `"GLL"`)

* `GM` (value: `"GM"`)

* `GO` (value: `"GO"`)

* `GP` (value: `"GP"`)

* `GQ` (value: `"GQ"`)

* `GRM` (value: `"GRM"`)

* `GRN` (value: `"GRN"`)

* `GRO` (value: `"GRO"`)

* `GV` (value: `"GV"`)

* `GWH` (value: `"GWH"`)

* `H03` (value: `"H03"`)

* `H04` (value: `"H04"`)

* `H05` (value: `"H05"`)

* `H06` (value: `"H06"`)

* `H07` (value: `"H07"`)

* `H08` (value: `"H08"`)

* `H09` (value: `"H09"`)

* `H10` (value: `"H10"`)

* `H11` (value: `"H11"`)

* `H12` (value: `"H12"`)

* `H13` (value: `"H13"`)

* `H14` (value: `"H14"`)

* `H15` (value: `"H15"`)

* `H16` (value: `"H16"`)

* `H18` (value: `"H18"`)

* `H19` (value: `"H19"`)

* `H20` (value: `"H20"`)

* `H21` (value: `"H21"`)

* `H22` (value: `"H22"`)

* `H23` (value: `"H23"`)

* `H24` (value: `"H24"`)

* `H25` (value: `"H25"`)

* `H26` (value: `"H26"`)

* `H27` (value: `"H27"`)

* `H28` (value: `"H28"`)

* `H29` (value: `"H29"`)

* `H30` (value: `"H30"`)

* `H31` (value: `"H31"`)

* `H32` (value: `"H32"`)

* `H33` (value: `"H33"`)

* `H34` (value: `"H34"`)

* `H35` (value: `"H35"`)

* `H36` (value: `"H36"`)

* `H37` (value: `"H37"`)

* `H38` (value: `"H38"`)

* `H39` (value: `"H39"`)

* `H40` (value: `"H40"`)

* `H41` (value: `"H41"`)

* `H42` (value: `"H42"`)

* `H43` (value: `"H43"`)

* `H44` (value: `"H44"`)

* `H45` (value: `"H45"`)

* `H46` (value: `"H46"`)

* `H47` (value: `"H47"`)

* `H48` (value: `"H48"`)

* `H49` (value: `"H49"`)

* `H50` (value: `"H50"`)

* `H51` (value: `"H51"`)

* `H52` (value: `"H52"`)

* `H53` (value: `"H53"`)

* `H54` (value: `"H54"`)

* `H55` (value: `"H55"`)

* `H56` (value: `"H56"`)

* `H57` (value: `"H57"`)

* `H58` (value: `"H58"`)

* `H59` (value: `"H59"`)

* `H60` (value: `"H60"`)

* `H61` (value: `"H61"`)

* `H62` (value: `"H62"`)

* `H63` (value: `"H63"`)

* `H64` (value: `"H64"`)

* `H65` (value: `"H65"`)

* `H66` (value: `"H66"`)

* `H67` (value: `"H67"`)

* `H68` (value: `"H68"`)

* `H69` (value: `"H69"`)

* `H70` (value: `"H70"`)

* `H71` (value: `"H71"`)

* `H72` (value: `"H72"`)

* `H73` (value: `"H73"`)

* `H74` (value: `"H74"`)

* `H75` (value: `"H75"`)

* `H76` (value: `"H76"`)

* `H77` (value: `"H77"`)

* `H79` (value: `"H79"`)

* `H80` (value: `"H80"`)

* `H81` (value: `"H81"`)

* `H82` (value: `"H82"`)

* `H83` (value: `"H83"`)

* `H84` (value: `"H84"`)

* `H85` (value: `"H85"`)

* `H87` (value: `"H87"`)

* `H88` (value: `"H88"`)

* `H89` (value: `"H89"`)

* `H90` (value: `"H90"`)

* `H91` (value: `"H91"`)

* `H92` (value: `"H92"`)

* `H93` (value: `"H93"`)

* `H94` (value: `"H94"`)

* `H95` (value: `"H95"`)

* `H96` (value: `"H96"`)

* `H98` (value: `"H98"`)

* `H99` (value: `"H99"`)

* `HA` (value: `"HA"`)

* `HBA` (value: `"HBA"`)

* `HBX` (value: `"HBX"`)

* `HC` (value: `"HC"`)

* `HDW` (value: `"HDW"`)

* `HEA` (value: `"HEA"`)

* `HGM` (value: `"HGM"`)

* `HH` (value: `"HH"`)

* `HIU` (value: `"HIU"`)

* `HKM` (value: `"HKM"`)

* `HLT` (value: `"HLT"`)

* `HM` (value: `"HM"`)

* `HMQ` (value: `"HMQ"`)

* `HMT` (value: `"HMT"`)

* `HPA` (value: `"HPA"`)

* `HTZ` (value: `"HTZ"`)

* `HUR` (value: `"HUR"`)

* `IA` (value: `"IA"`)

* `IE` (value: `"IE"`)

* `INH` (value: `"INH"`)

* `INK` (value: `"INK"`)

* `INQ` (value: `"INQ"`)

* `ISD` (value: `"ISD"`)

* `IU` (value: `"IU"`)

* `IV` (value: `"IV"`)

* `J10` (value: `"J10"`)

* `J12` (value: `"J12"`)

* `J13` (value: `"J13"`)

* `J14` (value: `"J14"`)

* `J15` (value: `"J15"`)

* `J16` (value: `"J16"`)

* `J17` (value: `"J17"`)

* `J18` (value: `"J18"`)

* `J19` (value: `"J19"`)

* `J2` (value: `"J2"`)

* `J20` (value: `"J20"`)

* `J21` (value: `"J21"`)

* `J22` (value: `"J22"`)

* `J23` (value: `"J23"`)

* `J24` (value: `"J24"`)

* `J25` (value: `"J25"`)

* `J26` (value: `"J26"`)

* `J27` (value: `"J27"`)

* `J28` (value: `"J28"`)

* `J29` (value: `"J29"`)

* `J30` (value: `"J30"`)

* `J31` (value: `"J31"`)

* `J32` (value: `"J32"`)

* `J33` (value: `"J33"`)

* `J34` (value: `"J34"`)

* `J35` (value: `"J35"`)

* `J36` (value: `"J36"`)

* `J38` (value: `"J38"`)

* `J39` (value: `"J39"`)

* `J40` (value: `"J40"`)

* `J41` (value: `"J41"`)

* `J42` (value: `"J42"`)

* `J43` (value: `"J43"`)

* `J44` (value: `"J44"`)

* `J45` (value: `"J45"`)

* `J46` (value: `"J46"`)

* `J47` (value: `"J47"`)

* `J48` (value: `"J48"`)

* `J49` (value: `"J49"`)

* `J50` (value: `"J50"`)

* `J51` (value: `"J51"`)

* `J52` (value: `"J52"`)

* `J53` (value: `"J53"`)

* `J54` (value: `"J54"`)

* `J55` (value: `"J55"`)

* `J56` (value: `"J56"`)

* `J57` (value: `"J57"`)

* `J58` (value: `"J58"`)

* `J59` (value: `"J59"`)

* `J60` (value: `"J60"`)

* `J61` (value: `"J61"`)

* `J62` (value: `"J62"`)

* `J63` (value: `"J63"`)

* `J64` (value: `"J64"`)

* `J65` (value: `"J65"`)

* `J66` (value: `"J66"`)

* `J67` (value: `"J67"`)

* `J68` (value: `"J68"`)

* `J69` (value: `"J69"`)

* `J70` (value: `"J70"`)

* `J71` (value: `"J71"`)

* `J72` (value: `"J72"`)

* `J73` (value: `"J73"`)

* `J74` (value: `"J74"`)

* `J75` (value: `"J75"`)

* `J76` (value: `"J76"`)

* `J78` (value: `"J78"`)

* `J79` (value: `"J79"`)

* `J81` (value: `"J81"`)

* `J82` (value: `"J82"`)

* `J83` (value: `"J83"`)

* `J84` (value: `"J84"`)

* `J85` (value: `"J85"`)

* `J87` (value: `"J87"`)

* `J90` (value: `"J90"`)

* `J91` (value: `"J91"`)

* `J92` (value: `"J92"`)

* `J93` (value: `"J93"`)

* `J95` (value: `"J95"`)

* `J96` (value: `"J96"`)

* `J97` (value: `"J97"`)

* `J98` (value: `"J98"`)

* `J99` (value: `"J99"`)

* `JE` (value: `"JE"`)

* `JK` (value: `"JK"`)

* `JM` (value: `"JM"`)

* `JNT` (value: `"JNT"`)

* `JOU` (value: `"JOU"`)

* `JPS` (value: `"JPS"`)

* `JWL` (value: `"JWL"`)

* `K1` (value: `"K1"`)

* `K10` (value: `"K10"`)

* `K11` (value: `"K11"`)

* `K12` (value: `"K12"`)

* `K13` (value: `"K13"`)

* `K14` (value: `"K14"`)

* `K15` (value: `"K15"`)

* `K16` (value: `"K16"`)

* `K17` (value: `"K17"`)

* `K18` (value: `"K18"`)

* `K19` (value: `"K19"`)

* `K2` (value: `"K2"`)

* `K20` (value: `"K20"`)

* `K21` (value: `"K21"`)

* `K22` (value: `"K22"`)

* `K23` (value: `"K23"`)

* `K26` (value: `"K26"`)

* `K27` (value: `"K27"`)

* `K28` (value: `"K28"`)

* `K3` (value: `"K3"`)

* `K30` (value: `"K30"`)

* `K31` (value: `"K31"`)

* `K32` (value: `"K32"`)

* `K33` (value: `"K33"`)

* `K34` (value: `"K34"`)

* `K35` (value: `"K35"`)

* `K36` (value: `"K36"`)

* `K37` (value: `"K37"`)

* `K38` (value: `"K38"`)

* `K39` (value: `"K39"`)

* `K40` (value: `"K40"`)

* `K41` (value: `"K41"`)

* `K42` (value: `"K42"`)

* `K43` (value: `"K43"`)

* `K45` (value: `"K45"`)

* `K46` (value: `"K46"`)

* `K47` (value: `"K47"`)

* `K48` (value: `"K48"`)

* `K49` (value: `"K49"`)

* `K50` (value: `"K50"`)

* `K51` (value: `"K51"`)

* `K52` (value: `"K52"`)

* `K53` (value: `"K53"`)

* `K54` (value: `"K54"`)

* `K55` (value: `"K55"`)

* `K58` (value: `"K58"`)

* `K59` (value: `"K59"`)

* `K6` (value: `"K6"`)

* `K60` (value: `"K60"`)

* `K61` (value: `"K61"`)

* `K62` (value: `"K62"`)

* `K63` (value: `"K63"`)

* `K64` (value: `"K64"`)

* `K65` (value: `"K65"`)

* `K66` (value: `"K66"`)

* `K67` (value: `"K67"`)

* `K68` (value: `"K68"`)

* `K69` (value: `"K69"`)

* `K70` (value: `"K70"`)

* `K71` (value: `"K71"`)

* `K73` (value: `"K73"`)

* `K74` (value: `"K74"`)

* `K75` (value: `"K75"`)

* `K76` (value: `"K76"`)

* `K77` (value: `"K77"`)

* `K78` (value: `"K78"`)

* `K79` (value: `"K79"`)

* `K80` (value: `"K80"`)

* `K81` (value: `"K81"`)

* `K82` (value: `"K82"`)

* `K83` (value: `"K83"`)

* `K84` (value: `"K84"`)

* `K85` (value: `"K85"`)

* `K86` (value: `"K86"`)

* `K87` (value: `"K87"`)

* `K88` (value: `"K88"`)

* `K89` (value: `"K89"`)

* `K90` (value: `"K90"`)

* `K91` (value: `"K91"`)

* `K92` (value: `"K92"`)

* `K93` (value: `"K93"`)

* `K94` (value: `"K94"`)

* `K95` (value: `"K95"`)

* `K96` (value: `"K96"`)

* `K97` (value: `"K97"`)

* `K98` (value: `"K98"`)

* `K99` (value: `"K99"`)

* `KA` (value: `"KA"`)

* `KAT` (value: `"KAT"`)

* `KB` (value: `"KB"`)

* `KBA` (value: `"KBA"`)

* `KCC` (value: `"KCC"`)

* `KDW` (value: `"KDW"`)

* `KEL` (value: `"KEL"`)

* `KGM` (value: `"KGM"`)

* `KGS` (value: `"KGS"`)

* `KHY` (value: `"KHY"`)

* `KHZ` (value: `"KHZ"`)

* `KI` (value: `"KI"`)

* `KIC` (value: `"KIC"`)

* `KIP` (value: `"KIP"`)

* `KJ` (value: `"KJ"`)

* `KJO` (value: `"KJO"`)

* `KL` (value: `"KL"`)

* `KLK` (value: `"KLK"`)

* `KLX` (value: `"KLX"`)

* `KMA` (value: `"KMA"`)

* `KMH` (value: `"KMH"`)

* `KMK` (value: `"KMK"`)

* `KMQ` (value: `"KMQ"`)

* `KMT` (value: `"KMT"`)

* `KNI` (value: `"KNI"`)

* `KNM` (value: `"KNM"`)

* `KNS` (value: `"KNS"`)

* `KNT` (value: `"KNT"`)

* `KO` (value: `"KO"`)

* `KPA` (value: `"KPA"`)

* `KPH` (value: `"KPH"`)

* `KPO` (value: `"KPO"`)

* `KPP` (value: `"KPP"`)

* `KR` (value: `"KR"`)

* `KSD` (value: `"KSD"`)

* `KSH` (value: `"KSH"`)

* `KT` (value: `"KT"`)

* `KTN` (value: `"KTN"`)

* `KUR` (value: `"KUR"`)

* `KVA` (value: `"KVA"`)

* `KVR` (value: `"KVR"`)

* `KVT` (value: `"KVT"`)

* `KW` (value: `"KW"`)

* `KWH` (value: `"KWH"`)

* `KWO` (value: `"KWO"`)

* `KWT` (value: `"KWT"`)

* `KX` (value: `"KX"`)

* `L10` (value: `"L10"`)

* `L11` (value: `"L11"`)

* `L12` (value: `"L12"`)

* `L13` (value: `"L13"`)

* `L14` (value: `"L14"`)

* `L15` (value: `"L15"`)

* `L16` (value: `"L16"`)

* `L17` (value: `"L17"`)

* `L18` (value: `"L18"`)

* `L19` (value: `"L19"`)

* `L2` (value: `"L2"`)

* `L20` (value: `"L20"`)

* `L21` (value: `"L21"`)

* `L23` (value: `"L23"`)

* `L24` (value: `"L24"`)

* `L25` (value: `"L25"`)

* `L26` (value: `"L26"`)

* `L27` (value: `"L27"`)

* `L28` (value: `"L28"`)

* `L29` (value: `"L29"`)

* `L30` (value: `"L30"`)

* `L31` (value: `"L31"`)

* `L32` (value: `"L32"`)

* `L33` (value: `"L33"`)

* `L34` (value: `"L34"`)

* `L35` (value: `"L35"`)

* `L36` (value: `"L36"`)

* `L37` (value: `"L37"`)

* `L38` (value: `"L38"`)

* `L39` (value: `"L39"`)

* `L40` (value: `"L40"`)

* `L41` (value: `"L41"`)

* `L42` (value: `"L42"`)

* `L43` (value: `"L43"`)

* `L44` (value: `"L44"`)

* `L45` (value: `"L45"`)

* `L46` (value: `"L46"`)

* `L47` (value: `"L47"`)

* `L48` (value: `"L48"`)

* `L49` (value: `"L49"`)

* `L50` (value: `"L50"`)

* `L51` (value: `"L51"`)

* `L52` (value: `"L52"`)

* `L53` (value: `"L53"`)

* `L54` (value: `"L54"`)

* `L55` (value: `"L55"`)

* `L56` (value: `"L56"`)

* `L57` (value: `"L57"`)

* `L58` (value: `"L58"`)

* `L59` (value: `"L59"`)

* `L60` (value: `"L60"`)

* `L63` (value: `"L63"`)

* `L64` (value: `"L64"`)

* `L65` (value: `"L65"`)

* `L66` (value: `"L66"`)

* `L67` (value: `"L67"`)

* `L68` (value: `"L68"`)

* `L69` (value: `"L69"`)

* `L70` (value: `"L70"`)

* `L71` (value: `"L71"`)

* `L72` (value: `"L72"`)

* `L73` (value: `"L73"`)

* `L74` (value: `"L74"`)

* `L75` (value: `"L75"`)

* `L76` (value: `"L76"`)

* `L77` (value: `"L77"`)

* `L78` (value: `"L78"`)

* `L79` (value: `"L79"`)

* `L80` (value: `"L80"`)

* `L81` (value: `"L81"`)

* `L82` (value: `"L82"`)

* `L83` (value: `"L83"`)

* `L84` (value: `"L84"`)

* `L85` (value: `"L85"`)

* `L86` (value: `"L86"`)

* `L87` (value: `"L87"`)

* `L88` (value: `"L88"`)

* `L89` (value: `"L89"`)

* `L90` (value: `"L90"`)

* `L91` (value: `"L91"`)

* `L92` (value: `"L92"`)

* `L93` (value: `"L93"`)

* `L94` (value: `"L94"`)

* `L95` (value: `"L95"`)

* `L96` (value: `"L96"`)

* `L98` (value: `"L98"`)

* `L99` (value: `"L99"`)

* `LA` (value: `"LA"`)

* `LAC` (value: `"LAC"`)

* `LBR` (value: `"LBR"`)

* `LBT` (value: `"LBT"`)

* `LD` (value: `"LD"`)

* `LEF` (value: `"LEF"`)

* `LF` (value: `"LF"`)

* `LH` (value: `"LH"`)

* `LK` (value: `"LK"`)

* `LM` (value: `"LM"`)

* `LN` (value: `"LN"`)

* `LO` (value: `"LO"`)

* `LP` (value: `"LP"`)

* `LPA` (value: `"LPA"`)

* `LR` (value: `"LR"`)

* `LS` (value: `"LS"`)

* `LTN` (value: `"LTN"`)

* `LTR` (value: `"LTR"`)

* `LUB` (value: `"LUB"`)

* `LUM` (value: `"LUM"`)

* `LUX` (value: `"LUX"`)

* `LY` (value: `"LY"`)

* `M1` (value: `"M1"`)

* `M10` (value: `"M10"`)

* `M11` (value: `"M11"`)

* `M12` (value: `"M12"`)

* `M13` (value: `"M13"`)

* `M14` (value: `"M14"`)

* `M15` (value: `"M15"`)

* `M16` (value: `"M16"`)

* `M17` (value: `"M17"`)

* `M18` (value: `"M18"`)

* `M19` (value: `"M19"`)

* `M20` (value: `"M20"`)

* `M21` (value: `"M21"`)

* `M22` (value: `"M22"`)

* `M23` (value: `"M23"`)

* `M24` (value: `"M24"`)

* `M25` (value: `"M25"`)

* `M26` (value: `"M26"`)

* `M27` (value: `"M27"`)

* `M29` (value: `"M29"`)

* `M30` (value: `"M30"`)

* `M31` (value: `"M31"`)

* `M32` (value: `"M32"`)

* `M33` (value: `"M33"`)

* `M34` (value: `"M34"`)

* `M35` (value: `"M35"`)

* `M36` (value: `"M36"`)

* `M37` (value: `"M37"`)

* `M38` (value: `"M38"`)

* `M39` (value: `"M39"`)

* `M4` (value: `"M4"`)

* `M40` (value: `"M40"`)

* `M41` (value: `"M41"`)

* `M42` (value: `"M42"`)

* `M43` (value: `"M43"`)

* `M44` (value: `"M44"`)

* `M45` (value: `"M45"`)

* `M46` (value: `"M46"`)

* `M47` (value: `"M47"`)

* `M48` (value: `"M48"`)

* `M49` (value: `"M49"`)

* `M5` (value: `"M5"`)

* `M50` (value: `"M50"`)

* `M51` (value: `"M51"`)

* `M52` (value: `"M52"`)

* `M53` (value: `"M53"`)

* `M55` (value: `"M55"`)

* `M56` (value: `"M56"`)

* `M57` (value: `"M57"`)

* `M58` (value: `"M58"`)

* `M59` (value: `"M59"`)

* `M60` (value: `"M60"`)

* `M61` (value: `"M61"`)

* `M62` (value: `"M62"`)

* `M63` (value: `"M63"`)

* `M64` (value: `"M64"`)

* `M65` (value: `"M65"`)

* `M66` (value: `"M66"`)

* `M67` (value: `"M67"`)

* `M68` (value: `"M68"`)

* `M69` (value: `"M69"`)

* `M7` (value: `"M7"`)

* `M70` (value: `"M70"`)

* `M71` (value: `"M71"`)

* `M72` (value: `"M72"`)

* `M73` (value: `"M73"`)

* `M74` (value: `"M74"`)

* `M75` (value: `"M75"`)

* `M76` (value: `"M76"`)

* `M77` (value: `"M77"`)

* `M78` (value: `"M78"`)

* `M79` (value: `"M79"`)

* `M80` (value: `"M80"`)

* `M81` (value: `"M81"`)

* `M82` (value: `"M82"`)

* `M83` (value: `"M83"`)

* `M84` (value: `"M84"`)

* `M85` (value: `"M85"`)

* `M86` (value: `"M86"`)

* `M87` (value: `"M87"`)

* `M88` (value: `"M88"`)

* `M89` (value: `"M89"`)

* `M9` (value: `"M9"`)

* `M90` (value: `"M90"`)

* `M91` (value: `"M91"`)

* `M92` (value: `"M92"`)

* `M93` (value: `"M93"`)

* `M94` (value: `"M94"`)

* `M95` (value: `"M95"`)

* `M96` (value: `"M96"`)

* `M97` (value: `"M97"`)

* `M98` (value: `"M98"`)

* `M99` (value: `"M99"`)

* `MAH` (value: `"MAH"`)

* `MAL` (value: `"MAL"`)

* `MAM` (value: `"MAM"`)

* `MAR` (value: `"MAR"`)

* `MAW` (value: `"MAW"`)

* `MBE` (value: `"MBE"`)

* `MBF` (value: `"MBF"`)

* `MBR` (value: `"MBR"`)

* `MC` (value: `"MC"`)

* `MCU` (value: `"MCU"`)

* `MD` (value: `"MD"`)

* `MGM` (value: `"MGM"`)

* `MHZ` (value: `"MHZ"`)

* `MIK` (value: `"MIK"`)

* `MIL` (value: `"MIL"`)

* `MIN` (value: `"MIN"`)

* `MIO` (value: `"MIO"`)

* `MIU` (value: `"MIU"`)

* `MLD` (value: `"MLD"`)

* `MLT` (value: `"MLT"`)

* `MMK` (value: `"MMK"`)

* `MMQ` (value: `"MMQ"`)

* `MMT` (value: `"MMT"`)

* `MND` (value: `"MND"`)

* `MON` (value: `"MON"`)

* `MPA` (value: `"MPA"`)

* `MQH` (value: `"MQH"`)

* `MQS` (value: `"MQS"`)

* `MSK` (value: `"MSK"`)

* `MTK` (value: `"MTK"`)

* `MTQ` (value: `"MTQ"`)

* `MTR` (value: `"MTR"`)

* `MTS` (value: `"MTS"`)

* `MVA` (value: `"MVA"`)

* `MWH` (value: `"MWH"`)

* `N1` (value: `"N1"`)

* `N10` (value: `"N10"`)

* `N11` (value: `"N11"`)

* `N12` (value: `"N12"`)

* `N13` (value: `"N13"`)

* `N14` (value: `"N14"`)

* `N15` (value: `"N15"`)

* `N16` (value: `"N16"`)

* `N17` (value: `"N17"`)

* `N18` (value: `"N18"`)

* `N19` (value: `"N19"`)

* `N20` (value: `"N20"`)

* `N21` (value: `"N21"`)

* `N22` (value: `"N22"`)

* `N23` (value: `"N23"`)

* `N24` (value: `"N24"`)

* `N25` (value: `"N25"`)

* `N26` (value: `"N26"`)

* `N27` (value: `"N27"`)

* `N28` (value: `"N28"`)

* `N29` (value: `"N29"`)

* `N3` (value: `"N3"`)

* `N30` (value: `"N30"`)

* `N31` (value: `"N31"`)

* `N32` (value: `"N32"`)

* `N33` (value: `"N33"`)

* `N34` (value: `"N34"`)

* `N35` (value: `"N35"`)

* `N36` (value: `"N36"`)

* `N37` (value: `"N37"`)

* `N38` (value: `"N38"`)

* `N39` (value: `"N39"`)

* `N40` (value: `"N40"`)

* `N41` (value: `"N41"`)

* `N42` (value: `"N42"`)

* `N43` (value: `"N43"`)

* `N44` (value: `"N44"`)

* `N45` (value: `"N45"`)

* `N46` (value: `"N46"`)

* `N47` (value: `"N47"`)

* `N48` (value: `"N48"`)

* `N49` (value: `"N49"`)

* `N50` (value: `"N50"`)

* `N51` (value: `"N51"`)

* `N52` (value: `"N52"`)

* `N53` (value: `"N53"`)

* `N54` (value: `"N54"`)

* `N55` (value: `"N55"`)

* `N56` (value: `"N56"`)

* `N57` (value: `"N57"`)

* `N58` (value: `"N58"`)

* `N59` (value: `"N59"`)

* `N60` (value: `"N60"`)

* `N61` (value: `"N61"`)

* `N62` (value: `"N62"`)

* `N63` (value: `"N63"`)

* `N64` (value: `"N64"`)

* `N65` (value: `"N65"`)

* `N66` (value: `"N66"`)

* `N67` (value: `"N67"`)

* `N68` (value: `"N68"`)

* `N69` (value: `"N69"`)

* `N70` (value: `"N70"`)

* `N71` (value: `"N71"`)

* `N72` (value: `"N72"`)

* `N73` (value: `"N73"`)

* `N74` (value: `"N74"`)

* `N75` (value: `"N75"`)

* `N76` (value: `"N76"`)

* `N77` (value: `"N77"`)

* `N78` (value: `"N78"`)

* `N79` (value: `"N79"`)

* `N80` (value: `"N80"`)

* `N81` (value: `"N81"`)

* `N82` (value: `"N82"`)

* `N83` (value: `"N83"`)

* `N84` (value: `"N84"`)

* `N85` (value: `"N85"`)

* `N86` (value: `"N86"`)

* `N87` (value: `"N87"`)

* `N88` (value: `"N88"`)

* `N89` (value: `"N89"`)

* `N90` (value: `"N90"`)

* `N91` (value: `"N91"`)

* `N92` (value: `"N92"`)

* `N93` (value: `"N93"`)

* `N94` (value: `"N94"`)

* `N95` (value: `"N95"`)

* `N96` (value: `"N96"`)

* `N97` (value: `"N97"`)

* `N98` (value: `"N98"`)

* `N99` (value: `"N99"`)

* `NA` (value: `"NA"`)

* `NAR` (value: `"NAR"`)

* `NCL` (value: `"NCL"`)

* `NEW` (value: `"NEW"`)

* `NF` (value: `"NF"`)

* `NIL` (value: `"NIL"`)

* `NIU` (value: `"NIU"`)

* `NL` (value: `"NL"`)

* `NM3` (value: `"NM3"`)

* `NMI` (value: `"NMI"`)

* `NMP` (value: `"NMP"`)

* `NPT` (value: `"NPT"`)

* `NT` (value: `"NT"`)

* `NU` (value: `"NU"`)

* `NX` (value: `"NX"`)

* `OA` (value: `"OA"`)

* `ODE` (value: `"ODE"`)

* `OHM` (value: `"OHM"`)

* `true` (value: `"true"`)

* `ONZ` (value: `"ONZ"`)

* `OPM` (value: `"OPM"`)

* `OT` (value: `"OT"`)

* `OZA` (value: `"OZA"`)

* `OZI` (value: `"OZI"`)

* `P1` (value: `"P1"`)

* `P10` (value: `"P10"`)

* `P11` (value: `"P11"`)

* `P12` (value: `"P12"`)

* `P13` (value: `"P13"`)

* `P14` (value: `"P14"`)

* `P15` (value: `"P15"`)

* `P16` (value: `"P16"`)

* `P17` (value: `"P17"`)

* `P18` (value: `"P18"`)

* `P19` (value: `"P19"`)

* `P2` (value: `"P2"`)

* `P20` (value: `"P20"`)

* `P21` (value: `"P21"`)

* `P22` (value: `"P22"`)

* `P23` (value: `"P23"`)

* `P24` (value: `"P24"`)

* `P25` (value: `"P25"`)

* `P26` (value: `"P26"`)

* `P27` (value: `"P27"`)

* `P28` (value: `"P28"`)

* `P29` (value: `"P29"`)

* `P30` (value: `"P30"`)

* `P31` (value: `"P31"`)

* `P32` (value: `"P32"`)

* `P33` (value: `"P33"`)

* `P34` (value: `"P34"`)

* `P35` (value: `"P35"`)

* `P36` (value: `"P36"`)

* `P37` (value: `"P37"`)

* `P38` (value: `"P38"`)

* `P39` (value: `"P39"`)

* `P40` (value: `"P40"`)

* `P41` (value: `"P41"`)

* `P42` (value: `"P42"`)

* `P43` (value: `"P43"`)

* `P44` (value: `"P44"`)

* `P45` (value: `"P45"`)

* `P46` (value: `"P46"`)

* `P47` (value: `"P47"`)

* `P48` (value: `"P48"`)

* `P49` (value: `"P49"`)

* `P5` (value: `"P5"`)

* `P50` (value: `"P50"`)

* `P51` (value: `"P51"`)

* `P52` (value: `"P52"`)

* `P53` (value: `"P53"`)

* `P54` (value: `"P54"`)

* `P55` (value: `"P55"`)

* `P56` (value: `"P56"`)

* `P57` (value: `"P57"`)

* `P58` (value: `"P58"`)

* `P59` (value: `"P59"`)

* `P60` (value: `"P60"`)

* `P61` (value: `"P61"`)

* `P62` (value: `"P62"`)

* `P63` (value: `"P63"`)

* `P64` (value: `"P64"`)

* `P65` (value: `"P65"`)

* `P66` (value: `"P66"`)

* `P67` (value: `"P67"`)

* `P68` (value: `"P68"`)

* `P69` (value: `"P69"`)

* `P70` (value: `"P70"`)

* `P71` (value: `"P71"`)

* `P72` (value: `"P72"`)

* `P73` (value: `"P73"`)

* `P74` (value: `"P74"`)

* `P75` (value: `"P75"`)

* `P76` (value: `"P76"`)

* `P77` (value: `"P77"`)

* `P78` (value: `"P78"`)

* `P79` (value: `"P79"`)

* `P80` (value: `"P80"`)

* `P81` (value: `"P81"`)

* `P82` (value: `"P82"`)

* `P83` (value: `"P83"`)

* `P84` (value: `"P84"`)

* `P85` (value: `"P85"`)

* `P86` (value: `"P86"`)

* `P87` (value: `"P87"`)

* `P88` (value: `"P88"`)

* `P89` (value: `"P89"`)

* `P90` (value: `"P90"`)

* `P91` (value: `"P91"`)

* `P92` (value: `"P92"`)

* `P93` (value: `"P93"`)

* `P94` (value: `"P94"`)

* `P95` (value: `"P95"`)

* `P96` (value: `"P96"`)

* `P97` (value: `"P97"`)

* `P98` (value: `"P98"`)

* `P99` (value: `"P99"`)

* `PAL` (value: `"PAL"`)

* `PD` (value: `"PD"`)

* `PFL` (value: `"PFL"`)

* `PGL` (value: `"PGL"`)

* `PI` (value: `"PI"`)

* `PLA` (value: `"PLA"`)

* `PO` (value: `"PO"`)

* `PQ` (value: `"PQ"`)

* `PR` (value: `"PR"`)

* `PS` (value: `"PS"`)

* `PTD` (value: `"PTD"`)

* `PTI` (value: `"PTI"`)

* `PTL` (value: `"PTL"`)

* `PTN` (value: `"PTN"`)

* `Q10` (value: `"Q10"`)

* `Q11` (value: `"Q11"`)

* `Q12` (value: `"Q12"`)

* `Q13` (value: `"Q13"`)

* `Q14` (value: `"Q14"`)

* `Q15` (value: `"Q15"`)

* `Q16` (value: `"Q16"`)

* `Q17` (value: `"Q17"`)

* `Q18` (value: `"Q18"`)

* `Q19` (value: `"Q19"`)

* `Q20` (value: `"Q20"`)

* `Q21` (value: `"Q21"`)

* `Q22` (value: `"Q22"`)

* `Q23` (value: `"Q23"`)

* `Q24` (value: `"Q24"`)

* `Q25` (value: `"Q25"`)

* `Q26` (value: `"Q26"`)

* `Q27` (value: `"Q27"`)

* `Q28` (value: `"Q28"`)

* `Q29` (value: `"Q29"`)

* `Q30` (value: `"Q30"`)

* `Q31` (value: `"Q31"`)

* `Q32` (value: `"Q32"`)

* `Q33` (value: `"Q33"`)

* `Q34` (value: `"Q34"`)

* `Q35` (value: `"Q35"`)

* `Q36` (value: `"Q36"`)

* `Q37` (value: `"Q37"`)

* `Q38` (value: `"Q38"`)

* `Q39` (value: `"Q39"`)

* `Q40` (value: `"Q40"`)

* `Q3` (value: `"Q3"`)

* `QA` (value: `"QA"`)

* `QAN` (value: `"QAN"`)

* `QB` (value: `"QB"`)

* `QR` (value: `"QR"`)

* `QTD` (value: `"QTD"`)

* `QTI` (value: `"QTI"`)

* `QTL` (value: `"QTL"`)

* `QTR` (value: `"QTR"`)

* `R1` (value: `"R1"`)

* `R9` (value: `"R9"`)

* `RH` (value: `"RH"`)

* `RM` (value: `"RM"`)

* `ROM` (value: `"ROM"`)

* `RP` (value: `"RP"`)

* `RPM` (value: `"RPM"`)

* `RPS` (value: `"RPS"`)

* `RT` (value: `"RT"`)

* `S3` (value: `"S3"`)

* `S4` (value: `"S4"`)

* `SAN` (value: `"SAN"`)

* `SCO` (value: `"SCO"`)

* `SCR` (value: `"SCR"`)

* `SEC` (value: `"SEC"`)

* `SET` (value: `"SET"`)

* `SG` (value: `"SG"`)

* `SIE` (value: `"SIE"`)

* `SM3` (value: `"SM3"`)

* `SMI` (value: `"SMI"`)

* `SQ` (value: `"SQ"`)

* `SQR` (value: `"SQR"`)

* `SR` (value: `"SR"`)

* `STC` (value: `"STC"`)

* `STI` (value: `"STI"`)

* `STK` (value: `"STK"`)

* `STL` (value: `"STL"`)

* `STN` (value: `"STN"`)

* `STW` (value: `"STW"`)

* `SW` (value: `"SW"`)

* `SX` (value: `"SX"`)

* `SYR` (value: `"SYR"`)

* `T0` (value: `"T0"`)

* `T3` (value: `"T3"`)

* `TAH` (value: `"TAH"`)

* `TAN` (value: `"TAN"`)

* `TI` (value: `"TI"`)

* `TIC` (value: `"TIC"`)

* `TIP` (value: `"TIP"`)

* `TKM` (value: `"TKM"`)

* `TMS` (value: `"TMS"`)

* `TNE` (value: `"TNE"`)

* `TP` (value: `"TP"`)

* `TPI` (value: `"TPI"`)

* `TPR` (value: `"TPR"`)

* `TQD` (value: `"TQD"`)

* `TRL` (value: `"TRL"`)

* `TST` (value: `"TST"`)

* `TTS` (value: `"TTS"`)

* `U1` (value: `"U1"`)

* `U2` (value: `"U2"`)

* `UB` (value: `"UB"`)

* `UC` (value: `"UC"`)

* `VA` (value: `"VA"`)

* `VLT` (value: `"VLT"`)

* `VP` (value: `"VP"`)

* `W2` (value: `"W2"`)

* `WA` (value: `"WA"`)

* `WB` (value: `"WB"`)

* `WCD` (value: `"WCD"`)

* `WE` (value: `"WE"`)

* `WEB` (value: `"WEB"`)

* `WEE` (value: `"WEE"`)

* `WG` (value: `"WG"`)

* `WHR` (value: `"WHR"`)

* `WM` (value: `"WM"`)

* `WSD` (value: `"WSD"`)

* `WTT` (value: `"WTT"`)

* `X1` (value: `"X1"`)

* `YDK` (value: `"YDK"`)

* `YDQ` (value: `"YDQ"`)

* `YRD` (value: `"YRD"`)

* `Z11` (value: `"Z11"`)

* `ZP` (value: `"ZP"`)

* `ZZ` (value: `"ZZ"`)

* `X1A` (value: `"X1A"`)

* `X1B` (value: `"X1B"`)

* `X1D` (value: `"X1D"`)

* `X1F` (value: `"X1F"`)

* `X1G` (value: `"X1G"`)

* `X1W` (value: `"X1W"`)

* `X2C` (value: `"X2C"`)

* `X3A` (value: `"X3A"`)

* `X3H` (value: `"X3H"`)

* `X43` (value: `"X43"`)

* `X44` (value: `"X44"`)

* `X4A` (value: `"X4A"`)

* `X4B` (value: `"X4B"`)

* `X4C` (value: `"X4C"`)

* `X4D` (value: `"X4D"`)

* `X4F` (value: `"X4F"`)

* `X4G` (value: `"X4G"`)

* `X4H` (value: `"X4H"`)

* `X5H` (value: `"X5H"`)

* `X5L` (value: `"X5L"`)

* `X5M` (value: `"X5M"`)

* `X6H` (value: `"X6H"`)

* `X6P` (value: `"X6P"`)

* `X7A` (value: `"X7A"`)

* `X7B` (value: `"X7B"`)

* `X8A` (value: `"X8A"`)

* `X8B` (value: `"X8B"`)

* `X8C` (value: `"X8C"`)

* `XAA` (value: `"XAA"`)

* `XAB` (value: `"XAB"`)

* `XAC` (value: `"XAC"`)

* `XAD` (value: `"XAD"`)

* `XAE` (value: `"XAE"`)

* `XAF` (value: `"XAF"`)

* `XAG` (value: `"XAG"`)

* `XAH` (value: `"XAH"`)

* `XAI` (value: `"XAI"`)

* `XAJ` (value: `"XAJ"`)

* `XAL` (value: `"XAL"`)

* `XAM` (value: `"XAM"`)

* `XAP` (value: `"XAP"`)

* `XAT` (value: `"XAT"`)

* `XAV` (value: `"XAV"`)

* `XB4` (value: `"XB4"`)

* `XBA` (value: `"XBA"`)

* `XBB` (value: `"XBB"`)

* `XBC` (value: `"XBC"`)

* `XBD` (value: `"XBD"`)

* `XBE` (value: `"XBE"`)

* `XBF` (value: `"XBF"`)

* `XBG` (value: `"XBG"`)

* `XBH` (value: `"XBH"`)

* `XBI` (value: `"XBI"`)

* `XBJ` (value: `"XBJ"`)

* `XBK` (value: `"XBK"`)

* `XBL` (value: `"XBL"`)

* `XBM` (value: `"XBM"`)

* `XBN` (value: `"XBN"`)

* `XBO` (value: `"XBO"`)

* `XBP` (value: `"XBP"`)

* `XBQ` (value: `"XBQ"`)

* `XBR` (value: `"XBR"`)

* `XBS` (value: `"XBS"`)

* `XBT` (value: `"XBT"`)

* `XBU` (value: `"XBU"`)

* `XBV` (value: `"XBV"`)

* `XBW` (value: `"XBW"`)

* `XBX` (value: `"XBX"`)

* `XBY` (value: `"XBY"`)

* `XBZ` (value: `"XBZ"`)

* `XCA` (value: `"XCA"`)

* `XCB` (value: `"XCB"`)

* `XCC` (value: `"XCC"`)

* `XCD` (value: `"XCD"`)

* `XCE` (value: `"XCE"`)

* `XCF` (value: `"XCF"`)

* `XCG` (value: `"XCG"`)

* `XCH` (value: `"XCH"`)

* `XCI` (value: `"XCI"`)

* `XCJ` (value: `"XCJ"`)

* `XCK` (value: `"XCK"`)

* `XCL` (value: `"XCL"`)

* `XCM` (value: `"XCM"`)

* `XCN` (value: `"XCN"`)

* `XCO` (value: `"XCO"`)

* `XCP` (value: `"XCP"`)

* `XCQ` (value: `"XCQ"`)

* `XCR` (value: `"XCR"`)

* `XCS` (value: `"XCS"`)

* `XCT` (value: `"XCT"`)

* `XCU` (value: `"XCU"`)

* `XCV` (value: `"XCV"`)

* `XCW` (value: `"XCW"`)

* `XCX` (value: `"XCX"`)

* `XCY` (value: `"XCY"`)

* `XCZ` (value: `"XCZ"`)

* `XDA` (value: `"XDA"`)

* `XDB` (value: `"XDB"`)

* `XDC` (value: `"XDC"`)

* `XDG` (value: `"XDG"`)

* `XDH` (value: `"XDH"`)

* `XDI` (value: `"XDI"`)

* `XDJ` (value: `"XDJ"`)

* `XDK` (value: `"XDK"`)

* `XDL` (value: `"XDL"`)

* `XDM` (value: `"XDM"`)

* `XDN` (value: `"XDN"`)

* `XDP` (value: `"XDP"`)

* `XDR` (value: `"XDR"`)

* `XDS` (value: `"XDS"`)

* `XDT` (value: `"XDT"`)

* `XDU` (value: `"XDU"`)

* `XDV` (value: `"XDV"`)

* `XDW` (value: `"XDW"`)

* `XDX` (value: `"XDX"`)

* `XDY` (value: `"XDY"`)

* `XEC` (value: `"XEC"`)

* `XED` (value: `"XED"`)

* `XEE` (value: `"XEE"`)

* `XEF` (value: `"XEF"`)

* `XEG` (value: `"XEG"`)

* `XEH` (value: `"XEH"`)

* `XEI` (value: `"XEI"`)

* `XEN` (value: `"XEN"`)

* `XFB` (value: `"XFB"`)

* `XFC` (value: `"XFC"`)

* `XFD` (value: `"XFD"`)

* `XFE` (value: `"XFE"`)

* `XFI` (value: `"XFI"`)

* `XFL` (value: `"XFL"`)

* `XFO` (value: `"XFO"`)

* `XFP` (value: `"XFP"`)

* `XFR` (value: `"XFR"`)

* `XFT` (value: `"XFT"`)

* `XFW` (value: `"XFW"`)

* `XFX` (value: `"XFX"`)

* `XGB` (value: `"XGB"`)

* `XGI` (value: `"XGI"`)

* `XGL` (value: `"XGL"`)

* `XGR` (value: `"XGR"`)

* `XGU` (value: `"XGU"`)

* `XGY` (value: `"XGY"`)

* `XGZ` (value: `"XGZ"`)

* `XHA` (value: `"XHA"`)

* `XHB` (value: `"XHB"`)

* `XHC` (value: `"XHC"`)

* `XHG` (value: `"XHG"`)

* `XHN` (value: `"XHN"`)

* `XHR` (value: `"XHR"`)

* `XIA` (value: `"XIA"`)

* `XIB` (value: `"XIB"`)

* `XIC` (value: `"XIC"`)

* `XID` (value: `"XID"`)

* `XIE` (value: `"XIE"`)

* `XIF` (value: `"XIF"`)

* `XIG` (value: `"XIG"`)

* `XIH` (value: `"XIH"`)

* `XIK` (value: `"XIK"`)

* `XIL` (value: `"XIL"`)

* `XIN` (value: `"XIN"`)

* `XIZ` (value: `"XIZ"`)

* `XJB` (value: `"XJB"`)

* `XJC` (value: `"XJC"`)

* `XJG` (value: `"XJG"`)

* `XJR` (value: `"XJR"`)

* `XJT` (value: `"XJT"`)

* `XJY` (value: `"XJY"`)

* `XKG` (value: `"XKG"`)

* `XKI` (value: `"XKI"`)

* `XLE` (value: `"XLE"`)

* `XLG` (value: `"XLG"`)

* `XLT` (value: `"XLT"`)

* `XLU` (value: `"XLU"`)

* `XLV` (value: `"XLV"`)

* `XLZ` (value: `"XLZ"`)

* `XMA` (value: `"XMA"`)

* `XMB` (value: `"XMB"`)

* `XMC` (value: `"XMC"`)

* `XME` (value: `"XME"`)

* `XMR` (value: `"XMR"`)

* `XMS` (value: `"XMS"`)

* `XMT` (value: `"XMT"`)

* `XMW` (value: `"XMW"`)

* `XMX` (value: `"XMX"`)

* `XNA` (value: `"XNA"`)

* `XNE` (value: `"XNE"`)

* `XNF` (value: `"XNF"`)

* `XNG` (value: `"XNG"`)

* `XNS` (value: `"XNS"`)

* `XNT` (value: `"XNT"`)

* `XNU` (value: `"XNU"`)

* `XNV` (value: `"XNV"`)

* `XOA` (value: `"XOA"`)

* `XOB` (value: `"XOB"`)

* `XOC` (value: `"XOC"`)

* `XOD` (value: `"XOD"`)

* `XOE` (value: `"XOE"`)

* `XOF` (value: `"XOF"`)

* `XOK` (value: `"XOK"`)

* `XOT` (value: `"XOT"`)

* `XOU` (value: `"XOU"`)

* `XP2` (value: `"XP2"`)

* `XPA` (value: `"XPA"`)

* `XPB` (value: `"XPB"`)

* `XPC` (value: `"XPC"`)

* `XPD` (value: `"XPD"`)

* `XPE` (value: `"XPE"`)

* `XPF` (value: `"XPF"`)

* `XPG` (value: `"XPG"`)

* `XPH` (value: `"XPH"`)

* `XPI` (value: `"XPI"`)

* `XPJ` (value: `"XPJ"`)

* `XPK` (value: `"XPK"`)

* `XPL` (value: `"XPL"`)

* `XPN` (value: `"XPN"`)

* `XPO` (value: `"XPO"`)

* `XPP` (value: `"XPP"`)

* `XPR` (value: `"XPR"`)

* `XPT` (value: `"XPT"`)

* `XPU` (value: `"XPU"`)

* `XPV` (value: `"XPV"`)

* `XPX` (value: `"XPX"`)

* `XPY` (value: `"XPY"`)

* `XPZ` (value: `"XPZ"`)

* `XQA` (value: `"XQA"`)

* `XQB` (value: `"XQB"`)

* `XQC` (value: `"XQC"`)

* `XQD` (value: `"XQD"`)

* `XQF` (value: `"XQF"`)

* `XQG` (value: `"XQG"`)

* `XQH` (value: `"XQH"`)

* `XQJ` (value: `"XQJ"`)

* `XQK` (value: `"XQK"`)

* `XQL` (value: `"XQL"`)

* `XQM` (value: `"XQM"`)

* `XQN` (value: `"XQN"`)

* `XQP` (value: `"XQP"`)

* `XQQ` (value: `"XQQ"`)

* `XQR` (value: `"XQR"`)

* `XQS` (value: `"XQS"`)

* `XRD` (value: `"XRD"`)

* `XRG` (value: `"XRG"`)

* `XRJ` (value: `"XRJ"`)

* `XRK` (value: `"XRK"`)

* `XRL` (value: `"XRL"`)

* `XRO` (value: `"XRO"`)

* `XRT` (value: `"XRT"`)

* `XRZ` (value: `"XRZ"`)

* `XSA` (value: `"XSA"`)

* `XSB` (value: `"XSB"`)

* `XSC` (value: `"XSC"`)

* `XSD` (value: `"XSD"`)

* `XSE` (value: `"XSE"`)

* `XSH` (value: `"XSH"`)

* `XSI` (value: `"XSI"`)

* `XSK` (value: `"XSK"`)

* `XSL` (value: `"XSL"`)

* `XSM` (value: `"XSM"`)

* `XSO` (value: `"XSO"`)

* `XSP` (value: `"XSP"`)

* `XSS` (value: `"XSS"`)

* `XST` (value: `"XST"`)

* `XSU` (value: `"XSU"`)

* `XSV` (value: `"XSV"`)

* `XSW` (value: `"XSW"`)

* `XSY` (value: `"XSY"`)

* `XSZ` (value: `"XSZ"`)

* `XT1` (value: `"XT1"`)

* `XTB` (value: `"XTB"`)

* `XTC` (value: `"XTC"`)

* `XTD` (value: `"XTD"`)

* `XTE` (value: `"XTE"`)

* `XTG` (value: `"XTG"`)

* `XTI` (value: `"XTI"`)

* `XTK` (value: `"XTK"`)

* `XTL` (value: `"XTL"`)

* `XTN` (value: `"XTN"`)

* `XTO` (value: `"XTO"`)

* `XTR` (value: `"XTR"`)

* `XTS` (value: `"XTS"`)

* `XTT` (value: `"XTT"`)

* `XTU` (value: `"XTU"`)

* `XTV` (value: `"XTV"`)

* `XTW` (value: `"XTW"`)

* `XTY` (value: `"XTY"`)

* `XTZ` (value: `"XTZ"`)

* `XUC` (value: `"XUC"`)

* `XUN` (value: `"XUN"`)

* `XVA` (value: `"XVA"`)

* `XVG` (value: `"XVG"`)

* `XVI` (value: `"XVI"`)

* `XVK` (value: `"XVK"`)

* `XVL` (value: `"XVL"`)

* `XVO` (value: `"XVO"`)

* `XVP` (value: `"XVP"`)

* `XVQ` (value: `"XVQ"`)

* `XVN` (value: `"XVN"`)

* `XVR` (value: `"XVR"`)

* `XVS` (value: `"XVS"`)

* `XVY` (value: `"XVY"`)

* `XWA` (value: `"XWA"`)

* `XWB` (value: `"XWB"`)

* `XWC` (value: `"XWC"`)

* `XWD` (value: `"XWD"`)

* `XWF` (value: `"XWF"`)

* `XWG` (value: `"XWG"`)

* `XWH` (value: `"XWH"`)

* `XWJ` (value: `"XWJ"`)

* `XWK` (value: `"XWK"`)

* `XWL` (value: `"XWL"`)

* `XWM` (value: `"XWM"`)

* `XWN` (value: `"XWN"`)

* `XWP` (value: `"XWP"`)

* `XWQ` (value: `"XWQ"`)

* `XWR` (value: `"XWR"`)

* `XWS` (value: `"XWS"`)

* `XWT` (value: `"XWT"`)

* `XWU` (value: `"XWU"`)

* `XWV` (value: `"XWV"`)

* `XWW` (value: `"XWW"`)

* `XWX` (value: `"XWX"`)

* `XWY` (value: `"XWY"`)

* `XWZ` (value: `"XWZ"`)

* `XXA` (value: `"XXA"`)

* `XXB` (value: `"XXB"`)

* `XXC` (value: `"XXC"`)

* `XXD` (value: `"XXD"`)

* `XXF` (value: `"XXF"`)

* `XXG` (value: `"XXG"`)

* `XXH` (value: `"XXH"`)

* `XXJ` (value: `"XXJ"`)

* `XXK` (value: `"XXK"`)

* `XYA` (value: `"XYA"`)

* `XYB` (value: `"XYB"`)

* `XYC` (value: `"XYC"`)

* `XYD` (value: `"XYD"`)

* `XYF` (value: `"XYF"`)

* `XYG` (value: `"XYG"`)

* `XYH` (value: `"XYH"`)

* `XYJ` (value: `"XYJ"`)

* `XYK` (value: `"XYK"`)

* `XYL` (value: `"XYL"`)

* `XYM` (value: `"XYM"`)

* `XYN` (value: `"XYN"`)

* `XYP` (value: `"XYP"`)

* `XYQ` (value: `"XYQ"`)

* `XYR` (value: `"XYR"`)

* `XYS` (value: `"XYS"`)

* `XYT` (value: `"XYT"`)

* `XYV` (value: `"XYV"`)

* `XYW` (value: `"XYW"`)

* `XYX` (value: `"XYX"`)

* `XYY` (value: `"XYY"`)

* `XYZ` (value: `"XYZ"`)

* `XZA` (value: `"XZA"`)

* `XZB` (value: `"XZB"`)

* `XZC` (value: `"XZC"`)

* `XZD` (value: `"XZD"`)

* `XZF` (value: `"XZF"`)

* `XZG` (value: `"XZG"`)

* `XZH` (value: `"XZH"`)

* `XZJ` (value: `"XZJ"`)

* `XZK` (value: `"XZK"`)

* `XZL` (value: `"XZL"`)

* `XZM` (value: `"XZM"`)

* `XZN` (value: `"XZN"`)

* `XZP` (value: `"XZP"`)

* `XZQ` (value: `"XZQ"`)

* `XZR` (value: `"XZR"`)

* `XZS` (value: `"XZS"`)

* `XZT` (value: `"XZT"`)

* `XZU` (value: `"XZU"`)

* `XZV` (value: `"XZV"`)

* `XZW` (value: `"XZW"`)

* `XZX` (value: `"XZX"`)

* `XZY` (value: `"XZY"`)

* `XZZ` (value: `"XZZ"`)

* `04` (value: `"04"`)

* `05` (value: `"05"`)

* `08` (value: `"08"`)

* `16` (value: `"16"`)

* `17` (value: `"17"`)

* `18` (value: `"18"`)

* `19` (value: `"19"`)

* `26` (value: `"26"`)

* `29` (value: `"29"`)

* `30` (value: `"30"`)

* `31` (value: `"31"`)

* `32` (value: `"32"`)

* `36` (value: `"36"`)

* `43` (value: `"43"`)

* `44` (value: `"44"`)

* `45` (value: `"45"`)

* `46` (value: `"46"`)

* `47` (value: `"47"`)

* `48` (value: `"48"`)

* `53` (value: `"53"`)

* `54` (value: `"54"`)

* `62` (value: `"62"`)

* `63` (value: `"63"`)

* `64` (value: `"64"`)

* `66` (value: `"66"`)

* `69` (value: `"69"`)

* `71` (value: `"71"`)

* `72` (value: `"72"`)

* `73` (value: `"73"`)

* `76` (value: `"76"`)

* `78` (value: `"78"`)

* `84` (value: `"84"`)

* `90` (value: `"90"`)

* `92` (value: `"92"`)

* `93` (value: `"93"`)

* `94` (value: `"94"`)

* `95` (value: `"95"`)

* `96` (value: `"96"`)

* `97` (value: `"97"`)

* `98` (value: `"98"`)

* `1A` (value: `"1A"`)

* `1B` (value: `"1B"`)

* `1C` (value: `"1C"`)

* `1D` (value: `"1D"`)

* `1E` (value: `"1E"`)

* `1F` (value: `"1F"`)

* `1G` (value: `"1G"`)

* `1H` (value: `"1H"`)

* `1J` (value: `"1J"`)

* `1K` (value: `"1K"`)

* `1L` (value: `"1L"`)

* `1M` (value: `"1M"`)

* `1X` (value: `"1X"`)

* `2V` (value: `"2V"`)

* `2W` (value: `"2W"`)

* `3E` (value: `"3E"`)

* `3G` (value: `"3G"`)

* `3H` (value: `"3H"`)

* `3I` (value: `"3I"`)

* `4A` (value: `"4A"`)

* `4B` (value: `"4B"`)

* `4E` (value: `"4E"`)

* `5C` (value: `"5C"`)

* `5F` (value: `"5F"`)

* `5G` (value: `"5G"`)

* `5H` (value: `"5H"`)

* `5I` (value: `"5I"`)

* `5K` (value: `"5K"`)

* `5P` (value: `"5P"`)

* `5Q` (value: `"5Q"`)

* `A1` (value: `"A1"`)

* `A25` (value: `"A25"`)

* `A50` (value: `"A50"`)

* `A51` (value: `"A51"`)

* `A52` (value: `"A52"`)

* `A57` (value: `"A57"`)

* `A58` (value: `"A58"`)

* `A60` (value: `"A60"`)

* `A61` (value: `"A61"`)

* `A62` (value: `"A62"`)

* `A63` (value: `"A63"`)

* `A64` (value: `"A64"`)

* `A65` (value: `"A65"`)

* `A66` (value: `"A66"`)

* `A67` (value: `"A67"`)

* `A77` (value: `"A77"`)

* `A78` (value: `"A78"`)

* `A79` (value: `"A79"`)

* `A80` (value: `"A80"`)

* `A81` (value: `"A81"`)

* `A82` (value: `"A82"`)

* `A83` (value: `"A83"`)

* `AJ` (value: `"AJ"`)

* `AM` (value: `"AM"`)

* `AP` (value: `"AP"`)

* `AR` (value: `"AR"`)

* `ARE` (value: `"ARE"`)

* `ATT` (value: `"ATT"`)

* `AV` (value: `"AV"`)

* `AW` (value: `"AW"`)

* `B0` (value: `"B0"`)

* `B2` (value: `"B2"`)

* `B36` (value: `"B36"`)

* `B37` (value: `"B37"`)

* `B38` (value: `"B38"`)

* `B39` (value: `"B39"`)

* `B40` (value: `"B40"`)

* `B5` (value: `"B5"`)

* `B51` (value: `"B51"`)

* `B6` (value: `"B6"`)

* `B65` (value: `"B65"`)

* `B9` (value: `"B9"`)

* `BD` (value: `"BD"`)

* `BE` (value: `"BE"`)

* `BG` (value: `"BG"`)

* `BH` (value: `"BH"`)

* `BJ` (value: `"BJ"`)

* `BK` (value: `"BK"`)

* `BL` (value: `"BL"`)

* `BO` (value: `"BO"`)

* `BR` (value: `"BR"`)

* `BT` (value: `"BT"`)

* `BW` (value: `"BW"`)

* `BX` (value: `"BX"`)

* `BZ` (value: `"BZ"`)

* `C1` (value: `"C1"`)

* `C2` (value: `"C2"`)

* `C4` (value: `"C4"`)

* `C5` (value: `"C5"`)

* `C6` (value: `"C6"`)

* `C77` (value: `"C77"`)

* `C98` (value: `"C98"`)

* `CA` (value: `"CA"`)

* `CH` (value: `"CH"`)

* `CJ` (value: `"CJ"`)

* `CK` (value: `"CK"`)

* `CL` (value: `"CL"`)

* `CO` (value: `"CO"`)

* `CQ` (value: `"CQ"`)

* `CR` (value: `"CR"`)

* `CS` (value: `"CS"`)

* `CT` (value: `"CT"`)

* `CU` (value: `"CU"`)

* `CV` (value: `"CV"`)

* `CY` (value: `"CY"`)

* `CZ` (value: `"CZ"`)

* `D14` (value: `"D14"`)

* `D28` (value: `"D28"`)

* `D35` (value: `"D35"`)

* `D37` (value: `"D37"`)

* `D38` (value: `"D38"`)

* `D39` (value: `"D39"`)

* `D40` (value: `"D40"`)

* `D64` (value: `"D64"`)

* `D66` (value: `"D66"`)

* `D67` (value: `"D67"`)

* `D7` (value: `"D7"`)

* `D70` (value: `"D70"`)

* `D71` (value: `"D71"`)

* `D72` (value: `"D72"`)

* `D75` (value: `"D75"`)

* `D76` (value: `"D76"`)

* `D79` (value: `"D79"`)

* `D8` (value: `"D8"`)

* `D9` (value: `"D9"`)

* `D90` (value: `"D90"`)

* `D92` (value: `"D92"`)

* `D96` (value: `"D96"`)

* `D97` (value: `"D97"`)

* `D98` (value: `"D98"`)

* `D99` (value: `"D99"`)

* `DC` (value: `"DC"`)

* `DE` (value: `"DE"`)

* `DI` (value: `"DI"`)

* `DQ` (value: `"DQ"`)

* `DR` (value: `"DR"`)

* `DRM` (value: `"DRM"`)

* `DS` (value: `"DS"`)

* `DU` (value: `"DU"`)

* `DX` (value: `"DX"`)

* `DY` (value: `"DY"`)

* `E2` (value: `"E2"`)

* `E3` (value: `"E3"`)

* `E5` (value: `"E5"`)

* `EC` (value: `"EC"`)

* `EP` (value: `"EP"`)

* `EV` (value: `"EV"`)

* `F1` (value: `"F1"`)

* `F9` (value: `"F9"`)

* `FB` (value: `"FB"`)

* `FD` (value: `"FD"`)

* `FE` (value: `"FE"`)

* `FG` (value: `"FG"`)

* `FM` (value: `"FM"`)

* `G7` (value: `"G7"`)

* `GC` (value: `"GC"`)

* `GD` (value: `"GD"`)

* `GH` (value: `"GH"`)

* `GK` (value: `"GK"`)

* `GN` (value: `"GN"`)

* `GRT` (value: `"GRT"`)

* `GT` (value: `"GT"`)

* `GW` (value: `"GW"`)

* `GY` (value: `"GY"`)

* `GZ` (value: `"GZ"`)

* `H1` (value: `"H1"`)

* `H2` (value: `"H2"`)

* `HAR` (value: `"HAR"`)

* `HD` (value: `"HD"`)

* `HE` (value: `"HE"`)

* `HF` (value: `"HF"`)

* `HI` (value: `"HI"`)

* `HJ` (value: `"HJ"`)

* `HK` (value: `"HK"`)

* `HL` (value: `"HL"`)

* `HN` (value: `"HN"`)

* `HO` (value: `"HO"`)

* `HP` (value: `"HP"`)

* `HS` (value: `"HS"`)

* `HT` (value: `"HT"`)

* `HY` (value: `"HY"`)

* `IC` (value: `"IC"`)

* `IF` (value: `"IF"`)

* `II` (value: `"II"`)

* `IL` (value: `"IL"`)

* `IM` (value: `"IM"`)

* `IP` (value: `"IP"`)

* `IT` (value: `"IT"`)

* `JB` (value: `"JB"`)

* `JG` (value: `"JG"`)

* `JO` (value: `"JO"`)

* `JR` (value: `"JR"`)

* `K5` (value: `"K5"`)

* `KD` (value: `"KD"`)

* `KF` (value: `"KF"`)

* `KG` (value: `"KG"`)

* `KS` (value: `"KS"`)

* `KTM` (value: `"KTM"`)

* `LC` (value: `"LC"`)

* `LE` (value: `"LE"`)

* `LI` (value: `"LI"`)

* `LJ` (value: `"LJ"`)

* `LX` (value: `"LX"`)

* `M0` (value: `"M0"`)

* `MA` (value: `"MA"`)

* `MF` (value: `"MF"`)

* `MK` (value: `"MK"`)

* `MQ` (value: `"MQ"`)

* `MT` (value: `"MT"`)

* `MV` (value: `"MV"`)

* `N2` (value: `"N2"`)

* `NB` (value: `"NB"`)

* `NBB` (value: `"NBB"`)

* `NC` (value: `"NC"`)

* `ND` (value: `"ND"`)

* `NE` (value: `"NE"`)

* `NG` (value: `"NG"`)

* `NH` (value: `"NH"`)

* `NI` (value: `"NI"`)

* `NJ` (value: `"NJ"`)

* `NN` (value: `"NN"`)

* `NPL` (value: `"NPL"`)

* `NPR` (value: `"NPR"`)

* `NQ` (value: `"NQ"`)

* `NR` (value: `"NR"`)

* `NRL` (value: `"NRL"`)

* `NTT` (value: `"NTT"`)

* `NV` (value: `"NV"`)

* `NY` (value: `"NY"`)

* `OP` (value: `"OP"`)

* `OZ` (value: `"OZ"`)

* `P0` (value: `"P0"`)

* `P3` (value: `"P3"`)

* `P4` (value: `"P4"`)

* `P6` (value: `"P6"`)

* `P7` (value: `"P7"`)

* `P8` (value: `"P8"`)

* `P9` (value: `"P9"`)

* `PA` (value: `"PA"`)

* `PB` (value: `"PB"`)

* `PE` (value: `"PE"`)

* `PF` (value: `"PF"`)

* `PG` (value: `"PG"`)

* `PK` (value: `"PK"`)

* `PL` (value: `"PL"`)

* `PM` (value: `"PM"`)

* `PN` (value: `"PN"`)

* `PT` (value: `"PT"`)

* `PU` (value: `"PU"`)

* `PV` (value: `"PV"`)

* `PW` (value: `"PW"`)

* `PY` (value: `"PY"`)

* `PZ` (value: `"PZ"`)

* `QD` (value: `"QD"`)

* `QH` (value: `"QH"`)

* `QK` (value: `"QK"`)

* `QT` (value: `"QT"`)

* `R4` (value: `"R4"`)

* `RA` (value: `"RA"`)

* `RD` (value: `"RD"`)

* `RG` (value: `"RG"`)

* `RK` (value: `"RK"`)

* `RL` (value: `"RL"`)

* `RN` (value: `"RN"`)

* `RO` (value: `"RO"`)

* `RS` (value: `"RS"`)

* `RU` (value: `"RU"`)

* `S5` (value: `"S5"`)

* `S6` (value: `"S6"`)

* `S7` (value: `"S7"`)

* `S8` (value: `"S8"`)

* `SA` (value: `"SA"`)

* `SD` (value: `"SD"`)

* `SE` (value: `"SE"`)

* `SHT` (value: `"SHT"`)

* `SK` (value: `"SK"`)

* `SL` (value: `"SL"`)

* `SN` (value: `"SN"`)

* `SO` (value: `"SO"`)

* `SP` (value: `"SP"`)

* `SS` (value: `"SS"`)

* `SST` (value: `"SST"`)

* `ST` (value: `"ST"`)

* `SV` (value: `"SV"`)

* `T1` (value: `"T1"`)

* `T4` (value: `"T4"`)

* `T5` (value: `"T5"`)

* `T6` (value: `"T6"`)

* `T7` (value: `"T7"`)

* `T8` (value: `"T8"`)

* `TA` (value: `"TA"`)

* `TC` (value: `"TC"`)

* `TD` (value: `"TD"`)

* `TE` (value: `"TE"`)

* `TF` (value: `"TF"`)

* `TJ` (value: `"TJ"`)

* `TK` (value: `"TK"`)

* `TL` (value: `"TL"`)

* `TN` (value: `"TN"`)

* `TQ` (value: `"TQ"`)

* `TR` (value: `"TR"`)

* `TS` (value: `"TS"`)

* `TSD` (value: `"TSD"`)

* `TSH` (value: `"TSH"`)

* `TT` (value: `"TT"`)

* `TU` (value: `"TU"`)

* `TV` (value: `"TV"`)

* `TW` (value: `"TW"`)

* `TY` (value: `"TY"`)

* `UA` (value: `"UA"`)

* `UD` (value: `"UD"`)

* `UE` (value: `"UE"`)

* `UF` (value: `"UF"`)

* `UH` (value: `"UH"`)

* `UM` (value: `"UM"`)

* `VI` (value: `"VI"`)

* `VQ` (value: `"VQ"`)

* `VS` (value: `"VS"`)

* `W4` (value: `"W4"`)

* `WH` (value: `"WH"`)

* `WI` (value: `"WI"`)

* `WR` (value: `"WR"`)

* `WW` (value: `"WW"`)

* `YL` (value: `"YL"`)

* `YT` (value: `"YT"`)

* `Z1` (value: `"Z1"`)

* `Z2` (value: `"Z2"`)

* `Z3` (value: `"Z3"`)

* `Z4` (value: `"Z4"`)

* `Z5` (value: `"Z5"`)

* `Z6` (value: `"Z6"`)

* `Z8` (value: `"Z8"`)




