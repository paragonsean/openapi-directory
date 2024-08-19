/*
 * Amazon Rekognition
 * <p>This is the API Reference for <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/images.html\">Amazon Rekognition Image</a>, <a href=\"https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html\">Amazon Rekognition Custom Labels</a>, <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/video.html\">Amazon Rekognition Stored Video</a>, <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html\">Amazon Rekognition Streaming Video</a>. It provides descriptions of actions, data types, common parameters, and common errors.</p> <p> <b>Amazon Rekognition Image</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html\">AssociateFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html\">CompareFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html\">CreateCollection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html\">CreateUser</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html\">DeleteCollection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html\">DeleteFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html\">DeleteUser</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html\">DescribeCollection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html\">DetectFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html\">DetectLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html\">DetectModerationLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html\">DetectProtectiveEquipment</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html\">DetectText</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html\">DisassociateFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityInfo.html\">GetCelebrityInfo</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html\">IndexFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html\">ListCollections</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html\">ListFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html\">ListUsers</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html\">RecognizeCelebrities</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html\">SearchFaces</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html\">SearchFacesByImage</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html\">SearchUsers</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html\">SearchUsersByImage</a> </p> </li> </ul> <p> <b>Amazon Rekognition Custom Labels</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CopyProjectVersion.html\">CopyProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateDataset.html\">CreateDataset</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProject.html\">CreateProject</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProjectVersion.html\">CreateProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteDataset.html\">DeleteDataset</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProject.html\">DeleteProject</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectPolicy.html\">DeleteProjectPolicy</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectVersion.html\">DeleteProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeDataset.html\">DescribeDataset</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjects.html\">DescribeProjects</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjectVersions.html\">DescribeProjectVersions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels.html\">DetectCustomLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DistributeDatasetEntries.html\">DistributeDatasetEntries</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetEntries.html\">ListDatasetEntries</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetLabels.html\">ListDatasetLabels</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListProjectPolicies.html\">ListProjectPolicies</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PutProjectPolicy.html\">PutProjectPolicy</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartProjectVersion.html\">StartProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StopProjectVersion.html\">StopProjectVersion</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateDatasetEntries.html\">UpdateDatasetEntries</a> </p> </li> </ul> <p> <b>Amazon Rekognition Video Stored Video</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityRecognition.html\">GetCelebrityRecognition</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetContentModeration.html\">GetContentModeration</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceDetection.html\">GetFaceDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceSearch.html\">GetFaceSearch</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetLabelDetection.html\">GetLabelDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetPersonTracking.html\">GetPersonTracking</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetSegmentDetection.html\">GetSegmentDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetTextDetection.html\">GetTextDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html\">StartCelebrityRecognition</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html\">StartContentModeration</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html\">StartFaceDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html\">StartFaceSearch</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html\">StartLabelDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html\">StartPersonTracking</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartSegmentDetection.html\">StartSegmentDetection</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartTextDetection.html\">StartTextDetection</a> </p> </li> </ul> <p> <b>Amazon Rekognition Video Streaming Video</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html\">CreateStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteStreamProcessor.html\">DeleteStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeStreamProcessor.html\">DescribeStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListStreamProcessors.html\">ListStreamProcessors</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html\">StartStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StopStreamProcessor.html\">StopStreamProcessor</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateStreamProcessor.html\">UpdateStreamProcessor</a> </p> </li> </ul>
 *
 * The version of the OpenAPI document: 2016-06-27
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AssociateFacesRequest;
import org.openapitools.client.model.AssociateFacesResponse;
import org.openapitools.client.model.CompareFacesRequest;
import org.openapitools.client.model.CompareFacesResponse;
import org.openapitools.client.model.CopyProjectVersionRequest;
import org.openapitools.client.model.CopyProjectVersionResponse;
import org.openapitools.client.model.CreateCollectionRequest;
import org.openapitools.client.model.CreateCollectionResponse;
import org.openapitools.client.model.CreateDatasetRequest;
import org.openapitools.client.model.CreateDatasetResponse;
import org.openapitools.client.model.CreateFaceLivenessSessionRequest;
import org.openapitools.client.model.CreateFaceLivenessSessionResponse;
import org.openapitools.client.model.CreateProjectRequest;
import org.openapitools.client.model.CreateProjectResponse;
import org.openapitools.client.model.CreateProjectVersionRequest;
import org.openapitools.client.model.CreateProjectVersionResponse;
import org.openapitools.client.model.CreateStreamProcessorRequest;
import org.openapitools.client.model.CreateStreamProcessorResponse;
import org.openapitools.client.model.CreateUserRequest;
import org.openapitools.client.model.DeleteCollectionRequest;
import org.openapitools.client.model.DeleteCollectionResponse;
import org.openapitools.client.model.DeleteDatasetRequest;
import org.openapitools.client.model.DeleteFacesRequest;
import org.openapitools.client.model.DeleteFacesResponse;
import org.openapitools.client.model.DeleteProjectPolicyRequest;
import org.openapitools.client.model.DeleteProjectRequest;
import org.openapitools.client.model.DeleteProjectResponse;
import org.openapitools.client.model.DeleteProjectVersionRequest;
import org.openapitools.client.model.DeleteProjectVersionResponse;
import org.openapitools.client.model.DeleteStreamProcessorRequest;
import org.openapitools.client.model.DeleteUserRequest;
import org.openapitools.client.model.DescribeCollectionRequest;
import org.openapitools.client.model.DescribeCollectionResponse;
import org.openapitools.client.model.DescribeDatasetRequest;
import org.openapitools.client.model.DescribeDatasetResponse;
import org.openapitools.client.model.DescribeProjectVersionsRequest;
import org.openapitools.client.model.DescribeProjectVersionsResponse;
import org.openapitools.client.model.DescribeProjectsRequest;
import org.openapitools.client.model.DescribeProjectsResponse;
import org.openapitools.client.model.DescribeStreamProcessorRequest;
import org.openapitools.client.model.DescribeStreamProcessorResponse;
import org.openapitools.client.model.DetectCustomLabelsRequest;
import org.openapitools.client.model.DetectCustomLabelsResponse;
import org.openapitools.client.model.DetectFacesRequest;
import org.openapitools.client.model.DetectFacesResponse;
import org.openapitools.client.model.DetectLabelsRequest;
import org.openapitools.client.model.DetectLabelsResponse;
import org.openapitools.client.model.DetectModerationLabelsRequest;
import org.openapitools.client.model.DetectModerationLabelsResponse;
import org.openapitools.client.model.DetectProtectiveEquipmentRequest;
import org.openapitools.client.model.DetectProtectiveEquipmentResponse;
import org.openapitools.client.model.DetectTextRequest;
import org.openapitools.client.model.DetectTextResponse;
import org.openapitools.client.model.DisassociateFacesRequest;
import org.openapitools.client.model.DisassociateFacesResponse;
import org.openapitools.client.model.DistributeDatasetEntriesRequest;
import org.openapitools.client.model.GetCelebrityInfoRequest;
import org.openapitools.client.model.GetCelebrityInfoResponse;
import org.openapitools.client.model.GetCelebrityRecognitionRequest;
import org.openapitools.client.model.GetCelebrityRecognitionResponse;
import org.openapitools.client.model.GetContentModerationRequest;
import org.openapitools.client.model.GetContentModerationResponse;
import org.openapitools.client.model.GetFaceDetectionRequest;
import org.openapitools.client.model.GetFaceDetectionResponse;
import org.openapitools.client.model.GetFaceLivenessSessionResultsRequest;
import org.openapitools.client.model.GetFaceLivenessSessionResultsResponse;
import org.openapitools.client.model.GetFaceSearchRequest;
import org.openapitools.client.model.GetFaceSearchResponse;
import org.openapitools.client.model.GetLabelDetectionRequest;
import org.openapitools.client.model.GetLabelDetectionResponse;
import org.openapitools.client.model.GetPersonTrackingRequest;
import org.openapitools.client.model.GetPersonTrackingResponse;
import org.openapitools.client.model.GetSegmentDetectionRequest;
import org.openapitools.client.model.GetSegmentDetectionResponse;
import org.openapitools.client.model.GetTextDetectionRequest;
import org.openapitools.client.model.GetTextDetectionResponse;
import org.openapitools.client.model.IndexFacesRequest;
import org.openapitools.client.model.IndexFacesResponse;
import org.openapitools.client.model.ListCollectionsRequest;
import org.openapitools.client.model.ListCollectionsResponse;
import org.openapitools.client.model.ListDatasetEntriesRequest;
import org.openapitools.client.model.ListDatasetEntriesResponse;
import org.openapitools.client.model.ListDatasetLabelsRequest;
import org.openapitools.client.model.ListDatasetLabelsResponse;
import org.openapitools.client.model.ListFacesRequest;
import org.openapitools.client.model.ListFacesResponse;
import org.openapitools.client.model.ListProjectPoliciesRequest;
import org.openapitools.client.model.ListProjectPoliciesResponse;
import org.openapitools.client.model.ListStreamProcessorsRequest;
import org.openapitools.client.model.ListStreamProcessorsResponse;
import org.openapitools.client.model.ListTagsForResourceRequest;
import org.openapitools.client.model.ListTagsForResourceResponse;
import org.openapitools.client.model.ListUsersRequest;
import org.openapitools.client.model.ListUsersResponse;
import org.openapitools.client.model.PutProjectPolicyRequest;
import org.openapitools.client.model.PutProjectPolicyResponse;
import org.openapitools.client.model.RecognizeCelebritiesRequest;
import org.openapitools.client.model.RecognizeCelebritiesResponse;
import org.openapitools.client.model.SearchFacesByImageRequest;
import org.openapitools.client.model.SearchFacesByImageResponse;
import org.openapitools.client.model.SearchFacesRequest;
import org.openapitools.client.model.SearchFacesResponse;
import org.openapitools.client.model.SearchUsersByImageRequest;
import org.openapitools.client.model.SearchUsersByImageResponse;
import org.openapitools.client.model.SearchUsersRequest;
import org.openapitools.client.model.SearchUsersResponse;
import org.openapitools.client.model.StartCelebrityRecognitionRequest;
import org.openapitools.client.model.StartCelebrityRecognitionResponse;
import org.openapitools.client.model.StartContentModerationRequest;
import org.openapitools.client.model.StartContentModerationResponse;
import org.openapitools.client.model.StartFaceDetectionRequest;
import org.openapitools.client.model.StartFaceDetectionResponse;
import org.openapitools.client.model.StartFaceSearchRequest;
import org.openapitools.client.model.StartFaceSearchResponse;
import org.openapitools.client.model.StartLabelDetectionRequest;
import org.openapitools.client.model.StartLabelDetectionResponse;
import org.openapitools.client.model.StartPersonTrackingRequest;
import org.openapitools.client.model.StartPersonTrackingResponse;
import org.openapitools.client.model.StartProjectVersionRequest;
import org.openapitools.client.model.StartProjectVersionResponse;
import org.openapitools.client.model.StartSegmentDetectionRequest;
import org.openapitools.client.model.StartSegmentDetectionResponse;
import org.openapitools.client.model.StartStreamProcessorRequest;
import org.openapitools.client.model.StartStreamProcessorResponse;
import org.openapitools.client.model.StartTextDetectionRequest;
import org.openapitools.client.model.StartTextDetectionResponse;
import org.openapitools.client.model.StopProjectVersionRequest;
import org.openapitools.client.model.StopProjectVersionResponse;
import org.openapitools.client.model.StopStreamProcessorRequest;
import org.openapitools.client.model.TagResourceRequest;
import org.openapitools.client.model.UntagResourceRequest;
import org.openapitools.client.model.UpdateDatasetEntriesRequest;
import org.openapitools.client.model.UpdateStreamProcessorRequest;
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
     * &lt;p&gt;Associates one or more faces with an existing UserID. Takes an array of &lt;code&gt;FaceIds&lt;/code&gt;. Each &lt;code&gt;FaceId&lt;/code&gt; that are present in the &lt;code&gt;FaceIds&lt;/code&gt; list is associated with the provided UserID. The maximum number of total &lt;code&gt;FaceIds&lt;/code&gt; per UserID is 100. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;UserMatchThreshold&lt;/code&gt; parameter specifies the minimum user match confidence required for the face to be associated with a UserID that has at least one &lt;code&gt;FaceID&lt;/code&gt; already associated. This ensures that the &lt;code&gt;FaceIds&lt;/code&gt; are associated with the right UserID. The value ranges from 0-100 and default value is 75. &lt;/p&gt; &lt;p&gt;If successful, an array of &lt;code&gt;AssociatedFace&lt;/code&gt; objects containing the associated &lt;code&gt;FaceIds&lt;/code&gt; is returned. If a given face is already associated with the given &lt;code&gt;UserID&lt;/code&gt;, it will be ignored and will not be returned in the response. If a given face is already associated to a different &lt;code&gt;UserID&lt;/code&gt;, isn&#39;t found in the collection, doesn’t meet the &lt;code&gt;UserMatchThreshold&lt;/code&gt;, or there are already 100 faces associated with the &lt;code&gt;UserID&lt;/code&gt;, it will be returned as part of an array of &lt;code&gt;UnsuccessfulFaceAssociations.&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The &lt;code&gt;UserStatus&lt;/code&gt; reflects the status of an operation which updates a UserID representation with a list of given faces. The &lt;code&gt;UserStatus&lt;/code&gt; can be: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;ACTIVE - All associations or disassociations of FaceID(s) for a UserID are complete.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CREATED - A UserID has been created, but has no FaceID(s) associated with it.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;UPDATING - A UserID is being updated and there are current associations or disassociations of FaceID(s) taking place.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void associateFacesTest() throws ApiException {
        String xAmzTarget = null;
        AssociateFacesRequest associateFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        AssociateFacesResponse response = api.associateFaces(xAmzTarget, associateFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Compares a face in the &lt;i&gt;source&lt;/i&gt; input image with each of the 100 largest faces detected in the &lt;i&gt;target&lt;/i&gt; input image. &lt;/p&gt; &lt;p&gt; If the source image contains multiple faces, the service detects the largest face and compares it with each face detected in the target image. &lt;/p&gt; &lt;note&gt; &lt;p&gt;CompareFaces uses machine learning algorithms, which are probabilistic. A false negative is an incorrect prediction that a face in the target image has a low similarity confidence score when compared to the face in the source image. To reduce the probability of false negatives, we recommend that you compare the target image against multiple source images. If you plan to use &lt;code&gt;CompareFaces&lt;/code&gt; to make a decision that impacts an individual&#39;s rights, privacy, or access to services, we recommend that you pass the result to a human for review and further validation before taking action.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You pass the input and target images either as base64-encoded image bytes or as references to images in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn&#39;t supported. The image must be formatted as a PNG or JPEG file. &lt;/p&gt; &lt;p&gt;In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, roll, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match. &lt;/p&gt; &lt;note&gt; &lt;p&gt;By default, only faces with a similarity score of greater than or equal to 80% are returned in the response. You can change this value by specifying the &lt;code&gt;SimilarityThreshold&lt;/code&gt; parameter.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;code&gt;CompareFaces&lt;/code&gt; also returns an array of faces that don&#39;t match the source image. For each face, it returns a bounding box, confidence value, landmarks, pose details, and quality. The response also returns information about the face in the source image, including the bounding box of the face and confidence value.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;QualityFilter&lt;/code&gt; input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. Use &lt;code&gt;QualityFilter&lt;/code&gt; to set the quality bar by specifying &lt;code&gt;LOW&lt;/code&gt;, &lt;code&gt;MEDIUM&lt;/code&gt;, or &lt;code&gt;HIGH&lt;/code&gt;. If you do not want to filter detected faces, specify &lt;code&gt;NONE&lt;/code&gt;. The default value is &lt;code&gt;NONE&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;If the image doesn&#39;t contain Exif metadata, &lt;code&gt;CompareFaces&lt;/code&gt; returns orientation information for the source and target images. Use these values to display the images with the correct image orientation.&lt;/p&gt; &lt;p&gt;If no faces are detected in the source or target images, &lt;code&gt;CompareFaces&lt;/code&gt; returns an &lt;code&gt;InvalidParameterException&lt;/code&gt; error. &lt;/p&gt; &lt;note&gt; &lt;p&gt; This is a stateless API operation. That is, data returned by this operation doesn&#39;t persist.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For an example, see Comparing Faces in Images in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:CompareFaces&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void compareFacesTest() throws ApiException {
        String xAmzTarget = null;
        CompareFacesRequest compareFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CompareFacesResponse response = api.compareFaces(xAmzTarget, compareFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Copies a version of an Amazon Rekognition Custom Labels model from a source project to a destination project. The source and destination projects can be in different AWS accounts but must be in the same AWS Region. You can&#39;t copy a model to another AWS service. &lt;/p&gt; &lt;p&gt;To copy a model version to a different AWS account, you need to create a resource-based policy known as a &lt;i&gt;project policy&lt;/i&gt;. You attach the project policy to the source project by calling &lt;a&gt;PutProjectPolicy&lt;/a&gt;. The project policy gives permission to copy the model version from a trusting AWS account to a trusted account.&lt;/p&gt; &lt;p&gt;For more information creating and attaching a project policy, see Attaching a project policy (SDK) in the &lt;i&gt;Amazon Rekognition Custom Labels Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;If you are copying a model version to a project in the same AWS account, you don&#39;t need to create a project policy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To copy a model, the destination project, source project, and source model version must already exist.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Copying a model version takes a while to complete. To get the current status, call &lt;a&gt;DescribeProjectVersions&lt;/a&gt; and check the value of &lt;code&gt;Status&lt;/code&gt; in the &lt;a&gt;ProjectVersionDescription&lt;/a&gt; object. The copy operation has finished when the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;COPYING_COMPLETED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:CopyProjectVersion&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void copyProjectVersionTest() throws ApiException {
        String xAmzTarget = null;
        CopyProjectVersionRequest copyProjectVersionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CopyProjectVersionResponse response = api.copyProjectVersion(xAmzTarget, copyProjectVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a collection in an AWS Region. You can add faces to the collection using the &lt;a&gt;IndexFaces&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;For example, you might create collections, one for each of your application users. A user can then index faces using the &lt;code&gt;IndexFaces&lt;/code&gt; operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container. &lt;/p&gt; &lt;p&gt;When you create a collection, it is associated with the latest version of the face model version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Collection names are case-sensitive.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:CreateCollection&lt;/code&gt; action. If you want to tag your collection, you also require permission to perform the &lt;code&gt;rekognition:TagResource&lt;/code&gt; operation.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createCollectionTest() throws ApiException {
        String xAmzTarget = null;
        CreateCollectionRequest createCollectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateCollectionResponse response = api.createCollection(xAmzTarget, createCollectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a new Amazon Rekognition Custom Labels dataset. You can create a dataset by using an Amazon Sagemaker format manifest file or by copying an existing Amazon Rekognition Custom Labels dataset.&lt;/p&gt; &lt;p&gt;To create a training dataset for a project, specify &lt;code&gt;TRAIN&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;. To create the test dataset for a project, specify &lt;code&gt;TEST&lt;/code&gt; for the value of &lt;code&gt;DatasetType&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;The response from &lt;code&gt;CreateDataset&lt;/code&gt; is the Amazon Resource Name (ARN) for the dataset. Creating a dataset takes a while to complete. Use &lt;a&gt;DescribeDataset&lt;/a&gt; to check the current status. The dataset created successfully if the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;CREATE_COMPLETE&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To check if any non-terminal errors occurred, call &lt;a&gt;ListDatasetEntries&lt;/a&gt; and check for the presence of &lt;code&gt;errors&lt;/code&gt; lists in the JSON Lines.&lt;/p&gt; &lt;p&gt;Dataset creation fails if a terminal error occurs (&lt;code&gt;Status&lt;/code&gt; &#x3D; &lt;code&gt;CREATE_FAILED&lt;/code&gt;). Currently, you can&#39;t access the terminal error information. &lt;/p&gt; &lt;p&gt;For more information, see Creating dataset in the &lt;i&gt;Amazon Rekognition Custom Labels Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:CreateDataset&lt;/code&gt; action. If you want to copy an existing dataset, you also require permission to perform the &lt;code&gt;rekognition:ListDatasetEntries&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createDatasetTest() throws ApiException {
        String xAmzTarget = null;
        CreateDatasetRequest createDatasetRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateDatasetResponse response = api.createDataset(xAmzTarget, createDatasetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;This API operation initiates a Face Liveness session. It returns a &lt;code&gt;SessionId&lt;/code&gt;, which you can use to start streaming Face Liveness video and get the results for a Face Liveness session. &lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;OutputConfig&lt;/code&gt; option in the Settings parameter to provide an Amazon S3 bucket location. The Amazon S3 bucket stores reference images and audit images. If no Amazon S3 bucket is defined, raw bytes are sent instead. &lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;AuditImagesLimit&lt;/code&gt; to limit the number of audit images returned when &lt;code&gt;GetFaceLivenessSessionResults&lt;/code&gt; is called. This number is between 0 and 4. By default, it is set to 0. The limit is best effort and based on the duration of the selfie-video. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createFaceLivenessSessionTest() throws ApiException {
        String xAmzTarget = null;
        CreateFaceLivenessSessionRequest createFaceLivenessSessionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateFaceLivenessSessionResponse response = api.createFaceLivenessSession(xAmzTarget, createFaceLivenessSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a new Amazon Rekognition Custom Labels project. A project is a group of resources (datasets, model versions) that you use to create and manage Amazon Rekognition Custom Labels models. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:CreateProject&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createProjectTest() throws ApiException {
        String xAmzTarget = null;
        CreateProjectRequest createProjectRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateProjectResponse response = api.createProject(xAmzTarget, createProjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a new version of a model and begins training. Models are managed as part of an Amazon Rekognition Custom Labels project. The response from &lt;code&gt;CreateProjectVersion&lt;/code&gt; is an Amazon Resource Name (ARN) for the version of the model. &lt;/p&gt; &lt;p&gt;Training uses the training and test datasets associated with the project. For more information, see Creating training and test dataset in the &lt;i&gt;Amazon Rekognition Custom Labels Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can train a model in a project that doesn&#39;t have associated datasets by specifying manifest files in the &lt;code&gt;TrainingData&lt;/code&gt; and &lt;code&gt;TestingData&lt;/code&gt; fields. &lt;/p&gt; &lt;p&gt;If you open the console after training a model with manifest files, Amazon Rekognition Custom Labels creates the datasets for you using the most recent manifest files. You can no longer train a model version for the project by specifying manifest files. &lt;/p&gt; &lt;p&gt;Instead of training with a project without associated datasets, we recommend that you use the manifest files to create training and test datasets for the project.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Training takes a while to complete. You can get the current status by calling &lt;a&gt;DescribeProjectVersions&lt;/a&gt;. Training completed successfully if the value of the &lt;code&gt;Status&lt;/code&gt; field is &lt;code&gt;TRAINING_COMPLETED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If training fails, see Debugging a failed model training in the &lt;i&gt;Amazon Rekognition Custom Labels&lt;/i&gt; developer guide. &lt;/p&gt; &lt;p&gt;Once training has successfully completed, call &lt;a&gt;DescribeProjectVersions&lt;/a&gt; to get the training results and evaluate the model. For more information, see Improving a trained Amazon Rekognition Custom Labels model in the &lt;i&gt;Amazon Rekognition Custom Labels&lt;/i&gt; developers guide. &lt;/p&gt; &lt;p&gt;After evaluating the model, you start the model by calling &lt;a&gt;StartProjectVersion&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:CreateProjectVersion&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createProjectVersionTest() throws ApiException {
        String xAmzTarget = null;
        CreateProjectVersionRequest createProjectVersionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateProjectVersionResponse response = api.createProjectVersion(xAmzTarget, createProjectVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates an Amazon Rekognition stream processor that you can use to detect and recognize faces or to detect labels in a streaming video.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams. There are two different settings for stream processors in Amazon Rekognition: detecting faces and detecting labels.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are creating a stream processor for detecting faces, you provide as input a Kinesis video stream (&lt;code&gt;Input&lt;/code&gt;) and a Kinesis data stream (&lt;code&gt;Output&lt;/code&gt;) stream for receiving the output. You must use the &lt;code&gt;FaceSearch&lt;/code&gt; option in &lt;code&gt;Settings&lt;/code&gt;, specifying the collection that contains the faces you want to recognize. After you have finished analyzing a streaming video, use &lt;a&gt;StopStreamProcessor&lt;/a&gt; to stop processing.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are creating a stream processor to detect labels, you provide as input a Kinesis video stream (&lt;code&gt;Input&lt;/code&gt;), Amazon S3 bucket information (&lt;code&gt;Output&lt;/code&gt;), and an Amazon SNS topic ARN (&lt;code&gt;NotificationChannel&lt;/code&gt;). You can also provide a KMS key ID to encrypt the data sent to your Amazon S3 bucket. You specify what you want to detect by using the &lt;code&gt;ConnectedHome&lt;/code&gt; option in settings, and selecting one of the following: &lt;code&gt;PERSON&lt;/code&gt;, &lt;code&gt;PET&lt;/code&gt;, &lt;code&gt;PACKAGE&lt;/code&gt;, &lt;code&gt;ALL&lt;/code&gt; You can also specify where in the frame you want Amazon Rekognition to monitor with &lt;code&gt;RegionsOfInterest&lt;/code&gt;. When you run the &lt;a&gt;StartStreamProcessor&lt;/a&gt; operation on a label detection stream processor, you input start and stop information to determine the length of the processing time.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; Use &lt;code&gt;Name&lt;/code&gt; to assign an identifier for the stream processor. You use &lt;code&gt;Name&lt;/code&gt; to manage the stream processor. For example, you can start processing the source video by calling &lt;a&gt;StartStreamProcessor&lt;/a&gt; with the &lt;code&gt;Name&lt;/code&gt; field. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:CreateStreamProcessor&lt;/code&gt; action. If you want to tag your stream processor, you also require permission to perform the &lt;code&gt;rekognition:TagResource&lt;/code&gt; operation.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createStreamProcessorTest() throws ApiException {
        String xAmzTarget = null;
        CreateStreamProcessorRequest createStreamProcessorRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateStreamProcessorResponse response = api.createStreamProcessor(xAmzTarget, createStreamProcessorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a new User within a collection specified by &lt;code&gt;CollectionId&lt;/code&gt;. Takes &lt;code&gt;UserId&lt;/code&gt; as a parameter, which is a user provided ID which should be unique within the collection. The provided &lt;code&gt;UserId&lt;/code&gt; will alias the system generated UUID to make the &lt;code&gt;UserId&lt;/code&gt; more user friendly. &lt;/p&gt; &lt;p&gt;Uses a &lt;code&gt;ClientToken&lt;/code&gt;, an idempotency token that ensures a call to &lt;code&gt;CreateUser&lt;/code&gt; completes only once. If the value is not supplied, the AWS SDK generates an idempotency token for the requests. This prevents retries after a network error results from making multiple &lt;code&gt;CreateUser&lt;/code&gt; calls. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createUserTest() throws ApiException {
        String xAmzTarget = null;
        CreateUserRequest createUserRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.createUser(xAmzTarget, createUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/dg/delete-collection-procedure.html\&quot;&gt;Deleting a collection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DeleteCollection&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteCollectionTest() throws ApiException {
        String xAmzTarget = null;
        DeleteCollectionRequest deleteCollectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteCollectionResponse response = api.deleteCollection(xAmzTarget, deleteCollectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes an existing Amazon Rekognition Custom Labels dataset. Deleting a dataset might take while. Use &lt;a&gt;DescribeDataset&lt;/a&gt; to check the current status. The dataset is still deleting if the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt;. If you try to access the dataset after it is deleted, you get a &lt;code&gt;ResourceNotFoundException&lt;/code&gt; exception. &lt;/p&gt; &lt;p&gt;You can&#39;t delete a dataset while it is creating (&lt;code&gt;Status&lt;/code&gt; &#x3D; &lt;code&gt;CREATE_IN_PROGRESS&lt;/code&gt;) or if the dataset is updating (&lt;code&gt;Status&lt;/code&gt; &#x3D; &lt;code&gt;UPDATE_IN_PROGRESS&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DeleteDataset&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDatasetTest() throws ApiException {
        String xAmzTarget = null;
        DeleteDatasetRequest deleteDatasetRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.deleteDataset(xAmzTarget, deleteDatasetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes faces from a collection. You specify a collection ID and an array of face IDs to remove from the collection.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DeleteFaces&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteFacesTest() throws ApiException {
        String xAmzTarget = null;
        DeleteFacesRequest deleteFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteFacesResponse response = api.deleteFaces(xAmzTarget, deleteFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes an Amazon Rekognition Custom Labels project. To delete a project you must first delete all models associated with the project. To delete a model, see &lt;a&gt;DeleteProjectVersion&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DeleteProject&lt;/code&gt; is an asynchronous operation. To check if the project is deleted, call &lt;a&gt;DescribeProjects&lt;/a&gt;. The project is deleted when the project no longer appears in the response. Be aware that deleting a given project will also delete any &lt;code&gt;ProjectPolicies&lt;/code&gt; associated with that project.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DeleteProject&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteProjectTest() throws ApiException {
        String xAmzTarget = null;
        DeleteProjectRequest deleteProjectRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteProjectResponse response = api.deleteProject(xAmzTarget, deleteProjectRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes an existing project policy.&lt;/p&gt; &lt;p&gt;To get a list of project policies attached to a project, call &lt;a&gt;ListProjectPolicies&lt;/a&gt;. To attach a project policy to a project, call &lt;a&gt;PutProjectPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DeleteProjectPolicy&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteProjectPolicyTest() throws ApiException {
        String xAmzTarget = null;
        DeleteProjectPolicyRequest deleteProjectPolicyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.deleteProjectPolicy(xAmzTarget, deleteProjectPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes an Amazon Rekognition Custom Labels model. &lt;/p&gt; &lt;p&gt;You can&#39;t delete a model if it is running or if it is training. To check the status of a model, use the &lt;code&gt;Status&lt;/code&gt; field returned from &lt;a&gt;DescribeProjectVersions&lt;/a&gt;. To stop a running model call &lt;a&gt;StopProjectVersion&lt;/a&gt;. If the model is training, wait until it finishes.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DeleteProjectVersion&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteProjectVersionTest() throws ApiException {
        String xAmzTarget = null;
        DeleteProjectVersionRequest deleteProjectVersionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteProjectVersionResponse response = api.deleteProjectVersion(xAmzTarget, deleteProjectVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes the stream processor identified by &lt;code&gt;Name&lt;/code&gt;. You assign the value for &lt;code&gt;Name&lt;/code&gt; when you create the stream processor with &lt;a&gt;CreateStreamProcessor&lt;/a&gt;. You might not be able to use the same name for a stream processor for a few seconds after calling &lt;code&gt;DeleteStreamProcessor&lt;/code&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteStreamProcessorTest() throws ApiException {
        String xAmzTarget = null;
        DeleteStreamProcessorRequest deleteStreamProcessorRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.deleteStreamProcessor(xAmzTarget, deleteStreamProcessorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes the specified UserID within the collection. Faces that are associated with the UserID are disassociated from the UserID before deleting the specified UserID. If the specified &lt;code&gt;Collection&lt;/code&gt; or &lt;code&gt;UserID&lt;/code&gt; is already deleted or not found, a &lt;code&gt;ResourceNotFoundException&lt;/code&gt; will be thrown. If the action is successful with a 200 response, an empty HTTP body is returned. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteUserTest() throws ApiException {
        String xAmzTarget = null;
        DeleteUserRequest deleteUserRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.deleteUser(xAmzTarget, deleteUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Describes the specified collection. You can use &lt;code&gt;DescribeCollection&lt;/code&gt; to get information, such as the number of faces indexed into a collection and the version of the model used by the collection for face detection.&lt;/p&gt; &lt;p&gt;For more information, see Describing a Collection in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeCollectionTest() throws ApiException {
        String xAmzTarget = null;
        DescribeCollectionRequest describeCollectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DescribeCollectionResponse response = api.describeCollection(xAmzTarget, describeCollectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Describes an Amazon Rekognition Custom Labels dataset. You can get information such as the current status of a dataset and statistics about the images and labels in a dataset. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DescribeDataset&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeDatasetTest() throws ApiException {
        String xAmzTarget = null;
        DescribeDatasetRequest describeDatasetRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DescribeDatasetResponse response = api.describeDataset(xAmzTarget, describeDatasetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Lists and describes the versions of a model in an Amazon Rekognition Custom Labels project. You can specify up to 10 model versions in &lt;code&gt;ProjectVersionArns&lt;/code&gt;. If you don&#39;t specify a value, descriptions for all model versions in the project are returned.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DescribeProjectVersions&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeProjectVersionsTest() throws ApiException {
        String xAmzTarget = null;
        DescribeProjectVersionsRequest describeProjectVersionsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        DescribeProjectVersionsResponse response = api.describeProjectVersions(xAmzTarget, describeProjectVersionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets information about your Amazon Rekognition Custom Labels projects. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DescribeProjects&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeProjectsTest() throws ApiException {
        String xAmzTarget = null;
        DescribeProjectsRequest describeProjectsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        DescribeProjectsResponse response = api.describeProjects(xAmzTarget, describeProjectsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Provides information about a stream processor created by &lt;a&gt;CreateStreamProcessor&lt;/a&gt;. You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void describeStreamProcessorTest() throws ApiException {
        String xAmzTarget = null;
        DescribeStreamProcessorRequest describeStreamProcessorRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DescribeStreamProcessorResponse response = api.describeStreamProcessor(xAmzTarget, describeStreamProcessorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Detects custom labels in a supplied image by using an Amazon Rekognition Custom Labels model. &lt;/p&gt; &lt;p&gt;You specify which version of a model version to use by using the &lt;code&gt;ProjectVersionArn&lt;/code&gt; input parameter. &lt;/p&gt; &lt;p&gt;You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. &lt;/p&gt; &lt;p&gt; For each object that the model version detects on an image, the API returns a (&lt;code&gt;CustomLabel&lt;/code&gt;) object in an array (&lt;code&gt;CustomLabels&lt;/code&gt;). Each &lt;code&gt;CustomLabel&lt;/code&gt; object provides the label name (&lt;code&gt;Name&lt;/code&gt;), the level of confidence that the image contains the object (&lt;code&gt;Confidence&lt;/code&gt;), and object location information, if it exists, for the label on the image (&lt;code&gt;Geometry&lt;/code&gt;). &lt;/p&gt; &lt;p&gt;To filter labels that are returned, specify a value for &lt;code&gt;MinConfidence&lt;/code&gt;. &lt;code&gt;DetectCustomLabelsLabels&lt;/code&gt; only returns labels with a confidence that&#39;s higher than the specified value. The value of &lt;code&gt;MinConfidence&lt;/code&gt; maps to the assumed threshold values created during training. For more information, see &lt;i&gt;Assumed threshold&lt;/i&gt; in the Amazon Rekognition Custom Labels Developer Guide. Amazon Rekognition Custom Labels metrics expresses an assumed threshold as a floating point value between 0-1. The range of &lt;code&gt;MinConfidence&lt;/code&gt; normalizes the threshold value to a percentage value (0-100). Confidence responses from &lt;code&gt;DetectCustomLabels&lt;/code&gt; are also returned as a percentage. You can use &lt;code&gt;MinConfidence&lt;/code&gt; to change the precision and recall or your model. For more information, see &lt;i&gt;Analyzing an image&lt;/i&gt; in the Amazon Rekognition Custom Labels Developer Guide. &lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for &lt;code&gt;MinConfidence&lt;/code&gt;, &lt;code&gt;DetectCustomLabels&lt;/code&gt; returns labels based on the assumed threshold of each label.&lt;/p&gt; &lt;p&gt;This is a stateless API operation. That is, the operation does not persist any data.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DetectCustomLabels&lt;/code&gt; action. &lt;/p&gt; &lt;p&gt;For more information, see &lt;i&gt;Analyzing an image&lt;/i&gt; in the Amazon Rekognition Custom Labels Developer Guide. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void detectCustomLabelsTest() throws ApiException {
        String xAmzTarget = null;
        DetectCustomLabelsRequest detectCustomLabelsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DetectCustomLabelsResponse response = api.detectCustomLabels(xAmzTarget, detectCustomLabelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Detects faces within an image that is provided as input.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectFaces&lt;/code&gt; detects the 100 largest faces in the image. For each face detected, the operation returns face details. These details include a bounding box of the face, a confidence value (that the bounding box contains a face), and a fixed set of attributes such as facial landmarks (for example, coordinates of eye and mouth), pose, presence of facial occlusion, and so on.&lt;/p&gt; &lt;p&gt;The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm might not detect the faces or might detect faces with lower confidence. &lt;/p&gt; &lt;p&gt;You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This is a stateless API operation. That is, the operation does not persist any data.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DetectFaces&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void detectFacesTest() throws ApiException {
        String xAmzTarget = null;
        DetectFacesRequest detectFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DetectFacesResponse response = api.detectFaces(xAmzTarget, detectFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Detects instances of real-world entities within an image (JPEG or PNG) provided as input. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature. &lt;/p&gt; &lt;p&gt;For an example, see Analyzing images stored in an Amazon S3 bucket in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Optional Parameters&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can specify one or both of the &lt;code&gt;GENERAL_LABELS&lt;/code&gt; and &lt;code&gt;IMAGE_PROPERTIES&lt;/code&gt; feature types when calling the DetectLabels API. Including &lt;code&gt;GENERAL_LABELS&lt;/code&gt; will ensure the response includes the labels detected in the input image, while including &lt;code&gt;IMAGE_PROPERTIES &lt;/code&gt;will ensure the response includes information about the image quality and color.&lt;/p&gt; &lt;p&gt;When using &lt;code&gt;GENERAL_LABELS&lt;/code&gt; and/or &lt;code&gt;IMAGE_PROPERTIES&lt;/code&gt; you can provide filtering criteria to the Settings parameter. You can filter with sets of individual labels or with label categories. You can specify inclusive filters, exclusive filters, or a combination of inclusive and exclusive filters. For more information on filtering see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html\&quot;&gt;Detecting Labels in an Image&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When getting labels, you can specify &lt;code&gt;MinConfidence&lt;/code&gt; to control the confidence threshold for the labels returned. The default is 55%. You can also add the &lt;code&gt;MaxLabels&lt;/code&gt; parameter to limit the number of labels returned. The default and upper limit is 1000 labels. These arguments are only valid when supplying GENERAL_LABELS as a feature type.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Response Elements&lt;/b&gt; &lt;/p&gt; &lt;p&gt; For each object, scene, and concept the API returns one or more labels. The API returns the following types of information about labels:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; Name - The name of the detected label. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Confidence - The level of confidence in the label assigned to a detected object. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Parents - The ancestor labels for a detected label. DetectLabels returns a hierarchical taxonomy of detected labels. For example, a detected car might be assigned the label car. The label car has two parent labels: Vehicle (its parent) and Transportation (its grandparent). The response includes the all ancestors for a label, where every ancestor is a unique label. In the previous example, Car, Vehicle, and Transportation are returned as unique labels in the response. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Aliases - Possible Aliases for the label. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Categories - The label categories that the detected label belongs to. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; BoundingBox — Bounding boxes are described for all instances of detected common object labels, returned in an array of Instance objects. An Instance object contains a BoundingBox object, describing the location of the label on the input image. It also includes the confidence for the accuracy of the detected bounding box. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; The API returns the following information regarding the image, as part of the ImageProperties structure:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Quality - Information about the Sharpness, Brightness, and Contrast of the input image, scored between 0 to 100. Image quality is returned for the entire image, as well as the background and the foreground. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Dominant Color - An array of the dominant colors in the image. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Foreground - Information about the sharpness, brightness, and dominant colors of the input image’s foreground. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Background - Information about the sharpness, brightness, and dominant colors of the input image’s background.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The list of returned labels will include at least one label for every detected object, along with information about that label. In the following example, suppose the input image has a lighthouse, the sea, and a rock. The response includes all three labels, one for each object, as well as the confidence in the label:&lt;/p&gt; &lt;p&gt; &lt;code&gt;{Name: lighthouse, Confidence: 98.4629}&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;{Name: rock,Confidence: 79.2097}&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; {Name: sea,Confidence: 75.061}&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The list of labels can include multiple labels for the same object. For example, if the input image shows a flower (for example, a tulip), the operation might return the following three labels. &lt;/p&gt; &lt;p&gt; &lt;code&gt;{Name: flower,Confidence: 99.0562}&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;{Name: plant,Confidence: 99.0562}&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;{Name: tulip,Confidence: 99.0562}&lt;/code&gt; &lt;/p&gt; &lt;p&gt;In this example, the detection algorithm more precisely identifies the flower as a tulip.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the object detected is a person, the operation doesn&#39;t provide the same facial details that the &lt;a&gt;DetectFaces&lt;/a&gt; operation provides.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This is a stateless API operation that doesn&#39;t return any data.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DetectLabels&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void detectLabelsTest() throws ApiException {
        String xAmzTarget = null;
        DetectLabelsRequest detectLabelsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DetectLabelsResponse response = api.detectLabels(xAmzTarget, detectLabelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Detects unsafe content in a specified JPEG or PNG format image. Use &lt;code&gt;DetectModerationLabels&lt;/code&gt; to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content.&lt;/p&gt; &lt;p&gt;To filter images, use the labels returned by &lt;code&gt;DetectModerationLabels&lt;/code&gt; to determine which types of content are appropriate.&lt;/p&gt; &lt;p&gt;For information about moderation labels, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void detectModerationLabelsTest() throws ApiException {
        String xAmzTarget = null;
        DetectModerationLabelsRequest detectModerationLabelsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DetectModerationLabelsResponse response = api.detectModerationLabels(xAmzTarget, detectModerationLabelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Detects Personal Protective Equipment (PPE) worn by people detected in an image. Amazon Rekognition can detect the following types of PPE.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Face cover&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Hand cover&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Head cover&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. The image must be either a PNG or JPG formatted file. &lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectProtectiveEquipment&lt;/code&gt; detects PPE worn by up to 15 persons detected in an image.&lt;/p&gt; &lt;p&gt;For each person detected in the image the API returns an array of body parts (face, head, left-hand, right-hand). For each body part, an array of detected items of PPE is returned, including an indicator of whether or not the PPE covers the body part. The API returns the confidence it has in each detection (person, PPE, body part and body part coverage). It also returns a bounding box (&lt;a&gt;BoundingBox&lt;/a&gt;) for each detected person and each detected item of PPE. &lt;/p&gt; &lt;p&gt;You can optionally request a summary of detected PPE items with the &lt;code&gt;SummarizationAttributes&lt;/code&gt; input parameter. The summary provides the following information. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The persons detected as wearing all of the types of PPE that you specify.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The persons detected as not wearing all of the types PPE that you specify.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The persons detected where PPE adornment could not be determined. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This is a stateless API operation. That is, the operation does not persist any data.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DetectProtectiveEquipment&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void detectProtectiveEquipmentTest() throws ApiException {
        String xAmzTarget = null;
        DetectProtectiveEquipmentRequest detectProtectiveEquipmentRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DetectProtectiveEquipmentResponse response = api.detectProtectiveEquipment(xAmzTarget, detectProtectiveEquipmentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Detects text in the input image and converts it into machine-readable text.&lt;/p&gt; &lt;p&gt;Pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image bytes is not supported. The image must be either a .png or .jpeg formatted file. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;DetectText&lt;/code&gt; operation returns text in an array of &lt;a&gt;TextDetection&lt;/a&gt; elements, &lt;code&gt;TextDetections&lt;/code&gt;. Each &lt;code&gt;TextDetection&lt;/code&gt; element provides information about a single word or line of text that was detected in the image. &lt;/p&gt; &lt;p&gt;A word is one or more script characters that are not separated by spaces. &lt;code&gt;DetectText&lt;/code&gt; can detect up to 100 words in an image.&lt;/p&gt; &lt;p&gt;A line is a string of equally spaced words. A line isn&#39;t necessarily a complete sentence. For example, a driver&#39;s license number is detected as a line. A line ends when there is no aligned text after it. Also, a line ends when there is a large gap between words, relative to the length of the words. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction. Periods don&#39;t represent the end of a line. If a sentence spans multiple lines, the &lt;code&gt;DetectText&lt;/code&gt; operation returns multiple lines.&lt;/p&gt; &lt;p&gt;To determine whether a &lt;code&gt;TextDetection&lt;/code&gt; element is a line of text or a word, use the &lt;code&gt;TextDetection&lt;/code&gt; object &lt;code&gt;Type&lt;/code&gt; field. &lt;/p&gt; &lt;p&gt;To be detected, text must be within +/- 90 degrees orientation of the horizontal axis.&lt;/p&gt; &lt;p&gt;For more information, see Detecting text in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void detectTextTest() throws ApiException {
        String xAmzTarget = null;
        DetectTextRequest detectTextRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DetectTextResponse response = api.detectText(xAmzTarget, detectTextRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Removes the association between a &lt;code&gt;Face&lt;/code&gt; supplied in an array of &lt;code&gt;FaceIds&lt;/code&gt; and the User. If the User is not present already, then a &lt;code&gt;ResourceNotFound&lt;/code&gt; exception is thrown. If successful, an array of faces that are disassociated from the User is returned. If a given face is already disassociated from the given UserID, it will be ignored and not be returned in the response. If a given face is already associated with a different User or not found in the collection it will be returned as part of &lt;code&gt;UnsuccessfulDisassociations&lt;/code&gt;. You can remove 1 - 100 face IDs from a user at one time.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disassociateFacesTest() throws ApiException {
        String xAmzTarget = null;
        DisassociateFacesRequest disassociateFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DisassociateFacesResponse response = api.disassociateFaces(xAmzTarget, disassociateFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Distributes the entries (images) in a training dataset across the training dataset and the test dataset for a project. &lt;code&gt;DistributeDatasetEntries&lt;/code&gt; moves 20% of the training dataset images to the test dataset. An entry is a JSON Line that describes an image. &lt;/p&gt; &lt;p&gt;You supply the Amazon Resource Names (ARN) of a project&#39;s training dataset and test dataset. The training dataset must contain the images that you want to split. The test dataset must be empty. The datasets must belong to the same project. To create training and test datasets for a project, call &lt;a&gt;CreateDataset&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Distributing a dataset takes a while to complete. To check the status call &lt;code&gt;DescribeDataset&lt;/code&gt;. The operation is complete when the &lt;code&gt;Status&lt;/code&gt; field for the training dataset and the test dataset is &lt;code&gt;UPDATE_COMPLETE&lt;/code&gt;. If the dataset split fails, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;UPDATE_FAILED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:DistributeDatasetEntries&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void distributeDatasetEntriesTest() throws ApiException {
        String xAmzTarget = null;
        DistributeDatasetEntriesRequest distributeDatasetEntriesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.distributeDatasetEntries(xAmzTarget, distributeDatasetEntriesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the name and additional information about a celebrity based on their Amazon Rekognition ID. The additional information is returned as an array of URLs. If there is no additional information about the celebrity, this list is empty.&lt;/p&gt; &lt;p&gt;For more information, see Getting information about a celebrity in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:GetCelebrityInfo&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCelebrityInfoTest() throws ApiException {
        String xAmzTarget = null;
        GetCelebrityInfoRequest getCelebrityInfoRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetCelebrityInfoResponse response = api.getCelebrityInfo(xAmzTarget, getCelebrityInfoRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the celebrity recognition results for a Amazon Rekognition Video analysis started by &lt;a&gt;StartCelebrityRecognition&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Celebrity recognition in a video is an asynchronous operation. Analysis is started by a call to &lt;a&gt;StartCelebrityRecognition&lt;/a&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). &lt;/p&gt; &lt;p&gt;When the celebrity recognition operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartCelebrityRecognition&lt;/code&gt;. To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetCelebrityDetection&lt;/code&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartCelebrityDetection&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For more information, see Working With Stored Videos in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetCelebrityRecognition&lt;/code&gt; returns detected celebrities and the time(s) they are detected in an array (&lt;code&gt;Celebrities&lt;/code&gt;) of &lt;a&gt;CelebrityRecognition&lt;/a&gt; objects. Each &lt;code&gt;CelebrityRecognition&lt;/code&gt; contains information about the celebrity in a &lt;a&gt;CelebrityDetail&lt;/a&gt; object and the time, &lt;code&gt;Timestamp&lt;/code&gt;, the celebrity was detected. This &lt;a&gt;CelebrityDetail&lt;/a&gt; object stores information about the detected celebrity&#39;s face attributes, a face bounding box, known gender, the celebrity&#39;s name, and a confidence estimate.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;GetCelebrityRecognition&lt;/code&gt; only returns the default facial attributes (&lt;code&gt;BoundingBox&lt;/code&gt;, &lt;code&gt;Confidence&lt;/code&gt;, &lt;code&gt;Landmarks&lt;/code&gt;, &lt;code&gt;Pose&lt;/code&gt;, and &lt;code&gt;Quality&lt;/code&gt;). The &lt;code&gt;BoundingBox&lt;/code&gt; field only applies to the detected face instance. The other facial attributes listed in the &lt;code&gt;Face&lt;/code&gt; object of the following response syntax are not returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;By default, the &lt;code&gt;Celebrities&lt;/code&gt; array is sorted by time (milliseconds from the start of the video). You can also sort the array by celebrity by specifying the value &lt;code&gt;ID&lt;/code&gt; in the &lt;code&gt;SortBy&lt;/code&gt; input parameter.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;CelebrityDetail&lt;/code&gt; object includes the celebrity identifer and additional information urls. If you don&#39;t store the additional information urls, you can get them later by calling &lt;a&gt;GetCelebrityInfo&lt;/a&gt; with the celebrity identifer.&lt;/p&gt; &lt;p&gt;No information is returned for faces not recognized as celebrities.&lt;/p&gt; &lt;p&gt;Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetCelebrityDetection&lt;/code&gt; and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value returned from the previous call to &lt;code&gt;GetCelebrityRecognition&lt;/code&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCelebrityRecognitionTest() throws ApiException {
        String xAmzTarget = null;
        GetCelebrityRecognitionRequest getCelebrityRecognitionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetCelebrityRecognitionResponse response = api.getCelebrityRecognition(xAmzTarget, getCelebrityRecognitionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the inappropriate, unwanted, or offensive content analysis results for a Amazon Rekognition Video analysis started by &lt;a&gt;StartContentModeration&lt;/a&gt;. For a list of moderation labels in Amazon Rekognition, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api\&quot;&gt;Using the image and video moderation APIs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video inappropriate or offensive content detection in a stored video is an asynchronous operation. You start analysis by calling &lt;a&gt;StartContentModeration&lt;/a&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When analysis finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartContentModeration&lt;/code&gt;. To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetContentModeration&lt;/code&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartContentModeration&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For more information, see Working with Stored Videos in the Amazon Rekognition Devlopers Guide.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetContentModeration&lt;/code&gt; returns detected inappropriate, unwanted, or offensive content moderation labels, and the time they are detected, in an array, &lt;code&gt;ModerationLabels&lt;/code&gt;, of &lt;a&gt;ContentModerationDetection&lt;/a&gt; objects. &lt;/p&gt; &lt;p&gt;By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying &lt;code&gt;NAME&lt;/code&gt; for the &lt;code&gt;SortBy&lt;/code&gt; input parameter. &lt;/p&gt; &lt;p&gt;Since video analysis can return a large number of results, use the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of labels returned in a single call to &lt;code&gt;GetContentModeration&lt;/code&gt;. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetContentModeration&lt;/code&gt; and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the value of &lt;code&gt;NextToken&lt;/code&gt; returned from the previous call to &lt;code&gt;GetContentModeration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see moderating content in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getContentModerationTest() throws ApiException {
        String xAmzTarget = null;
        GetContentModerationRequest getContentModerationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetContentModerationResponse response = api.getContentModeration(xAmzTarget, getContentModerationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets face detection results for a Amazon Rekognition Video analysis started by &lt;a&gt;StartFaceDetection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Face detection with Amazon Rekognition Video is an asynchronous operation. You start face detection by calling &lt;a&gt;StartFaceDetection&lt;/a&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the face detection operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartFaceDetection&lt;/code&gt;. To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetFaceDetection&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartFaceDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetFaceDetection&lt;/code&gt; returns an array of detected faces (&lt;code&gt;Faces&lt;/code&gt;) sorted by the time the faces were detected. &lt;/p&gt; &lt;p&gt;Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetFaceDetection&lt;/code&gt; and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value returned from the previous call to &lt;code&gt;GetFaceDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Note that for the &lt;code&gt;GetFaceDetection&lt;/code&gt; operation, the returned values for &lt;code&gt;FaceOccluded&lt;/code&gt; and &lt;code&gt;EyeDirection&lt;/code&gt; will always be \&quot;null\&quot;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getFaceDetectionTest() throws ApiException {
        String xAmzTarget = null;
        GetFaceDetectionRequest getFaceDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetFaceDetectionResponse response = api.getFaceDetection(xAmzTarget, getFaceDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Retrieves the results of a specific Face Liveness session. It requires the &lt;code&gt;sessionId&lt;/code&gt; as input, which was created using &lt;code&gt;CreateFaceLivenessSession&lt;/code&gt;. Returns the corresponding Face Liveness confidence score, a reference image that includes a face bounding box, and audit images that also contain face bounding boxes. The Face Liveness confidence score ranges from 0 to 100. &lt;/p&gt; &lt;p&gt;The number of audit images returned by &lt;code&gt;GetFaceLivenessSessionResults&lt;/code&gt; is defined by the &lt;code&gt;AuditImagesLimit&lt;/code&gt; paramater when calling &lt;code&gt;CreateFaceLivenessSession&lt;/code&gt;. Reference images are always returned when possible.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getFaceLivenessSessionResultsTest() throws ApiException {
        String xAmzTarget = null;
        GetFaceLivenessSessionResultsRequest getFaceLivenessSessionResultsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetFaceLivenessSessionResultsResponse response = api.getFaceLivenessSessionResults(xAmzTarget, getFaceLivenessSessionResultsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the face search results for Amazon Rekognition Video face search started by &lt;a&gt;StartFaceSearch&lt;/a&gt;. The search returns faces in a collection that match the faces of persons detected in a video. It also includes the time(s) that faces are matched in the video.&lt;/p&gt; &lt;p&gt;Face search in a video is an asynchronous operation. You start face search by calling to &lt;a&gt;StartFaceSearch&lt;/a&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the search operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartFaceSearch&lt;/code&gt;. To get the search results, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;code&gt;GetFaceSearch&lt;/code&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartFaceSearch&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see Searching Faces in a Collection in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;The search results are retured in an array, &lt;code&gt;Persons&lt;/code&gt;, of &lt;a&gt;PersonMatch&lt;/a&gt; objects. Each&lt;code&gt;PersonMatch&lt;/code&gt; element contains details about the matching faces in the input collection, person information (facial attributes, bounding boxes, and person identifer) for the matched person, and the time the person was matched in the video.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;GetFaceSearch&lt;/code&gt; only returns the default facial attributes (&lt;code&gt;BoundingBox&lt;/code&gt;, &lt;code&gt;Confidence&lt;/code&gt;, &lt;code&gt;Landmarks&lt;/code&gt;, &lt;code&gt;Pose&lt;/code&gt;, and &lt;code&gt;Quality&lt;/code&gt;). The other facial attributes listed in the &lt;code&gt;Face&lt;/code&gt; object of the following response syntax are not returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;By default, the &lt;code&gt;Persons&lt;/code&gt; array is sorted by the time, in milliseconds from the start of the video, persons are matched. You can also sort by persons by specifying &lt;code&gt;INDEX&lt;/code&gt; for the &lt;code&gt;SORTBY&lt;/code&gt; input parameter.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getFaceSearchTest() throws ApiException {
        String xAmzTarget = null;
        GetFaceSearchRequest getFaceSearchRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetFaceSearchResponse response = api.getFaceSearch(xAmzTarget, getFaceSearchRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the label detection results of a Amazon Rekognition Video analysis started by &lt;a&gt;StartLabelDetection&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;The label detection operation is started by a call to &lt;a&gt;StartLabelDetection&lt;/a&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the label detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartlabelDetection&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetLabelDetection&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLabelDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetLabelDetection&lt;/code&gt; returns an array of detected labels (&lt;code&gt;Labels&lt;/code&gt;) sorted by the time the labels were detected. You can also sort by the label name by specifying &lt;code&gt;NAME&lt;/code&gt; for the &lt;code&gt;SortBy&lt;/code&gt; input parameter. If there is no &lt;code&gt;NAME&lt;/code&gt; specified, the default sort is by timestamp.&lt;/p&gt; &lt;p&gt;You can select how results are aggregated by using the &lt;code&gt;AggregateBy&lt;/code&gt; input parameter. The default aggregation method is &lt;code&gt;TIMESTAMPS&lt;/code&gt;. You can also aggregate by &lt;code&gt;SEGMENTS&lt;/code&gt;, which aggregates all instances of labels detected in a given segment. &lt;/p&gt; &lt;p&gt;The returned Labels array may include the following attributes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Name - The name of the detected label.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Confidence - The level of confidence in the label assigned to a detected object. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Parents - The ancestor labels for a detected label. GetLabelDetection returns a hierarchical taxonomy of detected labels. For example, a detected car might be assigned the label car. The label car has two parent labels: Vehicle (its parent) and Transportation (its grandparent). The response includes the all ancestors for a label, where every ancestor is a unique label. In the previous example, Car, Vehicle, and Transportation are returned as unique labels in the response. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Aliases - Possible Aliases for the label. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Categories - The label categories that the detected label belongs to.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;BoundingBox — Bounding boxes are described for all instances of detected common object labels, returned in an array of Instance objects. An Instance object contains a BoundingBox object, describing the location of the label on the input image. It also includes the confidence for the accuracy of the detected bounding box.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Timestamp - Time, in milliseconds from the start of the video, that the label was detected. For aggregation by &lt;code&gt;SEGMENTS&lt;/code&gt;, the &lt;code&gt;StartTimestampMillis&lt;/code&gt;, &lt;code&gt;EndTimestampMillis&lt;/code&gt;, and &lt;code&gt;DurationMillis&lt;/code&gt; structures are what define a segment. Although the “Timestamp” structure is still returned with each label, its value is set to be the same as &lt;code&gt;StartTimestampMillis&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Timestamp and Bounding box information are returned for detected Instances, only if aggregation is done by &lt;code&gt;TIMESTAMPS&lt;/code&gt;. If aggregating by &lt;code&gt;SEGMENTS&lt;/code&gt;, information about detected instances isn’t returned. &lt;/p&gt; &lt;p&gt;The version of the label model used for the detection is also returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Note &lt;code&gt;DominantColors&lt;/code&gt; isn&#39;t returned for &lt;code&gt;Instances&lt;/code&gt;, although it is shown as part of the response in the sample seen below.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Use &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of labels returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetlabelDetection&lt;/code&gt; and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value returned from the previous call to &lt;code&gt;GetLabelDetection&lt;/code&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLabelDetectionTest() throws ApiException {
        String xAmzTarget = null;
        GetLabelDetectionRequest getLabelDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetLabelDetectionResponse response = api.getLabelDetection(xAmzTarget, getLabelDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the path tracking results of a Amazon Rekognition Video analysis started by &lt;a&gt;StartPersonTracking&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The person path tracking operation is started by a call to &lt;code&gt;StartPersonTracking&lt;/code&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartPersonTracking&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get the results of the person path tracking operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetPersonTracking&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartPersonTracking&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetPersonTracking&lt;/code&gt; returns an array, &lt;code&gt;Persons&lt;/code&gt;, of tracked persons and the time(s) their paths were tracked in the video. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;GetPersonTracking&lt;/code&gt; only returns the default facial attributes (&lt;code&gt;BoundingBox&lt;/code&gt;, &lt;code&gt;Confidence&lt;/code&gt;, &lt;code&gt;Landmarks&lt;/code&gt;, &lt;code&gt;Pose&lt;/code&gt;, and &lt;code&gt;Quality&lt;/code&gt;). The other facial attributes listed in the &lt;code&gt;Face&lt;/code&gt; object of the following response syntax are not returned. &lt;/p&gt; &lt;p&gt;For more information, see FaceDetail in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;By default, the array is sorted by the time(s) a person&#39;s path is tracked in the video. You can sort by tracked persons by specifying &lt;code&gt;INDEX&lt;/code&gt; for the &lt;code&gt;SortBy&lt;/code&gt; input parameter.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of items returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetPersonTracking&lt;/code&gt; and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value returned from the previous call to &lt;code&gt;GetPersonTracking&lt;/code&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonTrackingTest() throws ApiException {
        String xAmzTarget = null;
        GetPersonTrackingRequest getPersonTrackingRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetPersonTrackingResponse response = api.getPersonTracking(xAmzTarget, getPersonTrackingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the segment detection results of a Amazon Rekognition Video analysis started by &lt;a&gt;StartSegmentDetection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Segment detection with Amazon Rekognition Video is an asynchronous operation. You start segment detection by calling &lt;a&gt;StartSegmentDetection&lt;/a&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;). When the segment detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartSegmentDetection&lt;/code&gt;. To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. if so, call &lt;code&gt;GetSegmentDetection&lt;/code&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call of &lt;code&gt;StartSegmentDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetSegmentDetection&lt;/code&gt; returns detected segments in an array (&lt;code&gt;Segments&lt;/code&gt;) of &lt;a&gt;SegmentDetection&lt;/a&gt; objects. &lt;code&gt;Segments&lt;/code&gt; is sorted by the segment types specified in the &lt;code&gt;SegmentTypes&lt;/code&gt; input parameter of &lt;code&gt;StartSegmentDetection&lt;/code&gt;. Each element of the array includes the detected segment, the precentage confidence in the acuracy of the detected segment, the type of the segment, and the frame in which the segment was detected.&lt;/p&gt; &lt;p&gt;Use &lt;code&gt;SelectedSegmentTypes&lt;/code&gt; to find out the type of segment detection requested in the call to &lt;code&gt;StartSegmentDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of segment detections returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetSegmentDetection&lt;/code&gt; and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value returned from the previous call to &lt;code&gt;GetSegmentDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see Detecting video segments in stored video in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSegmentDetectionTest() throws ApiException {
        String xAmzTarget = null;
        GetSegmentDetectionRequest getSegmentDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetSegmentDetectionResponse response = api.getSegmentDetection(xAmzTarget, getSegmentDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets the text detection results of a Amazon Rekognition Video analysis started by &lt;a&gt;StartTextDetection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Text detection with Amazon Rekognition Video is an asynchronous operation. You start text detection by calling &lt;a&gt;StartTextDetection&lt;/a&gt; which returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) When the text detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to &lt;code&gt;StartTextDetection&lt;/code&gt;. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. if so, call &lt;code&gt;GetTextDetection&lt;/code&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call of &lt;code&gt;StartLabelDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetTextDetection&lt;/code&gt; returns an array of detected text (&lt;code&gt;TextDetections&lt;/code&gt;) sorted by the time the text was detected, up to 100 words per frame of video.&lt;/p&gt; &lt;p&gt;Each element of the array includes the detected text, the precentage confidence in the acuracy of the detected text, the time the text was detected, bounding box information for where the text was located, and unique identifiers for words and their lines.&lt;/p&gt; &lt;p&gt;Use MaxResults parameter to limit the number of text detections returned. If there are more results than specified in &lt;code&gt;MaxResults&lt;/code&gt;, the value of &lt;code&gt;NextToken&lt;/code&gt; in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call &lt;code&gt;GetTextDetection&lt;/code&gt; and populate the &lt;code&gt;NextToken&lt;/code&gt; request parameter with the token value returned from the previous call to &lt;code&gt;GetTextDetection&lt;/code&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTextDetectionTest() throws ApiException {
        String xAmzTarget = null;
        GetTextDetectionRequest getTextDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        GetTextDetectionResponse response = api.getTextDetection(xAmzTarget, getTextDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Detects faces in the input image and adds them to the specified collection. &lt;/p&gt; &lt;p&gt;Amazon Rekognition doesn&#39;t save the actual faces that are detected. Instead, the underlying detection algorithm first detects the faces in the input image. For each face, the algorithm extracts facial features into a feature vector, and stores it in the backend database. Amazon Rekognition uses feature vectors when it performs face match and search operations using the &lt;a&gt;SearchFaces&lt;/a&gt; and &lt;a&gt;SearchFacesByImage&lt;/a&gt; operations.&lt;/p&gt; &lt;p&gt;For more information, see Adding faces to a collection in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;To get the number of faces in a collection, call &lt;a&gt;DescribeCollection&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If you&#39;re using version 1.0 of the face detection model, &lt;code&gt;IndexFaces&lt;/code&gt; indexes the 15 largest faces in the input image. Later versions of the face detection model index the 100 largest faces in the input image. &lt;/p&gt; &lt;p&gt;If you&#39;re using version 4 or later of the face model, image orientation information is not returned in the &lt;code&gt;OrientationCorrection&lt;/code&gt; field. &lt;/p&gt; &lt;p&gt;To determine which version of the model you&#39;re using, call &lt;a&gt;DescribeCollection&lt;/a&gt; and supply the collection ID. You can also get the model version from the value of &lt;code&gt;FaceModelVersion&lt;/code&gt; in the response from &lt;code&gt;IndexFaces&lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information, see Model Versioning in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;If you provide the optional &lt;code&gt;ExternalImageId&lt;/code&gt; for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the &lt;a&gt;ListFaces&lt;/a&gt; operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image.&lt;/p&gt; &lt;p&gt;You can specify the maximum number of faces to index with the &lt;code&gt;MaxFaces&lt;/code&gt; input parameter. This is useful when you want to index the largest faces in an image and don&#39;t want to index smaller faces, such as those belonging to people standing in the background.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;QualityFilter&lt;/code&gt; input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. By default, &lt;code&gt;IndexFaces&lt;/code&gt; chooses the quality bar that&#39;s used to filter faces. You can also explicitly choose the quality bar. Use &lt;code&gt;QualityFilter&lt;/code&gt;, to set the quality bar by specifying &lt;code&gt;LOW&lt;/code&gt;, &lt;code&gt;MEDIUM&lt;/code&gt;, or &lt;code&gt;HIGH&lt;/code&gt;. If you do not want to filter detected faces, specify &lt;code&gt;NONE&lt;/code&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call &lt;a&gt;DescribeCollection&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Information about faces detected in an image, but not indexed, is returned in an array of &lt;a&gt;UnindexedFace&lt;/a&gt; objects, &lt;code&gt;UnindexedFaces&lt;/code&gt;. Faces aren&#39;t indexed for reasons such as:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The number of faces detected exceeds the value of the &lt;code&gt;MaxFaces&lt;/code&gt; request parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The face is too small compared to the image dimensions.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The face is too blurry.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The image is too dark.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The face has an extreme pose.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The face doesn’t have enough detail to be suitable for face search.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In response, the &lt;code&gt;IndexFaces&lt;/code&gt; operation returns an array of metadata for all detected faces, &lt;code&gt;FaceRecords&lt;/code&gt;. This includes: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The bounding box, &lt;code&gt;BoundingBox&lt;/code&gt;, of the detected face. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A confidence value, &lt;code&gt;Confidence&lt;/code&gt;, which indicates the confidence that the bounding box contains a face.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A face ID, &lt;code&gt;FaceId&lt;/code&gt;, assigned by the service for each face that&#39;s detected and stored.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An image ID, &lt;code&gt;ImageId&lt;/code&gt;, assigned by the service for the input image.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you request &lt;code&gt;ALL&lt;/code&gt; or specific facial attributes (e.g., &lt;code&gt;FACE_OCCLUDED&lt;/code&gt;) by using the detectionAttributes parameter, Amazon Rekognition returns detailed facial attributes, such as facial landmarks (for example, location of eye and mouth), facial occlusion, and other facial attributes.&lt;/p&gt; &lt;p&gt;If you provide the same image, specify the same collection, and use the same external ID in the &lt;code&gt;IndexFaces&lt;/code&gt; operation, Amazon Rekognition doesn&#39;t save duplicate face metadata.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;The input image is passed either as base64-encoded image bytes, or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn&#39;t supported. The image must be formatted as a PNG or JPEG file. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:IndexFaces&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void indexFacesTest() throws ApiException {
        String xAmzTarget = null;
        IndexFacesRequest indexFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        IndexFacesResponse response = api.indexFaces(xAmzTarget, indexFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns list of collection IDs in your account. If the result is truncated, the response also provides a &lt;code&gt;NextToken&lt;/code&gt; that you can use in the subsequent request to fetch the next set of collection IDs.&lt;/p&gt; &lt;p&gt;For an example, see Listing collections in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:ListCollections&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listCollectionsTest() throws ApiException {
        String xAmzTarget = null;
        ListCollectionsRequest listCollectionsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListCollectionsResponse response = api.listCollections(xAmzTarget, listCollectionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Lists the entries (images) within a dataset. An entry is a JSON Line that contains the information for a single image, including the image location, assigned labels, and object location bounding boxes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-manifest-files.html\&quot;&gt;Creating a manifest file&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;JSON Lines in the response include information about non-terminal errors found in the dataset. Non terminal errors are reported in &lt;code&gt;errors&lt;/code&gt; lists within each JSON Line. The same information is reported in the training and testing validation result manifests that Amazon Rekognition Custom Labels creates during model training. &lt;/p&gt; &lt;p&gt;You can filter the response in variety of ways, such as choosing which labels to return and returning JSON Lines created after a specific date. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:ListDatasetEntries&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listDatasetEntriesTest() throws ApiException {
        String xAmzTarget = null;
        ListDatasetEntriesRequest listDatasetEntriesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListDatasetEntriesResponse response = api.listDatasetEntries(xAmzTarget, listDatasetEntriesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Lists the labels in a dataset. Amazon Rekognition Custom Labels uses labels to describe images. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-labeling-images.html\&quot;&gt;Labeling images&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; Lists the labels in a dataset. Amazon Rekognition Custom Labels uses labels to describe images. For more information, see Labeling images in the &lt;i&gt;Amazon Rekognition Custom Labels Developer Guide&lt;/i&gt;. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listDatasetLabelsTest() throws ApiException {
        String xAmzTarget = null;
        ListDatasetLabelsRequest listDatasetLabelsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListDatasetLabelsResponse response = api.listDatasetLabels(xAmzTarget, listDatasetLabelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see Listing Faces in a Collection in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:ListFaces&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listFacesTest() throws ApiException {
        String xAmzTarget = null;
        ListFacesRequest listFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListFacesResponse response = api.listFaces(xAmzTarget, listFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Gets a list of the project policies attached to a project.&lt;/p&gt; &lt;p&gt;To attach a project policy to a project, call &lt;a&gt;PutProjectPolicy&lt;/a&gt;. To remove a project policy from a project, call &lt;a&gt;DeleteProjectPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:ListProjectPolicies&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listProjectPoliciesTest() throws ApiException {
        String xAmzTarget = null;
        ListProjectPoliciesRequest listProjectPoliciesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListProjectPoliciesResponse response = api.listProjectPolicies(xAmzTarget, listProjectPoliciesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets a list of stream processors that you have created with &lt;a&gt;CreateStreamProcessor&lt;/a&gt;. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listStreamProcessorsTest() throws ApiException {
        String xAmzTarget = null;
        ListStreamProcessorsRequest listStreamProcessorsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListStreamProcessorsResponse response = api.listStreamProcessors(xAmzTarget, listStreamProcessorsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Returns a list of tags in an Amazon Rekognition collection, stream processor, or Custom Labels model. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:ListTagsForResource&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTagsForResourceTest() throws ApiException {
        String xAmzTarget = null;
        ListTagsForResourceRequest listTagsForResourceRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        ListTagsForResourceResponse response = api.listTagsForResource(xAmzTarget, listTagsForResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Returns metadata of the User such as &lt;code&gt;UserID&lt;/code&gt; in the specified collection. Anonymous User (to reserve faces without any identity) is not returned as part of this request. The results are sorted by system generated primary key ID. If the response is truncated, &lt;code&gt;NextToken&lt;/code&gt; is returned in the response that can be used in the subsequent request to retrieve the next set of identities.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listUsersTest() throws ApiException {
        String xAmzTarget = null;
        ListUsersRequest listUsersRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListUsersResponse response = api.listUsers(xAmzTarget, listUsersRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Attaches a project policy to a Amazon Rekognition Custom Labels project in a trusting AWS account. A project policy specifies that a trusted AWS account can copy a model version from a trusting AWS account to a project in the trusted AWS account. To copy a model version you use the &lt;a&gt;CopyProjectVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;For more information about the format of a project policy document, see Attaching a project policy (SDK) in the &lt;i&gt;Amazon Rekognition Custom Labels Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;The response from &lt;code&gt;PutProjectPolicy&lt;/code&gt; is a revision ID for the project policy. You can attach multiple project policies to a project. You can also update an existing project policy by specifying the policy revision ID of the existing policy.&lt;/p&gt; &lt;p&gt;To remove a project policy from a project, call &lt;a&gt;DeleteProjectPolicy&lt;/a&gt;. To get a list of project policies attached to a project, call &lt;a&gt;ListProjectPolicies&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You copy a model version by calling &lt;a&gt;CopyProjectVersion&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:PutProjectPolicy&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putProjectPolicyTest() throws ApiException {
        String xAmzTarget = null;
        PutProjectPolicyRequest putProjectPolicyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        PutProjectPolicyResponse response = api.putProjectPolicy(xAmzTarget, putProjectPolicyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Returns an array of celebrities recognized in the input image. For more information, see Recognizing celebrities in the Amazon Rekognition Developer Guide. &lt;/p&gt; &lt;p&gt; &lt;code&gt;RecognizeCelebrities&lt;/code&gt; returns the 64 largest faces in the image. It lists the recognized celebrities in the &lt;code&gt;CelebrityFaces&lt;/code&gt; array and any unrecognized faces in the &lt;code&gt;UnrecognizedFaces&lt;/code&gt; array. &lt;code&gt;RecognizeCelebrities&lt;/code&gt; doesn&#39;t return celebrities whose faces aren&#39;t among the largest 64 faces in the image.&lt;/p&gt; &lt;p&gt;For each celebrity recognized, &lt;code&gt;RecognizeCelebrities&lt;/code&gt; returns a &lt;code&gt;Celebrity&lt;/code&gt; object. The &lt;code&gt;Celebrity&lt;/code&gt; object contains the celebrity name, ID, URL links to additional information, match confidence, and a &lt;code&gt;ComparedFace&lt;/code&gt; object that you can use to locate the celebrity&#39;s face on the image.&lt;/p&gt; &lt;p&gt;Amazon Rekognition doesn&#39;t retain information about which images a celebrity has been recognized in. Your application must store this information and use the &lt;code&gt;Celebrity&lt;/code&gt; ID property as a unique identifier for the celebrity. If you don&#39;t store the celebrity name or additional information URLs returned by &lt;code&gt;RecognizeCelebrities&lt;/code&gt;, you will need the ID to identify the celebrity in a call to the &lt;a&gt;GetCelebrityInfo&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. &lt;/p&gt; &lt;p&gt;For an example, see Recognizing celebrities in an image in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:RecognizeCelebrities&lt;/code&gt; operation.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void recognizeCelebritiesTest() throws ApiException {
        String xAmzTarget = null;
        RecognizeCelebritiesRequest recognizeCelebritiesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        RecognizeCelebritiesResponse response = api.recognizeCelebrities(xAmzTarget, recognizeCelebritiesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;For a given input face ID, searches for matching faces in the collection the face belongs to. You get a face ID when you add a face to the collection using the &lt;a&gt;IndexFaces&lt;/a&gt; operation. The operation compares the features of the input face with faces in the specified collection. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can also search faces without indexing faces by using the &lt;code&gt;SearchFacesByImage&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match that is found. Along with the metadata, the response also includes a &lt;code&gt;confidence&lt;/code&gt; value for each face match, indicating the confidence that the specific face matches the input face. &lt;/p&gt; &lt;p&gt;For an example, see Searching for a face using its face ID in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:SearchFaces&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void searchFacesTest() throws ApiException {
        String xAmzTarget = null;
        SearchFacesRequest searchFacesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        SearchFacesResponse response = api.searchFaces(xAmzTarget, searchFacesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection. &lt;/p&gt; &lt;note&gt; &lt;p&gt;To search for all faces in an input image, you might first call the &lt;a&gt;IndexFaces&lt;/a&gt; operation, and then use the face IDs returned in subsequent calls to the &lt;a&gt;SearchFaces&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt; You can also call the &lt;code&gt;DetectFaces&lt;/code&gt; operation and use the bounding boxes in the response to make face crops, which then you can pass in to the &lt;code&gt;SearchFacesByImage&lt;/code&gt; operation. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. &lt;/p&gt; &lt;p&gt; The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a &lt;code&gt;similarity&lt;/code&gt; indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image. &lt;/p&gt; &lt;p&gt;If no faces are detected in the input image, &lt;code&gt;SearchFacesByImage&lt;/code&gt; returns an &lt;code&gt;InvalidParameterException&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt;For an example, Searching for a Face Using an Image in the Amazon Rekognition Developer Guide.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;QualityFilter&lt;/code&gt; input parameter allows you to filter out detected faces that don’t meet a required quality bar. The quality bar is based on a variety of common use cases. Use &lt;code&gt;QualityFilter&lt;/code&gt; to set the quality bar for filtering by specifying &lt;code&gt;LOW&lt;/code&gt;, &lt;code&gt;MEDIUM&lt;/code&gt;, or &lt;code&gt;HIGH&lt;/code&gt;. If you do not want to filter detected faces, specify &lt;code&gt;NONE&lt;/code&gt;. The default value is &lt;code&gt;NONE&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use quality filtering, you need a collection associated with version 3 of the face model or higher. To get the version of the face model associated with a collection, call &lt;a&gt;DescribeCollection&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:SearchFacesByImage&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void searchFacesByImageTest() throws ApiException {
        String xAmzTarget = null;
        SearchFacesByImageRequest searchFacesByImageRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        SearchFacesByImageResponse response = api.searchFacesByImage(xAmzTarget, searchFacesByImageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Searches for UserIDs within a collection based on a &lt;code&gt;FaceId&lt;/code&gt; or &lt;code&gt;UserId&lt;/code&gt;. This API can be used to find the closest UserID (with a highest similarity) to associate a face. The request must be provided with either &lt;code&gt;FaceId&lt;/code&gt; or &lt;code&gt;UserId&lt;/code&gt;. The operation returns an array of UserID that match the &lt;code&gt;FaceId&lt;/code&gt; or &lt;code&gt;UserId&lt;/code&gt;, ordered by similarity score with the highest similarity first. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void searchUsersTest() throws ApiException {
        String xAmzTarget = null;
        SearchUsersRequest searchUsersRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        SearchUsersResponse response = api.searchUsers(xAmzTarget, searchUsersRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Searches for UserIDs using a supplied image. It first detects the largest face in the image, and then searches a specified collection for matching UserIDs. &lt;/p&gt; &lt;p&gt;The operation returns an array of UserIDs that match the face in the supplied image, ordered by similarity score with the highest similarity first. It also returns a bounding box for the face found in the input image. &lt;/p&gt; &lt;p&gt;Information about faces detected in the supplied image, but not used for the search, is returned in an array of &lt;code&gt;UnsearchedFace&lt;/code&gt; objects. If no valid face is detected in the image, the response will contain an empty &lt;code&gt;UserMatches&lt;/code&gt; list and no &lt;code&gt;SearchedFace&lt;/code&gt; object. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void searchUsersByImageTest() throws ApiException {
        String xAmzTarget = null;
        SearchUsersByImageRequest searchUsersByImageRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        SearchUsersByImageResponse response = api.searchUsersByImage(xAmzTarget, searchUsersByImageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts asynchronous recognition of celebrities in a stored video.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video can detect celebrities in a video must be stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartCelebrityRecognition&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) which you use to get the results of the analysis. When celebrity recognition analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetCelebrityRecognition&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartCelebrityRecognition&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For more information, see Recognizing celebrities in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startCelebrityRecognitionTest() throws ApiException {
        String xAmzTarget = null;
        StartCelebrityRecognitionRequest startCelebrityRecognitionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartCelebrityRecognitionResponse response = api.startCelebrityRecognition(xAmzTarget, startCelebrityRecognitionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Starts asynchronous detection of inappropriate, unwanted, or offensive content in a stored video. For a list of moderation labels in Amazon Rekognition, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api\&quot;&gt;Using the image and video moderation APIs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartContentModeration&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) which you use to get the results of the analysis. When content analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetContentModeration&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartContentModeration&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For more information, see Moderating content in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startContentModerationTest() throws ApiException {
        String xAmzTarget = null;
        StartContentModerationRequest startContentModerationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartContentModerationResponse response = api.startContentModeration(xAmzTarget, startContentModerationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts asynchronous detection of faces in a stored video.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video can detect faces in a video stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartFaceDetection&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) that you use to get the results of the operation. When face detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetFaceDetection&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartFaceDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see Detecting faces in a stored video in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startFaceDetectionTest() throws ApiException {
        String xAmzTarget = null;
        StartFaceDetectionRequest startFaceDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartFaceDetectionResponse response = api.startFaceDetection(xAmzTarget, startFaceDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts the asynchronous search for faces in a collection that match the faces of persons detected in a stored video.&lt;/p&gt; &lt;p&gt;The video must be stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartFaceSearch&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) which you use to get the search results once the search has completed. When searching is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. To get the search results, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetFaceSearch&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartFaceSearch&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/dg/procedure-person-search-videos.html\&quot;&gt;Searching stored videos for faces&lt;/a&gt;. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startFaceSearchTest() throws ApiException {
        String xAmzTarget = null;
        StartFaceSearchRequest startFaceSearchRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartFaceSearchResponse response = api.startFaceSearch(xAmzTarget, startFaceSearchRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts asynchronous detection of labels in a stored video.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video can detect labels in a video. Labels are instances of real-world entities. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; concepts like landscape, evening, and nature; and activities like a person getting out of a car or a person skiing.&lt;/p&gt; &lt;p&gt;The video must be stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartLabelDetection&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetLabelDetection&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartLabelDetection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Optional Parameters&lt;/i&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartLabelDetection&lt;/code&gt; has the &lt;code&gt;GENERAL_LABELS&lt;/code&gt; Feature applied by default. This feature allows you to provide filtering criteria to the &lt;code&gt;Settings&lt;/code&gt; parameter. You can filter with sets of individual labels or with label categories. You can specify inclusive filters, exclusive filters, or a combination of inclusive and exclusive filters. For more information on filtering, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-labels-video.html\&quot;&gt;Detecting labels in a video&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;MinConfidence&lt;/code&gt; to control the confidence threshold for the labels returned. The default is 50.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startLabelDetectionTest() throws ApiException {
        String xAmzTarget = null;
        StartLabelDetectionRequest startLabelDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartLabelDetectionResponse response = api.startLabelDetection(xAmzTarget, startLabelDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts the asynchronous tracking of a person&#39;s path in a stored video.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video can track the path of people in a video stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartPersonTracking&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get the results of the person detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. If so, call &lt;a&gt;GetPersonTracking&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartPersonTracking&lt;/code&gt;.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startPersonTrackingTest() throws ApiException {
        String xAmzTarget = null;
        StartPersonTrackingRequest startPersonTrackingRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartPersonTrackingResponse response = api.startPersonTracking(xAmzTarget, startPersonTrackingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts the running of the version of a model. Starting a model takes a while to complete. To check the current state of the model, use &lt;a&gt;DescribeProjectVersions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Once the model is running, you can detect custom labels in new images by calling &lt;a&gt;DetectCustomLabels&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You are charged for the amount of time that the model is running. To stop a running model, call &lt;a&gt;StopProjectVersion&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information, see &lt;i&gt;Running a trained Amazon Rekognition Custom Labels model&lt;/i&gt; in the Amazon Rekognition Custom Labels Guide.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:StartProjectVersion&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startProjectVersionTest() throws ApiException {
        String xAmzTarget = null;
        StartProjectVersionRequest startProjectVersionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartProjectVersionResponse response = api.startProjectVersion(xAmzTarget, startProjectVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts asynchronous detection of segment detection in a stored video.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video can detect segments in a video stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartSegmentDetection&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) which you use to get the results of the operation. When segment detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;Filters&lt;/code&gt; (&lt;a&gt;StartSegmentDetectionFilters&lt;/a&gt;) input parameter to specify the minimum detection confidence returned in the response. Within &lt;code&gt;Filters&lt;/code&gt;, use &lt;code&gt;ShotFilter&lt;/code&gt; (&lt;a&gt;StartShotDetectionFilter&lt;/a&gt;) to filter detected shots. Use &lt;code&gt;TechnicalCueFilter&lt;/code&gt; (&lt;a&gt;StartTechnicalCueDetectionFilter&lt;/a&gt;) to filter technical cues. &lt;/p&gt; &lt;p&gt;To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. if so, call &lt;a&gt;GetSegmentDetection&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartSegmentDetection&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For more information, see Detecting video segments in stored video in the Amazon Rekognition Developer Guide.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startSegmentDetectionTest() throws ApiException {
        String xAmzTarget = null;
        StartSegmentDetectionRequest startSegmentDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartSegmentDetectionResponse response = api.startSegmentDetection(xAmzTarget, startSegmentDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts processing a stream processor. You create a stream processor by calling &lt;a&gt;CreateStreamProcessor&lt;/a&gt;. To tell &lt;code&gt;StartStreamProcessor&lt;/code&gt; which stream processor to start, use the value of the &lt;code&gt;Name&lt;/code&gt; field specified in the call to &lt;code&gt;CreateStreamProcessor&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you are using a label detection stream processor to detect labels, you need to provide a &lt;code&gt;Start selector&lt;/code&gt; and a &lt;code&gt;Stop selector&lt;/code&gt; to determine the length of the stream processing time.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startStreamProcessorTest() throws ApiException {
        String xAmzTarget = null;
        StartStreamProcessorRequest startStreamProcessorRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartStreamProcessorResponse response = api.startStreamProcessor(xAmzTarget, startStreamProcessorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Starts asynchronous detection of text in a stored video.&lt;/p&gt; &lt;p&gt;Amazon Rekognition Video can detect text in a video stored in an Amazon S3 bucket. Use &lt;a&gt;Video&lt;/a&gt; to specify the bucket name and the filename of the video. &lt;code&gt;StartTextDetection&lt;/code&gt; returns a job identifier (&lt;code&gt;JobId&lt;/code&gt;) which you use to get the results of the operation. When text detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in &lt;code&gt;NotificationChannel&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is &lt;code&gt;SUCCEEDED&lt;/code&gt;. if so, call &lt;a&gt;GetTextDetection&lt;/a&gt; and pass the job identifier (&lt;code&gt;JobId&lt;/code&gt;) from the initial call to &lt;code&gt;StartTextDetection&lt;/code&gt;. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startTextDetectionTest() throws ApiException {
        String xAmzTarget = null;
        StartTextDetectionRequest startTextDetectionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StartTextDetectionResponse response = api.startTextDetection(xAmzTarget, startTextDetectionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Stops a running model. The operation might take a while to complete. To check the current status, call &lt;a&gt;DescribeProjectVersions&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:StopProjectVersion&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopProjectVersionTest() throws ApiException {
        String xAmzTarget = null;
        StopProjectVersionRequest stopProjectVersionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        StopProjectVersionResponse response = api.stopProjectVersion(xAmzTarget, stopProjectVersionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Stops a running stream processor that was created by &lt;a&gt;CreateStreamProcessor&lt;/a&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopStreamProcessorTest() throws ApiException {
        String xAmzTarget = null;
        StopStreamProcessorRequest stopStreamProcessorRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.stopStreamProcessor(xAmzTarget, stopStreamProcessorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Adds one or more key-value tags to an Amazon Rekognition collection, stream processor, or Custom Labels model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:TagResource&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tagResourceTest() throws ApiException {
        String xAmzTarget = null;
        TagResourceRequest tagResourceRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.tagResource(xAmzTarget, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt; Removes one or more tags from an Amazon Rekognition collection, stream processor, or Custom Labels model. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:UntagResource&lt;/code&gt; action. &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void untagResourceTest() throws ApiException {
        String xAmzTarget = null;
        UntagResourceRequest untagResourceRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.untagResource(xAmzTarget, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Adds or updates one or more entries (images) in a dataset. An entry is a JSON Line which contains the information for a single image, including the image location, assigned labels, and object location bounding boxes. For more information, see Image-Level labels in manifest files and Object localization in manifest files in the &lt;i&gt;Amazon Rekognition Custom Labels Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;If the &lt;code&gt;source-ref&lt;/code&gt; field in the JSON line references an existing image, the existing image in the dataset is updated. If &lt;code&gt;source-ref&lt;/code&gt; field doesn&#39;t reference an existing image, the image is added as a new image to the dataset. &lt;/p&gt; &lt;p&gt;You specify the changes that you want to make in the &lt;code&gt;Changes&lt;/code&gt; input parameter. There isn&#39;t a limit to the number JSON Lines that you can change, but the size of &lt;code&gt;Changes&lt;/code&gt; must be less than 5MB.&lt;/p&gt; &lt;p&gt; &lt;code&gt;UpdateDatasetEntries&lt;/code&gt; returns immediatly, but the dataset update might take a while to complete. Use &lt;a&gt;DescribeDataset&lt;/a&gt; to check the current status. The dataset updated successfully if the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;UPDATE_COMPLETE&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To check if any non-terminal errors occured, call &lt;a&gt;ListDatasetEntries&lt;/a&gt; and check for the presence of &lt;code&gt;errors&lt;/code&gt; lists in the JSON Lines.&lt;/p&gt; &lt;p&gt;Dataset update fails if a terminal error occurs (&lt;code&gt;Status&lt;/code&gt; &#x3D; &lt;code&gt;UPDATE_FAILED&lt;/code&gt;). Currently, you can&#39;t access the terminal error information from the Amazon Rekognition Custom Labels SDK. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;rekognition:UpdateDatasetEntries&lt;/code&gt; action.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateDatasetEntriesTest() throws ApiException {
        String xAmzTarget = null;
        UpdateDatasetEntriesRequest updateDatasetEntriesRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.updateDatasetEntries(xAmzTarget, updateDatasetEntriesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     *  Allows you to update a stream processor. You can change some settings and regions of interest and delete certain parameters. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateStreamProcessorTest() throws ApiException {
        String xAmzTarget = null;
        UpdateStreamProcessorRequest updateStreamProcessorRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.updateStreamProcessor(xAmzTarget, updateStreamProcessorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

}
