/**
 * IoTSpacesClient
 * Use this API to manage the IoTSpaces service instances in your Azure subscription.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
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
    factory(root.expect, root.IoTSpacesClient);
  }
}(this, function(expect, IoTSpacesClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new IoTSpacesClient.ProxyApi();
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

  describe('ProxyApi', function() {
    describe('ioTSpacesCheckNameAvailability', function() {
      it('should call ioTSpacesCheckNameAvailability successfully', function(done) {
        //uncomment below and update the code to test ioTSpacesCheckNameAvailability
        //instance.ioTSpacesCheckNameAvailability(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('operationsList', function() {
      it('should call operationsList successfully', function(done) {
        //uncomment below and update the code to test operationsList
        //instance.operationsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
