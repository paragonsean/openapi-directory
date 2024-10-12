# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.output_stream_target import OutputStreamTarget
from openapi_server import util


class Output(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aspect_ratio_height: int=None, aspect_ratio_width: int=None, bitrate_audio: int=None, bitrate_video: int=None, created_at: datetime=None, framerate_reduction: str=None, h264_profile: str=None, id: str=None, keyframes: str=None, name: str=None, output_stream_targets: List[OutputStreamTarget]=None, passthrough_audio: bool=None, passthrough_video: bool=None, stream_format: str=None, transcoder_id: str=None, updated_at: datetime=None):
        """Output - a model defined in OpenAPI

        :param aspect_ratio_height: The aspect_ratio_height of this Output.
        :param aspect_ratio_width: The aspect_ratio_width of this Output.
        :param bitrate_audio: The bitrate_audio of this Output.
        :param bitrate_video: The bitrate_video of this Output.
        :param created_at: The created_at of this Output.
        :param framerate_reduction: The framerate_reduction of this Output.
        :param h264_profile: The h264_profile of this Output.
        :param id: The id of this Output.
        :param keyframes: The keyframes of this Output.
        :param name: The name of this Output.
        :param output_stream_targets: The output_stream_targets of this Output.
        :param passthrough_audio: The passthrough_audio of this Output.
        :param passthrough_video: The passthrough_video of this Output.
        :param stream_format: The stream_format of this Output.
        :param transcoder_id: The transcoder_id of this Output.
        :param updated_at: The updated_at of this Output.
        """
        self.openapi_types = {
            'aspect_ratio_height': int,
            'aspect_ratio_width': int,
            'bitrate_audio': int,
            'bitrate_video': int,
            'created_at': datetime,
            'framerate_reduction': str,
            'h264_profile': str,
            'id': str,
            'keyframes': str,
            'name': str,
            'output_stream_targets': List[OutputStreamTarget],
            'passthrough_audio': bool,
            'passthrough_video': bool,
            'stream_format': str,
            'transcoder_id': str,
            'updated_at': datetime
        }

        self.attribute_map = {
            'aspect_ratio_height': 'aspect_ratio_height',
            'aspect_ratio_width': 'aspect_ratio_width',
            'bitrate_audio': 'bitrate_audio',
            'bitrate_video': 'bitrate_video',
            'created_at': 'created_at',
            'framerate_reduction': 'framerate_reduction',
            'h264_profile': 'h264_profile',
            'id': 'id',
            'keyframes': 'keyframes',
            'name': 'name',
            'output_stream_targets': 'output_stream_targets',
            'passthrough_audio': 'passthrough_audio',
            'passthrough_video': 'passthrough_video',
            'stream_format': 'stream_format',
            'transcoder_id': 'transcoder_id',
            'updated_at': 'updated_at'
        }

        self._aspect_ratio_height = aspect_ratio_height
        self._aspect_ratio_width = aspect_ratio_width
        self._bitrate_audio = bitrate_audio
        self._bitrate_video = bitrate_video
        self._created_at = created_at
        self._framerate_reduction = framerate_reduction
        self._h264_profile = h264_profile
        self._id = id
        self._keyframes = keyframes
        self._name = name
        self._output_stream_targets = output_stream_targets
        self._passthrough_audio = passthrough_audio
        self._passthrough_video = passthrough_video
        self._stream_format = stream_format
        self._transcoder_id = transcoder_id
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Output':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The output of this Output.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aspect_ratio_height(self):
        """Gets the aspect_ratio_height of this Output.

        The height, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is <strong>1080</strong>.

        :return: The aspect_ratio_height of this Output.
        :rtype: int
        """
        return self._aspect_ratio_height

    @aspect_ratio_height.setter
    def aspect_ratio_height(self, aspect_ratio_height):
        """Sets the aspect_ratio_height of this Output.

        The height, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is <strong>1080</strong>.

        :param aspect_ratio_height: The aspect_ratio_height of this Output.
        :type aspect_ratio_height: int
        """

        self._aspect_ratio_height = aspect_ratio_height

    @property
    def aspect_ratio_width(self):
        """Gets the aspect_ratio_width of this Output.

        The width, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is <strong>1980</strong>.

        :return: The aspect_ratio_width of this Output.
        :rtype: int
        """
        return self._aspect_ratio_width

    @aspect_ratio_width.setter
    def aspect_ratio_width(self, aspect_ratio_width):
        """Sets the aspect_ratio_width of this Output.

        The width, in pixels, of the output rendition. Should correspond to a widescreen or standard aspect ratio and be divisible by 8. The default is <strong>1980</strong>.

        :param aspect_ratio_width: The aspect_ratio_width of this Output.
        :type aspect_ratio_width: int
        """

        self._aspect_ratio_width = aspect_ratio_width

    @property
    def bitrate_audio(self):
        """Gets the bitrate_audio of this Output.

        The audio bitrate, in kilobits per second (Kbps). Must be between <strong>0</strong> (for passthrough audio) and <strong>1000</strong>. The default is <strong>128</strong>.

        :return: The bitrate_audio of this Output.
        :rtype: int
        """
        return self._bitrate_audio

    @bitrate_audio.setter
    def bitrate_audio(self, bitrate_audio):
        """Sets the bitrate_audio of this Output.

        The audio bitrate, in kilobits per second (Kbps). Must be between <strong>0</strong> (for passthrough audio) and <strong>1000</strong>. The default is <strong>128</strong>.

        :param bitrate_audio: The bitrate_audio of this Output.
        :type bitrate_audio: int
        """

        self._bitrate_audio = bitrate_audio

    @property
    def bitrate_video(self):
        """Gets the bitrate_video of this Output.

        The video bitrate, in kilobits per second (Kbps). Must be between <strong>0</strong> (for passthrough video) and <strong>10240</strong>. The default is <strong>4000</strong>.

        :return: The bitrate_video of this Output.
        :rtype: int
        """
        return self._bitrate_video

    @bitrate_video.setter
    def bitrate_video(self, bitrate_video):
        """Sets the bitrate_video of this Output.

        The video bitrate, in kilobits per second (Kbps). Must be between <strong>0</strong> (for passthrough video) and <strong>10240</strong>. The default is <strong>4000</strong>.

        :param bitrate_video: The bitrate_video of this Output.
        :type bitrate_video: int
        """

        self._bitrate_video = bitrate_video

    @property
    def created_at(self):
        """Gets the created_at of this Output.

        The date and time that the output rendition was created.

        :return: The created_at of this Output.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Output.

        The date and time that the output rendition was created.

        :param created_at: The created_at of this Output.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def framerate_reduction(self):
        """Gets the framerate_reduction of this Output.

        Reduce the frame rate of the transcoded output rendition. The default, <strong>0</strong>, uses the encoded stream's frame rate without reduction.

        :return: The framerate_reduction of this Output.
        :rtype: str
        """
        return self._framerate_reduction

    @framerate_reduction.setter
    def framerate_reduction(self, framerate_reduction):
        """Sets the framerate_reduction of this Output.

        Reduce the frame rate of the transcoded output rendition. The default, <strong>0</strong>, uses the encoded stream's frame rate without reduction.

        :param framerate_reduction: The framerate_reduction of this Output.
        :type framerate_reduction: str
        """
        allowed_values = ["0", "1/2", "1/4", "1/25", "1/30", "1/50", "1/60"]  # noqa: E501
        if framerate_reduction not in allowed_values:
            raise ValueError(
                "Invalid value for `framerate_reduction` ({0}), must be one of {1}"
                .format(framerate_reduction, allowed_values)
            )

        self._framerate_reduction = framerate_reduction

    @property
    def h264_profile(self):
        """Gets the h264_profile of this Output.

        The encoding method. Specify <strong>main</strong> for desktop streaming, <strong>baseline</strong> for playback on mobile devices, or <strong>high</strong> for HD playback. The default is <strong>high</strong>.

        :return: The h264_profile of this Output.
        :rtype: str
        """
        return self._h264_profile

    @h264_profile.setter
    def h264_profile(self, h264_profile):
        """Sets the h264_profile of this Output.

        The encoding method. Specify <strong>main</strong> for desktop streaming, <strong>baseline</strong> for playback on mobile devices, or <strong>high</strong> for HD playback. The default is <strong>high</strong>.

        :param h264_profile: The h264_profile of this Output.
        :type h264_profile: str
        """
        allowed_values = ["main", "baseline", "high"]  # noqa: E501
        if h264_profile not in allowed_values:
            raise ValueError(
                "Invalid value for `h264_profile` ({0}), must be one of {1}"
                .format(h264_profile, allowed_values)
            )

        self._h264_profile = h264_profile

    @property
    def id(self):
        """Gets the id of this Output.

        The unique alphanumeric string that identifies the output rendition.

        :return: The id of this Output.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Output.

        The unique alphanumeric string that identifies the output rendition.

        :param id: The id of this Output.
        :type id: str
        """

        self._id = id

    @property
    def keyframes(self):
        """Gets the keyframes of this Output.

        The interval used to define the compression applied to a group of frames. The default, <strong>follow_source</strong>, uses the keyframe interval of the source video.

        :return: The keyframes of this Output.
        :rtype: str
        """
        return self._keyframes

    @keyframes.setter
    def keyframes(self, keyframes):
        """Sets the keyframes of this Output.

        The interval used to define the compression applied to a group of frames. The default, <strong>follow_source</strong>, uses the keyframe interval of the source video.

        :param keyframes: The keyframes of this Output.
        :type keyframes: str
        """
        allowed_values = ["follow_source", "25", "30", "50", "60", "100", "120"]  # noqa: E501
        if keyframes not in allowed_values:
            raise ValueError(
                "Invalid value for `keyframes` ({0}), must be one of {1}"
                .format(keyframes, allowed_values)
            )

        self._keyframes = keyframes

    @property
    def name(self):
        """Gets the name of this Output.

        A descriptive name for the output (generated, not writable).

        :return: The name of this Output.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Output.

        A descriptive name for the output (generated, not writable).

        :param name: The name of this Output.
        :type name: str
        """

        self._name = name

    @property
    def output_stream_targets(self):
        """Gets the output_stream_targets of this Output.


        :return: The output_stream_targets of this Output.
        :rtype: List[OutputStreamTarget]
        """
        return self._output_stream_targets

    @output_stream_targets.setter
    def output_stream_targets(self, output_stream_targets):
        """Sets the output_stream_targets of this Output.


        :param output_stream_targets: The output_stream_targets of this Output.
        :type output_stream_targets: List[OutputStreamTarget]
        """

        self._output_stream_targets = output_stream_targets

    @property
    def passthrough_audio(self):
        """Gets the passthrough_audio of this Output.

        If <strong>true</strong>, sends the audio track to the target without transcoding. The default is <strong>false</strong>.

        :return: The passthrough_audio of this Output.
        :rtype: bool
        """
        return self._passthrough_audio

    @passthrough_audio.setter
    def passthrough_audio(self, passthrough_audio):
        """Sets the passthrough_audio of this Output.

        If <strong>true</strong>, sends the audio track to the target without transcoding. The default is <strong>false</strong>.

        :param passthrough_audio: The passthrough_audio of this Output.
        :type passthrough_audio: bool
        """

        self._passthrough_audio = passthrough_audio

    @property
    def passthrough_video(self):
        """Gets the passthrough_video of this Output.

        If <strong>true</strong>, sends the video track to the target without transcoding. The default is <strong>false</strong>.

        :return: The passthrough_video of this Output.
        :rtype: bool
        """
        return self._passthrough_video

    @passthrough_video.setter
    def passthrough_video(self, passthrough_video):
        """Sets the passthrough_video of this Output.

        If <strong>true</strong>, sends the video track to the target without transcoding. The default is <strong>false</strong>.

        :param passthrough_video: The passthrough_video of this Output.
        :type passthrough_video: bool
        """

        self._passthrough_video = passthrough_video

    @property
    def stream_format(self):
        """Gets the stream_format of this Output.

        The contents of the stream. The default is both audio and video (<strong>audiovideo</strong>).

        :return: The stream_format of this Output.
        :rtype: str
        """
        return self._stream_format

    @stream_format.setter
    def stream_format(self, stream_format):
        """Sets the stream_format of this Output.

        The contents of the stream. The default is both audio and video (<strong>audiovideo</strong>).

        :param stream_format: The stream_format of this Output.
        :type stream_format: str
        """
        allowed_values = ["audiovideo", "videoonly", "audioonly"]  # noqa: E501
        if stream_format not in allowed_values:
            raise ValueError(
                "Invalid value for `stream_format` ({0}), must be one of {1}"
                .format(stream_format, allowed_values)
            )

        self._stream_format = stream_format

    @property
    def transcoder_id(self):
        """Gets the transcoder_id of this Output.

        The unique alphanumeric string that identifies the transcoder.

        :return: The transcoder_id of this Output.
        :rtype: str
        """
        return self._transcoder_id

    @transcoder_id.setter
    def transcoder_id(self, transcoder_id):
        """Sets the transcoder_id of this Output.

        The unique alphanumeric string that identifies the transcoder.

        :param transcoder_id: The transcoder_id of this Output.
        :type transcoder_id: str
        """

        self._transcoder_id = transcoder_id

    @property
    def updated_at(self):
        """Gets the updated_at of this Output.

        The date and time that the output rendition was updated.

        :return: The updated_at of this Output.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Output.

        The date and time that the output rendition was updated.

        :param updated_at: The updated_at of this Output.
        :type updated_at: datetime
        """

        self._updated_at = updated_at
