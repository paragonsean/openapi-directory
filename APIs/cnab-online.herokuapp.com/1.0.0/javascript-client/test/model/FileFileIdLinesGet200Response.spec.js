/**
 * Cnab Online
 * Processe arquivos de retorno CNAB
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.CnabOnline);
  }
}(this, function(expect, CnabOnline) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CnabOnline.FileFileIdLinesGet200Response();
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

  describe('FileFileIdLinesGet200Response', function() {
    it('should create an instance of FileFileIdLinesGet200Response', function() {
      // uncomment below and update the code to test FileFileIdLinesGet200Response
      //var instance = new CnabOnline.FileFileIdLinesGet200Response();
      //expect(instance).to.be.a(CnabOnline.FileFileIdLinesGet200Response);
    });

    it('should have the property data (base name: "data")', function() {
      // uncomment below and update the code to test the property data
      //var instance = new CnabOnline.FileFileIdLinesGet200Response();
      //expect(instance).to.be();
    });

  });

}));
