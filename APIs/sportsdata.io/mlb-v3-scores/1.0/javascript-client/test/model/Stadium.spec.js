/**
 * MLB v3 Scores
 * MLB scores API.
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
    factory(root.expect, root.MlbV3Scores);
  }
}(this, function(expect, MlbV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MlbV3Scores.Stadium();
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

  describe('Stadium', function() {
    it('should create an instance of Stadium', function() {
      // uncomment below and update the code to test Stadium
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be.a(MlbV3Scores.Stadium);
    });

    it('should have the property active (base name: "Active")', function() {
      // uncomment below and update the code to test the property active
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property altitude (base name: "Altitude")', function() {
      // uncomment below and update the code to test the property altitude
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property capacity (base name: "Capacity")', function() {
      // uncomment below and update the code to test the property capacity
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property centerField (base name: "CenterField")', function() {
      // uncomment below and update the code to test the property centerField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property city (base name: "City")', function() {
      // uncomment below and update the code to test the property city
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property country (base name: "Country")', function() {
      // uncomment below and update the code to test the property country
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property geoLat (base name: "GeoLat")', function() {
      // uncomment below and update the code to test the property geoLat
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property geoLong (base name: "GeoLong")', function() {
      // uncomment below and update the code to test the property geoLong
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property homePlateDirection (base name: "HomePlateDirection")', function() {
      // uncomment below and update the code to test the property homePlateDirection
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property leftCenterField (base name: "LeftCenterField")', function() {
      // uncomment below and update the code to test the property leftCenterField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property leftField (base name: "LeftField")', function() {
      // uncomment below and update the code to test the property leftField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property midLeftCenterField (base name: "MidLeftCenterField")', function() {
      // uncomment below and update the code to test the property midLeftCenterField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property midLeftField (base name: "MidLeftField")', function() {
      // uncomment below and update the code to test the property midLeftField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property midRightCenterField (base name: "MidRightCenterField")', function() {
      // uncomment below and update the code to test the property midRightCenterField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property midRightField (base name: "MidRightField")', function() {
      // uncomment below and update the code to test the property midRightField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property rightCenterField (base name: "RightCenterField")', function() {
      // uncomment below and update the code to test the property rightCenterField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property rightField (base name: "RightField")', function() {
      // uncomment below and update the code to test the property rightField
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property stadiumID (base name: "StadiumID")', function() {
      // uncomment below and update the code to test the property stadiumID
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "State")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property surface (base name: "Surface")', function() {
      // uncomment below and update the code to test the property surface
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new MlbV3Scores.Stadium();
      //expect(instance).to.be();
    });

  });

}));
