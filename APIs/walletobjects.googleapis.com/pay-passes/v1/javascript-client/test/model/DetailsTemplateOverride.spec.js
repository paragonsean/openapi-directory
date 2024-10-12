/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 * 
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
    factory(root.expect, root.GooglePayPassesApi);
  }
}(this, function(expect, GooglePayPassesApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GooglePayPassesApi.DetailsTemplateOverride();
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

  describe('DetailsTemplateOverride', function() {
    it('should create an instance of DetailsTemplateOverride', function() {
      // uncomment below and update the code to test DetailsTemplateOverride
      //var instance = new GooglePayPassesApi.DetailsTemplateOverride();
      //expect(instance).to.be.a(GooglePayPassesApi.DetailsTemplateOverride);
    });

    it('should have the property detailsItemInfos (base name: "detailsItemInfos")', function() {
      // uncomment below and update the code to test the property detailsItemInfos
      //var instance = new GooglePayPassesApi.DetailsTemplateOverride();
      //expect(instance).to.be();
    });

  });

}));
