/**
 * groov View Public API
 * #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. 
 *
 * The version of the OpenAPI document: R4.2a
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
    factory(root.expect, root.GroovViewPublicApi);
  }
}(this, function(expect, GroovViewPublicApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GroovViewPublicApi.TagReference();
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

  describe('TagReference', function() {
    it('should create an instance of TagReference', function() {
      // uncomment below and update the code to test TagReference
      //var instance = new GroovViewPublicApi.TagReference();
      //expect(instance).to.be.a(GroovViewPublicApi.TagReference);
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new GroovViewPublicApi.TagReference();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new GroovViewPublicApi.TagReference();
      //expect(instance).to.be();
    });

    it('should have the property index (base name: "index")', function() {
      // uncomment below and update the code to test the property index
      //var instance = new GroovViewPublicApi.TagReference();
      //expect(instance).to.be();
    });

  });

}));
