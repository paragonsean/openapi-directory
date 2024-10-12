# coding: utf-8

# import models into model package
from openapi_server.models.bounding_box import BoundingBox
from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.domain import Domain
from openapi_server.models.export import Export
from openapi_server.models.image import Image
from openapi_server.models.image_create_result import ImageCreateResult
from openapi_server.models.image_create_summary import ImageCreateSummary
from openapi_server.models.image_file_create_batch import ImageFileCreateBatch
from openapi_server.models.image_file_create_entry import ImageFileCreateEntry
from openapi_server.models.image_id_create_batch import ImageIdCreateBatch
from openapi_server.models.image_id_create_entry import ImageIdCreateEntry
from openapi_server.models.image_performance import ImagePerformance
from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_processing_settings import ImageProcessingSettings
from openapi_server.models.image_region import ImageRegion
from openapi_server.models.image_region_create_batch import ImageRegionCreateBatch
from openapi_server.models.image_region_create_entry import ImageRegionCreateEntry
from openapi_server.models.image_region_create_result import ImageRegionCreateResult
from openapi_server.models.image_region_create_summary import ImageRegionCreateSummary
from openapi_server.models.image_region_proposal import ImageRegionProposal
from openapi_server.models.image_tag import ImageTag
from openapi_server.models.image_tag_create_batch import ImageTagCreateBatch
from openapi_server.models.image_tag_create_entry import ImageTagCreateEntry
from openapi_server.models.image_tag_create_summary import ImageTagCreateSummary
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.image_url_create_batch import ImageUrlCreateBatch
from openapi_server.models.image_url_create_entry import ImageUrlCreateEntry
from openapi_server.models.iteration import Iteration
from openapi_server.models.iteration_performance import IterationPerformance
from openapi_server.models.prediction import Prediction
from openapi_server.models.prediction_query_result import PredictionQueryResult
from openapi_server.models.prediction_query_tag import PredictionQueryTag
from openapi_server.models.prediction_query_token import PredictionQueryToken
from openapi_server.models.project import Project
from openapi_server.models.project_settings import ProjectSettings
from openapi_server.models.region import Region
from openapi_server.models.region_proposal import RegionProposal
from openapi_server.models.stored_image_prediction import StoredImagePrediction
from openapi_server.models.stored_suggested_tag_and_region import StoredSuggestedTagAndRegion
from openapi_server.models.suggested_tag_and_region import SuggestedTagAndRegion
from openapi_server.models.suggested_tag_and_region_query import SuggestedTagAndRegionQuery
from openapi_server.models.suggested_tag_and_region_query_token import SuggestedTagAndRegionQueryToken
from openapi_server.models.tag import Tag
from openapi_server.models.tag_filter import TagFilter
from openapi_server.models.tag_performance import TagPerformance
