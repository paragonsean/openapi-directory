QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIError.h \
    $${PWD}/OAICompositeChildModel.h \
    $${PWD}/OAICompositeEntityModel.h \
    $${PWD}/OAIEntityModel.h \
    $${PWD}/OAIEntityWithResolution.h \
    $${PWD}/OAIEntityWithScore.h \
    $${PWD}/OAIIntentModel.h \
    $${PWD}/OAILuisResult.h \
    $${PWD}/OAISentiment.h \
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
    $${PWD}/OAIAPIError.cpp \
    $${PWD}/OAICompositeChildModel.cpp \
    $${PWD}/OAICompositeEntityModel.cpp \
    $${PWD}/OAIEntityModel.cpp \
    $${PWD}/OAIEntityWithResolution.cpp \
    $${PWD}/OAIEntityWithScore.cpp \
    $${PWD}/OAIIntentModel.cpp \
    $${PWD}/OAILuisResult.cpp \
    $${PWD}/OAISentiment.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
