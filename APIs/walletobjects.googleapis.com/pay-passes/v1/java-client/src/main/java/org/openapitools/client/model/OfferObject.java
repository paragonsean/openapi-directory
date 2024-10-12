/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AppLinkData;
import org.openapitools.client.model.Barcode;
import org.openapitools.client.model.GroupingInfo;
import org.openapitools.client.model.Image;
import org.openapitools.client.model.ImageModuleData;
import org.openapitools.client.model.InfoModuleData;
import org.openapitools.client.model.LatLongPoint;
import org.openapitools.client.model.LinksModuleData;
import org.openapitools.client.model.Message;
import org.openapitools.client.model.OfferClass;
import org.openapitools.client.model.PassConstraints;
import org.openapitools.client.model.RotatingBarcode;
import org.openapitools.client.model.TextModuleData;
import org.openapitools.client.model.TimeInterval;

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
 * OfferObject
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OfferObject {
  public static final String SERIALIZED_NAME_APP_LINK_DATA = "appLinkData";
  @SerializedName(SERIALIZED_NAME_APP_LINK_DATA)
  private AppLinkData appLinkData;

  public static final String SERIALIZED_NAME_BARCODE = "barcode";
  @SerializedName(SERIALIZED_NAME_BARCODE)
  private Barcode barcode;

  public static final String SERIALIZED_NAME_CLASS_ID = "classId";
  @SerializedName(SERIALIZED_NAME_CLASS_ID)
  private String classId;

  public static final String SERIALIZED_NAME_CLASS_REFERENCE = "classReference";
  @SerializedName(SERIALIZED_NAME_CLASS_REFERENCE)
  private OfferClass classReference;

  public static final String SERIALIZED_NAME_DISABLE_EXPIRATION_NOTIFICATION = "disableExpirationNotification";
  @SerializedName(SERIALIZED_NAME_DISABLE_EXPIRATION_NOTIFICATION)
  private Boolean disableExpirationNotification;

  public static final String SERIALIZED_NAME_GROUPING_INFO = "groupingInfo";
  @SerializedName(SERIALIZED_NAME_GROUPING_INFO)
  private GroupingInfo groupingInfo;

  public static final String SERIALIZED_NAME_HAS_LINKED_DEVICE = "hasLinkedDevice";
  @SerializedName(SERIALIZED_NAME_HAS_LINKED_DEVICE)
  private Boolean hasLinkedDevice;

  public static final String SERIALIZED_NAME_HAS_USERS = "hasUsers";
  @SerializedName(SERIALIZED_NAME_HAS_USERS)
  private Boolean hasUsers;

  public static final String SERIALIZED_NAME_HERO_IMAGE = "heroImage";
  @SerializedName(SERIALIZED_NAME_HERO_IMAGE)
  private Image heroImage;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IMAGE_MODULES_DATA = "imageModulesData";
  @SerializedName(SERIALIZED_NAME_IMAGE_MODULES_DATA)
  private List<ImageModuleData> imageModulesData = new ArrayList<>();

  public static final String SERIALIZED_NAME_INFO_MODULE_DATA = "infoModuleData";
  @SerializedName(SERIALIZED_NAME_INFO_MODULE_DATA)
  private InfoModuleData infoModuleData;

  public static final String SERIALIZED_NAME_KIND = "kind";
  @SerializedName(SERIALIZED_NAME_KIND)
  private String kind;

  public static final String SERIALIZED_NAME_LINKS_MODULE_DATA = "linksModuleData";
  @SerializedName(SERIALIZED_NAME_LINKS_MODULE_DATA)
  private LinksModuleData linksModuleData;

  public static final String SERIALIZED_NAME_LOCATIONS = "locations";
  @SerializedName(SERIALIZED_NAME_LOCATIONS)
  private List<LatLongPoint> locations = new ArrayList<>();

  public static final String SERIALIZED_NAME_MESSAGES = "messages";
  @SerializedName(SERIALIZED_NAME_MESSAGES)
  private List<Message> messages = new ArrayList<>();

  public static final String SERIALIZED_NAME_PASS_CONSTRAINTS = "passConstraints";
  @SerializedName(SERIALIZED_NAME_PASS_CONSTRAINTS)
  private PassConstraints passConstraints;

  public static final String SERIALIZED_NAME_ROTATING_BARCODE = "rotatingBarcode";
  @SerializedName(SERIALIZED_NAME_ROTATING_BARCODE)
  private RotatingBarcode rotatingBarcode;

  public static final String SERIALIZED_NAME_SMART_TAP_REDEMPTION_VALUE = "smartTapRedemptionValue";
  @SerializedName(SERIALIZED_NAME_SMART_TAP_REDEMPTION_VALUE)
  private String smartTapRedemptionValue;

  /**
   * Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section.
   */
  @JsonAdapter(StateEnum.Adapter.class)
  public enum StateEnum {
    STATE_UNSPECIFIED("STATE_UNSPECIFIED"),
    
    ACTIVE("ACTIVE"),
    
    ACTIVE2("active"),
    
    COMPLETED("COMPLETED"),
    
    COMPLETED2("completed"),
    
    EXPIRED("EXPIRED"),
    
    EXPIRED2("expired"),
    
    INACTIVE("INACTIVE"),
    
    INACTIVE2("inactive");

    private String value;

    StateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StateEnum fromValue(String value) {
      for (StateEnum b : StateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private StateEnum state;

  public static final String SERIALIZED_NAME_TEXT_MODULES_DATA = "textModulesData";
  @SerializedName(SERIALIZED_NAME_TEXT_MODULES_DATA)
  private List<TextModuleData> textModulesData = new ArrayList<>();

  public static final String SERIALIZED_NAME_VALID_TIME_INTERVAL = "validTimeInterval";
  @SerializedName(SERIALIZED_NAME_VALID_TIME_INTERVAL)
  private TimeInterval validTimeInterval;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public OfferObject() {
  }

  public OfferObject appLinkData(AppLinkData appLinkData) {
    this.appLinkData = appLinkData;
    return this;
  }

  /**
   * Get appLinkData
   * @return appLinkData
   */
  @javax.annotation.Nullable
  public AppLinkData getAppLinkData() {
    return appLinkData;
  }

  public void setAppLinkData(AppLinkData appLinkData) {
    this.appLinkData = appLinkData;
  }


  public OfferObject barcode(Barcode barcode) {
    this.barcode = barcode;
    return this;
  }

  /**
   * Get barcode
   * @return barcode
   */
  @javax.annotation.Nullable
  public Barcode getBarcode() {
    return barcode;
  }

  public void setBarcode(Barcode barcode) {
    this.barcode = barcode;
  }


  public OfferObject classId(String classId) {
    this.classId = classId;
    return this;
  }

  /**
   * Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you.
   * @return classId
   */
  @javax.annotation.Nullable
  public String getClassId() {
    return classId;
  }

  public void setClassId(String classId) {
    this.classId = classId;
  }


  public OfferObject classReference(OfferClass classReference) {
    this.classReference = classReference;
    return this;
  }

  /**
   * Get classReference
   * @return classReference
   */
  @javax.annotation.Nullable
  public OfferClass getClassReference() {
    return classReference;
  }

  public void setClassReference(OfferClass classReference) {
    this.classReference = classReference;
  }


  public OfferObject disableExpirationNotification(Boolean disableExpirationNotification) {
    this.disableExpirationNotification = disableExpirationNotification;
    return this;
  }

  /**
   * Indicates if notifications should explicitly be suppressed. If this field is set to true, regardless of the &#x60;messages&#x60; field, expiration notifications to the user will be suppressed. By default, this field is set to false. Currently, this can only be set for offers.
   * @return disableExpirationNotification
   */
  @javax.annotation.Nullable
  public Boolean getDisableExpirationNotification() {
    return disableExpirationNotification;
  }

  public void setDisableExpirationNotification(Boolean disableExpirationNotification) {
    this.disableExpirationNotification = disableExpirationNotification;
  }


  public OfferObject groupingInfo(GroupingInfo groupingInfo) {
    this.groupingInfo = groupingInfo;
    return this;
  }

  /**
   * Get groupingInfo
   * @return groupingInfo
   */
  @javax.annotation.Nullable
  public GroupingInfo getGroupingInfo() {
    return groupingInfo;
  }

  public void setGroupingInfo(GroupingInfo groupingInfo) {
    this.groupingInfo = groupingInfo;
  }


  public OfferObject hasLinkedDevice(Boolean hasLinkedDevice) {
    this.hasLinkedDevice = hasLinkedDevice;
    return this;
  }

  /**
   * Whether this object is currently linked to a single device. This field is set by the platform when a user saves the object, linking it to their device. Intended for use by select partners. Contact support for additional information.
   * @return hasLinkedDevice
   */
  @javax.annotation.Nullable
  public Boolean getHasLinkedDevice() {
    return hasLinkedDevice;
  }

  public void setHasLinkedDevice(Boolean hasLinkedDevice) {
    this.hasLinkedDevice = hasLinkedDevice;
  }


  public OfferObject hasUsers(Boolean hasUsers) {
    this.hasUsers = hasUsers;
    return this;
  }

  /**
   * Indicates if the object has users. This field is set by the platform.
   * @return hasUsers
   */
  @javax.annotation.Nullable
  public Boolean getHasUsers() {
    return hasUsers;
  }

  public void setHasUsers(Boolean hasUsers) {
    this.hasUsers = hasUsers;
  }


  public OfferObject heroImage(Image heroImage) {
    this.heroImage = heroImage;
    return this;
  }

  /**
   * Get heroImage
   * @return heroImage
   */
  @javax.annotation.Nullable
  public Image getHeroImage() {
    return heroImage;
  }

  public void setHeroImage(Image heroImage) {
    this.heroImage = heroImage;
  }


  public OfferObject id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. The unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public OfferObject imageModulesData(List<ImageModuleData> imageModulesData) {
    this.imageModulesData = imageModulesData;
    return this;
  }

  public OfferObject addImageModulesDataItem(ImageModuleData imageModulesDataItem) {
    if (this.imageModulesData == null) {
      this.imageModulesData = new ArrayList<>();
    }
    this.imageModulesData.add(imageModulesDataItem);
    return this;
  }

  /**
   * Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level.
   * @return imageModulesData
   */
  @javax.annotation.Nullable
  public List<ImageModuleData> getImageModulesData() {
    return imageModulesData;
  }

  public void setImageModulesData(List<ImageModuleData> imageModulesData) {
    this.imageModulesData = imageModulesData;
  }


  public OfferObject infoModuleData(InfoModuleData infoModuleData) {
    this.infoModuleData = infoModuleData;
    return this;
  }

  /**
   * Get infoModuleData
   * @return infoModuleData
   */
  @javax.annotation.Nullable
  public InfoModuleData getInfoModuleData() {
    return infoModuleData;
  }

  public void setInfoModuleData(InfoModuleData infoModuleData) {
    this.infoModuleData = infoModuleData;
  }


  public OfferObject kind(String kind) {
    this.kind = kind;
    return this;
  }

  /**
   * Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#offerObject\&quot;&#x60;.
   * @return kind
   */
  @javax.annotation.Nullable
  public String getKind() {
    return kind;
  }

  public void setKind(String kind) {
    this.kind = kind;
  }


  public OfferObject linksModuleData(LinksModuleData linksModuleData) {
    this.linksModuleData = linksModuleData;
    return this;
  }

  /**
   * Get linksModuleData
   * @return linksModuleData
   */
  @javax.annotation.Nullable
  public LinksModuleData getLinksModuleData() {
    return linksModuleData;
  }

  public void setLinksModuleData(LinksModuleData linksModuleData) {
    this.linksModuleData = linksModuleData;
  }


  public OfferObject locations(List<LatLongPoint> locations) {
    this.locations = locations;
    return this;
  }

  public OfferObject addLocationsItem(LatLongPoint locationsItem) {
    if (this.locations == null) {
      this.locations = new ArrayList<>();
    }
    this.locations.add(locationsItem);
    return this;
  }

  /**
   * Note: This field is currently not supported to trigger geo notifications.
   * @return locations
   */
  @javax.annotation.Nullable
  public List<LatLongPoint> getLocations() {
    return locations;
  }

  public void setLocations(List<LatLongPoint> locations) {
    this.locations = locations;
  }


  public OfferObject messages(List<Message> messages) {
    this.messages = messages;
    return this;
  }

  public OfferObject addMessagesItem(Message messagesItem) {
    if (this.messages == null) {
      this.messages = new ArrayList<>();
    }
    this.messages.add(messagesItem);
    return this;
  }

  /**
   * An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10.
   * @return messages
   */
  @javax.annotation.Nullable
  public List<Message> getMessages() {
    return messages;
  }

  public void setMessages(List<Message> messages) {
    this.messages = messages;
  }


  public OfferObject passConstraints(PassConstraints passConstraints) {
    this.passConstraints = passConstraints;
    return this;
  }

  /**
   * Get passConstraints
   * @return passConstraints
   */
  @javax.annotation.Nullable
  public PassConstraints getPassConstraints() {
    return passConstraints;
  }

  public void setPassConstraints(PassConstraints passConstraints) {
    this.passConstraints = passConstraints;
  }


  public OfferObject rotatingBarcode(RotatingBarcode rotatingBarcode) {
    this.rotatingBarcode = rotatingBarcode;
    return this;
  }

  /**
   * Get rotatingBarcode
   * @return rotatingBarcode
   */
  @javax.annotation.Nullable
  public RotatingBarcode getRotatingBarcode() {
    return rotatingBarcode;
  }

  public void setRotatingBarcode(RotatingBarcode rotatingBarcode) {
    this.rotatingBarcode = rotatingBarcode;
  }


  public OfferObject smartTapRedemptionValue(String smartTapRedemptionValue) {
    this.smartTapRedemptionValue = smartTapRedemptionValue;
    return this;
  }

  /**
   * The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported.
   * @return smartTapRedemptionValue
   */
  @javax.annotation.Nullable
  public String getSmartTapRedemptionValue() {
    return smartTapRedemptionValue;
  }

  public void setSmartTapRedemptionValue(String smartTapRedemptionValue) {
    this.smartTapRedemptionValue = smartTapRedemptionValue;
  }


  public OfferObject state(StateEnum state) {
    this.state = state;
    return this;
  }

  /**
   * Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section.
   * @return state
   */
  @javax.annotation.Nullable
  public StateEnum getState() {
    return state;
  }

  public void setState(StateEnum state) {
    this.state = state;
  }


  public OfferObject textModulesData(List<TextModuleData> textModulesData) {
    this.textModulesData = textModulesData;
    return this;
  }

  public OfferObject addTextModulesDataItem(TextModuleData textModulesDataItem) {
    if (this.textModulesData == null) {
      this.textModulesData = new ArrayList<>();
    }
    this.textModulesData.add(textModulesDataItem);
    return this;
  }

  /**
   * Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class.
   * @return textModulesData
   */
  @javax.annotation.Nullable
  public List<TextModuleData> getTextModulesData() {
    return textModulesData;
  }

  public void setTextModulesData(List<TextModuleData> textModulesData) {
    this.textModulesData = textModulesData;
  }


  public OfferObject validTimeInterval(TimeInterval validTimeInterval) {
    this.validTimeInterval = validTimeInterval;
    return this;
  }

  /**
   * Get validTimeInterval
   * @return validTimeInterval
   */
  @javax.annotation.Nullable
  public TimeInterval getValidTimeInterval() {
    return validTimeInterval;
  }

  public void setValidTimeInterval(TimeInterval validTimeInterval) {
    this.validTimeInterval = validTimeInterval;
  }


  public OfferObject version(String version) {
    this.version = version;
    return this;
  }

  /**
   * Deprecated
   * @return version
   */
  @javax.annotation.Nullable
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OfferObject offerObject = (OfferObject) o;
    return Objects.equals(this.appLinkData, offerObject.appLinkData) &&
        Objects.equals(this.barcode, offerObject.barcode) &&
        Objects.equals(this.classId, offerObject.classId) &&
        Objects.equals(this.classReference, offerObject.classReference) &&
        Objects.equals(this.disableExpirationNotification, offerObject.disableExpirationNotification) &&
        Objects.equals(this.groupingInfo, offerObject.groupingInfo) &&
        Objects.equals(this.hasLinkedDevice, offerObject.hasLinkedDevice) &&
        Objects.equals(this.hasUsers, offerObject.hasUsers) &&
        Objects.equals(this.heroImage, offerObject.heroImage) &&
        Objects.equals(this.id, offerObject.id) &&
        Objects.equals(this.imageModulesData, offerObject.imageModulesData) &&
        Objects.equals(this.infoModuleData, offerObject.infoModuleData) &&
        Objects.equals(this.kind, offerObject.kind) &&
        Objects.equals(this.linksModuleData, offerObject.linksModuleData) &&
        Objects.equals(this.locations, offerObject.locations) &&
        Objects.equals(this.messages, offerObject.messages) &&
        Objects.equals(this.passConstraints, offerObject.passConstraints) &&
        Objects.equals(this.rotatingBarcode, offerObject.rotatingBarcode) &&
        Objects.equals(this.smartTapRedemptionValue, offerObject.smartTapRedemptionValue) &&
        Objects.equals(this.state, offerObject.state) &&
        Objects.equals(this.textModulesData, offerObject.textModulesData) &&
        Objects.equals(this.validTimeInterval, offerObject.validTimeInterval) &&
        Objects.equals(this.version, offerObject.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appLinkData, barcode, classId, classReference, disableExpirationNotification, groupingInfo, hasLinkedDevice, hasUsers, heroImage, id, imageModulesData, infoModuleData, kind, linksModuleData, locations, messages, passConstraints, rotatingBarcode, smartTapRedemptionValue, state, textModulesData, validTimeInterval, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OfferObject {\n");
    sb.append("    appLinkData: ").append(toIndentedString(appLinkData)).append("\n");
    sb.append("    barcode: ").append(toIndentedString(barcode)).append("\n");
    sb.append("    classId: ").append(toIndentedString(classId)).append("\n");
    sb.append("    classReference: ").append(toIndentedString(classReference)).append("\n");
    sb.append("    disableExpirationNotification: ").append(toIndentedString(disableExpirationNotification)).append("\n");
    sb.append("    groupingInfo: ").append(toIndentedString(groupingInfo)).append("\n");
    sb.append("    hasLinkedDevice: ").append(toIndentedString(hasLinkedDevice)).append("\n");
    sb.append("    hasUsers: ").append(toIndentedString(hasUsers)).append("\n");
    sb.append("    heroImage: ").append(toIndentedString(heroImage)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    imageModulesData: ").append(toIndentedString(imageModulesData)).append("\n");
    sb.append("    infoModuleData: ").append(toIndentedString(infoModuleData)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    linksModuleData: ").append(toIndentedString(linksModuleData)).append("\n");
    sb.append("    locations: ").append(toIndentedString(locations)).append("\n");
    sb.append("    messages: ").append(toIndentedString(messages)).append("\n");
    sb.append("    passConstraints: ").append(toIndentedString(passConstraints)).append("\n");
    sb.append("    rotatingBarcode: ").append(toIndentedString(rotatingBarcode)).append("\n");
    sb.append("    smartTapRedemptionValue: ").append(toIndentedString(smartTapRedemptionValue)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    textModulesData: ").append(toIndentedString(textModulesData)).append("\n");
    sb.append("    validTimeInterval: ").append(toIndentedString(validTimeInterval)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("appLinkData");
    openapiFields.add("barcode");
    openapiFields.add("classId");
    openapiFields.add("classReference");
    openapiFields.add("disableExpirationNotification");
    openapiFields.add("groupingInfo");
    openapiFields.add("hasLinkedDevice");
    openapiFields.add("hasUsers");
    openapiFields.add("heroImage");
    openapiFields.add("id");
    openapiFields.add("imageModulesData");
    openapiFields.add("infoModuleData");
    openapiFields.add("kind");
    openapiFields.add("linksModuleData");
    openapiFields.add("locations");
    openapiFields.add("messages");
    openapiFields.add("passConstraints");
    openapiFields.add("rotatingBarcode");
    openapiFields.add("smartTapRedemptionValue");
    openapiFields.add("state");
    openapiFields.add("textModulesData");
    openapiFields.add("validTimeInterval");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OfferObject
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OfferObject.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OfferObject is not found in the empty JSON string", OfferObject.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OfferObject.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OfferObject` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `appLinkData`
      if (jsonObj.get("appLinkData") != null && !jsonObj.get("appLinkData").isJsonNull()) {
        AppLinkData.validateJsonElement(jsonObj.get("appLinkData"));
      }
      // validate the optional field `barcode`
      if (jsonObj.get("barcode") != null && !jsonObj.get("barcode").isJsonNull()) {
        Barcode.validateJsonElement(jsonObj.get("barcode"));
      }
      if ((jsonObj.get("classId") != null && !jsonObj.get("classId").isJsonNull()) && !jsonObj.get("classId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `classId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("classId").toString()));
      }
      // validate the optional field `classReference`
      if (jsonObj.get("classReference") != null && !jsonObj.get("classReference").isJsonNull()) {
        OfferClass.validateJsonElement(jsonObj.get("classReference"));
      }
      // validate the optional field `groupingInfo`
      if (jsonObj.get("groupingInfo") != null && !jsonObj.get("groupingInfo").isJsonNull()) {
        GroupingInfo.validateJsonElement(jsonObj.get("groupingInfo"));
      }
      // validate the optional field `heroImage`
      if (jsonObj.get("heroImage") != null && !jsonObj.get("heroImage").isJsonNull()) {
        Image.validateJsonElement(jsonObj.get("heroImage"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("imageModulesData") != null && !jsonObj.get("imageModulesData").isJsonNull()) {
        JsonArray jsonArrayimageModulesData = jsonObj.getAsJsonArray("imageModulesData");
        if (jsonArrayimageModulesData != null) {
          // ensure the json data is an array
          if (!jsonObj.get("imageModulesData").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `imageModulesData` to be an array in the JSON string but got `%s`", jsonObj.get("imageModulesData").toString()));
          }

          // validate the optional field `imageModulesData` (array)
          for (int i = 0; i < jsonArrayimageModulesData.size(); i++) {
            ImageModuleData.validateJsonElement(jsonArrayimageModulesData.get(i));
          };
        }
      }
      // validate the optional field `infoModuleData`
      if (jsonObj.get("infoModuleData") != null && !jsonObj.get("infoModuleData").isJsonNull()) {
        InfoModuleData.validateJsonElement(jsonObj.get("infoModuleData"));
      }
      if ((jsonObj.get("kind") != null && !jsonObj.get("kind").isJsonNull()) && !jsonObj.get("kind").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `kind` to be a primitive type in the JSON string but got `%s`", jsonObj.get("kind").toString()));
      }
      // validate the optional field `linksModuleData`
      if (jsonObj.get("linksModuleData") != null && !jsonObj.get("linksModuleData").isJsonNull()) {
        LinksModuleData.validateJsonElement(jsonObj.get("linksModuleData"));
      }
      if (jsonObj.get("locations") != null && !jsonObj.get("locations").isJsonNull()) {
        JsonArray jsonArraylocations = jsonObj.getAsJsonArray("locations");
        if (jsonArraylocations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("locations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `locations` to be an array in the JSON string but got `%s`", jsonObj.get("locations").toString()));
          }

          // validate the optional field `locations` (array)
          for (int i = 0; i < jsonArraylocations.size(); i++) {
            LatLongPoint.validateJsonElement(jsonArraylocations.get(i));
          };
        }
      }
      if (jsonObj.get("messages") != null && !jsonObj.get("messages").isJsonNull()) {
        JsonArray jsonArraymessages = jsonObj.getAsJsonArray("messages");
        if (jsonArraymessages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("messages").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `messages` to be an array in the JSON string but got `%s`", jsonObj.get("messages").toString()));
          }

          // validate the optional field `messages` (array)
          for (int i = 0; i < jsonArraymessages.size(); i++) {
            Message.validateJsonElement(jsonArraymessages.get(i));
          };
        }
      }
      // validate the optional field `passConstraints`
      if (jsonObj.get("passConstraints") != null && !jsonObj.get("passConstraints").isJsonNull()) {
        PassConstraints.validateJsonElement(jsonObj.get("passConstraints"));
      }
      // validate the optional field `rotatingBarcode`
      if (jsonObj.get("rotatingBarcode") != null && !jsonObj.get("rotatingBarcode").isJsonNull()) {
        RotatingBarcode.validateJsonElement(jsonObj.get("rotatingBarcode"));
      }
      if ((jsonObj.get("smartTapRedemptionValue") != null && !jsonObj.get("smartTapRedemptionValue").isJsonNull()) && !jsonObj.get("smartTapRedemptionValue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `smartTapRedemptionValue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("smartTapRedemptionValue").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        StateEnum.validateJsonElement(jsonObj.get("state"));
      }
      if (jsonObj.get("textModulesData") != null && !jsonObj.get("textModulesData").isJsonNull()) {
        JsonArray jsonArraytextModulesData = jsonObj.getAsJsonArray("textModulesData");
        if (jsonArraytextModulesData != null) {
          // ensure the json data is an array
          if (!jsonObj.get("textModulesData").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `textModulesData` to be an array in the JSON string but got `%s`", jsonObj.get("textModulesData").toString()));
          }

          // validate the optional field `textModulesData` (array)
          for (int i = 0; i < jsonArraytextModulesData.size(); i++) {
            TextModuleData.validateJsonElement(jsonArraytextModulesData.get(i));
          };
        }
      }
      // validate the optional field `validTimeInterval`
      if (jsonObj.get("validTimeInterval") != null && !jsonObj.get("validTimeInterval").isJsonNull()) {
        TimeInterval.validateJsonElement(jsonObj.get("validTimeInterval"));
      }
      if ((jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OfferObject.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OfferObject' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OfferObject> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OfferObject.class));

       return (TypeAdapter<T>) new TypeAdapter<OfferObject>() {
           @Override
           public void write(JsonWriter out, OfferObject value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OfferObject read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OfferObject given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OfferObject
   * @throws IOException if the JSON string is invalid with respect to OfferObject
   */
  public static OfferObject fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OfferObject.class);
  }

  /**
   * Convert an instance of OfferObject to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

