/*
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
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
import java.math.BigDecimal;
import java.net.URI;
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.client.model.CellPhone;
import org.openapitools.client.model.Email;
import org.openapitools.client.model.Fax;
import org.openapitools.client.model.HomePhone;
import org.openapitools.client.model.Phone;
import org.openapitools.client.model.Photo;
import org.openapitools.client.model.Title;
import org.openapitools.client.model.Url;
import org.openapitools.client.model.Videophone;
import org.openapitools.client.model.WorkPhone;

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
 * VCardData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:56.961414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VCardData {
  public static final String SERIALIZED_NAME_BIRTHDAY = "birthday";
  @SerializedName(SERIALIZED_NAME_BIRTHDAY)
  private LocalDate birthday;

  public static final String SERIALIZED_NAME_CELL_PHONE = "cell_phone";
  @SerializedName(SERIALIZED_NAME_CELL_PHONE)
  private CellPhone cellPhone;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "display_name";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private Email email;

  /**
   * &#x60;vcard&#x60; encoding. Universal standard for electronic business cards, typically stored as &#x60;*.vcf&#x60; file. It allows you to encode more types of data compared to its &#x60;mecard&#x60; equivalent, but it results in a larger QR code.  For more information please refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/VCard\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;en.wikipedia.org&lt;/a&gt;.
   */
  @JsonAdapter(EncodingEnum.Adapter.class)
  public enum EncodingEnum {
    VCARD("vcard");

    private String value;

    EncodingEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EncodingEnum fromValue(String value) {
      for (EncodingEnum b : EncodingEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EncodingEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EncodingEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EncodingEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EncodingEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EncodingEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ENCODING = "encoding";
  @SerializedName(SERIALIZED_NAME_ENCODING)
  private EncodingEnum encoding = EncodingEnum.VCARD;

  public static final String SERIALIZED_NAME_FAX = "fax";
  @SerializedName(SERIALIZED_NAME_FAX)
  private Fax fax;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_HOME_PHONE = "home_phone";
  @SerializedName(SERIALIZED_NAME_HOME_PHONE)
  private HomePhone homePhone;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_LATITUDE = "latitude";
  @SerializedName(SERIALIZED_NAME_LATITUDE)
  private BigDecimal latitude;

  public static final String SERIALIZED_NAME_LONGITUDE = "longitude";
  @SerializedName(SERIALIZED_NAME_LONGITUDE)
  private BigDecimal longitude;

  public static final String SERIALIZED_NAME_MEMO = "memo";
  @SerializedName(SERIALIZED_NAME_MEMO)
  private String memo;

  public static final String SERIALIZED_NAME_NICKNAME = "nickname";
  @SerializedName(SERIALIZED_NAME_NICKNAME)
  private String nickname;

  public static final String SERIALIZED_NAME_ORGANIZATION = "organization";
  @SerializedName(SERIALIZED_NAME_ORGANIZATION)
  private String organization;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private Phone phone;

  public static final String SERIALIZED_NAME_PHOTO = "photo";
  @SerializedName(SERIALIZED_NAME_PHOTO)
  private Photo photo;

  public static final String SERIALIZED_NAME_PO_BOX = "po_box";
  @SerializedName(SERIALIZED_NAME_PO_BOX)
  private String poBox;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_REVISION = "revision";
  @SerializedName(SERIALIZED_NAME_REVISION)
  private LocalDate revision;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private URI source;

  public static final String SERIALIZED_NAME_STREET = "street";
  @SerializedName(SERIALIZED_NAME_STREET)
  private String street;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private Title title;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private Url url;

  public static final String SERIALIZED_NAME_VIDEOPHONE = "videophone";
  @SerializedName(SERIALIZED_NAME_VIDEOPHONE)
  private Videophone videophone;

  public static final String SERIALIZED_NAME_WORK_PHONE = "work_phone";
  @SerializedName(SERIALIZED_NAME_WORK_PHONE)
  private WorkPhone workPhone;

  public static final String SERIALIZED_NAME_ZIP_CODE = "zip_code";
  @SerializedName(SERIALIZED_NAME_ZIP_CODE)
  private String zipCode;

  public VCardData() {
  }

  public VCardData birthday(LocalDate birthday) {
    this.birthday = birthday;
    return this;
  }

  /**
   * Birthday.
   * @return birthday
   */
  @javax.annotation.Nullable
  public LocalDate getBirthday() {
    return birthday;
  }

  public void setBirthday(LocalDate birthday) {
    this.birthday = birthday;
  }


  public VCardData cellPhone(CellPhone cellPhone) {
    this.cellPhone = cellPhone;
    return this;
  }

  /**
   * Get cellPhone
   * @return cellPhone
   */
  @javax.annotation.Nullable
  public CellPhone getCellPhone() {
    return cellPhone;
  }

  public void setCellPhone(CellPhone cellPhone) {
    this.cellPhone = cellPhone;
  }


  public VCardData city(String city) {
    this.city = city;
    return this;
  }

  /**
   * Address information: City.
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public VCardData country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Address information: Country.
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public VCardData displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * Common name. By default, equals to concatenated &#x60;first_name&#x60; and &#x60;last_name&#x60;.
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public VCardData email(Email email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public Email getEmail() {
    return email;
  }

  public void setEmail(Email email) {
    this.email = email;
  }


  public VCardData encoding(EncodingEnum encoding) {
    this.encoding = encoding;
    return this;
  }

  /**
   * &#x60;vcard&#x60; encoding. Universal standard for electronic business cards, typically stored as &#x60;*.vcf&#x60; file. It allows you to encode more types of data compared to its &#x60;mecard&#x60; equivalent, but it results in a larger QR code.  For more information please refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/VCard\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;en.wikipedia.org&lt;/a&gt;.
   * @return encoding
   */
  @javax.annotation.Nullable
  public EncodingEnum getEncoding() {
    return encoding;
  }

  public void setEncoding(EncodingEnum encoding) {
    this.encoding = encoding;
  }


  public VCardData fax(Fax fax) {
    this.fax = fax;
    return this;
  }

  /**
   * Get fax
   * @return fax
   */
  @javax.annotation.Nullable
  public Fax getFax() {
    return fax;
  }

  public void setFax(Fax fax) {
    this.fax = fax;
  }


  public VCardData firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * First name.
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public VCardData homePhone(HomePhone homePhone) {
    this.homePhone = homePhone;
    return this;
  }

  /**
   * Get homePhone
   * @return homePhone
   */
  @javax.annotation.Nullable
  public HomePhone getHomePhone() {
    return homePhone;
  }

  public void setHomePhone(HomePhone homePhone) {
    this.homePhone = homePhone;
  }


  public VCardData lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * Last name.
   * @return lastName
   */
  @javax.annotation.Nonnull
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public VCardData latitude(BigDecimal latitude) {
    this.latitude = latitude;
    return this;
  }

  /**
   * Location latitude.
   * minimum: -90
   * maximum: 90
   * @return latitude
   */
  @javax.annotation.Nullable
  public BigDecimal getLatitude() {
    return latitude;
  }

  public void setLatitude(BigDecimal latitude) {
    this.latitude = latitude;
  }


  public VCardData longitude(BigDecimal longitude) {
    this.longitude = longitude;
    return this;
  }

  /**
   * Location longitude.
   * minimum: -180
   * maximum: 180
   * @return longitude
   */
  @javax.annotation.Nullable
  public BigDecimal getLongitude() {
    return longitude;
  }

  public void setLongitude(BigDecimal longitude) {
    this.longitude = longitude;
  }


  public VCardData memo(String memo) {
    this.memo = memo;
    return this;
  }

  /**
   * Short notice.
   * @return memo
   */
  @javax.annotation.Nullable
  public String getMemo() {
    return memo;
  }

  public void setMemo(String memo) {
    this.memo = memo;
  }


  public VCardData nickname(String nickname) {
    this.nickname = nickname;
    return this;
  }

  /**
   * Nickname.
   * @return nickname
   */
  @javax.annotation.Nullable
  public String getNickname() {
    return nickname;
  }

  public void setNickname(String nickname) {
    this.nickname = nickname;
  }


  public VCardData organization(String organization) {
    this.organization = organization;
    return this;
  }

  /**
   * Organization/company name
   * @return organization
   */
  @javax.annotation.Nullable
  public String getOrganization() {
    return organization;
  }

  public void setOrganization(String organization) {
    this.organization = organization;
  }


  public VCardData phone(Phone phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Get phone
   * @return phone
   */
  @javax.annotation.Nullable
  public Phone getPhone() {
    return phone;
  }

  public void setPhone(Phone phone) {
    this.phone = phone;
  }


  public VCardData photo(Photo photo) {
    this.photo = photo;
    return this;
  }

  /**
   * Get photo
   * @return photo
   */
  @javax.annotation.Nullable
  public Photo getPhoto() {
    return photo;
  }

  public void setPhoto(Photo photo) {
    this.photo = photo;
  }


  public VCardData poBox(String poBox) {
    this.poBox = poBox;
    return this;
  }

  /**
   * Address information: Post Office Box.
   * @return poBox
   */
  @javax.annotation.Nullable
  public String getPoBox() {
    return poBox;
  }

  public void setPoBox(String poBox) {
    this.poBox = poBox;
  }


  public VCardData region(String region) {
    this.region = region;
    return this;
  }

  /**
   * Address information: Region.
   * @return region
   */
  @javax.annotation.Nullable
  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }


  public VCardData revision(LocalDate revision) {
    this.revision = revision;
    return this;
  }

  /**
   * vCard revision/last modification date.
   * @return revision
   */
  @javax.annotation.Nullable
  public LocalDate getRevision() {
    return revision;
  }

  public void setRevision(LocalDate revision) {
    this.revision = revision;
  }


  public VCardData source(URI source) {
    this.source = source;
    return this;
  }

  /**
   * URL pointing to vCard file itself.
   * @return source
   */
  @javax.annotation.Nullable
  public URI getSource() {
    return source;
  }

  public void setSource(URI source) {
    this.source = source;
  }


  public VCardData street(String street) {
    this.street = street;
    return this;
  }

  /**
   * Address information: Street.
   * @return street
   */
  @javax.annotation.Nullable
  public String getStreet() {
    return street;
  }

  public void setStreet(String street) {
    this.street = street;
  }


  public VCardData title(Title title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public Title getTitle() {
    return title;
  }

  public void setTitle(Title title) {
    this.title = title;
  }


  public VCardData url(Url url) {
    this.url = url;
    return this;
  }

  /**
   * Get url
   * @return url
   */
  @javax.annotation.Nullable
  public Url getUrl() {
    return url;
  }

  public void setUrl(Url url) {
    this.url = url;
  }


  public VCardData videophone(Videophone videophone) {
    this.videophone = videophone;
    return this;
  }

  /**
   * Get videophone
   * @return videophone
   */
  @javax.annotation.Nullable
  public Videophone getVideophone() {
    return videophone;
  }

  public void setVideophone(Videophone videophone) {
    this.videophone = videophone;
  }


  public VCardData workPhone(WorkPhone workPhone) {
    this.workPhone = workPhone;
    return this;
  }

  /**
   * Get workPhone
   * @return workPhone
   */
  @javax.annotation.Nullable
  public WorkPhone getWorkPhone() {
    return workPhone;
  }

  public void setWorkPhone(WorkPhone workPhone) {
    this.workPhone = workPhone;
  }


  public VCardData zipCode(String zipCode) {
    this.zipCode = zipCode;
    return this;
  }

  /**
   * Address information: ZIP code.
   * @return zipCode
   */
  @javax.annotation.Nullable
  public String getZipCode() {
    return zipCode;
  }

  public void setZipCode(String zipCode) {
    this.zipCode = zipCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VCardData vcardData = (VCardData) o;
    return Objects.equals(this.birthday, vcardData.birthday) &&
        Objects.equals(this.cellPhone, vcardData.cellPhone) &&
        Objects.equals(this.city, vcardData.city) &&
        Objects.equals(this.country, vcardData.country) &&
        Objects.equals(this.displayName, vcardData.displayName) &&
        Objects.equals(this.email, vcardData.email) &&
        Objects.equals(this.encoding, vcardData.encoding) &&
        Objects.equals(this.fax, vcardData.fax) &&
        Objects.equals(this.firstName, vcardData.firstName) &&
        Objects.equals(this.homePhone, vcardData.homePhone) &&
        Objects.equals(this.lastName, vcardData.lastName) &&
        Objects.equals(this.latitude, vcardData.latitude) &&
        Objects.equals(this.longitude, vcardData.longitude) &&
        Objects.equals(this.memo, vcardData.memo) &&
        Objects.equals(this.nickname, vcardData.nickname) &&
        Objects.equals(this.organization, vcardData.organization) &&
        Objects.equals(this.phone, vcardData.phone) &&
        Objects.equals(this.photo, vcardData.photo) &&
        Objects.equals(this.poBox, vcardData.poBox) &&
        Objects.equals(this.region, vcardData.region) &&
        Objects.equals(this.revision, vcardData.revision) &&
        Objects.equals(this.source, vcardData.source) &&
        Objects.equals(this.street, vcardData.street) &&
        Objects.equals(this.title, vcardData.title) &&
        Objects.equals(this.url, vcardData.url) &&
        Objects.equals(this.videophone, vcardData.videophone) &&
        Objects.equals(this.workPhone, vcardData.workPhone) &&
        Objects.equals(this.zipCode, vcardData.zipCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(birthday, cellPhone, city, country, displayName, email, encoding, fax, firstName, homePhone, lastName, latitude, longitude, memo, nickname, organization, phone, photo, poBox, region, revision, source, street, title, url, videophone, workPhone, zipCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VCardData {\n");
    sb.append("    birthday: ").append(toIndentedString(birthday)).append("\n");
    sb.append("    cellPhone: ").append(toIndentedString(cellPhone)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    encoding: ").append(toIndentedString(encoding)).append("\n");
    sb.append("    fax: ").append(toIndentedString(fax)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    homePhone: ").append(toIndentedString(homePhone)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    latitude: ").append(toIndentedString(latitude)).append("\n");
    sb.append("    longitude: ").append(toIndentedString(longitude)).append("\n");
    sb.append("    memo: ").append(toIndentedString(memo)).append("\n");
    sb.append("    nickname: ").append(toIndentedString(nickname)).append("\n");
    sb.append("    organization: ").append(toIndentedString(organization)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    photo: ").append(toIndentedString(photo)).append("\n");
    sb.append("    poBox: ").append(toIndentedString(poBox)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    revision: ").append(toIndentedString(revision)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    street: ").append(toIndentedString(street)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    videophone: ").append(toIndentedString(videophone)).append("\n");
    sb.append("    workPhone: ").append(toIndentedString(workPhone)).append("\n");
    sb.append("    zipCode: ").append(toIndentedString(zipCode)).append("\n");
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
    openapiFields.add("birthday");
    openapiFields.add("cell_phone");
    openapiFields.add("city");
    openapiFields.add("country");
    openapiFields.add("display_name");
    openapiFields.add("email");
    openapiFields.add("encoding");
    openapiFields.add("fax");
    openapiFields.add("first_name");
    openapiFields.add("home_phone");
    openapiFields.add("last_name");
    openapiFields.add("latitude");
    openapiFields.add("longitude");
    openapiFields.add("memo");
    openapiFields.add("nickname");
    openapiFields.add("organization");
    openapiFields.add("phone");
    openapiFields.add("photo");
    openapiFields.add("po_box");
    openapiFields.add("region");
    openapiFields.add("revision");
    openapiFields.add("source");
    openapiFields.add("street");
    openapiFields.add("title");
    openapiFields.add("url");
    openapiFields.add("videophone");
    openapiFields.add("work_phone");
    openapiFields.add("zip_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("last_name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VCardData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VCardData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VCardData is not found in the empty JSON string", VCardData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VCardData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VCardData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : VCardData.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `cell_phone`
      if (jsonObj.get("cell_phone") != null && !jsonObj.get("cell_phone").isJsonNull()) {
        CellPhone.validateJsonElement(jsonObj.get("cell_phone"));
      }
      if ((jsonObj.get("city") != null && !jsonObj.get("city").isJsonNull()) && !jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if ((jsonObj.get("display_name") != null && !jsonObj.get("display_name").isJsonNull()) && !jsonObj.get("display_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_name").toString()));
      }
      // validate the optional field `email`
      if (jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) {
        Email.validateJsonElement(jsonObj.get("email"));
      }
      if ((jsonObj.get("encoding") != null && !jsonObj.get("encoding").isJsonNull()) && !jsonObj.get("encoding").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `encoding` to be a primitive type in the JSON string but got `%s`", jsonObj.get("encoding").toString()));
      }
      // validate the optional field `encoding`
      if (jsonObj.get("encoding") != null && !jsonObj.get("encoding").isJsonNull()) {
        EncodingEnum.validateJsonElement(jsonObj.get("encoding"));
      }
      // validate the optional field `fax`
      if (jsonObj.get("fax") != null && !jsonObj.get("fax").isJsonNull()) {
        Fax.validateJsonElement(jsonObj.get("fax"));
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      // validate the optional field `home_phone`
      if (jsonObj.get("home_phone") != null && !jsonObj.get("home_phone").isJsonNull()) {
        HomePhone.validateJsonElement(jsonObj.get("home_phone"));
      }
      if (!jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("memo") != null && !jsonObj.get("memo").isJsonNull()) && !jsonObj.get("memo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `memo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("memo").toString()));
      }
      if ((jsonObj.get("nickname") != null && !jsonObj.get("nickname").isJsonNull()) && !jsonObj.get("nickname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nickname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nickname").toString()));
      }
      if ((jsonObj.get("organization") != null && !jsonObj.get("organization").isJsonNull()) && !jsonObj.get("organization").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `organization` to be a primitive type in the JSON string but got `%s`", jsonObj.get("organization").toString()));
      }
      // validate the optional field `phone`
      if (jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) {
        Phone.validateJsonElement(jsonObj.get("phone"));
      }
      // validate the optional field `photo`
      if (jsonObj.get("photo") != null && !jsonObj.get("photo").isJsonNull()) {
        Photo.validateJsonElement(jsonObj.get("photo"));
      }
      if ((jsonObj.get("po_box") != null && !jsonObj.get("po_box").isJsonNull()) && !jsonObj.get("po_box").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `po_box` to be a primitive type in the JSON string but got `%s`", jsonObj.get("po_box").toString()));
      }
      if ((jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) && !jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      if ((jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) && !jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      if ((jsonObj.get("street") != null && !jsonObj.get("street").isJsonNull()) && !jsonObj.get("street").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `street` to be a primitive type in the JSON string but got `%s`", jsonObj.get("street").toString()));
      }
      // validate the optional field `title`
      if (jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) {
        Title.validateJsonElement(jsonObj.get("title"));
      }
      // validate the optional field `url`
      if (jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) {
        Url.validateJsonElement(jsonObj.get("url"));
      }
      // validate the optional field `videophone`
      if (jsonObj.get("videophone") != null && !jsonObj.get("videophone").isJsonNull()) {
        Videophone.validateJsonElement(jsonObj.get("videophone"));
      }
      // validate the optional field `work_phone`
      if (jsonObj.get("work_phone") != null && !jsonObj.get("work_phone").isJsonNull()) {
        WorkPhone.validateJsonElement(jsonObj.get("work_phone"));
      }
      if ((jsonObj.get("zip_code") != null && !jsonObj.get("zip_code").isJsonNull()) && !jsonObj.get("zip_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `zip_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("zip_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VCardData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VCardData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VCardData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VCardData.class));

       return (TypeAdapter<T>) new TypeAdapter<VCardData>() {
           @Override
           public void write(JsonWriter out, VCardData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VCardData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VCardData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VCardData
   * @throws IOException if the JSON string is invalid with respect to VCardData
   */
  public static VCardData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VCardData.class);
  }

  /**
   * Convert an instance of VCardData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

