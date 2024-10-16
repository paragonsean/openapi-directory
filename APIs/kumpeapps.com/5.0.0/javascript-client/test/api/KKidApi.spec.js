/**
 * KumpeApps API
 * KKid API. Due to security concerns all calls to this API requires authentication. If you have access then you may use your KumpeApps username/password to authenticate. To gain access please use the contact developer link below.
 *
 * The version of the OpenAPI document: 5.0.0
 * Contact: helpdesk@kumpeapps.com
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
    factory(root.expect, root.KumpeAppsApi);
  }
}(this, function(expect, KumpeAppsApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new KumpeAppsApi.KKidApi();
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

  describe('KKidApi', function() {
    describe('kkidAllowanceGet', function() {
      it('should call kkidAllowanceGet successfully', function(done) {
        //uncomment below and update the code to test kkidAllowanceGet
        //instance.kkidAllowanceGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidAllowancePost', function() {
      it('should call kkidAllowancePost successfully', function(done) {
        //uncomment below and update the code to test kkidAllowancePost
        //instance.kkidAllowancePost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidApnsPost', function() {
      it('should call kkidApnsPost successfully', function(done) {
        //uncomment below and update the code to test kkidApnsPost
        //instance.kkidApnsPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidChorelistDelete', function() {
      it('should call kkidChorelistDelete successfully', function(done) {
        //uncomment below and update the code to test kkidChorelistDelete
        //instance.kkidChorelistDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidChorelistGet', function() {
      it('should call kkidChorelistGet successfully', function(done) {
        //uncomment below and update the code to test kkidChorelistGet
        //instance.kkidChorelistGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidChorelistPost', function() {
      it('should call kkidChorelistPost successfully', function(done) {
        //uncomment below and update the code to test kkidChorelistPost
        //instance.kkidChorelistPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidChorelistPut', function() {
      it('should call kkidChorelistPut successfully', function(done) {
        //uncomment below and update the code to test kkidChorelistPut
        //instance.kkidChorelistPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidMasteruserPost', function() {
      it('should call kkidMasteruserPost successfully', function(done) {
        //uncomment below and update the code to test kkidMasteruserPost
        //instance.kkidMasteruserPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidShareGet', function() {
      it('should call kkidShareGet successfully', function(done) {
        //uncomment below and update the code to test kkidShareGet
        //instance.kkidShareGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidUserGet', function() {
      it('should call kkidUserGet successfully', function(done) {
        //uncomment below and update the code to test kkidUserGet
        //instance.kkidUserGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidUserlistDelete', function() {
      it('should call kkidUserlistDelete successfully', function(done) {
        //uncomment below and update the code to test kkidUserlistDelete
        //instance.kkidUserlistDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidUserlistGet', function() {
      it('should call kkidUserlistGet successfully', function(done) {
        //uncomment below and update the code to test kkidUserlistGet
        //instance.kkidUserlistGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidUserlistPost', function() {
      it('should call kkidUserlistPost successfully', function(done) {
        //uncomment below and update the code to test kkidUserlistPost
        //instance.kkidUserlistPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidUserlistPut', function() {
      it('should call kkidUserlistPut successfully', function(done) {
        //uncomment below and update the code to test kkidUserlistPut
        //instance.kkidUserlistPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidWishlistDelete', function() {
      it('should call kkidWishlistDelete successfully', function(done) {
        //uncomment below and update the code to test kkidWishlistDelete
        //instance.kkidWishlistDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidWishlistGet', function() {
      it('should call kkidWishlistGet successfully', function(done) {
        //uncomment below and update the code to test kkidWishlistGet
        //instance.kkidWishlistGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidWishlistPost', function() {
      it('should call kkidWishlistPost successfully', function(done) {
        //uncomment below and update the code to test kkidWishlistPost
        //instance.kkidWishlistPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('kkidWishlistPut', function() {
      it('should call kkidWishlistPut successfully', function(done) {
        //uncomment below and update the code to test kkidWishlistPut
        //instance.kkidWishlistPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
