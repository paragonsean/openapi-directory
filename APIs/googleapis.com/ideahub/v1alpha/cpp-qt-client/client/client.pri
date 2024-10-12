QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleSearchIdeahubV1alphaAvailableLocale.h \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaIdea.h \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaIdeaActivity.h \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaIdeaState.h \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaListAvailableLocalesResponse.h \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaListIdeasResponse.h \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaTopic.h \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaTopicState.h \
# APIs
    $${PWD}/OAIIdeasApi.h \
    $${PWD}/OAIPlatformsApi.h \
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
    $${PWD}/OAIGoogleSearchIdeahubV1alphaAvailableLocale.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaIdea.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaIdeaActivity.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaIdeaState.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaListAvailableLocalesResponse.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaListIdeasResponse.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaTopic.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1alphaTopicState.cpp \
# APIs
    $${PWD}/OAIIdeasApi.cpp \
    $${PWD}/OAIPlatformsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
