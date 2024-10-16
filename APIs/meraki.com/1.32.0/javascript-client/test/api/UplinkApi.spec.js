/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
    factory(root.expect, root.MerakiDashboardApi);
  }
}(this, function(expect, MerakiDashboardApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MerakiDashboardApi.UplinkApi();
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

  describe('UplinkApi', function() {
    describe('getNetworkCellularGatewayUplink_1', function() {
      it('should call getNetworkCellularGatewayUplink_1 successfully', function(done) {
        //uncomment below and update the code to test getNetworkCellularGatewayUplink_1
        //instance.getNetworkCellularGatewayUplink_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrganizationCellularGatewayUplinkStatuses_1', function() {
      it('should call getOrganizationCellularGatewayUplinkStatuses_1 successfully', function(done) {
        //uncomment below and update the code to test getOrganizationCellularGatewayUplinkStatuses_1
        //instance.getOrganizationCellularGatewayUplinkStatuses_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkCellularGatewayUplink_1', function() {
      it('should call updateNetworkCellularGatewayUplink_1 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkCellularGatewayUplink_1
        //instance.updateNetworkCellularGatewayUplink_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
