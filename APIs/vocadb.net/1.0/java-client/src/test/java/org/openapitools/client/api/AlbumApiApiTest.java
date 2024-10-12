/*
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AdvancedSearchFilterParams;
import org.openapitools.client.model.AlbumForApiContract;
import org.openapitools.client.model.AlbumForApiContractPartialFindResult;
import org.openapitools.client.model.AlbumForUserForApiContract;
import org.openapitools.client.model.AlbumOptionalFields;
import org.openapitools.client.model.AlbumReviewContract;
import org.openapitools.client.model.AlbumSortRule;
import org.openapitools.client.model.ArtistAlbumParticipationStatus;
import org.openapitools.client.model.CommentForApiContract;
import org.openapitools.client.model.ContentLanguagePreference;
import org.openapitools.client.model.DiscType;
import org.openapitools.client.model.EntryStatus;
import org.openapitools.client.model.NameMatchMode;
import java.time.OffsetDateTime;
import org.openapitools.client.model.SongInAlbumForApiContract;
import org.openapitools.client.model.SongOptionalFields;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AlbumApiApi
 */
@Disabled
public class AlbumApiApiTest {

    private final AlbumApiApi api = new AlbumApiApi();

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsCommentsCommentIdDeleteTest() throws ApiException {
        Integer commentId = null;
        api.apiAlbumsCommentsCommentIdDelete(commentId);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsCommentsCommentIdPostTest() throws ApiException {
        Integer commentId = null;
        CommentForApiContract commentForApiContract = null;
        api.apiAlbumsCommentsCommentIdPost(commentId, commentForApiContract);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsGetTest() throws ApiException {
        String query = null;
        DiscType discTypes = null;
        List<String> tagName = null;
        List<Integer> tagId = null;
        Boolean childTags = null;
        List<Integer> artistId = null;
        ArtistAlbumParticipationStatus artistParticipationStatus = null;
        Boolean childVoicebanks = null;
        Boolean includeMembers = null;
        String barcode = null;
        EntryStatus status = null;
        OffsetDateTime releaseDateAfter = null;
        OffsetDateTime releaseDateBefore = null;
        List<AdvancedSearchFilterParams> advancedFilters = null;
        Integer start = null;
        Integer maxResults = null;
        Boolean getTotalCount = null;
        AlbumSortRule sort = null;
        Boolean preferAccurateMatches = null;
        Boolean deleted = null;
        NameMatchMode nameMatchMode = null;
        AlbumOptionalFields fields = null;
        ContentLanguagePreference lang = null;
        AlbumForApiContractPartialFindResult response = api.apiAlbumsGet(query, discTypes, tagName, tagId, childTags, artistId, artistParticipationStatus, childVoicebanks, includeMembers, barcode, status, releaseDateAfter, releaseDateBefore, advancedFilters, start, maxResults, getTotalCount, sort, preferAccurateMatches, deleted, nameMatchMode, fields, lang);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdCommentsGetTest() throws ApiException {
        Integer id = null;
        List<CommentForApiContract> response = api.apiAlbumsIdCommentsGet(id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdCommentsPostTest() throws ApiException {
        Integer id = null;
        CommentForApiContract commentForApiContract = null;
        CommentForApiContract response = api.apiAlbumsIdCommentsPost(id, commentForApiContract);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdDeleteTest() throws ApiException {
        Integer id = null;
        String notes = null;
        api.apiAlbumsIdDelete(id, notes);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdGetTest() throws ApiException {
        Integer id = null;
        AlbumOptionalFields fields = null;
        SongOptionalFields songFields = null;
        ContentLanguagePreference lang = null;
        AlbumForApiContract response = api.apiAlbumsIdGet(id, fields, songFields, lang);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdReviewsGetTest() throws ApiException {
        Integer id = null;
        String languageCode = null;
        List<AlbumReviewContract> response = api.apiAlbumsIdReviewsGet(id, languageCode);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdReviewsPostTest() throws ApiException {
        Integer id = null;
        AlbumReviewContract albumReviewContract = null;
        AlbumReviewContract response = api.apiAlbumsIdReviewsPost(id, albumReviewContract);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdReviewsReviewIdDeleteTest() throws ApiException {
        Integer reviewId = null;
        String id = null;
        api.apiAlbumsIdReviewsReviewIdDelete(reviewId, id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdTracksFieldsGetTest() throws ApiException {
        Integer id = null;
        List<String> field = null;
        Integer discNumber = null;
        ContentLanguagePreference lang = null;
        List<Map<String, String>> response = api.apiAlbumsIdTracksFieldsGet(id, field, discNumber, lang);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdTracksGetTest() throws ApiException {
        Integer id = null;
        SongOptionalFields fields = null;
        ContentLanguagePreference lang = null;
        List<SongInAlbumForApiContract> response = api.apiAlbumsIdTracksGet(id, fields, lang);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsIdUserCollectionsGetTest() throws ApiException {
        Integer id = null;
        ContentLanguagePreference languagePreference = null;
        List<AlbumForUserForApiContract> response = api.apiAlbumsIdUserCollectionsGet(id, languagePreference);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsNamesGetTest() throws ApiException {
        String query = null;
        NameMatchMode nameMatchMode = null;
        Integer maxResults = null;
        List<String> response = api.apiAlbumsNamesGet(query, nameMatchMode, maxResults);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsNewGetTest() throws ApiException {
        ContentLanguagePreference languagePreference = null;
        AlbumOptionalFields fields = null;
        List<AlbumForApiContract> response = api.apiAlbumsNewGet(languagePreference, fields);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiAlbumsTopGetTest() throws ApiException {
        List<Integer> ignoreIds = null;
        ContentLanguagePreference languagePreference = null;
        AlbumOptionalFields fields = null;
        List<AlbumForApiContract> response = api.apiAlbumsTopGet(ignoreIds, languagePreference, fields);
        // TODO: test validations
    }

}
