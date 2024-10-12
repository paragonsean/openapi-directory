/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
    factory(root.expect, root.DaniWebConnectApi);
  }
}(this, function(expect, DaniWebConnectApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DaniWebConnectApi.EndpointGetUsersNearbyDataInner();
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

  describe('EndpointGetUsersNearbyDataInner', function() {
    it('should create an instance of EndpointGetUsersNearbyDataInner', function() {
      // uncomment below and update the code to test EndpointGetUsersNearbyDataInner
      //var instance = new DaniWebConnectApi.EndpointGetUsersNearbyDataInner();
      //expect(instance).to.be.a(DaniWebConnectApi.EndpointGetUsersNearbyDataInner);
    });

    it('should have the property distanceAway (base name: "distance_away")', function() {
      // uncomment below and update the code to test the property distanceAway
      //var instance = new DaniWebConnectApi.EndpointGetUsersNearbyDataInner();
      //expect(instance).to.be();
    });

    it('should have the property user (base name: "user")', function() {
      // uncomment below and update the code to test the property user
      //var instance = new DaniWebConnectApi.EndpointGetUsersNearbyDataInner();
      //expect(instance).to.be();
    });

  });

}));
