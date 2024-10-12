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
    instance = new FaceClient.DetectedFace();
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

  describe('DetectedFace', function() {
    it('should create an instance of DetectedFace', function() {
      // uncomment below and update the code to test DetectedFace
      //var instance = new FaceClient.DetectedFace();
      //expect(instance).to.be.a(FaceClient.DetectedFace);
    });

    it('should have the property faceAttributes (base name: "faceAttributes")', function() {
      // uncomment below and update the code to test the property faceAttributes
      //var instance = new FaceClient.DetectedFace();
      //expect(instance).to.be();
    });

    it('should have the property faceId (base name: "faceId")', function() {
      // uncomment below and update the code to test the property faceId
      //var instance = new FaceClient.DetectedFace();
      //expect(instance).to.be();
    });

    it('should have the property faceLandmarks (base name: "faceLandmarks")', function() {
      // uncomment below and update the code to test the property faceLandmarks
      //var instance = new FaceClient.DetectedFace();
      //expect(instance).to.be();
    });

    it('should have the property faceRectangle (base name: "faceRectangle")', function() {
      // uncomment below and update the code to test the property faceRectangle
      //var instance = new FaceClient.DetectedFace();
      //expect(instance).to.be();
    });

    it('should have the property recognitionModel (base name: "recognitionModel")', function() {
      // uncomment below and update the code to test the property recognitionModel
      //var instance = new FaceClient.DetectedFace();
      //expect(instance).to.be();
    });

  });

}));
