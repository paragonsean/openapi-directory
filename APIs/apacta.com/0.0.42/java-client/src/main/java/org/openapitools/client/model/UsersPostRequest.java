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
import java.util.Arrays;
import java.util.UUID;
import org.openapitools.client.model.ContactsPostRequestContactTypes;

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
 * UsersPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UsersPostRequest {
  public static final String SERIALIZED_NAME_CITY_ID = "city_id";
  @SerializedName(SERIALIZED_NAME_CITY_ID)
  private UUID cityId;

  public static final String SERIALIZED_NAME_COST_PRICE = "cost_price";
  @SerializedName(SERIALIZED_NAME_COST_PRICE)
  private Float costPrice;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_EXPECTED_BILLABLE_HOURS = "expected_billable_hours";
  @SerializedName(SERIALIZED_NAME_EXPECTED_BILLABLE_HOURS)
  private Float expectedBillableHours;

  public static final String SERIALIZED_NAME_EXTRA_PRICE = "extra_price";
  @SerializedName(SERIALIZED_NAME_EXTRA_PRICE)
  private Float extraPrice;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_HIDE_ADDRESS = "hide_address";
  @SerializedName(SERIALIZED_NAME_HIDE_ADDRESS)
  private Boolean hideAddress;

  public static final String SERIALIZED_NAME_HIDE_PHONE = "hide_phone";
  @SerializedName(SERIALIZED_NAME_HIDE_PHONE)
  private Boolean hidePhone;

  public static final String SERIALIZED_NAME_INITIALS = "initials";
  @SerializedName(SERIALIZED_NAME_INITIALS)
  private String initials;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "is_active";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_LANGUAGE_ID = "language_id";
  @SerializedName(SERIALIZED_NAME_LANGUAGE_ID)
  private UUID languageId;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_MOBILE = "mobile";
  @SerializedName(SERIALIZED_NAME_MOBILE)
  private String mobile;

  public static final String SERIALIZED_NAME_MOBILE_COUNTRYCODE = "mobile_countrycode";
  @SerializedName(SERIALIZED_NAME_MOBILE_COUNTRYCODE)
  private String mobileCountrycode;

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_PHONE_COUNTRYCODE = "phone_countrycode";
  @SerializedName(SERIALIZED_NAME_PHONE_COUNTRYCODE)
  private String phoneCountrycode;

  public static final String SERIALIZED_NAME_RECEIVE_FORM_MAILS = "receive_form_mails";
  @SerializedName(SERIALIZED_NAME_RECEIVE_FORM_MAILS)
  private Boolean receiveFormMails;

  public static final String SERIALIZED_NAME_ROLES = "roles";
  @SerializedName(SERIALIZED_NAME_ROLES)
  private ContactsPostRequestContactTypes roles;

  public static final String SERIALIZED_NAME_SALE_PRICE = "sale_price";
  @SerializedName(SERIALIZED_NAME_SALE_PRICE)
  private Float salePrice;

  public static final String SERIALIZED_NAME_STREET_NAME = "street_name";
  @SerializedName(SERIALIZED_NAME_STREET_NAME)
  private String streetName;

  public UsersPostRequest() {
  }

  public UsersPostRequest cityId(UUID cityId) {
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


  public UsersPostRequest costPrice(Float costPrice) {
    this.costPrice = costPrice;
    return this;
  }

  /**
   * Cost of salaries
   * @return costPrice
   */
  @javax.annotation.Nullable
  public Float getCostPrice() {
    return costPrice;
  }

  public void setCostPrice(Float costPrice) {
    this.costPrice = costPrice;
  }


  public UsersPostRequest email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public UsersPostRequest expectedBillableHours(Float expectedBillableHours) {
    this.expectedBillableHours = expectedBillableHours;
    return this;
  }

  /**
   * Get expectedBillableHours
   * @return expectedBillableHours
   */
  @javax.annotation.Nullable
  public Float getExpectedBillableHours() {
    return expectedBillableHours;
  }

  public void setExpectedBillableHours(Float expectedBillableHours) {
    this.expectedBillableHours = expectedBillableHours;
  }


  public UsersPostRequest extraPrice(Float extraPrice) {
    this.extraPrice = extraPrice;
    return this;
  }

  /**
   * Additional cost on this employee (pension, vacation etc.)
   * @return extraPrice
   */
  @javax.annotation.Nullable
  public Float getExtraPrice() {
    return extraPrice;
  }

  public void setExtraPrice(Float extraPrice) {
    this.extraPrice = extraPrice;
  }


  public UsersPostRequest firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * Get firstName
   * @return firstName
   */
  @javax.annotation.Nonnull
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public UsersPostRequest hideAddress(Boolean hideAddress) {
    this.hideAddress = hideAddress;
    return this;
  }

  /**
   * Get hideAddress
   * @return hideAddress
   */
  @javax.annotation.Nullable
  public Boolean getHideAddress() {
    return hideAddress;
  }

  public void setHideAddress(Boolean hideAddress) {
    this.hideAddress = hideAddress;
  }


  public UsersPostRequest hidePhone(Boolean hidePhone) {
    this.hidePhone = hidePhone;
    return this;
  }

  /**
   * Get hidePhone
   * @return hidePhone
   */
  @javax.annotation.Nullable
  public Boolean getHidePhone() {
    return hidePhone;
  }

  public void setHidePhone(Boolean hidePhone) {
    this.hidePhone = hidePhone;
  }


  public UsersPostRequest initials(String initials) {
    this.initials = initials;
    return this;
  }

  /**
   * Get initials
   * @return initials
   */
  @javax.annotation.Nullable
  public String getInitials() {
    return initials;
  }

  public void setInitials(String initials) {
    this.initials = initials;
  }


  public UsersPostRequest isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Get isActive
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public UsersPostRequest languageId(UUID languageId) {
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


  public UsersPostRequest lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * Get lastName
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public UsersPostRequest mobile(String mobile) {
    this.mobile = mobile;
    return this;
  }

  /**
   * Get mobile
   * @return mobile
   */
  @javax.annotation.Nullable
  public String getMobile() {
    return mobile;
  }

  public void setMobile(String mobile) {
    this.mobile = mobile;
  }


  public UsersPostRequest mobileCountrycode(String mobileCountrycode) {
    this.mobileCountrycode = mobileCountrycode;
    return this;
  }

  /**
   * Get mobileCountrycode
   * @return mobileCountrycode
   */
  @javax.annotation.Nullable
  public String getMobileCountrycode() {
    return mobileCountrycode;
  }

  public void setMobileCountrycode(String mobileCountrycode) {
    this.mobileCountrycode = mobileCountrycode;
  }


  public UsersPostRequest password(String password) {
    this.password = password;
    return this;
  }

  /**
   * Get password
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public UsersPostRequest phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Get phone
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public UsersPostRequest phoneCountrycode(String phoneCountrycode) {
    this.phoneCountrycode = phoneCountrycode;
    return this;
  }

  /**
   * Get phoneCountrycode
   * @return phoneCountrycode
   */
  @javax.annotation.Nullable
  public String getPhoneCountrycode() {
    return phoneCountrycode;
  }

  public void setPhoneCountrycode(String phoneCountrycode) {
    this.phoneCountrycode = phoneCountrycode;
  }


  public UsersPostRequest receiveFormMails(Boolean receiveFormMails) {
    this.receiveFormMails = receiveFormMails;
    return this;
  }

  /**
   * If &#x60;true&#x60; the employee will receive an email receipt of every form submitted
   * @return receiveFormMails
   */
  @javax.annotation.Nullable
  public Boolean getReceiveFormMails() {
    return receiveFormMails;
  }

  public void setReceiveFormMails(Boolean receiveFormMails) {
    this.receiveFormMails = receiveFormMails;
  }


  public UsersPostRequest roles(ContactsPostRequestContactTypes roles) {
    this.roles = roles;
    return this;
  }

  /**
   * Get roles
   * @return roles
   */
  @javax.annotation.Nullable
  public ContactsPostRequestContactTypes getRoles() {
    return roles;
  }

  public void setRoles(ContactsPostRequestContactTypes roles) {
    this.roles = roles;
  }


  public UsersPostRequest salePrice(Float salePrice) {
    this.salePrice = salePrice;
    return this;
  }

  /**
   * The price this employee costs per hour when working
   * @return salePrice
   */
  @javax.annotation.Nullable
  public Float getSalePrice() {
    return salePrice;
  }

  public void setSalePrice(Float salePrice) {
    this.salePrice = salePrice;
  }


  public UsersPostRequest streetName(String streetName) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UsersPostRequest usersPostRequest = (UsersPostRequest) o;
    return Objects.equals(this.cityId, usersPostRequest.cityId) &&
        Objects.equals(this.costPrice, usersPostRequest.costPrice) &&
        Objects.equals(this.email, usersPostRequest.email) &&
        Objects.equals(this.expectedBillableHours, usersPostRequest.expectedBillableHours) &&
        Objects.equals(this.extraPrice, usersPostRequest.extraPrice) &&
        Objects.equals(this.firstName, usersPostRequest.firstName) &&
        Objects.equals(this.hideAddress, usersPostRequest.hideAddress) &&
        Objects.equals(this.hidePhone, usersPostRequest.hidePhone) &&
        Objects.equals(this.initials, usersPostRequest.initials) &&
        Objects.equals(this.isActive, usersPostRequest.isActive) &&
        Objects.equals(this.languageId, usersPostRequest.languageId) &&
        Objects.equals(this.lastName, usersPostRequest.lastName) &&
        Objects.equals(this.mobile, usersPostRequest.mobile) &&
        Objects.equals(this.mobileCountrycode, usersPostRequest.mobileCountrycode) &&
        Objects.equals(this.password, usersPostRequest.password) &&
        Objects.equals(this.phone, usersPostRequest.phone) &&
        Objects.equals(this.phoneCountrycode, usersPostRequest.phoneCountrycode) &&
        Objects.equals(this.receiveFormMails, usersPostRequest.receiveFormMails) &&
        Objects.equals(this.roles, usersPostRequest.roles) &&
        Objects.equals(this.salePrice, usersPostRequest.salePrice) &&
        Objects.equals(this.streetName, usersPostRequest.streetName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cityId, costPrice, email, expectedBillableHours, extraPrice, firstName, hideAddress, hidePhone, initials, isActive, languageId, lastName, mobile, mobileCountrycode, password, phone, phoneCountrycode, receiveFormMails, roles, salePrice, streetName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UsersPostRequest {\n");
    sb.append("    cityId: ").append(toIndentedString(cityId)).append("\n");
    sb.append("    costPrice: ").append(toIndentedString(costPrice)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    expectedBillableHours: ").append(toIndentedString(expectedBillableHours)).append("\n");
    sb.append("    extraPrice: ").append(toIndentedString(extraPrice)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    hideAddress: ").append(toIndentedString(hideAddress)).append("\n");
    sb.append("    hidePhone: ").append(toIndentedString(hidePhone)).append("\n");
    sb.append("    initials: ").append(toIndentedString(initials)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    languageId: ").append(toIndentedString(languageId)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    mobile: ").append(toIndentedString(mobile)).append("\n");
    sb.append("    mobileCountrycode: ").append(toIndentedString(mobileCountrycode)).append("\n");
    sb.append("    password: ").append("*").append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    phoneCountrycode: ").append(toIndentedString(phoneCountrycode)).append("\n");
    sb.append("    receiveFormMails: ").append(toIndentedString(receiveFormMails)).append("\n");
    sb.append("    roles: ").append(toIndentedString(roles)).append("\n");
    sb.append("    salePrice: ").append(toIndentedString(salePrice)).append("\n");
    sb.append("    streetName: ").append(toIndentedString(streetName)).append("\n");
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
    openapiFields.add("cost_price");
    openapiFields.add("email");
    openapiFields.add("expected_billable_hours");
    openapiFields.add("extra_price");
    openapiFields.add("first_name");
    openapiFields.add("hide_address");
    openapiFields.add("hide_phone");
    openapiFields.add("initials");
    openapiFields.add("is_active");
    openapiFields.add("language_id");
    openapiFields.add("last_name");
    openapiFields.add("mobile");
    openapiFields.add("mobile_countrycode");
    openapiFields.add("password");
    openapiFields.add("phone");
    openapiFields.add("phone_countrycode");
    openapiFields.add("receive_form_mails");
    openapiFields.add("roles");
    openapiFields.add("sale_price");
    openapiFields.add("street_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("first_name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UsersPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UsersPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UsersPostRequest is not found in the empty JSON string", UsersPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UsersPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UsersPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UsersPostRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("city_id") != null && !jsonObj.get("city_id").isJsonNull()) && !jsonObj.get("city_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city_id").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if (!jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      if ((jsonObj.get("initials") != null && !jsonObj.get("initials").isJsonNull()) && !jsonObj.get("initials").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `initials` to be a primitive type in the JSON string but got `%s`", jsonObj.get("initials").toString()));
      }
      if ((jsonObj.get("language_id") != null && !jsonObj.get("language_id").isJsonNull()) && !jsonObj.get("language_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language_id").toString()));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("mobile") != null && !jsonObj.get("mobile").isJsonNull()) && !jsonObj.get("mobile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mobile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mobile").toString()));
      }
      if ((jsonObj.get("mobile_countrycode") != null && !jsonObj.get("mobile_countrycode").isJsonNull()) && !jsonObj.get("mobile_countrycode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mobile_countrycode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mobile_countrycode").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      if ((jsonObj.get("phone_countrycode") != null && !jsonObj.get("phone_countrycode").isJsonNull()) && !jsonObj.get("phone_countrycode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone_countrycode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone_countrycode").toString()));
      }
      // validate the optional field `roles`
      if (jsonObj.get("roles") != null && !jsonObj.get("roles").isJsonNull()) {
        ContactsPostRequestContactTypes.validateJsonElement(jsonObj.get("roles"));
      }
      if ((jsonObj.get("street_name") != null && !jsonObj.get("street_name").isJsonNull()) && !jsonObj.get("street_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `street_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("street_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UsersPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UsersPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UsersPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UsersPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UsersPostRequest>() {
           @Override
           public void write(JsonWriter out, UsersPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UsersPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UsersPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UsersPostRequest
   * @throws IOException if the JSON string is invalid with respect to UsersPostRequest
   */
  public static UsersPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UsersPostRequest.class);
  }

  /**
   * Convert an instance of UsersPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

