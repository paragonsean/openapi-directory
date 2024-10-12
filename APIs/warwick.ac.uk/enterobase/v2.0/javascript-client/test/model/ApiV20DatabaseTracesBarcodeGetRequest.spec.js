/**
 * Enterobase-API
 *  API for EnteroBase (https://enterobase.warwick.ac.uk)   EnteroBase is a user-friendly online resource, where users can upload their  own sequencing data for de novo assembly by a stream-lined pipeline. The assemblies  are used for calling MLST and wgMLST patterns, allowing users to compare their strains  to publically available genotyping data from other EnteroBase users, GenBank and classical MLST databases.  Click here to find how to get and use an API token: http://bit.ly/1TKlaOU 
 *
 * The version of the OpenAPI document: v2.0
 * Contact: enterobase@warwick.ac.uk
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
    factory(root.expect, root.EnterobaseApi);
  }
}(this, function(expect, EnterobaseApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
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

  describe('ApiV20DatabaseTracesBarcodeGetRequest', function() {
    it('should create an instance of ApiV20DatabaseTracesBarcodeGetRequest', function() {
      // uncomment below and update the code to test ApiV20DatabaseTracesBarcodeGetRequest
      //var instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
      //expect(instance).to.be.a(EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest);
    });

    it('should have the property barcode (base name: "barcode")', function() {
      // uncomment below and update the code to test the property barcode
      //var instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
      //expect(instance).to.be();
    });

    it('should have the property limit (base name: "limit")', function() {
      // uncomment below and update the code to test the property limit
      //var instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
      //expect(instance).to.be();
    });

    it('should have the property offset (base name: "offset")', function() {
      // uncomment below and update the code to test the property offset
      //var instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
      //expect(instance).to.be();
    });

    it('should have the property onlyFields (base name: "only_fields")', function() {
      // uncomment below and update the code to test the property onlyFields
      //var instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
      //expect(instance).to.be();
    });

    it('should have the property orderby (base name: "orderby")', function() {
      // uncomment below and update the code to test the property orderby
      //var instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
      //expect(instance).to.be();
    });

    it('should have the property sortorder (base name: "sortorder")', function() {
      // uncomment below and update the code to test the property sortorder
      //var instance = new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest();
      //expect(instance).to.be();
    });

  });

}));
