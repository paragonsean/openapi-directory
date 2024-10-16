/**
 * Api2Pdf - PDF Generation, Powered by AWS Lambda
 *  # Introduction [Api2Pdf](https://www.api2pdf.com) is a powerful PDF generation API with no rate limits or file size constraints. Api2Pdf runs on AWS Lambda, a serverless architecture powered by Amazon to scale to millions of requests while being up to 90% cheaper than alternatives. **Supports wkhtmltopdf, Headless Chrome, LibreOffice, and PDF Merge.** You can also generate barcodes with ZXING (Zebra Crossing). # SDKs & Client Libraries We've made a number of open source libraries available for the API - Python: [https://github.com/api2pdf/api2pdf.python](https://github.com/api2pdf/api2pdf.python) - .NET: [https://github.com/api2pdf/api2pdf.dotnet](https://github.com/api2pdf/api2pdf.dotnet) - Nodejs: [https://github.com/api2pdf/api2pdf.node](https://github.com/api2pdf/api2pdf.node) - PHP: [https://github.com/Api2Pdf/api2pdf.php](https://github.com/Api2Pdf/api2pdf.php) - Ruby: (Coming soon) # Authorization Create an account at [portal.api2pdf.com](https://portal.api2pdf.com/register) to get an API key.  **Authorize your API calls** - GET requests, include apikey=YOUR-API-KEY as a query string parameter - POST requests, add **Authorization** to your header. ``` Authorization: YOUR-API-KEY ```  # Quickstart If you are looking for just a quick call to grab PDFs of a URL, you can do a GET request like: ``` https://v2018.api2pdf.com/chrome/url?url={UrlToConvert}&apikey={YourApiKey} ```  For more advanced usage and settings, see the API specification below. 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@api2pdf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* ZXINGZebraCrossingBarCodes service.
* @module api/ZXINGZebraCrossingBarCodesApi
* @version 1.0.0
*/
export default class ZXINGZebraCrossingBarCodesApi {

    /**
    * Constructs a new ZXINGZebraCrossingBarCodesApi. 
    * @alias module:api/ZXINGZebraCrossingBarCodesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the zebraGET operation.
     * @callback module:api/ZXINGZebraCrossingBarCodesApi~zebraGETCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate bar codes and QR codes with ZXING.
     * See full list of options and documentation [here](https://www.api2pdf.com/documentation/advanced-options-zxing-zebra-crossing-barcodes/) ### Authorize via Query String Parameter **apikey=YOUR-API-KEY** ### Example ``` https://v2018.api2pdf.com/zebra?format={format}&apikey={YourApiKey}&value={YourText} ``` 
     * @param {String} format Most common is CODE_39 or QR_CODE
     * @param {String} value Specify the text value you want to convert
     * @param {Object} opts Optional parameters
     * @param {Boolean} [showlabel] Show label of text below barcode
     * @param {Number} [height] Height of the barcode generated image
     * @param {Number} [width] Width of the barcode generated image
     * @param {module:api/ZXINGZebraCrossingBarCodesApi~zebraGETCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    zebraGET(format, value, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling zebraGET");
      }
      // verify the required parameter 'value' is set
      if (value === undefined || value === null) {
        throw new Error("Missing the required parameter 'value' when calling zebraGET");
      }

      let pathParams = {
      };
      let queryParams = {
        'format': format,
        'value': value,
        'showlabel': opts['showlabel'],
        'height': opts['height'],
        'width': opts['width']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['QueryApiKey'];
      let contentTypes = [];
      let accepts = ['image/png'];
      let returnType = File;
      return this.apiClient.callApi(
        '/zebra', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
