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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Address;
import org.openapitools.client.model.VehicleBreak;

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
 * Vehicle
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Vehicle {
  public static final String SERIALIZED_NAME_BREAK = "break";
  @SerializedName(SERIALIZED_NAME_BREAK)
  private VehicleBreak _break;

  public static final String SERIALIZED_NAME_EARLIEST_START = "earliest_start";
  @SerializedName(SERIALIZED_NAME_EARLIEST_START)
  private Long earliestStart = 0l;

  public static final String SERIALIZED_NAME_END_ADDRESS = "end_address";
  @SerializedName(SERIALIZED_NAME_END_ADDRESS)
  private Address endAddress;

  public static final String SERIALIZED_NAME_LATEST_END = "latest_end";
  @SerializedName(SERIALIZED_NAME_LATEST_END)
  private Long latestEnd;

  public static final String SERIALIZED_NAME_MAX_ACTIVITIES = "max_activities";
  @SerializedName(SERIALIZED_NAME_MAX_ACTIVITIES)
  private Integer maxActivities;

  public static final String SERIALIZED_NAME_MAX_DISTANCE = "max_distance";
  @SerializedName(SERIALIZED_NAME_MAX_DISTANCE)
  private Long maxDistance;

  public static final String SERIALIZED_NAME_MAX_DRIVING_TIME = "max_driving_time";
  @SerializedName(SERIALIZED_NAME_MAX_DRIVING_TIME)
  private Long maxDrivingTime;

  public static final String SERIALIZED_NAME_MAX_JOBS = "max_jobs";
  @SerializedName(SERIALIZED_NAME_MAX_JOBS)
  private Integer maxJobs;

  public static final String SERIALIZED_NAME_MIN_JOBS = "min_jobs";
  @SerializedName(SERIALIZED_NAME_MIN_JOBS)
  private Integer minJobs;

  public static final String SERIALIZED_NAME_MOVE_TO_END_ADDRESS = "move_to_end_address";
  @SerializedName(SERIALIZED_NAME_MOVE_TO_END_ADDRESS)
  private Boolean moveToEndAddress;

  public static final String SERIALIZED_NAME_RETURN_TO_DEPOT = "return_to_depot";
  @SerializedName(SERIALIZED_NAME_RETURN_TO_DEPOT)
  private Boolean returnToDepot = true;

  public static final String SERIALIZED_NAME_SKILLS = "skills";
  @SerializedName(SERIALIZED_NAME_SKILLS)
  private List<String> skills = new ArrayList<>();

  public static final String SERIALIZED_NAME_START_ADDRESS = "start_address";
  @SerializedName(SERIALIZED_NAME_START_ADDRESS)
  private Address startAddress;

  public static final String SERIALIZED_NAME_TYPE_ID = "type_id";
  @SerializedName(SERIALIZED_NAME_TYPE_ID)
  private String typeId = "default-type";

  public static final String SERIALIZED_NAME_VEHICLE_ID = "vehicle_id";
  @SerializedName(SERIALIZED_NAME_VEHICLE_ID)
  private String vehicleId;

  public Vehicle() {
  }

  public Vehicle _break(VehicleBreak _break) {
    this._break = _break;
    return this;
  }

  /**
   * Get _break
   * @return _break
   */
  @javax.annotation.Nullable
  public VehicleBreak getBreak() {
    return _break;
  }

  public void setBreak(VehicleBreak _break) {
    this._break = _break;
  }


  public Vehicle earliestStart(Long earliestStart) {
    this.earliestStart = earliestStart;
    return this;
  }

  /**
   * Earliest start of vehicle in seconds. It is recommended to use the unix timestamp.
   * @return earliestStart
   */
  @javax.annotation.Nullable
  public Long getEarliestStart() {
    return earliestStart;
  }

  public void setEarliestStart(Long earliestStart) {
    this.earliestStart = earliestStart;
  }


  public Vehicle endAddress(Address endAddress) {
    this.endAddress = endAddress;
    return this;
  }

  /**
   * Get endAddress
   * @return endAddress
   */
  @javax.annotation.Nullable
  public Address getEndAddress() {
    return endAddress;
  }

  public void setEndAddress(Address endAddress) {
    this.endAddress = endAddress;
  }


  public Vehicle latestEnd(Long latestEnd) {
    this.latestEnd = latestEnd;
    return this;
  }

  /**
   * Latest end of vehicle in seconds, i.e. the time the vehicle needs to be at its end location at latest.
   * @return latestEnd
   */
  @javax.annotation.Nullable
  public Long getLatestEnd() {
    return latestEnd;
  }

  public void setLatestEnd(Long latestEnd) {
    this.latestEnd = latestEnd;
  }


  public Vehicle maxActivities(Integer maxActivities) {
    this.maxActivities = maxActivities;
    return this;
  }

  /**
   * Specifies the maximum number of activities a vehicle can conduct.
   * @return maxActivities
   */
  @javax.annotation.Nullable
  public Integer getMaxActivities() {
    return maxActivities;
  }

  public void setMaxActivities(Integer maxActivities) {
    this.maxActivities = maxActivities;
  }


  public Vehicle maxDistance(Long maxDistance) {
    this.maxDistance = maxDistance;
    return this;
  }

  /**
   * Specifies the maximum distance (in meters) a vehicle can go.
   * @return maxDistance
   */
  @javax.annotation.Nullable
  public Long getMaxDistance() {
    return maxDistance;
  }

  public void setMaxDistance(Long maxDistance) {
    this.maxDistance = maxDistance;
  }


  public Vehicle maxDrivingTime(Long maxDrivingTime) {
    this.maxDrivingTime = maxDrivingTime;
    return this;
  }

  /**
   * Specifies the maximum drive time (in seconds) a vehicle/driver can go, i.e. the maximum time on the road (service and waiting times are not included here)
   * @return maxDrivingTime
   */
  @javax.annotation.Nullable
  public Long getMaxDrivingTime() {
    return maxDrivingTime;
  }

  public void setMaxDrivingTime(Long maxDrivingTime) {
    this.maxDrivingTime = maxDrivingTime;
  }


  public Vehicle maxJobs(Integer maxJobs) {
    this.maxJobs = maxJobs;
    return this;
  }

  /**
   * Specifies the maximum number of jobs a vehicle can load.
   * @return maxJobs
   */
  @javax.annotation.Nullable
  public Integer getMaxJobs() {
    return maxJobs;
  }

  public void setMaxJobs(Integer maxJobs) {
    this.maxJobs = maxJobs;
  }


  public Vehicle minJobs(Integer minJobs) {
    this.minJobs = minJobs;
    return this;
  }

  /**
   * Specifies the minimum number of jobs a vehicle should load. This is a soft constraint, i.e. if it is not possible to fulfill “min_jobs”, we will still try to get as close as possible to this constraint.
   * @return minJobs
   */
  @javax.annotation.Nullable
  public Integer getMinJobs() {
    return minJobs;
  }

  public void setMinJobs(Integer minJobs) {
    this.minJobs = minJobs;
  }


  public Vehicle moveToEndAddress(Boolean moveToEndAddress) {
    this.moveToEndAddress = moveToEndAddress;
    return this;
  }

  /**
   * Indicates whether a vehicle should be moved even though it has not been assigned any jobs.
   * @return moveToEndAddress
   */
  @javax.annotation.Nullable
  public Boolean getMoveToEndAddress() {
    return moveToEndAddress;
  }

  public void setMoveToEndAddress(Boolean moveToEndAddress) {
    this.moveToEndAddress = moveToEndAddress;
  }


  public Vehicle returnToDepot(Boolean returnToDepot) {
    this.returnToDepot = returnToDepot;
    return this;
  }

  /**
   * If it is false, the algorithm decides where to end the vehicle route. It ends in one of your customers&#39; locations. The end is chosen such that it contributes to the overall objective function, e.g. min transport_time. If it is true, you can either specify a specific end location (which is then regarded as end depot) or you can leave it and the driver returns to its start location.
   * @return returnToDepot
   */
  @javax.annotation.Nullable
  public Boolean getReturnToDepot() {
    return returnToDepot;
  }

  public void setReturnToDepot(Boolean returnToDepot) {
    this.returnToDepot = returnToDepot;
  }


  public Vehicle skills(List<String> skills) {
    this.skills = skills;
    return this;
  }

  public Vehicle addSkillsItem(String skillsItem) {
    if (this.skills == null) {
      this.skills = new ArrayList<>();
    }
    this.skills.add(skillsItem);
    return this;
  }

  /**
   * Array of skills, i.e. array of string (not case sensitive).
   * @return skills
   */
  @javax.annotation.Nullable
  public List<String> getSkills() {
    return skills;
  }

  public void setSkills(List<String> skills) {
    this.skills = skills;
  }


  public Vehicle startAddress(Address startAddress) {
    this.startAddress = startAddress;
    return this;
  }

  /**
   * Get startAddress
   * @return startAddress
   */
  @javax.annotation.Nonnull
  public Address getStartAddress() {
    return startAddress;
  }

  public void setStartAddress(Address startAddress) {
    this.startAddress = startAddress;
  }


  public Vehicle typeId(String typeId) {
    this.typeId = typeId;
    return this;
  }

  /**
   * The type ID assigns a vehicle type to this vehicle. You can specify types in the array of vehicle types. If you omit the type ID, the default type is used. The default type is a &#x60;car&#x60; with a capacity of 0.
   * @return typeId
   */
  @javax.annotation.Nullable
  public String getTypeId() {
    return typeId;
  }

  public void setTypeId(String typeId) {
    this.typeId = typeId;
  }


  public Vehicle vehicleId(String vehicleId) {
    this.vehicleId = vehicleId;
    return this;
  }

  /**
   * Specifies the ID of the vehicle. Ids must be unique, i.e. if there are two vehicles with the same ID, an error is returned.
   * @return vehicleId
   */
  @javax.annotation.Nonnull
  public String getVehicleId() {
    return vehicleId;
  }

  public void setVehicleId(String vehicleId) {
    this.vehicleId = vehicleId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Vehicle vehicle = (Vehicle) o;
    return Objects.equals(this._break, vehicle._break) &&
        Objects.equals(this.earliestStart, vehicle.earliestStart) &&
        Objects.equals(this.endAddress, vehicle.endAddress) &&
        Objects.equals(this.latestEnd, vehicle.latestEnd) &&
        Objects.equals(this.maxActivities, vehicle.maxActivities) &&
        Objects.equals(this.maxDistance, vehicle.maxDistance) &&
        Objects.equals(this.maxDrivingTime, vehicle.maxDrivingTime) &&
        Objects.equals(this.maxJobs, vehicle.maxJobs) &&
        Objects.equals(this.minJobs, vehicle.minJobs) &&
        Objects.equals(this.moveToEndAddress, vehicle.moveToEndAddress) &&
        Objects.equals(this.returnToDepot, vehicle.returnToDepot) &&
        Objects.equals(this.skills, vehicle.skills) &&
        Objects.equals(this.startAddress, vehicle.startAddress) &&
        Objects.equals(this.typeId, vehicle.typeId) &&
        Objects.equals(this.vehicleId, vehicle.vehicleId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(_break, earliestStart, endAddress, latestEnd, maxActivities, maxDistance, maxDrivingTime, maxJobs, minJobs, moveToEndAddress, returnToDepot, skills, startAddress, typeId, vehicleId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Vehicle {\n");
    sb.append("    _break: ").append(toIndentedString(_break)).append("\n");
    sb.append("    earliestStart: ").append(toIndentedString(earliestStart)).append("\n");
    sb.append("    endAddress: ").append(toIndentedString(endAddress)).append("\n");
    sb.append("    latestEnd: ").append(toIndentedString(latestEnd)).append("\n");
    sb.append("    maxActivities: ").append(toIndentedString(maxActivities)).append("\n");
    sb.append("    maxDistance: ").append(toIndentedString(maxDistance)).append("\n");
    sb.append("    maxDrivingTime: ").append(toIndentedString(maxDrivingTime)).append("\n");
    sb.append("    maxJobs: ").append(toIndentedString(maxJobs)).append("\n");
    sb.append("    minJobs: ").append(toIndentedString(minJobs)).append("\n");
    sb.append("    moveToEndAddress: ").append(toIndentedString(moveToEndAddress)).append("\n");
    sb.append("    returnToDepot: ").append(toIndentedString(returnToDepot)).append("\n");
    sb.append("    skills: ").append(toIndentedString(skills)).append("\n");
    sb.append("    startAddress: ").append(toIndentedString(startAddress)).append("\n");
    sb.append("    typeId: ").append(toIndentedString(typeId)).append("\n");
    sb.append("    vehicleId: ").append(toIndentedString(vehicleId)).append("\n");
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
    openapiFields.add("break");
    openapiFields.add("earliest_start");
    openapiFields.add("end_address");
    openapiFields.add("latest_end");
    openapiFields.add("max_activities");
    openapiFields.add("max_distance");
    openapiFields.add("max_driving_time");
    openapiFields.add("max_jobs");
    openapiFields.add("min_jobs");
    openapiFields.add("move_to_end_address");
    openapiFields.add("return_to_depot");
    openapiFields.add("skills");
    openapiFields.add("start_address");
    openapiFields.add("type_id");
    openapiFields.add("vehicle_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("start_address");
    openapiRequiredFields.add("vehicle_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Vehicle
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Vehicle.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Vehicle is not found in the empty JSON string", Vehicle.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Vehicle.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Vehicle` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Vehicle.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `break`
      if (jsonObj.get("break") != null && !jsonObj.get("break").isJsonNull()) {
        VehicleBreak.validateJsonElement(jsonObj.get("break"));
      }
      // validate the optional field `end_address`
      if (jsonObj.get("end_address") != null && !jsonObj.get("end_address").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("end_address"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("skills") != null && !jsonObj.get("skills").isJsonNull() && !jsonObj.get("skills").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `skills` to be an array in the JSON string but got `%s`", jsonObj.get("skills").toString()));
      }
      // validate the required field `start_address`
      Address.validateJsonElement(jsonObj.get("start_address"));
      if ((jsonObj.get("type_id") != null && !jsonObj.get("type_id").isJsonNull()) && !jsonObj.get("type_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type_id").toString()));
      }
      if (!jsonObj.get("vehicle_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vehicle_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vehicle_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Vehicle.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Vehicle' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Vehicle> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Vehicle.class));

       return (TypeAdapter<T>) new TypeAdapter<Vehicle>() {
           @Override
           public void write(JsonWriter out, Vehicle value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Vehicle read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Vehicle given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Vehicle
   * @throws IOException if the JSON string is invalid with respect to Vehicle
   */
  public static Vehicle fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Vehicle.class);
  }

  /**
   * Convert an instance of Vehicle to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

