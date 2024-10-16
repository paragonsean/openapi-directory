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
    instance = new KumpeAppsApi.User();
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

  describe('User', function() {
    it('should create an instance of User', function() {
      // uncomment below and update the code to test User
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be.a(KumpeAppsApi.User);
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property emoji (base name: "emoji")', function() {
      // uncomment below and update the code to test the property emoji
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property enableAllowance (base name: "enableAllowance")', function() {
      // uncomment below and update the code to test the property enableAllowance
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property enableBehaviorChart (base name: "enableBehaviorChart")', function() {
      // uncomment below and update the code to test the property enableBehaviorChart
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property enableChores (base name: "enableChores")', function() {
      // uncomment below and update the code to test the property enableChores
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property enableNoAds (base name: "enableNoAds")', function() {
      // uncomment below and update the code to test the property enableNoAds
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property enableObjectDetection (base name: "enableObjectDetection")', function() {
      // uncomment below and update the code to test the property enableObjectDetection
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property enableTmdb (base name: "enableTmdb")', function() {
      // uncomment below and update the code to test the property enableTmdb
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "firstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property homeId (base name: "homeId")', function() {
      // uncomment below and update the code to test the property homeId
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property isActive (base name: "isActive")', function() {
      // uncomment below and update the code to test the property isActive
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property isAdmin (base name: "isAdmin")', function() {
      // uncomment below and update the code to test the property isAdmin
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property isBanned (base name: "isBanned")', function() {
      // uncomment below and update the code to test the property isBanned
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property isChild (base name: "isChild")', function() {
      // uncomment below and update the code to test the property isChild
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property isDisabled (base name: "isDisabled")', function() {
      // uncomment below and update the code to test the property isDisabled
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property isLocked (base name: "isLocked")', function() {
      // uncomment below and update the code to test the property isLocked
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property isMaster (base name: "isMaster")', function() {
      // uncomment below and update the code to test the property isMaster
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "lastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property masterId (base name: "masterId")', function() {
      // uncomment below and update the code to test the property masterId
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property pushAllowance (base name: "pushAllowance")', function() {
      // uncomment below and update the code to test the property pushAllowance
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property pushAllowanceNew (base name: "pushAllowanceNew")', function() {
      // uncomment below and update the code to test the property pushAllowanceNew
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property pushChores (base name: "pushChores")', function() {
      // uncomment below and update the code to test the property pushChores
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property pushChoresNew (base name: "pushChoresNew")', function() {
      // uncomment below and update the code to test the property pushChoresNew
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property pushChoresReminders (base name: "pushChoresReminders")', function() {
      // uncomment below and update the code to test the property pushChoresReminders
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property tmdbKey (base name: "tmdbKey")', function() {
      // uncomment below and update the code to test the property tmdbKey
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property userId (base name: "userId")', function() {
      // uncomment below and update the code to test the property userId
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property username (base name: "username")', function() {
      // uncomment below and update the code to test the property username
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

    it('should have the property weeklyAllowance (base name: "weeklyAllowance")', function() {
      // uncomment below and update the code to test the property weeklyAllowance
      //var instance = new KumpeAppsApi.User();
      //expect(instance).to.be();
    });

  });

}));
