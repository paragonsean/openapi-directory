/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-07-01
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
    factory(root.expect, root.NetworkManagementClient);
  }
}(this, function(expect, NetworkManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NetworkManagementClient.ExpressRouteGatewayList();
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

  describe('ExpressRouteGatewayList', function() {
    it('should create an instance of ExpressRouteGatewayList', function() {
      // uncomment below and update the code to test ExpressRouteGatewayList
      //var instance = new NetworkManagementClient.ExpressRouteGatewayList();
      //expect(instance).to.be.a(NetworkManagementClient.ExpressRouteGatewayList);
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new NetworkManagementClient.ExpressRouteGatewayList();
      //expect(instance).to.be();
    });

  });

}));
