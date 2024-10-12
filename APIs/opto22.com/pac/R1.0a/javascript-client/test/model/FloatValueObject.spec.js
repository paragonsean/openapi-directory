/**
 * PAC Control REST API
 * #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller's variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC's strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   ``` https://1.2.3.4/api/v1/device/strategy/vars/int32s ``` and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  ```json [ { \"nMyVeryFavoriteNumber\": 22 },   { \"nWidgetsProducedToday\": 22222 },   { \"DELAY_LOOP_TIME_IN_MSECS\"  : 200 } ] ``` **Read the engineering units** (EU) of an analog input point configured in the PAC's strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   `https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu`  The GET response will be a single JSON name-value pair such as: ```json { \"value\": 72.22 } ```      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
 *
 * The version of the OpenAPI document: R1.0a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PacControlRestApi);
  }
}(this, function(expect, PacControlRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PacControlRestApi.FloatValueObject();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('FloatValueObject', function() {
    it('should create an instance of FloatValueObject', function() {
      // uncomment below and update the code to test FloatValueObject
      //var instance = new PacControlRestApi.FloatValueObject();
      //expect(instance).to.be.a(PacControlRestApi.FloatValueObject);
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new PacControlRestApi.FloatValueObject();
      //expect(instance).to.be();
    });

  });

}));
