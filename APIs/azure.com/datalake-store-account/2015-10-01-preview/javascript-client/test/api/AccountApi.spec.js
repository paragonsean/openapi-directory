/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2015-10-01-preview
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
    factory(root.expect, root.DataLakeStoreAccountManagementClient);
  }
}(this, function(expect, DataLakeStoreAccountManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DataLakeStoreAccountManagementClient.AccountApi();
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

  describe('AccountApi', function() {
    describe('accountCreate', function() {
      it('should call accountCreate successfully', function(done) {
        //uncomment below and update the code to test accountCreate
        //instance.accountCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountCreateOrUpdateFirewallRule', function() {
      it('should call accountCreateOrUpdateFirewallRule successfully', function(done) {
        //uncomment below and update the code to test accountCreateOrUpdateFirewallRule
        //instance.accountCreateOrUpdateFirewallRule(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountDelete', function() {
      it('should call accountDelete successfully', function(done) {
        //uncomment below and update the code to test accountDelete
        //instance.accountDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountDeleteFirewallRule', function() {
      it('should call accountDeleteFirewallRule successfully', function(done) {
        //uncomment below and update the code to test accountDeleteFirewallRule
        //instance.accountDeleteFirewallRule(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountEnableKeyVault', function() {
      it('should call accountEnableKeyVault successfully', function(done) {
        //uncomment below and update the code to test accountEnableKeyVault
        //instance.accountEnableKeyVault(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountGet', function() {
      it('should call accountGet successfully', function(done) {
        //uncomment below and update the code to test accountGet
        //instance.accountGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountGetFirewallRule', function() {
      it('should call accountGetFirewallRule successfully', function(done) {
        //uncomment below and update the code to test accountGetFirewallRule
        //instance.accountGetFirewallRule(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountList', function() {
      it('should call accountList successfully', function(done) {
        //uncomment below and update the code to test accountList
        //instance.accountList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountListByResourceGroup', function() {
      it('should call accountListByResourceGroup successfully', function(done) {
        //uncomment below and update the code to test accountListByResourceGroup
        //instance.accountListByResourceGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountListFirewallRules', function() {
      it('should call accountListFirewallRules successfully', function(done) {
        //uncomment below and update the code to test accountListFirewallRules
        //instance.accountListFirewallRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accountUpdate', function() {
      it('should call accountUpdate successfully', function(done) {
        //uncomment below and update the code to test accountUpdate
        //instance.accountUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
