/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AvazaApiDocumentation);
  }
}(this, function(expect, AvazaApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AvazaApiDocumentation.UserDetails();
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

  describe('UserDetails', function() {
    it('should create an instance of UserDetails', function() {
      // uncomment below and update the code to test UserDetails
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be.a(AvazaApiDocumentation.UserDetails);
    });

    it('should have the property accountIDFK (base name: "AccountIDFK")', function() {
      // uncomment below and update the code to test the property accountIDFK
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property companyIDFK (base name: "CompanyIDFK")', function() {
      // uncomment below and update the code to test the property companyIDFK
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property companyName (base name: "CompanyName")', function() {
      // uncomment below and update the code to test the property companyName
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property defaultBillableRate (base name: "DefaultBillableRate")', function() {
      // uncomment below and update the code to test the property defaultBillableRate
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property defaultCostRate (base name: "DefaultCostRate")', function() {
      // uncomment below and update the code to test the property defaultCostRate
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "Email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property firstname (base name: "Firstname")', function() {
      // uncomment below and update the code to test the property firstname
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property fridayAvailableHours (base name: "FridayAvailableHours")', function() {
      // uncomment below and update the code to test the property fridayAvailableHours
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property iANATimezone (base name: "IANATimezone")', function() {
      // uncomment below and update the code to test the property iANATimezone
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property lastname (base name: "Lastname")', function() {
      // uncomment below and update the code to test the property lastname
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property mobile (base name: "Mobile")', function() {
      // uncomment below and update the code to test the property mobile
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property mondayAvailableHours (base name: "MondayAvailableHours")', function() {
      // uncomment below and update the code to test the property mondayAvailableHours
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property phone (base name: "Phone")', function() {
      // uncomment below and update the code to test the property phone
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property positionTitle (base name: "PositionTitle")', function() {
      // uncomment below and update the code to test the property positionTitle
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property roles (base name: "Roles")', function() {
      // uncomment below and update the code to test the property roles
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property saturdayAvailableHours (base name: "SaturdayAvailableHours")', function() {
      // uncomment below and update the code to test the property saturdayAvailableHours
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property sundayAvailableHours (base name: "SundayAvailableHours")', function() {
      // uncomment below and update the code to test the property sundayAvailableHours
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property tags (base name: "Tags")', function() {
      // uncomment below and update the code to test the property tags
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property thursdayAvailableHours (base name: "ThursdayAvailableHours")', function() {
      // uncomment below and update the code to test the property thursdayAvailableHours
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property timeZone (base name: "TimeZone")', function() {
      // uncomment below and update the code to test the property timeZone
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property tuesdayAvailableHours (base name: "TuesdayAvailableHours")', function() {
      // uncomment below and update the code to test the property tuesdayAvailableHours
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property userID (base name: "UserID")', function() {
      // uncomment below and update the code to test the property userID
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property wednesdayAvailableHours (base name: "WednesdayAvailableHours")', function() {
      // uncomment below and update the code to test the property wednesdayAvailableHours
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

    it('should have the property isTeamMember (base name: "isTeamMember")', function() {
      // uncomment below and update the code to test the property isTeamMember
      //var instance = new AvazaApiDocumentation.UserDetails();
      //expect(instance).to.be();
    });

  });

}));
