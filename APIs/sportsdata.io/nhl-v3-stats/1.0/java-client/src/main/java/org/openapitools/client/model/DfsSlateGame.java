/*
 * NHL v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
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
import org.openapitools.client.model.Game;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * DfsSlateGame
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:40.960519-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DfsSlateGame {
  public static final String SERIALIZED_NAME_GAME = "Game";
  @SerializedName(SERIALIZED_NAME_GAME)
  private Game game;

  public static final String SERIALIZED_NAME_GAME_I_D = "GameID";
  @SerializedName(SERIALIZED_NAME_GAME_I_D)
  private Integer gameID;

  public static final String SERIALIZED_NAME_OPERATOR_GAME_I_D = "OperatorGameID";
  @SerializedName(SERIALIZED_NAME_OPERATOR_GAME_I_D)
  private Integer operatorGameID;

  public static final String SERIALIZED_NAME_REMOVED_BY_OPERATOR = "RemovedByOperator";
  @SerializedName(SERIALIZED_NAME_REMOVED_BY_OPERATOR)
  private Boolean removedByOperator;

  public static final String SERIALIZED_NAME_SLATE_GAME_I_D = "SlateGameID";
  @SerializedName(SERIALIZED_NAME_SLATE_GAME_I_D)
  private Integer slateGameID;

  public static final String SERIALIZED_NAME_SLATE_I_D = "SlateID";
  @SerializedName(SERIALIZED_NAME_SLATE_I_D)
  private Integer slateID;

  public DfsSlateGame() {
  }

  public DfsSlateGame game(Game game) {
    this.game = game;
    return this;
  }

  /**
   * Get game
   * @return game
   */
  @javax.annotation.Nullable
  public Game getGame() {
    return game;
  }

  public void setGame(Game game) {
    this.game = game;
  }


  public DfsSlateGame gameID(Integer gameID) {
    this.gameID = gameID;
    return this;
  }

  /**
   * Get gameID
   * @return gameID
   */
  @javax.annotation.Nullable
  public Integer getGameID() {
    return gameID;
  }

  public void setGameID(Integer gameID) {
    this.gameID = gameID;
  }


  public DfsSlateGame operatorGameID(Integer operatorGameID) {
    this.operatorGameID = operatorGameID;
    return this;
  }

  /**
   * Get operatorGameID
   * @return operatorGameID
   */
  @javax.annotation.Nullable
  public Integer getOperatorGameID() {
    return operatorGameID;
  }

  public void setOperatorGameID(Integer operatorGameID) {
    this.operatorGameID = operatorGameID;
  }


  public DfsSlateGame removedByOperator(Boolean removedByOperator) {
    this.removedByOperator = removedByOperator;
    return this;
  }

  /**
   * Get removedByOperator
   * @return removedByOperator
   */
  @javax.annotation.Nullable
  public Boolean getRemovedByOperator() {
    return removedByOperator;
  }

  public void setRemovedByOperator(Boolean removedByOperator) {
    this.removedByOperator = removedByOperator;
  }


  public DfsSlateGame slateGameID(Integer slateGameID) {
    this.slateGameID = slateGameID;
    return this;
  }

  /**
   * Get slateGameID
   * @return slateGameID
   */
  @javax.annotation.Nullable
  public Integer getSlateGameID() {
    return slateGameID;
  }

  public void setSlateGameID(Integer slateGameID) {
    this.slateGameID = slateGameID;
  }


  public DfsSlateGame slateID(Integer slateID) {
    this.slateID = slateID;
    return this;
  }

  /**
   * Get slateID
   * @return slateID
   */
  @javax.annotation.Nullable
  public Integer getSlateID() {
    return slateID;
  }

  public void setSlateID(Integer slateID) {
    this.slateID = slateID;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DfsSlateGame dfsSlateGame = (DfsSlateGame) o;
    return Objects.equals(this.game, dfsSlateGame.game) &&
        Objects.equals(this.gameID, dfsSlateGame.gameID) &&
        Objects.equals(this.operatorGameID, dfsSlateGame.operatorGameID) &&
        Objects.equals(this.removedByOperator, dfsSlateGame.removedByOperator) &&
        Objects.equals(this.slateGameID, dfsSlateGame.slateGameID) &&
        Objects.equals(this.slateID, dfsSlateGame.slateID);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(game, gameID, operatorGameID, removedByOperator, slateGameID, slateID);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DfsSlateGame {\n");
    sb.append("    game: ").append(toIndentedString(game)).append("\n");
    sb.append("    gameID: ").append(toIndentedString(gameID)).append("\n");
    sb.append("    operatorGameID: ").append(toIndentedString(operatorGameID)).append("\n");
    sb.append("    removedByOperator: ").append(toIndentedString(removedByOperator)).append("\n");
    sb.append("    slateGameID: ").append(toIndentedString(slateGameID)).append("\n");
    sb.append("    slateID: ").append(toIndentedString(slateID)).append("\n");
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
    openapiFields.add("Game");
    openapiFields.add("GameID");
    openapiFields.add("OperatorGameID");
    openapiFields.add("RemovedByOperator");
    openapiFields.add("SlateGameID");
    openapiFields.add("SlateID");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DfsSlateGame
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DfsSlateGame.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DfsSlateGame is not found in the empty JSON string", DfsSlateGame.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DfsSlateGame.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DfsSlateGame` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `Game`
      if (jsonObj.get("Game") != null && !jsonObj.get("Game").isJsonNull()) {
        Game.validateJsonElement(jsonObj.get("Game"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DfsSlateGame.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DfsSlateGame' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DfsSlateGame> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DfsSlateGame.class));

       return (TypeAdapter<T>) new TypeAdapter<DfsSlateGame>() {
           @Override
           public void write(JsonWriter out, DfsSlateGame value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DfsSlateGame read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DfsSlateGame given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DfsSlateGame
   * @throws IOException if the JSON string is invalid with respect to DfsSlateGame
   */
  public static DfsSlateGame fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DfsSlateGame.class);
  }

  /**
   * Convert an instance of DfsSlateGame to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

