/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
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
    factory(root.expect, root.Mailsquad);
  }
}(this, function(expect, Mailsquad) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Mailsquad.ListsApi();
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

  describe('ListsApi', function() {
    describe('contactsListsGet', function() {
      it('should call contactsListsGet successfully', function(done) {
        //uncomment below and update the code to test contactsListsGet
        //instance.contactsListsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('contactsListsListidDelete', function() {
      it('should call contactsListsListidDelete successfully', function(done) {
        //uncomment below and update the code to test contactsListsListidDelete
        //instance.contactsListsListidDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('contactsListsListidPut', function() {
      it('should call contactsListsListidPut successfully', function(done) {
        //uncomment below and update the code to test contactsListsListidPut
        //instance.contactsListsListidPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('contactsListsPost', function() {
      it('should call contactsListsPost successfully', function(done) {
        //uncomment below and update the code to test contactsListsPost
        //instance.contactsListsPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
