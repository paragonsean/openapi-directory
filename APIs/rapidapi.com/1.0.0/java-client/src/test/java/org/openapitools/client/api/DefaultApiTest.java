/*
 * Moon API
 * # Moon-API.com Postman Collection  Welcome to the Moon Phase API Postman Collection! This collection contains a set of pre-configured API requests to interact with the Moon Phase API endpoints provided by [moon-api.com](https://moon-api.com). Explore the enchanting world of the moon and its ever-changing phases with ease using this collection.  ## Getting Started  To start using this Postman collection, follow these steps:  1. [Download and install Postman](https://www.postman.com/downloads/) if you haven't already. 2. Import the Moon API Postman Collection into your Postman app. 3. Set your RapidAPI key in the collection's environment variables. 4. Begin making requests to explore the moon phase data and retrieve lunar information.       ## Collection Structure  The Moon-API.com Postman Collection consists of the following requests:  - **Basic Moon Phase**: Retrieve the main moon phase data. - **Advanced Moon Phase**: Get detailed moon phase data based on a specific timezone and coordinates. - **Plain Text Moon Phase**: Get a plain text description of the current moon phase. - **Emoji Moon Phase**: Get the relevant emoji of the current moon phase. - **Lunar Calender**: Get the current year's moon phases in a markdown calender.       ## Environment Variables  The collection uses environment variables to store your RapidAPI key. To use this collection effectively, ensure you set the `X-Rapidapi-Key` variable in the collection's environment with your actual RapidAPI key.  ## How to Use  1. Select the desired request from the Moon API collection. 2. Click on the request to open it. 3. Send the request and view the response to retrieve the moon phase data.       ## Documentation  For more information on the Moon Phase API endpoints and their response formats, refer to the [official Moon API documentation](https://rapidapi.com/MoonAPIcom/api/moon-phase/details). Visit [moon-api.com](https://moon-api.com) to learn more about the Moon Phase API and the services provided.  Happy moon exploration with the Moon Phase API Postman Collection provided by [moon-api.com](https://moon-api.com)!
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.GetAdvancedMoonPhaseData200Response;
import org.openapitools.client.model.GetBasicMoonPhaseData200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Get Advanced Moon Phase Data
     *
     * Get Advanced Moon Phase Data
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAdvancedMoonPhaseDataTest() throws ApiException {
        String filters = null;
        String xRapidapiKey = null;
        GetAdvancedMoonPhaseData200Response response = api.getAdvancedMoonPhaseData(filters, xRapidapiKey);
        // TODO: test validations
    }

    /**
     * Get Basic Moon Phase Data
     *
     * Get Basic Moon Phase Data
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBasicMoonPhaseDataTest() throws ApiException {
        String xRapidapiKey = null;
        GetBasicMoonPhaseData200Response response = api.getBasicMoonPhaseData(xRapidapiKey);
        // TODO: test validations
    }

    /**
     * Get Emoji of Moon Phase
     *
     * Get Emoji of Moon Phase
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEmojiOfMoonPhaseTest() throws ApiException {
        String xRapidapiKey = null;
        api.getEmojiOfMoonPhase(xRapidapiKey);
        // TODO: test validations
    }

    /**
     * Get Lunar Calendar
     *
     * Get Lunar Calendar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLunarCalendarTest() throws ApiException {
        String filters = null;
        String xRapidapiKey = null;
        api.getLunarCalendar(filters, xRapidapiKey);
        // TODO: test validations
    }

    /**
     * Get Plain Text Moon Phase Data
     *
     * Get Plain Text Moon Phase Data
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPlainTextMoonPhaseDataTest() throws ApiException {
        String xRapidapiKey = null;
        api.getPlainTextMoonPhaseData(xRapidapiKey);
        // TODO: test validations
    }

}
