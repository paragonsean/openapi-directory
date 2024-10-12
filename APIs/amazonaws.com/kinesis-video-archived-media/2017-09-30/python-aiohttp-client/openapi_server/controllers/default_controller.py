from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_clip_output import GetClipOutput
from openapi_server.models.get_clip_request import GetClipRequest
from openapi_server.models.get_dash_streaming_session_url_output import GetDASHStreamingSessionURLOutput
from openapi_server.models.get_dash_streaming_session_url_request import GetDASHStreamingSessionURLRequest
from openapi_server.models.get_hls_streaming_session_url_output import GetHLSStreamingSessionURLOutput
from openapi_server.models.get_hls_streaming_session_url_request import GetHLSStreamingSessionURLRequest
from openapi_server.models.get_images_output import GetImagesOutput
from openapi_server.models.get_images_request import GetImagesRequest
from openapi_server.models.get_media_for_fragment_list_output import GetMediaForFragmentListOutput
from openapi_server.models.get_media_for_fragment_list_request import GetMediaForFragmentListRequest
from openapi_server.models.list_fragments_output import ListFragmentsOutput
from openapi_server.models.list_fragments_request import ListFragmentsRequest
from openapi_server import util


async def get_clip(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_clip

    &lt;p&gt;Downloads an MP4 file (clip) containing the archived, on-demand media from the specified video stream over the specified time range. &lt;/p&gt; &lt;p&gt;Both the StreamName and the StreamARN parameters are optional, but you must specify either the StreamName or the StreamARN when invoking this API operation. &lt;/p&gt; &lt;p&gt;As a prerequisite to using GetCLip API, you must obtain an endpoint using &lt;code&gt;GetDataEndpoint&lt;/code&gt;, specifying GET_CLIP for&lt;code/&gt; the &lt;code&gt;APIName&lt;/code&gt; parameter. &lt;/p&gt; &lt;p&gt;An Amazon Kinesis video stream has the following requirements for providing data through MP4:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The media must contain h.264 or h.265 encoded video and, optionally, AAC or G.711 encoded audio. Specifically, the codec ID of track 1 should be &lt;code&gt;V_MPEG/ISO/AVC&lt;/code&gt; (for h.264) or V_MPEGH/ISO/HEVC (for H.265). Optionally, the codec ID of track 2 should be &lt;code&gt;A_AAC&lt;/code&gt; (for AAC) or A_MS/ACM (for G.711).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data retention must be greater than 0.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format and HEVC for H.265 format. For more information, see &lt;a href&#x3D;\&quot;https://www.iso.org/standard/55980.html\&quot;&gt;MPEG-4 specification ISO/IEC 14496-15&lt;/a&gt;. For information about adapting stream data to a given format, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html\&quot;&gt;NAL Adaptation Flags&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The audio track (if present) of each fragment must contain codec private data in the AAC format (&lt;a href&#x3D;\&quot;https://www.iso.org/standard/43345.html\&quot;&gt;AAC specification ISO/IEC 13818-7&lt;/a&gt;) or the &lt;a href&#x3D;\&quot;http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html\&quot;&gt;MS Wave format&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can monitor the amount of outgoing data by monitoring the &lt;code&gt;GetClip.OutgoingBytes&lt;/code&gt; Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html\&quot;&gt;Monitoring Kinesis Video Streams&lt;/a&gt;. For pricing information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/kinesis/video-streams/pricing/\&quot;&gt;Amazon Kinesis Video Streams Pricing&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://aws.amazon.com/pricing/\&quot;&gt; Amazon Web Services Pricing&lt;/a&gt;. Charges for outgoing Amazon Web Services data apply.&lt;/p&gt;

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
    body = GetClipRequest.from_dict(body)
    return web.Response(status=200)


async def get_dash_streaming_session_url(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dash_streaming_session_url

    &lt;p&gt;Retrieves an MPEG Dynamic Adaptive Streaming over HTTP (DASH) URL for the stream. You can then open the URL in a media player to view the stream contents.&lt;/p&gt; &lt;p&gt;Both the &lt;code&gt;StreamName&lt;/code&gt; and the &lt;code&gt;StreamARN&lt;/code&gt; parameters are optional, but you must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt; when invoking this API operation.&lt;/p&gt; &lt;p&gt;An Amazon Kinesis video stream has the following requirements for providing data through MPEG-DASH:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The media must contain h.264 or h.265 encoded video and, optionally, AAC or G.711 encoded audio. Specifically, the codec ID of track 1 should be &lt;code&gt;V_MPEG/ISO/AVC&lt;/code&gt; (for h.264) or V_MPEGH/ISO/HEVC (for H.265). Optionally, the codec ID of track 2 should be &lt;code&gt;A_AAC&lt;/code&gt; (for AAC) or A_MS/ACM (for G.711).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data retention must be greater than 0.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format and HEVC for H.265 format. For more information, see &lt;a href&#x3D;\&quot;https://www.iso.org/standard/55980.html\&quot;&gt;MPEG-4 specification ISO/IEC 14496-15&lt;/a&gt;. For information about adapting stream data to a given format, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html\&quot;&gt;NAL Adaptation Flags&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The audio track (if present) of each fragment must contain codec private data in the AAC format (&lt;a href&#x3D;\&quot;https://www.iso.org/standard/43345.html\&quot;&gt;AAC specification ISO/IEC 13818-7&lt;/a&gt;) or the &lt;a href&#x3D;\&quot;http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html\&quot;&gt;MS Wave format&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following procedure shows how to use MPEG-DASH with Kinesis Video Streams:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Get an endpoint using &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html\&quot;&gt;GetDataEndpoint&lt;/a&gt;, specifying &lt;code&gt;GET_DASH_STREAMING_SESSION_URL&lt;/code&gt; for the &lt;code&gt;APIName&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Retrieve the MPEG-DASH URL using &lt;code&gt;GetDASHStreamingSessionURL&lt;/code&gt;. Kinesis Video Streams creates an MPEG-DASH streaming session to be used for accessing content in a stream using the MPEG-DASH protocol. &lt;code&gt;GetDASHStreamingSessionURL&lt;/code&gt; returns an authenticated URL (that includes an encrypted session token) for the session&#39;s MPEG-DASH &lt;i&gt;manifest&lt;/i&gt; (the root resource needed for streaming with MPEG-DASH).&lt;/p&gt; &lt;note&gt; &lt;p&gt;Don&#39;t share or store this token where an unauthorized entity can access it. The token provides access to the content of the stream. Safeguard the token with the same measures that you use with your Amazon Web Services credentials.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The media that is made available through the manifest consists only of the requested stream, time range, and format. No other media data (such as frames outside the requested window or alternate bitrates) is made available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Provide the URL (containing the encrypted session token) for the MPEG-DASH manifest to a media player that supports the MPEG-DASH protocol. Kinesis Video Streams makes the initialization fragment and media fragments available through the manifest URL. The initialization fragment contains the codec private data for the stream, and other data needed to set up the video or audio decoder and renderer. The media fragments contain encoded video frames or encoded audio samples.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The media player receives the authenticated URL and requests stream metadata and media data normally. When the media player requests data, it calls the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetDASHManifest:&lt;/b&gt; Retrieves an MPEG DASH manifest, which contains the metadata for the media that you want to playback.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetMP4InitFragment:&lt;/b&gt; Retrieves the MP4 initialization fragment. The media player typically loads the initialization fragment before loading any media fragments. This fragment contains the \&quot;&lt;code&gt;fytp&lt;/code&gt;\&quot; and \&quot;&lt;code&gt;moov&lt;/code&gt;\&quot; MP4 atoms, and the child atoms that are needed to initialize the media player decoder.&lt;/p&gt; &lt;p&gt;The initialization fragment does not correspond to a fragment in a Kinesis video stream. It contains only the codec private data for the stream and respective track, which the media player needs to decode the media frames.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetMP4MediaFragment:&lt;/b&gt; Retrieves MP4 media fragments. These fragments contain the \&quot;&lt;code&gt;moof&lt;/code&gt;\&quot; and \&quot;&lt;code&gt;mdat&lt;/code&gt;\&quot; MP4 atoms and their child atoms, containing the encoded fragment&#39;s media frames and their timestamps. &lt;/p&gt; &lt;note&gt; &lt;p&gt;After the first media fragment is made available in a streaming session, any fragments that don&#39;t contain the same codec private data cause an error to be returned when those different media fragments are loaded. Therefore, the codec private data should not change between fragments in a session. This also means that the session fails if the fragments in a stream change from having only video to having both audio and video.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Data retrieved with this action is billable. See &lt;a href&#x3D;\&quot;https://aws.amazon.com/kinesis/video-streams/pricing/\&quot;&gt;Pricing&lt;/a&gt; for details.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ol&gt; &lt;note&gt; &lt;p&gt;For restrictions that apply to MPEG-DASH sessions, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html\&quot;&gt;Kinesis Video Streams Limits&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can monitor the amount of data that the media player consumes by monitoring the &lt;code&gt;GetMP4MediaFragment.OutgoingBytes&lt;/code&gt; Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html\&quot;&gt;Monitoring Kinesis Video Streams&lt;/a&gt;. For pricing information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/kinesis/video-streams/pricing/\&quot;&gt;Amazon Kinesis Video Streams Pricing&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://aws.amazon.com/pricing/\&quot;&gt;Amazon Web Services Pricing&lt;/a&gt;. Charges for both HLS sessions and outgoing Amazon Web Services data apply.&lt;/p&gt; &lt;p&gt;For more information about HLS, see &lt;a href&#x3D;\&quot;https://developer.apple.com/streaming/\&quot;&gt;HTTP Live Streaming&lt;/a&gt; on the &lt;a href&#x3D;\&quot;https://developer.apple.com\&quot;&gt;Apple Developer site&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-ErrorType&lt;/code&gt; HTTP header – contains a more specific error type in addition to what the HTTP status code provides. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-RequestId&lt;/code&gt; HTTP header – if you want to report an issue to Amazon Web Services the support team can better diagnose the problem if given the Request Id.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;b&gt;Errors&lt;/b&gt; section at the bottom of this topic, as well as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html\&quot;&gt;Common Errors&lt;/a&gt;. &lt;/p&gt; &lt;/important&gt;

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
    body = GetDASHStreamingSessionURLRequest.from_dict(body)
    return web.Response(status=200)


async def get_hls_streaming_session_url(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_hls_streaming_session_url

    &lt;p&gt;Retrieves an HTTP Live Streaming (HLS) URL for the stream. You can then open the URL in a browser or media player to view the stream contents.&lt;/p&gt; &lt;p&gt;Both the &lt;code&gt;StreamName&lt;/code&gt; and the &lt;code&gt;StreamARN&lt;/code&gt; parameters are optional, but you must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt; when invoking this API operation.&lt;/p&gt; &lt;p&gt;An Amazon Kinesis video stream has the following requirements for providing data through HLS:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For streaming video, the media must contain H.264 or H.265 encoded video and, optionally, AAC encoded audio. Specifically, the codec ID of track 1 should be &lt;code&gt;V_MPEG/ISO/AVC&lt;/code&gt; (for H.264) or &lt;code&gt;V_MPEG/ISO/HEVC&lt;/code&gt; (for H.265). Optionally, the codec ID of track 2 should be &lt;code&gt;A_AAC&lt;/code&gt;. For audio only streaming, the codec ID of track 1 should be &lt;code&gt;A_AAC&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data retention must be greater than 0.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The video track of each fragment must contain codec private data in the Advanced Video Coding (AVC) for H.264 format or HEVC for H.265 format (&lt;a href&#x3D;\&quot;https://www.iso.org/standard/55980.html\&quot;&gt;MPEG-4 specification ISO/IEC 14496-15&lt;/a&gt;). For information about adapting stream data to a given format, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html\&quot;&gt;NAL Adaptation Flags&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The audio track (if present) of each fragment must contain codec private data in the AAC format (&lt;a href&#x3D;\&quot;https://www.iso.org/standard/43345.html\&quot;&gt;AAC specification ISO/IEC 13818-7&lt;/a&gt;).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Kinesis Video Streams HLS sessions contain fragments in the fragmented MPEG-4 form (also called fMP4 or CMAF) or the MPEG-2 form (also called TS chunks, which the HLS specification also supports). For more information about HLS fragment types, see the &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/draft-pantos-http-live-streaming-23\&quot;&gt;HLS specification&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following procedure shows how to use HLS with Kinesis Video Streams:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Get an endpoint using &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html\&quot;&gt;GetDataEndpoint&lt;/a&gt;, specifying &lt;code&gt;GET_HLS_STREAMING_SESSION_URL&lt;/code&gt; for the &lt;code&gt;APIName&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Retrieve the HLS URL using &lt;code&gt;GetHLSStreamingSessionURL&lt;/code&gt;. Kinesis Video Streams creates an HLS streaming session to be used for accessing content in a stream using the HLS protocol. &lt;code&gt;GetHLSStreamingSessionURL&lt;/code&gt; returns an authenticated URL (that includes an encrypted session token) for the session&#39;s HLS &lt;i&gt;master playlist&lt;/i&gt; (the root resource needed for streaming with HLS).&lt;/p&gt; &lt;note&gt; &lt;p&gt;Don&#39;t share or store this token where an unauthorized entity could access it. The token provides access to the content of the stream. Safeguard the token with the same measures that you would use with your Amazon Web Services credentials.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The media that is made available through the playlist consists only of the requested stream, time range, and format. No other media data (such as frames outside the requested window or alternate bitrates) is made available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Provide the URL (containing the encrypted session token) for the HLS master playlist to a media player that supports the HLS protocol. Kinesis Video Streams makes the HLS media playlist, initialization fragment, and media fragments available through the master playlist URL. The initialization fragment contains the codec private data for the stream, and other data needed to set up the video or audio decoder and renderer. The media fragments contain H.264-encoded video frames or AAC-encoded audio samples.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The media player receives the authenticated URL and requests stream metadata and media data normally. When the media player requests data, it calls the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetHLSMasterPlaylist:&lt;/b&gt; Retrieves an HLS master playlist, which contains a URL for the &lt;code&gt;GetHLSMediaPlaylist&lt;/code&gt; action for each track, and additional metadata for the media player, including estimated bitrate and resolution.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetHLSMediaPlaylist:&lt;/b&gt; Retrieves an HLS media playlist, which contains a URL to access the MP4 initialization fragment with the &lt;code&gt;GetMP4InitFragment&lt;/code&gt; action, and URLs to access the MP4 media fragments with the &lt;code&gt;GetMP4MediaFragment&lt;/code&gt; actions. The HLS media playlist also contains metadata about the stream that the player needs to play it, such as whether the &lt;code&gt;PlaybackMode&lt;/code&gt; is &lt;code&gt;LIVE&lt;/code&gt; or &lt;code&gt;ON_DEMAND&lt;/code&gt;. The HLS media playlist is typically static for sessions with a &lt;code&gt;PlaybackType&lt;/code&gt; of &lt;code&gt;ON_DEMAND&lt;/code&gt;. The HLS media playlist is continually updated with new fragments for sessions with a &lt;code&gt;PlaybackType&lt;/code&gt; of &lt;code&gt;LIVE&lt;/code&gt;. There is a distinct HLS media playlist for the video track and the audio track (if applicable) that contains MP4 media URLs for the specific track. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetMP4InitFragment:&lt;/b&gt; Retrieves the MP4 initialization fragment. The media player typically loads the initialization fragment before loading any media fragments. This fragment contains the \&quot;&lt;code&gt;fytp&lt;/code&gt;\&quot; and \&quot;&lt;code&gt;moov&lt;/code&gt;\&quot; MP4 atoms, and the child atoms that are needed to initialize the media player decoder.&lt;/p&gt; &lt;p&gt;The initialization fragment does not correspond to a fragment in a Kinesis video stream. It contains only the codec private data for the stream and respective track, which the media player needs to decode the media frames.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetMP4MediaFragment:&lt;/b&gt; Retrieves MP4 media fragments. These fragments contain the \&quot;&lt;code&gt;moof&lt;/code&gt;\&quot; and \&quot;&lt;code&gt;mdat&lt;/code&gt;\&quot; MP4 atoms and their child atoms, containing the encoded fragment&#39;s media frames and their timestamps. &lt;/p&gt; &lt;note&gt; &lt;p&gt;For the HLS streaming session, in-track codec private data (CPD) changes are supported. After the first media fragment is made available in a streaming session, fragments can contain CPD changes for each track. Therefore, the fragments in a session can have a different resolution, bit rate, or other information in the CPD without interrupting playback. However, any change made in the track number or track codec format can return an error when those different media fragments are loaded. For example, streaming will fail if the fragments in the stream change from having only video to having both audio and video, or if an AAC audio track is changed to an ALAW audio track. For each streaming session, only 500 CPD changes are allowed.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Data retrieved with this action is billable. For information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/kinesis/video-streams/pricing/\&quot;&gt;Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;GetTSFragment:&lt;/b&gt; Retrieves MPEG TS fragments containing both initialization and media data for all tracks in the stream.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the &lt;code&gt;ContainerFormat&lt;/code&gt; is &lt;code&gt;MPEG_TS&lt;/code&gt;, this API is used instead of &lt;code&gt;GetMP4InitFragment&lt;/code&gt; and &lt;code&gt;GetMP4MediaFragment&lt;/code&gt; to retrieve stream media.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Data retrieved with this action is billable. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/kinesis/video-streams/pricing/\&quot;&gt;Kinesis Video Streams pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;A streaming session URL must not be shared between players. The service might throttle a session if multiple media players are sharing it. For connection limits, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html\&quot;&gt;Kinesis Video Streams Limits&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can monitor the amount of data that the media player consumes by monitoring the &lt;code&gt;GetMP4MediaFragment.OutgoingBytes&lt;/code&gt; Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html\&quot;&gt;Monitoring Kinesis Video Streams&lt;/a&gt;. For pricing information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/kinesis/video-streams/pricing/\&quot;&gt;Amazon Kinesis Video Streams Pricing&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://aws.amazon.com/pricing/\&quot;&gt;Amazon Web Services Pricing&lt;/a&gt;. Charges for both HLS sessions and outgoing Amazon Web Services data apply.&lt;/p&gt; &lt;p&gt;For more information about HLS, see &lt;a href&#x3D;\&quot;https://developer.apple.com/streaming/\&quot;&gt;HTTP Live Streaming&lt;/a&gt; on the &lt;a href&#x3D;\&quot;https://developer.apple.com\&quot;&gt;Apple Developer site&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-ErrorType&lt;/code&gt; HTTP header – contains a more specific error type in addition to what the HTTP status code provides. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-RequestId&lt;/code&gt; HTTP header – if you want to report an issue to Amazon Web Services, the support team can better diagnose the problem if given the Request Id.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;b&gt;Errors&lt;/b&gt; section at the bottom of this topic, as well as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html\&quot;&gt;Common Errors&lt;/a&gt;. &lt;/p&gt; &lt;/important&gt;

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
    body = GetHLSStreamingSessionURLRequest.from_dict(body)
    return web.Response(status=200)


async def get_images(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_images

    Retrieves a list of Images corresponding to each timestamp for a given time range, sampling interval, and image format configuration.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetImagesRequest.from_dict(body)
    return web.Response(status=200)


async def get_media_for_fragment_list(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_media_for_fragment_list

    &lt;p&gt;Gets media for a list of fragments (specified by fragment number) from the archived data in an Amazon Kinesis video stream.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You must first call the &lt;code&gt;GetDataEndpoint&lt;/code&gt; API to get an endpoint. Then send the &lt;code&gt;GetMediaForFragmentList&lt;/code&gt; requests to this endpoint using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/\&quot;&gt;--endpoint-url parameter&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;For limits, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html\&quot;&gt;Kinesis Video Streams Limits&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-ErrorType&lt;/code&gt; HTTP header – contains a more specific error type in addition to what the HTTP status code provides. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-RequestId&lt;/code&gt; HTTP header – if you want to report an issue to Amazon Web Services, the support team can better diagnose the problem if given the Request Id.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;b&gt;Errors&lt;/b&gt; section at the bottom of this topic, as well as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html\&quot;&gt;Common Errors&lt;/a&gt;. &lt;/p&gt; &lt;/important&gt;

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
    body = GetMediaForFragmentListRequest.from_dict(body)
    return web.Response(status=200)


async def list_fragments(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_fragments

    &lt;p&gt;Returns a list of &lt;a&gt;Fragment&lt;/a&gt; objects from the specified stream and timestamp range within the archived data.&lt;/p&gt; &lt;p&gt;Listing fragments is eventually consistent. This means that even if the producer receives an acknowledgment that a fragment is persisted, the result might not be returned immediately from a request to &lt;code&gt;ListFragments&lt;/code&gt;. However, results are typically available in less than one second.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You must first call the &lt;code&gt;GetDataEndpoint&lt;/code&gt; API to get an endpoint. Then send the &lt;code&gt;ListFragments&lt;/code&gt; requests to this endpoint using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/\&quot;&gt;--endpoint-url parameter&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;If an error is thrown after invoking a Kinesis Video Streams archived media API, in addition to the HTTP status code and the response body, it includes the following pieces of information: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-ErrorType&lt;/code&gt; HTTP header – contains a more specific error type in addition to what the HTTP status code provides. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;x-amz-RequestId&lt;/code&gt; HTTP header – if you want to report an issue to Amazon Web Services, the support team can better diagnose the problem if given the Request Id.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Both the HTTP status code and the ErrorType header can be utilized to make programmatic decisions about whether errors are retry-able and under what conditions, as well as provide information on what actions the client programmer might need to take in order to successfully try again.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;b&gt;Errors&lt;/b&gt; section at the bottom of this topic, as well as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html\&quot;&gt;Common Errors&lt;/a&gt;. &lt;/p&gt; &lt;/important&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListFragmentsRequest.from_dict(body)
    return web.Response(status=200)
