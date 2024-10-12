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
import org.openapitools.client.model.Algorithm;
import org.openapitools.client.model.CostMatrix;
import org.openapitools.client.model.ModelConfiguration;
import org.openapitools.client.model.Objective;
import org.openapitools.client.model.RequestRelationsInner;
import org.openapitools.client.model.Service;
import org.openapitools.client.model.Shipment;
import org.openapitools.client.model.Vehicle;
import org.openapitools.client.model.VehicleType;

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
 * Request
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Request {
  public static final String SERIALIZED_NAME_ALGORITHM = "algorithm";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_ALGORITHM)
  private Algorithm algorithm;

  public static final String SERIALIZED_NAME_CONFIGURATION = "configuration";
  @SerializedName(SERIALIZED_NAME_CONFIGURATION)
  private ModelConfiguration _configuration;

  public static final String SERIALIZED_NAME_COST_MATRICES = "cost_matrices";
  @SerializedName(SERIALIZED_NAME_COST_MATRICES)
  private List<CostMatrix> costMatrices = new ArrayList<>();

  public static final String SERIALIZED_NAME_OBJECTIVES = "objectives";
  @SerializedName(SERIALIZED_NAME_OBJECTIVES)
  private List<Objective> objectives = new ArrayList<>();

  public static final String SERIALIZED_NAME_RELATIONS = "relations";
  @SerializedName(SERIALIZED_NAME_RELATIONS)
  private List<RequestRelationsInner> relations = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVICES = "services";
  @SerializedName(SERIALIZED_NAME_SERVICES)
  private List<Service> services = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHIPMENTS = "shipments";
  @SerializedName(SERIALIZED_NAME_SHIPMENTS)
  private List<Shipment> shipments = new ArrayList<>();

  public static final String SERIALIZED_NAME_VEHICLE_TYPES = "vehicle_types";
  @SerializedName(SERIALIZED_NAME_VEHICLE_TYPES)
  private List<VehicleType> vehicleTypes = new ArrayList<>();

  public static final String SERIALIZED_NAME_VEHICLES = "vehicles";
  @SerializedName(SERIALIZED_NAME_VEHICLES)
  private List<Vehicle> vehicles = new ArrayList<>();

  public Request() {
  }

  @Deprecated
  public Request algorithm(Algorithm algorithm) {
    this.algorithm = algorithm;
    return this;
  }

  /**
   * Get algorithm
   * @return algorithm
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Algorithm getAlgorithm() {
    return algorithm;
  }

  @Deprecated
  public void setAlgorithm(Algorithm algorithm) {
    this.algorithm = algorithm;
  }


  public Request _configuration(ModelConfiguration _configuration) {
    this._configuration = _configuration;
    return this;
  }

  /**
   * Get _configuration
   * @return _configuration
   */
  @javax.annotation.Nullable
  public ModelConfiguration getConfiguration() {
    return _configuration;
  }

  public void setConfiguration(ModelConfiguration _configuration) {
    this._configuration = _configuration;
  }


  public Request costMatrices(List<CostMatrix> costMatrices) {
    this.costMatrices = costMatrices;
    return this;
  }

  public Request addCostMatricesItem(CostMatrix costMatricesItem) {
    if (this.costMatrices == null) {
      this.costMatrices = new ArrayList<>();
    }
    this.costMatrices.add(costMatricesItem);
    return this;
  }

  /**
   * Specifies your own tranport time and distance matrices.
   * @return costMatrices
   */
  @javax.annotation.Nullable
  public List<CostMatrix> getCostMatrices() {
    return costMatrices;
  }

  public void setCostMatrices(List<CostMatrix> costMatrices) {
    this.costMatrices = costMatrices;
  }


  public Request objectives(List<Objective> objectives) {
    this.objectives = objectives;
    return this;
  }

  public Request addObjectivesItem(Objective objectivesItem) {
    if (this.objectives == null) {
      this.objectives = new ArrayList<>();
    }
    this.objectives.add(objectivesItem);
    return this;
  }

  /**
   * Specifies an objective function. The vehicle routing problem is solved in such a way that this objective function is minimized.
   * @return objectives
   */
  @javax.annotation.Nullable
  public List<Objective> getObjectives() {
    return objectives;
  }

  public void setObjectives(List<Objective> objectives) {
    this.objectives = objectives;
  }


  public Request relations(List<RequestRelationsInner> relations) {
    this.relations = relations;
    return this;
  }

  public Request addRelationsItem(RequestRelationsInner relationsItem) {
    if (this.relations == null) {
      this.relations = new ArrayList<>();
    }
    this.relations.add(relationsItem);
    return this;
  }

  /**
   * Defines additional relationships between orders.
   * @return relations
   */
  @javax.annotation.Nullable
  public List<RequestRelationsInner> getRelations() {
    return relations;
  }

  public void setRelations(List<RequestRelationsInner> relations) {
    this.relations = relations;
  }


  public Request services(List<Service> services) {
    this.services = services;
    return this;
  }

  public Request addServicesItem(Service servicesItem) {
    if (this.services == null) {
      this.services = new ArrayList<>();
    }
    this.services.add(servicesItem);
    return this;
  }

  /**
   * Specifies the orders of the type \&quot;service\&quot;. These are, for example, pick-ups, deliveries or other stops that are to be approached by the specified vehicles. Each of these orders contains only one location.
   * @return services
   */
  @javax.annotation.Nullable
  public List<Service> getServices() {
    return services;
  }

  public void setServices(List<Service> services) {
    this.services = services;
  }


  public Request shipments(List<Shipment> shipments) {
    this.shipments = shipments;
    return this;
  }

  public Request addShipmentsItem(Shipment shipmentsItem) {
    if (this.shipments == null) {
      this.shipments = new ArrayList<>();
    }
    this.shipments.add(shipmentsItem);
    return this;
  }

  /**
   * Specifies the available shipments. Each shipment contains a pickup and a delivery stop, which must be processed one after the other.
   * @return shipments
   */
  @javax.annotation.Nullable
  public List<Shipment> getShipments() {
    return shipments;
  }

  public void setShipments(List<Shipment> shipments) {
    this.shipments = shipments;
  }


  public Request vehicleTypes(List<VehicleType> vehicleTypes) {
    this.vehicleTypes = vehicleTypes;
    return this;
  }

  public Request addVehicleTypesItem(VehicleType vehicleTypesItem) {
    if (this.vehicleTypes == null) {
      this.vehicleTypes = new ArrayList<>();
    }
    this.vehicleTypes.add(vehicleTypesItem);
    return this;
  }

  /**
   * Specifies the available vehicle types. These types can be assigned to vehicles.
   * @return vehicleTypes
   */
  @javax.annotation.Nullable
  public List<VehicleType> getVehicleTypes() {
    return vehicleTypes;
  }

  public void setVehicleTypes(List<VehicleType> vehicleTypes) {
    this.vehicleTypes = vehicleTypes;
  }


  public Request vehicles(List<Vehicle> vehicles) {
    this.vehicles = vehicles;
    return this;
  }

  public Request addVehiclesItem(Vehicle vehiclesItem) {
    if (this.vehicles == null) {
      this.vehicles = new ArrayList<>();
    }
    this.vehicles.add(vehiclesItem);
    return this;
  }

  /**
   * Specifies the available vehicles.
   * @return vehicles
   */
  @javax.annotation.Nullable
  public List<Vehicle> getVehicles() {
    return vehicles;
  }

  public void setVehicles(List<Vehicle> vehicles) {
    this.vehicles = vehicles;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Request request = (Request) o;
    return Objects.equals(this.algorithm, request.algorithm) &&
        Objects.equals(this._configuration, request._configuration) &&
        Objects.equals(this.costMatrices, request.costMatrices) &&
        Objects.equals(this.objectives, request.objectives) &&
        Objects.equals(this.relations, request.relations) &&
        Objects.equals(this.services, request.services) &&
        Objects.equals(this.shipments, request.shipments) &&
        Objects.equals(this.vehicleTypes, request.vehicleTypes) &&
        Objects.equals(this.vehicles, request.vehicles);
  }

  @Override
  public int hashCode() {
    return Objects.hash(algorithm, _configuration, costMatrices, objectives, relations, services, shipments, vehicleTypes, vehicles);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Request {\n");
    sb.append("    algorithm: ").append(toIndentedString(algorithm)).append("\n");
    sb.append("    _configuration: ").append(toIndentedString(_configuration)).append("\n");
    sb.append("    costMatrices: ").append(toIndentedString(costMatrices)).append("\n");
    sb.append("    objectives: ").append(toIndentedString(objectives)).append("\n");
    sb.append("    relations: ").append(toIndentedString(relations)).append("\n");
    sb.append("    services: ").append(toIndentedString(services)).append("\n");
    sb.append("    shipments: ").append(toIndentedString(shipments)).append("\n");
    sb.append("    vehicleTypes: ").append(toIndentedString(vehicleTypes)).append("\n");
    sb.append("    vehicles: ").append(toIndentedString(vehicles)).append("\n");
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
    openapiFields.add("algorithm");
    openapiFields.add("configuration");
    openapiFields.add("cost_matrices");
    openapiFields.add("objectives");
    openapiFields.add("relations");
    openapiFields.add("services");
    openapiFields.add("shipments");
    openapiFields.add("vehicle_types");
    openapiFields.add("vehicles");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Request
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Request.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Request is not found in the empty JSON string", Request.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Request.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Request` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `algorithm`
      if (jsonObj.get("algorithm") != null && !jsonObj.get("algorithm").isJsonNull()) {
        Algorithm.validateJsonElement(jsonObj.get("algorithm"));
      }
      // validate the optional field `configuration`
      if (jsonObj.get("configuration") != null && !jsonObj.get("configuration").isJsonNull()) {
        ModelConfiguration.validateJsonElement(jsonObj.get("configuration"));
      }
      if (jsonObj.get("cost_matrices") != null && !jsonObj.get("cost_matrices").isJsonNull()) {
        JsonArray jsonArraycostMatrices = jsonObj.getAsJsonArray("cost_matrices");
        if (jsonArraycostMatrices != null) {
          // ensure the json data is an array
          if (!jsonObj.get("cost_matrices").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `cost_matrices` to be an array in the JSON string but got `%s`", jsonObj.get("cost_matrices").toString()));
          }

          // validate the optional field `cost_matrices` (array)
          for (int i = 0; i < jsonArraycostMatrices.size(); i++) {
            CostMatrix.validateJsonElement(jsonArraycostMatrices.get(i));
          };
        }
      }
      if (jsonObj.get("objectives") != null && !jsonObj.get("objectives").isJsonNull()) {
        JsonArray jsonArrayobjectives = jsonObj.getAsJsonArray("objectives");
        if (jsonArrayobjectives != null) {
          // ensure the json data is an array
          if (!jsonObj.get("objectives").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `objectives` to be an array in the JSON string but got `%s`", jsonObj.get("objectives").toString()));
          }

          // validate the optional field `objectives` (array)
          for (int i = 0; i < jsonArrayobjectives.size(); i++) {
            Objective.validateJsonElement(jsonArrayobjectives.get(i));
          };
        }
      }
      if (jsonObj.get("relations") != null && !jsonObj.get("relations").isJsonNull()) {
        JsonArray jsonArrayrelations = jsonObj.getAsJsonArray("relations");
        if (jsonArrayrelations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("relations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `relations` to be an array in the JSON string but got `%s`", jsonObj.get("relations").toString()));
          }

          // validate the optional field `relations` (array)
          for (int i = 0; i < jsonArrayrelations.size(); i++) {
            RequestRelationsInner.validateJsonElement(jsonArrayrelations.get(i));
          };
        }
      }
      if (jsonObj.get("services") != null && !jsonObj.get("services").isJsonNull()) {
        JsonArray jsonArrayservices = jsonObj.getAsJsonArray("services");
        if (jsonArrayservices != null) {
          // ensure the json data is an array
          if (!jsonObj.get("services").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `services` to be an array in the JSON string but got `%s`", jsonObj.get("services").toString()));
          }

          // validate the optional field `services` (array)
          for (int i = 0; i < jsonArrayservices.size(); i++) {
            Service.validateJsonElement(jsonArrayservices.get(i));
          };
        }
      }
      if (jsonObj.get("shipments") != null && !jsonObj.get("shipments").isJsonNull()) {
        JsonArray jsonArrayshipments = jsonObj.getAsJsonArray("shipments");
        if (jsonArrayshipments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("shipments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `shipments` to be an array in the JSON string but got `%s`", jsonObj.get("shipments").toString()));
          }

          // validate the optional field `shipments` (array)
          for (int i = 0; i < jsonArrayshipments.size(); i++) {
            Shipment.validateJsonElement(jsonArrayshipments.get(i));
          };
        }
      }
      if (jsonObj.get("vehicle_types") != null && !jsonObj.get("vehicle_types").isJsonNull()) {
        JsonArray jsonArrayvehicleTypes = jsonObj.getAsJsonArray("vehicle_types");
        if (jsonArrayvehicleTypes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("vehicle_types").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `vehicle_types` to be an array in the JSON string but got `%s`", jsonObj.get("vehicle_types").toString()));
          }

          // validate the optional field `vehicle_types` (array)
          for (int i = 0; i < jsonArrayvehicleTypes.size(); i++) {
            VehicleType.validateJsonElement(jsonArrayvehicleTypes.get(i));
          };
        }
      }
      if (jsonObj.get("vehicles") != null && !jsonObj.get("vehicles").isJsonNull()) {
        JsonArray jsonArrayvehicles = jsonObj.getAsJsonArray("vehicles");
        if (jsonArrayvehicles != null) {
          // ensure the json data is an array
          if (!jsonObj.get("vehicles").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `vehicles` to be an array in the JSON string but got `%s`", jsonObj.get("vehicles").toString()));
          }

          // validate the optional field `vehicles` (array)
          for (int i = 0; i < jsonArrayvehicles.size(); i++) {
            Vehicle.validateJsonElement(jsonArrayvehicles.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Request.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Request' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Request> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Request.class));

       return (TypeAdapter<T>) new TypeAdapter<Request>() {
           @Override
           public void write(JsonWriter out, Request value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Request read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Request given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Request
   * @throws IOException if the JSON string is invalid with respect to Request
   */
  public static Request fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Request.class);
  }

  /**
   * Convert an instance of Request to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

