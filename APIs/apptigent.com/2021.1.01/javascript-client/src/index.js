/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import DecodeStringRequest from './model/DecodeStringRequest';
import InputCalculateMinMax from './model/InputCalculateMinMax';
import InputCalculateNumber from './model/InputCalculateNumber';
import InputCalculateNumbers from './model/InputCalculateNumbers';
import InputCalculatePower from './model/InputCalculatePower';
import InputCalculateSeries from './model/InputCalculateSeries';
import InputCaseConversion from './model/InputCaseConversion';
import InputCollectionConversion from './model/InputCollectionConversion';
import InputCollectionConversionXML from './model/InputCollectionConversionXML';
import InputCollectionCount from './model/InputCollectionCount';
import InputCollectionFilter from './model/InputCollectionFilter';
import InputCollectionModify from './model/InputCollectionModify';
import InputCollectionReplace from './model/InputCollectionReplace';
import InputCollectionSearch from './model/InputCollectionSearch';
import InputCollectionSearchNumeric from './model/InputCollectionSearchNumeric';
import InputCollectionSort from './model/InputCollectionSort';
import InputCollectionSplit from './model/InputCollectionSplit';
import InputConvertAngle from './model/InputConvertAngle';
import InputConvertArea from './model/InputConvertArea';
import InputConvertDistance from './model/InputConvertDistance';
import InputConvertDuration from './model/InputConvertDuration';
import InputConvertEnergy from './model/InputConvertEnergy';
import InputConvertPower from './model/InputConvertPower';
import InputConvertSpeed from './model/InputConvertSpeed';
import InputConvertTemperature from './model/InputConvertTemperature';
import InputConvertVolume from './model/InputConvertVolume';
import InputConvertWeight from './model/InputConvertWeight';
import InputCsvConversionJSON from './model/InputCsvConversionJSON';
import InputCurrencyConversion from './model/InputCurrencyConversion';
import InputCurrencyFormat from './model/InputCurrencyFormat';
import InputDataQuery from './model/InputDataQuery';
import InputDateTimeConversion from './model/InputDateTimeConversion';
import InputDateTimeDifference from './model/InputDateTimeDifference';
import InputDateTimeFormat from './model/InputDateTimeFormat';
import InputDateTimeInfo from './model/InputDateTimeInfo';
import InputGenerateHash from './model/InputGenerateHash';
import InputGenerateUniqueID from './model/InputGenerateUniqueID';
import InputJoinStrings from './model/InputJoinStrings';
import InputJsonConversionCSV from './model/InputJsonConversionCSV';
import InputJsonConversionHTML from './model/InputJsonConversionHTML';
import InputJsonConversionXML from './model/InputJsonConversionXML';
import InputMarketIndex from './model/InputMarketIndex';
import InputNumberRange from './model/InputNumberRange';
import InputQRCode from './model/InputQRCode';
import InputRedactString from './model/InputRedactString';
import InputReplaceString from './model/InputReplaceString';
import InputSplitString from './model/InputSplitString';
import InputStockPrices from './model/InputStockPrices';
import InputString from './model/InputString';
import InputStringComparison from './model/InputStringComparison';
import InputStringContains from './model/InputStringContains';
import InputStringToFile from './model/InputStringToFile';
import InputTextToSpeech from './model/InputTextToSpeech';
import InputTranslateString from './model/InputTranslateString';
import InputTrimString from './model/InputTrimString';
import InputVerifyHash from './model/InputVerifyHash';
import InputXmlConversionJSON from './model/InputXmlConversionJSON';
import OutputBoolean from './model/OutputBoolean';
import OutputCollectionNumber from './model/OutputCollectionNumber';
import OutputCollectionResult from './model/OutputCollectionResult';
import OutputCollectionString from './model/OutputCollectionString';
import OutputDateDifference from './model/OutputDateDifference';
import OutputDateInfo from './model/OutputDateInfo';
import OutputFileByte from './model/OutputFileByte';
import OutputMarketIndex from './model/OutputMarketIndex';
import OutputMultiCollection from './model/OutputMultiCollection';
import OutputNumber from './model/OutputNumber';
import OutputStockPrice from './model/OutputStockPrice';
import OutputStockPriceResultInner from './model/OutputStockPriceResultInner';
import OutputString from './model/OutputString';
import OutputStringArray from './model/OutputStringArray';
import ShortenLinkRequest from './model/ShortenLinkRequest';
import UrlDecodeRequest from './model/UrlDecodeRequest';
import ValidateEmailRequest from './model/ValidateEmailRequest';
import CollectionsApi from './api/CollectionsApi';
import DataApi from './api/DataApi';
import DateTimeApi from './api/DateTimeApi';
import FilesApi from './api/FilesApi';
import FinanceApi from './api/FinanceApi';
import MathApi from './api/MathApi';
import TextApi from './api/TextApi';


