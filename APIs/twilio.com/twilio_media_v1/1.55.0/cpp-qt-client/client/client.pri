QT += network

HEADERS += \
# Models
    $${PWD}/OAIListMediaProcessorResponse.h \
    $${PWD}/OAIListMediaProcessorResponse_meta.h \
    $${PWD}/OAIListMediaRecordingResponse.h \
    $${PWD}/OAIListPlayerStreamerResponse.h \
    $${PWD}/OAIMedia_processor_enum_order.h \
    $${PWD}/OAIMedia_processor_enum_status.h \
    $${PWD}/OAIMedia_processor_enum_update_status.h \
    $${PWD}/OAIMedia_recording_enum_format.h \
    $${PWD}/OAIMedia_recording_enum_order.h \
    $${PWD}/OAIMedia_recording_enum_status.h \
    $${PWD}/OAIMedia_v1_media_processor.h \
    $${PWD}/OAIMedia_v1_media_recording.h \
    $${PWD}/OAIMedia_v1_player_streamer.h \
    $${PWD}/OAIMedia_v1_player_streamer_player_streamer_playback_grant.h \
    $${PWD}/OAIPlayer_streamer_enum_ended_reason.h \
    $${PWD}/OAIPlayer_streamer_enum_order.h \
    $${PWD}/OAIPlayer_streamer_enum_status.h \
    $${PWD}/OAIPlayer_streamer_enum_update_status.h \
# APIs
    $${PWD}/OAIMediaV1MediaProcessorApi.h \
    $${PWD}/OAIMediaV1MediaRecordingApi.h \
    $${PWD}/OAIMediaV1PlaybackGrantApi.h \
    $${PWD}/OAIMediaV1PlayerStreamerApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIListMediaProcessorResponse.cpp \
    $${PWD}/OAIListMediaProcessorResponse_meta.cpp \
    $${PWD}/OAIListMediaRecordingResponse.cpp \
    $${PWD}/OAIListPlayerStreamerResponse.cpp \
    $${PWD}/OAIMedia_processor_enum_order.cpp \
    $${PWD}/OAIMedia_processor_enum_status.cpp \
    $${PWD}/OAIMedia_processor_enum_update_status.cpp \
    $${PWD}/OAIMedia_recording_enum_format.cpp \
    $${PWD}/OAIMedia_recording_enum_order.cpp \
    $${PWD}/OAIMedia_recording_enum_status.cpp \
    $${PWD}/OAIMedia_v1_media_processor.cpp \
    $${PWD}/OAIMedia_v1_media_recording.cpp \
    $${PWD}/OAIMedia_v1_player_streamer.cpp \
    $${PWD}/OAIMedia_v1_player_streamer_player_streamer_playback_grant.cpp \
    $${PWD}/OAIPlayer_streamer_enum_ended_reason.cpp \
    $${PWD}/OAIPlayer_streamer_enum_order.cpp \
    $${PWD}/OAIPlayer_streamer_enum_status.cpp \
    $${PWD}/OAIPlayer_streamer_enum_update_status.cpp \
# APIs
    $${PWD}/OAIMediaV1MediaProcessorApi.cpp \
    $${PWD}/OAIMediaV1MediaRecordingApi.cpp \
    $${PWD}/OAIMediaV1PlaybackGrantApi.cpp \
    $${PWD}/OAIMediaV1PlayerStreamerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
