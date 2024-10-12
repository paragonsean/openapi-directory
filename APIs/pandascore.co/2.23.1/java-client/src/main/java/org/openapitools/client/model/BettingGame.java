/*
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
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
import org.openapitools.client.model.BettingCSGOGame;
import org.openapitools.client.model.BettingDota2Game;
import org.openapitools.client.model.BettingGameRoundTeams1;
import org.openapitools.client.model.BettingGameTeams1;
import org.openapitools.client.model.BettingLoLGame;
import org.openapitools.client.model.BettingOwGame;
import org.openapitools.client.model.BettingPUBGGame;
import org.openapitools.client.model.CSGOMap1;
import org.openapitools.client.model.GameStatus;
import org.openapitools.client.model.GameWinner;



import java.io.IOException;
import java.lang.reflect.Type;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.JsonPrimitive;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonSerializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;
import com.google.gson.JsonParseException;

import org.openapitools.client.JSON;

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:25.859268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BettingGame extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(BettingGame.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!BettingGame.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'BettingGame' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<BettingCSGOGame> adapterBettingCSGOGame = gson.getDelegateAdapter(this, TypeToken.get(BettingCSGOGame.class));
            final TypeAdapter<BettingDota2Game> adapterBettingDota2Game = gson.getDelegateAdapter(this, TypeToken.get(BettingDota2Game.class));
            final TypeAdapter<BettingLoLGame> adapterBettingLoLGame = gson.getDelegateAdapter(this, TypeToken.get(BettingLoLGame.class));
            final TypeAdapter<BettingOwGame> adapterBettingOwGame = gson.getDelegateAdapter(this, TypeToken.get(BettingOwGame.class));
            final TypeAdapter<BettingPUBGGame> adapterBettingPUBGGame = gson.getDelegateAdapter(this, TypeToken.get(BettingPUBGGame.class));

            return (TypeAdapter<T>) new TypeAdapter<BettingGame>() {
                @Override
                public void write(JsonWriter out, BettingGame value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `BettingCSGOGame`
                    if (value.getActualInstance() instanceof BettingCSGOGame) {
                        JsonElement element = adapterBettingCSGOGame.toJsonTree((BettingCSGOGame)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `BettingDota2Game`
                    if (value.getActualInstance() instanceof BettingDota2Game) {
                        JsonElement element = adapterBettingDota2Game.toJsonTree((BettingDota2Game)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `BettingLoLGame`
                    if (value.getActualInstance() instanceof BettingLoLGame) {
                        JsonElement element = adapterBettingLoLGame.toJsonTree((BettingLoLGame)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `BettingOwGame`
                    if (value.getActualInstance() instanceof BettingOwGame) {
                        JsonElement element = adapterBettingOwGame.toJsonTree((BettingOwGame)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `BettingPUBGGame`
                    if (value.getActualInstance() instanceof BettingPUBGGame) {
                        JsonElement element = adapterBettingPUBGGame.toJsonTree((BettingPUBGGame)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: BettingCSGOGame, BettingDota2Game, BettingLoLGame, BettingOwGame, BettingPUBGGame");
                }

                @Override
                public BettingGame read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize BettingCSGOGame
                    try {
                        // validate the JSON object to see if any exception is thrown
                        BettingCSGOGame.validateJsonElement(jsonElement);
                        actualAdapter = adapterBettingCSGOGame;
                        BettingGame ret = new BettingGame();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for BettingCSGOGame failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'BettingCSGOGame'", e);
                    }
                    // deserialize BettingDota2Game
                    try {
                        // validate the JSON object to see if any exception is thrown
                        BettingDota2Game.validateJsonElement(jsonElement);
                        actualAdapter = adapterBettingDota2Game;
                        BettingGame ret = new BettingGame();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for BettingDota2Game failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'BettingDota2Game'", e);
                    }
                    // deserialize BettingLoLGame
                    try {
                        // validate the JSON object to see if any exception is thrown
                        BettingLoLGame.validateJsonElement(jsonElement);
                        actualAdapter = adapterBettingLoLGame;
                        BettingGame ret = new BettingGame();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for BettingLoLGame failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'BettingLoLGame'", e);
                    }
                    // deserialize BettingOwGame
                    try {
                        // validate the JSON object to see if any exception is thrown
                        BettingOwGame.validateJsonElement(jsonElement);
                        actualAdapter = adapterBettingOwGame;
                        BettingGame ret = new BettingGame();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for BettingOwGame failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'BettingOwGame'", e);
                    }
                    // deserialize BettingPUBGGame
                    try {
                        // validate the JSON object to see if any exception is thrown
                        BettingPUBGGame.validateJsonElement(jsonElement);
                        actualAdapter = adapterBettingPUBGGame;
                        BettingGame ret = new BettingGame();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for BettingPUBGGame failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'BettingPUBGGame'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for BettingGame: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public BettingGame() {
        super("anyOf", Boolean.FALSE);
    }

    public BettingGame(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("BettingCSGOGame", BettingCSGOGame.class);
        schemas.put("BettingDota2Game", BettingDota2Game.class);
        schemas.put("BettingLoLGame", BettingLoLGame.class);
        schemas.put("BettingOwGame", BettingOwGame.class);
        schemas.put("BettingPUBGGame", BettingPUBGGame.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return BettingGame.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * BettingCSGOGame, BettingDota2Game, BettingLoLGame, BettingOwGame, BettingPUBGGame
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof BettingCSGOGame) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof BettingDota2Game) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof BettingLoLGame) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof BettingOwGame) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof BettingPUBGGame) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be BettingCSGOGame, BettingDota2Game, BettingLoLGame, BettingOwGame, BettingPUBGGame");
    }

    /**
     * Get the actual instance, which can be the following:
     * BettingCSGOGame, BettingDota2Game, BettingLoLGame, BettingOwGame, BettingPUBGGame
     *
     * @return The actual instance (BettingCSGOGame, BettingDota2Game, BettingLoLGame, BettingOwGame, BettingPUBGGame)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `BettingCSGOGame`. If the actual instance is not `BettingCSGOGame`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `BettingCSGOGame`
     * @throws ClassCastException if the instance is not `BettingCSGOGame`
     */
    public BettingCSGOGame getBettingCSGOGame() throws ClassCastException {
        return (BettingCSGOGame)super.getActualInstance();
    }
    /**
     * Get the actual instance of `BettingDota2Game`. If the actual instance is not `BettingDota2Game`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `BettingDota2Game`
     * @throws ClassCastException if the instance is not `BettingDota2Game`
     */
    public BettingDota2Game getBettingDota2Game() throws ClassCastException {
        return (BettingDota2Game)super.getActualInstance();
    }
    /**
     * Get the actual instance of `BettingLoLGame`. If the actual instance is not `BettingLoLGame`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `BettingLoLGame`
     * @throws ClassCastException if the instance is not `BettingLoLGame`
     */
    public BettingLoLGame getBettingLoLGame() throws ClassCastException {
        return (BettingLoLGame)super.getActualInstance();
    }
    /**
     * Get the actual instance of `BettingOwGame`. If the actual instance is not `BettingOwGame`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `BettingOwGame`
     * @throws ClassCastException if the instance is not `BettingOwGame`
     */
    public BettingOwGame getBettingOwGame() throws ClassCastException {
        return (BettingOwGame)super.getActualInstance();
    }
    /**
     * Get the actual instance of `BettingPUBGGame`. If the actual instance is not `BettingPUBGGame`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `BettingPUBGGame`
     * @throws ClassCastException if the instance is not `BettingPUBGGame`
     */
    public BettingPUBGGame getBettingPUBGGame() throws ClassCastException {
        return (BettingPUBGGame)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to BettingGame
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate anyOf schemas one by one
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with BettingCSGOGame
        try {
            BettingCSGOGame.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for BettingCSGOGame failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with BettingDota2Game
        try {
            BettingDota2Game.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for BettingDota2Game failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with BettingLoLGame
        try {
            BettingLoLGame.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for BettingLoLGame failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with BettingOwGame
        try {
            BettingOwGame.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for BettingOwGame failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with BettingPUBGGame
        try {
            BettingPUBGGame.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for BettingPUBGGame failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for BettingGame with anyOf schemas: BettingCSGOGame, BettingDota2Game, BettingLoLGame, BettingOwGame, BettingPUBGGame. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of BettingGame given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of BettingGame
     * @throws IOException if the JSON string is invalid with respect to BettingGame
     */
    public static BettingGame fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, BettingGame.class);
    }

    /**
     * Convert an instance of BettingGame to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

