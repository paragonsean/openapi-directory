/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
    factory(root.expect, root.SliceboxApi);
  }
}(this, function(expect, SliceboxApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SliceboxApi.OutgoingTransactionImage();
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

  describe('OutgoingTransactionImage', function() {
    it('should create an instance of OutgoingTransactionImage', function() {
      // uncomment below and update the code to test OutgoingTransactionImage
      //var instance = new SliceboxApi.OutgoingTransactionImage();
      //expect(instance).to.be.a(SliceboxApi.OutgoingTransactionImage);
    });

    it('should have the property image (base name: "image")', function() {
      // uncomment below and update the code to test the property image
      //var instance = new SliceboxApi.OutgoingTransactionImage();
      //expect(instance).to.be();
    });

    it('should have the property transaction (base name: "transaction")', function() {
      // uncomment below and update the code to test the property transaction
      //var instance = new SliceboxApi.OutgoingTransactionImage();
      //expect(instance).to.be();
    });

  });

}));
