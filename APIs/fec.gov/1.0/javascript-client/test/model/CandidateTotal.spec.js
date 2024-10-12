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
    instance = new OpenFec.CandidateTotal();
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

  describe('CandidateTotal', function() {
    it('should create an instance of CandidateTotal', function() {
      // uncomment below and update the code to test CandidateTotal
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be.a(OpenFec.CandidateTotal);
    });

    it('should have the property candidateId (base name: "candidate_id")', function() {
      // uncomment below and update the code to test the property candidateId
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property candidateInactive (base name: "candidate_inactive")', function() {
      // uncomment below and update the code to test the property candidateInactive
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property cashOnHandEndPeriod (base name: "cash_on_hand_end_period")', function() {
      // uncomment below and update the code to test the property cashOnHandEndPeriod
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property coverageEndDate (base name: "coverage_end_date")', function() {
      // uncomment below and update the code to test the property coverageEndDate
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property coverageStartDate (base name: "coverage_start_date")', function() {
      // uncomment below and update the code to test the property coverageStartDate
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property cycle (base name: "cycle")', function() {
      // uncomment below and update the code to test the property cycle
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property debtsOwedByCommittee (base name: "debts_owed_by_committee")', function() {
      // uncomment below and update the code to test the property debtsOwedByCommittee
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property disbursements (base name: "disbursements")', function() {
      // uncomment below and update the code to test the property disbursements
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property district (base name: "district")', function() {
      // uncomment below and update the code to test the property district
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property districtNumber (base name: "district_number")', function() {
      // uncomment below and update the code to test the property districtNumber
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property electionYear (base name: "election_year")', function() {
      // uncomment below and update the code to test the property electionYear
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property federalFundsFlag (base name: "federal_funds_flag")', function() {
      // uncomment below and update the code to test the property federalFundsFlag
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property hasRaisedFunds (base name: "has_raised_funds")', function() {
      // uncomment below and update the code to test the property hasRaisedFunds
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property individualItemizedContributions (base name: "individual_itemized_contributions")', function() {
      // uncomment below and update the code to test the property individualItemizedContributions
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property isElection (base name: "is_election")', function() {
      // uncomment below and update the code to test the property isElection
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property office (base name: "office")', function() {
      // uncomment below and update the code to test the property office
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property otherPoliticalCommitteeContributions (base name: "other_political_committee_contributions")', function() {
      // uncomment below and update the code to test the property otherPoliticalCommitteeContributions
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property party (base name: "party")', function() {
      // uncomment below and update the code to test the property party
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property receipts (base name: "receipts")', function() {
      // uncomment below and update the code to test the property receipts
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property stateFull (base name: "state_full")', function() {
      // uncomment below and update the code to test the property stateFull
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

    it('should have the property transfersFromOtherAuthorizedCommittee (base name: "transfers_from_other_authorized_committee")', function() {
      // uncomment below and update the code to test the property transfersFromOtherAuthorizedCommittee
      //var instance = new OpenFec.CandidateTotal();
      //expect(instance).to.be();
    });

  });

}));
