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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PowerToolsDeveloper);
  }
}(this, function(expect, PowerToolsDeveloper) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PowerToolsDeveloper.InputGenerateHash();
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

  describe('InputGenerateHash', function() {
    it('should create an instance of InputGenerateHash', function() {
      // uncomment below and update the code to test InputGenerateHash
      //var instance = new PowerToolsDeveloper.InputGenerateHash();
      //expect(instance).to.be.a(PowerToolsDeveloper.InputGenerateHash);
    });

    it('should have the property algorithm (base name: "algorithm")', function() {
      // uncomment below and update the code to test the property algorithm
      //var instance = new PowerToolsDeveloper.InputGenerateHash();
      //expect(instance).to.be();
    });

    it('should have the property input (base name: "input")', function() {
      // uncomment below and update the code to test the property input
      //var instance = new PowerToolsDeveloper.InputGenerateHash();
      //expect(instance).to.be();
    });

  });

}));
