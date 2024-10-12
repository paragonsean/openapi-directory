/**
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ActivitiesGet200Response from './model/ActivitiesGet200Response';
import ActivitiesPostRequest from './model/ActivitiesPostRequest';
import Activity from './model/Activity';
import AddCompaniesVendorRequest from './model/AddCompaniesVendorRequest';
import AddContactPersonRequest from './model/AddContactPersonRequest';
import AddDefaultProjectStatusesError from './model/AddDefaultProjectStatusesError';
import AddDefaultProjectStatusesSuccess from './model/AddDefaultProjectStatusesSuccess';
import AddVendorRequest from './model/AddVendorRequest';
import BadRequestResponse from './model/BadRequestResponse';
import BadRequestResponseData from './model/BadRequestResponseData';
import BulkActionRequestBody from './model/BulkActionRequestBody';
import BulkEditIntegrationSettingsUsersItemsRequestBody from './model/BulkEditIntegrationSettingsUsersItemsRequestBody';
import BulkEditIntegrationSettingsUsersRequestBody from './model/BulkEditIntegrationSettingsUsersRequestBody';
import CitiesCityIdGet200Response from './model/CitiesCityIdGet200Response';
import CitiesGet200Response from './model/CitiesGet200Response';
import City from './model/City';
import ClockingRecord from './model/ClockingRecord';
import ClockingRecordsCheckoutPost201Response from './model/ClockingRecordsCheckoutPost201Response';
import ClockingRecordsClockingRecordIdDelete200Response from './model/ClockingRecordsClockingRecordIdDelete200Response';
import ClockingRecordsClockingRecordIdGet200Response from './model/ClockingRecordsClockingRecordIdGet200Response';
import ClockingRecordsClockingRecordIdPut200Response from './model/ClockingRecordsClockingRecordIdPut200Response';
import ClockingRecordsGet200Response from './model/ClockingRecordsGet200Response';
import ClockingRecordsPost201Response from './model/ClockingRecordsPost201Response';
import ClockingRecordsPost201ResponseData from './model/ClockingRecordsPost201ResponseData';
import ClockingRecordsPostRequest from './model/ClockingRecordsPostRequest';
import CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response from './model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response';
import CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest from './model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest';
import CompaniesCompanyIdFormTemplatesGet200Response from './model/CompaniesCompanyIdFormTemplatesGet200Response';
import CompaniesCompanyIdGet200Response from './model/CompaniesCompanyIdGet200Response';
import CompaniesCompanyIdIntegrationFeatureSettingsGet200Response from './model/CompaniesCompanyIdIntegrationFeatureSettingsGet200Response';
import CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response from './model/CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response';
import CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response from './model/CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response';
import CompaniesCompanyIdIntegrationSettingsGet200Response from './model/CompaniesCompanyIdIntegrationSettingsGet200Response';
import CompaniesCompanyIdIntegrationSettingsPostRequest from './model/CompaniesCompanyIdIntegrationSettingsPostRequest';
import CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response from './model/CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response';
import CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest from './model/CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest';
import CompaniesFormTemplates from './model/CompaniesFormTemplates';
import CompaniesGet200Response from './model/CompaniesGet200Response';
import CompaniesIntegrationFeatureSetting from './model/CompaniesIntegrationFeatureSetting';
import CompaniesIntegrationSetting from './model/CompaniesIntegrationSetting';
import CompaniesSubscriptionSelfServiceGet200Response from './model/CompaniesSubscriptionSelfServiceGet200Response';
import CompaniesVendor from './model/CompaniesVendor';
import Company from './model/Company';
import CompanyPriceMargins from './model/CompanyPriceMargins';
import CompanySettings from './model/CompanySettings';
import Contact from './model/Contact';
import ContactCustomFieldAttribute from './model/ContactCustomFieldAttribute';
import ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response from './model/ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response';
import ContactCustomFieldAttributesGet200Response from './model/ContactCustomFieldAttributesGet200Response';
import ContactCustomFieldValue from './model/ContactCustomFieldValue';
import ContactPerson from './model/ContactPerson';
import ContactType from './model/ContactType';
import ContactTypesContactTypeIdGet200Response from './model/ContactTypesContactTypeIdGet200Response';
import ContactTypesGet200Response from './model/ContactTypesGet200Response';
import ContactsContactIdContactCustomFieldValuesGet200Response from './model/ContactsContactIdContactCustomFieldValuesGet200Response';
import ContactsContactIdGet200Response from './model/ContactsContactIdGet200Response';
import ContactsGet200Response from './model/ContactsGet200Response';
import ContactsPostRequest from './model/ContactsPostRequest';
import ContactsPostRequestContactTypes from './model/ContactsPostRequestContactTypes';
import Countries from './model/Countries';
import CountriesCountryIdGet200Response from './model/CountriesCountryIdGet200Response';
import CountriesGet200Response from './model/CountriesGet200Response';
import CreateSuccessResponse from './model/CreateSuccessResponse';
import CurrenciesCurrencyIdGet200Response from './model/CurrenciesCurrencyIdGet200Response';
import CurrenciesGet200Response from './model/CurrenciesGet200Response';
import Currency from './model/Currency';
import DrivingType from './model/DrivingType';
import Email from './model/Email';
import EmployeeHoursGet200Response from './model/EmployeeHoursGet200Response';
import EmployeeHoursGet200ResponseDataInner from './model/EmployeeHoursGet200ResponseDataInner';
import EmptySuccessResponse from './model/EmptySuccessResponse';
import ErrorNotFound from './model/ErrorNotFound';
import ErrorNotFoundData from './model/ErrorNotFoundData';
import ErrorValidation from './model/ErrorValidation';
import ErrorValidationData from './model/ErrorValidationData';
import Event from './model/Event';
import EventsEventIdGet200Response from './model/EventsEventIdGet200Response';
import EventsGet200Response from './model/EventsGet200Response';
import EventsIsUserFreeGet200Response from './model/EventsIsUserFreeGet200Response';
import EventsPostRequest from './model/EventsPostRequest';
import Expense from './model/Expense';
import ExpenseFile from './model/ExpenseFile';
import ExpenseFilesExpenseFileIdGet200Response from './model/ExpenseFilesExpenseFileIdGet200Response';
import ExpenseFilesExpenseFileIdPut200Response from './model/ExpenseFilesExpenseFileIdPut200Response';
import ExpenseFilesGet200Response from './model/ExpenseFilesGet200Response';
import ExpenseLine from './model/ExpenseLine';
import ExpenseLinesExpenseLineIdGet200Response from './model/ExpenseLinesExpenseLineIdGet200Response';
import ExpenseLinesGet200Response from './model/ExpenseLinesGet200Response';
import ExpenseLinesPostRequest from './model/ExpenseLinesPostRequest';
import ExpensesExpenseIdGet200Response from './model/ExpensesExpenseIdGet200Response';
import ExpensesGet200Response from './model/ExpensesGet200Response';
import ExpensesHighestAmountGet200Response from './model/ExpensesHighestAmountGet200Response';
import ExpensesHighestAmountGet200ResponseDataInner from './model/ExpensesHighestAmountGet200ResponseDataInner';
import ExpensesPostRequest from './model/ExpensesPostRequest';
import FinancialStatisticsWorkingHoursGet200Response from './model/FinancialStatisticsWorkingHoursGet200Response';
import FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner from './model/FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner';
import ForbiddenError from './model/ForbiddenError';
import ForbiddenErrorData from './model/ForbiddenErrorData';
import Form from './model/Form';
import FormField from './model/FormField';
import FormFieldType from './model/FormFieldType';
import FormFieldTypesFormFieldTypeIdGet200Response from './model/FormFieldTypesFormFieldTypeIdGet200Response';
import FormFieldTypesGet200Response from './model/FormFieldTypesGet200Response';
import FormFieldsFormFieldIdGet200Response from './model/FormFieldsFormFieldIdGet200Response';
import FormFieldsPostRequest from './model/FormFieldsPostRequest';
import FormTemplate from './model/FormTemplate';
import FormTemplatesFormTemplateIdGet200Response from './model/FormTemplatesFormTemplateIdGet200Response';
import FormTemplatesGet200Response from './model/FormTemplatesGet200Response';
import FormsFormIdGet200Response from './model/FormsFormIdGet200Response';
import FormsGet200Response from './model/FormsGet200Response';
import FormsPostRequest from './model/FormsPostRequest';
import GetCompaiesVendorsList200Response from './model/GetCompaiesVendorsList200Response';
import GetCompaniesVendor200Response from './model/GetCompaniesVendor200Response';
import GetCompaniesVendorsExpenseStatistics200Response from './model/GetCompaniesVendorsExpenseStatistics200Response';
import GetCompaniesVendorsExpenseStatistics200ResponseDataInner from './model/GetCompaniesVendorsExpenseStatistics200ResponseDataInner';
import GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner from './model/GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner';
import GetCompaySettingsList200Response from './model/GetCompaySettingsList200Response';
import GetContactPerson200Response from './model/GetContactPerson200Response';
import GetContactPersonsList200Response from './model/GetContactPersonsList200Response';
import GetDrivingTypes200Response from './model/GetDrivingTypes200Response';
import GetExpensesSalesPrice200Response from './model/GetExpensesSalesPrice200Response';
import GetFinancialStatistics200Response from './model/GetFinancialStatistics200Response';
import GetFinancialStatistics200ResponseData from './model/GetFinancialStatistics200ResponseData';
import GetFinancialStatisticsOverview200Response from './model/GetFinancialStatisticsOverview200Response';
import GetFinancialStatisticsOverview200ResponseData from './model/GetFinancialStatisticsOverview200ResponseData';
import GetIntegrationsList200Response from './model/GetIntegrationsList200Response';
import GetInvoiceFiles200Response from './model/GetInvoiceFiles200Response';
import GetInvoicedAmount200Response from './model/GetInvoicedAmount200Response';
import GetMargin200Response from './model/GetMargin200Response';
import GetMaterialRentalsCostPrice200Response from './model/GetMaterialRentalsCostPrice200Response';
import GetOneInvoiceEmails200Response from './model/GetOneInvoiceEmails200Response';
import GetOneInvoiceFiles200Response from './model/GetOneInvoiceFiles200Response';
import GetProductsCostPrice200Response from './model/GetProductsCostPrice200Response';
import GetVendor200Response from './model/GetVendor200Response';
import GetVendorsList200Response from './model/GetVendorsList200Response';
import IntegrationFeatureSetting from './model/IntegrationFeatureSetting';
import IntegrationSettingsUser from './model/IntegrationSettingsUser';
import IntegrationSettingsUsers from './model/IntegrationSettingsUsers';
import IntegrationsBillysAuthenticatePost200Response from './model/IntegrationsBillysAuthenticatePost200Response';
import IntegrationsProductsSyncGet200Response from './model/IntegrationsProductsSyncGet200Response';
import Invoice from './model/Invoice';
import InvoiceFile from './model/InvoiceFile';
import InvoiceLine from './model/InvoiceLine';
import InvoiceLineText from './model/InvoiceLineText';
import InvoiceLineTextTemplate from './model/InvoiceLineTextTemplate';
import InvoiceLineTextTemplateGet200Response from './model/InvoiceLineTextTemplateGet200Response';
import InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response from './model/InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response';
import InvoiceLinesGet200Response from './model/InvoiceLinesGet200Response';
import InvoiceLinesInvoiceLineIdGet200Response from './model/InvoiceLinesInvoiceLineIdGet200Response';
import InvoiceLinesInvoiceLineIdPutRequest from './model/InvoiceLinesInvoiceLineIdPutRequest';
import InvoiceLinesPostRequest from './model/InvoiceLinesPostRequest';
import InvoicesGet200Response from './model/InvoicesGet200Response';
import InvoicesInvoiceIdGet200Response from './model/InvoicesInvoiceIdGet200Response';
import InvoicesInvoiceIdPutRequest from './model/InvoicesInvoiceIdPutRequest';
import InvoicesPostRequest from './model/InvoicesPostRequest';
import MassMessage from './model/MassMessage';
import MassMessagesUser from './model/MassMessagesUser';
import MassMessagesUsersGet200Response from './model/MassMessagesUsersGet200Response';
import MassMessagesUsersMassMessagesUserIdGet200Response from './model/MassMessagesUsersMassMessagesUserIdGet200Response';
import Material from './model/Material';
import MaterialRental from './model/MaterialRental';
import MaterialsGet200Response from './model/MaterialsGet200Response';
import MaterialsMaterialIdGet200Response from './model/MaterialsMaterialIdGet200Response';
import MaterialsMaterialIdRentalsCheckoutPostRequest from './model/MaterialsMaterialIdRentalsCheckoutPostRequest';
import MaterialsMaterialIdRentalsGet200Response from './model/MaterialsMaterialIdRentalsGet200Response';
import MaterialsMaterialIdRentalsMaterialRentalIdGet200Response from './model/MaterialsMaterialIdRentalsMaterialRentalIdGet200Response';
import MaterialsMaterialIdRentalsPostRequest from './model/MaterialsMaterialIdRentalsPostRequest';
import MaterialsPostRequest from './model/MaterialsPostRequest';
import Offer from './model/Offer';
import OfferLine from './model/OfferLine';
import OfferStatus from './model/OfferStatus';
import OfferStatusesGet200Response from './model/OfferStatusesGet200Response';
import OfferStatusesOfferStatusIdGet200Response from './model/OfferStatusesOfferStatusIdGet200Response';
import OfferStatusesPostRequest from './model/OfferStatusesPostRequest';
import OffersGet200Response from './model/OffersGet200Response';
import OffersOfferIdChangelogGet200Response from './model/OffersOfferIdChangelogGet200Response';
import OffersOfferIdGet200Response from './model/OffersOfferIdGet200Response';
import OffersPostRequest from './model/OffersPostRequest';
import OverviewRejectionReasonsGet200Response from './model/OverviewRejectionReasonsGet200Response';
import PaginationDetails from './model/PaginationDetails';
import PaymentTerm from './model/PaymentTerm';
import PaymentTermType from './model/PaymentTermType';
import PaymentTermTypesGet200Response from './model/PaymentTermTypesGet200Response';
import PaymentTermTypesPaymentTermTypeIdGet200Response from './model/PaymentTermTypesPaymentTermTypeIdGet200Response';
import PaymentTermsData from './model/PaymentTermsData';
import PaymentTermsErpGet200Response from './model/PaymentTermsErpGet200Response';
import PaymentTermsGet200Response from './model/PaymentTermsGet200Response';
import PaymentTermsPaymentTermIdGet200Response from './model/PaymentTermsPaymentTermIdGet200Response';
import PingGet200Response from './model/PingGet200Response';
import PlannedProduct from './model/PlannedProduct';
import PostDrivingTypesRequest from './model/PostDrivingTypesRequest';
import Product from './model/Product';
import ProductVariant from './model/ProductVariant';
import ProductsGet200Response from './model/ProductsGet200Response';
import ProductsPostRequest from './model/ProductsPostRequest';
import ProductsProductIdGet200Response from './model/ProductsProductIdGet200Response';
import ProductsProductIdVariantsGet200Response from './model/ProductsProductIdVariantsGet200Response';
import Project from './model/Project';
import ProjectCustomFieldAttribute from './model/ProjectCustomFieldAttribute';
import ProjectCustomFieldAttributesGet200Response from './model/ProjectCustomFieldAttributesGet200Response';
import ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response from './model/ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response';
import ProjectCustomFieldValue from './model/ProjectCustomFieldValue';
import ProjectStatus from './model/ProjectStatus';
import ProjectStatusType from './model/ProjectStatusType';
import ProjectStatusTypesGet200Response from './model/ProjectStatusTypesGet200Response';
import ProjectStatusesGet200Response from './model/ProjectStatusesGet200Response';
import ProjectStatusesPostRequest from './model/ProjectStatusesPostRequest';
import ProjectStatusesProjectStatusIdGet200Response from './model/ProjectStatusesProjectStatusIdGet200Response';
import ProjectsGet200Response from './model/ProjectsGet200Response';
import ProjectsHasProjectsWithCustomStatusesGet200Response from './model/ProjectsHasProjectsWithCustomStatusesGet200Response';
import ProjectsPostRequest from './model/ProjectsPostRequest';
import ProjectsProjectIdAllFilesGet200Response from './model/ProjectsProjectIdAllFilesGet200Response';
import ProjectsProjectIdGet200Response from './model/ProjectsProjectIdGet200Response';
import ProjectsProjectIdPutRequest from './model/ProjectsProjectIdPutRequest';
import ProjectsProjectIdSendBulkPdfPostRequest from './model/ProjectsProjectIdSendBulkPdfPostRequest';
import ProjectsProjectIdUsersGet200Response from './model/ProjectsProjectIdUsersGet200Response';
import ProjectsProjectIdUsersPostRequest from './model/ProjectsProjectIdUsersPostRequest';
import ProjectsProjectIdUsersUserIdGet200Response from './model/ProjectsProjectIdUsersUserIdGet200Response';
import Role from './model/Role';
import RolesGet200Response from './model/RolesGet200Response';
import Sender from './model/Sender';
import SharedProjectContact from './model/SharedProjectContact';
import SharedProjectVendor from './model/SharedProjectVendor';
import StockLocation from './model/StockLocation';
import StockLocationsGet200Response from './model/StockLocationsGet200Response';
import StockLocationsLocationIdGet200Response from './model/StockLocationsLocationIdGet200Response';
import StockLocationsPostRequest from './model/StockLocationsPostRequest';
import SubscriptionSelfServiceRequestBody from './model/SubscriptionSelfServiceRequestBody';
import TimeEntriesGet200Response from './model/TimeEntriesGet200Response';
import TimeEntriesPostRequest from './model/TimeEntriesPostRequest';
import TimeEntriesTimeEntryIdGet200Response from './model/TimeEntriesTimeEntryIdGet200Response';
import TimeEntry from './model/TimeEntry';
import TimeEntryInterval from './model/TimeEntryInterval';
import TimeEntryIntervalsGet200Response from './model/TimeEntryIntervalsGet200Response';
import TimeEntryIntervalsTimeEntryIntervalIdGet200Response from './model/TimeEntryIntervalsTimeEntryIntervalIdGet200Response';
import TimeEntryRate from './model/TimeEntryRate';
import TimeEntryRatesGet200Response from './model/TimeEntryRatesGet200Response';
import TimeEntryRatesTimeEntryRateIdGet200Response from './model/TimeEntryRatesTimeEntryRateIdGet200Response';
import TimeEntryRuleGroup from './model/TimeEntryRuleGroup';
import TimeEntryRuleGroupsGet200Response from './model/TimeEntryRuleGroupsGet200Response';
import TimeEntryType from './model/TimeEntryType';
import TimeEntryTypesGet200Response from './model/TimeEntryTypesGet200Response';
import TimeEntryTypesPostRequest from './model/TimeEntryTypesPostRequest';
import TimeEntryTypesTimeEntryTypeIdGet200Response from './model/TimeEntryTypesTimeEntryTypeIdGet200Response';
import TimeEntryUnitType from './model/TimeEntryUnitType';
import TimeEntryUnitTypesGet200Response from './model/TimeEntryUnitTypesGet200Response';
import TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response from './model/TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response';
import TimeEntryValueType from './model/TimeEntryValueType';
import TimeEntryValueTypesGet200Response from './model/TimeEntryValueTypesGet200Response';
import TimeEntryValueTypesTimeEntryValueTypeIdGet200Response from './model/TimeEntryValueTypesTimeEntryValueTypeIdGet200Response';
import UnauthorizedError from './model/UnauthorizedError';
import UnauthorizedErrorData from './model/UnauthorizedErrorData';
import User from './model/User';
import UserCustomFieldAttribute from './model/UserCustomFieldAttribute';
import UserCustomFieldAttributesGet200Response from './model/UserCustomFieldAttributesGet200Response';
import UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response from './model/UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response';
import UserCustomFieldValue from './model/UserCustomFieldValue';
import UsersPostRequest from './model/UsersPostRequest';
import UsersResendWelcomeSmsGet200Response from './model/UsersResendWelcomeSmsGet200Response';
import UsersResendWelcomeSmsGet200ResponseData from './model/UsersResendWelcomeSmsGet200ResponseData';
import UsersUserIdIntegrationSettingsGet200Response from './model/UsersUserIdIntegrationSettingsGet200Response';
import UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response from './model/UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response';
import UsersUserIdUserCustomFieldValueGet200Response from './model/UsersUserIdUserCustomFieldValueGet200Response';
import UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response from './model/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response';
import UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response from './model/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response';
import Vendor from './model/Vendor';
import VendorProduct from './model/VendorProduct';
import VendorProductPriceFile from './model/VendorProductPriceFile';
import VendorProductPriceFilesGet200Response from './model/VendorProductPriceFilesGet200Response';
import VendorProductPriceFilesVendorProductPriceFileIdGet200Response from './model/VendorProductPriceFilesVendorProductPriceFileIdGet200Response';
import VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData from './model/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData';
import VendorProductsGet200Response from './model/VendorProductsGet200Response';
import VendorProductsVendorProductIdGet200Response from './model/VendorProductsVendorProductIdGet200Response';
import WallComment from './model/WallComment';
import WallCommentsPostRequest from './model/WallCommentsPostRequest';
import WallCommentsWallCommentIdGet200Response from './model/WallCommentsWallCommentIdGet200Response';
import WallPost from './model/WallPost';
import WallPostsGet200Response from './model/WallPostsGet200Response';
import WallPostsPostRequest from './model/WallPostsPostRequest';
import WallPostsWallPostIdGet200Response from './model/WallPostsWallPostIdGet200Response';
import WallPostsWallPostIdWallCommentsGet200Response from './model/WallPostsWallPostIdWallCommentsGet200Response';
import ActivitiesApi from './api/ActivitiesApi';
import ChangelogApi from './api/ChangelogApi';
import CitiesApi from './api/CitiesApi';
import ClockingRecordsApi from './api/ClockingRecordsApi';
import CompaniesApi from './api/CompaniesApi';
import CompaniesVendorsApi from './api/CompaniesVendorsApi';
import CompanySettingsApi from './api/CompanySettingsApi';
import ContactCustomFieldAttributesApi from './api/ContactCustomFieldAttributesApi';
import ContactCustomFieldValueApi from './api/ContactCustomFieldValueApi';
import ContactPersonsApi from './api/ContactPersonsApi';
import ContactTypesApi from './api/ContactTypesApi';
import ContactsApi from './api/ContactsApi';
import CountriesApi from './api/CountriesApi';
import CurrenciesApi from './api/CurrenciesApi';
import DefaultProjectStatusesApi from './api/DefaultProjectStatusesApi';
import DrivingTypesApi from './api/DrivingTypesApi';
import EmployeeHoursApi from './api/EmployeeHoursApi';
import EventsApi from './api/EventsApi';
import ExpenseFilesApi from './api/ExpenseFilesApi';
import ExpenseLinesApi from './api/ExpenseLinesApi';
import ExpenseOIOUBLFilesApi from './api/ExpenseOIOUBLFilesApi';
import ExpensesApi from './api/ExpensesApi';
import FinancialStatisticsApi from './api/FinancialStatisticsApi';
import FormFieldTypesApi from './api/FormFieldTypesApi';
import FormFieldsApi from './api/FormFieldsApi';
import FormTemplatesApi from './api/FormTemplatesApi';
import FormsApi from './api/FormsApi';
import IntegrationsApi from './api/IntegrationsApi';
import InvoiceEmailsApi from './api/InvoiceEmailsApi';
import InvoiceFilesApi from './api/InvoiceFilesApi';
import InvoiceLineTextTemplatesApi from './api/InvoiceLineTextTemplatesApi';
import InvoiceLinesApi from './api/InvoiceLinesApi';
import InvoicesApi from './api/InvoicesApi';
import MassMessagesUsersApi from './api/MassMessagesUsersApi';
import MaterialRentalsApi from './api/MaterialRentalsApi';
import MaterialsApi from './api/MaterialsApi';
import OfferStatusesApi from './api/OfferStatusesApi';
import OffersApi from './api/OffersApi';
import PaymentTermTypesApi from './api/PaymentTermTypesApi';
import PaymentTermsApi from './api/PaymentTermsApi';
import PingApi from './api/PingApi';
import ProductVariantsApi from './api/ProductVariantsApi';
import ProductsApi from './api/ProductsApi';
import ProjectCustomFieldAttributesApi from './api/ProjectCustomFieldAttributesApi';
import ProjectStatusTypesApi from './api/ProjectStatusTypesApi';
import ProjectStatusesApi from './api/ProjectStatusesApi';
import ProjectsApi from './api/ProjectsApi';
import RejectionReasonsApi from './api/RejectionReasonsApi';
import ReportsApi from './api/ReportsApi';
import RolesApi from './api/RolesApi';
import StockLocationsApi from './api/StockLocationsApi';
import TimeEntriesApi from './api/TimeEntriesApi';
import TimeEntryIntervalsApi from './api/TimeEntryIntervalsApi';
import TimeEntryRateApi from './api/TimeEntryRateApi';
import TimeEntryRatesApi from './api/TimeEntryRatesApi';
import TimeEntryRuleGroupsApi from './api/TimeEntryRuleGroupsApi';
import TimeEntryTypesApi from './api/TimeEntryTypesApi';
import TimeEntryUnitTypesApi from './api/TimeEntryUnitTypesApi';
import TimeEntryValueTypesApi from './api/TimeEntryValueTypesApi';
import UserCustomFieldAttributesApi from './api/UserCustomFieldAttributesApi';
import UserCustomFieldValueApi from './api/UserCustomFieldValueApi';
import UsersApi from './api/UsersApi';
import VendorProductPriceFilesApi from './api/VendorProductPriceFilesApi';
import VendorProductsApi from './api/VendorProductsApi';
import VendorsApi from './api/VendorsApi';
import WagesApi from './api/WagesApi';
import WallCommentsApi from './api/WallCommentsApi';
import WallPostsApi from './api/WallPostsApi';


/**
* API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint &#x60;https://app.apacta.com/api/v1&#x60; should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending &#x60;?api_key&#x3D;{api_key}&#x60; to the URL where &#x60;{api_key}&#x60; is found within Apacta settings is used for authentication # Pagination If the endpoint returns a &#x60;pagination&#x60; object it means the endpoint supports pagination - currently it&#39;s only possible to change pages with &#x60;?page&#x3D;{page_number}&#x60; but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints&#39; docs for further explanation. # Ordering Is currently experimental, but on some endpoints it&#39;s implemented on URL querys so eg. to order Invoices by &#x60;invoice_number&#x60; appending &#x60;?sort&#x3D;Invoices.invoice_number&amp;direction&#x3D;desc&#x60; would sort the list descending by the value of &#x60;invoice_number&#x60;. # Associations Is currently implemented on an experimental basis where you can append eg. &#x60;?include&#x3D;Contacts,Projects&#x60;  to the &#x60;/api/v1/invoices/&#x60; endpoint to embed &#x60;Contact&#x60; and &#x60;Project&#x60; objects directly. # Project Files Currently project files can be retrieved from two endpoints. &#x60;/projects/{project_id}/files&#x60; handles files uploaded from wall posts or forms. &#x60;/projects/{project_id}/project_files&#x60; allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the &#x60;errors&#x60; object contains keys with the properties that failes validation like: &#x60;&#x60;&#x60;   {       \&quot;success\&quot;: false,       \&quot;data\&quot;: {           \&quot;code\&quot;: 422,           \&quot;url\&quot;: \&quot;/api/v1/contacts?api_key&#x3D;5523be3b-30ef-425d-8203-04df7caaa93a\&quot;,           \&quot;message\&quot;: \&quot;A validation error occurred\&quot;,           \&quot;errorCount\&quot;: 1,           \&quot;errors\&quot;: {               \&quot;contact_types\&quot;: [ ## Property name that failed validation                   \&quot;Contacts must have at least one contact type\&quot; ## Message with further explanation               ]           }       }   } &#x60;&#x60;&#x60; ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift &#x60;&#x60;&#x60; &#x60;&#x60;&#x60; ### Java #### OkHttp &#x60;&#x60;&#x60;   OkHttpClient client &#x3D; new OkHttpClient();    Request request &#x3D; new Request.Builder()     .url(\&quot;https://app.apacta.com/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5\&quot;)     .get()     .addHeader(\&quot;x-auth-token\&quot;, \&quot;{INSERT_YOUR_TOKEN}\&quot;)     .addHeader(\&quot;accept\&quot;, \&quot;application/json\&quot;)     .build();    Response response &#x3D; client.newCall(request).execute(); &#x60;&#x60;&#x60; #### Unirest &#x60;&#x60;&#x60;   HttpResponse&lt;String&gt; response &#x3D; Unirest.get(\&quot;https://app.apacta.com/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5\&quot;)     .header(\&quot;x-auth-token\&quot;, \&quot;{INSERT_YOUR_TOKEN}\&quot;)     .header(\&quot;accept\&quot;, \&quot;application/json\&quot;)     .asString(); &#x60;&#x60;&#x60; ### Javascript #### Native &#x60;&#x60;&#x60;   var data &#x3D; null;    var xhr &#x3D; new XMLHttpRequest();    xhr.addEventListener(\&quot;readystatechange\&quot;, function () {     if (this.readyState &#x3D;&#x3D;&#x3D; 4) {       console.log(this.responseText);     }   });    xhr.open(\&quot;GET\&quot;, \&quot;https://app.apacta.com/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5\&quot;);   xhr.setRequestHeader(\&quot;x-auth-token\&quot;, \&quot;{INSERT_YOUR_TOKEN}\&quot;);   xhr.setRequestHeader(\&quot;accept\&quot;, \&quot;application/json\&quot;);    xhr.send(data); &#x60;&#x60;&#x60; #### jQuery &#x60;&#x60;&#x60;   var settings &#x3D; {     \&quot;async\&quot;: true,     \&quot;crossDomain\&quot;: true,     \&quot;url\&quot;: \&quot;https://app.apacta.com/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5\&quot;,     \&quot;method\&quot;: \&quot;GET\&quot;,     \&quot;headers\&quot;: {       \&quot;x-auth-token\&quot;: \&quot;{INSERT_YOUR_TOKEN}\&quot;,       \&quot;accept\&quot;: \&quot;application/json\&quot;,     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); &#x60;&#x60;&#x60; #### NodeJS (Request) &#x60;&#x60;&#x60;   var request &#x3D; require(\&quot;request\&quot;);    var options &#x3D; { method: &#39;GET&#39;,     url: &#39;https://app.apacta.com/api/v1/forms&#39;,     qs:      { extended: &#39;true&#39;,        sort: &#39;Forms.created&#39;,        direction: &#39;DESC&#39;,        include: &#39;Products,CreatedBy&#39;,        limit: &#39;5&#39; },     headers:      { accept: &#39;application/json&#39;,        &#39;x-auth-token&#39;: &#39;{INSERT_YOUR_TOKEN}&#39; } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  &#x60;&#x60;&#x60; ### Python 3 &#x60;&#x60;&#x60;   import http.client    conn &#x3D; http.client.HTTPSConnection(\&quot;app.apacta.com\&quot;)    payload &#x3D; \&quot;\&quot;    headers &#x3D; {       &#39;x-auth-token&#39;: \&quot;{INSERT_YOUR_TOKEN}\&quot;,       &#39;accept&#39;: \&quot;application/json\&quot;,       }    conn.request(\&quot;GET\&quot;, \&quot;/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5\&quot;, payload, headers)    res &#x3D; conn.getresponse()   data &#x3D; res.read()    print(data.decode(\&quot;utf-8\&quot;)) &#x60;&#x60;&#x60; ### C# #### RestSharp &#x60;&#x60;&#x60;   var client &#x3D; new RestClient(\&quot;https://app.apacta.com/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5\&quot;);   var request &#x3D; new RestRequest(Method.GET);   request.AddHeader(\&quot;accept\&quot;, \&quot;application/json\&quot;);   request.AddHeader(\&quot;x-auth-token\&quot;, \&quot;{INSERT_YOUR_TOKEN}\&quot;);   IRestResponse response &#x3D; client.Execute(request); &#x60;&#x60;&#x60; ### Ruby &#x60;&#x60;&#x60;   require &#39;uri&#39;   require &#39;net/http&#39;    url &#x3D; URI(\&quot;https://app.apacta.com/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5\&quot;)    http &#x3D; Net::HTTP.new(url.host, url.port)   http.use_ssl &#x3D; true   http.verify_mode &#x3D; OpenSSL::SSL::VERIFY_NONE    request &#x3D; Net::HTTP::Get.new(url)   request[\&quot;x-auth-token\&quot;] &#x3D; &#39;{INSERT_YOUR_TOKEN}&#39;   request[\&quot;accept\&quot;] &#x3D; &#39;application/json&#39;    response &#x3D; http.request(request)   puts response.read_body &#x60;&#x60;&#x60; ### PHP (HttpRequest) &#x60;&#x60;&#x60;   &lt;?php    $request &#x3D; new HttpRequest();   $request-&gt;setUrl(&#39;https://app.apacta.com/api/v1/forms&#39;);   $request-&gt;setMethod(HTTP_METH_GET);    $request-&gt;setQueryData(array(     &#39;extended&#39; &#x3D;&gt; &#39;true&#39;,     &#39;sort&#39; &#x3D;&gt; &#39;Forms.created&#39;,     &#39;direction&#39; &#x3D;&gt; &#39;DESC&#39;,     &#39;include&#39; &#x3D;&gt; &#39;Products,CreatedBy&#39;,     &#39;limit&#39; &#x3D;&gt; &#39;5&#39;   ));    $request-&gt;setHeaders(array(     &#39;accept&#39; &#x3D;&gt; &#39;application/json&#39;,     &#39;x-auth-token&#39; &#x3D;&gt; &#39;{INSERT_YOUR_TOKEN}&#39;   ));    try {     $response &#x3D; $request-&gt;send();      echo $response-&gt;getBody();   } catch (HttpException $ex) {     echo $ex;   } &#x60;&#x60;&#x60; ### Shell (cURL) &#x60;&#x60;&#x60;    $ curl --request GET --url &#39;https://app.apacta.com/api/v1/forms?extended&#x3D;true&amp;sort&#x3D;Forms.created&amp;direction&#x3D;DESC&amp;include&#x3D;Products%2CCreatedBy&amp;limit&#x3D;5&#39; --header &#39;accept: application/json&#39; --header &#39;x-auth-token: {INSERT_YOUR_TOKEN}&#39;  &#x60;&#x60;&#x60;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var Apacta = require('index'); // See note below*.
* var xxxSvc = new Apacta.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new Apacta.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new Apacta.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new Apacta.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 0.0.42
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ActivitiesGet200Response model constructor.
     * @property {module:model/ActivitiesGet200Response}
     */
    ActivitiesGet200Response,

    /**
     * The ActivitiesPostRequest model constructor.
     * @property {module:model/ActivitiesPostRequest}
     */
    ActivitiesPostRequest,

    /**
     * The Activity model constructor.
     * @property {module:model/Activity}
     */
    Activity,

    /**
     * The AddCompaniesVendorRequest model constructor.
     * @property {module:model/AddCompaniesVendorRequest}
     */
    AddCompaniesVendorRequest,

    /**
     * The AddContactPersonRequest model constructor.
     * @property {module:model/AddContactPersonRequest}
     */
    AddContactPersonRequest,

    /**
     * The AddDefaultProjectStatusesError model constructor.
     * @property {module:model/AddDefaultProjectStatusesError}
     */
    AddDefaultProjectStatusesError,

    /**
     * The AddDefaultProjectStatusesSuccess model constructor.
     * @property {module:model/AddDefaultProjectStatusesSuccess}
     */
    AddDefaultProjectStatusesSuccess,

    /**
     * The AddVendorRequest model constructor.
     * @property {module:model/AddVendorRequest}
     */
    AddVendorRequest,

    /**
     * The BadRequestResponse model constructor.
     * @property {module:model/BadRequestResponse}
     */
    BadRequestResponse,

    /**
     * The BadRequestResponseData model constructor.
     * @property {module:model/BadRequestResponseData}
     */
    BadRequestResponseData,

    /**
     * The BulkActionRequestBody model constructor.
     * @property {module:model/BulkActionRequestBody}
     */
    BulkActionRequestBody,

    /**
     * The BulkEditIntegrationSettingsUsersItemsRequestBody model constructor.
     * @property {module:model/BulkEditIntegrationSettingsUsersItemsRequestBody}
     */
    BulkEditIntegrationSettingsUsersItemsRequestBody,

    /**
     * The BulkEditIntegrationSettingsUsersRequestBody model constructor.
     * @property {module:model/BulkEditIntegrationSettingsUsersRequestBody}
     */
    BulkEditIntegrationSettingsUsersRequestBody,

    /**
     * The CitiesCityIdGet200Response model constructor.
     * @property {module:model/CitiesCityIdGet200Response}
     */
    CitiesCityIdGet200Response,

    /**
     * The CitiesGet200Response model constructor.
     * @property {module:model/CitiesGet200Response}
     */
    CitiesGet200Response,

    /**
     * The City model constructor.
     * @property {module:model/City}
     */
    City,

    /**
     * The ClockingRecord model constructor.
     * @property {module:model/ClockingRecord}
     */
    ClockingRecord,

    /**
     * The ClockingRecordsCheckoutPost201Response model constructor.
     * @property {module:model/ClockingRecordsCheckoutPost201Response}
     */
    ClockingRecordsCheckoutPost201Response,

    /**
     * The ClockingRecordsClockingRecordIdDelete200Response model constructor.
     * @property {module:model/ClockingRecordsClockingRecordIdDelete200Response}
     */
    ClockingRecordsClockingRecordIdDelete200Response,

    /**
     * The ClockingRecordsClockingRecordIdGet200Response model constructor.
     * @property {module:model/ClockingRecordsClockingRecordIdGet200Response}
     */
    ClockingRecordsClockingRecordIdGet200Response,

    /**
     * The ClockingRecordsClockingRecordIdPut200Response model constructor.
     * @property {module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    ClockingRecordsClockingRecordIdPut200Response,

    /**
     * The ClockingRecordsGet200Response model constructor.
     * @property {module:model/ClockingRecordsGet200Response}
     */
    ClockingRecordsGet200Response,

    /**
     * The ClockingRecordsPost201Response model constructor.
     * @property {module:model/ClockingRecordsPost201Response}
     */
    ClockingRecordsPost201Response,

    /**
     * The ClockingRecordsPost201ResponseData model constructor.
     * @property {module:model/ClockingRecordsPost201ResponseData}
     */
    ClockingRecordsPost201ResponseData,

    /**
     * The ClockingRecordsPostRequest model constructor.
     * @property {module:model/ClockingRecordsPostRequest}
     */
    ClockingRecordsPostRequest,

    /**
     * The CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response}
     */
    CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response,

    /**
     * The CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest model constructor.
     * @property {module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest}
     */
    CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest,

    /**
     * The CompaniesCompanyIdFormTemplatesGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdFormTemplatesGet200Response}
     */
    CompaniesCompanyIdFormTemplatesGet200Response,

    /**
     * The CompaniesCompanyIdGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdGet200Response}
     */
    CompaniesCompanyIdGet200Response,

    /**
     * The CompaniesCompanyIdIntegrationFeatureSettingsGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdIntegrationFeatureSettingsGet200Response}
     */
    CompaniesCompanyIdIntegrationFeatureSettingsGet200Response,

    /**
     * The CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response}
     */
    CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response,

    /**
     * The CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response}
     */
    CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response,

    /**
     * The CompaniesCompanyIdIntegrationSettingsGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdIntegrationSettingsGet200Response}
     */
    CompaniesCompanyIdIntegrationSettingsGet200Response,

    /**
     * The CompaniesCompanyIdIntegrationSettingsPostRequest model constructor.
     * @property {module:model/CompaniesCompanyIdIntegrationSettingsPostRequest}
     */
    CompaniesCompanyIdIntegrationSettingsPostRequest,

    /**
     * The CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response model constructor.
     * @property {module:model/CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response}
     */
    CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response,

    /**
     * The CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest model constructor.
     * @property {module:model/CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest}
     */
    CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest,

    /**
     * The CompaniesFormTemplates model constructor.
     * @property {module:model/CompaniesFormTemplates}
     */
    CompaniesFormTemplates,

    /**
     * The CompaniesGet200Response model constructor.
     * @property {module:model/CompaniesGet200Response}
     */
    CompaniesGet200Response,

    /**
     * The CompaniesIntegrationFeatureSetting model constructor.
     * @property {module:model/CompaniesIntegrationFeatureSetting}
     */
    CompaniesIntegrationFeatureSetting,

    /**
     * The CompaniesIntegrationSetting model constructor.
     * @property {module:model/CompaniesIntegrationSetting}
     */
    CompaniesIntegrationSetting,

    /**
     * The CompaniesSubscriptionSelfServiceGet200Response model constructor.
     * @property {module:model/CompaniesSubscriptionSelfServiceGet200Response}
     */
    CompaniesSubscriptionSelfServiceGet200Response,

    /**
     * The CompaniesVendor model constructor.
     * @property {module:model/CompaniesVendor}
     */
    CompaniesVendor,

    /**
     * The Company model constructor.
     * @property {module:model/Company}
     */
    Company,

    /**
     * The CompanyPriceMargins model constructor.
     * @property {module:model/CompanyPriceMargins}
     */
    CompanyPriceMargins,

    /**
     * The CompanySettings model constructor.
     * @property {module:model/CompanySettings}
     */
    CompanySettings,

    /**
     * The Contact model constructor.
     * @property {module:model/Contact}
     */
    Contact,

    /**
     * The ContactCustomFieldAttribute model constructor.
     * @property {module:model/ContactCustomFieldAttribute}
     */
    ContactCustomFieldAttribute,

    /**
     * The ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response model constructor.
     * @property {module:model/ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response}
     */
    ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response,

    /**
     * The ContactCustomFieldAttributesGet200Response model constructor.
     * @property {module:model/ContactCustomFieldAttributesGet200Response}
     */
    ContactCustomFieldAttributesGet200Response,

    /**
     * The ContactCustomFieldValue model constructor.
     * @property {module:model/ContactCustomFieldValue}
     */
    ContactCustomFieldValue,

    /**
     * The ContactPerson model constructor.
     * @property {module:model/ContactPerson}
     */
    ContactPerson,

    /**
     * The ContactType model constructor.
     * @property {module:model/ContactType}
     */
    ContactType,

    /**
     * The ContactTypesContactTypeIdGet200Response model constructor.
     * @property {module:model/ContactTypesContactTypeIdGet200Response}
     */
    ContactTypesContactTypeIdGet200Response,

    /**
     * The ContactTypesGet200Response model constructor.
     * @property {module:model/ContactTypesGet200Response}
     */
    ContactTypesGet200Response,

    /**
     * The ContactsContactIdContactCustomFieldValuesGet200Response model constructor.
     * @property {module:model/ContactsContactIdContactCustomFieldValuesGet200Response}
     */
    ContactsContactIdContactCustomFieldValuesGet200Response,

    /**
     * The ContactsContactIdGet200Response model constructor.
     * @property {module:model/ContactsContactIdGet200Response}
     */
    ContactsContactIdGet200Response,

    /**
     * The ContactsGet200Response model constructor.
     * @property {module:model/ContactsGet200Response}
     */
    ContactsGet200Response,

    /**
     * The ContactsPostRequest model constructor.
     * @property {module:model/ContactsPostRequest}
     */
    ContactsPostRequest,

    /**
     * The ContactsPostRequestContactTypes model constructor.
     * @property {module:model/ContactsPostRequestContactTypes}
     */
    ContactsPostRequestContactTypes,

    /**
     * The Countries model constructor.
     * @property {module:model/Countries}
     */
    Countries,

    /**
     * The CountriesCountryIdGet200Response model constructor.
     * @property {module:model/CountriesCountryIdGet200Response}
     */
    CountriesCountryIdGet200Response,

    /**
     * The CountriesGet200Response model constructor.
     * @property {module:model/CountriesGet200Response}
     */
    CountriesGet200Response,

    /**
     * The CreateSuccessResponse model constructor.
     * @property {module:model/CreateSuccessResponse}
     */
    CreateSuccessResponse,

    /**
     * The CurrenciesCurrencyIdGet200Response model constructor.
     * @property {module:model/CurrenciesCurrencyIdGet200Response}
     */
    CurrenciesCurrencyIdGet200Response,

    /**
     * The CurrenciesGet200Response model constructor.
     * @property {module:model/CurrenciesGet200Response}
     */
    CurrenciesGet200Response,

    /**
     * The Currency model constructor.
     * @property {module:model/Currency}
     */
    Currency,

    /**
     * The DrivingType model constructor.
     * @property {module:model/DrivingType}
     */
    DrivingType,

    /**
     * The Email model constructor.
     * @property {module:model/Email}
     */
    Email,

    /**
     * The EmployeeHoursGet200Response model constructor.
     * @property {module:model/EmployeeHoursGet200Response}
     */
    EmployeeHoursGet200Response,

    /**
     * The EmployeeHoursGet200ResponseDataInner model constructor.
     * @property {module:model/EmployeeHoursGet200ResponseDataInner}
     */
    EmployeeHoursGet200ResponseDataInner,

    /**
     * The EmptySuccessResponse model constructor.
     * @property {module:model/EmptySuccessResponse}
     */
    EmptySuccessResponse,

    /**
     * The ErrorNotFound model constructor.
     * @property {module:model/ErrorNotFound}
     */
    ErrorNotFound,

    /**
     * The ErrorNotFoundData model constructor.
     * @property {module:model/ErrorNotFoundData}
     */
    ErrorNotFoundData,

    /**
     * The ErrorValidation model constructor.
     * @property {module:model/ErrorValidation}
     */
    ErrorValidation,

    /**
     * The ErrorValidationData model constructor.
     * @property {module:model/ErrorValidationData}
     */
    ErrorValidationData,

    /**
     * The Event model constructor.
     * @property {module:model/Event}
     */
    Event,

    /**
     * The EventsEventIdGet200Response model constructor.
     * @property {module:model/EventsEventIdGet200Response}
     */
    EventsEventIdGet200Response,

    /**
     * The EventsGet200Response model constructor.
     * @property {module:model/EventsGet200Response}
     */
    EventsGet200Response,

    /**
     * The EventsIsUserFreeGet200Response model constructor.
     * @property {module:model/EventsIsUserFreeGet200Response}
     */
    EventsIsUserFreeGet200Response,

    /**
     * The EventsPostRequest model constructor.
     * @property {module:model/EventsPostRequest}
     */
    EventsPostRequest,

    /**
     * The Expense model constructor.
     * @property {module:model/Expense}
     */
    Expense,

    /**
     * The ExpenseFile model constructor.
     * @property {module:model/ExpenseFile}
     */
    ExpenseFile,

    /**
     * The ExpenseFilesExpenseFileIdGet200Response model constructor.
     * @property {module:model/ExpenseFilesExpenseFileIdGet200Response}
     */
    ExpenseFilesExpenseFileIdGet200Response,

    /**
     * The ExpenseFilesExpenseFileIdPut200Response model constructor.
     * @property {module:model/ExpenseFilesExpenseFileIdPut200Response}
     */
    ExpenseFilesExpenseFileIdPut200Response,

    /**
     * The ExpenseFilesGet200Response model constructor.
     * @property {module:model/ExpenseFilesGet200Response}
     */
    ExpenseFilesGet200Response,

    /**
     * The ExpenseLine model constructor.
     * @property {module:model/ExpenseLine}
     */
    ExpenseLine,

    /**
     * The ExpenseLinesExpenseLineIdGet200Response model constructor.
     * @property {module:model/ExpenseLinesExpenseLineIdGet200Response}
     */
    ExpenseLinesExpenseLineIdGet200Response,

    /**
     * The ExpenseLinesGet200Response model constructor.
     * @property {module:model/ExpenseLinesGet200Response}
     */
    ExpenseLinesGet200Response,

    /**
     * The ExpenseLinesPostRequest model constructor.
     * @property {module:model/ExpenseLinesPostRequest}
     */
    ExpenseLinesPostRequest,

    /**
     * The ExpensesExpenseIdGet200Response model constructor.
     * @property {module:model/ExpensesExpenseIdGet200Response}
     */
    ExpensesExpenseIdGet200Response,

    /**
     * The ExpensesGet200Response model constructor.
     * @property {module:model/ExpensesGet200Response}
     */
    ExpensesGet200Response,

    /**
     * The ExpensesHighestAmountGet200Response model constructor.
     * @property {module:model/ExpensesHighestAmountGet200Response}
     */
    ExpensesHighestAmountGet200Response,

    /**
     * The ExpensesHighestAmountGet200ResponseDataInner model constructor.
     * @property {module:model/ExpensesHighestAmountGet200ResponseDataInner}
     */
    ExpensesHighestAmountGet200ResponseDataInner,

    /**
     * The ExpensesPostRequest model constructor.
     * @property {module:model/ExpensesPostRequest}
     */
    ExpensesPostRequest,

    /**
     * The FinancialStatisticsWorkingHoursGet200Response model constructor.
     * @property {module:model/FinancialStatisticsWorkingHoursGet200Response}
     */
    FinancialStatisticsWorkingHoursGet200Response,

    /**
     * The FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner model constructor.
     * @property {module:model/FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner}
     */
    FinancialStatisticsWorkingHoursGet200ResponseTimeEntriesInner,

    /**
     * The ForbiddenError model constructor.
     * @property {module:model/ForbiddenError}
     */
    ForbiddenError,

    /**
     * The ForbiddenErrorData model constructor.
     * @property {module:model/ForbiddenErrorData}
     */
    ForbiddenErrorData,

    /**
     * The Form model constructor.
     * @property {module:model/Form}
     */
    Form,

    /**
     * The FormField model constructor.
     * @property {module:model/FormField}
     */
    FormField,

    /**
     * The FormFieldType model constructor.
     * @property {module:model/FormFieldType}
     */
    FormFieldType,

    /**
     * The FormFieldTypesFormFieldTypeIdGet200Response model constructor.
     * @property {module:model/FormFieldTypesFormFieldTypeIdGet200Response}
     */
    FormFieldTypesFormFieldTypeIdGet200Response,

    /**
     * The FormFieldTypesGet200Response model constructor.
     * @property {module:model/FormFieldTypesGet200Response}
     */
    FormFieldTypesGet200Response,

    /**
     * The FormFieldsFormFieldIdGet200Response model constructor.
     * @property {module:model/FormFieldsFormFieldIdGet200Response}
     */
    FormFieldsFormFieldIdGet200Response,

    /**
     * The FormFieldsPostRequest model constructor.
     * @property {module:model/FormFieldsPostRequest}
     */
    FormFieldsPostRequest,

    /**
     * The FormTemplate model constructor.
     * @property {module:model/FormTemplate}
     */
    FormTemplate,

    /**
     * The FormTemplatesFormTemplateIdGet200Response model constructor.
     * @property {module:model/FormTemplatesFormTemplateIdGet200Response}
     */
    FormTemplatesFormTemplateIdGet200Response,

    /**
     * The FormTemplatesGet200Response model constructor.
     * @property {module:model/FormTemplatesGet200Response}
     */
    FormTemplatesGet200Response,

    /**
     * The FormsFormIdGet200Response model constructor.
     * @property {module:model/FormsFormIdGet200Response}
     */
    FormsFormIdGet200Response,

    /**
     * The FormsGet200Response model constructor.
     * @property {module:model/FormsGet200Response}
     */
    FormsGet200Response,

    /**
     * The FormsPostRequest model constructor.
     * @property {module:model/FormsPostRequest}
     */
    FormsPostRequest,

    /**
     * The GetCompaiesVendorsList200Response model constructor.
     * @property {module:model/GetCompaiesVendorsList200Response}
     */
    GetCompaiesVendorsList200Response,

    /**
     * The GetCompaniesVendor200Response model constructor.
     * @property {module:model/GetCompaniesVendor200Response}
     */
    GetCompaniesVendor200Response,

    /**
     * The GetCompaniesVendorsExpenseStatistics200Response model constructor.
     * @property {module:model/GetCompaniesVendorsExpenseStatistics200Response}
     */
    GetCompaniesVendorsExpenseStatistics200Response,

    /**
     * The GetCompaniesVendorsExpenseStatistics200ResponseDataInner model constructor.
     * @property {module:model/GetCompaniesVendorsExpenseStatistics200ResponseDataInner}
     */
    GetCompaniesVendorsExpenseStatistics200ResponseDataInner,

    /**
     * The GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner model constructor.
     * @property {module:model/GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner}
     */
    GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner,

    /**
     * The GetCompaySettingsList200Response model constructor.
     * @property {module:model/GetCompaySettingsList200Response}
     */
    GetCompaySettingsList200Response,

    /**
     * The GetContactPerson200Response model constructor.
     * @property {module:model/GetContactPerson200Response}
     */
    GetContactPerson200Response,

    /**
     * The GetContactPersonsList200Response model constructor.
     * @property {module:model/GetContactPersonsList200Response}
     */
    GetContactPersonsList200Response,

    /**
     * The GetDrivingTypes200Response model constructor.
     * @property {module:model/GetDrivingTypes200Response}
     */
    GetDrivingTypes200Response,

    /**
     * The GetExpensesSalesPrice200Response model constructor.
     * @property {module:model/GetExpensesSalesPrice200Response}
     */
    GetExpensesSalesPrice200Response,

    /**
     * The GetFinancialStatistics200Response model constructor.
     * @property {module:model/GetFinancialStatistics200Response}
     */
    GetFinancialStatistics200Response,

    /**
     * The GetFinancialStatistics200ResponseData model constructor.
     * @property {module:model/GetFinancialStatistics200ResponseData}
     */
    GetFinancialStatistics200ResponseData,

    /**
     * The GetFinancialStatisticsOverview200Response model constructor.
     * @property {module:model/GetFinancialStatisticsOverview200Response}
     */
    GetFinancialStatisticsOverview200Response,

    /**
     * The GetFinancialStatisticsOverview200ResponseData model constructor.
     * @property {module:model/GetFinancialStatisticsOverview200ResponseData}
     */
    GetFinancialStatisticsOverview200ResponseData,

    /**
     * The GetIntegrationsList200Response model constructor.
     * @property {module:model/GetIntegrationsList200Response}
     */
    GetIntegrationsList200Response,

    /**
     * The GetInvoiceFiles200Response model constructor.
     * @property {module:model/GetInvoiceFiles200Response}
     */
    GetInvoiceFiles200Response,

    /**
     * The GetInvoicedAmount200Response model constructor.
     * @property {module:model/GetInvoicedAmount200Response}
     */
    GetInvoicedAmount200Response,

    /**
     * The GetMargin200Response model constructor.
     * @property {module:model/GetMargin200Response}
     */
    GetMargin200Response,

    /**
     * The GetMaterialRentalsCostPrice200Response model constructor.
     * @property {module:model/GetMaterialRentalsCostPrice200Response}
     */
    GetMaterialRentalsCostPrice200Response,

    /**
     * The GetOneInvoiceEmails200Response model constructor.
     * @property {module:model/GetOneInvoiceEmails200Response}
     */
    GetOneInvoiceEmails200Response,

    /**
     * The GetOneInvoiceFiles200Response model constructor.
     * @property {module:model/GetOneInvoiceFiles200Response}
     */
    GetOneInvoiceFiles200Response,

    /**
     * The GetProductsCostPrice200Response model constructor.
     * @property {module:model/GetProductsCostPrice200Response}
     */
    GetProductsCostPrice200Response,

    /**
     * The GetVendor200Response model constructor.
     * @property {module:model/GetVendor200Response}
     */
    GetVendor200Response,

    /**
     * The GetVendorsList200Response model constructor.
     * @property {module:model/GetVendorsList200Response}
     */
    GetVendorsList200Response,

    /**
     * The IntegrationFeatureSetting model constructor.
     * @property {module:model/IntegrationFeatureSetting}
     */
    IntegrationFeatureSetting,

    /**
     * The IntegrationSettingsUser model constructor.
     * @property {module:model/IntegrationSettingsUser}
     */
    IntegrationSettingsUser,

    /**
     * The IntegrationSettingsUsers model constructor.
     * @property {module:model/IntegrationSettingsUsers}
     */
    IntegrationSettingsUsers,

    /**
     * The IntegrationsBillysAuthenticatePost200Response model constructor.
     * @property {module:model/IntegrationsBillysAuthenticatePost200Response}
     */
    IntegrationsBillysAuthenticatePost200Response,

    /**
     * The IntegrationsProductsSyncGet200Response model constructor.
     * @property {module:model/IntegrationsProductsSyncGet200Response}
     */
    IntegrationsProductsSyncGet200Response,

    /**
     * The Invoice model constructor.
     * @property {module:model/Invoice}
     */
    Invoice,

    /**
     * The InvoiceFile model constructor.
     * @property {module:model/InvoiceFile}
     */
    InvoiceFile,

    /**
     * The InvoiceLine model constructor.
     * @property {module:model/InvoiceLine}
     */
    InvoiceLine,

    /**
     * The InvoiceLineText model constructor.
     * @property {module:model/InvoiceLineText}
     */
    InvoiceLineText,

    /**
     * The InvoiceLineTextTemplate model constructor.
     * @property {module:model/InvoiceLineTextTemplate}
     */
    InvoiceLineTextTemplate,

    /**
     * The InvoiceLineTextTemplateGet200Response model constructor.
     * @property {module:model/InvoiceLineTextTemplateGet200Response}
     */
    InvoiceLineTextTemplateGet200Response,

    /**
     * The InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response model constructor.
     * @property {module:model/InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response}
     */
    InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response,

    /**
     * The InvoiceLinesGet200Response model constructor.
     * @property {module:model/InvoiceLinesGet200Response}
     */
    InvoiceLinesGet200Response,

    /**
     * The InvoiceLinesInvoiceLineIdGet200Response model constructor.
     * @property {module:model/InvoiceLinesInvoiceLineIdGet200Response}
     */
    InvoiceLinesInvoiceLineIdGet200Response,

    /**
     * The InvoiceLinesInvoiceLineIdPutRequest model constructor.
     * @property {module:model/InvoiceLinesInvoiceLineIdPutRequest}
     */
    InvoiceLinesInvoiceLineIdPutRequest,

    /**
     * The InvoiceLinesPostRequest model constructor.
     * @property {module:model/InvoiceLinesPostRequest}
     */
    InvoiceLinesPostRequest,

    /**
     * The InvoicesGet200Response model constructor.
     * @property {module:model/InvoicesGet200Response}
     */
    InvoicesGet200Response,

    /**
     * The InvoicesInvoiceIdGet200Response model constructor.
     * @property {module:model/InvoicesInvoiceIdGet200Response}
     */
    InvoicesInvoiceIdGet200Response,

    /**
     * The InvoicesInvoiceIdPutRequest model constructor.
     * @property {module:model/InvoicesInvoiceIdPutRequest}
     */
    InvoicesInvoiceIdPutRequest,

    /**
     * The InvoicesPostRequest model constructor.
     * @property {module:model/InvoicesPostRequest}
     */
    InvoicesPostRequest,

    /**
     * The MassMessage model constructor.
     * @property {module:model/MassMessage}
     */
    MassMessage,

    /**
     * The MassMessagesUser model constructor.
     * @property {module:model/MassMessagesUser}
     */
    MassMessagesUser,

    /**
     * The MassMessagesUsersGet200Response model constructor.
     * @property {module:model/MassMessagesUsersGet200Response}
     */
    MassMessagesUsersGet200Response,

    /**
     * The MassMessagesUsersMassMessagesUserIdGet200Response model constructor.
     * @property {module:model/MassMessagesUsersMassMessagesUserIdGet200Response}
     */
    MassMessagesUsersMassMessagesUserIdGet200Response,

    /**
     * The Material model constructor.
     * @property {module:model/Material}
     */
    Material,

    /**
     * The MaterialRental model constructor.
     * @property {module:model/MaterialRental}
     */
    MaterialRental,

    /**
     * The MaterialsGet200Response model constructor.
     * @property {module:model/MaterialsGet200Response}
     */
    MaterialsGet200Response,

    /**
     * The MaterialsMaterialIdGet200Response model constructor.
     * @property {module:model/MaterialsMaterialIdGet200Response}
     */
    MaterialsMaterialIdGet200Response,

    /**
     * The MaterialsMaterialIdRentalsCheckoutPostRequest model constructor.
     * @property {module:model/MaterialsMaterialIdRentalsCheckoutPostRequest}
     */
    MaterialsMaterialIdRentalsCheckoutPostRequest,

    /**
     * The MaterialsMaterialIdRentalsGet200Response model constructor.
     * @property {module:model/MaterialsMaterialIdRentalsGet200Response}
     */
    MaterialsMaterialIdRentalsGet200Response,

    /**
     * The MaterialsMaterialIdRentalsMaterialRentalIdGet200Response model constructor.
     * @property {module:model/MaterialsMaterialIdRentalsMaterialRentalIdGet200Response}
     */
    MaterialsMaterialIdRentalsMaterialRentalIdGet200Response,

    /**
     * The MaterialsMaterialIdRentalsPostRequest model constructor.
     * @property {module:model/MaterialsMaterialIdRentalsPostRequest}
     */
    MaterialsMaterialIdRentalsPostRequest,

    /**
     * The MaterialsPostRequest model constructor.
     * @property {module:model/MaterialsPostRequest}
     */
    MaterialsPostRequest,

    /**
     * The Offer model constructor.
     * @property {module:model/Offer}
     */
    Offer,

    /**
     * The OfferLine model constructor.
     * @property {module:model/OfferLine}
     */
    OfferLine,

    /**
     * The OfferStatus model constructor.
     * @property {module:model/OfferStatus}
     */
    OfferStatus,

    /**
     * The OfferStatusesGet200Response model constructor.
     * @property {module:model/OfferStatusesGet200Response}
     */
    OfferStatusesGet200Response,

    /**
     * The OfferStatusesOfferStatusIdGet200Response model constructor.
     * @property {module:model/OfferStatusesOfferStatusIdGet200Response}
     */
    OfferStatusesOfferStatusIdGet200Response,

    /**
     * The OfferStatusesPostRequest model constructor.
     * @property {module:model/OfferStatusesPostRequest}
     */
    OfferStatusesPostRequest,

    /**
     * The OffersGet200Response model constructor.
     * @property {module:model/OffersGet200Response}
     */
    OffersGet200Response,

    /**
     * The OffersOfferIdChangelogGet200Response model constructor.
     * @property {module:model/OffersOfferIdChangelogGet200Response}
     */
    OffersOfferIdChangelogGet200Response,

    /**
     * The OffersOfferIdGet200Response model constructor.
     * @property {module:model/OffersOfferIdGet200Response}
     */
    OffersOfferIdGet200Response,

    /**
     * The OffersPostRequest model constructor.
     * @property {module:model/OffersPostRequest}
     */
    OffersPostRequest,

    /**
     * The OverviewRejectionReasonsGet200Response model constructor.
     * @property {module:model/OverviewRejectionReasonsGet200Response}
     */
    OverviewRejectionReasonsGet200Response,

    /**
     * The PaginationDetails model constructor.
     * @property {module:model/PaginationDetails}
     */
    PaginationDetails,

    /**
     * The PaymentTerm model constructor.
     * @property {module:model/PaymentTerm}
     */
    PaymentTerm,

    /**
     * The PaymentTermType model constructor.
     * @property {module:model/PaymentTermType}
     */
    PaymentTermType,

    /**
     * The PaymentTermTypesGet200Response model constructor.
     * @property {module:model/PaymentTermTypesGet200Response}
     */
    PaymentTermTypesGet200Response,

    /**
     * The PaymentTermTypesPaymentTermTypeIdGet200Response model constructor.
     * @property {module:model/PaymentTermTypesPaymentTermTypeIdGet200Response}
     */
    PaymentTermTypesPaymentTermTypeIdGet200Response,

    /**
     * The PaymentTermsData model constructor.
     * @property {module:model/PaymentTermsData}
     */
    PaymentTermsData,

    /**
     * The PaymentTermsErpGet200Response model constructor.
     * @property {module:model/PaymentTermsErpGet200Response}
     */
    PaymentTermsErpGet200Response,

    /**
     * The PaymentTermsGet200Response model constructor.
     * @property {module:model/PaymentTermsGet200Response}
     */
    PaymentTermsGet200Response,

    /**
     * The PaymentTermsPaymentTermIdGet200Response model constructor.
     * @property {module:model/PaymentTermsPaymentTermIdGet200Response}
     */
    PaymentTermsPaymentTermIdGet200Response,

    /**
     * The PingGet200Response model constructor.
     * @property {module:model/PingGet200Response}
     */
    PingGet200Response,

    /**
     * The PlannedProduct model constructor.
     * @property {module:model/PlannedProduct}
     */
    PlannedProduct,

    /**
     * The PostDrivingTypesRequest model constructor.
     * @property {module:model/PostDrivingTypesRequest}
     */
    PostDrivingTypesRequest,

    /**
     * The Product model constructor.
     * @property {module:model/Product}
     */
    Product,

    /**
     * The ProductVariant model constructor.
     * @property {module:model/ProductVariant}
     */
    ProductVariant,

    /**
     * The ProductsGet200Response model constructor.
     * @property {module:model/ProductsGet200Response}
     */
    ProductsGet200Response,

    /**
     * The ProductsPostRequest model constructor.
     * @property {module:model/ProductsPostRequest}
     */
    ProductsPostRequest,

    /**
     * The ProductsProductIdGet200Response model constructor.
     * @property {module:model/ProductsProductIdGet200Response}
     */
    ProductsProductIdGet200Response,

    /**
     * The ProductsProductIdVariantsGet200Response model constructor.
     * @property {module:model/ProductsProductIdVariantsGet200Response}
     */
    ProductsProductIdVariantsGet200Response,

    /**
     * The Project model constructor.
     * @property {module:model/Project}
     */
    Project,

    /**
     * The ProjectCustomFieldAttribute model constructor.
     * @property {module:model/ProjectCustomFieldAttribute}
     */
    ProjectCustomFieldAttribute,

    /**
     * The ProjectCustomFieldAttributesGet200Response model constructor.
     * @property {module:model/ProjectCustomFieldAttributesGet200Response}
     */
    ProjectCustomFieldAttributesGet200Response,

    /**
     * The ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response model constructor.
     * @property {module:model/ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response}
     */
    ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response,

    /**
     * The ProjectCustomFieldValue model constructor.
     * @property {module:model/ProjectCustomFieldValue}
     */
    ProjectCustomFieldValue,

    /**
     * The ProjectStatus model constructor.
     * @property {module:model/ProjectStatus}
     */
    ProjectStatus,

    /**
     * The ProjectStatusType model constructor.
     * @property {module:model/ProjectStatusType}
     */
    ProjectStatusType,

    /**
     * The ProjectStatusTypesGet200Response model constructor.
     * @property {module:model/ProjectStatusTypesGet200Response}
     */
    ProjectStatusTypesGet200Response,

    /**
     * The ProjectStatusesGet200Response model constructor.
     * @property {module:model/ProjectStatusesGet200Response}
     */
    ProjectStatusesGet200Response,

    /**
     * The ProjectStatusesPostRequest model constructor.
     * @property {module:model/ProjectStatusesPostRequest}
     */
    ProjectStatusesPostRequest,

    /**
     * The ProjectStatusesProjectStatusIdGet200Response model constructor.
     * @property {module:model/ProjectStatusesProjectStatusIdGet200Response}
     */
    ProjectStatusesProjectStatusIdGet200Response,

    /**
     * The ProjectsGet200Response model constructor.
     * @property {module:model/ProjectsGet200Response}
     */
    ProjectsGet200Response,

    /**
     * The ProjectsHasProjectsWithCustomStatusesGet200Response model constructor.
     * @property {module:model/ProjectsHasProjectsWithCustomStatusesGet200Response}
     */
    ProjectsHasProjectsWithCustomStatusesGet200Response,

    /**
     * The ProjectsPostRequest model constructor.
     * @property {module:model/ProjectsPostRequest}
     */
    ProjectsPostRequest,

    /**
     * The ProjectsProjectIdAllFilesGet200Response model constructor.
     * @property {module:model/ProjectsProjectIdAllFilesGet200Response}
     */
    ProjectsProjectIdAllFilesGet200Response,

    /**
     * The ProjectsProjectIdGet200Response model constructor.
     * @property {module:model/ProjectsProjectIdGet200Response}
     */
    ProjectsProjectIdGet200Response,

    /**
     * The ProjectsProjectIdPutRequest model constructor.
     * @property {module:model/ProjectsProjectIdPutRequest}
     */
    ProjectsProjectIdPutRequest,

    /**
     * The ProjectsProjectIdSendBulkPdfPostRequest model constructor.
     * @property {module:model/ProjectsProjectIdSendBulkPdfPostRequest}
     */
    ProjectsProjectIdSendBulkPdfPostRequest,

    /**
     * The ProjectsProjectIdUsersGet200Response model constructor.
     * @property {module:model/ProjectsProjectIdUsersGet200Response}
     */
    ProjectsProjectIdUsersGet200Response,

    /**
     * The ProjectsProjectIdUsersPostRequest model constructor.
     * @property {module:model/ProjectsProjectIdUsersPostRequest}
     */
    ProjectsProjectIdUsersPostRequest,

    /**
     * The ProjectsProjectIdUsersUserIdGet200Response model constructor.
     * @property {module:model/ProjectsProjectIdUsersUserIdGet200Response}
     */
    ProjectsProjectIdUsersUserIdGet200Response,

    /**
     * The Role model constructor.
     * @property {module:model/Role}
     */
    Role,

    /**
     * The RolesGet200Response model constructor.
     * @property {module:model/RolesGet200Response}
     */
    RolesGet200Response,

    /**
     * The Sender model constructor.
     * @property {module:model/Sender}
     */
    Sender,

    /**
     * The SharedProjectContact model constructor.
     * @property {module:model/SharedProjectContact}
     */
    SharedProjectContact,

    /**
     * The SharedProjectVendor model constructor.
     * @property {module:model/SharedProjectVendor}
     */
    SharedProjectVendor,

    /**
     * The StockLocation model constructor.
     * @property {module:model/StockLocation}
     */
    StockLocation,

    /**
     * The StockLocationsGet200Response model constructor.
     * @property {module:model/StockLocationsGet200Response}
     */
    StockLocationsGet200Response,

    /**
     * The StockLocationsLocationIdGet200Response model constructor.
     * @property {module:model/StockLocationsLocationIdGet200Response}
     */
    StockLocationsLocationIdGet200Response,

    /**
     * The StockLocationsPostRequest model constructor.
     * @property {module:model/StockLocationsPostRequest}
     */
    StockLocationsPostRequest,

    /**
     * The SubscriptionSelfServiceRequestBody model constructor.
     * @property {module:model/SubscriptionSelfServiceRequestBody}
     */
    SubscriptionSelfServiceRequestBody,

    /**
     * The TimeEntriesGet200Response model constructor.
     * @property {module:model/TimeEntriesGet200Response}
     */
    TimeEntriesGet200Response,

    /**
     * The TimeEntriesPostRequest model constructor.
     * @property {module:model/TimeEntriesPostRequest}
     */
    TimeEntriesPostRequest,

    /**
     * The TimeEntriesTimeEntryIdGet200Response model constructor.
     * @property {module:model/TimeEntriesTimeEntryIdGet200Response}
     */
    TimeEntriesTimeEntryIdGet200Response,

    /**
     * The TimeEntry model constructor.
     * @property {module:model/TimeEntry}
     */
    TimeEntry,

    /**
     * The TimeEntryInterval model constructor.
     * @property {module:model/TimeEntryInterval}
     */
    TimeEntryInterval,

    /**
     * The TimeEntryIntervalsGet200Response model constructor.
     * @property {module:model/TimeEntryIntervalsGet200Response}
     */
    TimeEntryIntervalsGet200Response,

    /**
     * The TimeEntryIntervalsTimeEntryIntervalIdGet200Response model constructor.
     * @property {module:model/TimeEntryIntervalsTimeEntryIntervalIdGet200Response}
     */
    TimeEntryIntervalsTimeEntryIntervalIdGet200Response,

    /**
     * The TimeEntryRate model constructor.
     * @property {module:model/TimeEntryRate}
     */
    TimeEntryRate,

    /**
     * The TimeEntryRatesGet200Response model constructor.
     * @property {module:model/TimeEntryRatesGet200Response}
     */
    TimeEntryRatesGet200Response,

    /**
     * The TimeEntryRatesTimeEntryRateIdGet200Response model constructor.
     * @property {module:model/TimeEntryRatesTimeEntryRateIdGet200Response}
     */
    TimeEntryRatesTimeEntryRateIdGet200Response,

    /**
     * The TimeEntryRuleGroup model constructor.
     * @property {module:model/TimeEntryRuleGroup}
     */
    TimeEntryRuleGroup,

    /**
     * The TimeEntryRuleGroupsGet200Response model constructor.
     * @property {module:model/TimeEntryRuleGroupsGet200Response}
     */
    TimeEntryRuleGroupsGet200Response,

    /**
     * The TimeEntryType model constructor.
     * @property {module:model/TimeEntryType}
     */
    TimeEntryType,

    /**
     * The TimeEntryTypesGet200Response model constructor.
     * @property {module:model/TimeEntryTypesGet200Response}
     */
    TimeEntryTypesGet200Response,

    /**
     * The TimeEntryTypesPostRequest model constructor.
     * @property {module:model/TimeEntryTypesPostRequest}
     */
    TimeEntryTypesPostRequest,

    /**
     * The TimeEntryTypesTimeEntryTypeIdGet200Response model constructor.
     * @property {module:model/TimeEntryTypesTimeEntryTypeIdGet200Response}
     */
    TimeEntryTypesTimeEntryTypeIdGet200Response,

    /**
     * The TimeEntryUnitType model constructor.
     * @property {module:model/TimeEntryUnitType}
     */
    TimeEntryUnitType,

    /**
     * The TimeEntryUnitTypesGet200Response model constructor.
     * @property {module:model/TimeEntryUnitTypesGet200Response}
     */
    TimeEntryUnitTypesGet200Response,

    /**
     * The TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response model constructor.
     * @property {module:model/TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response}
     */
    TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response,

    /**
     * The TimeEntryValueType model constructor.
     * @property {module:model/TimeEntryValueType}
     */
    TimeEntryValueType,

    /**
     * The TimeEntryValueTypesGet200Response model constructor.
     * @property {module:model/TimeEntryValueTypesGet200Response}
     */
    TimeEntryValueTypesGet200Response,

    /**
     * The TimeEntryValueTypesTimeEntryValueTypeIdGet200Response model constructor.
     * @property {module:model/TimeEntryValueTypesTimeEntryValueTypeIdGet200Response}
     */
    TimeEntryValueTypesTimeEntryValueTypeIdGet200Response,

    /**
     * The UnauthorizedError model constructor.
     * @property {module:model/UnauthorizedError}
     */
    UnauthorizedError,

    /**
     * The UnauthorizedErrorData model constructor.
     * @property {module:model/UnauthorizedErrorData}
     */
    UnauthorizedErrorData,

    /**
     * The User model constructor.
     * @property {module:model/User}
     */
    User,

    /**
     * The UserCustomFieldAttribute model constructor.
     * @property {module:model/UserCustomFieldAttribute}
     */
    UserCustomFieldAttribute,

    /**
     * The UserCustomFieldAttributesGet200Response model constructor.
     * @property {module:model/UserCustomFieldAttributesGet200Response}
     */
    UserCustomFieldAttributesGet200Response,

    /**
     * The UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response model constructor.
     * @property {module:model/UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response}
     */
    UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response,

    /**
     * The UserCustomFieldValue model constructor.
     * @property {module:model/UserCustomFieldValue}
     */
    UserCustomFieldValue,

    /**
     * The UsersPostRequest model constructor.
     * @property {module:model/UsersPostRequest}
     */
    UsersPostRequest,

    /**
     * The UsersResendWelcomeSmsGet200Response model constructor.
     * @property {module:model/UsersResendWelcomeSmsGet200Response}
     */
    UsersResendWelcomeSmsGet200Response,

    /**
     * The UsersResendWelcomeSmsGet200ResponseData model constructor.
     * @property {module:model/UsersResendWelcomeSmsGet200ResponseData}
     */
    UsersResendWelcomeSmsGet200ResponseData,

    /**
     * The UsersUserIdIntegrationSettingsGet200Response model constructor.
     * @property {module:model/UsersUserIdIntegrationSettingsGet200Response}
     */
    UsersUserIdIntegrationSettingsGet200Response,

    /**
     * The UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response model constructor.
     * @property {module:model/UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response}
     */
    UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response,

    /**
     * The UsersUserIdUserCustomFieldValueGet200Response model constructor.
     * @property {module:model/UsersUserIdUserCustomFieldValueGet200Response}
     */
    UsersUserIdUserCustomFieldValueGet200Response,

    /**
     * The UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response model constructor.
     * @property {module:model/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response}
     */
    UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response,

    /**
     * The UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response model constructor.
     * @property {module:model/UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response}
     */
    UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response,

    /**
     * The Vendor model constructor.
     * @property {module:model/Vendor}
     */
    Vendor,

    /**
     * The VendorProduct model constructor.
     * @property {module:model/VendorProduct}
     */
    VendorProduct,

    /**
     * The VendorProductPriceFile model constructor.
     * @property {module:model/VendorProductPriceFile}
     */
    VendorProductPriceFile,

    /**
     * The VendorProductPriceFilesGet200Response model constructor.
     * @property {module:model/VendorProductPriceFilesGet200Response}
     */
    VendorProductPriceFilesGet200Response,

    /**
     * The VendorProductPriceFilesVendorProductPriceFileIdGet200Response model constructor.
     * @property {module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200Response}
     */
    VendorProductPriceFilesVendorProductPriceFileIdGet200Response,

    /**
     * The VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData model constructor.
     * @property {module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData}
     */
    VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData,

    /**
     * The VendorProductsGet200Response model constructor.
     * @property {module:model/VendorProductsGet200Response}
     */
    VendorProductsGet200Response,

    /**
     * The VendorProductsVendorProductIdGet200Response model constructor.
     * @property {module:model/VendorProductsVendorProductIdGet200Response}
     */
    VendorProductsVendorProductIdGet200Response,

    /**
     * The WallComment model constructor.
     * @property {module:model/WallComment}
     */
    WallComment,

    /**
     * The WallCommentsPostRequest model constructor.
     * @property {module:model/WallCommentsPostRequest}
     */
    WallCommentsPostRequest,

    /**
     * The WallCommentsWallCommentIdGet200Response model constructor.
     * @property {module:model/WallCommentsWallCommentIdGet200Response}
     */
    WallCommentsWallCommentIdGet200Response,

    /**
     * The WallPost model constructor.
     * @property {module:model/WallPost}
     */
    WallPost,

    /**
     * The WallPostsGet200Response model constructor.
     * @property {module:model/WallPostsGet200Response}
     */
    WallPostsGet200Response,

    /**
     * The WallPostsPostRequest model constructor.
     * @property {module:model/WallPostsPostRequest}
     */
    WallPostsPostRequest,

    /**
     * The WallPostsWallPostIdGet200Response model constructor.
     * @property {module:model/WallPostsWallPostIdGet200Response}
     */
    WallPostsWallPostIdGet200Response,

    /**
     * The WallPostsWallPostIdWallCommentsGet200Response model constructor.
     * @property {module:model/WallPostsWallPostIdWallCommentsGet200Response}
     */
    WallPostsWallPostIdWallCommentsGet200Response,

    /**
    * The ActivitiesApi service constructor.
    * @property {module:api/ActivitiesApi}
    */
    ActivitiesApi,

    /**
    * The ChangelogApi service constructor.
    * @property {module:api/ChangelogApi}
    */
    ChangelogApi,

    /**
    * The CitiesApi service constructor.
    * @property {module:api/CitiesApi}
    */
    CitiesApi,

    /**
    * The ClockingRecordsApi service constructor.
    * @property {module:api/ClockingRecordsApi}
    */
    ClockingRecordsApi,

    /**
    * The CompaniesApi service constructor.
    * @property {module:api/CompaniesApi}
    */
    CompaniesApi,

    /**
    * The CompaniesVendorsApi service constructor.
    * @property {module:api/CompaniesVendorsApi}
    */
    CompaniesVendorsApi,

    /**
    * The CompanySettingsApi service constructor.
    * @property {module:api/CompanySettingsApi}
    */
    CompanySettingsApi,

    /**
    * The ContactCustomFieldAttributesApi service constructor.
    * @property {module:api/ContactCustomFieldAttributesApi}
    */
    ContactCustomFieldAttributesApi,

    /**
    * The ContactCustomFieldValueApi service constructor.
    * @property {module:api/ContactCustomFieldValueApi}
    */
    ContactCustomFieldValueApi,

    /**
    * The ContactPersonsApi service constructor.
    * @property {module:api/ContactPersonsApi}
    */
    ContactPersonsApi,

    /**
    * The ContactTypesApi service constructor.
    * @property {module:api/ContactTypesApi}
    */
    ContactTypesApi,

    /**
    * The ContactsApi service constructor.
    * @property {module:api/ContactsApi}
    */
    ContactsApi,

    /**
    * The CountriesApi service constructor.
    * @property {module:api/CountriesApi}
    */
    CountriesApi,

    /**
    * The CurrenciesApi service constructor.
    * @property {module:api/CurrenciesApi}
    */
    CurrenciesApi,

    /**
    * The DefaultProjectStatusesApi service constructor.
    * @property {module:api/DefaultProjectStatusesApi}
    */
    DefaultProjectStatusesApi,

    /**
    * The DrivingTypesApi service constructor.
    * @property {module:api/DrivingTypesApi}
    */
    DrivingTypesApi,

    /**
    * The EmployeeHoursApi service constructor.
    * @property {module:api/EmployeeHoursApi}
    */
    EmployeeHoursApi,

    /**
    * The EventsApi service constructor.
    * @property {module:api/EventsApi}
    */
    EventsApi,

    /**
    * The ExpenseFilesApi service constructor.
    * @property {module:api/ExpenseFilesApi}
    */
    ExpenseFilesApi,

    /**
    * The ExpenseLinesApi service constructor.
    * @property {module:api/ExpenseLinesApi}
    */
    ExpenseLinesApi,

    /**
    * The ExpenseOIOUBLFilesApi service constructor.
    * @property {module:api/ExpenseOIOUBLFilesApi}
    */
    ExpenseOIOUBLFilesApi,

    /**
    * The ExpensesApi service constructor.
    * @property {module:api/ExpensesApi}
    */
    ExpensesApi,

    /**
    * The FinancialStatisticsApi service constructor.
    * @property {module:api/FinancialStatisticsApi}
    */
    FinancialStatisticsApi,

    /**
    * The FormFieldTypesApi service constructor.
    * @property {module:api/FormFieldTypesApi}
    */
    FormFieldTypesApi,

    /**
    * The FormFieldsApi service constructor.
    * @property {module:api/FormFieldsApi}
    */
    FormFieldsApi,

    /**
    * The FormTemplatesApi service constructor.
    * @property {module:api/FormTemplatesApi}
    */
    FormTemplatesApi,

    /**
    * The FormsApi service constructor.
    * @property {module:api/FormsApi}
    */
    FormsApi,

    /**
    * The IntegrationsApi service constructor.
    * @property {module:api/IntegrationsApi}
    */
    IntegrationsApi,

    /**
    * The InvoiceEmailsApi service constructor.
    * @property {module:api/InvoiceEmailsApi}
    */
    InvoiceEmailsApi,

    /**
    * The InvoiceFilesApi service constructor.
    * @property {module:api/InvoiceFilesApi}
    */
    InvoiceFilesApi,

    /**
    * The InvoiceLineTextTemplatesApi service constructor.
    * @property {module:api/InvoiceLineTextTemplatesApi}
    */
    InvoiceLineTextTemplatesApi,

    /**
    * The InvoiceLinesApi service constructor.
    * @property {module:api/InvoiceLinesApi}
    */
    InvoiceLinesApi,

    /**
    * The InvoicesApi service constructor.
    * @property {module:api/InvoicesApi}
    */
    InvoicesApi,

    /**
    * The MassMessagesUsersApi service constructor.
    * @property {module:api/MassMessagesUsersApi}
    */
    MassMessagesUsersApi,

    /**
    * The MaterialRentalsApi service constructor.
    * @property {module:api/MaterialRentalsApi}
    */
    MaterialRentalsApi,

    /**
    * The MaterialsApi service constructor.
    * @property {module:api/MaterialsApi}
    */
    MaterialsApi,

    /**
    * The OfferStatusesApi service constructor.
    * @property {module:api/OfferStatusesApi}
    */
    OfferStatusesApi,

    /**
    * The OffersApi service constructor.
    * @property {module:api/OffersApi}
    */
    OffersApi,

    /**
    * The PaymentTermTypesApi service constructor.
    * @property {module:api/PaymentTermTypesApi}
    */
    PaymentTermTypesApi,

    /**
    * The PaymentTermsApi service constructor.
    * @property {module:api/PaymentTermsApi}
    */
    PaymentTermsApi,

    /**
    * The PingApi service constructor.
    * @property {module:api/PingApi}
    */
    PingApi,

    /**
    * The ProductVariantsApi service constructor.
    * @property {module:api/ProductVariantsApi}
    */
    ProductVariantsApi,

    /**
    * The ProductsApi service constructor.
    * @property {module:api/ProductsApi}
    */
    ProductsApi,

    /**
    * The ProjectCustomFieldAttributesApi service constructor.
    * @property {module:api/ProjectCustomFieldAttributesApi}
    */
    ProjectCustomFieldAttributesApi,

    /**
    * The ProjectStatusTypesApi service constructor.
    * @property {module:api/ProjectStatusTypesApi}
    */
    ProjectStatusTypesApi,

    /**
    * The ProjectStatusesApi service constructor.
    * @property {module:api/ProjectStatusesApi}
    */
    ProjectStatusesApi,

    /**
    * The ProjectsApi service constructor.
    * @property {module:api/ProjectsApi}
    */
    ProjectsApi,

    /**
    * The RejectionReasonsApi service constructor.
    * @property {module:api/RejectionReasonsApi}
    */
    RejectionReasonsApi,

    /**
    * The ReportsApi service constructor.
    * @property {module:api/ReportsApi}
    */
    ReportsApi,

    /**
    * The RolesApi service constructor.
    * @property {module:api/RolesApi}
    */
    RolesApi,

    /**
    * The StockLocationsApi service constructor.
    * @property {module:api/StockLocationsApi}
    */
    StockLocationsApi,

    /**
    * The TimeEntriesApi service constructor.
    * @property {module:api/TimeEntriesApi}
    */
    TimeEntriesApi,

    /**
    * The TimeEntryIntervalsApi service constructor.
    * @property {module:api/TimeEntryIntervalsApi}
    */
    TimeEntryIntervalsApi,

    /**
    * The TimeEntryRateApi service constructor.
    * @property {module:api/TimeEntryRateApi}
    */
    TimeEntryRateApi,

    /**
    * The TimeEntryRatesApi service constructor.
    * @property {module:api/TimeEntryRatesApi}
    */
    TimeEntryRatesApi,

    /**
    * The TimeEntryRuleGroupsApi service constructor.
    * @property {module:api/TimeEntryRuleGroupsApi}
    */
    TimeEntryRuleGroupsApi,

    /**
    * The TimeEntryTypesApi service constructor.
    * @property {module:api/TimeEntryTypesApi}
    */
    TimeEntryTypesApi,

    /**
    * The TimeEntryUnitTypesApi service constructor.
    * @property {module:api/TimeEntryUnitTypesApi}
    */
    TimeEntryUnitTypesApi,

    /**
    * The TimeEntryValueTypesApi service constructor.
    * @property {module:api/TimeEntryValueTypesApi}
    */
    TimeEntryValueTypesApi,

    /**
    * The UserCustomFieldAttributesApi service constructor.
    * @property {module:api/UserCustomFieldAttributesApi}
    */
    UserCustomFieldAttributesApi,

    /**
    * The UserCustomFieldValueApi service constructor.
    * @property {module:api/UserCustomFieldValueApi}
    */
    UserCustomFieldValueApi,

    /**
    * The UsersApi service constructor.
    * @property {module:api/UsersApi}
    */
    UsersApi,

    /**
    * The VendorProductPriceFilesApi service constructor.
    * @property {module:api/VendorProductPriceFilesApi}
    */
    VendorProductPriceFilesApi,

    /**
    * The VendorProductsApi service constructor.
    * @property {module:api/VendorProductsApi}
    */
    VendorProductsApi,

    /**
    * The VendorsApi service constructor.
    * @property {module:api/VendorsApi}
    */
    VendorsApi,

    /**
    * The WagesApi service constructor.
    * @property {module:api/WagesApi}
    */
    WagesApi,

    /**
    * The WallCommentsApi service constructor.
    * @property {module:api/WallCommentsApi}
    */
    WallCommentsApi,

    /**
    * The WallPostsApi service constructor.
    * @property {module:api/WallPostsApi}
    */
    WallPostsApi
};
