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
    instance = new SliceboxApi.FailedOutgoingTransactionImage();
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

  describe('FailedOutgoingTransactionImage', function() {
    it('should create an instance of FailedOutgoingTransactionImage', function() {
      // uncomment below and update the code to test FailedOutgoingTransactionImage
      //var instance = new SliceboxApi.FailedOutgoingTransactionImage();
      //expect(instance).to.be.a(SliceboxApi.FailedOutgoingTransactionImage);
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instance = new SliceboxApi.FailedOutgoingTransactionImage();
      //expect(instance).to.be();
    });

    it('should have the property transactionImage (base name: "transactionImage")', function() {
      // uncomment below and update the code to test the property transactionImage
      //var instance = new SliceboxApi.FailedOutgoingTransactionImage();
      //expect(instance).to.be();
    });

  });

}));
