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
    instance = new DaniWebConnectApi.UsersApi();
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

  describe('UsersApi', function() {
    describe('usersGet', function() {
      it('should call usersGet successfully', function(done) {
        //uncomment below and update the code to test usersGet
        //instance.usersGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersGet_0', function() {
      it('should call usersGet_0 successfully', function(done) {
        //uncomment below and update the code to test usersGet_0
        //instance.usersGet_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDGet', function() {
      it('should call usersIDGet successfully', function(done) {
        //uncomment below and update the code to test usersIDGet
        //instance.usersIDGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDGroupsGet', function() {
      it('should call usersIDGroupsGet successfully', function(done) {
        //uncomment below and update the code to test usersIDGroupsGet
        //instance.usersIDGroupsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDGroupsMessagesGet', function() {
      it('should call usersIDGroupsMessagesGet successfully', function(done) {
        //uncomment below and update the code to test usersIDGroupsMessagesGet
        //instance.usersIDGroupsMessagesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDMessagesPost', function() {
      it('should call usersIDMessagesPost successfully', function(done) {
        //uncomment below and update the code to test usersIDMessagesPost
        //instance.usersIDMessagesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDMetadataCollectionsGet', function() {
      it('should call usersIDMetadataCollectionsGet successfully', function(done) {
        //uncomment below and update the code to test usersIDMetadataCollectionsGet
        //instance.usersIDMetadataCollectionsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDMetadataGet', function() {
      it('should call usersIDMetadataGet successfully', function(done) {
        //uncomment below and update the code to test usersIDMetadataGet
        //instance.usersIDMetadataGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDMetadataPost', function() {
      it('should call usersIDMetadataPost successfully', function(done) {
        //uncomment below and update the code to test usersIDMetadataPost
        //instance.usersIDMetadataPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDPositionsGet', function() {
      it('should call usersIDPositionsGet successfully', function(done) {
        //uncomment below and update the code to test usersIDPositionsGet
        //instance.usersIDPositionsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDSynergiesGet', function() {
      it('should call usersIDSynergiesGet successfully', function(done) {
        //uncomment below and update the code to test usersIDSynergiesGet
        //instance.usersIDSynergiesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersIDSynergiesPatch', function() {
      it('should call usersIDSynergiesPatch successfully', function(done) {
        //uncomment below and update the code to test usersIDSynergiesPatch
        //instance.usersIDSynergiesPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersInvitesPost', function() {
      it('should call usersInvitesPost successfully', function(done) {
        //uncomment below and update the code to test usersInvitesPost
        //instance.usersInvitesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersMetadataFiltersPost', function() {
      it('should call usersMetadataFiltersPost successfully', function(done) {
        //uncomment below and update the code to test usersMetadataFiltersPost
        //instance.usersMetadataFiltersPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersNearbyGet', function() {
      it('should call usersNearbyGet successfully', function(done) {
        //uncomment below and update the code to test usersNearbyGet
        //instance.usersNearbyGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersPatch', function() {
      it('should call usersPatch successfully', function(done) {
        //uncomment below and update the code to test usersPatch
        //instance.usersPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('usersSearchesPost', function() {
      it('should call usersSearchesPost successfully', function(done) {
        //uncomment below and update the code to test usersSearchesPost
        //instance.usersSearchesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
