from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_get_record_request import BatchGetRecordRequest
from openapi_server.models.batch_get_record_response import BatchGetRecordResponse
from openapi_server.models.get_record_response import GetRecordResponse
from openapi_server.models.put_record_request import PutRecordRequest
from openapi_server.models.target_store import TargetStore
from openapi_server import util


async def batch_get_record(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_record

    Retrieves a batch of &lt;code&gt;Records&lt;/code&gt; from a &lt;code&gt;FeatureGroup&lt;/code&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchGetRecordRequest.from_dict(body)
    return web.Response(status=200)


async def delete_record(request: web.Request, feature_group_name, record_identifier_value_as_string, event_time, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, target_stores=None, deletion_mode=None) -> web.Response:
    """delete_record

    &lt;p&gt;Deletes a &lt;code&gt;Record&lt;/code&gt; from a &lt;code&gt;FeatureGroup&lt;/code&gt; in the &lt;code&gt;OnlineStore&lt;/code&gt;. Feature Store supports both &lt;code&gt;SoftDelete&lt;/code&gt; and &lt;code&gt;HardDelete&lt;/code&gt;. For &lt;code&gt;SoftDelete&lt;/code&gt; (default), feature columns are set to &lt;code&gt;null&lt;/code&gt; and the record is no longer retrievable by &lt;code&gt;GetRecord&lt;/code&gt; or &lt;code&gt;BatchGetRecord&lt;/code&gt;. For &lt;code&gt;HardDelete&lt;/code&gt;, the complete &lt;code&gt;Record&lt;/code&gt; is removed from the &lt;code&gt;OnlineStore&lt;/code&gt;. In both cases, Feature Store appends the deleted record marker to the &lt;code&gt;OfflineStore&lt;/code&gt; with feature values set to &lt;code&gt;null&lt;/code&gt;, &lt;code&gt;is_deleted&lt;/code&gt; value set to &lt;code&gt;True&lt;/code&gt;, and &lt;code&gt;EventTime&lt;/code&gt; set to the delete input &lt;code&gt;EventTime&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Note that the &lt;code&gt;EventTime&lt;/code&gt; specified in &lt;code&gt;DeleteRecord&lt;/code&gt; should be set later than the &lt;code&gt;EventTime&lt;/code&gt; of the existing record in the &lt;code&gt;OnlineStore&lt;/code&gt; for that &lt;code&gt;RecordIdentifer&lt;/code&gt;. If it is not, the deletion does not occur:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;SoftDelete&lt;/code&gt;, the existing (undeleted) record remains in the &lt;code&gt;OnlineStore&lt;/code&gt;, though the delete record marker is still written to the &lt;code&gt;OfflineStore&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HardDelete&lt;/code&gt; returns &lt;code&gt;EventTime&lt;/code&gt;: &lt;code&gt;400 ValidationException&lt;/code&gt; to indicate that the delete operation failed. No delete record marker is written to the &lt;code&gt;OfflineStore&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param feature_group_name: The name or Amazon Resource Name (ARN) of the feature group to delete the record from. 
    :type feature_group_name: str
    :param record_identifier_value_as_string: The value for the &lt;code&gt;RecordIdentifier&lt;/code&gt; that uniquely identifies the record, in string format. 
    :type record_identifier_value_as_string: str
    :param event_time: Timestamp indicating when the deletion event occurred. &lt;code&gt;EventTime&lt;/code&gt; can be used to query data at a certain point in time.
    :type event_time: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param target_stores: A list of stores from which you&#39;re deleting the record. By default, Feature Store deletes the record from all of the stores that you&#39;re using for the &lt;code&gt;FeatureGroup&lt;/code&gt;.
    :type target_stores: list | bytes
    :param deletion_mode: The name of the deletion mode for deleting the record. By default, the deletion mode is set to &lt;code&gt;SoftDelete&lt;/code&gt;.
    :type deletion_mode: str

    """
    target_stores = [TargetStore.from_dict(d) for d in target_stores]
    return web.Response(status=200)


async def get_record(request: web.Request, feature_group_name, record_identifier_value_as_string, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, feature_name=None, expiration_time_response=None) -> web.Response:
    """get_record

    Use for &lt;code&gt;OnlineStore&lt;/code&gt; serving from a &lt;code&gt;FeatureStore&lt;/code&gt;. Only the latest records stored in the &lt;code&gt;OnlineStore&lt;/code&gt; can be retrieved. If no Record with &lt;code&gt;RecordIdentifierValue&lt;/code&gt; is found, then an empty result is returned. 

    :param feature_group_name: The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record.
    :type feature_group_name: str
    :param record_identifier_value_as_string: The value that corresponds to &lt;code&gt;RecordIdentifier&lt;/code&gt; type and uniquely identifies the record in the &lt;code&gt;FeatureGroup&lt;/code&gt;. 
    :type record_identifier_value_as_string: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param feature_name: List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.
    :type feature_name: List[str]
    :param expiration_time_response: Parameter to request &lt;code&gt;ExpiresAt&lt;/code&gt; in response. If &lt;code&gt;Enabled&lt;/code&gt;, &lt;code&gt;GetRecord&lt;/code&gt; will return the value of &lt;code&gt;ExpiresAt&lt;/code&gt;, if it is not null. If &lt;code&gt;Disabled&lt;/code&gt; and null, &lt;code&gt;GetRecord&lt;/code&gt; will return null.
    :type expiration_time_response: str

    """
    return web.Response(status=200)


async def put_record(request: web.Request, feature_group_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_record

    &lt;p&gt;The &lt;code&gt;PutRecord&lt;/code&gt; API is used to ingest a list of &lt;code&gt;Records&lt;/code&gt; into your feature group. &lt;/p&gt; &lt;p&gt;If a new record’s &lt;code&gt;EventTime&lt;/code&gt; is greater, the new record is written to both the &lt;code&gt;OnlineStore&lt;/code&gt; and &lt;code&gt;OfflineStore&lt;/code&gt;. Otherwise, the record is a historic record and it is written only to the &lt;code&gt;OfflineStore&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;You can specify the ingestion to be applied to the &lt;code&gt;OnlineStore&lt;/code&gt;, &lt;code&gt;OfflineStore&lt;/code&gt;, or both by using the &lt;code&gt;TargetStores&lt;/code&gt; request parameter. &lt;/p&gt; &lt;p&gt;You can set the ingested record to expire at a given time to live (TTL) duration after the record’s event time, &lt;code&gt;ExpiresAt&lt;/code&gt; &#x3D; &lt;code&gt;EventTime&lt;/code&gt; + &lt;code&gt;TtlDuration&lt;/code&gt;, by specifying the &lt;code&gt;TtlDuration&lt;/code&gt; parameter. A record level &lt;code&gt;TtlDuration&lt;/code&gt; is set when specifying the &lt;code&gt;TtlDuration&lt;/code&gt; parameter using the &lt;code&gt;PutRecord&lt;/code&gt; API call. If the input &lt;code&gt;TtlDuration&lt;/code&gt; is &lt;code&gt;null&lt;/code&gt; or unspecified, &lt;code&gt;TtlDuration&lt;/code&gt; is set to the default feature group level &lt;code&gt;TtlDuration&lt;/code&gt;. A record level &lt;code&gt;TtlDuration&lt;/code&gt; supersedes the group level &lt;code&gt;TtlDuration&lt;/code&gt;.&lt;/p&gt;

    :param feature_group_name: The name or Amazon Resource Name (ARN) of the feature group that you want to insert the record into.
    :type feature_group_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutRecordRequest.from_dict(body)
    return web.Response(status=200)
