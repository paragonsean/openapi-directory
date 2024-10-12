/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
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
    factory(root.expect, root.TripParser);
  }
}(this, function(expect, TripParser) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TripParser.Stakeholder();
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

  describe('Stakeholder', function() {
    it('should create an instance of Stakeholder', function() {
      // uncomment below and update the code to test Stakeholder
      //var instance = new TripParser.Stakeholder();
      //expect(instance).to.be.a(TripParser.Stakeholder);
    });

    it('should have the property age (base name: "age")', function() {
      // uncomment below and update the code to test the property age
      //var instance = new TripParser.Stakeholder();
      //expect(instance).to.be();
    });

    it('should have the property dateOfBirth (base name: "dateOfBirth")', function() {
      // uncomment below and update the code to test the property dateOfBirth
      //var instance = new TripParser.Stakeholder();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new TripParser.Stakeholder();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new TripParser.Stakeholder();
      //expect(instance).to.be();
    });

    it('should have the property nationality (base name: "nationality")', function() {
      // uncomment below and update the code to test the property nationality
      //var instance = new TripParser.Stakeholder();
      //expect(instance).to.be();
    });

    it('should have the property passangerTypeCode (base name: "passangerTypeCode")', function() {
      // uncomment below and update the code to test the property passangerTypeCode
      //var instance = new TripParser.Stakeholder();
      //expect(instance).to.be();
    });

  });

}));
