/**
 * LoL v3 Scores
 * LoL v3 Scores
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
    factory(root.expect, root.LoLV3Scores);
  }
}(this, function(expect, LoLV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LoLV3Scores.Team();
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

  describe('Team', function() {
    it('should create an instance of Team', function() {
      // uncomment below and update the code to test Team
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be.a(LoLV3Scores.Team);
    });

    it('should have the property active (base name: "Active")', function() {
      // uncomment below and update the code to test the property active
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property areaId (base name: "AreaId")', function() {
      // uncomment below and update the code to test the property areaId
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property areaName (base name: "AreaName")', function() {
      // uncomment below and update the code to test the property areaName
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "Email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property facebook (base name: "Facebook")', function() {
      // uncomment below and update the code to test the property facebook
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property founded (base name: "Founded")', function() {
      // uncomment below and update the code to test the property founded
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property gender (base name: "Gender")', function() {
      // uncomment below and update the code to test the property gender
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property instagram (base name: "Instagram")', function() {
      // uncomment below and update the code to test the property instagram
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property key (base name: "Key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property primaryColor (base name: "PrimaryColor")', function() {
      // uncomment below and update the code to test the property primaryColor
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property quaternaryColor (base name: "QuaternaryColor")', function() {
      // uncomment below and update the code to test the property quaternaryColor
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property secondaryColor (base name: "SecondaryColor")', function() {
      // uncomment below and update the code to test the property secondaryColor
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property shortName (base name: "ShortName")', function() {
      // uncomment below and update the code to test the property shortName
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property teamId (base name: "TeamId")', function() {
      // uncomment below and update the code to test the property teamId
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property tertiaryColor (base name: "TertiaryColor")', function() {
      // uncomment below and update the code to test the property tertiaryColor
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property twitter (base name: "Twitter")', function() {
      // uncomment below and update the code to test the property twitter
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property website (base name: "Website")', function() {
      // uncomment below and update the code to test the property website
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

    it('should have the property youTube (base name: "YouTube")', function() {
      // uncomment below and update the code to test the property youTube
      //var instance = new LoLV3Scores.Team();
      //expect(instance).to.be();
    });

  });

}));
