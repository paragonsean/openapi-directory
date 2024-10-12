/**
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.OpenFec);
  }
}(this, function(expect, OpenFec) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
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

  describe('LegalSearchGetDefaultResponseAdvisoryOpinionsInner', function() {
    it('should create an instance of LegalSearchGetDefaultResponseAdvisoryOpinionsInner', function() {
      // uncomment below and update the code to test LegalSearchGetDefaultResponseAdvisoryOpinionsInner
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be.a(OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner);
    });

    it('should have the property aoCitations (base name: "ao_citations")', function() {
      // uncomment below and update the code to test the property aoCitations
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property aosCitedBy (base name: "aos_cited_by")', function() {
      // uncomment below and update the code to test the property aosCitedBy
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property commenterNames (base name: "commenter_names")', function() {
      // uncomment below and update the code to test the property commenterNames
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property documentHighlights (base name: "document_highlights")', function() {
      // uncomment below and update the code to test the property documentHighlights
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property documents (base name: "documents")', function() {
      // uncomment below and update the code to test the property documents
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property entities (base name: "entities")', function() {
      // uncomment below and update the code to test the property entities
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property highlights (base name: "highlights")', function() {
      // uncomment below and update the code to test the property highlights
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property isPending (base name: "is_pending")', function() {
      // uncomment below and update the code to test the property isPending
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property issueDate (base name: "issue_date")', function() {
      // uncomment below and update the code to test the property issueDate
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property _false (base name: "false")', function() {
      // uncomment below and update the code to test the property _false
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property regulatoryCitations (base name: "regulatory_citations")', function() {
      // uncomment below and update the code to test the property regulatoryCitations
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property representativeNames (base name: "representative_names")', function() {
      // uncomment below and update the code to test the property representativeNames
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property requestDate (base name: "request_date")', function() {
      // uncomment below and update the code to test the property requestDate
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property requestorNames (base name: "requestor_names")', function() {
      // uncomment below and update the code to test the property requestorNames
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property requestorTypes (base name: "requestor_types")', function() {
      // uncomment below and update the code to test the property requestorTypes
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property statutoryCitations (base name: "statutory_citations")', function() {
      // uncomment below and update the code to test the property statutoryCitations
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

    it('should have the property summary (base name: "summary")', function() {
      // uncomment below and update the code to test the property summary
      //var instance = new OpenFec.LegalSearchGetDefaultResponseAdvisoryOpinionsInner();
      //expect(instance).to.be();
    });

  });

}));
