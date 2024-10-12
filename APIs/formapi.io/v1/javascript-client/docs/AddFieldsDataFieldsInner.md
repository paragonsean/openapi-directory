# ApiV1.AddFieldsDataFieldsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | **String** |  | [optional] 
**autoCalculateMaxLength** | **Boolean** |  | [optional] 
**backgroundColor** | **String** |  | [optional] 
**backgroundColorFieldName** | **String** |  | [optional] 
**backgroundColorFieldRequired** | **Boolean** |  | [optional] 
**barcodeSymbology** | **String** |  | [optional] 
**bold** | **Boolean** |  | [optional] 
**characterSpacing** | **Number** |  | [optional] 
**checkCharacter** | **String** |  | [optional] 
**checkColor** | **String** |  | [optional] 
**checkColorFieldName** | **String** |  | [optional] 
**checkColorFieldRequired** | **Boolean** |  | [optional] 
**color** | **String** |  | [optional] 
**colorFieldName** | **String** |  | [optional] 
**colorFieldRequired** | **Boolean** |  | [optional] 
**comb** | **Boolean** |  | [optional] 
**combNumberOfCells** | **Number** |  | [optional] 
**combValueOffset** | **Number** |  | [optional] 
**combinedFieldFormat** | **String** |  | [optional] 
**combinedFieldNames** | **String** |  | [optional] 
**combinedFieldSeparator** | **String** |  | [optional] 
**combinedFieldType** | **String** |  | [optional] 
**condition** | **String** |  | [optional] 
**currency** | **Boolean** |  | [optional] 
**dateTimeFormat** | **String** |  | [optional] 
**decimalPlaces** | **Number** |  | [optional] 
**_default** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**displayType** | **String** |  | [optional] 
**exclusiveMaximum** | **Boolean** |  | [optional] 
**exclusiveMinimum** | **Boolean** |  | [optional] 
**falseText** | **String** |  | [optional] 
**fontSize** | **Number** |  | [optional] 
**height** | **Number** |  | [optional] 
**hidden** | **Boolean** |  | [optional] 
**id** | **Number** |  | [optional] 
**imageGravity** | **String** |  | [optional] 
**imageScaleType** | **String** |  | [optional] 
**includeTime** | **Boolean** |  | [optional] 
**integer** | **Boolean** |  | [optional] 
**invertBooleanCondition** | **Boolean** |  | [optional] 
**maxLength** | **Number** |  | [optional] 
**maximum** | **Number** |  | [optional] 
**metadata** | **String** |  | [optional] 
**minLength** | **Number** |  | [optional] 
**minimum** | **Number** |  | [optional] 
**multiline** | **Boolean** |  | [optional] 
**multilineLines** | **Number** |  | [optional] 
**name** | **String** |  | 
**numberConditionRangeExclusiveMax** | **Boolean** |  | [optional] 
**numberConditionRangeExclusiveMin** | **Boolean** |  | [optional] 
**numberConditionRangeMax** | **Number** |  | [optional] 
**numberConditionRangeMin** | **Number** |  | [optional] 
**numberConditionType** | **String** |  | [optional] 
**opacity** | **Number** |  | [optional] 
**optionList** | **String** |  | [optional] 
**overflow** | **String** |  | [optional] 
**page** | **Number** |  | 
**placeholder** | **String** |  | [optional] 
**qrcodeColor** | **String** |  | [optional] 
**qrcodeColorFieldName** | **String** |  | [optional] 
**qrcodeColorFieldRequired** | **Boolean** |  | [optional] 
**required** | **Boolean** |  | [optional] 
**rotation** | **Number** |  | [optional] 
**shapeBorderColor** | **String** |  | [optional] 
**shapeBorderColorFieldName** | **String** |  | [optional] 
**shapeBorderColorFieldRequired** | **Boolean** |  | [optional] 
**shapeBorderWidth** | **Number** |  | [optional] 
**shapeFillColor** | **String** |  | [optional] 
**shapeFillColorFieldName** | **String** |  | [optional] 
**shapeFillColorFieldRequired** | **Boolean** |  | [optional] 
**shapeType** | **String** |  | [optional] 
**signatureAllowDraw** | **Boolean** |  | [optional] 
**signatureAllowType** | **Boolean** |  | [optional] 
**_static** | **Boolean** |  | [optional] 
**strikethrough** | **Boolean** |  | [optional] 
**stringConditionType** | **String** |  | [optional] 
**title** | **String** |  | [optional] 
**trueText** | **String** |  | [optional] 
**type** | **String** |  | [optional] 
**typeface** | **String** |  | [optional] 
**uppercase** | **Boolean** |  | [optional] 
**vAlignment** | **String** |  | [optional] 
**width** | **Number** |  | [optional] 
**x** | **Number** |  | [optional] 
**y** | **Number** |  | [optional] 



## Enum: AlignmentEnum


* `left` (value: `"left"`)

* `center` (value: `"center"`)

* `right` (value: `"right"`)





## Enum: CheckCharacterEnum


* `10003;` (value: `"&#10003;"`)

* `10004;` (value: `"&#10004;"`)

* `10006;` (value: `"&#10006;"`)

* `10007;` (value: `"&#10007;"`)

* `10008;` (value: `"&#10008;"`)





## Enum: DisplayTypeEnum


* `text` (value: `"text"`)

* `check` (value: `"check"`)

* `qrcode` (value: `"qrcode"`)

* `barcode` (value: `"barcode"`)

* `image` (value: `"image"`)

* `shape` (value: `"shape"`)





## Enum: ImageGravityEnum


* `NorthWest` (value: `"NorthWest"`)

* `North` (value: `"North"`)

* `NorthEast` (value: `"NorthEast"`)

* `West` (value: `"West"`)

* `Center` (value: `"Center"`)

* `East` (value: `"East"`)

* `SouthWest` (value: `"SouthWest"`)

* `South` (value: `"South"`)

* `SouthEast` (value: `"SouthEast"`)





## Enum: ImageScaleTypeEnum


* `fit` (value: `"fit"`)

* `fill` (value: `"fill"`)

* `stretch` (value: `"stretch"`)





## Enum: NumberConditionTypeEnum


* `equals` (value: `"equals"`)

* `range` (value: `"range"`)

* `gte` (value: `"gte"`)

* `gt` (value: `"gt"`)

* `lte` (value: `"lte"`)

* `lt` (value: `"lt"`)





## Enum: OverflowEnum


* `shrink_to_fit` (value: `"shrink_to_fit"`)

* `truncate` (value: `"truncate"`)





## Enum: ShapeTypeEnum


* `square` (value: `"square"`)

* `rectangle` (value: `"rectangle"`)

* `circle` (value: `"circle"`)

* `ellipse` (value: `"ellipse"`)





## Enum: StringConditionTypeEnum


* `equals` (value: `"equals"`)

* `contains` (value: `"contains"`)

* `starts_with` (value: `"starts_with"`)

* `ends_with` (value: `"ends_with"`)

* `regex` (value: `"regex"`)





## Enum: TypeEnum


* `string` (value: `"string"`)

* `number` (value: `"number"`)

* `boolean` (value: `"boolean"`)

* `date` (value: `"date"`)

* `address` (value: `"address"`)

* `country` (value: `"country"`)

* `email` (value: `"email"`)

* `url` (value: `"url"`)

* `image` (value: `"image"`)

* `signature` (value: `"signature"`)

* `barcode` (value: `"barcode"`)

* `combined` (value: `"combined"`)





## Enum: VAlignmentEnum


* `bottom` (value: `"bottom"`)

* `center` (value: `"center"`)

* `top` (value: `"top"`)




