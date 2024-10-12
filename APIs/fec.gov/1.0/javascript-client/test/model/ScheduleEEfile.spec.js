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
    instance = new OpenFec.ScheduleEEfile();
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

  describe('ScheduleEEfile', function() {
    it('should create an instance of ScheduleEEfile', function() {
      // uncomment below and update the code to test ScheduleEEfile
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be.a(OpenFec.ScheduleEEfile);
    });

    it('should have the property amendmentIndicator (base name: "amendment_indicator")', function() {
      // uncomment below and update the code to test the property amendmentIndicator
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property backReferenceScheduleName (base name: "back_reference_schedule_name")', function() {
      // uncomment below and update the code to test the property backReferenceScheduleName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property backReferenceTransactionId (base name: "back_reference_transaction_id")', function() {
      // uncomment below and update the code to test the property backReferenceTransactionId
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property beginningImageNumber (base name: "beginning_image_number")', function() {
      // uncomment below and update the code to test the property beginningImageNumber
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateFirstName (base name: "candidate_first_name")', function() {
      // uncomment below and update the code to test the property candidateFirstName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateId (base name: "candidate_id")', function() {
      // uncomment below and update the code to test the property candidateId
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateMiddleName (base name: "candidate_middle_name")', function() {
      // uncomment below and update the code to test the property candidateMiddleName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateName (base name: "candidate_name")', function() {
      // uncomment below and update the code to test the property candidateName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateOffice (base name: "candidate_office")', function() {
      // uncomment below and update the code to test the property candidateOffice
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateOfficeDistrict (base name: "candidate_office_district")', function() {
      // uncomment below and update the code to test the property candidateOfficeDistrict
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateOfficeState (base name: "candidate_office_state")', function() {
      // uncomment below and update the code to test the property candidateOfficeState
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateParty (base name: "candidate_party")', function() {
      // uncomment below and update the code to test the property candidateParty
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidatePrefix (base name: "candidate_prefix")', function() {
      // uncomment below and update the code to test the property candidatePrefix
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property candidateSuffix (base name: "candidate_suffix")', function() {
      // uncomment below and update the code to test the property candidateSuffix
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property categoryCode (base name: "category_code")', function() {
      // uncomment below and update the code to test the property categoryCode
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property committee (base name: "committee")', function() {
      // uncomment below and update the code to test the property committee
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property committeeId (base name: "committee_id")', function() {
      // uncomment below and update the code to test the property committeeId
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property csvUrl (base name: "csv_url")', function() {
      // uncomment below and update the code to test the property csvUrl
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property disseminationDate (base name: "dissemination_date")', function() {
      // uncomment below and update the code to test the property disseminationDate
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property entityType (base name: "entity_type")', function() {
      // uncomment below and update the code to test the property entityType
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property expenditureAmount (base name: "expenditure_amount")', function() {
      // uncomment below and update the code to test the property expenditureAmount
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property expenditureDate (base name: "expenditure_date")', function() {
      // uncomment below and update the code to test the property expenditureDate
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property expenditureDescription (base name: "expenditure_description")', function() {
      // uncomment below and update the code to test the property expenditureDescription
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property fecUrl (base name: "fec_url")', function() {
      // uncomment below and update the code to test the property fecUrl
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property fileNumber (base name: "file_number")', function() {
      // uncomment below and update the code to test the property fileNumber
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property filerFirstName (base name: "filer_first_name")', function() {
      // uncomment below and update the code to test the property filerFirstName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property filerLastName (base name: "filer_last_name")', function() {
      // uncomment below and update the code to test the property filerLastName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property filerMiddleName (base name: "filer_middle_name")', function() {
      // uncomment below and update the code to test the property filerMiddleName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property filerPrefix (base name: "filer_prefix")', function() {
      // uncomment below and update the code to test the property filerPrefix
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property filerSuffix (base name: "filer_suffix")', function() {
      // uncomment below and update the code to test the property filerSuffix
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property filing (base name: "filing")', function() {
      // uncomment below and update the code to test the property filing
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property filingForm (base name: "filing_form")', function() {
      // uncomment below and update the code to test the property filingForm
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property imageNumber (base name: "image_number")', function() {
      // uncomment below and update the code to test the property imageNumber
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property isNotice (base name: "is_notice")', function() {
      // uncomment below and update the code to test the property isNotice
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property lineNumber (base name: "line_number")', function() {
      // uncomment below and update the code to test the property lineNumber
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property loadTimestamp (base name: "load_timestamp")', function() {
      // uncomment below and update the code to test the property loadTimestamp
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property memoCode (base name: "memo_code")', function() {
      // uncomment below and update the code to test the property memoCode
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property memoText (base name: "memo_text")', function() {
      // uncomment below and update the code to test the property memoText
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property mostRecent (base name: "most_recent")', function() {
      // uncomment below and update the code to test the property mostRecent
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property notarySignDate (base name: "notary_sign_date")', function() {
      // uncomment below and update the code to test the property notarySignDate
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property officeTotalYtd (base name: "office_total_ytd")', function() {
      // uncomment below and update the code to test the property officeTotalYtd
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeCity (base name: "payee_city")', function() {
      // uncomment below and update the code to test the property payeeCity
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeFirstName (base name: "payee_first_name")', function() {
      // uncomment below and update the code to test the property payeeFirstName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeLastName (base name: "payee_last_name")', function() {
      // uncomment below and update the code to test the property payeeLastName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeMiddleName (base name: "payee_middle_name")', function() {
      // uncomment below and update the code to test the property payeeMiddleName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeName (base name: "payee_name")', function() {
      // uncomment below and update the code to test the property payeeName
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeePrefix (base name: "payee_prefix")', function() {
      // uncomment below and update the code to test the property payeePrefix
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeState (base name: "payee_state")', function() {
      // uncomment below and update the code to test the property payeeState
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeStreet1 (base name: "payee_street_1")', function() {
      // uncomment below and update the code to test the property payeeStreet1
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeStreet2 (base name: "payee_street_2")', function() {
      // uncomment below and update the code to test the property payeeStreet2
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeSuffix (base name: "payee_suffix")', function() {
      // uncomment below and update the code to test the property payeeSuffix
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property payeeZip (base name: "payee_zip")', function() {
      // uncomment below and update the code to test the property payeeZip
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property pdfUrl (base name: "pdf_url")', function() {
      // uncomment below and update the code to test the property pdfUrl
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property relatedLineNumber (base name: "related_line_number")', function() {
      // uncomment below and update the code to test the property relatedLineNumber
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property reportType (base name: "report_type")', function() {
      // uncomment below and update the code to test the property reportType
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property supportOpposeIndicator (base name: "support_oppose_indicator")', function() {
      // uncomment below and update the code to test the property supportOpposeIndicator
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

    it('should have the property transactionId (base name: "transaction_id")', function() {
      // uncomment below and update the code to test the property transactionId
      //var instance = new OpenFec.ScheduleEEfile();
      //expect(instance).to.be();
    });

  });

}));
