/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
    factory(root.expect, root.MagentoB2B);
  }
}(this, function(expect, MagentoB2B) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MagentoB2B.CompanyDataCompanyInterface();
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

  describe('CompanyDataCompanyInterface', function() {
    it('should create an instance of CompanyDataCompanyInterface', function() {
      // uncomment below and update the code to test CompanyDataCompanyInterface
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be.a(MagentoB2B.CompanyDataCompanyInterface);
    });

    it('should have the property city (base name: "city")', function() {
      // uncomment below and update the code to test the property city
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property comment (base name: "comment")', function() {
      // uncomment below and update the code to test the property comment
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property companyEmail (base name: "company_email")', function() {
      // uncomment below and update the code to test the property companyEmail
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property companyName (base name: "company_name")', function() {
      // uncomment below and update the code to test the property companyName
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property countryId (base name: "country_id")', function() {
      // uncomment below and update the code to test the property countryId
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property customerGroupId (base name: "customer_group_id")', function() {
      // uncomment below and update the code to test the property customerGroupId
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property legalName (base name: "legal_name")', function() {
      // uncomment below and update the code to test the property legalName
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property postcode (base name: "postcode")', function() {
      // uncomment below and update the code to test the property postcode
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property region (base name: "region")', function() {
      // uncomment below and update the code to test the property region
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property regionId (base name: "region_id")', function() {
      // uncomment below and update the code to test the property regionId
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property rejectReason (base name: "reject_reason")', function() {
      // uncomment below and update the code to test the property rejectReason
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property rejectedAt (base name: "rejected_at")', function() {
      // uncomment below and update the code to test the property rejectedAt
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property resellerId (base name: "reseller_id")', function() {
      // uncomment below and update the code to test the property resellerId
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property salesRepresentativeId (base name: "sales_representative_id")', function() {
      // uncomment below and update the code to test the property salesRepresentativeId
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property street (base name: "street")', function() {
      // uncomment below and update the code to test the property street
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property superUserId (base name: "super_user_id")', function() {
      // uncomment below and update the code to test the property superUserId
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property telephone (base name: "telephone")', function() {
      // uncomment below and update the code to test the property telephone
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

    it('should have the property vatTaxId (base name: "vat_tax_id")', function() {
      // uncomment below and update the code to test the property vatTaxId
      //var instance = new MagentoB2B.CompanyDataCompanyInterface();
      //expect(instance).to.be();
    });

  });

}));
