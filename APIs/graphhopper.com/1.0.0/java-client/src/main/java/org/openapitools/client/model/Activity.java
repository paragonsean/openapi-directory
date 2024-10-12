/*
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ResponseAddress;

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
 * Activity
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Activity {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private ResponseAddress address;

  public static final String SERIALIZED_NAME_ARR_DATE_TIME = "arr_date_time";
  @SerializedName(SERIALIZED_NAME_ARR_DATE_TIME)
  private OffsetDateTime arrDateTime;

  public static final String SERIALIZED_NAME_ARR_TIME = "arr_time";
  @SerializedName(SERIALIZED_NAME_ARR_TIME)
  private Long arrTime;

  public static final String SERIALIZED_NAME_DISTANCE = "distance";
  @SerializedName(SERIALIZED_NAME_DISTANCE)
  private Long distance;

  public static final String SERIALIZED_NAME_DRIVING_TIME = "driving_time";
  @SerializedName(SERIALIZED_NAME_DRIVING_TIME)
  private Long drivingTime;

  public static final String SERIALIZED_NAME_END_DATE_TIME = "end_date_time";
  @SerializedName(SERIALIZED_NAME_END_DATE_TIME)
  private OffsetDateTime endDateTime;

  public static final String SERIALIZED_NAME_END_TIME = "end_time";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private Long endTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LOAD_AFTER = "load_after";
  @SerializedName(SERIALIZED_NAME_LOAD_AFTER)
  private List<Integer> loadAfter = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOAD_BEFORE = "load_before";
  @SerializedName(SERIALIZED_NAME_LOAD_BEFORE)
  private List<Integer> loadBefore = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOCATION_ID = "location_id";
  @SerializedName(SERIALIZED_NAME_LOCATION_ID)
  private String locationId;

  public static final String SERIALIZED_NAME_PREPARATION_TIME = "preparation_time";
  @SerializedName(SERIALIZED_NAME_PREPARATION_TIME)
  private Long preparationTime;

  /**
   * type of activity
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    START("start"),
    
    END("end"),
    
    SERVICE("service"),
    
    PICKUP_SHIPMENT("pickupShipment"),
    
    DELIVER_SHIPMENT("deliverShipment"),
    
    PICKUP("pickup"),
    
    DELIVERY("delivery"),
    
    BREAK("break");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_WAITING_TIME = "waiting_time";
  @SerializedName(SERIALIZED_NAME_WAITING_TIME)
  private Long waitingTime;

  public Activity() {
  }

  public Activity address(ResponseAddress address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public ResponseAddress getAddress() {
    return address;
  }

  public void setAddress(ResponseAddress address) {
    this.address = address;
  }


  public Activity arrDateTime(OffsetDateTime arrDateTime) {
    this.arrDateTime = arrDateTime;
    return this;
  }

  /**
   * Arrival date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is &#x60;null&#x60;.
   * @return arrDateTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getArrDateTime() {
    return arrDateTime;
  }

  public void setArrDateTime(OffsetDateTime arrDateTime) {
    this.arrDateTime = arrDateTime;
  }


  public Activity arrTime(Long arrTime) {
    this.arrTime = arrTime;
    return this;
  }

  /**
   * Arrival time at this activity in seconds. If type is &#x60;start&#x60;, this is not available (since it makes no sense to have &#x60;arr_time&#x60; at start). However, &#x60;end_time&#x60; is available and actually means \\\&quot;departure time\\\&quot; at start location. It is important to note that &#x60;arr_time&#x60; does not necessarily mean \\\&quot;start of underlying activity\\\&quot;, it solely means arrival time at activity location. If this activity has no time windows and if there are no further preparation times, &#x60;arr_time&#x60; is equal to activity start time.
   * @return arrTime
   */
  @javax.annotation.Nullable
  public Long getArrTime() {
    return arrTime;
  }

  public void setArrTime(Long arrTime) {
    this.arrTime = arrTime;
  }


  public Activity distance(Long distance) {
    this.distance = distance;
    return this;
  }

  /**
   * cumulated distance from start to this activity in m
   * @return distance
   */
  @javax.annotation.Nullable
  public Long getDistance() {
    return distance;
  }

  public void setDistance(Long distance) {
    this.distance = distance;
  }


  public Activity drivingTime(Long drivingTime) {
    this.drivingTime = drivingTime;
    return this;
  }

  /**
   * cumulated driving time from start to this driver activity in seconds
   * @return drivingTime
   */
  @javax.annotation.Nullable
  public Long getDrivingTime() {
    return drivingTime;
  }

  public void setDrivingTime(Long drivingTime) {
    this.drivingTime = drivingTime;
  }


  public Activity endDateTime(OffsetDateTime endDateTime) {
    this.endDateTime = endDateTime;
    return this;
  }

  /**
   * End date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is &#x60;null&#x60;.
   * @return endDateTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndDateTime() {
    return endDateTime;
  }

  public void setEndDateTime(OffsetDateTime endDateTime) {
    this.endDateTime = endDateTime;
  }


  public Activity endTime(Long endTime) {
    this.endTime = endTime;
    return this;
  }

  /**
   * End time of and thus departure time at this activity. If type is &#x60;end&#x60;, this is not available (since it makes no sense to have an &#x60;end_time&#x60; at end) &#x60;end_time&#x60; at each activity is equal to the departure time at the activity location.
   * @return endTime
   */
  @javax.annotation.Nullable
  public Long getEndTime() {
    return endTime;
  }

  public void setEndTime(Long endTime) {
    this.endTime = endTime;
  }


  public Activity id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Id referring to the underlying service or shipment, i.e. the shipment or service this activity belongs to
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Activity loadAfter(List<Integer> loadAfter) {
    this.loadAfter = loadAfter;
    return this;
  }

  public Activity addLoadAfterItem(Integer loadAfterItem) {
    if (this.loadAfter == null) {
      this.loadAfter = new ArrayList<>();
    }
    this.loadAfter.add(loadAfterItem);
    return this;
  }

  /**
   * Array with size/capacity dimensions after this activity
   * @return loadAfter
   */
  @javax.annotation.Nullable
  public List<Integer> getLoadAfter() {
    return loadAfter;
  }

  public void setLoadAfter(List<Integer> loadAfter) {
    this.loadAfter = loadAfter;
  }


  public Activity loadBefore(List<Integer> loadBefore) {
    this.loadBefore = loadBefore;
    return this;
  }

  public Activity addLoadBeforeItem(Integer loadBeforeItem) {
    if (this.loadBefore == null) {
      this.loadBefore = new ArrayList<>();
    }
    this.loadBefore.add(loadBeforeItem);
    return this;
  }

  /**
   * Array with size/capacity dimensions before this activity
   * @return loadBefore
   */
  @javax.annotation.Nullable
  public List<Integer> getLoadBefore() {
    return loadBefore;
  }

  public void setLoadBefore(List<Integer> loadBefore) {
    this.loadBefore = loadBefore;
  }


  public Activity locationId(String locationId) {
    this.locationId = locationId;
    return this;
  }

  /**
   * Id that refers to address
   * @return locationId
   */
  @javax.annotation.Nullable
  public String getLocationId() {
    return locationId;
  }

  public void setLocationId(String locationId) {
    this.locationId = locationId;
  }


  public Activity preparationTime(Long preparationTime) {
    this.preparationTime = preparationTime;
    return this;
  }

  /**
   * preparation time at this activity in seconds
   * @return preparationTime
   */
  @javax.annotation.Nullable
  public Long getPreparationTime() {
    return preparationTime;
  }

  public void setPreparationTime(Long preparationTime) {
    this.preparationTime = preparationTime;
  }


  public Activity type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * type of activity
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public Activity waitingTime(Long waitingTime) {
    this.waitingTime = waitingTime;
    return this;
  }

  /**
   * Waiting time at this activity in seconds. A waiting time can occur if the activity has at least one time window. If &#x60;arr_time&#x60; &lt; &#x60;time_window.earliest&#x60; a waiting time of &#x60;time_window_earliest&#x60; - &#x60;arr_time&#x60; occurs.
   * @return waitingTime
   */
  @javax.annotation.Nullable
  public Long getWaitingTime() {
    return waitingTime;
  }

  public void setWaitingTime(Long waitingTime) {
    this.waitingTime = waitingTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Activity activity = (Activity) o;
    return Objects.equals(this.address, activity.address) &&
        Objects.equals(this.arrDateTime, activity.arrDateTime) &&
        Objects.equals(this.arrTime, activity.arrTime) &&
        Objects.equals(this.distance, activity.distance) &&
        Objects.equals(this.drivingTime, activity.drivingTime) &&
        Objects.equals(this.endDateTime, activity.endDateTime) &&
        Objects.equals(this.endTime, activity.endTime) &&
        Objects.equals(this.id, activity.id) &&
        Objects.equals(this.loadAfter, activity.loadAfter) &&
        Objects.equals(this.loadBefore, activity.loadBefore) &&
        Objects.equals(this.locationId, activity.locationId) &&
        Objects.equals(this.preparationTime, activity.preparationTime) &&
        Objects.equals(this.type, activity.type) &&
        Objects.equals(this.waitingTime, activity.waitingTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, arrDateTime, arrTime, distance, drivingTime, endDateTime, endTime, id, loadAfter, loadBefore, locationId, preparationTime, type, waitingTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Activity {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    arrDateTime: ").append(toIndentedString(arrDateTime)).append("\n");
    sb.append("    arrTime: ").append(toIndentedString(arrTime)).append("\n");
    sb.append("    distance: ").append(toIndentedString(distance)).append("\n");
    sb.append("    drivingTime: ").append(toIndentedString(drivingTime)).append("\n");
    sb.append("    endDateTime: ").append(toIndentedString(endDateTime)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    loadAfter: ").append(toIndentedString(loadAfter)).append("\n");
    sb.append("    loadBefore: ").append(toIndentedString(loadBefore)).append("\n");
    sb.append("    locationId: ").append(toIndentedString(locationId)).append("\n");
    sb.append("    preparationTime: ").append(toIndentedString(preparationTime)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    waitingTime: ").append(toIndentedString(waitingTime)).append("\n");
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
    openapiFields.add("arr_date_time");
    openapiFields.add("arr_time");
    openapiFields.add("distance");
    openapiFields.add("driving_time");
    openapiFields.add("end_date_time");
    openapiFields.add("end_time");
    openapiFields.add("id");
    openapiFields.add("load_after");
    openapiFields.add("load_before");
    openapiFields.add("location_id");
    openapiFields.add("preparation_time");
    openapiFields.add("type");
    openapiFields.add("waiting_time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Activity
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Activity.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Activity is not found in the empty JSON string", Activity.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Activity.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Activity` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `address`
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) {
        ResponseAddress.validateJsonElement(jsonObj.get("address"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("load_after") != null && !jsonObj.get("load_after").isJsonNull() && !jsonObj.get("load_after").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `load_after` to be an array in the JSON string but got `%s`", jsonObj.get("load_after").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("load_before") != null && !jsonObj.get("load_before").isJsonNull() && !jsonObj.get("load_before").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `load_before` to be an array in the JSON string but got `%s`", jsonObj.get("load_before").toString()));
      }
      if ((jsonObj.get("location_id") != null && !jsonObj.get("location_id").isJsonNull()) && !jsonObj.get("location_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location_id").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Activity.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Activity' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Activity> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Activity.class));

       return (TypeAdapter<T>) new TypeAdapter<Activity>() {
           @Override
           public void write(JsonWriter out, Activity value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Activity read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Activity given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Activity
   * @throws IOException if the JSON string is invalid with respect to Activity
   */
  public static Activity fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Activity.class);
  }

  /**
   * Convert an instance of Activity to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

