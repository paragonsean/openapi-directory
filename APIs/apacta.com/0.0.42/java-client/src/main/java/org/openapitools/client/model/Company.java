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
import java.time.OffsetDateTime;
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
 * Company
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Company {
  public static final String SERIALIZED_NAME_CITY_ID = "city_id";
  @SerializedName(SERIALIZED_NAME_CITY_ID)
  private UUID cityId;

  public static final String SERIALIZED_NAME_CONTACT_PERSON_ID = "contact_person_id";
  @SerializedName(SERIALIZED_NAME_CONTACT_PERSON_ID)
  private UUID contactPersonId;

  public static final String SERIALIZED_NAME_COUNTRY_ID = "country_id";
  @SerializedName(SERIALIZED_NAME_COUNTRY_ID)
  private UUID countryId;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CREATED_BY_ID = "created_by_id";
  @SerializedName(SERIALIZED_NAME_CREATED_BY_ID)
  private UUID createdById;

  public static final String SERIALIZED_NAME_CVR = "cvr";
  @SerializedName(SERIALIZED_NAME_CVR)
  private String cvr;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private String deleted;

  public static final String SERIALIZED_NAME_EXPIRED = "expired";
  @SerializedName(SERIALIZED_NAME_EXPIRED)
  private OffsetDateTime expired;

  public static final String SERIALIZED_NAME_FILE_ID = "file_id";
  @SerializedName(SERIALIZED_NAME_FILE_ID)
  private UUID fileId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_INVOICE_EMAIL = "invoice_email";
  @SerializedName(SERIALIZED_NAME_INVOICE_EMAIL)
  private String invoiceEmail;

  public static final String SERIALIZED_NAME_LANGUAGE_ID = "language_id";
  @SerializedName(SERIALIZED_NAME_LANGUAGE_ID)
  private UUID languageId;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NEXT_INVOICE_NUMBER = "next_invoice_number";
  @SerializedName(SERIALIZED_NAME_NEXT_INVOICE_NUMBER)
  private Integer nextInvoiceNumber;

  public static final String SERIALIZED_NAME_NEXT_OFFER_NUMBER = "next_offer_number";
  @SerializedName(SERIALIZED_NAME_NEXT_OFFER_NUMBER)
  private Integer nextOfferNumber;

  public static final String SERIALIZED_NAME_NEXT_PROJECT_NUMBER = "next_project_number";
  @SerializedName(SERIALIZED_NAME_NEXT_PROJECT_NUMBER)
  private Integer nextProjectNumber;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_PHONE_COUNTRYCODE = "phone_countrycode";
  @SerializedName(SERIALIZED_NAME_PHONE_COUNTRYCODE)
  private String phoneCountrycode;

  public static final String SERIALIZED_NAME_RECEIVE_FORM_MAILS = "receive_form_mails";
  @SerializedName(SERIALIZED_NAME_RECEIVE_FORM_MAILS)
  private String receiveFormMails;

  public static final String SERIALIZED_NAME_STREET_NAME = "street_name";
  @SerializedName(SERIALIZED_NAME_STREET_NAME)
  private String streetName;

  public static final String SERIALIZED_NAME_VAT_PERCENT = "vat_percent";
  @SerializedName(SERIALIZED_NAME_VAT_PERCENT)
  private Integer vatPercent;

  public static final String SERIALIZED_NAME_WEBSITE = "website";
  @SerializedName(SERIALIZED_NAME_WEBSITE)
  private String website;

  public Company() {
  }

  public Company(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Company cityId(UUID cityId) {
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


  public Company contactPersonId(UUID contactPersonId) {
    this.contactPersonId = contactPersonId;
    return this;
  }

  /**
   * Get contactPersonId
   * @return contactPersonId
   */
  @javax.annotation.Nullable
  public UUID getContactPersonId() {
    return contactPersonId;
  }

  public void setContactPersonId(UUID contactPersonId) {
    this.contactPersonId = contactPersonId;
  }


  public Company countryId(UUID countryId) {
    this.countryId = countryId;
    return this;
  }

  /**
   * Get countryId
   * @return countryId
   */
  @javax.annotation.Nullable
  public UUID getCountryId() {
    return countryId;
  }

  public void setCountryId(UUID countryId) {
    this.countryId = countryId;
  }


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  public Company createdById(UUID createdById) {
    this.createdById = createdById;
    return this;
  }

  /**
   * Read-only
   * @return createdById
   */
  @javax.annotation.Nullable
  public UUID getCreatedById() {
    return createdById;
  }

  public void setCreatedById(UUID createdById) {
    this.createdById = createdById;
  }


  public Company cvr(String cvr) {
    this.cvr = cvr;
    return this;
  }

  /**
   * Get cvr
   * @return cvr
   */
  @javax.annotation.Nullable
  public String getCvr() {
    return cvr;
  }

  public void setCvr(String cvr) {
    this.cvr = cvr;
  }


  /**
   * Only present if it&#39;s a deleted object
   * @return deleted
   */
  @javax.annotation.Nullable
  public String getDeleted() {
    return deleted;
  }



  public Company expired(OffsetDateTime expired) {
    this.expired = expired;
    return this;
  }

  /**
   * Get expired
   * @return expired
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpired() {
    return expired;
  }

  public void setExpired(OffsetDateTime expired) {
    this.expired = expired;
  }


  public Company fileId(UUID fileId) {
    this.fileId = fileId;
    return this;
  }

  /**
   * Get fileId
   * @return fileId
   */
  @javax.annotation.Nullable
  public UUID getFileId() {
    return fileId;
  }

  public void setFileId(UUID fileId) {
    this.fileId = fileId;
  }


  public Company id(UUID id) {
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


  public Company invoiceEmail(String invoiceEmail) {
    this.invoiceEmail = invoiceEmail;
    return this;
  }

  /**
   * Get invoiceEmail
   * @return invoiceEmail
   */
  @javax.annotation.Nullable
  public String getInvoiceEmail() {
    return invoiceEmail;
  }

  public void setInvoiceEmail(String invoiceEmail) {
    this.invoiceEmail = invoiceEmail;
  }


  public Company languageId(UUID languageId) {
    this.languageId = languageId;
    return this;
  }

  /**
   * Get languageId
   * @return languageId
   */
  @javax.annotation.Nullable
  public UUID getLanguageId() {
    return languageId;
  }

  public void setLanguageId(UUID languageId) {
    this.languageId = languageId;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Company name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Company nextInvoiceNumber(Integer nextInvoiceNumber) {
    this.nextInvoiceNumber = nextInvoiceNumber;
    return this;
  }

  /**
   * Get nextInvoiceNumber
   * @return nextInvoiceNumber
   */
  @javax.annotation.Nullable
  public Integer getNextInvoiceNumber() {
    return nextInvoiceNumber;
  }

  public void setNextInvoiceNumber(Integer nextInvoiceNumber) {
    this.nextInvoiceNumber = nextInvoiceNumber;
  }


  public Company nextOfferNumber(Integer nextOfferNumber) {
    this.nextOfferNumber = nextOfferNumber;
    return this;
  }

  /**
   * Get nextOfferNumber
   * @return nextOfferNumber
   */
  @javax.annotation.Nullable
  public Integer getNextOfferNumber() {
    return nextOfferNumber;
  }

  public void setNextOfferNumber(Integer nextOfferNumber) {
    this.nextOfferNumber = nextOfferNumber;
  }


  public Company nextProjectNumber(Integer nextProjectNumber) {
    this.nextProjectNumber = nextProjectNumber;
    return this;
  }

  /**
   * Get nextProjectNumber
   * @return nextProjectNumber
   */
  @javax.annotation.Nullable
  public Integer getNextProjectNumber() {
    return nextProjectNumber;
  }

  public void setNextProjectNumber(Integer nextProjectNumber) {
    this.nextProjectNumber = nextProjectNumber;
  }


  public Company phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Format like eg. &#x60;28680133&#x60; or &#x60;046158971404&#x60;
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public Company phoneCountrycode(String phoneCountrycode) {
    this.phoneCountrycode = phoneCountrycode;
    return this;
  }

  /**
   * Format like eg. &#x60;45&#x60; or &#x60;49&#x60;
   * @return phoneCountrycode
   */
  @javax.annotation.Nullable
  public String getPhoneCountrycode() {
    return phoneCountrycode;
  }

  public void setPhoneCountrycode(String phoneCountrycode) {
    this.phoneCountrycode = phoneCountrycode;
  }


  public Company receiveFormMails(String receiveFormMails) {
    this.receiveFormMails = receiveFormMails;
    return this;
  }

  /**
   * Get receiveFormMails
   * @return receiveFormMails
   */
  @javax.annotation.Nullable
  public String getReceiveFormMails() {
    return receiveFormMails;
  }

  public void setReceiveFormMails(String receiveFormMails) {
    this.receiveFormMails = receiveFormMails;
  }


  public Company streetName(String streetName) {
    this.streetName = streetName;
    return this;
  }

  /**
   * Get streetName
   * @return streetName
   */
  @javax.annotation.Nullable
  public String getStreetName() {
    return streetName;
  }

  public void setStreetName(String streetName) {
    this.streetName = streetName;
  }


  public Company vatPercent(Integer vatPercent) {
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


  public Company website(String website) {
    this.website = website;
    return this;
  }

  /**
   * Get website
   * @return website
   */
  @javax.annotation.Nullable
  public String getWebsite() {
    return website;
  }

  public void setWebsite(String website) {
    this.website = website;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Company company = (Company) o;
    return Objects.equals(this.cityId, company.cityId) &&
        Objects.equals(this.contactPersonId, company.contactPersonId) &&
        Objects.equals(this.countryId, company.countryId) &&
        Objects.equals(this.created, company.created) &&
        Objects.equals(this.createdById, company.createdById) &&
        Objects.equals(this.cvr, company.cvr) &&
        Objects.equals(this.deleted, company.deleted) &&
        Objects.equals(this.expired, company.expired) &&
        Objects.equals(this.fileId, company.fileId) &&
        Objects.equals(this.id, company.id) &&
        Objects.equals(this.invoiceEmail, company.invoiceEmail) &&
        Objects.equals(this.languageId, company.languageId) &&
        Objects.equals(this.modified, company.modified) &&
        Objects.equals(this.name, company.name) &&
        Objects.equals(this.nextInvoiceNumber, company.nextInvoiceNumber) &&
        Objects.equals(this.nextOfferNumber, company.nextOfferNumber) &&
        Objects.equals(this.nextProjectNumber, company.nextProjectNumber) &&
        Objects.equals(this.phone, company.phone) &&
        Objects.equals(this.phoneCountrycode, company.phoneCountrycode) &&
        Objects.equals(this.receiveFormMails, company.receiveFormMails) &&
        Objects.equals(this.streetName, company.streetName) &&
        Objects.equals(this.vatPercent, company.vatPercent) &&
        Objects.equals(this.website, company.website);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cityId, contactPersonId, countryId, created, createdById, cvr, deleted, expired, fileId, id, invoiceEmail, languageId, modified, name, nextInvoiceNumber, nextOfferNumber, nextProjectNumber, phone, phoneCountrycode, receiveFormMails, streetName, vatPercent, website);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Company {\n");
    sb.append("    cityId: ").append(toIndentedString(cityId)).append("\n");
    sb.append("    contactPersonId: ").append(toIndentedString(contactPersonId)).append("\n");
    sb.append("    countryId: ").append(toIndentedString(countryId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    cvr: ").append(toIndentedString(cvr)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    expired: ").append(toIndentedString(expired)).append("\n");
    sb.append("    fileId: ").append(toIndentedString(fileId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    invoiceEmail: ").append(toIndentedString(invoiceEmail)).append("\n");
    sb.append("    languageId: ").append(toIndentedString(languageId)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nextInvoiceNumber: ").append(toIndentedString(nextInvoiceNumber)).append("\n");
    sb.append("    nextOfferNumber: ").append(toIndentedString(nextOfferNumber)).append("\n");
    sb.append("    nextProjectNumber: ").append(toIndentedString(nextProjectNumber)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    phoneCountrycode: ").append(toIndentedString(phoneCountrycode)).append("\n");
    sb.append("    receiveFormMails: ").append(toIndentedString(receiveFormMails)).append("\n");
    sb.append("    streetName: ").append(toIndentedString(streetName)).append("\n");
    sb.append("    vatPercent: ").append(toIndentedString(vatPercent)).append("\n");
    sb.append("    website: ").append(toIndentedString(website)).append("\n");
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
    openapiFields.add("city_id");
    openapiFields.add("contact_person_id");
    openapiFields.add("country_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("cvr");
    openapiFields.add("deleted");
    openapiFields.add("expired");
    openapiFields.add("file_id");
    openapiFields.add("id");
    openapiFields.add("invoice_email");
    openapiFields.add("language_id");
    openapiFields.add("modified");
    openapiFields.add("name");
    openapiFields.add("next_invoice_number");
    openapiFields.add("next_offer_number");
    openapiFields.add("next_project_number");
    openapiFields.add("phone");
    openapiFields.add("phone_countrycode");
    openapiFields.add("receive_form_mails");
    openapiFields.add("street_name");
    openapiFields.add("vat_percent");
    openapiFields.add("website");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Company
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Company.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Company is not found in the empty JSON string", Company.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Company.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Company` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("city_id") != null && !jsonObj.get("city_id").isJsonNull()) && !jsonObj.get("city_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city_id").toString()));
      }
      if ((jsonObj.get("contact_person_id") != null && !jsonObj.get("contact_person_id").isJsonNull()) && !jsonObj.get("contact_person_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_person_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact_person_id").toString()));
      }
      if ((jsonObj.get("country_id") != null && !jsonObj.get("country_id").isJsonNull()) && !jsonObj.get("country_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country_id").toString()));
      }
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      if ((jsonObj.get("created_by_id") != null && !jsonObj.get("created_by_id").isJsonNull()) && !jsonObj.get("created_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by_id").toString()));
      }
      if ((jsonObj.get("cvr") != null && !jsonObj.get("cvr").isJsonNull()) && !jsonObj.get("cvr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cvr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cvr").toString()));
      }
      if ((jsonObj.get("deleted") != null && !jsonObj.get("deleted").isJsonNull()) && !jsonObj.get("deleted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted").toString()));
      }
      if ((jsonObj.get("file_id") != null && !jsonObj.get("file_id").isJsonNull()) && !jsonObj.get("file_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `file_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("file_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("invoice_email") != null && !jsonObj.get("invoice_email").isJsonNull()) && !jsonObj.get("invoice_email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `invoice_email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("invoice_email").toString()));
      }
      if ((jsonObj.get("language_id") != null && !jsonObj.get("language_id").isJsonNull()) && !jsonObj.get("language_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language_id").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      if ((jsonObj.get("phone_countrycode") != null && !jsonObj.get("phone_countrycode").isJsonNull()) && !jsonObj.get("phone_countrycode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone_countrycode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone_countrycode").toString()));
      }
      if ((jsonObj.get("receive_form_mails") != null && !jsonObj.get("receive_form_mails").isJsonNull()) && !jsonObj.get("receive_form_mails").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `receive_form_mails` to be a primitive type in the JSON string but got `%s`", jsonObj.get("receive_form_mails").toString()));
      }
      if ((jsonObj.get("street_name") != null && !jsonObj.get("street_name").isJsonNull()) && !jsonObj.get("street_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `street_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("street_name").toString()));
      }
      if ((jsonObj.get("website") != null && !jsonObj.get("website").isJsonNull()) && !jsonObj.get("website").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `website` to be a primitive type in the JSON string but got `%s`", jsonObj.get("website").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Company.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Company' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Company> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Company.class));

       return (TypeAdapter<T>) new TypeAdapter<Company>() {
           @Override
           public void write(JsonWriter out, Company value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Company read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Company given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Company
   * @throws IOException if the JSON string is invalid with respect to Company
   */
  public static Company fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Company.class);
  }

  /**
   * Convert an instance of Company to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