/**
* Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL&#39;s, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var PowerToolsDeveloper = require('index'); // See note below*.
* var xxxSvc = new PowerToolsDeveloper.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new PowerToolsDeveloper.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new PowerToolsDeveloper.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new PowerToolsDeveloper.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2021.1.01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The DecodeStringRequest model constructor.
     * @property {module:model/DecodeStringRequest}
     */
    DecodeStringRequest,

    /**
     * The InputCalculateMinMax model constructor.
     * @property {module:model/InputCalculateMinMax}
     */
    InputCalculateMinMax,

    /**
     * The InputCalculateNumber model constructor.
     * @property {module:model/InputCalculateNumber}
     */
    InputCalculateNumber,

    /**
     * The InputCalculateNumbers model constructor.
     * @property {module:model/InputCalculateNumbers}
     */
    InputCalculateNumbers,

    /**
     * The InputCalculatePower model constructor.
     * @property {module:model/InputCalculatePower}
     */
    InputCalculatePower,

    /**
     * The InputCalculateSeries model constructor.
     * @property {module:model/InputCalculateSeries}
     */
    InputCalculateSeries,

    /**
     * The InputCaseConversion model constructor.
     * @property {module:model/InputCaseConversion}
     */
    InputCaseConversion,

    /**
     * The InputCollectionConversion model constructor.
     * @property {module:model/InputCollectionConversion}
     */
    InputCollectionConversion,

    /**
     * The InputCollectionConversionXML model constructor.
     * @property {module:model/InputCollectionConversionXML}
     */
    InputCollectionConversionXML,

    /**
     * The InputCollectionCount model constructor.
     * @property {module:model/InputCollectionCount}
     */
    InputCollectionCount,

    /**
     * The InputCollectionFilter model constructor.
     * @property {module:model/InputCollectionFilter}
     */
    InputCollectionFilter,

    /**
     * The InputCollectionModify model constructor.
     * @property {module:model/InputCollectionModify}
     */
    InputCollectionModify,

    /**
     * The InputCollectionReplace model constructor.
     * @property {module:model/InputCollectionReplace}
     */
    InputCollectionReplace,

    /**
     * The InputCollectionSearch model constructor.
     * @property {module:model/InputCollectionSearch}
     */
    InputCollectionSearch,

    /**
     * The InputCollectionSearchNumeric model constructor.
     * @property {module:model/InputCollectionSearchNumeric}
     */
    InputCollectionSearchNumeric,

    /**
     * The InputCollectionSort model constructor.
     * @property {module:model/InputCollectionSort}
     */
    InputCollectionSort,

    /**
     * The InputCollectionSplit model constructor.
     * @property {module:model/InputCollectionSplit}
     */
    InputCollectionSplit,

    /**
     * The InputConvertAngle model constructor.
     * @property {module:model/InputConvertAngle}
     */
    InputConvertAngle,

    /**
     * The InputConvertArea model constructor.
     * @property {module:model/InputConvertArea}
     */
    InputConvertArea,

    /**
     * The InputConvertDistance model constructor.
     * @property {module:model/InputConvertDistance}
     */
    InputConvertDistance,

    /**
     * The InputConvertDuration model constructor.
     * @property {module:model/InputConvertDuration}
     */
    InputConvertDuration,

    /**
     * The InputConvertEnergy model constructor.
     * @property {module:model/InputConvertEnergy}
     */
    InputConvertEnergy,

    /**
     * The InputConvertPower model constructor.
     * @property {module:model/InputConvertPower}
     */
    InputConvertPower,

    /**
     * The InputConvertSpeed model constructor.
     * @property {module:model/InputConvertSpeed}
     */
    InputConvertSpeed,

    /**
     * The InputConvertTemperature model constructor.
     * @property {module:model/InputConvertTemperature}
     */
    InputConvertTemperature,

    /**
     * The InputConvertVolume model constructor.
     * @property {module:model/InputConvertVolume}
     */
    InputConvertVolume,

    /**
     * The InputConvertWeight model constructor.
     * @property {module:model/InputConvertWeight}
     */
    InputConvertWeight,

    /**
     * The InputCsvConversionJSON model constructor.
     * @property {module:model/InputCsvConversionJSON}
     */
    InputCsvConversionJSON,

    /**
     * The InputCurrencyConversion model constructor.
     * @property {module:model/InputCurrencyConversion}
     */
    InputCurrencyConversion,

    /**
     * The InputCurrencyFormat model constructor.
     * @property {module:model/InputCurrencyFormat}
     */
    InputCurrencyFormat,

    /**
     * The InputDataQuery model constructor.
     * @property {module:model/InputDataQuery}
     */
    InputDataQuery,

    /**
     * The InputDateTimeConversion model constructor.
     * @property {module:model/InputDateTimeConversion}
     */
    InputDateTimeConversion,

    /**
     * The InputDateTimeDifference model constructor.
     * @property {module:model/InputDateTimeDifference}
     */
    InputDateTimeDifference,

    /**
     * The InputDateTimeFormat model constructor.
     * @property {module:model/InputDateTimeFormat}
     */
    InputDateTimeFormat,

    /**
     * The InputDateTimeInfo model constructor.
     * @property {module:model/InputDateTimeInfo}
     */
    InputDateTimeInfo,

    /**
     * The InputGenerateHash model constructor.
     * @property {module:model/InputGenerateHash}
     */
    InputGenerateHash,

    /**
     * The InputGenerateUniqueID model constructor.
     * @property {module:model/InputGenerateUniqueID}
     */
    InputGenerateUniqueID,

    /**
     * The InputJoinStrings model constructor.
     * @property {module:model/InputJoinStrings}
     */
    InputJoinStrings,

    /**
     * The InputJsonConversionCSV model constructor.
     * @property {module:model/InputJsonConversionCSV}
     */
    InputJsonConversionCSV,

    /**
     * The InputJsonConversionHTML model constructor.
     * @property {module:model/InputJsonConversionHTML}
     */
    InputJsonConversionHTML,

    /**
     * The InputJsonConversionXML model constructor.
     * @property {module:model/InputJsonConversionXML}
     */
    InputJsonConversionXML,

    /**
     * The InputMarketIndex model constructor.
     * @property {module:model/InputMarketIndex}
     */
    InputMarketIndex,

    /**
     * The InputNumberRange model constructor.
     * @property {module:model/InputNumberRange}
     */
    InputNumberRange,

    /**
     * The InputQRCode model constructor.
     * @property {module:model/InputQRCode}
     */
    InputQRCode,

    /**
     * The InputRedactString model constructor.
     * @property {module:model/InputRedactString}
     */
    InputRedactString,

    /**
     * The InputReplaceString model constructor.
     * @property {module:model/InputReplaceString}
     */
    InputReplaceString,

    /**
     * The InputSplitString model constructor.
     * @property {module:model/InputSplitString}
     */
    InputSplitString,

    /**
     * The InputStockPrices model constructor.
     * @property {module:model/InputStockPrices}
     */
    InputStockPrices,

    /**
     * The InputString model constructor.
     * @property {module:model/InputString}
     */
    InputString,

    /**
     * The InputStringComparison model constructor.
     * @property {module:model/InputStringComparison}
     */
    InputStringComparison,

    /**
     * The InputStringContains model constructor.
     * @property {module:model/InputStringContains}
     */
    InputStringContains,

    /**
     * The InputStringToFile model constructor.
     * @property {module:model/InputStringToFile}
     */
    InputStringToFile,

    /**
     * The InputTextToSpeech model constructor.
     * @property {module:model/InputTextToSpeech}
     */
    InputTextToSpeech,

    /**
     * The InputTranslateString model constructor.
     * @property {module:model/InputTranslateString}
     */
    InputTranslateString,

    /**
     * The InputTrimString model constructor.
     * @property {module:model/InputTrimString}
     */
    InputTrimString,

    /**
     * The InputVerifyHash model constructor.
     * @property {module:model/InputVerifyHash}
     */
    InputVerifyHash,

    /**
     * The InputXmlConversionJSON model constructor.
     * @property {module:model/InputXmlConversionJSON}
     */
    InputXmlConversionJSON,

    /**
     * The OutputBoolean model constructor.
     * @property {module:model/OutputBoolean}
     */
    OutputBoolean,

    /**
     * The OutputCollectionNumber model constructor.
     * @property {module:model/OutputCollectionNumber}
     */
    OutputCollectionNumber,

    /**
     * The OutputCollectionResult model constructor.
     * @property {module:model/OutputCollectionResult}
     */
    OutputCollectionResult,

    /**
     * The OutputCollectionString model constructor.
     * @property {module:model/OutputCollectionString}
     */
    OutputCollectionString,

    /**
     * The OutputDateDifference model constructor.
     * @property {module:model/OutputDateDifference}
     */
    OutputDateDifference,

    /**
     * The OutputDateInfo model constructor.
     * @property {module:model/OutputDateInfo}
     */
    OutputDateInfo,

    /**
     * The OutputFileByte model constructor.
     * @property {module:model/OutputFileByte}
     */
    OutputFileByte,

    /**
     * The OutputMarketIndex model constructor.
     * @property {module:model/OutputMarketIndex}
     */
    OutputMarketIndex,

    /**
     * The OutputMultiCollection model constructor.
     * @property {module:model/OutputMultiCollection}
     */
    OutputMultiCollection,

    /**
     * The OutputNumber model constructor.
     * @property {module:model/OutputNumber}
     */
    OutputNumber,

    /**
     * The OutputStockPrice model constructor.
     * @property {module:model/OutputStockPrice}
     */
    OutputStockPrice,

    /**
     * The OutputStockPriceResultInner model constructor.
     * @property {module:model/OutputStockPriceResultInner}
     */
    OutputStockPriceResultInner,

    /**
     * The OutputString model constructor.
     * @property {module:model/OutputString}
     */
    OutputString,

    /**
     * The OutputStringArray model constructor.
     * @property {module:model/OutputStringArray}
     */
    OutputStringArray,

    /**
     * The ShortenLinkRequest model constructor.
     * @property {module:model/ShortenLinkRequest}
     */
    ShortenLinkRequest,

    /**
     * The UrlDecodeRequest model constructor.
     * @property {module:model/UrlDecodeRequest}
     */
    UrlDecodeRequest,

    /**
     * The ValidateEmailRequest model constructor.
     * @property {module:model/ValidateEmailRequest}
     */
    ValidateEmailRequest,

    /**
    * The CollectionsApi service constructor.
    * @property {module:api/CollectionsApi}
    */
    CollectionsApi,

    /**
    * The DataApi service constructor.
    * @property {module:api/DataApi}
    */
    DataApi,

    /**
    * The DateTimeApi service constructor.
    * @property {module:api/DateTimeApi}
    */
    DateTimeApi,

    /**
    * The FilesApi service constructor.
    * @property {module:api/FilesApi}
    */
    FilesApi,

    /**
    * The FinanceApi service constructor.
    * @property {module:api/FinanceApi}
    */
    FinanceApi,

    /**
    * The MathApi service constructor.
    * @property {module:api/MathApi}
    */
    MathApi,

    /**
    * The TextApi service constructor.
    * @property {module:api/TextApi}
    */
    TextApi
};
