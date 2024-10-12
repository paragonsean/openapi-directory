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
 * Offer
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Offer {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_ALL_LINES_ONE_LINE = "all_lines_one_line";
  @SerializedName(SERIALIZED_NAME_ALL_LINES_ONE_LINE)
  private Boolean allLinesOneLine;

  public static final String SERIALIZED_NAME_ALL_PRODUCTS_ONE_LINE = "all_products_one_line";
  @SerializedName(SERIALIZED_NAME_ALL_PRODUCTS_ONE_LINE)
  private Boolean allProductsOneLine;

  public static final String SERIALIZED_NAME_ALL_WORKING_HOURS_ONE_LINE = "all_working_hours_one_line";
  @SerializedName(SERIALIZED_NAME_ALL_WORKING_HOURS_ONE_LINE)
  private Boolean allWorkingHoursOneLine;

  public static final String SERIALIZED_NAME_CITY_ID = "city_id";
  @SerializedName(SERIALIZED_NAME_CITY_ID)
  private UUID cityId;

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

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private String deleted;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISCOUNT_PERCENT = "discount_percent";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_PERCENT)
  private Integer discountPercent;

  public static final String SERIALIZED_NAME_ERP_PAYMENT_TERM_ID = "erp_payment_term_id";
  @SerializedName(SERIALIZED_NAME_ERP_PAYMENT_TERM_ID)
  private String erpPaymentTermId;

  public static final String SERIALIZED_NAME_EXPIRATON_DATE = "expiraton_date";
  @SerializedName(SERIALIZED_NAME_EXPIRATON_DATE)
  private String expiratonDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_ISSUE_DATE = "issue_date";
  @SerializedName(SERIALIZED_NAME_ISSUE_DATE)
  private LocalDate issueDate;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_MODIFIED_BY_ID = "modified_by_id";
  @SerializedName(SERIALIZED_NAME_MODIFIED_BY_ID)
  private UUID modifiedById;

  public static final String SERIALIZED_NAME_OFFER_NUMBER = "offer_number";
  @SerializedName(SERIALIZED_NAME_OFFER_NUMBER)
  private Integer offerNumber;

  public static final String SERIALIZED_NAME_OFFER_STATUS_ID = "offer_status_id";
  @SerializedName(SERIALIZED_NAME_OFFER_STATUS_ID)
  private UUID offerStatusId;

  public static final String SERIALIZED_NAME_PAYMENT_TERM_ID = "payment_term_id";
  @SerializedName(SERIALIZED_NAME_PAYMENT_TERM_ID)
  private String paymentTermId;

  public static final String SERIALIZED_NAME_REJECTION_REASON = "rejection_reason";
  @SerializedName(SERIALIZED_NAME_REJECTION_REASON)
  private String rejectionReason;

  public static final String SERIALIZED_NAME_SENDER_ID = "sender_id";
  @SerializedName(SERIALIZED_NAME_SENDER_ID)
  private UUID senderId;

  public static final String SERIALIZED_NAME_SHOW_EMPLOYEE_NAME = "show_employee_name";
  @SerializedName(SERIALIZED_NAME_SHOW_EMPLOYEE_NAME)
  private Boolean showEmployeeName;

  public static final String SERIALIZED_NAME_SHOW_OFFER_LINES = "show_offer_lines";
  @SerializedName(SERIALIZED_NAME_SHOW_OFFER_LINES)
  private Boolean showOfferLines;

  public static final String SERIALIZED_NAME_SHOW_PAYMENT_TERM = "show_payment_term";
  @SerializedName(SERIALIZED_NAME_SHOW_PAYMENT_TERM)
  private Boolean showPaymentTerm;

  public static final String SERIALIZED_NAME_SHOW_PRICES = "show_prices";
  @SerializedName(SERIALIZED_NAME_SHOW_PRICES)
  private Boolean showPrices;

  public static final String SERIALIZED_NAME_SHOW_PRODUCT_IMAGES = "show_product_images";
  @SerializedName(SERIALIZED_NAME_SHOW_PRODUCT_IMAGES)
  private Boolean showProductImages;

  public static final String SERIALIZED_NAME_SHOW_PRODUCTS_PRODUCT_BUNDLE = "show_products_product_bundle";
  @SerializedName(SERIALIZED_NAME_SHOW_PRODUCTS_PRODUCT_BUNDLE)
  private Boolean showProductsProductBundle;

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private String slug;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_VAT_PERCENT = "vat_percent";
  @SerializedName(SERIALIZED_NAME_VAT_PERCENT)
  private Integer vatPercent;

  public Offer() {
  }

  public Offer(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Offer address(String address) {
    this.address = address;
    return this;
  }

  /**
   * Street address
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public Offer allLinesOneLine(Boolean allLinesOneLine) {
    this.allLinesOneLine = allLinesOneLine;
    return this;
  }

  /**
   * Get allLinesOneLine
   * @return allLinesOneLine
   */
  @javax.annotation.Nullable
  public Boolean getAllLinesOneLine() {
    return allLinesOneLine;
  }

  public void setAllLinesOneLine(Boolean allLinesOneLine) {
    this.allLinesOneLine = allLinesOneLine;
  }


  public Offer allProductsOneLine(Boolean allProductsOneLine) {
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


  public Offer allWorkingHoursOneLine(Boolean allWorkingHoursOneLine) {
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


  public Offer cityId(UUID cityId) {
    this.cityId = cityId;
    return this;
  }

  /**
   * Get cityId
   * @return cityId
   */
  @javax.annotation.Nullable
  public UUID getCityId() {
    return cityId;
  }

  public void setCityId(UUID cityId) {
    this.cityId = cityId;
  }


  public Offer companyId(UUID companyId) {
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


  public Offer contactId(UUID contactId) {
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



  public Offer createdById(UUID createdById) {
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


  /**
   * Only present if it&#39;s a deleted object
   * @return deleted
   */
  @javax.annotation.Nullable
  public String getDeleted() {
    return deleted;
  }



  public Offer description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Offer discountPercent(Integer discountPercent) {
    this.discountPercent = discountPercent;
    return this;
  }

  /**
   * Get discountPercent
   * @return discountPercent
   */
  @javax.annotation.Nullable
  public Integer getDiscountPercent() {
    return discountPercent;
  }

  public void setDiscountPercent(Integer discountPercent) {
    this.discountPercent = discountPercent;
  }


  public Offer erpPaymentTermId(String erpPaymentTermId) {
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


  public Offer expiratonDate(String expiratonDate) {
    this.expiratonDate = expiratonDate;
    return this;
  }

  /**
   * Get expiratonDate
   * @return expiratonDate
   */
  @javax.annotation.Nullable
  public String getExpiratonDate() {
    return expiratonDate;
  }

  public void setExpiratonDate(String expiratonDate) {
    this.expiratonDate = expiratonDate;
  }


  public Offer id(UUID id) {
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


  public Offer issueDate(LocalDate issueDate) {
    this.issueDate = issueDate;
    return this;
  }

  /**
   * Get issueDate
   * @return issueDate
   */
  @javax.annotation.Nullable
  public LocalDate getIssueDate() {
    return issueDate;
  }

  public void setIssueDate(LocalDate issueDate) {
    this.issueDate = issueDate;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Offer modifiedById(UUID modifiedById) {
    this.modifiedById = modifiedById;
    return this;
  }

  /**
   * Get modifiedById
   * @return modifiedById
   */
  @javax.annotation.Nullable
  public UUID getModifiedById() {
    return modifiedById;
  }

  public void setModifiedById(UUID modifiedById) {
    this.modifiedById = modifiedById;
  }


  public Offer offerNumber(Integer offerNumber) {
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


  public Offer offerStatusId(UUID offerStatusId) {
    this.offerStatusId = offerStatusId;
    return this;
  }

  /**
   * Get offerStatusId
   * @return offerStatusId
   */
  @javax.annotation.Nullable
  public UUID getOfferStatusId() {
    return offerStatusId;
  }

  public void setOfferStatusId(UUID offerStatusId) {
    this.offerStatusId = offerStatusId;
  }


  public Offer paymentTermId(String paymentTermId) {
    this.paymentTermId = paymentTermId;
    return this;
  }

  /**
   * Get paymentTermId
   * @return paymentTermId
   */
  @javax.annotation.Nullable
  public String getPaymentTermId() {
    return paymentTermId;
  }

  public void setPaymentTermId(String paymentTermId) {
    this.paymentTermId = paymentTermId;
  }


  public Offer rejectionReason(String rejectionReason) {
    this.rejectionReason = rejectionReason;
    return this;
  }

  /**
   * Get rejectionReason
   * @return rejectionReason
   */
  @javax.annotation.Nullable
  public String getRejectionReason() {
    return rejectionReason;
  }

  public void setRejectionReason(String rejectionReason) {
    this.rejectionReason = rejectionReason;
  }


  public Offer senderId(UUID senderId) {
    this.senderId = senderId;
    return this;
  }

  /**
   * Get senderId
   * @return senderId
   */
  @javax.annotation.Nullable
  public UUID getSenderId() {
    return senderId;
  }

  public void setSenderId(UUID senderId) {
    this.senderId = senderId;
  }


  public Offer showEmployeeName(Boolean showEmployeeName) {
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


  public Offer showOfferLines(Boolean showOfferLines) {
    this.showOfferLines = showOfferLines;
    return this;
  }

  /**
   * Get showOfferLines
   * @return showOfferLines
   */
  @javax.annotation.Nullable
  public Boolean getShowOfferLines() {
    return showOfferLines;
  }

  public void setShowOfferLines(Boolean showOfferLines) {
    this.showOfferLines = showOfferLines;
  }


  public Offer showPaymentTerm(Boolean showPaymentTerm) {
    this.showPaymentTerm = showPaymentTerm;
    return this;
  }

  /**
   * Get showPaymentTerm
   * @return showPaymentTerm
   */
  @javax.annotation.Nullable
  public Boolean getShowPaymentTerm() {
    return showPaymentTerm;
  }

  public void setShowPaymentTerm(Boolean showPaymentTerm) {
    this.showPaymentTerm = showPaymentTerm;
  }


  public Offer showPrices(Boolean showPrices) {
    this.showPrices = showPrices;
    return this;
  }

  /**
   * Get showPrices
   * @return showPrices
   */
  @javax.annotation.Nullable
  public Boolean getShowPrices() {
    return showPrices;
  }

  public void setShowPrices(Boolean showPrices) {
    this.showPrices = showPrices;
  }


  public Offer showProductImages(Boolean showProductImages) {
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


  public Offer showProductsProductBundle(Boolean showProductsProductBundle) {
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


  public Offer slug(String slug) {
    this.slug = slug;
    return this;
  }

  /**
   * Get slug
   * @return slug
   */
  @javax.annotation.Nullable
  public String getSlug() {
    return slug;
  }

  public void setSlug(String slug) {
    this.slug = slug;
  }


  public Offer status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public Offer title(String title) {
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


  public Offer vatPercent(Integer vatPercent) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Offer offer = (Offer) o;
    return Objects.equals(this.address, offer.address) &&
        Objects.equals(this.allLinesOneLine, offer.allLinesOneLine) &&
        Objects.equals(this.allProductsOneLine, offer.allProductsOneLine) &&
        Objects.equals(this.allWorkingHoursOneLine, offer.allWorkingHoursOneLine) &&
        Objects.equals(this.cityId, offer.cityId) &&
        Objects.equals(this.companyId, offer.companyId) &&
        Objects.equals(this.contactId, offer.contactId) &&
        Objects.equals(this.created, offer.created) &&
        Objects.equals(this.createdById, offer.createdById) &&
        Objects.equals(this.deleted, offer.deleted) &&
        Objects.equals(this.description, offer.description) &&
        Objects.equals(this.discountPercent, offer.discountPercent) &&
        Objects.equals(this.erpPaymentTermId, offer.erpPaymentTermId) &&
        Objects.equals(this.expiratonDate, offer.expiratonDate) &&
        Objects.equals(this.id, offer.id) &&
        Objects.equals(this.issueDate, offer.issueDate) &&
        Objects.equals(this.modified, offer.modified) &&
        Objects.equals(this.modifiedById, offer.modifiedById) &&
        Objects.equals(this.offerNumber, offer.offerNumber) &&
        Objects.equals(this.offerStatusId, offer.offerStatusId) &&
        Objects.equals(this.paymentTermId, offer.paymentTermId) &&
        Objects.equals(this.rejectionReason, offer.rejectionReason) &&
        Objects.equals(this.senderId, offer.senderId) &&
        Objects.equals(this.showEmployeeName, offer.showEmployeeName) &&
        Objects.equals(this.showOfferLines, offer.showOfferLines) &&
        Objects.equals(this.showPaymentTerm, offer.showPaymentTerm) &&
        Objects.equals(this.showPrices, offer.showPrices) &&
        Objects.equals(this.showProductImages, offer.showProductImages) &&
        Objects.equals(this.showProductsProductBundle, offer.showProductsProductBundle) &&
        Objects.equals(this.slug, offer.slug) &&
        Objects.equals(this.status, offer.status) &&
        Objects.equals(this.title, offer.title) &&
        Objects.equals(this.vatPercent, offer.vatPercent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, allLinesOneLine, allProductsOneLine, allWorkingHoursOneLine, cityId, companyId, contactId, created, createdById, deleted, description, discountPercent, erpPaymentTermId, expiratonDate, id, issueDate, modified, modifiedById, offerNumber, offerStatusId, paymentTermId, rejectionReason, senderId, showEmployeeName, showOfferLines, showPaymentTerm, showPrices, showProductImages, showProductsProductBundle, slug, status, title, vatPercent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Offer {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    allLinesOneLine: ").append(toIndentedString(allLinesOneLine)).append("\n");
    sb.append("    allProductsOneLine: ").append(toIndentedString(allProductsOneLine)).append("\n");
    sb.append("    allWorkingHoursOneLine: ").append(toIndentedString(allWorkingHoursOneLine)).append("\n");
    sb.append("    cityId: ").append(toIndentedString(cityId)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    contactId: ").append(toIndentedString(contactId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    discountPercent: ").append(toIndentedString(discountPercent)).append("\n");
    sb.append("    erpPaymentTermId: ").append(toIndentedString(erpPaymentTermId)).append("\n");
    sb.append("    expiratonDate: ").append(toIndentedString(expiratonDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    issueDate: ").append(toIndentedString(issueDate)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    modifiedById: ").append(toIndentedString(modifiedById)).append("\n");
    sb.append("    offerNumber: ").append(toIndentedString(offerNumber)).append("\n");
    sb.append("    offerStatusId: ").append(toIndentedString(offerStatusId)).append("\n");
    sb.append("    paymentTermId: ").append(toIndentedString(paymentTermId)).append("\n");
    sb.append("    rejectionReason: ").append(toIndentedString(rejectionReason)).append("\n");
    sb.append("    senderId: ").append(toIndentedString(senderId)).append("\n");
    sb.append("    showEmployeeName: ").append(toIndentedString(showEmployeeName)).append("\n");
    sb.append("    showOfferLines: ").append(toIndentedString(showOfferLines)).append("\n");
    sb.append("    showPaymentTerm: ").append(toIndentedString(showPaymentTerm)).append("\n");
    sb.append("    showPrices: ").append(toIndentedString(showPrices)).append("\n");
    sb.append("    showProductImages: ").append(toIndentedString(showProductImages)).append("\n");
    sb.append("    showProductsProductBundle: ").append(toIndentedString(showProductsProductBundle)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    vatPercent: ").append(toIndentedString(vatPercent)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("all_lines_one_line");
    openapiFields.add("all_products_one_line");
    openapiFields.add("all_working_hours_one_line");
    openapiFields.add("city_id");
    openapiFields.add("company_id");
    openapiFields.add("contact_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("deleted");
    openapiFields.add("description");
    openapiFields.add("discount_percent");
    openapiFields.add("erp_payment_term_id");
    openapiFields.add("expiraton_date");
    openapiFields.add("id");
    openapiFields.add("issue_date");
    openapiFields.add("modified");
    openapiFields.add("modified_by_id");
    openapiFields.add("offer_number");
    openapiFields.add("offer_status_id");
    openapiFields.add("payment_term_id");
    openapiFields.add("rejection_reason");
    openapiFields.add("sender_id");
    openapiFields.add("show_employee_name");
    openapiFields.add("show_offer_lines");
    openapiFields.add("show_payment_term");
    openapiFields.add("show_prices");
    openapiFields.add("show_product_images");
    openapiFields.add("show_products_product_bundle");
    openapiFields.add("slug");
    openapiFields.add("status");
    openapiFields.add("title");
    openapiFields.add("vat_percent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Offer
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Offer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Offer is not found in the empty JSON string", Offer.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Offer.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Offer` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) && !jsonObj.get("address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("city_id") != null && !jsonObj.get("city_id").isJsonNull()) && !jsonObj.get("city_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city_id").toString()));
      }
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
      if ((jsonObj.get("deleted") != null && !jsonObj.get("deleted").isJsonNull()) && !jsonObj.get("deleted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("erp_payment_term_id") != null && !jsonObj.get("erp_payment_term_id").isJsonNull()) && !jsonObj.get("erp_payment_term_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_payment_term_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_payment_term_id").toString()));
      }
      if ((jsonObj.get("expiraton_date") != null && !jsonObj.get("expiraton_date").isJsonNull()) && !jsonObj.get("expiraton_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `expiraton_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("expiraton_date").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("modified_by_id") != null && !jsonObj.get("modified_by_id").isJsonNull()) && !jsonObj.get("modified_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified_by_id").toString()));
      }
      if ((jsonObj.get("offer_status_id") != null && !jsonObj.get("offer_status_id").isJsonNull()) && !jsonObj.get("offer_status_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `offer_status_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("offer_status_id").toString()));
      }
      if ((jsonObj.get("payment_term_id") != null && !jsonObj.get("payment_term_id").isJsonNull()) && !jsonObj.get("payment_term_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_term_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_term_id").toString()));
      }
      if ((jsonObj.get("rejection_reason") != null && !jsonObj.get("rejection_reason").isJsonNull()) && !jsonObj.get("rejection_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rejection_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rejection_reason").toString()));
      }
      if ((jsonObj.get("sender_id") != null && !jsonObj.get("sender_id").isJsonNull()) && !jsonObj.get("sender_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sender_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sender_id").toString()));
      }
      if ((jsonObj.get("slug") != null && !jsonObj.get("slug").isJsonNull()) && !jsonObj.get("slug").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be a primitive type in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Offer.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Offer' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Offer> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Offer.class));

       return (TypeAdapter<T>) new TypeAdapter<Offer>() {
           @Override
           public void write(JsonWriter out, Offer value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Offer read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Offer given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Offer
   * @throws IOException if the JSON string is invalid with respect to Offer
   */
  public static Offer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Offer.class);
  }

  /**
   * Convert an instance of Offer to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

