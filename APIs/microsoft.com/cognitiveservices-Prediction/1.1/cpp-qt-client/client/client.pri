QT += network

HEADERS += \
# Models
    $${PWD}/OAIImagePredictionResultModel.h \
    $${PWD}/OAIImageTagPredictionModel.h \
    $${PWD}/OAIImageUrl.h \
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
    $${PWD}/OAIImagePredictionResultModel.cpp \
    $${PWD}/OAIImageTagPredictionModel.cpp \
    $${PWD}/OAIImageUrl.cpp \
# APIs
    $${PWD}/OAIImagePredictionApiApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
