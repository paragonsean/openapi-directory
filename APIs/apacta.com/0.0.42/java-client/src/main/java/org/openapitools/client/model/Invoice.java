/*
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.Arrays;
import java.util.UUID;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * Invoice
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Invoice {
  public static final String SERIALIZED_NAME_ALL_PRODUCTS_ONE_LINE = "all_products_one_line";
  @SerializedName(SERIALIZED_NAME_ALL_PRODUCTS_ONE_LINE)
  private Boolean allProductsOneLine;

  public static final String SERIALIZED_NAME_ALL_WORKING_HOURS_ONE_LINE = "all_working_hours_one_line";
  @SerializedName(SERIALIZED_NAME_ALL_WORKING_HOURS_ONE_LINE)
  private Boolean allWorkingHoursOneLine;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private UUID companyId;

  public static final String SERIALIZED_NAME_CONTACT_ID = "contact_id";
  @SerializedName(SERIALIZED_NAME_CONTACT_ID)
  private UUID contactId;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CREATED_BY_ID = "created_by_id";
  @SerializedName(SERIALIZED_NAME_CREATED_BY_ID)
  private UUID createdById;

  public static final String SERIALIZED_NAME_CURRENCY_ID = "currency_id";
  @SerializedName(SERIALIZED_NAME_CURRENCY_ID)
  private UUID currencyId;

  public static final String SERIALIZED_NAME_DATE_FROM = "date_from";
  @SerializedName(SERIALIZED_NAME_DATE_FROM)
  private LocalDate dateFrom;

  public static final String SERIALIZED_NAME_DATE_TO = "date_to";
  @SerializedName(SERIALIZED_NAME_DATE_TO)
  private LocalDate dateTo;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private String deleted;

  public static final String SERIALIZED_NAME_DOWNLOADED = "downloaded";
  @SerializedName(SERIALIZED_NAME_DOWNLOADED)
  private String downloaded;

  public static final String SERIALIZED_NAME_ERP_ID = "erp_id";
  @SerializedName(SERIALIZED_NAME_ERP_ID)
  private String erpId;

  public static final String SERIALIZED_NAME_ERP_PAYMENT_TERM_ID = "erp_payment_term_id";
  @SerializedName(SERIALIZED_NAME_ERP_PAYMENT_TERM_ID)
  private String erpPaymentTermId;

  public static final String SERIALIZED_NAME_EU_CUSTOMER = "eu_customer";
  @SerializedName(SERIALIZED_NAME_EU_CUSTOMER)
  private Boolean euCustomer;

  public static final String SERIALIZED_NAME_GROSS_PAYMENT = "gross_payment";
  @SerializedName(SERIALIZED_NAME_GROSS_PAYMENT)
  private Float grossPayment;

  public static final String SERIALIZED_NAME_GROUP_BY_FORMS = "group_by_forms";
  @SerializedName(SERIALIZED_NAME_GROUP_BY_FORMS)
  private Boolean groupByForms;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_INCLUDE_INVOICED_LINES = "include_invoiced_lines";
  @SerializedName(SERIALIZED_NAME_INCLUDE_INVOICED_LINES)
  private Boolean includeInvoicedLines;

  public static final String SERIALIZED_NAME_INTEGRATION_ID = "integration_id";
  @SerializedName(SERIALIZED_NAME_INTEGRATION_ID)
  private UUID integrationId;

  public static final String SERIALIZED_NAME_INVOICE_NUMBER = "invoice_number";
  @SerializedName(SERIALIZED_NAME_INVOICE_NUMBER)
  private Integer invoiceNumber;

  public static final String SERIALIZED_NAME_IS_DRAFT = "is_draft";
  @SerializedName(SERIALIZED_NAME_IS_DRAFT)
  private Boolean isDraft;

  public static final String SERIALIZED_NAME_IS_FINAL_INVOICE = "is_final_invoice";
  @SerializedName(SERIALIZED_NAME_IS_FINAL_INVOICE)
  private Boolean isFinalInvoice;

  public static final String SERIALIZED_NAME_IS_LOCKED = "is_locked";
  @SerializedName(SERIALIZED_NAME_IS_LOCKED)
  private Boolean isLocked;

  public static final String SERIALIZED_NAME_IS_OFFER = "is_offer";
  @SerializedName(SERIALIZED_NAME_IS_OFFER)
  private Boolean isOffer;

  public static final String SERIALIZED_NAME_ISSUED_DATE = "issued_date";
  @SerializedName(SERIALIZED_NAME_ISSUED_DATE)
  private LocalDate issuedDate;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_NET_PAYMENT = "net_payment";
  @SerializedName(SERIALIZED_NAME_NET_PAYMENT)
  private Float netPayment;

  public static final String SERIALIZED_NAME_OFFER_NUMBER = "offer_number";
  @SerializedName(SERIALIZED_NAME_OFFER_NUMBER)
  private Integer offerNumber;

  public static final String SERIALIZED_NAME_ORDER_LINE_GROUP_ID = "order_line_group_id";
  @SerializedName(SERIALIZED_NAME_ORDER_LINE_GROUP_ID)
  private UUID orderLineGroupId;

  public static final String SERIALIZED_NAME_PAYMENT_DUE_DATE = "payment_due_date";
  @SerializedName(SERIALIZED_NAME_PAYMENT_DUE_DATE)
  private LocalDate paymentDueDate;

  public static final String SERIALIZED_NAME_PAYMENT_TERM_ID = "payment_term_id";
  @SerializedName(SERIALIZED_NAME_PAYMENT_TERM_ID)
  private UUID paymentTermId;

  public static final String SERIALIZED_NAME_PROJECT_ID = "project_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public static final String SERIALIZED_NAME_PROJECT_OVERVIEW_ATTACHED = "project_overview_attached";
  @SerializedName(SERIALIZED_NAME_PROJECT_OVERVIEW_ATTACHED)
  private Boolean projectOverviewAttached;

  public static final String SERIALIZED_NAME_REFERENCE = "reference";
  @SerializedName(SERIALIZED_NAME_REFERENCE)
  private String reference;

  public static final String SERIALIZED_NAME_SHOW_EMPLOYEE_NAME = "show_employee_name";
  @SerializedName(SERIALIZED_NAME_SHOW_EMPLOYEE_NAME)
  private Boolean showEmployeeName;

  public static final String SERIALIZED_NAME_SHOW_PRICE_PRODUCT_BUNDLE = "show_price_product_bundle";
  @SerializedName(SERIALIZED_NAME_SHOW_PRICE_PRODUCT_BUNDLE)
  private Boolean showPriceProductBundle;

  public static final String SERIALIZED_NAME_SHOW_PRICES_PRODUCTS_AND_HOURS = "show_prices_products_and_hours";
  @SerializedName(SERIALIZED_NAME_SHOW_PRICES_PRODUCTS_AND_HOURS)
  private Boolean showPricesProductsAndHours;

  public static final String SERIALIZED_NAME_SHOW_PRODUCT_IMAGES = "show_product_images";
  @SerializedName(SERIALIZED_NAME_SHOW_PRODUCT_IMAGES)
  private Boolean showProductImages;

  public static final String SERIALIZED_NAME_SHOW_PRODUCTS_PRODUCT_BUNDLE = "show_products_product_bundle";
  @SerializedName(SERIALIZED_NAME_SHOW_PRODUCTS_PRODUCT_BUNDLE)
  private Boolean showProductsProductBundle;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TOTAL_COST_PRICE = "total_cost_price";
  @SerializedName(SERIALIZED_NAME_TOTAL_COST_PRICE)
  private Float totalCostPrice;

  public static final String SERIALIZED_NAME_TOTAL_DISCOUNT_PERCENT = "total_discount_percent";
  @SerializedName(SERIALIZED_NAME_TOTAL_DISCOUNT_PERCENT)
  private Float totalDiscountPercent;

  public static final String SERIALIZED_NAME_VAT_PERCENT = "vat_percent";
  @SerializedName(SERIALIZED_NAME_VAT_PERCENT)
  private Integer vatPercent;

  public static final String SERIALIZED_NAME_VENDOR_ID = "vendor_id";
  @SerializedName(SERIALIZED_NAME_VENDOR_ID)
  private UUID vendorId;

  public Invoice() {
  }

  public Invoice(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Invoice allProductsOneLine(Boolean allProductsOneLine) {
    this.allProductsOneLine = allProductsOneLine;
    return this;
  }

  /**
   * Get allProductsOneLine
   * @return allProductsOneLine
   */
  @javax.annotation.Nullable
  public Boolean getAllProductsOneLine() {
    return allProductsOneLine;
  }

  public void setAllProductsOneLine(Boolean allProductsOneLine) {
    this.allProductsOneLine = allProductsOneLine;
  }


  public Invoice allWorkingHoursOneLine(Boolean allWorkingHoursOneLine) {
    this.allWorkingHoursOneLine = allWorkingHoursOneLine;
    return this;
  }

  /**
   * Get allWorkingHoursOneLine
   * @return allWorkingHoursOneLine
   */
  @javax.annotation.Nullable
  public Boolean getAllWorkingHoursOneLine() {
    return allWorkingHoursOneLine;
  }

  public void setAllWorkingHoursOneLine(Boolean allWorkingHoursOneLine) {
    this.allWorkingHoursOneLine = allWorkingHoursOneLine;
  }


  public Invoice companyId(UUID companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * Get companyId
   * @return companyId
   */
  @javax.annotation.Nullable
  public UUID getCompanyId() {
    return companyId;
  }

  public void setCompanyId(UUID companyId) {
    this.companyId = companyId;
  }


  public Invoice contactId(UUID contactId) {
    this.contactId = contactId;
    return this;
  }

  /**
   * Get contactId
   * @return contactId
   */
  @javax.annotation.Nullable
  public UUID getContactId() {
    return contactId;
  }

  public void setContactId(UUID contactId) {
    this.contactId = contactId;
  }


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  public Invoice createdById(UUID createdById) {
    this.createdById = createdById;
    return this;
  }

  /**
   * Get createdById
   * @return createdById
   */
  @javax.annotation.Nullable
  public UUID getCreatedById() {
    return createdById;
  }

  public void setCreatedById(UUID createdById) {
    this.createdById = createdById;
  }


  public Invoice currencyId(UUID currencyId) {
    this.currencyId = currencyId;
    return this;
  }

  /**
   * Get currencyId
   * @return currencyId
   */
  @javax.annotation.Nullable
  public UUID getCurrencyId() {
    return currencyId;
  }

  public void setCurrencyId(UUID currencyId) {
    this.currencyId = currencyId;
  }


  public Invoice dateFrom(LocalDate dateFrom) {
    this.dateFrom = dateFrom;
    return this;
  }

  /**
   * Get dateFrom
   * @return dateFrom
   */
  @javax.annotation.Nullable
  public LocalDate getDateFrom() {
    return dateFrom;
  }

  public void setDateFrom(LocalDate dateFrom) {
    this.dateFrom = dateFrom;
  }


  public Invoice dateTo(LocalDate dateTo) {
    this.dateTo = dateTo;
    return this;
  }

  /**
   * Get dateTo
   * @return dateTo
   */
  @javax.annotation.Nullable
  public LocalDate getDateTo() {
    return dateTo;
  }

  public void setDateTo(LocalDate dateTo) {
    this.dateTo = dateTo;
  }


  /**
   * Only present if it&#39;s a deleted object
   * @return deleted
   */
  @javax.annotation.Nullable
  public String getDeleted() {
    return deleted;
  }



  public Invoice downloaded(String downloaded) {
    this.downloaded = downloaded;
    return this;
  }

  /**
   * Get downloaded
   * @return downloaded
   */
  @javax.annotation.Nullable
  public String getDownloaded() {
    return downloaded;
  }

  public void setDownloaded(String downloaded) {
    this.downloaded = downloaded;
  }


  public Invoice erpId(String erpId) {
    this.erpId = erpId;
    return this;
  }

  /**
   * Get erpId
   * @return erpId
   */
  @javax.annotation.Nullable
  public String getErpId() {
    return erpId;
  }

  public void setErpId(String erpId) {
    this.erpId = erpId;
  }


  public Invoice erpPaymentTermId(String erpPaymentTermId) {
    this.erpPaymentTermId = erpPaymentTermId;
    return this;
  }

  /**
   * Get erpPaymentTermId
   * @return erpPaymentTermId
   */
  @javax.annotation.Nullable
  public String getErpPaymentTermId() {
    return erpPaymentTermId;
  }

  public void setErpPaymentTermId(String erpPaymentTermId) {
    this.erpPaymentTermId = erpPaymentTermId;
  }


  public Invoice euCustomer(Boolean euCustomer) {
    this.euCustomer = euCustomer;
    return this;
  }

  /**
   * Get euCustomer
   * @return euCustomer
   */
  @javax.annotation.Nullable
  public Boolean getEuCustomer() {
    return euCustomer;
  }

  public void setEuCustomer(Boolean euCustomer) {
    this.euCustomer = euCustomer;
  }


  public Invoice grossPayment(Float grossPayment) {
    this.grossPayment = grossPayment;
    return this;
  }

  /**
   * Get grossPayment
   * @return grossPayment
   */
  @javax.annotation.Nullable
  public Float getGrossPayment() {
    return grossPayment;
  }

  public void setGrossPayment(Float grossPayment) {
    this.grossPayment = grossPayment;
  }


  public Invoice groupByForms(Boolean groupByForms) {
    this.groupByForms = groupByForms;
    return this;
  }

  /**
   * Get groupByForms
   * @return groupByForms
   */
  @javax.annotation.Nullable
  public Boolean getGroupByForms() {
    return groupByForms;
  }

  public void setGroupByForms(Boolean groupByForms) {
    this.groupByForms = groupByForms;
  }


  public Invoice id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public Invoice includeInvoicedLines(Boolean includeInvoicedLines) {
    this.includeInvoicedLines = includeInvoicedLines;
    return this;
  }

  /**
   * Get includeInvoicedLines
   * @return includeInvoicedLines
   */
  @javax.annotation.Nullable
  public Boolean getIncludeInvoicedLines() {
    return includeInvoicedLines;
  }

  public void setIncludeInvoicedLines(Boolean includeInvoicedLines) {
    this.includeInvoicedLines = includeInvoicedLines;
  }


  public Invoice integrationId(UUID integrationId) {
    this.integrationId = integrationId;
    return this;
  }

  /**
   * Get integrationId
   * @return integrationId
   */
  @javax.annotation.Nullable
  public UUID getIntegrationId() {
    return integrationId;
  }

  public void setIntegrationId(UUID integrationId) {
    this.integrationId = integrationId;
  }


  public Invoice invoiceNumber(Integer invoiceNumber) {
    this.invoiceNumber = invoiceNumber;
    return this;
  }

  /**
   * Get invoiceNumber
   * @return invoiceNumber
   */
  @javax.annotation.Nullable
  public Integer getInvoiceNumber() {
    return invoiceNumber;
  }

  public void setInvoiceNumber(Integer invoiceNumber) {
    this.invoiceNumber = invoiceNumber;
  }


  public Invoice isDraft(Boolean isDraft) {
    this.isDraft = isDraft;
    return this;
  }

  /**
   * Get isDraft
   * @return isDraft
   */
  @javax.annotation.Nullable
  public Boolean getIsDraft() {
    return isDraft;
  }

  public void setIsDraft(Boolean isDraft) {
    this.isDraft = isDraft;
  }


  public Invoice isFinalInvoice(Boolean isFinalInvoice) {
    this.isFinalInvoice = isFinalInvoice;
    return this;
  }

  /**
   * Get isFinalInvoice
   * @return isFinalInvoice
   */
  @javax.annotation.Nullable
  public Boolean getIsFinalInvoice() {
    return isFinalInvoice;
  }

  public void setIsFinalInvoice(Boolean isFinalInvoice) {
    this.isFinalInvoice = isFinalInvoice;
  }


  public Invoice isLocked(Boolean isLocked) {
    this.isLocked = isLocked;
    return this;
  }

  /**
   * Get isLocked
   * @return isLocked
   */
  @javax.annotation.Nullable
  public Boolean getIsLocked() {
    return isLocked;
  }

  public void setIsLocked(Boolean isLocked) {
    this.isLocked = isLocked;
  }


  public Invoice isOffer(Boolean isOffer) {
    this.isOffer = isOffer;
    return this;
  }

  /**
   * Get isOffer
   * @return isOffer
   */
  @javax.annotation.Nullable
  public Boolean getIsOffer() {
    return isOffer;
  }

  public void setIsOffer(Boolean isOffer) {
    this.isOffer = isOffer;
  }


  public Invoice issuedDate(LocalDate issuedDate) {
    this.issuedDate = issuedDate;
    return this;
  }

  /**
   * Get issuedDate
   * @return issuedDate
   */
  @javax.annotation.Nullable
  public LocalDate getIssuedDate() {
    return issuedDate;
  }

  public void setIssuedDate(LocalDate issuedDate) {
    this.issuedDate = issuedDate;
  }


  public Invoice message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Invoice netPayment(Float netPayment) {
    this.netPayment = netPayment;
    return this;
  }

  /**
   * Get netPayment
   * @return netPayment
   */
  @javax.annotation.Nullable
  public Float getNetPayment() {
    return netPayment;
  }

  public void setNetPayment(Float netPayment) {
    this.netPayment = netPayment;
  }


  public Invoice offerNumber(Integer offerNumber) {
    this.offerNumber = offerNumber;
    return this;
  }

  /**
   * Get offerNumber
   * @return offerNumber
   */
  @javax.annotation.Nullable
  public Integer getOfferNumber() {
    return offerNumber;
  }

  public void setOfferNumber(Integer offerNumber) {
    this.offerNumber = offerNumber;
  }


  public Invoice orderLineGroupId(UUID orderLineGroupId) {
    this.orderLineGroupId = orderLineGroupId;
    return this;
  }

  /**
   * Get orderLineGroupId
   * @return orderLineGroupId
   */
  @javax.annotation.Nullable
  public UUID getOrderLineGroupId() {
    return orderLineGroupId;
  }

  public void setOrderLineGroupId(UUID orderLineGroupId) {
    this.orderLineGroupId = orderLineGroupId;
  }


  public Invoice paymentDueDate(LocalDate paymentDueDate) {
    this.paymentDueDate = paymentDueDate;
    return this;
  }

  /**
   * Get paymentDueDate
   * @return paymentDueDate
   */
  @javax.annotation.Nullable
  public LocalDate getPaymentDueDate() {
    return paymentDueDate;
  }

  public void setPaymentDueDate(LocalDate paymentDueDate) {
    this.paymentDueDate = paymentDueDate;
  }


  public Invoice paymentTermId(UUID paymentTermId) {
    this.paymentTermId = paymentTermId;
    return this;
  }

  /**
   * Get paymentTermId
   * @return paymentTermId
   */
  @javax.annotation.Nullable
  public UUID getPaymentTermId() {
    return paymentTermId;
  }

  public void setPaymentTermId(UUID paymentTermId) {
    this.paymentTermId = paymentTermId;
  }


  public Invoice projectId(UUID projectId) {
    this.projectId = projectId;
    return this;
  }

  /**
   * Get projectId
   * @return projectId
   */
  @javax.annotation.Nullable
  public UUID getProjectId() {
    return projectId;
  }

  public void setProjectId(UUID projectId) {
    this.projectId = projectId;
  }


  public Invoice projectOverviewAttached(Boolean projectOverviewAttached) {
    this.projectOverviewAttached = projectOverviewAttached;
    return this;
  }

  /**
   * Get projectOverviewAttached
   * @return projectOverviewAttached
   */
  @javax.annotation.Nullable
  public Boolean getProjectOverviewAttached() {
    return projectOverviewAttached;
  }

  public void setProjectOverviewAttached(Boolean projectOverviewAttached) {
    this.projectOverviewAttached = projectOverviewAttached;
  }


  public Invoice reference(String reference) {
    this.reference = reference;
    return this;
  }

  /**
   * Get reference
   * @return reference
   */
  @javax.annotation.Nullable
  public String getReference() {
    return reference;
  }

  public void setReference(String reference) {
    this.reference = reference;
  }


  public Invoice showEmployeeName(Boolean showEmployeeName) {
    this.showEmployeeName = showEmployeeName;
    return this;
  }

  /**
   * Get showEmployeeName
   * @return showEmployeeName
   */
  @javax.annotation.Nullable
  public Boolean getShowEmployeeName() {
    return showEmployeeName;
  }

  public void setShowEmployeeName(Boolean showEmployeeName) {
    this.showEmployeeName = showEmployeeName;
  }


  public Invoice showPriceProductBundle(Boolean showPriceProductBundle) {
    this.showPriceProductBundle = showPriceProductBundle;
    return this;
  }

  /**
   * Get showPriceProductBundle
   * @return showPriceProductBundle
   */
  @javax.annotation.Nullable
  public Boolean getShowPriceProductBundle() {
    return showPriceProductBundle;
  }

  public void setShowPriceProductBundle(Boolean showPriceProductBundle) {
    this.showPriceProductBundle = showPriceProductBundle;
  }


  public Invoice showPricesProductsAndHours(Boolean showPricesProductsAndHours) {
    this.showPricesProductsAndHours = showPricesProductsAndHours;
    return this;
  }

  /**
   * Get showPricesProductsAndHours
   * @return showPricesProductsAndHours
   */
  @javax.annotation.Nullable
  public Boolean getShowPricesProductsAndHours() {
    return showPricesProductsAndHours;
  }

  public void setShowPricesProductsAndHours(Boolean showPricesProductsAndHours) {
    this.showPricesProductsAndHours = showPricesProductsAndHours;
  }


  public Invoice showProductImages(Boolean showProductImages) {
    this.showProductImages = showProductImages;
    return this;
  }

  /**
   * Get showProductImages
   * @return showProductImages
   */
  @javax.annotation.Nullable
  public Boolean getShowProductImages() {
    return showProductImages;
  }

  public void setShowProductImages(Boolean showProductImages) {
    this.showProductImages = showProductImages;
  }


  public Invoice showProductsProductBundle(Boolean showProductsProductBundle) {
    this.showProductsProductBundle = showProductsProductBundle;
    return this;
  }

  /**
   * Get showProductsProductBundle
   * @return showProductsProductBundle
   */
  @javax.annotation.Nullable
  public Boolean getShowProductsProductBundle() {
    return showProductsProductBundle;
  }

  public void setShowProductsProductBundle(Boolean showProductsProductBundle) {
    this.showProductsProductBundle = showProductsProductBundle;
  }


  public Invoice title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Invoice totalCostPrice(Float totalCostPrice) {
    this.totalCostPrice = totalCostPrice;
    return this;
  }

  /**
   * Get totalCostPrice
   * @return totalCostPrice
   */
  @javax.annotation.Nullable
  public Float getTotalCostPrice() {
    return totalCostPrice;
  }

  public void setTotalCostPrice(Float totalCostPrice) {
    this.totalCostPrice = totalCostPrice;
  }


  public Invoice totalDiscountPercent(Float totalDiscountPercent) {
    this.totalDiscountPercent = totalDiscountPercent;
    return this;
  }

  /**
   * Get totalDiscountPercent
   * @return totalDiscountPercent
   */
  @javax.annotation.Nullable
  public Float getTotalDiscountPercent() {
    return totalDiscountPercent;
  }

  public void setTotalDiscountPercent(Float totalDiscountPercent) {
    this.totalDiscountPercent = totalDiscountPercent;
  }


  public Invoice vatPercent(Integer vatPercent) {
    this.vatPercent = vatPercent;
    return this;
  }

  /**
   * Get vatPercent
   * @return vatPercent
   */
  @javax.annotation.Nullable
  public Integer getVatPercent() {
    return vatPercent;
  }

  public void setVatPercent(Integer vatPercent) {
    this.vatPercent = vatPercent;
  }


  public Invoice vendorId(UUID vendorId) {
    this.vendorId = vendorId;
    return this;
  }

  /**
   * Get vendorId
   * @return vendorId
   */
  @javax.annotation.Nullable
  public UUID getVendorId() {
    return vendorId;
  }

  public void setVendorId(UUID vendorId) {
    this.vendorId = vendorId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Invoice invoice = (Invoice) o;
    return Objects.equals(this.allProductsOneLine, invoice.allProductsOneLine) &&
        Objects.equals(this.allWorkingHoursOneLine, invoice.allWorkingHoursOneLine) &&
        Objects.equals(this.companyId, invoice.companyId) &&
        Objects.equals(this.contactId, invoice.contactId) &&
        Objects.equals(this.created, invoice.created) &&
        Objects.equals(this.createdById, invoice.createdById) &&
        Objects.equals(this.currencyId, invoice.currencyId) &&
        Objects.equals(this.dateFrom, invoice.dateFrom) &&
        Objects.equals(this.dateTo, invoice.dateTo) &&
        Objects.equals(this.deleted, invoice.deleted) &&
        Objects.equals(this.downloaded, invoice.downloaded) &&
        Objects.equals(this.erpId, invoice.erpId) &&
        Objects.equals(this.erpPaymentTermId, invoice.erpPaymentTermId) &&
        Objects.equals(this.euCustomer, invoice.euCustomer) &&
        Objects.equals(this.grossPayment, invoice.grossPayment) &&
        Objects.equals(this.groupByForms, invoice.groupByForms) &&
        Objects.equals(this.id, invoice.id) &&
        Objects.equals(this.includeInvoicedLines, invoice.includeInvoicedLines) &&
        Objects.equals(this.integrationId, invoice.integrationId) &&
        Objects.equals(this.invoiceNumber, invoice.invoiceNumber) &&
        Objects.equals(this.isDraft, invoice.isDraft) &&
        Objects.equals(this.isFinalInvoice, invoice.isFinalInvoice) &&
        Objects.equals(this.isLocked, invoice.isLocked) &&
        Objects.equals(this.isOffer, invoice.isOffer) &&
        Objects.equals(this.issuedDate, invoice.issuedDate) &&
        Objects.equals(this.message, invoice.message) &&
        Objects.equals(this.modified, invoice.modified) &&
        Objects.equals(this.netPayment, invoice.netPayment) &&
        Objects.equals(this.offerNumber, invoice.offerNumber) &&
        Objects.equals(this.orderLineGroupId, invoice.orderLineGroupId) &&
        Objects.equals(this.paymentDueDate, invoice.paymentDueDate) &&
        Objects.equals(this.paymentTermId, invoice.paymentTermId) &&
        Objects.equals(this.projectId, invoice.projectId) &&
        Objects.equals(this.projectOverviewAttached, invoice.projectOverviewAttached) &&
        Objects.equals(this.reference, invoice.reference) &&
        Objects.equals(this.showEmployeeName, invoice.showEmployeeName) &&
        Objects.equals(this.showPriceProductBundle, invoice.showPriceProductBundle) &&
        Objects.equals(this.showPricesProductsAndHours, invoice.showPricesProductsAndHours) &&
        Objects.equals(this.showProductImages, invoice.showProductImages) &&
        Objects.equals(this.showProductsProductBundle, invoice.showProductsProductBundle) &&
        Objects.equals(this.title, invoice.title) &&
        Objects.equals(this.totalCostPrice, invoice.totalCostPrice) &&
        Objects.equals(this.totalDiscountPercent, invoice.totalDiscountPercent) &&
        Objects.equals(this.vatPercent, invoice.vatPercent) &&
        Objects.equals(this.vendorId, invoice.vendorId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allProductsOneLine, allWorkingHoursOneLine, companyId, contactId, created, createdById, currencyId, dateFrom, dateTo, deleted, downloaded, erpId, erpPaymentTermId, euCustomer, grossPayment, groupByForms, id, includeInvoicedLines, integrationId, invoiceNumber, isDraft, isFinalInvoice, isLocked, isOffer, issuedDate, message, modified, netPayment, offerNumber, orderLineGroupId, paymentDueDate, paymentTermId, projectId, projectOverviewAttached, reference, showEmployeeName, showPriceProductBundle, showPricesProductsAndHours, showProductImages, showProductsProductBundle, title, totalCostPrice, totalDiscountPercent, vatPercent, vendorId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Invoice {\n");
    sb.append("    allProductsOneLine: ").append(toIndentedString(allProductsOneLine)).append("\n");
    sb.append("    allWorkingHoursOneLine: ").append(toIndentedString(allWorkingHoursOneLine)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    contactId: ").append(toIndentedString(contactId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    currencyId: ").append(toIndentedString(currencyId)).append("\n");
    sb.append("    dateFrom: ").append(toIndentedString(dateFrom)).append("\n");
    sb.append("    dateTo: ").append(toIndentedString(dateTo)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    downloaded: ").append(toIndentedString(downloaded)).append("\n");
    sb.append("    erpId: ").append(toIndentedString(erpId)).append("\n");
    sb.append("    erpPaymentTermId: ").append(toIndentedString(erpPaymentTermId)).append("\n");
    sb.append("    euCustomer: ").append(toIndentedString(euCustomer)).append("\n");
    sb.append("    grossPayment: ").append(toIndentedString(grossPayment)).append("\n");
    sb.append("    groupByForms: ").append(toIndentedString(groupByForms)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    includeInvoicedLines: ").append(toIndentedString(includeInvoicedLines)).append("\n");
    sb.append("    integrationId: ").append(toIndentedString(integrationId)).append("\n");
    sb.append("    invoiceNumber: ").append(toIndentedString(invoiceNumber)).append("\n");
    sb.append("    isDraft: ").append(toIndentedString(isDraft)).append("\n");
    sb.append("    isFinalInvoice: ").append(toIndentedString(isFinalInvoice)).append("\n");
    sb.append("    isLocked: ").append(toIndentedString(isLocked)).append("\n");
    sb.append("    isOffer: ").append(toIndentedString(isOffer)).append("\n");
    sb.append("    issuedDate: ").append(toIndentedString(issuedDate)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    netPayment: ").append(toIndentedString(netPayment)).append("\n");
    sb.append("    offerNumber: ").append(toIndentedString(offerNumber)).append("\n");
    sb.append("    orderLineGroupId: ").append(toIndentedString(orderLineGroupId)).append("\n");
    sb.append("    paymentDueDate: ").append(toIndentedString(paymentDueDate)).append("\n");
    sb.append("    paymentTermId: ").append(toIndentedString(paymentTermId)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    projectOverviewAttached: ").append(toIndentedString(projectOverviewAttached)).append("\n");
    sb.append("    reference: ").append(toIndentedString(reference)).append("\n");
    sb.append("    showEmployeeName: ").append(toIndentedString(showEmployeeName)).append("\n");
    sb.append("    showPriceProductBundle: ").append(toIndentedString(showPriceProductBundle)).append("\n");
    sb.append("    showPricesProductsAndHours: ").append(toIndentedString(showPricesProductsAndHours)).append("\n");
    sb.append("    showProductImages: ").append(toIndentedString(showProductImages)).append("\n");
    sb.append("    showProductsProductBundle: ").append(toIndentedString(showProductsProductBundle)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    totalCostPrice: ").append(toIndentedString(totalCostPrice)).append("\n");
    sb.append("    totalDiscountPercent: ").append(toIndentedString(totalDiscountPercent)).append("\n");
    sb.append("    vatPercent: ").append(toIndentedString(vatPercent)).append("\n");
    sb.append("    vendorId: ").append(toIndentedString(vendorId)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("all_products_one_line");
    openapiFields.add("all_working_hours_one_line");
    openapiFields.add("company_id");
    openapiFields.add("contact_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("currency_id");
    openapiFields.add("date_from");
    openapiFields.add("date_to");
    openapiFields.add("deleted");
    openapiFields.add("downloaded");
    openapiFields.add("erp_id");
    openapiFields.add("erp_payment_term_id");
    openapiFields.add("eu_customer");
    openapiFields.add("gross_payment");
    openapiFields.add("group_by_forms");
    openapiFields.add("id");
    openapiFields.add("include_invoiced_lines");
    openapiFields.add("integration_id");
    openapiFields.add("invoice_number");
    openapiFields.add("is_draft");
    openapiFields.add("is_final_invoice");
    openapiFields.add("is_locked");
    openapiFields.add("is_offer");
    openapiFields.add("issued_date");
    openapiFields.add("message");
    openapiFields.add("modified");
    openapiFields.add("net_payment");
    openapiFields.add("offer_number");
    openapiFields.add("order_line_group_id");
    openapiFields.add("payment_due_date");
    openapiFields.add("payment_term_id");
    openapiFields.add("project_id");
    openapiFields.add("project_overview_attached");
    openapiFields.add("reference");
    openapiFields.add("show_employee_name");
    openapiFields.add("show_price_product_bundle");
    openapiFields.add("show_prices_products_and_hours");
    openapiFields.add("show_product_images");
    openapiFields.add("show_products_product_bundle");
    openapiFields.add("title");
    openapiFields.add("total_cost_price");
    openapiFields.add("total_discount_percent");
    openapiFields.add("vat_percent");
    openapiFields.add("vendor_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Invoice
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Invoice.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Invoice is not found in the empty JSON string", Invoice.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Invoice.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Invoice` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("contact_id") != null && !jsonObj.get("contact_id").isJsonNull()) && !jsonObj.get("contact_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact_id").toString()));
      }
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      if ((jsonObj.get("created_by_id") != null && !jsonObj.get("created_by_id").isJsonNull()) && !jsonObj.get("created_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by_id").toString()));
      }
      if ((jsonObj.get("currency_id") != null && !jsonObj.get("currency_id").isJsonNull()) && !jsonObj.get("currency_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency_id").toString()));
      }
      if ((jsonObj.get("deleted") != null && !jsonObj.get("deleted").isJsonNull()) && !jsonObj.get("deleted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted").toString()));
      }
      if ((jsonObj.get("downloaded") != null && !jsonObj.get("downloaded").isJsonNull()) && !jsonObj.get("downloaded").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `downloaded` to be a primitive type in the JSON string but got `%s`", jsonObj.get("downloaded").toString()));
      }
      if ((jsonObj.get("erp_id") != null && !jsonObj.get("erp_id").isJsonNull()) && !jsonObj.get("erp_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_id").toString()));
      }
      if ((jsonObj.get("erp_payment_term_id") != null && !jsonObj.get("erp_payment_term_id").isJsonNull()) && !jsonObj.get("erp_payment_term_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_payment_term_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_payment_term_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("integration_id") != null && !jsonObj.get("integration_id").isJsonNull()) && !jsonObj.get("integration_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `integration_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("integration_id").toString()));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("order_line_group_id") != null && !jsonObj.get("order_line_group_id").isJsonNull()) && !jsonObj.get("order_line_group_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_line_group_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_line_group_id").toString()));
      }
      if ((jsonObj.get("payment_term_id") != null && !jsonObj.get("payment_term_id").isJsonNull()) && !jsonObj.get("payment_term_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_term_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_term_id").toString()));
      }
      if ((jsonObj.get("project_id") != null && !jsonObj.get("project_id").isJsonNull()) && !jsonObj.get("project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_id").toString()));
      }
      if ((jsonObj.get("reference") != null && !jsonObj.get("reference").isJsonNull()) && !jsonObj.get("reference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reference").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("vendor_id") != null && !jsonObj.get("vendor_id").isJsonNull()) && !jsonObj.get("vendor_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vendor_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vendor_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Invoice.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Invoice' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Invoice> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Invoice.class));

       return (TypeAdapter<T>) new TypeAdapter<Invoice>() {
           @Override
           public void write(JsonWriter out, Invoice value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Invoice read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Invoice given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Invoice
   * @throws IOException if the JSON string is invalid with respect to Invoice
   */
  public static Invoice fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Invoice.class);
  }

  /**
   * Convert an instance of Invoice to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

