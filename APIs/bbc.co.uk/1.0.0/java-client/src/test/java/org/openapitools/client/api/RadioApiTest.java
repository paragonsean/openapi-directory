/*
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
import org.openapitools.client.model.PersonalisedRadioBatchRequest;
import org.openapitools.client.model.PersonalisedRadioErrorResponse;
import org.openapitools.client.model.PersonalisedRadioRequest;
import org.openapitools.client.model.PersonalisedRadioResponse;
import org.openapitools.client.model.PersonalisedRadioSuccessResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for RadioApi
 */
@Disabled
public class RadioApiTest {

    private final RadioApi api = new RadioApi();

    /**
     * Favourite Episode or Clip
     *
     * Remove User favourite 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePersonalisedRadioByActivityTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        PersonalisedRadioSuccessResponse response = api.deletePersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid);
        // TODO: test validations
    }

    /**
     * Followed Brand or Series
     *
     * Remove &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePersonalisedRadioFollowsByTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        PersonalisedRadioSuccessResponse response = api.deletePersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid);
        // TODO: test validations
    }

    /**
     * Favourite Episode or Clip
     *
     * Check to see if a single clip or episode entity is in a users favourites - determines UX of add button.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalisedRadioByActivityTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        Boolean showAllActivity = null;
        PersonalisedRadioResponse response = api.getPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, showAllActivity);
        // TODO: test validations
    }

    /**
     * Favourite Episodes and Clips
     *
     * List of favourited episodes and clips for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalisedRadioFavouritesTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        Boolean showAllActivity = null;
        PersonalisedRadioResponse response = api.getPersonalisedRadioFavourites(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity);
        // TODO: test validations
    }

    /**
     * Favourite Episodes and Clips by Type
     *
     * List of followed &#39;clips&#39; or &#39;episode&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalisedRadioFavouritesByTypeTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String sort = null;
        Boolean showAllActivity = null;
        Integer offset = null;
        Integer limit = null;
        PersonalisedRadioResponse response = api.getPersonalisedRadioFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, sort, showAllActivity, offset, limit);
        // TODO: test validations
    }

    /**
     * Followed Brands and Series
     *
     * List of favourited brands and series for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalisedRadioFollowsTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        Boolean showAllActivity = null;
        PersonalisedRadioResponse response = api.getPersonalisedRadioFollows(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity);
        // TODO: test validations
    }

    /**
     * Followed Brands or Series by Type
     *
     * List of followed &#39;brand&#39; or &#39;series&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalisedRadioFollowsByTypeTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String sort = null;
        Integer offset = null;
        Integer limit = null;
        Boolean showAllActivity = null;
        PersonalisedRadioResponse response = api.getPersonalisedRadioFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, sort, offset, limit, showAllActivity);
        // TODO: test validations
    }

    /**
     * Followed Brand or Series
     *
     * Check to see if a single brand or series entity is in a users follows - determines UX of add button. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalisedRadioFollowsByTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        PersonalisedRadioResponse response = api.getPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid);
        // TODO: test validations
    }

    /**
     * Played Episode or Clip
     *
     * Returns mixed episode and clip plays for a given BBC iPlayer radio user.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalisedRadioPlaysTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        Boolean showAllActivity = null;
        PersonalisedRadioResponse response = api.getPersonalisedRadioPlays(authorization, xAuthenticationProvider, xAPIKey, offset, limit, sort, showAllActivity);
        // TODO: test validations
    }

    /**
     * Favourite Episodes and Clips
     *
     * Add User favourites  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postPersonalisedRadioBatchTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        List<PersonalisedRadioBatchRequest> body = null;
        PersonalisedRadioSuccessResponse response = api.postPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body);
        // TODO: test validations
    }

    /**
     * Favourite Episode or Clip
     *
     * Add User favourite  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postPersonalisedRadioByActivityTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        PersonalisedRadioRequest body = null;
        PersonalisedRadioSuccessResponse response = api.postPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
        // TODO: test validations
    }

    /**
     * Followed Brands and Series
     *
     * Add &#39;brand&#39; or &#39;series&#39; items to a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postPersonalisedRadioFollowsBatchTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        List<PersonalisedRadioBatchRequest> body = null;
        PersonalisedRadioSuccessResponse response = api.postPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body);
        // TODO: test validations
    }

    /**
     * Followed Brand or Series
     *
     * Add &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postPersonalisedRadioFollowsByTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        PersonalisedRadioRequest body = null;
        PersonalisedRadioSuccessResponse response = api.postPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
        // TODO: test validations
    }

    /**
     * Favourite Episodes and Clips
     *
     * Update user favourites  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putPersonalisedRadioBatchTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        List<PersonalisedRadioBatchRequest> body = null;
        PersonalisedRadioSuccessResponse response = api.putPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body);
        // TODO: test validations
    }

    /**
     * Favourite Episode or Clip
     *
     * Update user favourite  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putPersonalisedRadioByActivityTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        PersonalisedRadioRequest body = null;
        PersonalisedRadioSuccessResponse response = api.putPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
        // TODO: test validations
    }

    /**
     * Followed Brands and Series
     *
     * Update &#39;brands&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putPersonalisedRadioFollowsBatchTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        List<PersonalisedRadioBatchRequest> body = null;
        PersonalisedRadioSuccessResponse response = api.putPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body);
        // TODO: test validations
    }

    /**
     * Followed Brand or Series
     *
     * Update &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putPersonalisedRadioFollowsByTypeByIdTest() throws ApiException {
        String authorization = null;
        String xAuthenticationProvider = null;
        String xAPIKey = null;
        String type = null;
        String pid = null;
        PersonalisedRadioRequest body = null;
        PersonalisedRadioSuccessResponse response = api.putPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body);
        // TODO: test validations
    }

}
