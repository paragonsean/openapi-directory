QT += network

HEADERS += \
# Models
    $${PWD}/OAIAudio.h \
    $${PWD}/OAIAudioElement.h \
    $${PWD}/OAIBaseElement.h \
    $${PWD}/OAICaptureProperty.h \
    $${PWD}/OAICaptureProperty_capture.h \
    $${PWD}/OAIComponent.h \
    $${PWD}/OAIHtml.h \
    $${PWD}/OAIImage.h \
    $${PWD}/OAIMovie.h \
    $${PWD}/OAIMovie_elements_inner.h \
    $${PWD}/OAIScene.h \
    $${PWD}/OAIScene_elements_inner.h \
    $${PWD}/OAIScene_transition.h \
    $${PWD}/OAITemplate.h \
    $${PWD}/OAIText.h \
    $${PWD}/OAIVideo.h \
    $${PWD}/OAIVisualElement.h \
    $${PWD}/OAIVisualElement_chroma_key.h \
    $${PWD}/OAIVisualElement_crop.h \
    $${PWD}/OAIVisualElement_rotate.h \
    $${PWD}/OAIVisualElement_scale.h \
    $${PWD}/OAIVoice.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAudio.cpp \
    $${PWD}/OAIAudioElement.cpp \
    $${PWD}/OAIBaseElement.cpp \
    $${PWD}/OAICaptureProperty.cpp \
    $${PWD}/OAICaptureProperty_capture.cpp \
    $${PWD}/OAIComponent.cpp \
    $${PWD}/OAIHtml.cpp \
    $${PWD}/OAIImage.cpp \
    $${PWD}/OAIMovie.cpp \
    $${PWD}/OAIMovie_elements_inner.cpp \
    $${PWD}/OAIScene.cpp \
    $${PWD}/OAIScene_elements_inner.cpp \
    $${PWD}/OAIScene_transition.cpp \
    $${PWD}/OAITemplate.cpp \
    $${PWD}/OAIText.cpp \
    $${PWD}/OAIVideo.cpp \
    $${PWD}/OAIVisualElement.cpp \
    $${PWD}/OAIVisualElement_chroma_key.cpp \
    $${PWD}/OAIVisualElement_crop.cpp \
    $${PWD}/OAIVisualElement_rotate.cpp \
    $${PWD}/OAIVisualElement_scale.cpp \
    $${PWD}/OAIVoice.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
