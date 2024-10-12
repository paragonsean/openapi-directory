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
import org.openapitools.client.model.Stop;

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
 * Shipment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Shipment {
  public static final String SERIALIZED_NAME_ALLOWED_VEHICLES = "allowed_vehicles";
  @SerializedName(SERIALIZED_NAME_ALLOWED_VEHICLES)
  private List<String> allowedVehicles = new ArrayList<>();

  public static final String SERIALIZED_NAME_DELIVERY = "delivery";
  @SerializedName(SERIALIZED_NAME_DELIVERY)
  private Stop delivery;

  public static final String SERIALIZED_NAME_DISALLOWED_VEHICLES = "disallowed_vehicles";
  @SerializedName(SERIALIZED_NAME_DISALLOWED_VEHICLES)
  private List<String> disallowedVehicles = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MAX_TIME_IN_VEHICLE = "max_time_in_vehicle";
  @SerializedName(SERIALIZED_NAME_MAX_TIME_IN_VEHICLE)
  private Long maxTimeInVehicle;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PICKUP = "pickup";
  @SerializedName(SERIALIZED_NAME_PICKUP)
  private Stop pickup;

  public static final String SERIALIZED_NAME_PRIORITY = "priority";
  @SerializedName(SERIALIZED_NAME_PRIORITY)
  private Integer priority = 2;

  public static final String SERIALIZED_NAME_REQUIRED_SKILLS = "required_skills";
  @SerializedName(SERIALIZED_NAME_REQUIRED_SKILLS)
  private List<String> requiredSkills = new ArrayList<>();

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private List<Integer> size = new ArrayList<>(Arrays.asList(0));

  public Shipment() {
  }

  public Shipment allowedVehicles(List<String> allowedVehicles) {
    this.allowedVehicles = allowedVehicles;
    return this;
  }

  public Shipment addAllowedVehiclesItem(String allowedVehiclesItem) {
    if (this.allowedVehicles == null) {
      this.allowedVehicles = new ArrayList<>();
    }
    this.allowedVehicles.add(allowedVehiclesItem);
    return this;
  }

  /**
   * Specifies an array of allowed vehicles, i.e. array of vehicle ids. For example, if this shipment can only be conducted EITHER by \&quot;technician_peter\&quot; OR \&quot;technician_stefan\&quot; specify this as follows: [\&quot;technician_peter\&quot;,\&quot;technician_stefan\&quot;].
   * @return allowedVehicles
   */
  @javax.annotation.Nullable
  public List<String> getAllowedVehicles() {
    return allowedVehicles;
  }

  public void setAllowedVehicles(List<String> allowedVehicles) {
    this.allowedVehicles = allowedVehicles;
  }


  public Shipment delivery(Stop delivery) {
    this.delivery = delivery;
    return this;
  }

  /**
   * Get delivery
   * @return delivery
   */
  @javax.annotation.Nonnull
  public Stop getDelivery() {
    return delivery;
  }

  public void setDelivery(Stop delivery) {
    this.delivery = delivery;
  }


  public Shipment disallowedVehicles(List<String> disallowedVehicles) {
    this.disallowedVehicles = disallowedVehicles;
    return this;
  }

  public Shipment addDisallowedVehiclesItem(String disallowedVehiclesItem) {
    if (this.disallowedVehicles == null) {
      this.disallowedVehicles = new ArrayList<>();
    }
    this.disallowedVehicles.add(disallowedVehiclesItem);
    return this;
  }

  /**
   * Specifies an array of disallowed vehicles, i.e. array of vehicle ids.
   * @return disallowedVehicles
   */
  @javax.annotation.Nullable
  public List<String> getDisallowedVehicles() {
    return disallowedVehicles;
  }

  public void setDisallowedVehicles(List<String> disallowedVehicles) {
    this.disallowedVehicles = disallowedVehicles;
  }


  public Shipment id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Specifies the id of the shipment. Ids need to be unique so there must not be two services/shipments with the same id.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Shipment maxTimeInVehicle(Long maxTimeInVehicle) {
    this.maxTimeInVehicle = maxTimeInVehicle;
    return this;
  }

  /**
   * Specifies the maximum time in seconds a shipment can stay in the vehicle.
   * @return maxTimeInVehicle
   */
  @javax.annotation.Nullable
  public Long getMaxTimeInVehicle() {
    return maxTimeInVehicle;
  }

  public void setMaxTimeInVehicle(Long maxTimeInVehicle) {
    this.maxTimeInVehicle = maxTimeInVehicle;
  }


  public Shipment name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Meaningful name for shipment, e.g. \&quot;pickup and deliver pizza to Peter\&quot;.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Shipment pickup(Stop pickup) {
    this.pickup = pickup;
    return this;
  }

  /**
   * Get pickup
   * @return pickup
   */
  @javax.annotation.Nonnull
  public Stop getPickup() {
    return pickup;
  }

  public void setPickup(Stop pickup) {
    this.pickup = pickup;
  }


  public Shipment priority(Integer priority) {
    this.priority = priority;
    return this;
  }

  /**
   * Specifies the priority. Can be 1 &#x3D; high priority to 10 &#x3D; low priority. Often there are more services/shipments than the available vehicle fleet can handle. Then you can set priorities to differentiate high priority tasks from those that could be left unassigned. I.e. the lower the priority the earlier these tasks are omitted in the solution.
   * @return priority
   */
  @javax.annotation.Nullable
  public Integer getPriority() {
    return priority;
  }

  public void setPriority(Integer priority) {
    this.priority = priority;
  }


  public Shipment requiredSkills(List<String> requiredSkills) {
    this.requiredSkills = requiredSkills;
    return this;
  }

  public Shipment addRequiredSkillsItem(String requiredSkillsItem) {
    if (this.requiredSkills == null) {
      this.requiredSkills = new ArrayList<>();
    }
    this.requiredSkills.add(requiredSkillsItem);
    return this;
  }

  /**
   * Specifies an array of required skills, i.e. array of string (not case sensitive). For example, if this shipment needs to be conducted by a technician having a &#x60;drilling_machine&#x60; and a &#x60;screw_driver&#x60; then specify the array as follows: &#x60;[\&quot;drilling_machine\&quot;,\&quot;screw_driver\&quot;]&#x60;. This means that the service can only be done by a vehicle (technician) that has the skills &#x60;drilling_machine&#x60; AND &#x60;screw_driver&#x60; in its skill array. Otherwise it remains unassigned.
   * @return requiredSkills
   */
  @javax.annotation.Nullable
  public List<String> getRequiredSkills() {
    return requiredSkills;
  }

  public void setRequiredSkills(List<String> requiredSkills) {
    this.requiredSkills = requiredSkills;
  }


  public Shipment size(List<Integer> size) {
    this.size = size;
    return this;
  }

  public Shipment addSizeItem(Integer sizeItem) {
    if (this.size == null) {
      this.size = new ArrayList<>(Arrays.asList(0));
    }
    this.size.add(sizeItem);
    return this;
  }

  /**
   * Size can have multiple dimensions and should be in line with the capacity dimension array of the vehicle type. For example, if the item that needs to be delivered has two size dimension, volume and weight, then specify it as follow [ 20, 5 ] assuming a volume of 20 and a weight of 5.
   * @return size
   */
  @javax.annotation.Nullable
  public List<Integer> getSize() {
    return size;
  }

  public void setSize(List<Integer> size) {
    this.size = size;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Shipment shipment = (Shipment) o;
    return Objects.equals(this.allowedVehicles, shipment.allowedVehicles) &&
        Objects.equals(this.delivery, shipment.delivery) &&
        Objects.equals(this.disallowedVehicles, shipment.disallowedVehicles) &&
        Objects.equals(this.id, shipment.id) &&
        Objects.equals(this.maxTimeInVehicle, shipment.maxTimeInVehicle) &&
        Objects.equals(this.name, shipment.name) &&
        Objects.equals(this.pickup, shipment.pickup) &&
        Objects.equals(this.priority, shipment.priority) &&
        Objects.equals(this.requiredSkills, shipment.requiredSkills) &&
        Objects.equals(this.size, shipment.size);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowedVehicles, delivery, disallowedVehicles, id, maxTimeInVehicle, name, pickup, priority, requiredSkills, size);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Shipment {\n");
    sb.append("    allowedVehicles: ").append(toIndentedString(allowedVehicles)).append("\n");
    sb.append("    delivery: ").append(toIndentedString(delivery)).append("\n");
    sb.append("    disallowedVehicles: ").append(toIndentedString(disallowedVehicles)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    maxTimeInVehicle: ").append(toIndentedString(maxTimeInVehicle)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    pickup: ").append(toIndentedString(pickup)).append("\n");
    sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
    sb.append("    requiredSkills: ").append(toIndentedString(requiredSkills)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
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
    openapiFields.add("allowed_vehicles");
    openapiFields.add("delivery");
    openapiFields.add("disallowed_vehicles");
    openapiFields.add("id");
    openapiFields.add("max_time_in_vehicle");
    openapiFields.add("name");
    openapiFields.add("pickup");
    openapiFields.add("priority");
    openapiFields.add("required_skills");
    openapiFields.add("size");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("delivery");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("pickup");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Shipment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Shipment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Shipment is not found in the empty JSON string", Shipment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Shipment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Shipment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Shipment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("allowed_vehicles") != null && !jsonObj.get("allowed_vehicles").isJsonNull() && !jsonObj.get("allowed_vehicles").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `allowed_vehicles` to be an array in the JSON string but got `%s`", jsonObj.get("allowed_vehicles").toString()));
      }
      // validate the required field `delivery`
      Stop.validateJsonElement(jsonObj.get("delivery"));
      // ensure the optional json data is an array if present
      if (jsonObj.get("disallowed_vehicles") != null && !jsonObj.get("disallowed_vehicles").isJsonNull() && !jsonObj.get("disallowed_vehicles").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `disallowed_vehicles` to be an array in the JSON string but got `%s`", jsonObj.get("disallowed_vehicles").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the required field `pickup`
      Stop.validateJsonElement(jsonObj.get("pickup"));
      // ensure the optional json data is an array if present
      if (jsonObj.get("required_skills") != null && !jsonObj.get("required_skills").isJsonNull() && !jsonObj.get("required_skills").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `required_skills` to be an array in the JSON string but got `%s`", jsonObj.get("required_skills").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("size") != null && !jsonObj.get("size").isJsonNull() && !jsonObj.get("size").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `size` to be an array in the JSON string but got `%s`", jsonObj.get("size").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Shipment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Shipment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Shipment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Shipment.class));

       return (TypeAdapter<T>) new TypeAdapter<Shipment>() {
           @Override
           public void write(JsonWriter out, Shipment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Shipment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Shipment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Shipment
   * @throws IOException if the JSON string is invalid with respect to Shipment
   */
  public static Shipment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Shipment.class);
  }

  /**
   * Convert an instance of Shipment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

