/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.FaceClient);
  }
}(this, function(expect, FaceClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FaceClient.FaceDetectWithUrlRequest();
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

  describe('FaceDetectWithUrlRequest', function() {
    it('should create an instance of FaceDetectWithUrlRequest', function() {
      // uncomment below and update the code to test FaceDetectWithUrlRequest
      //var instance = new FaceClient.FaceDetectWithUrlRequest();
      //expect(instance).to.be.a(FaceClient.FaceDetectWithUrlRequest);
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new FaceClient.FaceDetectWithUrlRequest();
      //expect(instance).to.be();
    });

  });

}));
