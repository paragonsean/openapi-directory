QT += network

HEADERS += \
# Models
    $${PWD}/OAIAudioConfig.h \
    $${PWD}/OAICustomVoiceParams.h \
    $${PWD}/OAIGoogleCloudTexttospeechV1beta1SynthesizeLongAudioMetadata.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAIListVoicesResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAISynthesisInput.h \
    $${PWD}/OAISynthesizeLongAudioMetadata.h \
    $${PWD}/OAISynthesizeLongAudioRequest.h \
    $${PWD}/OAISynthesizeSpeechRequest.h \
    $${PWD}/OAISynthesizeSpeechResponse.h \
    $${PWD}/OAITimepoint.h \
    $${PWD}/OAIVoice.h \
    $${PWD}/OAIVoiceSelectionParams.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
    $${PWD}/OAITextApi.h \
    $${PWD}/OAIVoicesApi.h \
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
    $${PWD}/OAIAudioConfig.cpp \
    $${PWD}/OAICustomVoiceParams.cpp \
    $${PWD}/OAIGoogleCloudTexttospeechV1beta1SynthesizeLongAudioMetadata.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAIListVoicesResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAISynthesisInput.cpp \
    $${PWD}/OAISynthesizeLongAudioMetadata.cpp \
    $${PWD}/OAISynthesizeLongAudioRequest.cpp \
    $${PWD}/OAISynthesizeSpeechRequest.cpp \
    $${PWD}/OAISynthesizeSpeechResponse.cpp \
    $${PWD}/OAITimepoint.cpp \
    $${PWD}/OAIVoice.cpp \
    $${PWD}/OAIVoiceSelectionParams.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
    $${PWD}/OAITextApi.cpp \
    $${PWD}/OAIVoicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
