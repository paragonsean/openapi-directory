QT += network

HEADERS += \
# Models
    $${PWD}/OAIBoundingBox.h \
    $${PWD}/OAIImagePrediction.h \
    $${PWD}/OAIImageUrl.h \
    $${PWD}/OAIPrediction.h \
# APIs
    $${PWD}/OAIImagePredictionApiApi.h \
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
    $${PWD}/OAIBoundingBox.cpp \
    $${PWD}/OAIImagePrediction.cpp \
    $${PWD}/OAIImageUrl.cpp \
    $${PWD}/OAIPrediction.cpp \
# APIs
    $${PWD}/OAIImagePredictionApiApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
